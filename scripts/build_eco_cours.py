"""Assemble un cours d'économie (STMG, 1re + Tle) à partir des programmes Éduscol.

Même lecteur de tableaux que le droit (build_droit_cours.programme_rows), partie « Économie » :
sous-thèmes, contexte et finalités, notions, capacités. Rien n'est rédigé à la main.

Sortie : data/eco/cours/NN_theme.md (un titre ## par sous-thème).
Usage  : python scripts/build_eco_cours.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_droit_cours import ROOT, programme_rows  # noqa: E402

OUT = ROOT / "data" / "eco" / "cours"


def main():
    rows = {**programme_rows("eduscol_25015.pdf", range(1, 6), "economie"),
            **programme_rows("eduscol_25021.pdf", range(6, 10), "economie")}
    print(f"sous-thèmes : {len(rows)}")
    OUT.mkdir(parents=True, exist_ok=True)
    for f in OUT.glob("*.md"):
        f.unlink()
    by = {}
    for num in sorted(rows, key=lambda s: tuple(map(int, s.split(".")))):
        by.setdefault(rows[num]["theme"], []).append(rows[num])
    for (tn, tt), subs in by.items():
        lv = "Première" if tn <= 5 else "Terminale"
        md = [f"# Thème {tn} : {tt}", "", f"_{lv} STMG, économie._", ""]
        # chaque capacité du thème va au sous-thème dont le texte est le plus proche (TF-IDF)
        docs = [r["titre"] + " " + r["contexte"] + " " + r["notions"] for r in subs]
        caps = subs[0]["capacites"]
        own = {i: [] for i in range(len(subs))}
        if caps:
            vec = TfidfVectorizer(strip_accents="unicode", sublinear_tf=True).fit(docs + caps)
            best = (vec.transform(caps) @ vec.transform(docs).T).toarray().argmax(1)
            for c, b in zip(caps, best):
                own[int(b)].append(c)
        for i, r in enumerate(subs):
            md += [f"## {r['num']} {r['titre']}", ""]
            # contexte en paragraphes de deux phrases : un passage = une idée que le sujet peut viser
            ph = [x for x in re.split(r"(?<=[.!?])\s+(?=[A-ZÉÀ])", r["contexte"]) if x.strip()]
            md += [" ".join(ph[k:k + 2]) + "\n" for k in range(0, len(ph), 2)]
            if r["notions"]:
                md += [f"Notions : {r['notions']}", ""]
            for c in own[i]:
                md += [f"Capacité attendue : l'élève est capable {c}.", ""]
        slug = re.sub(r"[^a-z]+", "_", tt.lower().translate(str.maketrans("éèêàâùûôîç’'", "eeeaauuoic__")))[:40].strip("_")
        (OUT / f"{tn:02d}_{slug}.md").write_text("\n".join(md), encoding="utf-8")
        print(f"  thème {tn}: {len(subs)} sous-thèmes")


if __name__ == "__main__":
    main()
