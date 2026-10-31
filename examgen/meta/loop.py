"""Boucle complète sur une matière inconnue : rien que ses anciens sujets et son cours.

Chaque génération :
  1. le moteur relie les questions au cours (version actuelle) ;
  2. il découvre les variables PROPRES à la matière dans le cours lui-même : des thèmes (NMF sur
     les mots des passages) et des formes (NMF sur les suites de caractères : code, dates,
     formules...), nommés par leurs mots les plus forts ;
  3. il apprend « quel passage tombe quelle année » sur les autres années, avec plusieurs
     familles de modèles (logistique sur les 12 variables génériques, arbres boostés sur les
     12, arbres boostés sur génériques + propres à la matière + croisements) ; il choisit la
     famille lui-même, par validation emboîtée sur ses propres années passées ;
  4. ce qu'il a compris des intentions (probabilité qu'une section tombe cette année-là, prédite
     sans cette année) devient un a priori qui corrige l'alignement : version suivante ;
  5. garde-fou sans étiquette : diversité du cours conservée, arrêt à la convergence.
Aucune règle n'est apprise sur une autre matière : seule la procédure est commune.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import spearmanr
from sklearn.decomposition import NMF
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import roc_auc_score

from . import align as A, deep as DP, selftrain as ST
from .intent import Intent

PRIOR = 0.5  # poids de l'a priori d'intention dans l'alignement (même valeur pour toute matière)


def course_variables(pass_text: list[str], k_words: int = 12, k_form: int = 6):
    out, names = [], []
    for k, kw, tag in ((k_words, dict(token_pattern=r"(?u)\b[^\W\d_]{3,}\b"), "theme"),
                       (k_form, dict(analyzer="char_wb", ngram_range=(2, 4)), "forme")):
        v = TfidfVectorizer(sublinear_tf=True, strip_accents="unicode", min_df=2, max_df=0.5, **kw)
        X = v.fit_transform(pass_text)
        k = min(k, X.shape[1] - 1, X.shape[0] - 1)
        m = NMF(k, init="nndsvda", random_state=0, max_iter=400)
        W = m.fit_transform(X)
        voc = np.array(v.get_feature_names_out())
        out.append(W / (W.sum(1, keepdims=True) + 1e-9))
        names += [f"{tag}:" + "/".join(x.strip() or "_" for x in voc[np.argsort(-c)[:3]]) for c in m.components_]
    return np.hstack(out), names


def _hgb():
    return HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=200, l2_regularization=1.0,
                                          class_weight="balanced", random_state=0)


FAMILIES = {"logistique_12_generiques": ("base", DP._lr), "arbres_12_generiques": ("base", _hgb),
            "arbres_generiques_et_propres_a_la_matiere": ("full", _hgb)}


def _design(X, nm, T, n_pass):
    pidx = np.arange(len(X)) % n_pass
    Tm = T[pidx]
    deja = X[:, [nm.index("frequence_passee_du_passage")]]
    sec = X[:, [nm.index("frequence_passee_de_la_section")]]
    return np.hstack([X, Tm, Tm * deja, Tm * sec])


def _fit_pred(fam, Xb, Xf, y, tr, te):
    kind, mk = FAMILIES[fam]
    Z = Xb if kind == "base" else Xf
    return mk().fit(Z[tr], y[tr]).predict_proba(Z[te])[:, 1]


def testability(X, y, g, nm, T, tnames, n_pass) -> dict:
    """Validation emboîtée par année : pour chaque année testée, la famille est choisie sur les
    autres années seulement. Renvoie aussi les probabilités hors année (pour l'a priori)."""
    Xf = _design(X, nm, T, n_pass)
    years = [k for k in np.unique(g) if len(set(y[g == k])) > 1]
    per = {f: [] for f in FAMILIES}
    chosen, auc_chosen, prob = [], [], np.zeros(len(y))
    for k in np.unique(g):
        tr, te = g != k, g == k
        inner = {}
        for f in FAMILIES:
            sc = []
            for j in [j for j in years if j != k][:6]:  # 6 années internes suffisent à départager
                itr, ite = tr & (g != j), g == j
                sc.append(roc_auc_score(y[ite], _fit_pred(f, X, Xf, y, itr, ite)))
            inner[f] = np.mean(sc)
        best = max(inner, key=inner.get)
        p = {f: _fit_pred(f, X, Xf, y, tr, te) for f in FAMILIES}
        prob[te] = p[best]
        if k in years:
            for f in FAMILIES:
                per[f].append(roc_auc_score(y[te], p[f]))
            chosen.append(best)
            auc_chosen.append(roc_auc_score(y[te], p[best]))
    final = max(set(chosen), key=chosen.count)
    rules = _rules(final, X, Xf, y, nm, tnames)
    return {"auc_par_famille": {f: round(float(np.mean(v)), 3) for f, v in per.items()},
            "auc_famille_choisie_seule": round(float(np.mean(auc_chosen)), 3),
            "famille_choisie": final, "choix_par_annee": {f: chosen.count(f) for f in set(chosen)},
            "auc_popularite": round(float(np.mean([roc_auc_score(y[g == k], X[g == k, -2]) for k in years])), 3),
            "regles_decouvertes": rules, "_prob": prob}


def _rules(fam, X, Xf, y, nm, tnames, top: int = 10):
    """Variables qui pèsent le plus dans le modèle final (permutation sur un échantillon) et sens."""
    kind, mk = FAMILIES[fam]
    Z = X if kind == "base" else Xf
    names = list(nm) + ([f"{t}" for t in tnames] + [f"{t} × déjà tombé" for t in tnames] + [f"{t} × section déjà tombée" for t in tnames]
                        if kind == "full" else [])
    m = mk().fit(Z, y)
    rng = np.random.default_rng(0)
    idx = rng.choice(len(y), min(len(y), 4000), replace=False)
    Zs, ys = Z[idx], y[idx]
    base = roc_auc_score(ys, m.predict_proba(Zs)[:, 1])
    imp = []
    for j in range(Z.shape[1]):
        Zp = Zs.copy()
        Zp[:, j] = rng.permutation(Zp[:, j])
        imp.append(base - roc_auc_score(ys, m.predict_proba(Zp)[:, 1]))
    pred = m.predict_proba(Zs)[:, 1]
    out = []
    for j in np.argsort(imp)[::-1][:top]:
        if imp[j] <= 0.001:
            break
        r = spearmanr(Zs[:, j], pred)[0] if Zs[:, j].std() > 0 else 0
        out.append({"variable": DP.SHORT.get(names[j], names[j]), "importance": round(float(imp[j]), 4),
                    "sens": "+" if r > 0 else "-", "propre_a_la_matiere": bool(j >= len(nm))})
    return out


def section_prior(t, prob, g, n_pass) -> np.ndarray:
    """Pour chaque question : z-score du log de la probabilité (prédite sans son année) que
    chaque section tombe cette année-là."""
    K, ps = len(t.sections), np.asarray(t.pass_sec)
    by_year = {}
    for k in np.unique(g):
        p = prob[g == k]
        by_year[k] = np.log(np.array([p[ps == s].max() if (ps == s).any() else 1e-3 for s in range(K)]) + 1e-3)
    Pm = np.array([by_year.get(q.year, np.zeros(K)) for q in t.Q])
    return (Pm - Pm.mean(1, keepdims=True)) / (Pm.std(1, keepdims=True) + 1e-9)


def run(t, S, labels=None, gens: int = 3, log=print):
    """S : alignement après auto-entraînement (selftrain.improve). Renvoie l'alignement final,
    l'historique et le dernier bilan d'intentions."""
    allx = (np.arange(len(t.Q)), np.arange(len(t.sections)))
    meas = (lambda M: round(A.truth(M, labels, *allx), 3)) if labels else (lambda M: None)
    T, tnames = course_variables(t.pass_text)
    d0 = ST.diversity(S)
    S_start = ST.rz(S)  # ancre : l'a priori corrige la version de départ, il ne s'accumule pas
    hist, rep = [], None
    for gen in range(gens + 1):
        for q, s in zip(t.Q, S.argmax(1)):
            q.sec = int(s)
        it = Intent(t, S)
        it.features()
        d = it.testability_data()
        if d is None:
            break
        X, y, g, nm = d
        rep = testability(X, y, g, nm, T, tnames, len(t.pass_text))
        hist.append({"generation": gen, "vrai_top3": meas(S), "auc_intention": rep["auc_famille_choisie_seule"],
                     "famille": rep["famille_choisie"], "diversite": round(ST.diversity(S), 3)})
        log(f"    génération {gen} : {hist[-1]}")
        if gen == gens:
            break
        new = S_start + PRIOR * section_prior(t, rep["_prob"], g, len(t.pass_text))
        changed = float(np.mean(new.argmax(1) != S.argmax(1)))
        if ST.diversity(new) < ST.GARDE * d0 or changed < 0.01:
            hist[-1]["arret"] = "diversité écrasée" if changed >= 0.01 else "convergence"
            break
        S = new
    rep.pop("_prob", None)
    rep["variables_propres_decouvertes"] = tnames
    return S, hist, rep
