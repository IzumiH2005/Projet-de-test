"""Cours PDF quelconque -> markdown lisible par `docs.parse_course`.

Aucune règle propre à une matière : la structure vient de la typographie.
- taille de police au-dessus du corps de texte -> titres (# pour la plus grande, ## ensuite) ;
- ligne courte en gras, à la taille du corps -> ### (collé au paragraphe suivant) ;
- tableaux -> une ligne de tableau = un passage « colonne 1 — colonne 2 : … » ;
- en-têtes / pieds de page répétés et numéros de page retirés.
Sert à l'entraînement (programmes officiels) et en production (cours envoyés en PDF).
"""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

import pdfplumber


def _clean(s: str) -> str:
    s = re.sub(r"\(cid:\d+\)", "", s)  # glyphes sans correspondance unicode
    s = s.replace("\u00a0", " ").replace("\uf0b7", "•").replace("\uf0a7", "•").replace("\uf0d8", "•")
    return re.sub(r"\s+", " ", s).strip()


def _sentences_chunks(text: str, max_len: int = 450) -> list[str]:
    if len(text) <= max_len:
        return [text]
    sents = re.split(r"(?<=[.!?;])\s+(?=[A-ZÉÈÀÂÎÔ«•\-–])", text)
    out, buf = [], ""
    for s in sents:
        if buf and len(buf) + len(s) > max_len:
            out.append(buf)
            buf = s
        else:
            buf = f"{buf} {s}".strip()
    if buf:
        out.append(buf)
    return out


def _lines(page, tables_bbox):
    def inside(l):
        cx, cy = (l["x0"] + l["x1"]) / 2, (l["top"] + l["bottom"]) / 2
        return any(b[0] - 2 <= cx <= b[2] + 2 and b[1] - 2 <= cy <= b[3] + 2 for b in tables_bbox)

    for l in page.extract_text_lines(return_chars=True):
        if inside(l):
            continue
        chars = [c for c in l["chars"] if c["text"].strip()]
        if not chars:
            continue
        letters = [c for c in chars if c["text"].isalpha()] or chars
        sizes = collections.Counter(round(c["size"]) for c in letters)
        bold = sum("bold" in c["fontname"].lower() for c in letters) / len(letters)
        col = collections.Counter(str(c.get("non_stroking_color")) for c in letters).most_common(1)[0][0]
        yield {"text": _clean(l["text"]), "size": sizes.most_common(1)[0][0], "bold": bold > 0.6,
               "color": col, "top": l["top"], "bottom": l["bottom"], "page": page.page_number}


def _blocks(path: Path) -> list[tuple]:
    """Suite de blocs : ("h", rang_de_style, texte) | ("p", texte) | ("row", intitulé, [passages])."""
    pdf = pdfplumber.open(str(path))
    items = []
    for page in pdf.pages:
        tabs = [t for t in page.find_tables() if len(t.rows) >= 2]
        for t in tabs:
            for row in t.extract():
                cells = [c for c in (_clean(c or "") for c in row) if c]
                if cells:
                    items.append((page.page_number, t.bbox[1], "row", cells))
        for l in _lines(page, [t.bbox for t in tabs]):
            items.append((l["page"], l["top"], "line", l))
    items.sort(key=lambda x: (x[0], x[1]))
    lines = [x[3] for x in items if x[2] == "line"]
    if not lines:
        return []
    rep = collections.Counter(re.sub(r"\d+", "#", l["text"]) for l in lines)
    noise = {k for k, v in rep.items() if v >= max(3, len(pdf.pages) // 3) and len(k) < 120}
    style = lambda l: (l["size"], l["bold"], l["color"])
    vol = collections.Counter()
    for l in lines:
        vol[style(l)] += len(l["text"])
    body = vol.most_common(1)[0][0]
    total = sum(vol.values())
    cand = [st for st in vol if st != body and vol[st] < 0.15 * total and
            (st[0] > body[0] or st[1] or st[2] != body[2]) and st[0] >= body[0]]
    rank = {st: i for i, st in enumerate(sorted(cand, key=lambda st: (-st[0], not st[2] != body[2], not st[1])))}

    out, para, last, header_seen = [], [], None, False
    def flush():
        if para:
            for c in _sentences_chunks(_clean(" ".join(para))):
                out.append(("p", c))
            para.clear()

    for _, _, kind, x in items:
        if kind == "row":
            flush()
            cells, last = x, None
            if not header_seen and all(len(c) < 60 for c in cells):
                header_seen = True  # en-tête de tableau
                continue
            rest = " ".join(cells[1:])
            if len(cells) >= 2 and len(cells[0]) < 200 and len(rest) > len(cells[0]):
                ps = [c for b in re.split(r"\s(?=[-•▪–]\s)", rest) for c in _sentences_chunks(b.strip(" -•▪–"))]
                out.append(("row", cells[0], ps))
            else:
                for c in _sentences_chunks(" : ".join([cells[0], " ; ".join(cells[1:])]) if len(cells) > 1 else cells[0], 600):
                    out.append(("p", c))
            continue
        header_seen = False
        l, t = x, x["text"]
        if re.sub(r"\d+", "#", t) in noise or re.fullmatch(r"[\d\s/.\-–]+", t):
            continue
        r = rank.get(style(l))
        if r is not None and len(t) < 150 and not t.endswith((",", ";")):
            flush()
            if out and out[-1][0] == "h" and out[-1][1] == r and last is not None and last.get("h") \
                    and l["page"] == last["page"] and l["top"] - last["bottom"] < l["size"] * 1.2:
                out[-1] = ("h", r, out[-1][2] + " " + t)  # titre sur deux lignes
            else:
                out.append(("h", r, t.lstrip("•▪ ").strip()))
            last = {**l, "h": True}
            continue
        if (last is None or last.get("h") or l["page"] != last["page"]
                or l["top"] - last["bottom"] > l["size"] * 0.9 or t[:1] in "•-–▪◦"):
            flush()
        para.append(t)
        last = l
    flush()
    return out


def _render(blocks, k: int) -> str:
    md = []
    for b in blocks:
        if b[0] == "p":
            md.append(b[1])
        elif b[0] == "row":
            md.append(f"## {b[1]}")
            md += b[2]
        else:
            md.append(("#" if b[1] < k else "##" if b[1] == k else "###") + " " + b[2])
    return "\n\n".join(md) + "\n"


def _score(md: str) -> int:
    from . import docs
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(md)
    secs = docs.parse_course([Path(f.name)])
    Path(f.name).unlink()
    return sum(len(s.passages) >= 2 for s in secs)


def pdf_to_markdown(path: Path) -> str:
    """Le niveau de titre qui devient « section » est choisi sur le document lui-même :
    celui qui donne le plus de sections exploitables (au moins deux passages)."""
    blocks = _blocks(path)
    tiers = sorted({b[1] for b in blocks if b[0] == "h"})
    if not tiers:
        return _render(blocks, 0)
    best = max(tiers, key=lambda k: (_score(_render(blocks, k)), -k))
    return _render(blocks, best)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(pdf_to_markdown(Path(a)))
