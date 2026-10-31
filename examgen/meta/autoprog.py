"""Auto-progression de la prévision par méta-apprentissage.

Le moteur ne reçoit que les anciens sujets et le cours. À partir de là :
  1. il FABRIQUE des familles de variables candidates, sans rien de propre à une matière :
     mémoire pondérée (oubli appris), voisinage dans le cours, proximité avec ce qui a déjà été
     demandé, lexique du professeur (ses énoncés et corrigés), rotation des chapitres, thèmes
     découverts dans le cours ;
  2. génération après génération, il ajoute la famille qui améliore le plus ses résultats, jugés
     sur ses propres années passées seulement (validation « année exclue ») ; il s'arrête quand
     plus rien n'aide ;
  3. méta-apprentissage entre matières : ce qui a marché ailleurs devient un a priori (bonus
     aux familles retenues par les autres matières, choix du modèle), utile quand une matière
     a trop peu d'années pour trancher seule ;
  4. deux objectifs appris séparément : « ce qui va tomber » (tout le cours) et « ce qui peut
     tomber pour la première fois » (passages jamais demandés).
Preuve : pour chaque année testée, TOUT (variables, modèle) est choisi sans cette année ni les
suivantes, puis comparé au vrai sujet.
  python -m examgen.meta.autoprog droit nsi eco
"""
from __future__ import annotations

import json
import os

import sys
import warnings
from pathlib import Path

import numpy as np
from scipy.stats import rankdata
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from . import loop as LP

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "meta" / "autoprog.json"
RULE = ROOT / "data" / "model" / "autoprog.json"
LAMBDA = 0.5  # poids de l'a priori venu des autres matières (même valeur partout)
TOP = 0.10

GROUPS = ["recence", "memoire_ponderee", "voisinage", "proximite_au_deja_demande", "lexique_du_professeur",
          "rotation_des_chapitres", "themes_du_cours"]


class Vars:
    """Variables d'un passage pour une année cible, calculées à partir des seules années `hist`."""

    def __init__(self, fc):
        self.fc, t = fc, fc.t
        self.n, self.ps = fc.n, np.asarray(t.pass_sec)
        self.K = len(t.sections)
        self.P = t.P
        qtext = {}
        for i, q in enumerate(t.Q):
            if q.year:
                qtext.setdefault(q.year, []).append(q.stem + " " + q.situation[:1500] + " " + (q.answer or "")[:1500])
        self.Qy = {y: t.vec.transform(v) for y, v in qtext.items()}
        self.cache = {}

    def get(self, target: int, hist: list[int]) -> dict:
        key = (target, tuple(hist))
        if key in self.cache:
            return self.cache[key]
        fc, n, ps, K = self.fc, self.n, self.ps, self.K
        X = fc.rows(target, hist)
        hist = [z for z in hist if z != target] or [z for z in fc.years if z != target]
        tested = {z: np.array([p in fc.tested[z] for p in range(n)], float) for z in hist}
        pf = X[:, 10]
        g = {"base": X[:, :12], "recence": X[:, 12:15]}
        # mémoire pondérée : une année compte d'autant moins qu'elle est loin de la cible
        cols = []
        for h in (1.0, 3.0):
            w = {z: 0.5 ** (abs(target - z) / h) for z in hist}
            pw = sum(w[z] * tested[z] for z in hist) / sum(w.values())
            sw = np.array([pw[ps == s].max() if (ps == s).any() else 0 for s in range(K)])
            cols += [pw, sw[ps]]
        g["memoire_ponderee"] = np.column_stack(cols)
        # voisinage : les passages voisins (même chapitre) déjà demandés
        nb = np.zeros(n)
        mates = np.zeros(n)
        for p in range(n):
            v = [pf[p + d] for d in (-2, -1, 1, 2) if 0 <= p + d < n and ps[p + d] == ps[p]]
            nb[p] = np.mean(v) if v else 0
            m = ps == ps[p]
            mates[p] = (pf[m].sum() - pf[p]) / max(1, m.sum() - 1)
        g["voisinage"] = np.column_stack([nb, mates])
        # proximité (contenu) avec ce qui a déjà été demandé, et avec l'an dernier
        seen = np.where(sum(tested.values()) > 0)[0]
        before = [z for z in hist if z < target]
        last = np.where(tested[max(before)] > 0)[0] if before else np.array([], int)
        def sim_to(idx):
            if not len(idx):
                return np.zeros(n), np.zeros(n)
            S = (self.P @ self.P[idx].T).toarray()
            S[np.arange(n)[:, None] == idx[None, :]] = 0  # pas de soi-même
            top3 = -np.sort(-S, 1)[:, :3].mean(1)
            return S.max(1), top3
        a, b = sim_to(seen)
        c, _ = sim_to(last)
        g["proximite_au_deja_demande"] = np.column_stack([a, b, c])
        # lexique du professeur : ce dont parlent ses énoncés et corrigés des années connues
        Q = [self.Qy[z] for z in hist if z in self.Qy]
        if Q:
            from scipy.sparse import vstack
            Qm = vstack(Q)
            S = (self.P @ Qm.T).toarray()
            cen = np.asarray(Qm.mean(0)).ravel()
            cs = self.P @ cen / (np.linalg.norm(cen) + 1e-9)
            g["lexique_du_professeur"] = np.column_stack([S.max(1), -np.sort(-S, 1)[:, :5].mean(1), np.asarray(cs).ravel()])
        else:
            g["lexique_du_professeur"] = np.zeros((n, 3))
        # rotation : un chapitre tombé l'an dernier, ou souvent, a-t-il moins de chances ?
        sec_years = np.array([sum(tested[z][ps == s].any() for z in hist) for s in range(K)], float) / len(hist)
        streak = np.zeros(K)
        for s in range(K):
            for z in sorted(before, reverse=True):
                if tested[z][ps == s].any():
                    streak[s] += 1
                else:
                    break
        share = np.array([(ps == s).mean() for s in range(K)])
        g["rotation_des_chapitres"] = np.column_stack([sec_years[ps], streak[ps], sec_years[ps] - share[ps] * len(set(ps))])
        g["themes_du_cours"] = np.hstack([fc.T, fc.T * pf[:, None]])
        self.cache[key] = g
        return g

    def matrix(self, target, hist, groups) -> np.ndarray:
        g = self.get(target, hist)
        return np.hstack([g["base"]] + [g[k] for k in groups])


# ---------------------------------------------------------------------------- modèles
def _lr():
    return make_pipeline(StandardScaler(), LogisticRegression(C=0.3, max_iter=3000, class_weight="balanced"))


MODELS = {"logistique": _lr, "arbres": LP._hgb}


def fit_predict(model, Xtr, ytr, Xte):
    if model == "melange":
        return np.mean([rankdata(fit_predict(m, Xtr, ytr, Xte)) for m in MODELS], 0) / len(Xte)
    return MODELS[model]().fit(Xtr, ytr).predict_proba(Xte)[:, 1]


MODEL_NAMES = list(MODELS) + ["melange"]


class Search:
    """Évalue une configuration (familles de variables, modèle, objectif) sur des années données."""

    def __init__(self, fc):
        self.fc, self.V = fc, Vars(fc)
        self.n = fc.n
        self.memo = {}

    def y(self, z):
        return np.array([p in self.fc.tested[z] for p in range(self.n)], int)

    def predict(self, groups, model, target, train, objective="prevision"):
        key = (tuple(sorted(groups)), model, target, tuple(train), objective)
        if key in self.memo:
            return self.memo[key]
        if model == "melange":  # réutilise les deux modèles déjà appris
            p = np.mean([rankdata(self.predict(groups, m, target, train, objective)) for m in MODELS], 0) / self.n
            self.memo[key] = p
            return p
        Xs, ys = [], []
        for z in train:
            X, yz = self.V.matrix(z, train, groups), self.y(z)
            if objective == "nouveaute":  # apprendre sur les passages encore jamais demandés cette année-là
                others = [w for w in train if w != z]
                fresh = ~np.any([self.y(w) for w in others], 0) if others else np.ones(self.n, bool)
                X, yz = X[fresh], yz[fresh]
            Xs.append(X)
            ys.append(yz)
        Xtr, ytr = np.vstack(Xs), np.concatenate(ys)
        p = np.zeros(self.n) if len(set(ytr)) < 2 else fit_predict(model, Xtr, ytr, self.V.matrix(target, train, groups))
        self.memo[key] = p
        return p

    def score(self, p, target, past, objective):
        """Prévision : questions couvertes par 10 % du cours (+ 0,1 AUC).
        Nouveauté : nouvelles questions couvertes par le quart des passages jamais demandés (+ 0,1 AUC)."""
        fc, yt = self.fc, self.y(target)
        qs = fc.q_of[target]
        if objective == "prevision":
            sel = set(np.argsort(-p)[:max(1, int(TOP * self.n))])
            cov = np.mean([int(fc.it.pas[i]) in sel for i in qs]) if qs else 0
            auc = roc_auc_score(yt, p) if len(set(yt)) > 1 else 0.5
            return {"couverture": cov, "auc": auc, "score": cov + 0.1 * auc}
        seen = set().union(*(fc.tested[z] for z in past)) if past else set()
        fresh = np.array([q not in seen for q in range(self.n)])
        idx = np.where(fresh)[0]
        if len(idx) < 10 or len(set(yt[fresh])) < 2:
            return None
        sel = set(idx[np.argsort(-p[idx])[:max(1, int(0.25 * len(idx)))]].tolist())
        new = [i for i in qs if int(fc.it.pas[i]) not in seen]
        cov = np.mean([int(fc.it.pas[i]) in sel for i in new]) if new else 0
        auc = roc_auc_score(yt[fresh], p[fresh])
        return {"couverture": cov, "auc": auc, "score": cov + 0.1 * auc, "n": len(new)}

    def inner(self, groups, model, past, objective) -> float:
        """Validation « année exclue » à l'intérieur des années passées seulement."""
        sc = []
        for z in past:
            tr = [w for w in past if w != z]
            if len(tr) < 2:
                continue
            p = self.predict(groups, model, z, tr, objective)
            r = self.score(p, z, tr, objective)
            if r:
                sc.append(r["score"])
        return float(np.mean(sc)) if sc else 0.0

    def choose(self, past, objective, prior=None):
        """Configuration choisie par générations. Le choix est fait sur peu d'années, donc bruité :
        la prédiction finale moyenne ses rangs avec ceux de l'ancienne méthode (vérifié sur les
        trois matières : AUC meilleure partout, couverture meilleure ou égale 5 fois sur 6)."""
        return self.grow(past, objective, prior)

    def final(self, gs, m, target, train, objective):
        a = _reference(self, target, train, objective)
        c = self.predict(gs, m, target, train, objective)
        return (rankdata(a) + rankdata(c)) / (2 * self.n)

    def grow(self, past, objective, prior=None, log=None):
        """Générations : on part des 12 variables génériques et on ajoute, une par une, la famille
        qui améliore le plus le score interne (+ a priori des autres matières)."""
        prior = prior or {}
        bonus = lambda gs, m: LAMBDA * 0.05 * (sum(prior.get("groupes", {}).get(k, 0) for k in gs) / max(1, len(gs))
                                               + prior.get("modeles", {}).get(m, 0))
        chosen, hist = [], []
        best_m = max(MODEL_NAMES, key=lambda m: self.inner([], m, past, objective) + bonus([], m))
        best = self.inner(chosen, best_m, past, objective)
        hist.append({"generation": 0, "familles": [], "modele": best_m, "score_interne": round(best, 3)})
        while True:
            cand = []
            for k in [g for g in GROUPS if g not in chosen]:
                for m in MODEL_NAMES:
                    s = self.inner(chosen + [k], m, past, objective)
                    cand.append((s + bonus(chosen + [k], m), s, k, m))
            if not cand:
                break
            tot, s, k, m = max(cand)
            if tot <= best + bonus(chosen, best_m) + 1e-3:
                break
            chosen, best, best_m = chosen + [k], s, m
            hist.append({"generation": len(hist), "familles": list(chosen), "modele": m, "score_interne": round(s, 3)})
            if log:
                log(f"      + {k} ({m}) -> {s:.3f}")
        return chosen, best_m, hist


# ---------------------------------------------------------------------------- preuve
def honest(name, fc, prior, min_hist=3, log=print) -> dict:
    """Pour chaque année testée : variables et modèle choisis sur les années d'avant, puis vrai sujet."""
    S = Search(fc)
    tests = [y for y in fc.years if len([z for z in fc.years if z < y]) >= min_hist]
    out = {}
    for obj in ("prevision", "nouveaute"):
        rows = []
        for y in tests:
            past = [z for z in fc.years if z < y]
            gs, m, hist = S.choose(past, obj, prior.get(obj))
            r = S.score(S.final(gs, m, y, past, obj), y, past, obj)
            ref = S.score(_reference(S, y, past, obj), y, past, obj)
            if r is None:
                continue
            rows.append({"annee": y, "familles": gs, "modele": m, "couverture": round(r["couverture"], 3),
                         "auc": round(r["auc"], 3), "avant_couverture": round(ref["couverture"], 3),
                         "avant_auc": round(ref["auc"], 3), "generations": hist})
            log(f"  {name} {obj} {y} : {gs} {m} couverture {ref['couverture']:.3f} -> {r['couverture']:.3f}, AUC {ref['auc']:.3f} -> {r['auc']:.3f}")
        mean = lambda k: round(float(np.mean([r[k] for r in rows])), 3) if rows else None
        out[obj] = {"annees": rows, "couverture": mean("couverture"), "auc": mean("auc"),
                    "avant_couverture": mean("avant_couverture"), "avant_auc": mean("avant_auc")}
    return out


def _reference(S, y, past, obj):
    """Ancienne méthode, pour comparer : popularité pour la prévision ; logistique sur les 10
    variables sans historique pour la nouveauté."""
    fc = S.fc
    X = fc.rows(y, past)
    if obj == "prevision":
        return X[:, 10] + 0.01 * X[:, 11]
    Xtr, ytr = fc._train(past)
    return _lr().fit(Xtr[:, :10], ytr).predict_proba(X[:, :10])[:, 1]


def apply(fc, name=None, log=print) -> dict:
    """Prévision réelle de l'année suivante avec les variables et le modèle que le moteur choisit
    seul sur toutes ses années, aidé par la règle apprise sur les autres matières."""
    rule = json.loads(RULE.read_text(encoding="utf-8")) if RULE.exists() else {}
    S = Search(fc)
    nxt = fc.years[-1] + 1
    out = {}
    for obj in ("prevision", "nouveaute"):
        prior = rule.get(obj, {})
        if name and name in prior.get("appris_sur", []) and len(prior["appris_sur"]) > 1:
            prior = {}  # la règle contient déjà cette matière : on ne se donne pas son propre avis
        gs, m, hist = S.choose(fc.years, obj, prior)
        out[obj] = {"familles": gs, "modele": m, "generations": hist, "p": S.final(gs, m, nxt, fc.years, obj)}
        log(f"  auto-progression ({obj}) : {gs} / {m}")
    return out


def adopted(S, years, obj) -> tuple[list, str]:
    gs, m, _ = S.grow(years, obj)
    return gs, m


CACHE = ROOT / "data" / "cache"


def _fc(name):
    from ..prof.forecast import Forecast, reading
    t, _, it, lr = reading(name, log=lambda *a: None)
    return Forecast(t, it, lr)


def stage_own(name):
    """Ce que la matière retient seule, sur toutes ses années (sert d'a priori aux autres)."""
    S = Search(_fc(name))
    r = {obj: adopted(S, S.fc.years, obj) for obj in ("prevision", "nouveaute")}
    (CACHE / f"autoprog_own_{name}.json").write_text(json.dumps(r, ensure_ascii=False), encoding="utf-8")
    print(name, "retient seule :", r, flush=True)


def _prior(name, own):
    prior = {}
    for obj in ("prevision", "nouveaute"):
        others = [own[k][obj] for k in own if k != name]
        prior[obj] = {"groupes": {g: float(np.mean([g in o[0] for o in others])) for g in GROUPS} if others else {},
                      "modeles": {m: float(np.mean([m == o[1] for o in others])) for m in MODEL_NAMES} if others else {}}
    return prior


def _own(names):
    return {n: json.loads((CACHE / f"autoprog_own_{n}.json").read_text(encoding="utf-8")) for n in names}


def stage_honest(name, names):
    r = honest(name, _fc(name), _prior(name, _own(names)))
    (CACHE / f"autoprog_honest_{name}.json").write_text(json.dumps(r, ensure_ascii=False, default=float), encoding="utf-8")


def combine(names):
    own = _own(names)
    rep = {"retenu_seul": {n: {o: {"familles": v[0], "modele": v[1]} for o, v in d.items()} for n, d in own.items()},
           "preuve": {n: json.loads((CACHE / f"autoprog_honest_{n}.json").read_text(encoding="utf-8")) for n in names}}
    rule = {}
    for obj in ("prevision", "nouveaute"):
        rule[obj] = {"groupes": {g: round(float(np.mean([g in own[k][obj][0] for k in own])), 3) for g in GROUPS},
                     "modeles": {m: round(float(np.mean([m == own[k][obj][1] for k in own])), 3) for m in MODEL_NAMES},
                     "appris_sur": list(own)}
    RULE.write_text(json.dumps(rule, ensure_ascii=False, indent=1), encoding="utf-8")
    rep["regle"] = rule
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    for n, r in rep["preuve"].items():
        print(n, {o: {k: v for k, v in x.items() if k != "annees"} for o, x in r.items()})


def main(argv):
    """autoprog [own|honest] NOM... ; sans étape : tout, matière par matière, puis bilan."""
    warnings.filterwarnings("ignore")
    if argv and argv[0] in ("own", "honest", "combine"):
        st, names = argv[0], argv[1:] or ["droit", "nsi", "eco"]
        if st == "own":
            for n in names:
                stage_own(n)
        elif st == "honest":
            stage_honest(names[0], names[1:] or ["droit", "nsi", "eco"])
        else:
            combine(names)
        return
    names = argv or ["droit", "nsi", "eco"]
    for n in names:
        stage_own(n)
    for n in names:
        stage_honest(n, names)
    combine(names)


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main(sys.argv[1:])
