"""Méta-entraînement pour les domaines inconnus : apprendre à se juger et à se choisir.

But : sur une matière jamais vue (cours + anciens sujets seulement), choisir les bonnes variables
et le bon modèle, et annoncer à l'avance quelle qualité on peut en attendre.

1. Tâches. Chaque (matière, année testée) est une tâche. Pour en avoir beaucoup, chaque cours est
   aussi découpé en « pseudo-domaines » : la moitié de ses chapitres, tirée au hasard. Une tâche ne
   voit que les années d'avant l'année testée.
2. Candidats. Familles de variables (y compris des croisements construits automatiquement) ×
   modèles, purs ou mêlés à l'ancienne méthode. Pour chaque candidat : son score en validation
   interne (années passées seulement) et son vrai score sur l'année testée.
3. Juge. Un méta-modèle apprend, à partir de traits du domaine (taille, répétition des questions,
   concentration des chapitres…) et du score interne de chaque candidat, à prédire son vrai gain
   sur l'ancienne méthode. Il corrige l'optimisme de la validation interne selon le domaine.
4. Preuve « matière inconnue ». Le juge est appris sans la matière testée (ni ses pseudo-domaines),
   puis appliqué à elle. On compare à l'ancienne méthode et à l'auto-progression précédente.
   Il annonce aussi le score attendu ; on mesure l'écart avec le score réel (auto-jugement).

    python -m examgen.meta.transfer tasks droit      # (une matière par processus)
    python -m examgen.meta.transfer judge droit nsi eco
    python -m examgen.meta.transfer rule droit nsi eco   # règle universelle retenue (voir plus bas)
"""
from __future__ import annotations

import json
import sys
import warnings
from itertools import product

import joblib
import numpy as np
from scipy.stats import rankdata
from sklearn.ensemble import ExtraTreesRegressor
from ..fast import auc as roc_auc_score

from . import autoprog as AP
from ..fast import pmap

CACHE = AP.CACHE
OUT = AP.ROOT / "output" / "meta" / "transfer.json"
MODEL = AP.ROOT / "data" / "model" / "transfer.joblib"
TOP = AP.TOP
GROUPS = AP.GROUPS + ["croisements"]
SETS = [()] + [(g,) for g in GROUPS] + [tuple(GROUPS)]
FIT_MODELS = ["logistique", "arbres"]
N_MASKS = 5
OBJ = ("prevision", "nouveaute")


# ---------------------------------------------------------------------------- variables construites
class TVars(AP.Vars):
    """Ajoute une famille construite sans intervention : chaque famille croisée avec la popularité."""

    def get(self, target, hist):
        g = super().get(target, hist)
        if "croisements" not in g:
            pf = g["base"][:, 10:11]
            g["croisements"] = np.hstack([pf * g[k][:, :1] for k in AP.GROUPS] + [pf * g["base"][:, :10]])
        return g


# ---------------------------------------------------------------------------- domaine masqué
class Domain:
    """Une matière, ou un pseudo-domaine (sous-ensemble de chapitres)."""

    def __init__(self, fc, V, mask):
        self.fc, self.V, self.mask = fc, V, mask
        self.idx = np.where(mask)[0]
        self.n = len(self.idx)
        self.memo = {}
        m = set(self.idx.tolist())
        self.Y = {z: np.array([p in fc.tested[z] for p in self.idx], int) for z in fc.years}
        self.Q = {z: [int(fc.it.pas[i]) for i in fc.q_of[z] if int(fc.it.pas[i]) in m] for z in fc.years}

    def y(self, z):
        return self.Y[z]

    def qs(self, z):
        return self.Q[z]

    def X(self, target, train, groups):
        return self.V.matrix(target, train, list(groups))[self.idx]

    def predict(self, groups, model, target, train, obj):
        key = (groups, model, target, tuple(train), obj)
        if key in self.memo:
            return self.memo[key]
        if model == "melange":
            p = (rankdata(self.predict(groups, "logistique", target, train, obj)) +
                 rankdata(self.predict(groups, "arbres", target, train, obj))) / (2 * self.n)
        elif model == "ancienne":
            p = self.reference(target, train, obj)
        else:
            Xs, ys = [], []
            for z in train:
                X, yz = self.X(z, train, groups), self.y(z)
                if obj == "nouveaute":
                    others = [w for w in train if w != z]
                    fresh = ~np.any([self.y(w) for w in others], 0) if others else np.ones(self.n, bool)
                    X, yz = X[fresh], yz[fresh]
                Xs.append(X)
                ys.append(yz)
            Xtr, ytr = np.vstack(Xs), np.concatenate(ys)
            p = np.zeros(self.n) if len(set(ytr)) < 2 else AP.fit_predict(model, Xtr, ytr, self.X(target, train, groups))
        self.memo[key] = p
        return p

    def reference(self, target, train, obj):
        B = self.V.get(target, train)["base"][self.idx]
        if obj == "prevision":
            return B[:, 10] + 0.01 * B[:, 11]
        Xtr = np.vstack([self.V.get(z, train)["base"][self.idx][:, :10] for z in train])
        ytr = np.concatenate([self.y(z) for z in train])
        return AP._lr().fit(Xtr, ytr).predict_proba(B[:, :10])[:, 1] if len(set(ytr)) > 1 else np.zeros(self.n)

    def score(self, p, target, past, obj):
        yt, qs = self.y(target), self.qs(target)
        pos = {int(g): k for k, g in enumerate(self.idx)}
        if obj == "prevision":
            if not qs or len(set(yt)) < 2:
                return None
            sel = set(np.argsort(-p)[:max(1, int(TOP * self.n))].tolist())
            cov = float(np.mean([pos[q] in sel for q in qs]))
            return {"couverture": cov, "auc": float(roc_auc_score(yt, p)), "score": cov + 0.1 * float(roc_auc_score(yt, p))}
        seen = np.any([self.y(z) for z in past], 0) if past else np.zeros(self.n, bool)
        fr = np.where(~seen)[0]
        new = [pos[q] for q in qs if not seen[pos[q]]]
        if len(fr) < 10 or len(set(yt[fr])) < 2 or not new:
            return None
        sel = set(fr[np.argsort(-p[fr])[:max(1, int(0.25 * len(fr)))]].tolist())
        cov = float(np.mean([q in sel for q in new]))
        auc = float(roc_auc_score(yt[fr], p[fr]))
        return {"couverture": cov, "auc": auc, "score": cov + 0.1 * auc}

    def traits(self, past):
        """Ce qu'on sait du domaine avant l'année testée (rien de l'année testée)."""
        fc, ps = self.fc, np.asarray(self.fc.t.pass_sec)[self.idx]
        qn = [len(self.qs(z)) for z in past]
        rep = []
        for k, z in enumerate(past[1:], 1):
            before = np.any([self.y(w) for w in past[:k]], 0)
            q = self.qs(z)
            pos = {int(g): i for i, g in enumerate(self.idx)}
            if q:
                rep.append(np.mean([before[pos[x]] for x in q]))
        ever = np.any([self.y(z) for z in past], 0)
        secs = ps[ever]
        _, c = np.unique(secs, return_counts=True) if len(secs) else (None, np.array([1]))
        pr = c / c.sum()
        ent = float(-(pr * np.log(pr)).sum() / np.log(max(2, len(set(ps)))))
        return {"log_passages": float(np.log(self.n)), "annees_passees": len(past),
                "questions_par_an": float(np.mean(qn)), "log_questions_par_passage": float(np.log((np.mean(qn) + 1) / self.n)),
                "repetition": float(np.mean(rep)) if rep else 0.0, "part_deja_tombee": float(ever.mean()),
                "dispersion_des_chapitres": ent, "chapitres": float(len(set(ps)))}


def candidates():
    """(familles, modèle, mêlé à l'ancienne méthode ?) ; l'ancienne méthode seule est un candidat."""
    out = [((), "ancienne", False)]
    for gs, m in product(SETS, FIT_MODELS + ["melange"]):
        out += [(gs, m, False), (gs, m, True)]
    return out


def cand_pred(D, c, target, train, obj):
    gs, m, mix = c
    p = D.predict(gs, m, target, train, obj)
    if mix:
        p = (rankdata(p) + rankdata(D.predict((), "ancienne", target, train, obj))) / (2 * D.n)
    return p


def run_task(D, y, past, obj):
    """Score interne et vrai score de chaque candidat pour une tâche."""
    rows = []
    for c in candidates():
        ins = []
        for z in past:
            tr = [w for w in past if w != z]
            if len(tr) < 2:
                continue
            r = D.score(cand_pred(D, c, z, tr, obj), z, tr, obj)
            if r:
                ins.append(r["score"])
        out = D.score(cand_pred(D, c, y, past, obj), y, past, obj)
        if out is None or not ins:
            continue
        rows.append({"c": [list(c[0]), c[1], c[2]], "interne": float(np.mean(ins)), "interne_min": float(np.min(ins)), **out})
    return rows


def _fc(name):
    fc = AP._fc(name)
    return fc, TVars(fc)


_CTX = {}  # matière en cours, partagée avec les processus forkés sans copie


def _mask_tasks(k):
    """Toutes les tâches d'un domaine (ou pseudo-domaine) ; indépendant des autres domaines."""
    name, fc, V, tests = _CTX["name"], _CTX["fc"], _CTX["V"], _CTX["tests"]
    mname, mask = _CTX["masks"][k]
    D = Domain(fc, V, mask)
    out = []
    for y in tests:
        past = [z for z in fc.years if z < y]
        tr = D.traits(past)
        for obj in OBJ:
            rows = run_task(D, y, past, obj)
            if rows:
                out.append({"matiere": name, "domaine": mname, "annee": y, "objectif": obj, "traits": tr, "candidats": rows})
        print(name, mname, y, flush=True)
    return out


def stage_tasks(name, min_hist=3, seed=0):
    fc, V = _fc(name)
    secs = sorted(set(np.asarray(fc.t.pass_sec).tolist()))
    rng = np.random.default_rng(seed)
    masks = [("complet", np.ones(fc.n, bool))]
    for k in range(N_MASKS):
        keep = set(rng.choice(secs, max(2, len(secs) // 2), replace=False).tolist())
        masks.append((f"moitie_{k}", np.isin(np.asarray(fc.t.pass_sec), list(keep))))
    tests = [y for y in fc.years if len([z for z in fc.years if z < y]) >= min_hist]
    # chaque domaine sur son cœur : mêmes calculs, même ordre de sortie
    _CTX.update(name=name, fc=fc, V=V, tests=tests, masks=masks)
    tasks = [t for part in pmap(_mask_tasks, range(len(masks))) for t in part]
    (CACHE / f"transfer_tasks_{name}.json").write_text(json.dumps(tasks), encoding="utf-8")


# ---------------------------------------------------------------------------- le juge
def featurize(task, row, ref_in):
    gs, m, mix = row["c"]
    f = list(task["traits"].values())
    f += [float(task["objectif"] == "prevision")]
    f += [float(g in gs) for g in GROUPS] + [len(gs) / len(GROUPS)]
    f += [float(m == k) for k in ("ancienne", "logistique", "arbres", "melange")] + [float(mix)]
    f += [row["interne"], row["interne"] - ref_in, row["interne_min"]]
    return f


def FEATURE_NAMES(task):
    return (list(task["traits"]) + ["objectif_prevision"] + [f"famille_{g}" for g in GROUPS] + ["nb_familles"] +
            [f"modele_{k}" for k in ("ancienne", "logistique", "arbres", "melange")] + ["mele_a_l_ancienne"] +
            ["score_interne", "gain_interne", "score_interne_pire_annee"])


def _ref(task):
    return next(r for r in task["candidats"] if r["c"][1] == "ancienne")


def dataset(tasks):
    X, yg, ya = [], [], []
    for t in tasks:
        ref = _ref(t)
        for r in t["candidats"]:
            X.append(featurize(t, r, ref["interne"]))
            yg.append(r["score"] - ref["score"])
            ya.append(r["couverture"])
    return np.array(X), np.array(yg), np.array(ya)


def fit_judge(tasks):
    X, yg, ya = dataset(tasks)
    mk = lambda: ExtraTreesRegressor(n_estimators=300, min_samples_leaf=20, max_features=0.5, random_state=0, n_jobs=1)
    return {"gain": mk().fit(X, yg), "couverture": mk().fit(X, ya)}


def decide(J, task, k=3):
    """Choix du juge : les k candidats au plus fort gain prédit, mêlés ; l'ancienne méthode s'il
    n'en voit aucun qui gagne. Renvoie aussi la couverture qu'il s'attend à obtenir."""
    ref = _ref(task)
    X = np.array([featurize(task, r, ref["interne"]) for r in task["candidats"]])
    g = J["gain"].predict(X)
    order = np.argsort(-g)
    top = [i for i in order[:k] if g[i] > 0] or [next(i for i, r in enumerate(task["candidats"]) if r["c"][1] == "ancienne")]
    exp = float(np.mean(J["couverture"].predict(X[top])))
    return top, g, exp


def evaluate_choice(D, task, rows_idx):
    """Vrai score du mélange des candidats retenus (recalculé sur l'année testée)."""
    cs = [task["candidats"][i]["c"] for i in rows_idx]
    y, obj = task["annee"], task["objectif"]
    past = [z for z in D.fc.years if z < y]
    p = sum(rankdata(cand_pred(D, (tuple(gs), m, mix), y, past, obj)) for gs, m, mix in cs)
    return D.score(p, y, past, obj)


def stage_judge(names):
    warnings.filterwarnings("ignore")
    allt = {n: json.loads((CACHE / f"transfer_tasks_{n}.json").read_text(encoding="utf-8")) for n in names}
    auto = {n: json.loads((CACHE / f"autoprog_honest_{n}.json").read_text(encoding="utf-8"))
            for n in names if (CACHE / f"autoprog_honest_{n}.json").exists()}
    rep = {"principe": __doc__.split("\n\n")[0], "matieres": {}}
    for n in names:
        train = [t for m in names if m != n for t in allt[m]]  # ni la matière, ni ses pseudo-domaines
        J = fit_judge(train)
        # meilleur candidat fixe sur les autres matières (référence « règle unique »)
        gains = {}
        for t in train:
            ref = _ref(t)
            for r in t["candidats"]:
                gains.setdefault((t["objectif"], json.dumps(r["c"])), []).append(r["score"] - ref["score"])
        fc, V = _fc(n)
        D = Domain(fc, V, np.ones(fc.n, bool))
        res = {}
        for obj in OBJ:
            fixed = max((k for k in gains if k[0] == obj), key=lambda k: np.mean(gains[k]))
            rows = []
            for t in [t for t in allt[n] if t["domaine"] == "complet" and t["objectif"] == obj]:
                top, g, exp = decide(J, t)
                r = evaluate_choice(D, t, top)
                ref = _ref(t)
                fx = next(x for x in t["candidats"] if json.dumps(x["c"]) == fixed[1])
                ap = next((a for a in auto.get(n, {}).get(obj, {}).get("annees", []) if a["annee"] == t["annee"]), None)
                rows.append({"annee": t["annee"], "choix": [t["candidats"][i]["c"] for i in top],
                             "ancienne": [ref["couverture"], ref["auc"]], "regle_unique": [fx["couverture"], fx["auc"]],
                             "auto_progression": [ap["couverture"], ap["auc"]] if ap else None,
                             "juge": [r["couverture"], r["auc"]], "couverture_annoncee": exp})
                print(n, obj, t["annee"], "ancienne", ref["couverture"], "juge", round(r["couverture"], 3), "annoncé", round(exp, 3), flush=True)
            m = lambda k, i: round(float(np.mean([r[k][i] for r in rows if r[k]])), 3)
            res[obj] = {"annees": rows, **{f"{k}_{s}": m(k, i) for k in ("ancienne", "regle_unique", "auto_progression", "juge")
                                            for i, s in ((0, "couverture"), (1, "auc"))},
                        "ecart_auto_jugement": round(float(np.mean([abs(r["couverture_annoncee"] - r["juge"][0]) for r in rows])), 3),
                        "regle_unique": json.loads(fixed[1])}
        rep["matieres"][n] = res
    # juge final, appris sur tout : sert aux matières nouvelles ; et ce qu'il a appris (pistes)
    every = [t for n in names for t in allt[n]]
    J = fit_judge(every)
    fn = FEATURE_NAMES(every[0])
    imp = sorted(zip(fn, J["gain"].feature_importances_), key=lambda x: -x[1])
    rep["ce_qui_guide_le_choix"] = [[k, round(float(v), 3)] for k, v in imp[:12]]
    rep["domaines_d_entrainement"] = {n: sorted({t["domaine"] for t in allt[n]}) for n in names}
    joblib.dump({"juge": J, "noms": fn, "traits_vus": {n: allt[n][0]["traits"] for n in names},
                 "appris_sur": names}, MODEL)
    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    for n, r in rep["matieres"].items():
        print(n, {o: {k: v for k, v in x.items() if k not in ("annees", "regle_unique")} for o, x in r.items()})
    print("guide :", rep["ce_qui_guide_le_choix"][:8])


# ---------------------------------------------------------------------------- règle universelle
# Résultat du méta-entraînement : le juge appris (ci-dessus) se trompe sur une matière inconnue,
# car deux matières d'entraînement ne suffisent pas à apprendre quand changer de choix. Une seule
# règle, la même pour tous les domaines, fait mieux. Elle est choisie pour marcher partout
# (moyenne + pire domaine), jamais pour une matière précise.
RULE_OUT = AP.ROOT / "output" / "meta" / "regle.json"
DEFAULT_RULE = {"prevision": [["lexique_du_professeur"], "arbres", False],
                "nouveaute": [["lexique_du_professeur"], "melange", True]}
MARGE = 0.275  # élargit la fourchette annoncée ; calibrée sur 445 choix faits à l'aveugle (14 matières)


# Prudence du choix : « moyenne + pire domaine » devient plus frileux à chaque domaine ajouté (le
# minimum de 120 domaines est presque toujours mauvais). Le degré de prudence est donc lui aussi
# appris : celui dont la règle marche le mieux sur des matières laissées de côté (ordre = du plus
# prudent au moins prudent ; à égalité, le plus prudent).
AGGS = {"moyenne+pire": lambda g: g.mean() + g.min(),
        "moyenne+q10": lambda g: g.mean() + np.quantile(g, 0.10),
        "moyenne+q25": lambda g: g.mean() + np.quantile(g, 0.25),
        "moyenne": lambda g: g.mean()}


def _gains(tasks, obj):
    """Candidat -> domaine -> gains de score sur l'ancienne méthode."""
    rows = {}
    for t in tasks:
        if t["objectif"] != obj:
            continue
        ref = _ref(t)
        dom = (t["matiere"], t["domaine"] == "complet")
        for r in t["candidats"]:
            rows.setdefault(json.dumps(r["c"]), {}).setdefault(dom, []).append(r["score"] - ref["score"])
    return rows


def _select(tasks, obj, agg):
    rows = _gains(tasks, obj)
    doms = set.intersection(*[set(d) for d in rows.values()])
    crit = {k: AGGS[agg](np.array([np.mean(d[x]) for x in doms])) for k, d in rows.items()}
    return json.loads(max(crit, key=crit.get))


def _held_out(tasks, obj, agg):
    """Gain de score de la règle sur chaque matière, choisie sans elle (domaine complet)."""
    subs = sorted({t["matiere"] for t in tasks})
    out = []
    for n in subs:
        c = _select([t for t in tasks if t["matiere"] != n], obj, agg)
        T = [t for t in tasks if t["matiere"] == n and t["domaine"] == "complet" and t["objectif"] == obj]
        if T:
            out.append(np.mean([next(x for x in t["candidats"] if x["c"] == c)["score"] - _ref(t)["score"] for t in T]))
    return np.array(out)


def choose_agg(tasks, obj):
    if len({t["matiere"] for t in tasks}) < 4:
        return "moyenne+pire"
    sc = {a: round(float(_held_out(tasks, obj, a).mean()), 4) for a in AGGS}
    return max(AGGS, key=lambda a: sc[a])  # max garde le premier à égalité : le plus prudent


def select_rule(tasks, obj):
    """La règle, avec le degré de prudence qui généralise le mieux d'une matière à l'autre."""
    return _select(tasks, obj, choose_agg(tasks, obj))


def fourchette(interne, interne_min, marge=MARGE):
    return [max(0.0, interne_min - marge), min(1.0, 2 * interne - interne_min + marge)]


def stage_rule(names):
    """Preuve « matière inconnue » de la règle : choisie sans la matière, testée sur elle."""
    allt = {n: json.loads((CACHE / f"transfer_tasks_{n}.json").read_text(encoding="utf-8")) for n in names}
    every = [t for n in names for t in allt[n]]
    final = {o: select_rule(every, o) for o in OBJ}
    rep = {"principe": "Une seule règle pour tous les domaines, choisie pour marcher partout ; "
                       "chaque matière est testée avec la règle choisie sans elle.",
           "regle": final, "appris_sur": names, "matieres": {}}
    get = lambda t, c: next(x for x in t["candidats"] if x["c"] == c)
    for n in names:
        res = {}
        for obj in OBJ:
            c = select_rule([t for m in names if m != n for t in allt[m]], obj)
            T = [t for t in allt[n] if t["domaine"] == "complet" and t["objectif"] == obj]
            P = [t for t in allt[n] if t["domaine"] != "complet" and t["objectif"] == obj]
            mean = lambda ts, k, cc: round(float(np.mean([get(t, cc)[k] for t in ts])), 3)
            anc = [[], "ancienne", False]
            res[obj] = {"regle_sans_cette_matiere": c,
                        "avant_couverture": mean(T, "couverture", anc), "couverture": mean(T, "couverture", c),
                        "avant_auc": mean(T, "auc", anc), "auc": mean(T, "auc", c),
                        "regle_finale_couverture": mean(T, "couverture", final[obj]),
                        "pseudo_domaines": {"avant": mean(P, "couverture", anc), "apres": mean(P, "couverture", final[obj]),
                                            "n": len(P)}}
        rep["matieres"][n] = res
    hit, wid = [], []
    for t in every:
        x = get(t, final[t["objectif"]])
        lo, hi = fourchette(x["interne"], x["interne_min"])
        hit.append(lo <= x["couverture"] <= hi)
        wid.append(hi - lo)
    rep["auto_jugement"] = {"principe": "Avant de répondre, le moteur rejoue la règle sur ses propres années passées "
                                        "et annonce une fourchette de couverture.",
                            "fourchette_juste": round(float(np.mean(hit)), 3), "largeur_moyenne": round(float(np.mean(wid)), 3),
                            "taches": len(every)}
    RULE_OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print(json.dumps(rep, ensure_ascii=False, indent=1, default=float))


# ---------------------------------------------------------------------------- apprendre à apprendre
# Avec beaucoup de matières, on ne cherche plus seulement « le » bon réglage : on apprend une
# manière de se régler. Le méta-entraînement retient une courte liste de réglages robustes (ordre =
# a priori) et un seuil ; sur un domaine neuf, le moteur choisit seul dans cette liste en rejouant
# ses propres années passées, et ne quitte le premier réglage que si la preuve interne dépasse le
# seuil. Liste et seuil sont choisis en laissant de côté chaque matière d'entraînement tour à tour.
LEARN_OUT = AP.ROOT / "output" / "meta" / "apprendre.json"
KS = (1, 2, 3, 4, 6, 8)
DELTAS = (0.0, 0.02, 0.05, 0.1, 0.2)


def _dom(t):
    return (t["matiere"], t["domaine"] == "complet")


class _M:
    """Tâches d'un objectif en matrices : gain sur l'ancienne (G) et score interne (I) par candidat."""
    def __init__(self, tasks, keys=None):
        self.keys = keys or sorted({json.dumps(r["c"]) for t in tasks for r in t["candidats"]})
        ix = {k: j for j, k in enumerate(self.keys)}
        n, c = len(tasks), len(self.keys)
        self.G, self.I = np.zeros((n, c)), np.full((n, c), -np.inf)
        self.C, self.A, self.Im = np.zeros((n, c)), np.zeros((n, c)), np.zeros((n, c))
        for i, t in enumerate(tasks):
            ref = _ref(t)
            self.C[i], self.A[i] = ref["couverture"], ref["auc"]
            for r in t["candidats"]:
                j = ix[json.dumps(r["c"])]
                self.G[i, j], self.I[i, j] = r["score"] - ref["score"], r["interne"]
                self.C[i, j], self.A[i, j], self.Im[i, j] = r["couverture"], r["auc"], r["interne_min"]
        doms = sorted({_dom(t) for t in tasks})
        self.d = np.array([doms.index(_dom(t)) for t in tasks])
        self.nd = len(doms)

    def robust(self, g):
        """Moyenne des domaines + pire domaine (même critère que la règle universelle) ; g : (n,) ou (n, k)."""
        g = g.reshape(len(self.d), -1)
        m = np.stack([g[self.d == k].mean(0) for k in range(self.nd)])
        return m.mean(0) + m.min(0)

    def pick(self, short, delta):
        """Indice choisi par tâche : le meilleur interne de la liste s'il bat le premier de plus du seuil."""
        sub = self.I[:, short]
        b = np.array(short)[np.argmax(sub, 1)]
        r = np.arange(len(self.d))
        return np.where(self.I[r, b] - self.I[:, short[0]] > delta, b, short[0])

    def greedy(self, first, K, delta):
        """Liste gloutonne : chaque ajout est le réglage qui améliore le plus la politique."""
        short, r = [first], np.arange(len(self.d))
        while len(short) < K:
            sub = self.I[:, short]
            bI = sub.max(1)
            b = np.array(short)[np.argmax(sub, 1)]
            nb = np.where(self.I > bI[:, None], np.arange(self.I.shape[1])[None, :], b[:, None])
            ch = np.where(self.I[r[:, None], nb] - self.I[:, [short[0]]] > delta, nb, short[0])
            val = self.robust(self.G[r[:, None], ch])
            val[short] = -np.inf
            short.append(int(np.argmax(val)))
        return short


def _first(M):
    return int(np.argmax(M.robust(M.G)))  # = la règle universelle


def learn_policy(tasks, obj):
    """(K, seuil) choisis en laissant de côté chaque matière d'entraînement ; puis liste finale."""
    T = [t for t in tasks if t["objectif"] == obj]
    keys = sorted({json.dumps(r["c"]) for t in T for r in t["candidats"]})
    names = sorted({t["matiere"] for t in T})
    Mall = _M(T, keys)
    gains = {(K, d): np.zeros(len(T)) for K in KS for d in DELTAS}
    for m in names:
        tr = np.array([t["matiere"] != m for t in T])
        Mtr = _M([t for t, k in zip(T, tr) if k], keys)
        Mte = _M([t for t, k in zip(T, tr) if not k], keys)
        f = _first(Mtr)
        for d in DELTAS:
            sh = Mtr.greedy(f, max(KS), d)
            for K in KS:
                ch = Mte.pick(sh[:K], d)
                gains[(K, d)][~tr] = Mte.G[np.arange(len(ch)), ch]
    grid = {k: float(Mall.robust(v)[0]) for k, v in gains.items()}
    K, d = max(grid, key=lambda k: (round(grid[k], 4), -k[0], k[1]))
    sh = Mall.greedy(_first(Mall), K, d)
    return {"K": K, "seuil": d, "liste": [json.loads(keys[j]) for j in sh],
            "grille": {f"K={k[0]} seuil={k[1]}": round(v, 4) for k, v in grid.items()}}


def choose(cands, pol):
    """Production : dans la liste apprise, le moteur choisit seul d'après ses propres années passées.
    cands : {json(c): score interne}."""
    sh = [json.dumps(c) for c in pol["liste"] if json.dumps(c) in cands]
    best = max(sh, key=cands.get)
    return json.loads(best if cands[best] - cands[sh[0]] > pol["seuil"] else sh[0])


def stage_learn(names):
    """Compare, matière par matière (chaque matière absente de son propre entraînement) :
    ancienne méthode, règle universelle, juge appris, et « se régler soi-même »."""
    warnings.filterwarnings("ignore")
    allt = {n: json.loads((CACHE / f"transfer_tasks_{n}.json").read_text(encoding="utf-8")) for n in names}
    for n in names:
        for t in allt[n]:
            t["matiere"] = n
    every = [t for n in names for t in allt[n]]
    meth = ("ancienne", "regle", "juge", "se_regler")
    rep = {"principe": "Chaque matière est traitée comme un domaine inconnu : tout ce qui est appris "
                       "(règle, juge, liste de réglages, seuil) l'est sans elle.", "matieres": {}}
    blind = {m: [] for m in meth}  # (interne, interne_min, vraie couverture) des choix faits à l'aveugle
    for n in names:
        tr = [t for t in every if t["matiere"] != n]
        J = fit_judge(tr)
        res = {}
        for obj in OBJ:
            Ttr = [t for t in tr if t["objectif"] == obj]
            keys = sorted({json.dumps(r["c"]) for t in Ttr for r in t["candidats"]})
            Mtr = _M(Ttr, keys)
            pol = learn_policy(tr, obj)
            sh = [keys.index(json.dumps(c)) for c in pol["liste"]]
            te = [t for t in allt[n] if t["objectif"] == obj]
            Mte = _M(te, keys)
            jsel = []
            for t in te:
                ref = _ref(t)
                X = np.array([featurize(t, r, ref["interne"]) for r in t["candidats"]])
                g = J["gain"].predict(X)
                c = t["candidats"][int(np.argmax(g))]["c"] if g.max() > 0 else ref["c"]
                jsel.append(keys.index(json.dumps(c)))
            ri = np.arange(len(te))
            sel = {"ancienne": np.full(len(te), keys.index(json.dumps(_ref(te[0])["c"]))),
                   "regle": np.full(len(te), keys.index(json.dumps(select_rule(Ttr, obj)))), "juge": np.array(jsel),
                   "se_regler": Mte.pick(sh, pol["seuil"])}
            full = np.array([t["domaine"] == "complet" for t in te])
            for m, s_ in sel.items():
                blind[m] += list(zip(Mte.I[ri, s_], Mte.Im[ri, s_], Mte.C[ri, s_]))
            f = lambda v: round(float(np.mean(v)), 3) if len(v) else None
            res[obj] = {m: {"couverture": f(Mte.C[ri, s][full]), "auc": f(Mte.A[ri, s][full]),
                            "gain": f(Mte.G[ri, s][full]), "pseudo_gain": f(Mte.G[ri, s][~full])}
                        for m, s in sel.items()}
            res[obj]["politique"] = {"K": pol["K"], "seuil": pol["seuil"], "liste": pol["liste"]}
            print(n, obj, {m: (res[obj][m]["couverture"], res[obj][m]["gain"], res[obj][m]["pseudo_gain"]) for m in meth}, flush=True)
        rep["matieres"][n] = res
    summ = {}
    for obj in OBJ:
        summ[obj] = {}
        for m in meth:
            v = lambda k: [rep["matieres"][n][obj][m][k] for n in names]
            g = v("gain")
            summ[obj][m] = {"gain_moyen": round(float(np.mean(g)), 4), "pire_matiere": round(float(min(g)), 4),
                            "matieres_gagnees": int(sum(x > 0.005 for x in g)),
                            "matieres_perdues": int(sum(x < -0.005 for x in g)),
                            "pseudo_gain_moyen": round(float(np.mean(v("pseudo_gain"))), 4),
                            "couverture_moyenne": round(float(np.mean(v("couverture"))), 3),
                            "auc_moyenne": round(float(np.mean(v("auc"))), 3)}
    rep["synthese"] = summ
    rep["politique_finale"] = {obj: learn_policy(every, obj) for obj in OBJ}
    # adoption : la stratégie de production est celle qui gagne en moyenne ET dans la pire matière
    # (le juge, trop dépendant des matières vues, n'est retenu que comme témoin)
    rep["adoptee"] = {}
    for obj in OBJ:
        agg = choose_agg(every, obj)  # même prudence que celle apprise pour la règle
        gm = lambda m: np.array([rep["matieres"][n][obj][m]["gain"] for n in names])
        crit = {m: float(AGGS[agg](gm(m))) for m in ("ancienne", "regle", "se_regler")}
        win = max(crit, key=lambda m: (round(crit[m], 4), m == "regle"))
        pf = rep["politique_finale"][obj]
        liste = {"ancienne": [[[], "ancienne", False]], "regle": [select_rule(every, obj)], "se_regler": pf["liste"]}[win]
        rep["adoptee"][obj] = {"strategie": win, "liste": liste, "seuil": pf["seuil"] if win == "se_regler" else 0.0,
                               "prudence": agg, "critere": {m: round(v, 4) for m, v in crit.items()}}
    # auto-jugement : la plus petite marge dont la fourchette contient le vrai résultat ≥ 85 % du temps
    rep["auto_jugement"] = {}
    for m in meth:
        b = np.array(blind[m])
        cal = {}
        for mg in np.arange(0.0, 0.41, 0.025):
            lo, hi = np.maximum(0, b[:, 1] - mg), np.minimum(1, 2 * b[:, 0] - b[:, 1] + mg)
            cal[round(float(mg), 3)] = (float(np.mean((lo <= b[:, 2]) & (b[:, 2] <= hi))), float(np.mean(hi - lo)))
        mg = min([k for k, v in cal.items() if v[0] >= 0.85] or [max(cal)])
        rep["auto_jugement"][m] = {"marge": mg, "fourchette_juste": round(cal[mg][0], 3),
                                   "largeur_moyenne": round(cal[mg][1], 3), "taches": len(b)}
    for obj in OBJ:
        rep["adoptee"][obj]["marge"] = rep["auto_jugement"][rep["adoptee"][obj]["strategie"]]["marge"]
    rep["appris_sur"] = names
    LEARN_OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print(json.dumps({"synthese": summ, "adoptee": rep["adoptee"], "auto_jugement": rep["auto_jugement"], "politique_finale": {o: {k: v for k, v in p.items() if k != "grille"}
                                                              for o, p in rep["politique_finale"].items()}},
                     ensure_ascii=False, indent=1))


def _replay(D, c, ys, obj):
    ins = []
    for z in ys:  # auto-jugement : le réglage rejoué sur ses propres années (même calcul qu'à la calibration)
        tr = [w for w in ys if w != z]
        if len(tr) >= 2:
            r = D.score(cand_pred(D, c, z, tr, obj), z, tr, obj)
            if r:
                ins.append(r["score"])
    return ins


def apply(fc, log=print) -> dict:
    """Production, aucun choix propre à la matière : le moteur rejoue sur ses années passées les
    réglages de la liste apprise (méta-entraînement multi-matières) et choisit seul ; sans liste,
    la règle universelle."""
    pol = json.loads(LEARN_OUT.read_text(encoding="utf-8")).get("adoptee", {}) if LEARN_OUT.exists() else {}
    rule = json.loads(RULE_OUT.read_text(encoding="utf-8"))["regle"] if RULE_OUT.exists() else DEFAULT_RULE
    D = Domain(fc, TVars(fc), np.ones(fc.n, bool))
    nxt, ys = fc.years[-1] + 1, list(fc.years)
    out = {}
    for obj in OBJ:
        liste = pol[obj]["liste"] if obj in pol else [rule[obj]]
        rej = {json.dumps(c): _replay(D, (tuple(c[0]), c[1], c[2]), ys, obj) for c in liste}
        rej = {k: v for k, v in rej.items() if v}
        if rej:
            c = choose({k: float(np.mean(v)) for k, v in rej.items()},
                       pol.get(obj, {"liste": liste, "seuil": 0.0})) if obj in pol else liste[0]
            ins = rej[json.dumps(c)]
        else:
            c, ins = liste[0], []
        gs, m, mix = c
        f = fourchette(float(np.mean(ins)), float(np.min(ins)), pol.get(obj, {}).get("marge", MARGE)) if ins else None
        out[obj] = {"familles": gs, "modele": m, "mele_a_l_ancienne": mix,
                    "essayes": {k: round(float(np.mean(v)), 3) for k, v in rej.items()},
                    "score_rejoue": [round(v, 3) for v in ins], "fourchette": f,
                    "p": cand_pred(D, (tuple(gs), m, mix), nxt, ys, obj)}
        log(f"  réglage choisi seul ({obj}, parmi {len(liste)}) : {gs} / {m}{' + ancienne' if mix else ''}, fourchette {f}")
    return out


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    st, names = sys.argv[1], sys.argv[2:] or ["droit", "nsi", "eco"]
    if st == "tasks":
        for n in names:
            stage_tasks(n)
    elif st == "judge":
        stage_judge(names)
    elif st == "learn":
        stage_learn(names)
    else:
        stage_rule(names)
