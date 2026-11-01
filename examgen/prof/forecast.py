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
        qw = [set(re.findall(r"[a-z]{4,}", D.norm(q.stem + " " + q.situation[:2000]))) for q in t.Q]
        df = Counter(w for x in qw for w in x)
        self.generic = {w for w, c in df.items() if c > 0.12 * len(qw)}
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
        if fam == "ensemble":  # moyenne des rangs des trois familles
            from scipy.stats import rankdata
            return np.mean([rankdata(self._fit_predict(f, Xtr, ytr, Xte)) for f in LP.FAMILIES], 0) / len(Xte)
        kind, mk = LP.FAMILIES[fam]
        Btr, Ftr = self.design(Xtr)
        Bte, Fte = self.design(Xte)
        A_, B_ = (Btr, Bte) if kind == "base" else (Ftr, Fte)
        return mk().fit(A_, ytr).predict_proba(B_)[:, 1]

    # ------------------------------------------------------------------ preuve : comme en vrai
    def backtest(self, k_years: int = 5, min_hist: int = 3) -> dict:
        """Chaque année testée : apprentissage sur les seules années d'avant. La famille « choisie
        seule » pour une année est celle qui a le mieux prévu les années testées précédentes."""
        learned = list(LP.FAMILIES) + ["ensemble"]
        fams = ["popularite"] + learned
        tests = [y for y in self.years if len([z for z in self.years if z < y]) >= min_hist][-k_years:]
        res = {f: defaultdict(list) for f in fams + ["choisie_seule"]}
        top = max(1, int(TOP * self.n))
        self.choices = []
        for y in tests:
            past = [z for z in self.years if z < y]
            Xtr, ytr = self._train(past)
            Xte = self.rows(y, past)
            yte = np.array([p in self.tested[y] for p in range(self.n)], int)
            qs = self.q_of[y]
            prev = {f: self._score(res[f]) for f in learned}
            pick = max(prev, key=prev.get) if res[learned[0]]["auc"] else self.lr.get("famille_choisie", learned[-2])
            self.choices.append(pick)
            P = {f: self._fit_predict(f, Xtr, ytr, Xte) for f in fams}
            P["choisie_seule"] = P[pick]
            for f, p in P.items():
                sel = set(np.argsort(-p)[:top])
                near = self._near(sel)
                res[f]["auc"].append(roc_auc_score(yte, p) if len(set(yte)) > 1 else 0.5)
                res[f]["questions_couvertes"].append(np.mean([self.it.pas[i] in sel for i in qs]))
                res[f]["questions_couvertes_a_un_passage_pres"].append(np.mean([self.it.pas[i] in near for i in qs]))
                real = {int(self.t.pass_sec[self.it.pas[i]]) for i in qs}
                res[f]["chapitres_prevus_tombes_sur_5"].append(len(set(self._top_sections(p, 5)) & real))
        self.final = max(learned, key=lambda f: self._score(res[f]))
        out = {"annees_testees": tests, "passages_du_cours": self.n, "passages_prevus": top,
               "hasard_questions_couvertes": round(top / self.n, 3), "choix_par_annee": dict(zip(map(str, tests), self.choices)),
               "famille_pour_l_annee_prevue": self.final}
        for f, r in res.items():
            out[f] = {k: round(float(np.mean(v)), 3) for k, v in r.items()}
            out[f]["par_annee"] = {str(y): round(float(v), 3) for y, v in zip(tests, r["questions_couvertes"])}
        return out

    @staticmethod
    def _score(r) -> float:
        return float(np.mean(r["questions_couvertes"]) + 0.1 * np.mean(r["auc"])) if r["auc"] else 0.0

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
        fam = getattr(self, "final", None) or self.lr.get("famille_choisie", "arbres_generiques_et_propres_a_la_matiere")
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
        # mot propre au chapitre : bien plus fréquent dans ses passages que dans le reste du cours
        col = {w: it.wv.vocabulary_[w] for w in terms}
        insec = np.asarray((it.Pw[t.pass_sec == s] > 0).mean(0)).ravel()
        allc = np.asarray((it.Pw > 0).mean(0)).ravel()
        if not hasattr(self, "_spread"):  # part des chapitres où le mot apparaît : un mot de liaison est partout
            ps = np.asarray(t.pass_sec)
            M = np.vstack([np.asarray((it.Pw[ps == z] > 0).max(0).todense()).ravel() for z in np.unique(ps)])
            self._spread = M.mean(0)
        terms = [w for w in terms if insec[col[w]] >= 2.5 * allc[col[w]] and w not in self.generic and allc[col[w]] < 0.06
                 and self._spread[col[w]] < 0.3]
        if not hasattr(self, "_all_ans"):  # tous les corrigés : pour écarter les mots de liaison
            self._all_ans = [set(re.findall(r"[a-z]{4,}", D.norm(q.answer))) for q in t.Q if q.answer]
            ex_w = defaultdict(set)  # sans corrigés : vocabulaire réellement employé par l'enseignant
            for q in t.Q:
                for w in set(re.findall(r"[a-z]{4,}", D.norm(q.stem + " " + q.situation))):
                    ex_w[w].add(q.exam)
            self._exam_n = {w: len(e) for w, e in ex_w.items()}
        cachee, dite = [], []
        for w in terms:
            r_said = np.mean([w in x for x in said])
            r_ans = np.mean([w in x for x in ans]) if ans else None
            r_all = np.mean([w in x for x in self._all_ans]) if self._all_ans else 0
            if r_ans is None:  # pas de corrigé : mot de l'enseignant (≥ 3 sujets) et récurrent dans le chapitre
                spec = self._exam_n.get(w, 0) >= 3 and insec[col[w]] >= 0.1
            else:
                spec = r_ans >= 2 * r_all  # propre aux corrigés de ce chapitre
            if r_said < 0.2 and spec and (r_ans is None or r_ans >= max(0.25, 2 * r_said)):
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

    # ------------------------------------------------------------------ tout le cours
    def _pot_model(self, train_years):
        """Manière de l'enseignant sans l'historique : quel GENRE de passage il choisit
        (place, centralité, insistance, références...), donc applicable à un passage jamais tombé."""
        Xtr, ytr = self._train(train_years)
        from sklearn.linear_model import LogisticRegression
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        return make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight="balanced")).fit(Xtr[:, :10], ytr)

    def novelty_proof(self, min_hist: int = 3) -> dict:
        """Preuve « comme en vrai » sur les questions NOUVELLES : passage jamais interrogé avant
        l'année testée. Le potentiel les classe-t-il mieux que le hasard ?"""
        aucs, cov, n_new, tests = [], [], 0, []
        for y in [z for z in self.years if len([w for w in self.years if w < z]) >= min_hist]:
            past = [z for z in self.years if z < y]
            seen = set().union(*(self.tested[z] for z in past))
            fresh = np.array([p not in seen for p in range(self.n)])
            yte = np.array([p in self.tested[y] for p in range(self.n)], int)
            if fresh.sum() < 10 or len(set(yte[fresh])) < 2:
                continue
            pot = self._pot_model(past).predict_proba(self.rows(y, past)[:, :10])[:, 1]
            aucs.append(roc_auc_score(yte[fresh], pot[fresh]))
            idx = np.where(fresh)[0]
            sel = set(idx[np.argsort(-pot[idx])[:max(1, int(0.25 * len(idx)))]].tolist())
            qs = [i for i in self.q_of[y] if int(self.it.pas[i]) not in seen]
            n_new += len(qs)
            if qs:
                cov.append(np.mean([int(self.it.pas[i]) in sel for i in qs]))
            tests.append(y)
        return {"annees_testees": tests, "questions_nouvelles": n_new,
                "auc_potentiel_sur_passages_jamais_tombes": round(float(np.mean(aucs)), 3) if aucs else None,
                "nouvelles_couvertes_par_le_quart_retenu": round(float(np.mean(cov)), 3) if cov else None, "hasard": 0.25}

    def programme(self, per_sec: int = 3) -> list[dict]:
        """Chaque chapitre du cours, classé par priorité d'entraînement."""
        t, ps, K = self.t, np.asarray(self.t.pass_sec), len(self.t.sections)
        if getattr(self, "pot", None) is None:
            self.pot = self._pot_model(self.years).predict_proba(self.rows(self.annee, self.years)[:, :10])[:, 1]
        from scipy.stats import rankdata
        rp, rq = rankdata(self.prob) / self.n, rankdata(self.pot) / self.n
        sec_years = {s: sum(any(int(ps[p]) == s for p in self.tested[z]) for z in self.years) for s in range(K)}
        rows = []
        for s in range(K):
            idx = np.where(ps == s)[0]
            if not len(idx):
                continue
            score = 0.6 * rp[idx] + 0.4 * rq[idx]
            rows.append({"section": s, "titre": t.sections[s].title, "passages": int(len(idx)),
                         "proba": round(float(self.prob[idx].max()), 3), "potentiel": round(float(self.pot[idx].max()), 3),
                         "annees_tombees": int(sec_years[s]), "sur": len(self.years),
                         "priorite": round(float(score.max()), 3), "_top": idx[np.argsort(-score)[:per_sec]].tolist()})
        rows.sort(key=lambda r: -r["priorite"])
        q = np.quantile([r["priorite"] for r in rows], [0.5, 0.75])
        qp = np.quantile([r["potentiel"] for r in rows], 0.5)
        for r in rows:
            if r["priorite"] >= q[1] and r["annees_tombees"] >= 2:
                r["niveau"] = "incontournable"
            elif r["annees_tombees"] <= 1 and r["potentiel"] >= qp:
                r["niveau"] = "peu ou jamais tombé, mais dans la manière du professeur"
            elif r["priorite"] >= q[0]:
                r["niveau"] = "probable"
            else:
                r["niveau"] = "à connaître"
            r["passages_cles"] = [{"passage": int(p), "texte": t.pass_text[p][:400], "proba": round(float(self.prob[p]), 3),
                                   "potentiel": round(float(self.pot[p]), 3),
                                   "deja_tombe": int(sum(p in self.tested[z] for z in self.years)), **self.hidden(int(p))}
                                  for p in r.pop("_top")]
        return rows


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
    from ..meta import transfer as TR
    auto = TR.apply(fc, log)  # même règle pour tous les domaines, sans choix propre à la matière
    # le classement vient de la règle universelle ; les probabilités affichées gardent la loi de
    # l'ancien modèle (même nombre attendu de passages), réordonnées selon ce classement
    order = np.argsort(np.argsort(auto["prevision"]["p"], kind="stable"), kind="stable")
    fc.prob, fc.pot = np.sort(fc.prob)[order], auto["nouveaute"]["p"]
    rk = fc.ranking()
    nov = fc.novelty_proof()
    log(f"  nouveautés : {nov}")
    prog = fc.programme()
    lab = {x["id"]: x for x in ty["types"]}
    for r in rk + [x for g in prog for x in g["passages_cles"]]:
        k = r.pop("type_d_intention")
        r["intention"] = {"fort": lab[k]["fort"], "faible": lab[k]["faible"]} if k in lab else None
    rep = {"matiere": name, "annee_prevue": fc.annee, "annees_connues": fc.years, "preuve_comme_en_vrai": bt,
           "famille_choisie": fc.final, "passages_les_plus_probables": rk,
           "preuve_sur_les_nouveautes": nov, "programme": prog,
           "auto_progression": {o: {k: v for k, v in a.items() if k != "p"} for o, a in auto.items()}}
    if TR.RULE_OUT.exists():
        rg = json.loads(TR.RULE_OUT.read_text(encoding="utf-8"))
        rep["preuve_auto_progression"] = {**rg["matieres"].get(name, {}), "auto_jugement": rg["auto_jugement"]}
    from ..meta.domain import out_dir
    out = out_dir(name)
    out.mkdir(parents=True, exist_ok=True)
    (out / "previsions.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    joblib.dump((t, fc.prob, rk), ROOT / "data" / "cache" / f"prevision_{name}.joblib")
    return rep


if __name__ == "__main__":
    for n in sys.argv[1:] or ["droit", "nsi"]:
        run(n)
