"""Programmes officiels (PDF Éduscol) -> data/<matière>/cours/*.md via le lecteur générique.

    python scripts/build_cours_pdf.py <matière> <pdf> [<pdf> ...]
Les PDF sont récupérés par scripts/fetch_programmes.sh."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from examgen.prof import pdfcours  # noqa: E402

name, pdfs = sys.argv[1], [Path(p) for p in sys.argv[2:]]
out = Path(__file__).resolve().parents[1] / "data" / name / "cours"
out.mkdir(parents=True, exist_ok=True)
for i, p in enumerate(pdfs, 1):
    md = pdfcours.pdf_to_markdown(p)
    m = re.search(r"^# (.+)$", md, re.M)
    slug = re.sub(r"[^a-z0-9]+", "_", (m.group(1) if m else p.stem).lower())[:40].strip("_")
    (out / f"{i:02d}_{slug}.md").write_text(md, encoding="utf-8")
    print(out / f"{i:02d}_{slug}.md", len(md))
