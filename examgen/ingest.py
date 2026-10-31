"""Ingestion : PDF / Markdown -> corpus structuré.

Sorties (data/corpus/) :
  exams.jsonl   un sujet par ligne : métadonnées + exercices + questions
  course.jsonl  une section de cours par ligne : chapitre, titre, texte
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .config import CORPUS, SOURCES

# --------------------------------------------------------------------------- utils

CENTERS = {
    "ME": "Métropole", "G1": "Centres étrangers", "G11": "Centres étrangers",
    "AN": "Amérique du Nord", "AS": "Amérique du Sud", "JA": "Asie", "PO": "Polynésie",
    "NC": "Nouvelle-Calédonie", "LI": "Liban", "AG": "Antilles-Guyane", "IN": "Inde",
    "MA": "Mayotte", "RE": "La Réunion", "PE": "Sujet zéro", "SU": "Suède",
}
NAME_CENTERS = [
    ("metropole", "Métropole"), ("etranger", "Centres étrangers"), ("amerique", "Amérique du Nord"),
    ("asie", "Asie"), ("polynesie", "Polynésie"), ("caledonie", "Nouvelle-Calédonie"),
    ("antilles", "Antilles-Guyane"), ("liban", "Liban"), ("sujet_0", "Sujet zéro"),
    ("sujet0", "Sujet zéro"), ("blanc", "Bac blanc"), ("amnord", "Amérique du Nord"),
]


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def pdf_text(path: Path) -> str:
    try:
        reader = PdfReader(str(path))
        return "\n".join((p.extract_text() or "") for p in reader.pages)
    except Exception as e:  # PDF corrompu / chiffré
        print(f"  ! {path.name}: {e}")
        return ""


HEADER_RE = re.compile(
    r"^\s*(\d{2}[-_ ]?NSI\w*|NSI\w*)?\s*(Page\s*:?\s*)?\d+\s*/\s*\d+\s*$|"
    r"^\s*\d{2}[-_ ]?NSI[A-Z0-9]+\s+Page\s*:?\s*\d+\s*/\s*\d+.*$|"
    r"^\s*Page\s+\d+\s+(sur|/)\s+\d+\s*$",
    re.I,
)


def clean_pdf_text(t: str) -> str:
    t = t.replace(" ", " ").replace("’", "'").replace("", "•")
    lines = [ln.rstrip() for ln in t.splitlines() if not HEADER_RE.match(ln)]
    t = "\n".join(lines)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()


# --------------------------------------------------------------------------- métadonnées

CODE_RE = re.compile(r"(\d{2})[-_ ]?NSI(?:J(\d))?([A-Z]{2})(\d{1,2})", re.I)


def exam_metadata(path: Path, text: str) -> dict:
    name = path.stem
    low = strip_accents(name.lower())
    m = CODE_RE.search(name.upper()) or CODE_RE.search(text[:400].upper())
    year = None
    if (s := re.search(r"SESSION\s+(20\d\d)", text[:1500], re.I)):
        year = int(s.group(1))
    elif m:
        year = 2000 + int(m.group(1))
    elif (s := re.search(r"(20\d\d)", name)):
        year = int(s.group(1))
    elif (s := re.search(r"^(\d{2})[-_]", name)):
        year = 2000 + int(s.group(1))
    day = None
    if m and m.group(2):
        day = int(m.group(2))
    elif (d := re.search(r"J(\d)", name, re.I)):
        day = int(d.group(1))
    elif (d := re.search(r"-(\d)-sujet", low)):
        day = int(d.group(1))
    center = None
    for key, val in NAME_CENTERS:
        if key in low:
            center = val
            break
    if center is None and m:
        center = CENTERS.get(m.group(3).upper(), m.group(3).upper())
    kind = "blanc" if "blanc" in low else ("sujet0" if ("sujet_0" in low or "sujet0" in low or "sujet 0" in low) else "officiel")
    if year is None and (s := re.search(r"(20\d\d)", str(path))):
        year = int(s.group(1))
    duration = None
    if (dm := re.search(r"Durée de l'épreuve\s*:\s*(\d)\s*heures?\s*(\d+)?", text[:2500], re.I)):
        duration = int(dm.group(1)) * 60 + int(dm.group(2) or 0)
    return {"year": year, "day": day, "center": center, "kind": kind, "duration_min": duration}


# --------------------------------------------------------------------------- segmentation écrit

EX_RE = re.compile(
    r"^\s*EXERCICE\s*(?:N°\s*)?(\d)\s*(?:[\(:\-–]\s*)?(?:sur\s*)?(?:(\d+(?:[,.]\d+)?)\s*points?)?",
    re.I | re.M,
)
THEME_RE = re.compile(
    r"(Cet exercice|L'exercice|Ce exercice)\s+(porte|traite|aborde|concerne|est consacré|utilise|mobilise|étudie)"
    r"[^.]*?(?:sur|de|à|des|les|la|le)?\s*(.+?)\.(?:\s|$)",
    re.I | re.S,
)
PART_RE = re.compile(r"^\s*Partie\s+([A-E]|\d)\b\s*[:\-–]?\s*(.*)$", re.I)
Q_RES = [
    # "Question A.1", "Question 3 :", "Question 2.b"
    re.compile(r"^\s*Question\s+((?:[A-E][\.\-]?)?\d{1,2}(?:[\.\-]?[a-z\d])?)\s*[\.:\-–)]?\s*(.*)$", re.I),
    # "A.1. ", "B.3) "
    re.compile(r"^\s*([A-E]\.\d{1,2}(?:\.[a-z\d])?)\s*[\.)]\s*(.+)$"),
    # "1.a. ", "2.b) ", "3.2. "
    re.compile(r"^\s*(\d{1,2}\.(?:[a-h]|\d))\s*[\.)]\s*(.+)$"),
    # "1. Écrire ..."  (pas "1. 0" ni numéros de lignes de code)
    re.compile(r"^\s*(\d{1,2})\s*[\.)]\s+([A-ZÉÈÀÂÇÎÔa-zéèêàç«\"'(].*)$"),
    # "Q1. ", "Q.3 "
    re.compile(r"^\s*Q\.?\s?(\d{1,2}(?:\.[a-z\d])?)\s*[\.:)\-–]?\s*(.+)$"),
]
SUBQ_RE = re.compile(r"^\s*([a-h])\s*[\.)]\s+(.+)$")
INSTR_VERBS = (
    "écrire|ecrire|donner|expliquer|justifier|compléter|completer|recopier|déterminer|determiner|"
    "indiquer|proposer|calculer|montrer|démontrer|dessiner|représenter|representer|citer|préciser|"
    "preciser|décrire|decrire|identifier|modifier|implémenter|implementer|lister|établir|etablir|"
    "construire|tracer|nommer|traduire|vérifier|verifier|justifie|quel|quelle|quels|quelles|"
    "combien|pourquoi|comment|que|qu'|définir|definir|énoncer|enoncer|exprimer|évaluer|evaluer|"
    "choisir|associer|réécrire|reecrire|dire|écrivez|donnez|expliquez|complétez|corriger|"
    "estimer|comparer|déduire|deduire|rédiger|rediger|recopiez|sélectionner|selectionner|en déduire"
)
INSTR_RE = re.compile(rf"\b({INSTR_VERBS})\b", re.I)


def looks_like_code(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    return bool(
        re.match(r"^\d{1,3}\s{1,}\S", s) and not re.match(r"^\d{1,2}\s*[\.)]\s", s)
        or re.search(r"(def |return |class |for .* in |while |if .*:|==|!=|\[\d*\]|\(\)|=\s*\S|SELECT|FROM|WHERE|>>>)", s)
    )


def split_stem_context(lines: list[str]) -> tuple[str, str]:
    """Sépare l'énoncé propre de la question du texte de contexte qui suit
    (et qui sert en réalité de préambule à la question suivante)."""
    stem, ctx = [], []
    has_instr = False
    for i, ln in enumerate(lines):
        if ctx:
            ctx.append(ln)
            continue
        prev = stem[-1].strip() if stem else ""
        sentence_closed = prev.endswith((".", "?", "!")) or looks_like_code(prev)
        starts_new = bool(re.match(r"^\s*[A-ZÉÈÀÇ][a-zéèàêç]", ln)) and not looks_like_code(ln)
        if has_instr and sentence_closed and starts_new and not INSTR_RE.search(ln[:40]) and i > 0:
            ctx.append(ln)
            continue
        stem.append(ln)
        if INSTR_RE.search(ln):
            has_instr = True
    return "\n".join(stem).strip(), "\n".join(ctx).strip()


def segment_questions(body: str) -> tuple[str, list[dict]]:
    """Découpe le corps d'un exercice en questions. Renvoie (préambule, questions)."""
    lines = body.splitlines()
    starts = []  # (index_ligne, label, partie)
    part = None
    last_num, last_part = 0, None
    for i, ln in enumerate(lines):
        if (pm := PART_RE.match(ln)) and len(ln) < 120:
            part = pm.group(1).upper()
            starts.append((i, None, part, "part"))
            last_num = 0
            continue
        for rx in Q_RES:
            if (qm := rx.match(ln)):
                label = qm.group(1)
                # filtre : une liste numérotée sans verbe dans un préambule n'est pas une question,
                # sauf si elle suit exactement la numérotation attendue
                window = " ".join(lines[i:i + 8])
                top = re.match(r"(?:[A-E][\.\-]?)?(\d{1,2})", label)
                n = int(top.group(1)) if top else None
                sequential = n is not None and (n == last_num + 1 or (n == 1 and part != last_part))
                if (INSTR_RE.search(window) or "?" in window) and (sequential or n is None or n > last_num):
                    starts.append((i, label, part, "q"))
                    if n is not None:
                        last_num, last_part = n, part
                elif sequential:
                    starts.append((i, label, part, "q"))
                    last_num, last_part = n, part
                break
        else:
            if (sm := SUBQ_RE.match(ln)) and starts and starts[-1][3] in ("q", "sub"):
                window = " ".join(lines[i:i + 3])
                if INSTR_RE.search(window) or "?" in window:
                    starts.append((i, sm.group(1), part, "sub"))
    if not starts:
        return body.strip(), []
    preamble = "\n".join(lines[: starts[0][0]]).strip()
    questions = []
    carry = ""
    parent = None
    for k, (i, label, prt, typ) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        block = lines[i:end]
        if typ == "part":
            carry = (carry + "\n" + "\n".join(block)).strip()
            parent = None
            continue
        stem, ctx = split_stem_context(block)
        if typ == "q":
            parent = label
            full_label = label
        else:
            full_label = f"{parent}.{label}" if parent else label
        questions.append({
            "label": full_label, "part": prt, "is_sub": typ == "sub",
            "context_before": carry, "text": stem,
        })
        carry = ctx
    return preamble, questions


def segment_exam(text: str) -> list[dict]:
    matches = list(EX_RE.finditer(text))
    # pour chaque numéro d'exercice, préférer l'occurrence qui annonce un barème « (x points) »
    # et qui n'est pas une annexe ; garder l'ordre croissant
    best = {}
    for m in matches:
        n = int(m.group(1))
        tail = text[m.end():m.end() + 40].lower()
        score = (m.group(2) is not None) * 2 - ("annexe" in tail) * 3
        if n not in best or score > best[n][0]:
            best[n] = (score, m)
    kept, last = [], -1
    for n in sorted(best):
        m = best[n][1]
        if m.start() > last:
            kept.append(m)
            last = m.start()
    exercises = []
    for k, m in enumerate(kept):
        start = m.end()
        end = kept[k + 1].start() if k + 1 < len(kept) else len(text)
        body = text[start:end]
        pts = m.group(2)
        theme = None
        if (tm := THEME_RE.search(body[:900])):
            theme = re.sub(r"\s+", " ", tm.group(3)).strip()
        preamble, qs = segment_questions(body)
        exercises.append({
            "number": int(m.group(1)),
            "points": float(pts.replace(",", ".")) if pts else None,
            "theme_sentence": theme,
            "preamble": preamble,
            "questions": qs,
            "raw": body.strip(),
        })
    return exercises


# --------------------------------------------------------------------------- écrit

EXCLUDE = re.compile(r"corr|correc|corrig|solution", re.I)


def ingest_written() -> list[dict]:
    pdfs = []
    for base in [
        SOURCES / "trahobisoa_Terminale_NSI" / "Sujets Epreuve Ecrite",
        SOURCES / "glassus_terminale_nsi" / "docs" / "T6_Annales" / "data",
    ]:
        if base.exists():
            pdfs += [p for p in base.rglob("*.pdf") if not EXCLUDE.search(p.name)]
    print(f"[écrit] {len(pdfs)} PDF candidats")
    exams = []
    for p in sorted(pdfs):
        raw = pdf_text(p)
        if len(raw) < 2000:
            continue
        txt = clean_pdf_text(raw)
        head = strip_accents(txt[:3000].lower())
        if "correction" in head[:600] or "corrige" in head[:600] or "elements de correction" in head:
            continue
        meta = exam_metadata(p, txt)
        exs = segment_exam(txt)
        if len(exs) < 2:
            continue
        exams.append({
            "id": hashlib.md5(txt.encode()).hexdigest()[:10],
            "type": "ecrit", "source": str(p.relative_to(SOURCES)), **meta,
            "n_exercises": len(exs), "exercises": exs, "text": txt,
        })
    # déduplication (le même sujet existe dans plusieurs dépôts)
    vec = TfidfVectorizer(max_features=20000, ngram_range=(1, 2)).fit([e["text"] for e in exams])
    X = vec.transform([e["text"] for e in exams])
    sim = cosine_similarity(X)
    keep, dropped = [], set()
    order = sorted(range(len(exams)), key=lambda i: -sum(len(x["questions"]) for x in exams[i]["exercises"]))
    for i in order:
        if i in dropped:
            continue
        keep.append(exams[i])
        for j in range(len(exams)):
            if j != i and sim[i, j] > 0.80:
                dropped.add(j)
    print(f"[écrit] {len(exams)} sujets extraits -> {len(keep)} après déduplication")
    return sorted(keep, key=lambda e: (e["year"] or 0, e["center"] or "", e["day"] or 0))


# --------------------------------------------------------------------------- pratique

def ingest_practical() -> list[dict]:
    base = SOURCES / "glassus_terminale_nsi" / "includes"
    exams = {}
    for f in sorted(base.glob("*/files/*_*/enonce.md")):
        year = int(f.parts[-4])
        sujet, num = f.parent.name.split("_")[:2]
        txt = f.read_text(encoding="utf-8", errors="ignore").strip()
        if len(txt) < 80:
            continue
        key = (year, sujet)
        e = exams.setdefault(key, {
            "id": f"P{year}-{sujet}", "type": "pratique", "source": str(f.parent.parent.relative_to(SOURCES)),
            "year": year, "day": None, "center": "BNS", "kind": "officiel", "duration_min": 60,
            "exercises": [], "text": "",
        })
        e["exercises"].append({
            "number": int(num) if num.isdigit() else len(e["exercises"]) + 1,
            "points": 10.0, "theme_sentence": None, "preamble": "",
            "questions": [{"label": "1", "part": None, "is_sub": False, "context_before": "", "text": txt}],
            "raw": txt,
        })
        e["text"] += "\n\n" + txt
    out = list(exams.values())
    for e in out:
        e["n_exercises"] = len(e["exercises"])
    # dédupliquer les exercices identiques d'une année sur l'autre (la BNS est reconduite)
    seen, n_dup = set(), 0
    for e in out:
        for ex in e["exercises"]:
            h = hashlib.md5(re.sub(r"\W+", "", ex["raw"].lower()).encode()).hexdigest()
            ex["duplicate_of_previous_year"] = h in seen
            n_dup += h in seen
            seen.add(h)
    print(f"[pratique] {len(out)} sujets, {sum(e['n_exercises'] for e in out)} exercices ({n_dup} reconduits)")
    return out


# --------------------------------------------------------------------------- cours

MD_NOISE = [
    (re.compile(r"!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?"), ""),       # images
    (re.compile(r"\{\{[^}]*\}\}"), ""),                          # macros mkdocs
    (re.compile(r"\{[:.][^}]*\}"), ""),                          # attributs
    (re.compile(r"^\s*(!!!|\?\?\?\+?|===)\s*\w*\s*(\"[^\"]*\")?", re.M), ""),
    (re.compile(r"--8<--.*$", re.M), ""),
    (re.compile(r"\[([^\]]+)\]\([^)]*\)"), r"\1"),               # liens
    (re.compile(r"<[^>]+>"), ""),
]

CHAPTER_NAMES = {
    "T1": "Structures de données", "T2": "Programmation", "T3": "Algorithmique",
    "T4": "Bases de données", "T5": "Architecture, OS et réseaux",
    "T6_2": "Rappels de Première", "T6_5": "Algorithmes de Première",
}
PDF_PREFIX = {
    "ALGO": "Algorithmique", "AMSER": "Architecture, OS et réseaux", "BDD": "Bases de données",
    "LP": "Programmation", "SD": "Structures de données",
}


def clean_md(t: str) -> str:
    for rx, rep in MD_NOISE:
        t = rx.sub(rep, t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def split_md_sections(text: str) -> list[tuple[str, str]]:
    parts, title, buf = [], "Introduction", []
    for ln in text.splitlines():
        if re.match(r"^#{1,3}\s", ln):
            if buf:
                parts.append((title, "\n".join(buf)))
            title, buf = ln.lstrip("#").strip(), []
        else:
            buf.append(ln)
    if buf:
        parts.append((title, "\n".join(buf)))
    return parts


def ingest_course() -> list[dict]:
    secs = []
    docs = SOURCES / "glassus_terminale_nsi" / "docs"
    for f in sorted(docs.glob("T[1-5]_*/*/*.md")) + sorted(docs.glob("T6_[25]_*/cours.md")):
        if "Copie en conflit" in f.name:
            continue
        top = f.parts[len(docs.parts)]
        key = "T6_2" if top.startswith("T6_2") else "T6_5" if top.startswith("T6_5") else top[:2]
        chapter = CHAPTER_NAMES.get(key, top)
        lesson = f.parent.name if not top.startswith("T6") else top
        lesson = re.sub(r"^[\d.]+_", "", lesson).replace("_", " ")
        kind = "exercices" if "exercice" in f.stem else ("tp" if "TP" in f.stem else "cours")
        body = clean_md(f.read_text(encoding="utf-8", errors="ignore"))
        for title, txt in split_md_sections(body):
            if len(txt.strip()) < 120:
                continue
            secs.append({"source": "glassus", "chapter": chapter, "lesson": lesson,
                         "kind": kind, "title": title, "text": txt.strip()})
    tdir = SOURCES / "trahobisoa_Terminale_NSI"
    for f in sorted(tdir.glob("*.pdf")):
        pre = re.match(r"([A-Z]+)\d+", f.name)
        if not pre or pre.group(1) not in PDF_PREFIX:
            continue
        txt = clean_pdf_text(pdf_text(f))
        lesson = re.sub(r"^[A-Z]+\d+-", "", f.stem).replace("_", " ")
        # découpe en blocs ~1500 caractères sur frontières de paragraphes
        buf = ""
        for para in re.split(r"\n\s*\n", txt):
            buf += para + "\n\n"
            if len(buf) > 1500:
                secs.append({"source": "trahobisoa", "chapter": PDF_PREFIX[pre.group(1)], "lesson": lesson,
                             "kind": "cours", "title": lesson, "text": buf.strip()})
                buf = ""
        if len(buf) > 200:
            secs.append({"source": "trahobisoa", "chapter": PDF_PREFIX[pre.group(1)], "lesson": lesson,
                         "kind": "cours", "title": lesson, "text": buf.strip()})
    bo = tdir / "BO progamme Term NSI.pdf"
    if bo.exists():
        secs.append({"source": "BO", "chapter": "Programme officiel", "lesson": "Programme",
                     "kind": "programme", "title": "Programme officiel de Terminale NSI",
                     "text": clean_pdf_text(pdf_text(bo))})
    print(f"[cours] {len(secs)} sections ({sum(len(s['text']) for s in secs)//1000} k caractères)")
    return secs


def write_jsonl(path: Path, rows: list[dict]):
    with path.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.open(encoding="utf-8")]


def run():
    written = ingest_written()
    practical = ingest_practical()
    course = ingest_course()
    write_jsonl(CORPUS / "exams.jsonl", written + practical)
    write_jsonl(CORPUS / "course.jsonl", course)
    nq = sum(len(x["questions"]) for e in written for x in e["exercises"])
    print(f"[ok] {len(written)} sujets écrits ({nq} questions), {len(practical)} sujets pratiques")


if __name__ == "__main__":
    run()
