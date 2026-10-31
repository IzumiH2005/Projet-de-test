"""Apprendre à se débrouiller sur une matière inconnue, puis le prouver.

  python -m examgen.meta.learn            # toutes les matières de domain.DOMAINS

1. Alignement : méta-règle (quels signaux auto-supervisés désignent le bon réglage de lecture).
   Preuve : apprise sur une matière, appliquée à l'autre (matière exclue). La règle finale,
   apprise sur toutes les matières, est écrite dans data/model/meta.json ; le moteur l'emploie
   seul quand une matière nouvelle n'a pas de corrigé (Teacher.align).
2. Auto-entraînement : v0 (lecture auto-réglée) -> v1 -> ... chaque version entraîne la suivante,
   avec un garde-fou sans étiquette ; règle de lecture apprise SANS la matière évaluée.
3. Intentions : variables relationnelles cours <-> question, retenues par tâches auto-supervisées,
   puis bilan d'universalité (retenues dans plusieurs matières avec le même sens d'effet).
   Mesurées avant et après auto-entraînement (meilleur alignement -> meilleures intentions ?).
4. Variables d'intention à grande échelle (deep.py) : centaines de variables générées, sélection
   par stabilité, transfert à froid entre matières.
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
from . import deep as DP, selftrain as ST
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


def selftraining(names: list[str]) -> tuple[dict, dict]:
    rows = joblib.load(ROWS)
    rep, start = {}, {}
    for n in names:
        others = [r for k in names if k != n for r in rows.get(k, [])]
        coef = A.fit_meta(others).coef_ if others else json.loads(META.read_text())["poids"]
        t = load(n)
        cfg, w, _ = A.self_tune(t, coef)
        S0 = A.combine(A.views(t, cfg), w)
        S, hist = ST.improve(t, S0, labels=eval_labels(t))
        rep[n] = {"regle_de_lecture_apprise_sans_cette_matiere": True, "generations": hist}
        start[n] = (t, S0, S)
        print(n, [h.get("vrai_top3") for h in hist])
    return rep, start


def _intent(t, S):
    t.rep = getattr(t, "rep", {})
    for q, s in zip(t.Q, S.argmax(1)):
        q.sec = int(s)
    t.consigne_vocab()
    t.consigne_facets()
    it = Intent(t, S)
    it.features()
    return it


def intentions(names: list[str], start: dict) -> dict:
    per, avant_apres, tdata = {}, {}, {}
    for n in names:
        t, S0, S = start[n]
        it0 = _intent(t, S0)
        r0 = it0.tasks()
        it = _intent(t, S)
        res = it.tasks()
        tdata[n] = it.testability_data()
        sc = lambda r, k: r.get(k, {}).get("score_sujets_exclus")
        avant_apres[n] = {k: {"avant": sc(r0, k), "apres": sc(res, k)} for k in res if sc(res, k) is not None}
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
    deep = DP.study({n: d for n, d in tdata.items() if d is not None})
    return {"par_matiere": per, "universelles": universal, "avant_apres_auto_entrainement": avant_apres, "grande_echelle": deep}


def main(argv=None):
    warnings.filterwarnings("ignore")
    names = (argv or sys.argv[1:]) or list(DOMAINS)
    rep = {"alignement": alignment(names)}
    rep["auto_entrainement"], start = selftraining(names)
    rep["intentions"] = intentions(names, start)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "rapport.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    for k, v in rep["alignement"]["matiere_exclue"].items():
        print(k, {x: v[x] for x in ("choisi_par_le_meta_modele", "reglage_par_defaut", "meilleur_possible_oracle")})
    print("avant/après", rep["intentions"]["avant_apres_auto_entrainement"])
    print("grande échelle", {k: v for k, v in rep["intentions"]["grande_echelle"].items() if k != "par_matiere"})
    for u in rep["intentions"]["universelles"]:
        print("universelle", u["tache"], u["variable"], u["sens"], u["importance"])
    print("->", OUT / "rapport.json", "et", META)


if __name__ == "__main__":
    main()
