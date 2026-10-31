"""Boucle vérifier → réviser (NSI) : questions inédites dont le type de support visé n'est pas
reconnu par le modèle découvert (support_top3_ok faux).

  python scripts/nsi_revise.py prepare   # écrit output/revision_nsi/lot_*.json + sauvegarde « avant »
  (agents rédacteurs : révisent output/generated/I-*.json en place)
  python -m examgen.cli validate && python scripts/nsi_revise.py keep_best
  python -m examgen.cli validate && python scripts/nsi_revise.py compare

Chaque item de révision donne au rédacteur le diagnostic du validateur et de vrais exemples du
type de support attendu, pris dans les anciens sujets (unités classées dans cette facette).
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import joblib
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
REV = OUT / "revision_nsi"


def prepare(batch: int = 12):
    v = json.loads((OUT / "validation.json").read_text(encoding="utf-8"))
    plans = {p["id"]: {q["slot"]: q for q in p["questions"]} for p in json.loads((OUT / "plans_inedit.json").read_text(encoding="utf-8"))}
    d = joblib.load(ROOT / "data" / "model" / "discovery_data.joblib")
    units, fu = d["units"], np.asarray(d["fu"])
    rng = np.random.default_rng(3)
    ex_by_s = {}
    for s in set(fu.tolist()):
        idx = [i for i in np.where(fu == s)[0] if 80 < len(units[i]["text"]) < 900]
        ex_by_s[int(s)] = [units[i]["text"] for i in rng.choice(idx, size=min(4, len(idx)), replace=False)] if idx else []
    items = []
    for x in v["detail"]:
        if not x["id"].startswith("I") or x.get("support_top3_ok") is not False:
            continue
        g = json.loads((OUT / "generated" / f"{x['id']}.json").read_text(encoding="utf-8"))
        ex = next(e for e in g["exercices"] if e["numero"] == x["exercice"])
        q = next(q for q in ex["questions"] if q["slot"] == x["slot"])
        ps = plans[x["id"]][x["slot"]]
        items.append({"fichier": f"output/generated/{x['id']}.json", "exercice": x["exercice"], "slot": x["slot"],
                      "notion": x["notion"], "enonce_actuel": q["enonce"], "fin_du_contexte": ex.get("contexte", "")[-500:],
                      "support_vise": ps["support"], "consigne_visee": ps["consigne"]["nom"],
                      "exemples_reels_du_support": ex_by_s.get(ps["support_id"], []),
                      "diagnostic": "le validateur ne reconnaît pas le type de support visé dans l'énoncé (ni dans la fin du contexte)"})
    REV.mkdir(parents=True, exist_ok=True)
    for f in REV.glob("lot_*.json"):
        f.unlink()
    for i in range(0, len(items), batch):
        (REV / f"lot_{i // batch + 1}.json").write_text(json.dumps(items[i:i + batch], ensure_ascii=False, indent=1), encoding="utf-8")
    shutil.copy(OUT / "validation.json", REV / "validation_avant.json")
    print(f"{len(items)} questions à réviser -> {REV}")


def compare():
    a = json.loads((REV / "validation_avant.json").read_text(encoding="utf-8"))
    b = json.loads((OUT / "validation.json").read_text(encoding="utf-8"))
    key = lambda d: (d["id"], d.get("exercice"), d.get("slot"))
    todo = {(it["fichier"].split("/")[-1][:-5], it["exercice"], it["slot"])
            for f in REV.glob("lot_*.json") for it in json.loads(f.read_text(encoding="utf-8"))}
    bd = {key(d): d for d in b["detail"]}
    rev = [bd[k] for k in todo if k in bd]
    res = {"questions_revisees": len(rev),
           "support_top3_ok_apres_revision": round(float(np.mean([bool(d["support_top3_ok"]) for d in rev if d.get("support_top3_ok") is not None])), 3) if rev else None,
           "consigne_top3_ok_apres_revision": round(float(np.mean([bool(d["consigne_top3_ok"]) for d in rev if d.get("consigne_top3_ok") is not None])), 3) if rev else None,
           "notion_ok_apres_revision": round(float(np.mean([bool(d["notion_ok"]) for d in rev if d.get("notion_ok") is not None])), 3) if rev else None,
           "inedit_avant": {k: a["resume"]["inedit"][k] for k in ("support_top3_ok", "consigne_top3_ok", "notion_ok", "plausible")},
           "inedit_apres": {k: b["resume"]["inedit"][k] for k in ("support_top3_ok", "consigne_top3_ok", "notion_ok", "plausible")}}
    (REV / "resultat.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))


def keep_best():
    """Accepter / rejeter chaque révision : on garde la version (avant ou après) que le validateur
    note le mieux (support + consigne + notion). Une révision qui gagne le support mais perd la
    consigne est rejetée. L'ancienne version vient du dernier commit (git)."""
    import subprocess
    a = json.loads((REV / "validation_avant.json").read_text(encoding="utf-8"))
    b = json.loads((OUT / "validation.json").read_text(encoding="utf-8"))
    key = lambda d: (d["id"], d.get("exercice"), d.get("slot"))
    A, B = {key(d): d for d in a["detail"]}, {key(d): d for d in b["detail"]}
    sc = lambda d: sum(bool(d.get(m)) for m in ("support_top3_ok", "consigne_top3_ok", "notion_ok"))
    items = [it for f in sorted(REV.glob("lot_*.json")) for it in json.loads(f.read_text(encoding="utf-8"))]
    kept = rejected = 0
    for it in items:
        k = (it["fichier"].split("/")[-1][:-5], it["exercice"], it["slot"])
        if k not in A or k not in B or sc(B[k]) >= sc(A[k]):
            kept += 1
            continue
        old = json.loads(subprocess.run(["git", "show", f"HEAD:{it['fichier']}"], cwd=ROOT, capture_output=True, text=True, check=True).stdout)
        oq = next(q for e in old["exercices"] if e["numero"] == it["exercice"] for q in e["questions"] if q["slot"] == it["slot"])
        path = ROOT / it["fichier"]
        g = json.loads(path.read_text(encoding="utf-8"))
        for e in g["exercices"]:
            if e["numero"] == it["exercice"]:
                for q in e["questions"]:
                    if q["slot"] == it["slot"]:
                        q["enonce"], q["reponse_attendue"] = oq["enonce"], oq.get("reponse_attendue", q.get("reponse_attendue"))
        path.write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8")
        rejected += 1
    print(f"révisions gardées : {kept}, rejetées (version d'origine rétablie) : {rejected}")
    (REV / "acceptation.json").write_text(json.dumps({"gardees": kept, "rejetees": rejected}, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    {"prepare": prepare, "compare": compare, "keep_best": keep_best}[sys.argv[1]]()
