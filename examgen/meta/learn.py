"""Apprendre à se débrouiller sur une matière inconnue, puis le prouver.

  python -m examgen.meta.learn            # toutes les matières de domain.DOMAINS

1. Alignement : méta-règle (quels signaux auto-supervisés désignent le bon réglage de lecture).
   Preuve : apprise sur une matière, appliquée à l'autre (matière exclue). La règle finale,
   apprise sur toutes les matières, est écrite dans data/model/meta.json ; le moteur l'emploie
   seul quand une matière nouvelle n'a pas de corrigé (Teacher.align).
2. Intentions : variables relationnelles cours <-> question, retenues par tâches auto-supervisées,
   puis bilan d'universalité (retenues dans plusieurs matières avec le même sens d'effet).
Sortie : output/meta/rapport.json.
"""
from __future__ import annotations

import json
import sys
import warnings
from collections import defaultdict
from pathlib import Path

import joblib
import numpy as np

from . import align as A
from .domain import DOMAINS, eval_labels, load
from .intent import Intent
from ..prof.profile import DEFAULT_CFG

ROOT = Path(__file__).resolve().parents[2]
META = ROOT / "data" / "model" / "meta.json"
OUT = ROOT / "output" / "meta"
ROWS = ROOT / "data" / "cache" / "meta_align_rows.joblib"


def alignment(names: list[str], refresh: bool = False) -> dict:
    rows = joblib.load(ROWS) if ROWS.exists() and not refresh else {}
    for n in names:
        if n not in rows:
            t = load(n)
            rows[n] = A.collect(t, eval_labels(t), n_ep=12)
    joblib.dump(rows, ROWS)
    rep = {"matiere_exclue": {}, "correlation_signal_reussite": {}}
    for te in names:
        tr = [r for n in names if n != te for r in rows[n]]
        if not tr:
            continue
        m = A.fit_meta(tr)
        rep["matiere_exclue"][f"appris_sans_{te}"] = {"poids": dict(zip(A.PROXIES, np.round(m.coef_, 3).tolist())), **A.pick(m, rows[te])}
    for n in names:
        X, y, _ = A.design(rows[n])
        rep["correlation_signal_reussite"][n] = {p: round(float(np.corrcoef(X[:, j], y)[0, 1]), 2) for j, p in enumerate(A.PROXIES)}
    # règle finale : toutes les matières, épisodes renumérotés pour rester distincts
    pooled = [dict(r, episode=f"{n}:{r['episode']}") for n in names for r in rows[n]]
    final = A.fit_meta(pooled)
    rule = {"signaux": A.PROXIES, "poids": np.round(final.coef_, 4).tolist(), "appris_sur": names}
    META.parent.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps(rule, ensure_ascii=False, indent=1), encoding="utf-8")
    rep["regle_finale"] = rule
    return rep


def intentions(names: list[str]) -> dict:
    per = {}
    for n in names:
        t = load(n)
        t.rep = getattr(t, "rep", {})
        V = A.views(t, DEFAULT_CFG)
        S = A.combine(V, (1, 0.5, 0.25, 1))
        for q, s in zip(t.Q, S.argmax(1)):
            q.sec = int(s)
        t.consigne_vocab()
        t.consigne_facets()
        it = Intent(t, S)
        it.features()
        res = it.tasks()
        keep = sorted({v["variable"] for k, r in res.items() if k != "testabilite" for v in r.get("variables_retenues", [])})
        ty = it.types(keep)
        step = max(1, len(t.Q) // 6)
        per[n] = {"questions": len(t.Q), "taches": res, "types_d_intention": ty,
                  "ce_qui_est_evalue_sans_etre_dit": [{"enonce": t.Q[i].stem[:180], "mots": it.implicit(i)} for i in range(0, len(t.Q), step)]}
    # universalité : même tâche, même variable, retenue partout, même sens
    uni = defaultdict(list)
    for n, r in per.items():
        for task, tr in r["taches"].items():
            for v in tr.get("variables_retenues", []):
                uni[(task, v["variable"])].append((n, v["sens"], v["importance"]))
    universal = []
    for (task, var), lst in uni.items():
        if len({x[0] for x in lst}) == len(names) > 1:
            signs = {x[1] for x in lst}
            universal.append({"tache": task, "variable": var, "meme_sens": len(signs) == 1,
                              "importance": {x[0]: x[2] for x in lst}, "sens": lst[0][1] if len(signs) == 1 else "variable"})
    universal.sort(key=lambda r: (r["tache"], -min(r["importance"].values())))
    return {"par_matiere": per, "universelles": universal}


def main(argv=None):
    warnings.filterwarnings("ignore")
    names = (argv or sys.argv[1:]) or list(DOMAINS)
    rep = {"alignement": alignment(names), "intentions": intentions(names)}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "rapport.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    for k, v in rep["alignement"]["matiere_exclue"].items():
        print(k, {x: v[x] for x in ("choisi_par_le_meta_modele", "reglage_par_defaut", "meilleur_possible_oracle")})
    for u in rep["intentions"]["universelles"]:
        print("universelle", u["tache"], u["variable"], u["sens"], u["importance"])
    print("->", OUT / "rapport.json", "et", META)


if __name__ == "__main__":
    main()
