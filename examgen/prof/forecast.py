"""Prévoir le sujet suivant : quels passages du cours tomberont, posés comment, avec quelle intention.

Le moteur ne reçoit que les anciens sujets et le cours (aucune règle propre à une matière) :
  1. lecture des anciens sujets (auto-réglage, auto-entraînement, boucle intentions <-> alignement) ;
  2. pour chaque passage du cours, probabilité de tomber l'année suivante. Variables : les 12
     génériques (place, poids, centralité, historique...) + récence (tombé l'an dernier, années
     depuis) + variables propres à la matière découvertes dans le cours (thèmes, formes) ;
  3. preuve « comme en vrai » : pour chaque année récente, le modèle n'apprend QUE sur les années
     d'avant, prédit, puis on regarde le vrai sujet de l'année (couverture des questions réelles) ;
  4. pour chaque passage prévu : manière de demander la plus probable, type d'intention, et
     intention cachée = ce que l'enseignant évalue sans le dire (mots du passage que ses énoncés
     taisent mais que ses corrigés exigent).
  python -m examgen.prof.forecast droit nsi
"""
from __future__ import annotations

import json
import re
import sys
import warnings
from collections import Counter, defaultdict
from pathlib import Path

import joblib
import numpy as np
from sklearn.metrics import roc_auc_score

from ..meta import align as A, loop as LP, selftrain as ST
from ..meta.domain import eval_labels, load
from ..meta.intent import Intent
from . import docs as D

ROOT = Path(__file__).resolve().parents[2]
TOP = 0.10  # part du cours « à réviser » : les 10 % de passages jugés les plus probables
EXTRA = ["section_tombee_l_an_dernier", "annees_depuis_la_section", "passage_tombe_l_an_dernier"]


def reading(name: str, log=print):
    """Lecture complète des anciens sujets (mise en cache : c'est la partie longue)."""
    cache = ROOT / "data" / "cache" / f"lecture_{name}.joblib"
    t = load(name)
    if cache.exists():
        S, loop_rep = joblib.load(cache)
    else:
        meta = json.loads((ROOT / "data" / "model" / "meta.json").read_text())
        cfg, w, _ = A.self_tune(t, meta["poids"])
        S, _ = ST.improve(t, A.combine(A.views(t, cfg), w))
        S, _, loop_rep = LP.run(t, S, gens=2, log=log)
        joblib.dump((S, loop_rep), cache)
    t.rep = getattr(t, "rep", {})
    for q, s in zip(t.Q, S.argmax(1)):
        q.sec = int(s)
    t.consigne_vocab()
    t.consigne_facets()
    it = Intent(t, S)
    it.features()
    return t, S, it, loop_rep


class Forecast:
    def __init__(self, t, it, loop_rep):
        self.t, self.it, self.lr = t, it, loop_rep
        self.n = len(t.pass_text)
        self.T, self.tnames = LP.course_variables(t.pass_text)
        self.tested = defaultdict(set)
        self.q_of = defaultdict(list)
        for i, (q, p) in enumerate(zip(t.Q, it.pas)):
            if q.year:
                self.tested[q.year].add(int(p))
                self.q_of[q.year].append(i)
        self.years = sorted(self.tested)
        self.base = ["rang_du_passage_dans_la_section", "longueur_du_passage", "centralite_du_passage", "redondance_du_passage",
                     "insistance_typographique", "passage_avec_reference", "densite_symboles_du_passage",
                     "place_de_la_section_dans_le_cours", "taille_de_la_section", "centralite_de_la_section",
                     "frequence_passee_du_passage", "frequence_passee_de_la_section"]

    # ------------------------------------------------------------------ variables d'une année
    def rows(self, target: int, hist: list[int]) -> np.ndarray:
        it, ps, K = self.it, self.t.pass_sec, len(self.t.sections)
        hist = [z for z in hist if z != target] or [z for z in self.years if z != target]
        pf = np.array([np.mean([p in self.tested[z] for z in hist]) for p in range(self.n)])
        sec_t = {z: {int(ps[p]) for p in self.tested[z]} for z in hist}
        sf = np.array([np.mean([s in sec_t[z] for z in hist]) for s in range(K)])
        before = [z for z in hist if z < target]
        last = max(before) if before else None
        s_last = np.array([float(last is not None and s in sec_t[last]) for s in range(K)])
        since = np.array([min([target - z for z in before if s in sec_t[z]] or [8]) for s in range(K)], float)
        p_last = np.array([float(last is not None and p in self.tested[last]) for p in range(self.n)])
        X = np.column_stack([it.p_rank, it.p_len, it.p_central, it.p_redund, it.p_emph, it.p_ref, it.p_sym,
                             it.s_order[ps], it.s_size[ps], it.s_central[ps], pf, sf[ps], s_last[ps], since[ps], p_last])
        return X

    def design(self, X):
        """Base + récence ; et, pour les arbres, variables propres à la matière et croisements."""
        Xb = X
        nm = self.base + EXTRA
        Xf = np.hstack([LP._design(X[:, :12], self.base, self.T, self.n), X[:, 12:]])
        return Xb, Xf

    def _train(self, train_years: list[int]):
        """Une ligne par (année d'entraînement, passage) ; historique = les autres années d'entraînement."""
        Xs, ys = [], []
        for z in train_years:
            Xs.append(self.rows(z, train_years))
            ys.append(np.array([p in self.tested[z] for p in range(self.n)], int))
        return np.vstack(Xs), np.concatenate(ys)

    def _fit_predict(self, fam: str, Xtr, ytr, Xte) -> np.ndarray:
        if fam == "popularite":
            return Xte[:, 10] + 0.01 * Xte[:, 11]
        kind, mk = LP.FAMILIES[fam]
        Btr, Ftr = self.design(Xtr)
        Bte, Fte = self.design(Xte)
        A_, B_ = (Btr, Bte) if kind == "base" else (Ftr, Fte)
        return mk().fit(A_, ytr).predict_proba(B_)[:, 1]

    # ------------------------------------------------------------------ preuve : comme en vrai
    def backtest(self, k_years: int = 5, min_hist: int = 5) -> dict:
        fams = ["popularite", "logistique_12_generiques", self.lr.get("famille_choisie", "arbres_generiques_et_propres_a_la_matiere")]
        fams = list(dict.fromkeys(fams))
        tests = [y for y in self.years if len([z for z in self.years if z < y]) >= min_hist][-k_years:]
        res = {f: defaultdict(list) for f in fams}
        top = max(1, int(TOP * self.n))
        for y in tests:
            past = [z for z in self.years if z < y]
            Xtr, ytr = self._train(past)
            Xte = self.rows(y, past)
            yte = np.array([p in self.tested[y] for p in range(self.n)], int)
            qs = self.q_of[y]
            for f in fams:
                p = self._fit_predict(f, Xtr, ytr, Xte)
                sel = set(np.argsort(-p)[:top])
                near = self._near(sel)
                res[f]["auc"].append(roc_auc_score(yte, p) if len(set(yte)) > 1 else 0.5)
                res[f]["questions_couvertes"].append(np.mean([self.it.pas[i] in sel for i in qs]))
                res[f]["questions_couvertes_a_un_passage_pres"].append(np.mean([self.it.pas[i] in near for i in qs]))
                secs_pred = self._top_sections(p, 5)
                real = {int(self.t.pass_sec[self.it.pas[i]]) for i in qs}
                res[f]["chapitres_prevus_tombes_sur_5"].append(len(set(secs_pred) & real))
        out = {"annees_testees": tests, "passages_du_cours": self.n, "passages_prevus": top,
               "hasard_questions_couvertes": round(top / self.n, 3)}
        for f, r in res.items():
            out[f] = {k: round(float(np.mean(v)), 3) for k, v in r.items()}
            out[f]["par_annee"] = {str(y): round(float(v), 3) for y, v in zip(tests, r["questions_couvertes"])}
        return out

    def _near(self, sel: set) -> set:
        """Passage prévu ou son voisin immédiat dans la même section."""
        ps = self.t.pass_sec
        out = set(sel)
        for p in sel:
            for d in (-1, 1):
                if 0 <= p + d < self.n and ps[p + d] == ps[p]:
                    out.add(p + d)
        return out

    def _top_sections(self, p, k):
        ps = self.t.pass_sec
        sp = np.array([p[ps == s].max() if (ps == s).any() else 0 for s in range(len(self.t.sections))])
        return [int(s) for s in np.argsort(-sp)[:k]]

    # ------------------------------------------------------------------ l'année suivante
    def next_year(self) -> np.ndarray:
        fam = self.lr.get("famille_choisie", "arbres_generiques_et_propres_a_la_matiere")
        Xtr, ytr = self._train(self.years)
        nxt = self.years[-1] + 1
        self.prob = self._fit_predict(fam, Xtr, ytr, self.rows(nxt, self.years))
        self.annee = nxt
        return self.prob

    def hidden(self, p: int, k: int = 6) -> dict:
        """Ce que l'enseignant évalue sans le dire, appris de ses questions sur cette section."""
        t, it = self.t, self.it
        s = int(t.pass_sec[p])
        voc = it.wv.get_feature_names_out()
        row = it.Pw[p].toarray().ravel()
        terms = [voc[j] for j in np.argsort(-row)[:25] if row[j] > 0]
        past = [i for i, q in enumerate(t.Q) if int(t.pass_sec[it.pas[i]]) == s]
        if not past:  # section jamais tombée : questions sur les passages les plus proches
            sims = (t.P[it.pas] @ t.P[p].T).toarray().ravel()
            past = list(np.argsort(-sims)[:8])
        said = [set(re.findall(r"[a-z]{4,}", D.norm(t.Q[i].stem + " " + t.Q[i].situation[:3000]))) for i in past]
        ans = [set(re.findall(r"[a-z]{4,}", D.norm(t.Q[i].answer))) for i in past if t.Q[i].answer]
        cachee, dite = [], []
        for w in terms:
            r_said = np.mean([w in x for x in said])
            r_ans = np.mean([w in x for x in ans]) if ans else None
            if r_said < 0.2 and (r_ans is None or r_ans > r_said):
                cachee.append(w)
            elif r_said >= 0.4:
                dite.append(w)
        fac = Counter(t.Q[i].facet for i in past)
        ex = sorted(past, key=lambda i: -float((t.P[it.pas[i]] @ t.P[p].T).toarray()[0, 0]))[:2]
        types = Counter(int(it.labels[i]) for i in past) if hasattr(it, "labels") else Counter()
        return {"evalue_sans_etre_dit": cachee[:k], "toujours_nomme": dite[:4],
                "manieres_de_demander": [{"facette": int(f), "nom": t.facets[f]["nom"], "part": round(c / len(past), 2)} for f, c in fac.most_common(3)],
                "type_d_intention": types.most_common(1)[0][0] if types else None,
                "questions_passees_proches": [{"sujet": t.Q[i].exam, "enonce": t.Q[i].stem[:220]} for i in ex]}

    def ranking(self, n_top: int = 15, per_section: int = 2) -> list[dict]:
        t = self.t
        out, cnt = [], Counter()
        for p in np.argsort(-self.prob):
            s = int(t.pass_sec[p])
            if cnt[s] >= per_section:
                continue
            cnt[s] += 1
            out.append({"passage": int(p), "section": s, "section_titre": t.sections[s].title,
                        "probabilite": round(float(self.prob[p]), 3), "texte": t.pass_text[p][:600],
                        "deja_tombe": int(sum(p in self.tested[z] for z in self.years)), **self.hidden(int(p))})
            if len(out) == n_top:
                break
        return out


def run(name: str, log=print) -> dict:
    warnings.filterwarnings("ignore")
    t, S, it, loop_rep = reading(name, log)
    rp = json.loads((ROOT / "output" / "meta" / "rapport.json").read_text())
    keep = rp["intentions"]["par_matiere"].get(name, {}).get("types_d_intention", {}).get("variables_utilisees", [])
    ty = it.types(keep) if keep else {"types": []}
    fc = Forecast(t, it, loop_rep)
    log(f"{name} : {len(fc.years)} années, {fc.n} passages")
    bt = fc.backtest()
    log(f"  preuve : {json.dumps({k: v for k, v in bt.items() if isinstance(v, dict)}, ensure_ascii=False)[:600]}")
    fc.next_year()
    rk = fc.ranking()
    lab = {x["id"]: x for x in ty["types"]}
    for r in rk:
        k = r.pop("type_d_intention")
        r["intention"] = {"fort": lab[k]["fort"], "faible": lab[k]["faible"]} if k in lab else None
    rep = {"matiere": name, "annee_prevue": fc.annee, "annees_connues": fc.years, "preuve_comme_en_vrai": bt,
           "famille_choisie": loop_rep.get("famille_choisie"), "passages_les_plus_probables": rk}
    out = ROOT / "output" / ("droit" if name == "droit" else f"{name}_prof")
    out.mkdir(parents=True, exist_ok=True)
    (out / "previsions.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    joblib.dump((t, fc.prob, rk), ROOT / "data" / "cache" / f"prevision_{name}.joblib")
    return rep


if __name__ == "__main__":
    for n in sys.argv[1:] or ["droit", "nsi"]:
        run(n)
