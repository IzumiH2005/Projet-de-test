"""Accélérations qui ne changent aucun résultat.

- `auc` : aire sous la courbe ROC par la formule exacte des rangs (Mann-Whitney, ex aequo comptés
  pour moitié), identique à `sklearn.metrics.roc_auc_score` mais sans ses vérifications coûteuses.
- `pmap` : applique une fonction à une liste sur plusieurs cœurs, dans l'ordre (processus forkés,
  donc les objets déjà chargés sont partagés sans copie). `EXAMGEN_JOBS=1` désactive.
"""
from __future__ import annotations

import multiprocessing as mp
import os

import numpy as np
from scipy.stats import rankdata


def auc(y, s) -> float:
    y = np.asarray(y)
    u = np.unique(y)
    if len(u) != 2:
        raise ValueError("il faut exactement deux classes")
    y = y == u[1]  # comme scikit-learn : la plus grande étiquette est la classe positive
    n1 = int(y.sum())
    n0 = len(y) - n1
    r = rankdata(np.asarray(s, float))
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def jobs() -> int:
    try:
        return max(1, int(os.environ.get("EXAMGEN_JOBS", "0")) or len(os.sched_getaffinity(0)))
    except (ValueError, AttributeError):
        return os.cpu_count() or 1


_FN = None


def _call(x):
    return _FN(x)


def pmap(fn, items, n: int | None = None) -> list:
    """Comme [fn(x) for x in items], sur plusieurs processus si possible (même ordre, mêmes résultats)."""
    global _FN
    items = list(items)
    n = min(n or jobs(), len(items))
    if n <= 1 or mp.current_process().daemon:
        return [fn(x) for x in items]
    _FN = fn
    try:
        with mp.get_context("fork").Pool(n) as pool:
            return pool.map(_call, items, chunksize=1)
    finally:
        _FN = None
