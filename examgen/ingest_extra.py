"""Matière supplémentaire d'exposition (aucune variable ajoutée à la main).

Sources :
  codex          exercices CodEx (forge.apps.education.fr) : énoncé + tags + difficulté (étiquettes faibles)
  qcm            banque de QCM de Terminale (forge projets-qcm)
  prof           exercices extraits des cours d'enseignants (blocs !!! / ??? et sections « Exercice »)
  entrainement   fiches PDF « type bac » non officielles des dépôts d'enseignants

Sorties (data/corpus/) :
  exposure.jsonl       même format que exams.jsonl (exercices -> questions), type = source
  course_extra.jsonl   sections de cours d'enseignants, sans chapitre (le modèle les étiquettera seul)
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

from .config import CORPUS, SOURCES
from .ingest import (EXCLUDE, clean_md, clean_pdf_text, is_official, pdf_text, segment_exam,
                     segment_questions, split_md_sections, strip_accents, write_jsonl)

CODEX = SOURCES / "forge_codex_codex.forge.apps.education.fr"
QCM = SOURCES / "forge_projets-qcm_qcm-nsi-terminale"
SKIP_REPOS = {CODEX.name, QCM.name}

ADM = re.compile(r"^(?P<ind>[ \t]*)(?:!!!|\?\?\?\+?)\s*(?P<typ>[\w-]+)(?P<title>[^\n]*)$", re.M)
SOLUTION = re.compile(r"solution|correction|corrig|réponse|reponse|indice|aide|astuce", re.I)
EXO_TYPES = {"example", "question", "exercice", "exo", "exercise", "ex", "travail", "faq", "abstract", "done"}
SUBQ = re.compile(r"(?m)^\s*(?:\*\*)?(Q\d+|\d+[.)]|[a-h][.)])(?:\*\*)?\s+(?=\S)")
FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)


def _hid(*parts) -> str:
    return hashlib.md5("|".join(map(str, parts)).encode()).hexdigest()[:10]


def _exam(typ, src, exercises, **meta):
    exercises = [x for x in exercises if x["questions"]]
    return {"id": f"{typ}-{_hid(src)}", "type": typ, "source": src, "year": None, "center": None, "day": None,
            "kind": typ, "duration_min": None, "n_exercises": len(exercises), "exercises": exercises, **meta}


def _exercise(num, preamble, questions, **extra):
    raw = preamble + "\n" + "\n".join(q["text"] for q in questions)
    return {"number": str(num), "points": None, "theme_sentence": None, "preamble": preamble,
            "raw": raw, "questions": questions, **extra}


def split_block(b: str) -> tuple[str, list[dict]]:
    """Découpe un bloc d'exercice en questions (sous-questions numérotées, sinon bloc unique :
    la consigne est le dernier paragraphe impératif, le reste sert de support)."""
    pre, qs = segment_questions(b)
    if len(qs) >= 2:
        return pre, qs
    cuts = [s.start() for s in SUBQ.finditer(b)]
    if len(cuts) >= 2:
        pre = b[:cuts[0]]
        parts = [b[s:e].strip() for s, e in zip(cuts, cuts[1:] + [len(b)])]
        return pre, [{"label": str(i + 1), "part": None, "is_sub": False,
                      "context_before": pre[-600:] if i == 0 else "", "text": p[:1500]}
                     for i, p in enumerate(parts) if len(p) > 15]
    paras = [p for p in re.split(r"\n\s*\n", b) if p.strip()]
    if not paras:
        return "", []
    from .ingest import INSTR_RE
    k = max((i for i, p in enumerate(paras) if INSTR_RE.search(p) or "?" in p), default=len(paras) - 1)
    # la consigne peut se prolonger par une liste à puces
    end = k + 1
    while end < len(paras) and re.match(r"\s*[-*•]", paras[end]):
        end += 1
    stem = "\n\n".join(paras[k:end])
    ctx = "\n\n".join(paras[:k] + paras[end:])
    return "", [{"label": "1", "part": None, "is_sub": False, "context_before": ctx[-1500:], "text": stem[:1500]}]


# ----------------------------------------------------------------------------------- CodEx
def _front(txt):
    m = FRONT.match(txt)
    meta = {}
    if not m:
        return meta, txt
    cur = None
    for ln in m.group(1).splitlines():
        if (kv := re.match(r"^(\w+):\s*(.*)$", ln)):
            cur = kv.group(1)
            meta[cur] = kv.group(2).strip() or []
        elif cur and (it := re.match(r"^\s+-\s*(.+)$", ln)) and isinstance(meta[cur], list):
            meta[cur].append(it.group(1).strip())
    return meta, txt[m.end():]


def _strip_solutions(txt: str) -> str:
    """Retire les blocs-réponses (admonitions dont le titre parle de solution/correction)."""
    out, skip_ind = [], None
    for ln in txt.splitlines():
        if skip_ind is not None:
            if not ln.strip() or len(ln) - len(ln.lstrip()) > skip_ind:
                continue
            skip_ind = None
        m = ADM.match(ln)
        if m and (SOLUTION.search(m.group("title")) or m.group("typ") in ("success", "done", "check")):
            skip_ind = len(m.group("ind").expandtabs(4))
            continue
        out.append(ln)
    return "\n".join(out)


def ingest_codex() -> list[dict]:
    out = []
    for kind in ("exercices", "exam"):
        for f in sorted((CODEX / "docs" / kind).glob("*/index.md")):
            meta, body = _front(f.read_text(encoding="utf-8", errors="ignore"))
            body = re.sub(r"`#!py ([^`]*)`", r"`\1`", _strip_solutions(body))
            body = re.sub(r"\{\{\s*IDE\([^}]*\}\}", "\n", body)
            b = clean_md(body)
            if len(b) < 80:
                continue
            pre, qs = split_block(b)
            if not qs:
                continue
            diff = meta.get("difficulty")
            tags = meta.get("tags") if isinstance(meta.get("tags"), list) else []
            ex = _exercise(1, pre, qs, title=meta.get("title"), tags=tags,
                           difficulty=int(diff) if isinstance(diff, str) and diff.isdigit() else None)
            out.append(_exam("codex", str(f.relative_to(SOURCES)), [ex], tags=tags,
                             difficulty=ex["difficulty"], center=meta.get("title")))
    print(f"[codex] {len(out)} exercices, {sum(len(x['questions']) for e in out for x in e['exercises'])} questions")
    return out


# ----------------------------------------------------------------------------------- QCM
def _txt(h: str) -> str:
    h = re.sub(r"<br\s*/?>|</p>|</li>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    return re.sub(r"[ \t\xa0]+", " ", html.unescape(h)).strip()


def ingest_qcm() -> list[dict]:
    seen, exams = set(), []
    for f in sorted(QCM.rglob("*.json")):
        try:
            data = json.load(f.open(encoding="utf-8"))
        except Exception:
            continue
        qs = data.get("questions") if isinstance(data, dict) else None
        if not isinstance(qs, list):
            continue
        exs = []
        for q in qs:
            if not (isinstance(q, list) and len(q) >= 2 and isinstance(q[1], list)):
                continue
            stem = _txt(q[0])
            key = re.sub(r"\W+", "", stem.lower())[:200]
            if len(stem) < 15 or key in seen:
                continue
            seen.add(key)
            choices = "\n".join(f"{chr(65 + i)}. {_txt(c)}" for i, c in enumerate(q[1]))
            exs.append(_exercise(len(exs) + 1, "", [{"label": "1", "part": None, "is_sub": False,
                                                     "context_before": "", "text": stem + "\n" + choices}]))
        if exs:
            exams.append(_exam("qcm", str(f.relative_to(SOURCES)), exs))
    n = sum(len(e["exercises"]) for e in exams)
    print(f"[qcm] {n} questions distinctes")
    return exams


# ----------------------------------------------------------------------------------- enseignants
def _md_files():
    for repo in sorted(SOURCES.glob("forge_*")):
        if repo.name in SKIP_REPOS:
            continue
        for f in sorted(repo.rglob("*.md")):
            if any(p.startswith(".") for p in f.relative_to(repo).parts) or EXCLUDE.search(f.name):
                continue
            yield repo, f


def _admonition_blocks(txt: str):
    lines = txt.splitlines()
    i = 0
    while i < len(lines):
        m = ADM.match(lines[i])
        if m and (m.group("typ").lower() in EXO_TYPES and not SOLUTION.search(m.group("title"))
                  or re.search(r"exercice|question|à faire", m.group("title"), re.I)):
            ind = len(m.group("ind").expandtabs(4))
            body = []
            j = i + 1
            while j < len(lines) and (not lines[j].strip() or len(lines[j].expandtabs(4)) - len(lines[j].expandtabs(4).lstrip()) > ind):
                body.append(lines[j].expandtabs(4)[ind + 4:] if lines[j].strip() else "")
                j += 1
            yield m.group("title").strip(' "'), "\n".join(body)
            i = j
        else:
            i += 1


def _heading_blocks(txt: str):
    for title, body in split_md_sections(txt):
        if re.search(r"\bexercices?\b|\bexo\b", title, re.I):
            yield title, body


def ingest_teacher_md() -> tuple[list[dict], list[dict]]:
    exams, course, seen = [], [], set()
    for repo, f in _md_files():
        raw = f.read_text(encoding="utf-8", errors="ignore")
        raw = FRONT.sub("", raw)
        exs = []
        for title, body in list(_admonition_blocks(raw)) + list(_heading_blocks(raw)):
            b = clean_md(re.sub(r"\{\{.*?\}\}", " ", _strip_solutions(body), flags=re.S)).strip()
            key = re.sub(r"\W+", "", b.lower())[:300]
            if len(b) < 60 or key in seen:
                continue
            seen.add(key)
            pre, qs = split_block(b)
            if qs:
                exs.append(_exercise(len(exs) + 1, pre, qs, title=title))
        rel = str(f.relative_to(SOURCES))
        if exs:
            exams.append(_exam("prof", rel, exs, center=f.parent.name))
        # sections de cours (hors fichiers d'exercices) : matière non étiquetée
        if not re.search(r"exo|exercice|td|tp|correction|qcm", f.stem, re.I):
            body = clean_md(_strip_solutions(re.sub(r"\{\{.*?\}\}", " ", raw, flags=re.S)))
            for title, txt in split_md_sections(body):
                key = re.sub(r"\W+", "", txt.lower())[:300]
                if len(txt.strip()) >= 200 and key not in seen:
                    seen.add(key)
                    course.append({"source": repo.name.removeprefix("forge_"), "chapter": None,
                                   "lesson": f.parent.name, "kind": "cours", "title": title,
                                   "file": rel, "text": txt.strip()[:6000]})
    print(f"[prof] {len(exams)} fichiers, {sum(len(e['exercises']) for e in exams)} exercices, "
          f"{sum(len(x['questions']) for e in exams for x in e['exercises'])} questions ; {len(course)} sections de cours")
    return exams, course


def ingest_training_pdfs() -> list[dict]:
    """Fiches PDF non officielles (TD, « type bac », bacs blancs) : énoncés sans correction."""
    out = []
    for repo in sorted(SOURCES.glob("forge_*")):
        for p in sorted(repo.rglob("*.pdf")):
            if EXCLUDE.search(str(p.relative_to(repo))):
                continue
            raw = pdf_text(p)
            if len(raw) < 800 or is_official(raw):
                continue
            txt = clean_pdf_text(raw)
            head = strip_accents(txt[:1500].lower())
            if "correction" in head or "corrige" in head or "solution" in head:
                continue
            exs = segment_exam(txt)
            if len(exs) < 2:
                pre, qs = segment_questions(txt)
                if len(qs) < 2:
                    continue
                exs = [_exercise(1, pre[-2000:], qs)]
            out.append(_exam("entrainement", str(p.relative_to(SOURCES)), exs, center=p.stem))
    print(f"[entraînement] {len(out)} fiches PDF, {sum(len(x['questions']) for e in out for x in e['exercises'])} questions")
    return out


def run():
    exposure = ingest_codex() + ingest_qcm()
    tex, course = ingest_teacher_md()
    exposure += tex + ingest_training_pdfs()
    write_jsonl(CORPUS / "exposure.jsonl", exposure)
    write_jsonl(CORPUS / "course_extra.jsonl", course)


if __name__ == "__main__":
    run()
