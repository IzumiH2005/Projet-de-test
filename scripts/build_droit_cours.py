"""Assemble un cours de droit (STMG, 1re + Tle) à partir de documents officiels.

Matière utilisée (rien n'est rédigé à la main) :
  - programmes Éduscol de 1re (eduscol_25015) et Tle (eduscol_25021) : sous-thèmes,
    contexte et finalités, notions, capacités ;
  - indications complémentaires de Tle (eduscol_25252) : précisions didactiques ;
  - textes en vigueur (Code civil, du travail, de la consommation, de commerce, dépôts
    git de tricoteuses.fr) : pour chaque sous-thème, les articles les plus proches de
    son texte sont retrouvés par TF-IDF, sans liste écrite à la main.

Sortie : data/droit/cours/NN_theme.md (un titre ## par sous-thème).
Usage  : python scripts/build_droit_cours.py CODES_DIR
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "sources" / "droit_cours"
OUT = ROOT / "data" / "droit" / "cours"


def pdf_layout(name: str) -> list[str]:
    return subprocess.run(["pdftotext", "-layout", str(SRC / name), "-"], capture_output=True,
                          text=True).stdout.splitlines()


def pdf_raw(name: str) -> str:
    return subprocess.run(["pdftotext", str(SRC / name), "-"], capture_output=True, text=True).stdout


NOISE = re.compile(r"Retrouvez éduscol|eduscol\.education\.fr|VOIE TECHNOLOGIQUE|^\s*(1re|Tle)\s+Droit et économie|"
                   r"Ministère de l|^\s*\d+\s*$")


def pdf_words(name: str):
    """Mots du PDF regroupés en lignes, avec les bords de colonnes de chaque page
    (pics de l'histogramme des abscisses de début de mot) : [(page, y, [(x, mot)], bords)]."""
    import collections
    xml = subprocess.run(["pdftotext", "-bbox", str(SRC / name), "-"], capture_output=True, text=True).stdout
    lines = []
    for pi, page in enumerate(xml.split("<page ")[1:]):
        h, ws = collections.Counter(), []
        for x, y, w in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)"[^>]*>([^<]*)</word>', page):
            ws.append((float(y), float(x), w.replace("&amp;", "&").replace("&apos;", "'")))
            h[round(float(x))] += 1
        cur, y0 = {}, -99.0
        for y, x, w in sorted(ws):  # une ligne = mots dont l'ordonnée est à moins de 4 pt de la première
            if y - y0 > 4:
                y0 = y
            cur.setdefault(y0, []).append((x, w))
        b1 = max(range(125, 300), key=lambda v: h[v] + h[v + 1])
        b2 = max(range(300, 480), key=lambda v: h[v] + h[v + 1])
        for k in sorted(cur):
            lines.append((pi, k, sorted(cur[k]), (b1 - 3, b2 - 3)))
    return lines


ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}


def programme_rows(name: str, themes: range, partie: str = "droit") -> dict:
    """Tableaux « Sous-thèmes | Contexte et finalités | Notions » lus par coordonnées -> {num: {...}}.
    partie="economie" : saute la partie droit et lit celle qui suit le titre « Économie »."""
    rows, theme, cols, cur, caps, in_caps, started = {}, None, None, None, {}, False, False
    titles = {}
    skip = partie != "droit"
    for page, y, words, bords in pdf_words(name):
        text = " ".join(w for _, w in words)
        if NOISE.search(text):
            continue
        if skip:
            if re.search(r"Contextes? et finalités", text):
                started = True
            elif started and text.strip() in ("Économie", "ÉCONOMIE"):
                skip, started = False, False
            continue
        m = re.match(r"Thème (\d)\s*[:\-–]\s*(.+)", text)
        if m and words[0][0] < 120:
            n = int(m.group(1))
            if started and theme and n < theme[0]:
                break  # partie suivante du programme (économie)
            if n in themes and len(m.group(2).strip()) > 5:
                titles.setdefault(n, m.group(2).strip())
            if n in themes and not (theme and theme[0] == n):
                theme = (n, m.group(2).strip())
                cols, cur, in_caps = None, None, False
                caps.setdefault(n, [])
            elif n not in themes:
                theme = None
            continue
        if theme is None:
            continue
        if partie == "droit" and text.strip() in ("Économie", "ÉCONOMIE"):
            if started:
                break
            theme = None
            continue
        if re.search(r"capables?\s*:?\s*$", text):
            in_caps, cols, prev_end = True, None, ":"
            continue
        if re.search(r"Contextes? et finalités", text):
            cols, started = True, True
            in_caps = False
            continue
        if in_caps:
            t = text.replace("\uf02d", "").strip(" •;.")
            new = not caps[theme[0]] or prev_end in ";:." or text.lstrip()[:1] in ("\uf02d", "•") \
                or bool(re.match(r"(d[’']|de )\s*\w+(er|ir|re)\b", t))  # « de calculer… » : puce perdue
            prev_end = text.rstrip()[-1:]
            if t and (new or t[:1].islower() or t[:1] == "("):
                if new:
                    caps[theme[0]].append(t)
                else:  # suite de la capacité précédente, coupée en fin de ligne
                    caps[theme[0]][-1] += " " + t
            continue
        if cols is None:
            continue
        c = ["", "", ""]
        for x, w in words:
            i = 0 if x < bords[0] else (1 if x < bords[1] else 2)
            c[i] += " " + w
        c0, c1, c2 = (t.strip() for t in c)
        m = re.match(r"(\d|[IVX]+)\.\s?(\d)\.?\s*(.*)", c0)
        if m and ROMAN.get(m.group(1), int(m.group(1)) if m.group(1).isdigit() else 0) == theme[0]:
            num = f"{theme[0]}.{m.group(2)}"
            cur = rows.setdefault(num, {"theme": theme, "num": num, "titre": [m.group(3)], "contexte": [],
                                        "notions": []})
        elif cur is not None and c0:
            cur["titre"].append(c0)
        if cur is not None:
            if c1: cur["contexte"].append(c1)
            if c2: cur["notions"].append(c2)
    for r in rows.values():
        r["titre"] = re.sub(r"\s+", " ", " ".join(t for t in r["titre"] if t)).strip()
        r["contexte"] = re.sub(r"\s+", " ", " ".join(r["contexte"])).strip()
        r["notions"] = re.sub(r"\s+", " ", " ".join(r["notions"])).strip()
        r["capacites"] = [c for c in caps.get(r["theme"][0], []) if len(c) > 8]
        r["theme"] = (r["theme"][0], titles.get(r["theme"][0], r["theme"][1]))
    return rows


def indications(raw: str) -> dict:
    """Indications complémentaires (Tle) : texte libre par sous-thème."""
    out, cur = {}, None
    for ln in raw.splitlines():
        if NOISE.search(ln):
            continue
        m = re.match(r"^([5-8])\.(\d) (.+)$", ln.strip())
        if m:
            cur = f"{m.group(1)}.{m.group(2)}"
            out.setdefault(cur, [])
            continue
        if re.match(r"^Thème [5-8]", ln.strip()):
            cur = None
        if cur:
            out[cur].append(ln.strip())
    res = {}
    for k, ls in out.items():
        paras, buf = [], []
        for l in ls + [""]:
            if l:
                buf.append(l)
            elif buf:
                paras.append(" ".join(buf)); buf = []
        # on ne garde que les vraies phrases (les colonnes de notions sont déjà dans le programme)
        res[k] = [p for p in paras if len(p) > 120 and p.count(".") >= 1]
    return res


def load_articles(codes_dir: Path):
    arts = []
    names = {"code_civil": "Code civil", "code_du_travail": "Code du travail",
             "code_de_la_consommation": "Code de la consommation", "code_de_commerce": "Code de commerce"}
    for code, label in names.items():
        for f in (codes_dir / code).rglob("article_*.md"):
            t = f.read_text(encoding="utf-8", errors="ignore")
            if "État: VIGUEUR" not in t:
                continue
            body = t.split("---", 2)[-1]
            body = re.sub(r"<br\s*/?>", "", body)
            body = re.sub(r"## \[Autres formats\].*", "", body, flags=re.S)
            body = re.sub(r"### Nota.*", "", body, flags=re.S)
            num = re.search(r"Numéro: (\S+)", t).group(1)
            if num[0] in "RDA":  # partie réglementaire : trop technique pour un cours de lycée
                continue
            body = re.sub(r"^# Article.*\n", "", body.strip()).strip()
            body = re.sub(r"\n{2,}", "\n", body)
            if 60 < len(body) < 1800:
                arts.append({"code": label, "num": num, "texte": body})
    return arts


def main(codes_dir: Path):
    p1 = programme_rows("eduscol_25015.pdf", range(1, 5))
    tl = programme_rows("eduscol_25021.pdf", range(5, 9))
    ic = indications(pdf_raw("eduscol_25252.pdf"))
    rows = {**p1, **tl}
    print(f"sous-thèmes : {len(rows)} ({sorted(rows)})")
    arts = load_articles(codes_dir)
    print(f"articles en vigueur : {len(arts)}")
    docs = [a["texte"] for a in arts]
    vec = TfidfVectorizer(sublinear_tf=True, min_df=2, max_df=0.3, ngram_range=(1, 2), strip_accents="unicode")
    A = vec.fit_transform(docs)
    OUT.mkdir(parents=True, exist_ok=True)
    for f in OUT.glob("*.md"):
        f.unlink()
    by_theme = {}
    used = set()
    for num in sorted(rows, key=lambda s: tuple(map(int, s.split(".")))):
        r = rows[num]
        q = " ".join([r["titre"], r["contexte"], r["notions"], " ".join(ic.get(num, []))])
        sims = (A @ vec.transform([q]).T).toarray().ravel()
        top = [i for i in np.argsort(-sims)[:4] if sims[i] > 0.12]
        # puis chaque notion du programme cherche ses propres articles
        for notion in re.split(r"[.;]\s+", r["notions"]):
            if len(notion) < 8:
                continue
            sn = (A @ vec.transform([notion + " " + r["titre"]]).T).toarray().ravel()
            top += [i for i in np.argsort(-sn)[:2] if sn[i] > 0.15]
        top = [i for i in dict.fromkeys(top) if i not in used][:14]
        used.update(top)
        by_theme.setdefault(r["theme"], []).append((r, top))
    for (tn, tt), subs in by_theme.items():
        lv = "Première" if tn <= 4 else "Terminale"
        md = [f"# Thème {tn} : {tt}", "", f"_{lv} STMG, droit._", ""]
        caps = subs[0][0]["capacites"]
        if caps:
            md += ["Capacités attendues : l'élève est capable " + " ; ".join(caps) + ".", ""]
        for r, top in subs:
            md += [f"## {r['num']} {r['titre']}", "", r["contexte"], ""]
            if r["notions"]:
                md += [f"Notions : {r['notions']}", ""]
            for p in ic.get(r["num"], []):
                md += [p, ""]
            for i in top:
                a = arts[i]
                md += [f"### Article {a['num']} du {a['code']}", "", a["texte"], ""]
        slug = re.sub(r"[^a-z]+", "_", tt.lower().translate(str.maketrans("éèêàâùûôîç’'", "eeeaauuoic__")))[:40].strip("_")
        (OUT / f"{tn:02d}_{slug}.md").write_text("\n".join(md), encoding="utf-8")
        print(f"  thème {tn}: {len(subs)} sous-thèmes, {sum(len(t) for _, t in subs)} articles")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
