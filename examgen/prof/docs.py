"""Lecture et découpage génériques : sujets, corrigés, cours.

Rien ici ne dépend de la matière : on lit des PDF / Markdown / texte, on repère la numérotation
des questions, les titres de parties et d'annexes, et les titres du cours. Les seules hypothèses
sont typographiques (une question commence par « 1. », « 2) », « Question 3 », un cours a des titres).
"""
from __future__ import annotations

import re
import subprocess
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

CORR = re.compile(r"(corrig|correction|bareme|barème|solution)", re.I)
YEAR = re.compile(r"(?<!\d)(19[89]\d|20[0-4]\d)(?!\d)")


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        return subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True).stdout
    return path.read_text(encoding="utf-8", errors="ignore")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c)).replace("’", "'")


def strip_noise(text: str) -> list[str]:
    """Retire en-têtes / pieds de page : lignes courtes répétées sur plusieurs pages, numéros de page."""
    lines = [l.rstrip() for l in text.replace("\f", "\n").splitlines()]
    # numéro de question seul sur sa ligne (« 1 » puis l'énoncé plus bas) : on recolle
    merged, i = [], 0
    bare = lambda l: re.fullmatch(r"\s*(\d{1,2})\s*[.)]?\s*", l)
    while i < len(lines):
        # colonne de numéros (« 1. 2. 3. ») puis colonne d'énoncés : on apparie dans l'ordre
        run = []
        while i + len(run) < len(lines) and bare(lines[i + len(run)]):
            run.append(bare(lines[i + len(run)]).group(1))
        if len(run) >= 2 and [int(x) for x in run] == list(range(int(run[0]), int(run[0]) + len(run))):
            j, groups, buf = i + len(run), [], []
            while j < len(lines) and len(groups) < len(run):
                t = lines[j].strip()
                if t:
                    buf.append(t)
                    if re.search(r"[.?!]\s*[»\"]?\s*$", t):
                        groups.append(" ".join(buf)); buf = []
                j += 1
            if len(groups) == len(run):
                merged += [f"{n}. {g}" for n, g in zip(run, groups)] + [""]
                i = j
                continue
        m = re.fullmatch(r"\s*(\d{1,2})\s*[.)]?\s*", lines[i])
        if m:
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r"\s*[A-ZÉÈÀÂÎ][a-zéèêàâîôûç]", lines[j]) and j - i <= 3:
                merged.append(f"{m.group(1)}. {lines[j].strip()}")
                i = j + 1
                continue
        merged.append(lines[i])
        i += 1
    lines = merged
    cnt = Counter(l.strip() for l in lines if l.strip())
    out = []
    for l in lines:
        s = l.strip()
        if re.fullmatch(r"(page\s*)?\d+\s*(/|sur)\s*\d+", s, re.I) or re.fullmatch(r"\d{1,3}", s):
            continue
        if s and cnt[s] >= 3 and len(s) < 40:
            continue
        out.append(l)
    return out


# ------------------------------------------------------------------------------- sujets
@dataclass
class Question:
    exam: str
    part: str
    num: int
    stem: str
    preamble: str = ""          # texte d'amorce placé juste avant la question
    situation: str = ""         # mise en situation de la partie
    annexes: list = field(default_factory=list)   # [(titre, texte)]
    position: int = 0           # rang dans la partie (0..n-1)
    n_in_part: int = 0
    points: float | None = None
    answer: str = ""            # texte du corrigé
    year: int | None = None


QNUM = re.compile(r"^\s*(?:Question\s+)?(\d{1,2})\s*(?:[.)°]|-(?!\d)|–)\s*(?=\S)", re.I)
PART = re.compile(r"^\s*(PARTIE|Partie|EXERCICE|Exercice|DOSSIER|Dossier|SUJET|Sujet)\b[^.?]{0,60}$")
ANNEX = re.compile(r"^\s*(ANNEXE|Annexe|DOCUMENT|Document)\s*[A-Z0-9]{0,3}\b")
POINTS = re.compile(r"\(?\s*(\d{1,2}(?:[,.]\d+)?)\s*points?\s*\)?", re.I)


def _blocks(lines: list[str]):
    """Découpe en blocs typés : ('part', titre) | ('annex', titre) | ('q', num, ligne) | ('txt', ligne)."""
    for l in lines:
        s = l.strip()
        if not s:
            yield ("blank",)
        elif PART.match(s) and len(s) < 70:
            yield ("part", s)
        elif ANNEX.match(s) and len(s) < 160:
            yield ("annex", s)
        elif QNUM.match(s) and len(s) > 12:
            yield ("q", int(QNUM.match(s).group(1)), QNUM.sub("", s))
        else:
            yield ("txt", s)


def parse_exam(text: str, exam_id: str) -> list[Question]:
    lines = strip_noise(text)
    parts: list[dict] = []
    cur = {"title": "Sujet", "pre": [], "qs": [], "annexes": [], "mode": "pre"}
    parts.append(cur)
    last_q, major = None, ""
    for b in _blocks(lines):
        if b[0] == "part":
            title = b[1]
            # « SUJET 2 » sous une « PARTIE … » : sous-partie au choix, on garde la partie englobante
            if re.match(r"(?i)sujet\b", title) and major:
                title = f"{major} / {title}"
            elif not re.match(r"(?i)sujet\b", title):
                major = title
            cur = {"title": title, "pre": [], "qs": [], "annexes": [], "mode": "pre"}
            parts.append(cur)
            last_q = None
        elif b[0] == "annex":
            cur["annexes"].append([b[1], []])
            cur["mode"] = "annex"
        elif b[0] == "q" and cur["mode"] != "annex":
            expected = (last_q["num"] + 1) if last_q else 1
            if b[1] == expected or (last_q is None and b[1] <= 2):
                last_q = {"num": b[1], "lines": [b[2]], "pre": [], "open": True}
                cur["qs"].append(last_q)
                cur["mode"] = "q"
                continue
            _add_text(cur, last_q, b[2])
        elif b[0] == "txt":
            _add_text(cur, last_q, b[1])
        elif b[0] == "blank" and last_q is not None:
            last_q["open"] = False
    out = []
    year = YEAR.search(exam_id)
    for p in parts:
        if len(p["qs"]) < 2:
            continue
        sit = "\n".join(p["pre"]).strip()
        anx = [(t, "\n".join(x).strip()) for t, x in p["annexes"]]
        n = len(p["qs"])
        for i, q in enumerate(p["qs"]):
            stem = " ".join(q["lines"]).strip()
            m = POINTS.search(stem)
            pts = float(m.group(1).replace(",", ".")) if m and float(m.group(1).replace(",", ".")) <= 20 else None
            stem = POINTS.sub("", stem).strip() if pts else stem
            out.append(Question(exam_id, p["title"], q["num"], stem, " ".join(q["pre"]).strip(), sit, anx, i, n,
                                pts, "", int(year.group(1)) if year else None))
    return out


def _add_text(cur, last_q, s):
    if cur["mode"] == "annex" and cur["annexes"]:
        cur["annexes"][-1][1].append(s)
    elif last_q is None:
        cur["pre"].append(s)
    elif last_q["open"] and not re.search(r"[?.!]\s*$", " ".join(last_q["lines"])):
        last_q["lines"].append(s)       # suite de l'énoncé
    else:
        last_q["open"] = False
        # texte après une question terminée : amorce de la question suivante
        cur.setdefault("_pending", []).append(s)
        cur["pre_next"] = cur.get("pre_next", []) + [s]
        last_q.setdefault("after", []).append(s)


def attach_preambles(qs: list[Question], raw_parts=None):
    return qs


# ------------------------------------------------------------------------------- corrigés
def parse_correction(text: str, qs: list[Question], sim) -> dict:
    """Associe à chaque question du sujet son passage de corrigé : parmi les lignes numérotées du
    corrigé portant le même numéro, celle dont le texte ressemble le plus à l'énoncé."""
    lines = strip_noise(text)
    marks = []
    for i, l in enumerate(lines):
        m = QNUM.match(l.strip())
        if m and len(l.strip()) > 12:
            marks.append((i, int(m.group(1)), QNUM.sub("", l.strip())))
    if not marks:
        return {}
    # appariement un-à-un, glouton par similarité décroissante, en respectant l'ordre du sujet
    cands = sorted(((sim(q.stem, t + " " + " ".join(lines[i + 1:i + 3])), qi, i)
                    for qi, q in enumerate(qs) for i, n, t in marks if n == q.num), reverse=True)
    chosen, used = {}, set()
    for s, qi, i in cands:
        if s <= 0.25 or qi in chosen or i in used:
            continue
        before = [chosen[k] for k in chosen if k < qi]
        after = [chosen[k] for k in chosen if k > qi]
        if (before and i < max(before)) or (after and i > min(after)):
            continue
        chosen[qi] = i
        used.add(i)
    starts = sorted(set(chosen.values()))
    res = {}
    all_marks = [i for i, _, _ in marks]
    for qi, i in chosen.items():
        nxt = [j for j in starts if j > i]
        # fin : prochaine question retenue, ou prochain titre de partie
        end = nxt[0] if nxt else len(lines)
        for j in range(i + 1, end):
            if PART.match(lines[j].strip()) and len(lines[j].strip()) < 70:
                end = j
                break
        head = lines[i]
        m = POINTS.search(head) or POINTS.search(" ".join(lines[i + 1:i + 3]))
        pts = float(m.group(1).replace(",", ".")) if m else None
        body = "\n".join(lines[i + 1:end]).strip()
        res[qi] = {"answer": body[:6000], "points": pts if pts and pts <= 20 else None}
    return res


def course_refs(text: str, sections: list["Section"]) -> list[str]:
    """Sections du cours explicitement citées dans un corrigé (évaluation seulement)."""
    t = norm(text.split("Proposition de corrig")[0][:20000])
    hits = []
    for s in sections:
        if not s.num:
            continue
        title_words = {w for w in re.findall(r"[a-z]{4,}", norm(s.title))}
        for m in re.finditer(r"(?<![\d.])" + re.escape(s.num) + r"(?:\.\d)*\.?\s+([^\n]{0,80})", t):
            # le numéro doit être suivi d'un mot du titre (sinon : autre matière, autre numérotation)
            if title_words & set(re.findall(r"[a-z]{4,}", m.group(1))):
                hits.append(s.id)
                break
    return hits


# ------------------------------------------------------------------------------- cours
@dataclass
class Section:
    id: str
    num: str
    title: str
    parent: str
    text: str
    passages: list = field(default_factory=list)
    order: int = 0


def parse_course(paths: list[Path]) -> list[Section]:
    """Sections = titres de niveau 2 (## ou numérotation « 1.2 ») ; passages = paragraphes et
    sous-titres de niveau 3. Les titres de niveau 1 donnent le parent."""
    secs, parent, cur = [], "", None
    for p in sorted(paths):
        for raw in read_text(p).splitlines():
            l = raw.rstrip()
            m1 = re.match(r"^#\s+(.+)", l)
            m2 = re.match(r"^##\s+(.+)", l) or (re.match(r"^\s*((\d+\.\d+)\.?\s+[A-ZÉ].{3,80})$", l) if p.suffix == ".pdf" else None)
            if m1 and not l.startswith("##"):
                parent = m1.group(1).strip()
                continue
            if m2:
                title = m2.group(1).strip()
                num = re.match(r"(\d+(?:\.\d+)*)", title)
                cur = Section(f"s{len(secs)}", num.group(1) if num else "", title, parent, "", [], len(secs))
                secs.append(cur)
                continue
            if cur is None:
                continue
            cur.text += l + "\n"
    for s in secs:
        chunks = re.split(r"\n\s*\n|\n(?=### )", s.text)
        buf = []
        for c in chunks:
            c = c.strip()
            if not c:
                continue
            if c.startswith("### ") and "\n" not in c:
                buf.append(c[4:])  # titre seul : il sera collé au paragraphe suivant
                continue
            if buf:
                c = " — ".join(buf) + " : " + c
                buf = []
            if len(c) > 40:
                s.passages.append(re.sub(r"\s+", " ", c.replace("### ", "")))
    return [s for s in secs if s.passages]


# ------------------------------------------------------------------------------- lots
def pair_files(d: Path) -> list[tuple[str, Path, Path | None]]:
    files = [f for f in d.rglob("*") if f.suffix.lower() in (".pdf", ".md", ".txt")]
    key = lambda f: re.sub(r"[-_ ]*(sujet|officiel|enonce|énoncé|corrige|corrigé|correction|bareme)[-_ ]*", "-",
                           f.stem.lower()).strip("-")
    sujets = {key(f): f for f in files if not CORR.search(f.stem)}
    corr = {key(f): f for f in files if CORR.search(f.stem)}
    return [(k, f, corr.get(k)) for k, f in sorted(sujets.items())]
