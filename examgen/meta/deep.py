"""Variables d'intention à grande échelle : « qu'est-ce qui fait qu'un passage du cours tombe ? »

  1. expansion combinatoire : les 12 variables de base d'un passage (place, longueur, centralité,
     insistance, historique...) sont déclinées en vues invariantes d'échelle (z-score et rang dans
     l'année, haut du classement, carré) puis croisées deux à deux (produits, écarts, maximum).
     Plusieurs centaines de variables, aucune écrite à la main pour une matière ;
  2. sélection par stabilité : un modèle parcimonieux (L1) est réappris sur 40 sous-échantillons ;
     on ne garde que les variables choisies dans au moins 60 % des cas (le bruit, lui, change) ;
  3. preuves : année exclue dans la matière, et transfert à froid (appris sur une matière,
     appliqué tel quel à l'autre), comparés aux 12 variables de base et à la simple popularité.
"""
from __future__ import annotations

import itertools

import numpy as np
from scipy.stats import rankdata
from sklearn.linear_model import LogisticRegression
from ..fast import auc as roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

SHORT = {"rang_du_passage_dans_la_section": "rang", "longueur_du_passage": "longueur", "centralite_du_passage": "centralite",
         "redondance_du_passage": "redondance", "insistance_typographique": "insistance", "passage_avec_reference": "reference",
         "densite_symboles_du_passage": "symboles", "place_de_la_section_dans_le_cours": "place_section",
         "taille_de_la_section": "taille_section", "centralite_de_la_section": "centralite_section",
         "frequence_passee_du_passage": "deja_tombe", "frequence_passee_de_la_section": "section_deja_tombee"}


def expand(X: np.ndarray, g: np.ndarray, names: list[str]) -> tuple[np.ndarray, list[str]]:
    """Vues calculées dans chaque année (groupe) : invariantes à l'échelle propre à une matière."""
    nm = [SHORT.get(n, n) for n in names]
    Z = np.zeros_like(X, float)
    R = np.zeros_like(X, float)
    for y in np.unique(g):
        m = g == y
        Z[m] = (X[m] - X[m].mean(0)) / (X[m].std(0) + 1e-9)
        R[m] = np.column_stack([(rankdata(X[m, j]) - 1) / max(m.sum() - 1, 1) for j in range(X.shape[1])])
    cols, out = [], []
    for j, n in enumerate(nm):
        cols += [Z[:, j], R[:, j], (R[:, j] > 0.9).astype(float), Z[:, j] ** 2]
        out += [f"{n}", f"rang({n})", f"haut({n})", f"extreme({n})"]
    for i, j in itertools.combinations(range(len(nm)), 2):
        a, b = nm[i], nm[j]
        cols += [Z[:, i] * Z[:, j], R[:, i] * R[:, j], np.abs(R[:, i] - R[:, j]), np.maximum(R[:, i], R[:, j])]
        out += [f"{a}×{b}", f"rang({a})×rang({b})", f"ecart({a},{b})", f"max({a},{b})"]
    return np.column_stack(cols), out


def _lr(C=0.3):
    return make_pipeline(StandardScaler(), LogisticRegression(C=C, max_iter=3000, class_weight="balanced"))


def stability(X, y, n: int = 40, frac: float = 0.5, C: float = 0.02, thr: float = 0.6, seed: int = 0):
    rng = np.random.default_rng(seed)
    cnt = np.zeros(X.shape[1])
    Xs = StandardScaler().fit_transform(X)
    for _ in range(n):
        idx = rng.choice(len(y), int(frac * len(y)), replace=False)
        m = LogisticRegression(penalty="l1", C=C, solver="liblinear", class_weight="balanced").fit(Xs[idx], y[idx])
        cnt += m.coef_[0] != 0
    f = cnt / n
    return np.where(f >= thr)[0], f


def _auc_by_group(m, X, y, g):
    s = [roc_auc_score(y[g == k], m.predict_proba(X[g == k])[:, 1]) for k in np.unique(g) if len(set(y[g == k])) > 1]
    return float(np.mean(s))


def year_out(X, y, g, select: bool):
    """Année exclue ; la sélection par stabilité est refaite sans l'année testée."""
    sc = []
    for k in np.unique(g):
        tr, te = g != k, g == k
        if len(set(y[te])) < 2:
            continue
        cols = stability(X[tr], y[tr])[0] if select else np.arange(X.shape[1])
        if len(cols) == 0:
            cols = np.arange(X.shape[1])
        m = _lr().fit(X[tr][:, cols], y[tr])
        sc.append(roc_auc_score(y[te], m.predict_proba(X[te][:, cols])[:, 1]))
    return round(float(np.mean(sc)), 3)


def study(data: dict) -> dict:
    """data : matière -> (X_base, y, groupes, noms). Rapport par matière + transfert à froid."""
    E = {n: expand(X, g, nm) for n, (X, y, g, nm) in data.items()}
    rep = {"variables_generees": len(next(iter(E.values()))[1]), "par_matiere": {}, "transfert_a_froid": {}}
    stable = {}
    for n, (X, y, g, nm) in data.items():
        XE, en = E[n]
        cols, f = stability(XE, y)
        stable[n] = (cols, f)
        m = _lr().fit(XE[:, cols], y)
        coef = m[-1].coef_[0]
        rep["par_matiere"][n] = {
            "auc_annee_exclue_popularite": round(float(np.mean([roc_auc_score(y[g == k], X[g == k, -2]) for k in np.unique(g)
                                                                  if len(set(y[g == k])) > 1])), 3),
            "auc_annee_exclue_12_variables": year_out(X, y, g, select=False),
            "auc_annee_exclue_variables_stables": year_out(XE, y, g, select=True),
            "variables_stables": len(cols),
            "variables_par_matiere_rejetees": int(XE.shape[1] - len(cols)),
            "regles": [{"variable": en[c], "frequence": round(float(f[c]), 2), "sens": "+" if w > 0 else "-"}
                       for c, w in sorted(zip(cols, coef), key=lambda r: -abs(r[1]))][:12]}
    names = list(data)
    for a, b in itertools.permutations(names, 2):
        XA, yA, gA = E[a][0], data[a][1], data[a][2]
        XB, yB, gB = E[b][0], data[b][1], data[b][2]
        ca = stable[a][0]
        Zb = np.zeros_like(data[b][0], float)  # 12 variables : mises à l'échelle par année aussi, pour être juste
        Za = np.zeros_like(data[a][0], float)
        for Zx, (Xx, gx) in ((Za, (data[a][0], gA)), (Zb, (data[b][0], gB))):
            for k in np.unique(gx):
                mm = gx == k
                Zx[mm] = (Xx[mm] - Xx[mm].mean(0)) / (Xx[mm].std(0) + 1e-9)
        base = _lr().fit(Za, yA)
        deep = _lr().fit(XA[:, ca], yA)
        both = sorted(set(stable[a][0]) & set(stable[b][0]))
        rep["transfert_a_froid"][f"{a}->{b}"] = {
            "auc_12_variables": round(_auc_by_group(base, Zb, yB, gB), 3),
            "auc_variables_stables": round(_auc_by_group(deep, XB[:, ca], yB, gB), 3),
            "auc_appris_dans_la_matiere": rep["par_matiere"][b]["auc_annee_exclue_variables_stables"]}
    for n, r in rep["par_matiere"].items():  # choix fait par la matière elle-même, sur ses années passées
        r["modele_retenu"] = "variables stables" if r["auc_annee_exclue_variables_stables"] > r["auc_annee_exclue_12_variables"] else "12 variables"
        r["auc_modele_retenu"] = max(r["auc_annee_exclue_variables_stables"], r["auc_annee_exclue_12_variables"])
    common = sorted(set(stable[names[0]][0]).intersection(*[set(stable[n][0]) for n in names[1:]])) if len(names) > 1 else []
    en = next(iter(E.values()))[1]
    rep["regles_universelles"] = [en[c] for c in common]
    return rep
