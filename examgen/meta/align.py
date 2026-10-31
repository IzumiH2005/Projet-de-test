"""Méta-apprentissage de l'alignement question -> cours, sans vérité terrain au moment de l'emploi.

Le problème : sur une matière nouvelle, il n'y a pas forcément de corrigés qui disent quelle
partie du cours chaque question évalue. Le moteur doit alors régler seul sa lecture du texte
(représentation, poids de l'énoncé, de la situation, des documents, des références communes).

L'idée (apprendre à apprendre) :
  1. des signaux auto-supervisés, calculables sur n'importe quel corpus sans étiquette :
       coherence_partie   les questions d'une même partie visent des sections voisines, et des
                          parties différentes des sections différentes (information mutuelle) ;
       accord_des_vues    l'énoncé seul et la situation + documents seuls désignent la même section ;
       retrouve_partie    projetée sur le cours, une question retrouve sa propre partie ;
       marge              l'alignement tranche (écart entre la 1re et la 2e section) ;
       diversite          le cours entier est utilisé (pas d'effondrement sur une section) ;
  2. des épisodes : sous-ensembles de sujets et de chapitres du cours, dans chaque matière
     disponible ; pour chaque réglage candidat on mesure les signaux ET la vraie réussite
     (étiquettes d'évaluation, cachées au moteur) ;
  3. le méta-modèle apprend quelle combinaison des signaux désigne les bons réglages ;
  4. preuve de généralité : appris sur une matière, appliqué à l'autre qu'il n'a jamais vue
     (matière exclue), comparé au réglage par défaut et au meilleur réglage possible (oracle).
"""
from __future__ import annotations

import itertools

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import normalized_mutual_info_score as nmi

CFGS = [dict(analyzer=an, ngram=ng, a=a) for an, ng in (("word", (1, 1)), ("word", (1, 2)), ("char_wb", (3, 5)))
        for a in (0.2, 0.5, 0.8)]
WGRID = [(wa, wx, ws, wi) for wa in (0, 1) for wx in (0, 0.5, 1) for ws in (0, 0.25, 0.5) for wi in (0, 1)]
PROXIES = ["coherence_partie", "accord_des_vues", "retrouve_partie", "marge", "diversite"]


def views(t, cfg: dict) -> dict:
    """Matrices question x section pour chaque source de texte, sous un réglage de lecture."""
    t.cfg = dict(cfg)
    t._fit_vectorizer()
    Q = t.Q
    anx = [" ".join(a + " " + x for a, x in q.annexes)[:8000] for q in Q]
    V = {"stem": t.sec_scores([q.stem + " " + q.preamble for q in Q]),
         "ans": t.sec_scores([q.answer or q.stem for q in Q]),
         "anx": t.sec_scores(anx),
         "sit": t.sec_scores([q.situation[:3000] for q in Q]),
         "ids": t.id_bonus([q.stem + " " + q.answer + " " + a for q, a in zip(Q, anx)]),
         "has_ans": np.array([bool(q.answer) for q in Q])}
    parts = {}
    V["part"] = np.array([parts.setdefault((q.exam, q.part), len(parts)) for q in Q])
    V["exam"] = np.array([q.exam for q in Q])
    return V


def combine(V: dict, w) -> np.ndarray:
    return V["stem"] + w[0] * np.where(V["has_ans"][:, None], V["ans"], 0) + w[1] * V["anx"] + w[2] * V["sit"] + w[3] * V["ids"]


def _rownorm(M):
    return M / (np.linalg.norm(M, axis=1, keepdims=True) + 1e-9)


def proxies(V: dict, S: np.ndarray, idx: np.ndarray, cols: np.ndarray) -> dict:
    S = S[np.ix_(idx, cols)]
    top = S.argmax(1)
    srt = np.sort(S, 1)
    ctx = (V["sit"] + V["anx"])[np.ix_(idx, cols)]
    stem = V["stem"][np.ix_(idx, cols)]
    part = V["part"][idx]
    # retrouver sa partie : énoncé projeté sur le cours vs contexte projeté de chaque partie
    up = np.unique(part)
    P = _rownorm(np.vstack([ctx[part == p].mean(0) for p in up]))
    R = _rownorm(stem) @ P.T
    own = R[np.arange(len(part)), np.searchsorted(up, part)]
    rank = (R > own[:, None]).sum(1) + 1
    cnt = np.bincount(top, minlength=len(cols)) / len(top)
    ent = -(cnt[cnt > 0] * np.log(cnt[cnt > 0])).sum() / np.log(len(cols))
    return {"coherence_partie": nmi(part, top),
            "accord_des_vues": nmi(stem.argmax(1), ctx.argmax(1)),
            "retrouve_partie": float(np.mean(1 / rank)),
            "marge": float(np.mean((srt[:, -1] - srt[:, -2]) / (srt[:, -1] + 1e-9))) if len(cols) > 1 else 0.0,
            "diversite": float(ent)}


def truth(S: np.ndarray, labels: dict, idx: np.ndarray, cols: np.ndarray) -> float | None:
    """Réussite top 3 sur les questions étiquetées de l'épisode (évaluation seulement)."""
    pos = {c: j for j, c in enumerate(cols)}
    hits = []
    for i in idx:
        if i not in labels:
            continue
        lab = {pos[c] for c in labels[i] if c in pos}
        if not lab:
            continue
        top3 = set(np.argsort(-S[i, cols])[:3])
        hits.append(bool(lab & top3))
    return float(np.mean(hits)) if len(hits) >= 10 else None


def episodes(t, labels: dict, n: int, rng) -> list[tuple[np.ndarray, np.ndarray]]:
    """Sous-ensembles (questions, sections) : 60 % des sujets, et la moitié des épisodes sur une
    partie seulement des chapitres du cours (une « nouvelle matière » simulée)."""
    exams = np.array(sorted({q.exam for q in t.Q}))
    qex = np.array([q.exam for q in t.Q])
    parents = sorted({s.parent for s in t.sections})
    out = []
    tries = 0
    while len(out) < n and tries < n * 20:
        tries += 1
        ex = rng.choice(exams, size=max(3, int(0.6 * len(exams))), replace=False)
        idx = np.where(np.isin(qex, ex))[0]
        cols = np.arange(len(t.sections))
        if len(out) % 2 and len(parents) >= 3:
            keep = set(rng.choice(parents, size=max(2, int(0.6 * len(parents))), replace=False))
            cols = np.array([i for i, s in enumerate(t.sections) if s.parent in keep])
            # on garde les questions dont la notion est dans les chapitres retenus, plus autant
            # de questions non étiquetées (le moteur ne sait pas lesquelles le sont)
            cs = set(cols.tolist())
            idx = np.array([i for i in idx if i not in labels or labels[i] & cs])
        if len(idx) >= 30 and len(cols) >= 4:
            out.append((idx, cols))
    return out


def collect(t, labels: dict, n_ep: int = 16, seed: int = 0) -> list[dict]:
    """Pour chaque épisode et chaque réglage candidat : signaux auto-supervisés + vraie réussite."""
    rng = np.random.default_rng(seed)
    eps = episodes(t, labels, n_ep, rng)
    rows = []
    for ci, cfg in enumerate(CFGS):
        V = views(t, cfg)
        for wi, w in enumerate(WGRID):
            if w[0] and not V["has_ans"].any():
                continue
            S = combine(V, w)
            for ei, (idx, cols) in enumerate(eps):
                tr = truth(S, labels, idx, cols)
                if tr is None:
                    continue
                rows.append({"episode": ei, "cfg": ci, "w": wi, "vrai": tr, **proxies(V, S, idx, cols)})
    return rows


def _z(x):
    x = np.asarray(x, float)
    return (x - x.mean()) / (x.std() + 1e-9)


def design(rows: list[dict]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Signaux standardisés dans chaque épisode (on compare des réglages entre eux, pas des épisodes)."""
    eps = np.array([r["episode"] for r in rows])
    X = np.zeros((len(rows), len(PROXIES)))
    y = np.zeros(len(rows))
    for e in np.unique(eps):
        m = eps == e
        for j, p in enumerate(PROXIES):
            X[m, j] = _z([rows[i][p] for i in np.where(m)[0]])
        y[m] = _z([rows[i]["vrai"] for i in np.where(m)[0]])
    return X, y, eps


def fit_meta(rows: list[dict]) -> Ridge:
    X, y, _ = design(rows)
    return Ridge(alpha=1.0, fit_intercept=False).fit(X, y)


def pick(model: Ridge, rows: list[dict]) -> dict:
    """Dans chaque épisode, le réglage que le méta-modèle choisit, sans voir la vérité."""
    X, _, eps = design(rows)
    pred = model.predict(X)
    chosen, oracle, default, worst = [], [], [], []
    d_cfg = CFGS.index(dict(analyzer="word", ngram=(1, 2), a=0.5))
    for e in np.unique(eps):
        ids = np.where(eps == e)[0]
        chosen.append(rows[ids[pred[ids].argmax()]]["vrai"])
        oracle.append(max(rows[i]["vrai"] for i in ids))
        worst.append(min(rows[i]["vrai"] for i in ids))
        dd = [rows[i]["vrai"] for i in ids if rows[i]["cfg"] == d_cfg and rows[i]["w"] == 0]
        default.append(dd[0] if dd else np.nan)
    return {"choisi_par_le_meta_modele": round(float(np.mean(chosen)), 3),
            "reglage_par_defaut": round(float(np.nanmean(default)), 3),
            "meilleur_possible_oracle": round(float(np.mean(oracle)), 3),
            "pire_reglage": round(float(np.mean(worst)), 3),
            "episodes": int(len(np.unique(eps)))}


def self_tune(t, model_coef: list[float]) -> tuple[dict, tuple, dict]:
    """Emploi sur une matière nouvelle, sans étiquette : le moteur essaie les réglages et garde
    celui que la règle méta-apprise juge le meilleur."""
    idx = np.arange(len(t.Q))
    cols = np.arange(len(t.sections))
    cand = []
    for cfg in CFGS:
        V = views(t, cfg)
        for w in WGRID:
            if w[0] and not V["has_ans"].any():
                continue
            cand.append((cfg, w, proxies(V, combine(V, w), idx, cols)))
    X = np.column_stack([_z([c[2][p] for c in cand]) for p in PROXIES])
    best = int((X @ np.asarray(model_coef)).argmax())
    cfg, w, px = cand[best]
    t.cfg = dict(cfg)
    t._fit_vectorizer()
    return cfg, w, px
