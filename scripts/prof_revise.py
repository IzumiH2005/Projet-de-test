"""Boucle vérifier → réviser pour le moteur générique (examgen.prof), quel que soit le domaine.

  python scripts/prof_revise.py prepare output/droit      # lots de révision + sauvegarde « avant »
  (agents rédacteurs : révisent output/droit/generated/<id>.json en place, d'après le lot)
  python -m examgen.prof check ... --out output/droit
  python scripts/prof_revise.py keep_best output/droit    # accepter / rejeter chaque révision
  python -m examgen.prof check ... --out output/droit
  python scripts/prof_revise.py compare output/droit

Le validateur (modèles appris) sert de récompense : une révision n'est gardée que si elle ne fait
pas baisser la note du fichier (somme des critères réussis, questions et annexes).
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
KEYS = ("facette_ok", "section_ok", "articles_ok", "nouveaute_ok", "longueur_ok")


def score(r: dict) -> int:
    return sum(bool(q.get(k)) for q in r["questions"] for k in KEYS) + sum(bool(a["ok"]) for a in r["annexes"])


def prepare(out: Path, batch: int = 5):
    v = json.loads((out / "validation.json").read_text(encoding="utf-8"))
    rev = out / "revision"
    rev.mkdir(exist_ok=True)
    for f in rev.glob("lot_*.json"):
        f.unlink()
    items = [{"fichier": str((out / "generated" / f"{r['id']}.json").relative_to(ROOT)), "id": r["id"], "a_corriger": r["revision"]}
             for r in v["detail"] if r["revision"]]
    for i in range(0, len(items), batch):
        (rev / f"lot_{i // batch + 1}.json").write_text(json.dumps(items[i:i + batch], ensure_ascii=False, indent=1), encoding="utf-8")
    shutil.copy(out / "validation.json", rev / "validation_avant.json")
    (rev / "avant").mkdir(exist_ok=True)
    for it in items:  # versions d'origine, pour pouvoir rejeter une révision
        shutil.copy(ROOT / it["fichier"], rev / "avant" / f"{it['id']}.json")
    print(f"{len(items)} fichiers à réviser -> {rev}")


def keep_best(out: Path):
    rev = out / "revision"
    A = {r["id"]: r for r in json.loads((rev / "validation_avant.json").read_text(encoding="utf-8"))["detail"]}
    B = {r["id"]: r for r in json.loads((out / "validation.json").read_text(encoding="utf-8"))["detail"]}
    items = [it for f in sorted(rev.glob("lot_*.json")) for it in json.loads(f.read_text(encoding="utf-8"))]
    kept, rejected = [], []
    for it in items:
        i = it["id"]
        if i in B and score(B[i]) >= score(A[i]):
            kept.append(i)
            continue
        shutil.copy(rev / "avant" / f"{i}.json", ROOT / it["fichier"])
        rejected.append(i)
    res = {"gardees": kept, "rejetees": rejected}
    (rev / "acceptation.json").write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
    print(f"révisions gardées : {len(kept)}, rejetées (version d'origine rétablie) : {len(rejected)}")


def compare(out: Path):
    rev = out / "revision"
    a = json.loads((rev / "validation_avant.json").read_text(encoding="utf-8"))
    b = json.loads((out / "validation.json").read_text(encoding="utf-8"))
    ids = {it["id"] for f in rev.glob("lot_*.json") for it in json.loads(f.read_text(encoding="utf-8"))}
    sub = lambda v: [q for r in v["detail"] if r["id"] in ids for q in r["questions"]]
    m = lambda qs, k: round(float(np.mean([bool(q[k]) for q in qs if q.get(k) is not None])), 3) if qs else None
    res = {"fichiers_revises": len(ids),
           "revises_avant": {k: m(sub(a), k) for k in KEYS}, "revises_apres": {k: m(sub(b), k) for k in KEYS},
           "global_avant": a["resume"], "global_apres": b["resume"]}
    (rev / "resultat.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    {"prepare": prepare, "keep_best": keep_best, "compare": compare}[sys.argv[1]](ROOT / sys.argv[2])
