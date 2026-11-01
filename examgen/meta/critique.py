"""Autocritique méta-apprise : le moteur examine ses propres ratés et cherche seul quoi changer.

Rien n'est écrit pour une matière. Le point de départ est la stratégie actuelle (règle apprise sur
plusieurs matières). Puis, à chaque tour :

1. Autocritique. Sur les matières d'entraînement, le moteur relève les questions tombées qu'il
   n'avait pas retenues et cherche ce qui les aurait attrapées :
   - « rattrapage » : la part de ces ratés que chaque autre réglage (famille de variables × modèle)
     plaçait dans sa propre sélection ;
   - « chapitres oubliés » : les ratés sont-ils surreprésentés dans les chapitres où il n'a rien
     retenu ? Si oui, sa sélection est trop concentrée ; si non et qu'il diversifie déjà, trop dispersée.
2. Remèdes. De ce diagnostic seulement naissent des propositions : mêler un peu (ou beaucoup) d'un
   réglage qui rattrape ; diversifier davantage ou moins les chapitres retenus.
3. Preuve. Une proposition n'est gardée que si elle améliore le critère prudent appris (moyenne et
   bas de la distribution des gains par domaine). Sinon le moteur s'arrête : il ne change pas pour
   changer.

Toute la recherche est refaite sans la matière testée (validation « matière exclue »), puis la
stratégie trouvée est appliquée à elle. Elle n'est adoptée en production que si elle bat la
stratégie actuelle selon ce même critère.

Auto-jugement appris : au lieu d'une marge fixe, un méta-modèle prédit, à partir des traits du
domaine et de ce que donne le rejeu sur les années passées, la couverture attendue et l'erreur
probable ; la largeur de la fourchette est calibrée pour contenir le vrai résultat 85 % du temps
(calibration elle aussi faite sans la matière testée).

    python -m examgen.meta.critique droit nsi eco ...
"""
from __future__ import annotations

import json
import sys
import warnings

import joblib
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor

from . import transfer as TR
from ..fast import auc, pmap

OUT = TR.AP.ROOT / "output" / "meta" / "critique.json"
JUGE = TR.AP.ROOT / "output" / "meta" / "critique_juge.joblib"
BASE = TR.BASE
IX = {(tuple(gs), m): j for j, (gs, m) in enumerate(BASE)}
WEIGHTS = (0.25, 0.5, 1.0)  # part du réglage ajouté, relative au mélange courant
LAMBDAS = (0.0, 0.1, 0.25, 0.5, 1.0)  # diversification des chapitres (0 = aucune)
N_PROP = 6  # réglages « rattrapeurs » essayés à chaque tour
EPS = 0.002  # gain minimal pour accepter un changement
STEPS = 6
CIBLE = 0.85  # part des fourchettes qui doivent contenir le vrai résultat


# ---------------------------------------------------------------------------- données
def load(names):
    out = []
    for n in names:
        T = json.loads((TR.CACHE / f"transfer_tasks_{n}.json").read_text(encoding="utf-8"))
        E = joblib.load(TR.CACHE / f"critique_preds_{n}.joblib")
        for t, e in zip(T, E):
            t["matiere"], t["sec"], t["ev"] = n, np.unique(e["sec"], return_inverse=True)[1], e["ev"]
            out.append(t)
    return out


def weights_of(c):
    """Un candidat de transfer.py écrit comme mélange de rangs des réglages de base."""
    gs, m, mix = c
    w = np.zeros(len(BASE))
    if m == "melange":
        w[IX[(tuple(gs), "logistique")]] += 0.5
        w[IX[(tuple(gs), "arbres")]] += 0.5
    else:
        w[IX[(tuple(gs), m)] if m != "ancienne" else 0] += 1.0
    if mix:
        w = 0.5 * w / w.sum()
        w[0] += 0.5
    return w / w.sum()


# ---------------------------------------------------------------------------- noter
def _diversify(p, sec, lam):
    """Rabote le score des passages d'un chapitre déjà bien servi : p / (1 + k)^λ, k = nombre de
    passages du même chapitre mieux classés."""
    if lam == 0:
        return p
    o = np.argsort(-p, kind="stable")
    s = sec[o]
    g = np.argsort(s, kind="stable")
    first = np.r_[0, np.flatnonzero(np.diff(s[g])) + 1]
    k = np.empty(len(p))
    k[g] = np.arange(len(p)) - np.repeat(first, np.diff(np.r_[first, len(p)]))
    out = np.empty(len(p))
    out[o] = p[o] / (1.0 + k) ** lam
    return out


def judge(p, e, sec, obj, lam=0.0):
    """Même notation que transfer.Domain.score ; renvoie aussi ce qu'il faut pour l'autocritique."""
    y, q, seen = e["y"], e["q"], e["seen"]
    pool = ~seen if obj == "nouveaute" else np.ones(len(p), bool)
    qq = q[pool[q]]
    if not len(qq) or len(set(y[pool])) < 2 or (obj == "nouveaute" and pool.sum() < 10):
        return None
    ix = np.flatnonzero(pool)
    pp = _diversify(p[ix], sec[ix], lam)
    k = max(1, int((TR.TOP if obj == "prevision" else 0.25) * len(ix)))
    sel = np.zeros(len(p), bool)
    sel[ix[np.argsort(-pp, kind="stable")[:k]]] = True
    cov = float(sel[qq].mean())
    a = auc(y[ix], pp)
    return {"couverture": cov, "auc": a, "score": cov + 0.1 * a, "sel": sel, "rates": qq[~sel[qq]], "pool": pool, "k": k}


def blend(w, P):
    return w @ P


class Bench:
    """Tâches d'un objectif, prêtes à noter vite n'importe quelle stratégie (w, λ)."""

    def __init__(self, tasks, obj):
        self.T = [t for t in tasks if t["objectif"] == obj and judge(t["ev"][0]["P"][0], t["ev"][0], t["sec"], obj)]
        self.obj = obj
        doms = sorted({(t["matiere"], t["domaine"] == "complet") for t in self.T})
        self.d = np.array([doms.index((t["matiere"], t["domaine"] == "complet")) for t in self.T])
        self.nd = len(doms)
        self.ref = np.array([judge(t["ev"][0]["P"][0], t["ev"][0], t["sec"], obj)["score"] for t in self.T])

    def run(self, st, i):
        t = self.T[i]
        return judge(blend(st[0], t["ev"][0]["P"]), t["ev"][0], t["sec"], self.obj, st[1])

    def gains(self, st):
        return np.array([self.run(st, i)["score"] for i in range(len(self.T))]) - self.ref

    def dom_mean(self, v):
        return np.array([v[self.d == k].mean() for k in range(self.nd)])

    def value(self, st, agg):
        return float(TR.AGGS[agg](self.dom_mean(self.gains(st))))


# ---------------------------------------------------------------------------- autocritique
def critique(B, st):
    """Ce que le moteur se reproche, mesuré sur ses ratés."""
    resc, over = np.zeros((len(B.T), len(BASE))), np.zeros(len(B.T))
    for i, t in enumerate(B.T):
        r = B.run(st, i)
        miss = r["rates"]
        if not len(miss):
            continue
        e = t["ev"][0]
        ix = np.flatnonzero(r["pool"])
        for j in range(len(BASE)):  # le réglage j aurait-il retenu ces ratés ?
            sj = np.zeros(len(r["pool"]), bool)
            sj[ix[np.argsort(-e["P"][j][ix], kind="stable")[:r["k"]]]] = True
            resc[i, j] = sj[miss].mean()
        sec = t["sec"]
        empty = ~np.isin(sec, np.unique(sec[r["sel"]]))  # chapitres où rien n'est retenu
        rest = r["pool"] & ~r["sel"]
        over[i] = empty[miss].mean() / max(1e-9, empty[rest].mean()) if empty[rest].any() else 1.0
    return {"_resc": np.array([B.dom_mean(resc[:, j]).mean() for j in range(len(BASE))]),
            "chapitres_oublies": float(B.dom_mean(over).mean())}


def proposals(st, diag):
    w, lam = st
    out = []
    for j in np.argsort(-diag["_resc"])[:N_PROP]:
        for a in WEIGHTS:
            nw = w + a * np.eye(len(BASE))[j]
            out.append(((nw / nw.sum(), lam), f"mêler {name(j)} (part {a:g})"))
    li = LAMBDAS.index(lam)
    if diag["chapitres_oublies"] > 1 and li + 1 < len(LAMBDAS):
        out.append(((w, LAMBDAS[li + 1]), f"diversifier les chapitres (λ={LAMBDAS[li + 1]})"))
    if diag["chapitres_oublies"] < 1 and li > 0:
        out.append(((w, LAMBDAS[li - 1]), f"moins diversifier (λ={LAMBDAS[li - 1]})"))
    return out


def name(j):
    gs, m = BASE[j]
    return "ancienne méthode" if m == "ancienne" else f"{'+'.join(gs) or 'base'}/{m}"


def describe(st):
    w, lam = st
    return {"melange": {name(j): round(float(w[j]), 3) for j in np.flatnonzero(w > 1e-9)}, "diversification": lam}


def search(tasks, obj, agg, start, log=None):
    B = Bench(tasks, obj)
    st = (weights_of(start), 0.0)
    cur = B.value(st, agg)
    journal = [{"etat": describe(st), "valeur": round(cur, 4)}]
    for _ in range(STEPS):
        diag = critique(B, st)
        props = proposals(st, diag)
        vals = [B.value(s, agg) for s, _ in props]
        b = int(np.argmax(vals))
        entry = {"chapitres_oublies": round(diag["chapitres_oublies"], 3),
                 "rattrapeurs": [[name(j), round(float(diag["_resc"][j]), 3)] for j in np.argsort(-diag["_resc"])[:3]],
                 "meilleure_proposition": props[b][1], "valeur_proposee": round(vals[b], 4)}
        if vals[b] - cur <= EPS:
            entry["decision"] = "refusée : pas de gain prouvé, arrêt"
            journal.append(entry)
            break
        st, cur = props[b][0], vals[b]
        entry["decision"] = "acceptée"
        journal.append(entry)
        if log:
            log(f"  {obj} : {props[b][1]} -> {cur:.4f}")
    return st, journal


# ---------------------------------------------------------------------------- auto-jugement appris
def replay_scores(t, st, obj):
    out = []
    for e in t["ev"][1:]:
        r = judge(blend(st[0], e["P"]), e, t["sec"], obj, st[1])
        if r:
            out.append(r["score"])
    return out


def jfeat(traits, ins, obj):
    ins = np.asarray(ins) if len(ins) else np.zeros(1)
    return list(traits.values()) + [float(obj == "prevision"), ins.mean(), ins.min(), ins.max(), ins.std(), len(ins)]


def _et(leaf=15):
    return ExtraTreesRegressor(n_estimators=150, min_samples_leaf=leaf, max_features=0.6, random_state=0, n_jobs=-1)


def fit_interval(X, y):
    """Centre et erreur typique appris ; le facteur k est calibré à part."""
    m = _et().fit(X, y)
    # erreur typique apprise sur des résidus hors échantillon (sinon trop optimiste)
    res = np.zeros(len(y))
    for f in range(5):
        tr = np.arange(len(y)) % 5 != f
        res[~tr] = np.abs(y[~tr] - _et().fit(X[tr], y[tr]).predict(X[~tr]))
    s = _et(25).fit(X, res)
    return {"centre": m, "erreur": s}


def interval(J, X, k):
    c, s = J["centre"].predict(X), np.maximum(J["erreur"].predict(X), 0.01)
    return np.clip(c - k * s, 0, 1), np.clip(c + k * s, 0, 1)


# ---------------------------------------------------------------------------- validation
_CTX = {}


def _fold(n):
    tasks, every_obj = _CTX["tasks"], _CTX["objs"]
    tr = [t for t in tasks if t["matiere"] != n]
    res = {}
    for obj in every_obj:
        agg = TR.choose_agg(tr, obj)
        cur = TR.select_rule(tr, obj)
        st, jr = search(tr, obj, agg, cur)
        te = Bench([t for t in tasks if t["matiere"] == n], obj)
        full = np.array([t["domaine"] == "complet" for t in te.T])
        R = {m: [te.run(s, i) for i in range(len(te.T))] for m, s in
             (("ancienne", (weights_of([[], "ancienne", False]), 0.0)), ("regle", (weights_of(cur), 0.0)), ("critique", st))}
        f = lambda v: round(float(np.mean(v)), 4) if len(v) else None
        res[obj] = {m: {"couverture": f([r["couverture"] for r, k in zip(R[m], full) if k]),
                        "auc": f([r["auc"] for r, k in zip(R[m], full) if k]),
                        "gain": f([r["score"] - a["score"] for r, a, k in zip(R[m], R["ancienne"], full) if k]),
                        "pseudo_gain": f([r["score"] - a["score"] for r, a, k in zip(R[m], R["ancienne"], full) if not k])}
                    for m in R}
        res[obj]["strategie_trouvee"] = describe(st)
        res[obj]["prudence"] = agg
        res[obj]["tours_acceptes"] = sum(e.get("decision") == "acceptée" for e in jr)
        # pour l'auto-jugement : choix fait à l'aveugle, ce que dit le rejeu, résultat réel
        res[obj]["_aveugle"] = [(t["traits"], replay_scores(t, st, obj), r["couverture"])
                                for t, r in zip(te.T, R["critique"])]
        print(n, obj, {m: (res[obj][m]["couverture"], res[obj][m]["gain"]) for m in R}, describe(st), flush=True)
    return n, res


def main(names):
    warnings.filterwarnings("ignore")
    tasks = load(names)
    _CTX.update(tasks=tasks, objs=TR.OBJ)
    folds = dict(pmap(_fold, names))
    rep = {"principe": __doc__.split("\n\n")[0] + " " + __doc__.split("\n\n")[1].split("\n")[0],
           "appris_sur": names, "matieres": {}, "synthese": {}, "adoptee": {}, "journal": {}}
    blind = {}
    for n in names:
        rep["matieres"][n] = {o: {k: v for k, v in folds[n][o].items() if k != "_aveugle"} for o in TR.OBJ}
        for o in TR.OBJ:
            blind.setdefault(o, []).extend([(n, *x) for x in folds[n][o]["_aveugle"]])
    for obj in TR.OBJ:
        agg = TR.choose_agg(tasks, obj)
        S = {}
        for m in ("ancienne", "regle", "critique"):
            g = np.array([rep["matieres"][n][obj][m]["gain"] for n in names])
            S[m] = {"gain_moyen": round(float(g.mean()), 4), "pire_matiere": round(float(g.min()), 4),
                    "matieres_gagnees": int((g > 0.005).sum()), "matieres_perdues": int((g < -0.005).sum()),
                    "couverture_moyenne": round(float(np.mean([rep["matieres"][n][obj][m]["couverture"] for n in names])), 3),
                    "auc_moyenne": round(float(np.mean([rep["matieres"][n][obj][m]["auc"] for n in names])), 3),
                    "critere": round(float(TR.AGGS[agg](g)), 4)}
        rep["synthese"][obj] = S
        st, jr = search(tasks, obj, agg, TR.select_rule(tasks, obj), log=print)
        rep["journal"][obj] = jr
        win = "critique" if S["critique"]["critere"] > S["regle"]["critere"] + 1e-4 else "regle"
        rep["adoptee"][obj] = {"strategie": win, "prudence": agg,
                               **(describe(st) if win == "critique" else {"regle": TR.select_rule(tasks, obj)}),
                               "poids": st[0].round(6).tolist() if win == "critique" else None}
    # ---- auto-jugement : fourchette apprise vs fourchette à marge fixe, toutes deux matière exclue
    aj, X, Y, G = {}, [], [], []
    for obj in TR.OBJ:
        for n, tr_, ins, cov in blind[obj]:
            X.append(jfeat(tr_, ins, obj))
            Y.append(cov)
            G.append(n)
    X, Y, G = np.array(X), np.array(Y), np.array(G)
    lo_l, hi_l, lo_f, hi_f = (np.zeros(len(Y)) for _ in range(4))
    for n in names:
        tr, te = G != n, G == n
        J = fit_interval(X[tr], Y[tr])
        k = calib_k_oof(X[tr], Y[tr], G[tr])  # calibré sans la matière testée
        lo_l[te], hi_l[te] = interval(J, X[te], k)
        # marge fixe calibrée de la même façon (sans la matière)
        im, imn = X[:, -5], X[:, -4]
        for mg in np.arange(0, 0.61, 0.025):
            lo, hi = np.maximum(0, imn - mg), np.minimum(1, 2 * im - imn + mg)
            if np.mean(((lo <= Y) & (Y <= hi))[tr]) >= CIBLE:
                break
        lo_f[te], hi_f[te] = lo[te], hi[te]
    for m, lo, hi in (("marge_fixe", lo_f, hi_f), ("appris", lo_l, hi_l)):
        aj[m] = {"fourchette_juste": round(float(np.mean((lo <= Y) & (Y <= hi))), 3),
                 "largeur_moyenne": round(float(np.mean(hi - lo)), 3), "taches": int(len(Y))}
    J = fit_interval(X, Y)
    k = calib_k_oof(X, Y, G)
    aj["k"] = round(k, 3)
    joblib.dump({"juge": J, "k": k}, JUGE, compress=3)
    ok = aj["appris"]["fourchette_juste"] >= CIBLE - 0.02 and aj["appris"]["largeur_moyenne"] < aj["marge_fixe"]["largeur_moyenne"]
    aj["adopte"] = "appris" if ok else "marge_fixe"
    rep["auto_jugement"] = aj
    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print(json.dumps({"synthese": rep["synthese"], "adoptee": {o: {k: v for k, v in a.items() if k != "poids"}
                                                               for o, a in rep["adoptee"].items()},
                      "auto_jugement": aj}, ensure_ascii=False, indent=1))


def calib_k_oof(X, Y, G, groups=5):
    """k : calibré sur des prédictions hors matière (matières réparties en quelques paquets,
    chaque paquet prédit par un juge appris sans lui)."""
    subs = sorted(set(G))
    if len(subs) < 2:
        return 2.0
    pk = {n: i % groups for i, n in enumerate(subs)}
    g = np.array([pk[n] for n in G])
    C, S = np.zeros(len(Y)), np.zeros(len(Y))
    for f in range(min(groups, len(subs))):
        J = fit_interval(X[g != f], Y[g != f])
        C[g == f] = J["centre"].predict(X[g == f])
        S[g == f] = np.maximum(J["erreur"].predict(X[g == f]), 0.01)
    for k in np.arange(0.25, 6.01, 0.05):
        if np.mean(np.abs(Y - C) <= k * S) >= CIBLE:
            return float(k)
    return 6.0


if __name__ == "__main__":
    main(sys.argv[1:])
