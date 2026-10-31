"""Auto-entraînement par générations : chaque version du moteur entraîne la suivante.

  v0  lecture du cours auto-réglée (align.self_tune) ;
  vk+1 un « élève » est entraîné sur ce que vk sait :
         - les passages du cours, étiquetés gratuitement par leur section ;
         - les questions sur lesquelles vk est le plus sûr de lui (pseudo-étiquettes),
           toujours prédites hors pli (sujet exclu), pour qu'il ne recopie pas son maître ;
       puis l'élève est fusionné avec son maître.
  Plusieurs candidats sont produits à chaque génération (part de pseudo-étiquettes, poids
  de l'élève). Une RÈGLE D'ACCEPTATION méta-apprise choisit le candidat, ou garde la version
  actuelle (arrêt). Elle ne voit que des signaux auto-supervisés : elle a appris, sur d'autres
  matières, quels signaux annoncent un vrai progrès. Aucune étiquette au moment de l'emploi.
"""
from __future__ import annotations

import numpy as np
from scipy.sparse import vstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge, SGDClassifier
from sklearn.model_selection import GroupKFold

from . import align as A

PROXIES = A.PROXIES + ["stabilite", "confiance", "accord_eleve", "accord_v0", "accord_lecteur_du_cours", "precision_estimee"]
QFRAC = (0.0, 0.3, 0.6)
BETA = (0.25, 0.5, 0.75, 1.0)


def rz(S):
    return (S - S.mean(1, keepdims=True)) / (S.std(1, keepdims=True) + 1e-9)


def margin(S):
    s = np.sort(rz(S), 1)
    return s[:, -1] - s[:, -2]


class Student:
    """Lecteur indépendant du maître (mots 1-2), réutilisé à chaque génération."""

    def __init__(self, t):
        Q = t.Q
        qt = [" ".join([q.stem, q.preamble, q.situation[:3000], " ".join(x for _, x in q.annexes)[:4000], q.answer]) for q in Q]
        v = TfidfVectorizer(sublinear_tf=True, strip_accents="unicode", min_df=2, max_df=0.5, ngram_range=(1, 2),
                            token_pattern=r"(?u)\b\w\w+\b").fit(t.pass_text + qt)
        self.XP, self.XQ = v.transform(t.pass_text), v.transform(qt)
        self.yP = np.asarray(t.pass_sec)
        self.K = len(t.sections)
        self.groups = np.array([q.exam for q in Q])
        self._course_only = None

    def _fit(self, X, y, w):
        return SGDClassifier(loss="log_loss", alpha=2e-5, max_iter=12, tol=None, random_state=0).fit(X, y, sample_weight=w)

    def _place(self, clf, X):
        out = np.full((X.shape[0], self.K), -20.0)
        out[:, clf.classes_] = clf.predict_log_proba(X)
        return out

    def predict(self, S_teacher, qfrac: float) -> np.ndarray:
        if qfrac == 0:
            if self._course_only is None:
                self._course_only = self._place(self._fit(self.XP, self.yP, np.ones(len(self.yP))), self.XQ)
            return self._course_only
        lab, conf = S_teacher.argmax(1), margin(S_teacher)
        sel = conf >= np.quantile(conf, 1 - qfrac)
        out = np.zeros((self.XQ.shape[0], self.K))
        n = min(4, len(set(self.groups)))
        for tr, te in GroupKFold(n_splits=n).split(self.XQ, groups=self.groups):
            ts = tr[sel[tr]]
            X = vstack([self.XP, self.XQ[ts]])
            y = np.concatenate([self.yP, lab[ts]])
            w = np.concatenate([np.ones(len(self.yP)), 1 + conf[ts] / (conf[ts].mean() + 1e-9)])
            out[te] = self._place(self._fit(X, y, w), self.XQ[te])
        return out


def candidates(cur, prev_top, stu: Student):
    out = [("garder", cur)]
    for q in QFRAC:
        P = rz(stu.predict(cur, q))
        for b in BETA:
            out.append(((q, b), (1 - b) * rz(cur) + b * P))
    return out


def signals(V, S, idx, cols, prev, stu, v0, course) -> dict:
    """prev, stu, v0, course : matrices de scores (version actuelle, élève du candidat,
    version de départ, lecteur entraîné sur le seul cours)."""
    p = A.proxies(V, S, idx, cols)
    sub = lambda M: M[np.ix_(idx, cols)].argmax(1)
    top = sub(S)
    p["stabilite"] = float(np.mean(top == sub(prev)))
    p["confiance"] = float(np.mean(margin(S[np.ix_(idx, cols)])))
    p["accord_eleve"] = float(np.mean(top == sub(stu)))
    p["accord_v0"] = float(np.mean(top == sub(v0)))
    p["accord_lecteur_du_cours"] = float(np.mean(top == sub(course)))
    p["precision_estimee"] = triplet(top, [sub(V["stem"]), sub(V["sit"] + V["anx"]), sub(course)])
    return p


def triplet(top, views) -> float:
    """Précision estimée sans étiquette : si deux lecteurs indépendants X, Y ont des précisions
    pX, pY, ils s'accordent environ pX*pY fois ; donc p(S)^2 ~ accord(S,X)*accord(S,Y)/accord(X,Y)."""
    ag = lambda a, b: max(float(np.mean(a == b)), 1e-3)
    est = []
    for i in range(len(views)):
        for j in range(i + 1, len(views)):
            est.append(np.sqrt(ag(top, views[i]) * ag(top, views[j]) / ag(views[i], views[j])))
    return float(np.median(est))


def _z(x):
    x = np.asarray(x, float)
    return (x - x.mean()) / (x.std() + 1e-9)


def design(rows):
    eps = np.array([r["episode"] for r in rows])
    X = np.zeros((len(rows), len(PROXIES)))
    y = np.zeros(len(rows))
    for e in np.unique(eps):
        m = np.where(eps == e)[0]
        for j, p in enumerate(PROXIES):
            X[m, j] = _z([rows[i][p] for i in m])
        y[m] = _z([rows[i]["vrai"] for i in m])
    return X, y, eps


def fit_rule(rows, min_sign=0.75) -> list[float]:
    """Règle invariante : on ne garde que les signaux dont l'effet a le même sens dans au moins
    min_sign des épisodes d'entraînement (sous-matières simulées) ; les autres sont propres à
    une matière et ne se transfèrent pas."""
    X, y, eps = design(rows)
    keep = []
    for j in range(X.shape[1]):
        c = [np.corrcoef(X[eps == e, j], y[eps == e])[0, 1] for e in np.unique(eps) if X[eps == e, j].std() > 0 and y[eps == e].std() > 0]
        c = np.nan_to_num(c)
        keep.append(len(c) > 0 and max(np.mean(c > 0), np.mean(c < 0)) >= min_sign)
    coef = np.zeros(X.shape[1])
    if any(keep):
        k = np.array(keep)
        coef[k] = Ridge(alpha=1.0, fit_intercept=False).fit(X[:, k], y).coef_
    return coef.tolist()


def run(t, align_coef, rule=None, labels=None, gens: int = 6, n_ep: int = 8, follow="regle", seed=0, log=print):
    """Boucle de générations. follow='regle' : la règle d'acceptation choisit (emploi réel) ;
    follow='oracle' : on suit le meilleur candidat selon la vérité (seulement pour produire des
    exemples d'apprentissage de la règle, sur une matière d'entraînement)."""
    cfg, w, _ = A.self_tune(t, align_coef)
    V = A.views(t, cfg)
    cur = A.combine(V, w)
    stu = Student(t)
    course = stu.predict(cur, 0)
    v0 = cur
    rng = np.random.default_rng(seed)
    eps = A.episodes(t, labels or {}, n_ep, rng) if labels else []
    allx = (np.arange(len(t.Q)), np.arange(len(t.sections)))
    hist, rows = [], []
    truth = lambda S: A.truth(S, labels, *allx) if labels else None
    hist.append({"version": 0, "reglage": "lecture auto-réglée", "vrai_top3": truth(cur)})
    log(f"    v0 {hist[-1]}")
    prev_top = cur.argmax(1)
    for g in range(1, gens + 1):
        C = candidates(cur, prev_top, stu)
        studs = {q: stu.predict(cur, q) for q in QFRAC}
        sig = []
        for k, S in C:
            st = studs[k[0]] if k != "garder" else course
            sig.append(signals(V, S, *allx, cur, st, v0, course))
            for ei, (idx, cols) in enumerate(eps):
                tr = A.truth(S, labels, idx, cols)
                if tr is not None:
                    rows.append({"episode": f"{t.domain}:{seed}:{g}:{ei}", "cand": str(k), "vrai": tr,
                                 **signals(V, S, idx, cols, cur, st, v0, course)})
        if follow == "oracle":
            best = int(np.argmax([truth(S) for _, S in C]))
        elif follow == "hasard":  # états variés pour apprendre la règle (pas seulement le chemin idéal)
            best = int(rng.integers(1, len(C)))
        else:
            X = np.column_stack([_z([s[p] for s in sig]) for p in PROXIES])
            best = int((X @ np.asarray(rule)).argmax())
        k, S = C[best]
        if k == "garder":
            log(f"    v{g}: la règle garde la version précédente -> arrêt")
            break
        prev_top, cur = cur.argmax(1), S
        hist.append({"version": g, "reglage": {"part_pseudo_etiquettes": k[0], "poids_eleve": k[1]}, "vrai_top3": truth(cur)})
        log(f"    v{g} {hist[-1]}")
    t.S_self = cur
    return cur, hist, rows


POLICIES = [(q, b) for q in (0.0, 0.3, 0.6) for b in (0.25, 0.5, 1.0)]


def run_policy(t, align_coef, policy, gens: int = 5, labels=None, tol: float = 0.01, stu=None, start=None):
    """Politique fixe (part de pseudo-étiquettes, poids de l'élève) répétée génération après
    génération ; arrêt quand la nouvelle version change moins de tol des réponses (convergence)."""
    if start is None:
        cfg, w, _ = A.self_tune(t, align_coef)
        start = A.combine(A.views(t, cfg), w)
    stu = stu or Student(t)
    q, b = policy
    cur = start
    allx = (np.arange(len(t.Q)), np.arange(len(t.sections)))
    hist = [A.truth(cur, labels, *allx) if labels else None]
    for g in range(gens):
        new = (1 - b) * rz(cur) + b * rz(stu.predict(cur, q))
        changed = float(np.mean(new.argmax(1) != cur.argmax(1)))
        cur = new
        hist.append(A.truth(cur, labels, *allx) if labels else None)
        if changed < tol:
            break
    return cur, hist


# ---------------------------------------------------------------------------------------------
# Procédure retenue (la même pour toutes les matières, validée matière exclue) :
#   1. cohérence de partie : les questions d'une même partie d'un sujet portent sur un même thème ;
#      chaque question emprunte une part LISSAGE du profil moyen de sa partie ;
#   2. générations : l'élève (cours seul, poids ELEVE) corrige son maître, puis on relisse ;
#   3. garde-fou sans étiquette : une génération est refusée si elle écrase la diversité du cours
#      (moins de GARDE x la diversité de départ) ou ne change presque plus rien (convergence).
# Les règles par signal (ci-dessus) ne se transféraient pas d'une matière à l'autre ; cette
# procédure, si : droit 0,78 -> 0,87, NSI 0,77 -> 0,82 (top 3, vérité cachée au moteur).
LISSAGE, ELEVE, GARDE = 0.75, 0.25, 0.9


def diversity(S) -> float:
    c = np.bincount(S.argmax(1), minlength=S.shape[1]) / len(S)
    c = c[c > 0]
    return float(-(c * np.log(c)).sum() / np.log(S.shape[1]))


def smooth(t, S, g: float = LISSAGE):
    Z = rz(S)
    key = np.array([hash((q.exam, q.part)) for q in t.Q])
    out = Z.copy()
    for k in np.unique(key):
        m = key == k
        out[m] = (1 - g) * Z[m] + g * Z[m].mean(0)
    return out


def improve(t, S0, gens: int = 5, labels=None, stu=None):
    """v0 -> v1 -> ... ; chaque version est entraînée par la précédente. labels : seulement pour
    mesurer (jamais pour décider)."""
    stu = stu or Student(t)
    allx = (np.arange(len(t.Q)), np.arange(len(t.sections)))
    meas = (lambda S: round(A.truth(S, labels, *allx), 3)) if labels else (lambda S: None)
    d0 = diversity(S0)
    hist = [{"version": "v0 lecture auto-réglée", "vrai_top3": meas(S0), "diversite": round(d0, 3)}]
    cur = smooth(t, S0)
    hist.append({"version": "v1 cohérence de partie", "vrai_top3": meas(cur), "diversite": round(diversity(cur), 3)})
    for g in range(gens):
        new = smooth(t, (1 - ELEVE) * rz(cur) + ELEVE * rz(stu.predict(cur, 0)))
        changed = float(np.mean(new.argmax(1) != cur.argmax(1)))
        if diversity(new) < GARDE * d0:
            hist.append({"version": f"v{g + 2} refusée", "raison": "diversité du cours écrasée", "vrai_top3": meas(new)})
            break
        if changed < 0.01:
            hist.append({"version": f"v{g + 2} inutile", "raison": "convergence (moins de 1 % de réponses changées)"})
            break
        cur = new
        hist.append({"version": f"v{g + 2} entraînée par v{g + 1}", "vrai_top3": meas(cur), "diversite": round(diversity(cur), 3),
                     "reponses_changees": round(changed, 3)})
    return cur, hist
