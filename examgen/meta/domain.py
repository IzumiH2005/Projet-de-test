"""Chargement d'un domaine (sujets + cours) pour le méta-apprentissage.

Le moteur ne reçoit que les sujets et le cours. Une vérité terrain sert uniquement à JUGER le
méta-apprentissage, jamais au moteur lui-même :
  - droit : « références au programme » des corrigés officiels ;
  - NSI   : phrase de thème des exercices officiels (« Cet exercice porte sur… »).
"""
from __future__ import annotations

import re
from pathlib import Path

import joblib

from ..prof import docs as D
from ..prof.profile import Teacher

ROOT = Path(__file__).resolve().parents[2]
DOMAINS = {
    "droit": ("data/sources/droit_stmg", "data/droit/cours"),
    "nsi": ("data/sources/sujetdebac", "data/nsi/cours"),
}
# registre extensible : toute matière ajoutée par « python -m examgen.prof tout » (sujets + cours)
REGISTRY = ROOT / "data" / "domaines.json"


def _registry() -> dict:
    import json
    try:
        return {k: tuple(v) for k, v in json.loads(REGISTRY.read_text(encoding="utf-8")).items()}
    except (OSError, ValueError):
        return {}


DOMAINS.update(_registry())


def register(name: str, sujets: str | Path, cours: str | Path):
    import json
    rel = lambda p: str(Path(p).resolve().relative_to(ROOT)) if Path(p).resolve().is_relative_to(ROOT) else str(Path(p).resolve())
    reg = _registry()
    reg[name] = (rel(sujets), rel(cours))
    REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")
    DOMAINS[name] = reg[name]


def out_dir(name: str) -> Path:
    return ROOT / "output" / {"droit": "droit", "nsi": "nsi_prof"}.get(name, name)


def load(name: str, refresh: bool = False) -> Teacher:
    cache = ROOT / "data" / "cache" / f"meta_{name}.joblib"
    if cache.exists() and not refresh:
        return joblib.load(cache)
    s, c = DOMAINS[name]
    t = Teacher(ROOT / s, ROOT / c)
    t.relevant_parts()
    t.Q = [t.qs[i] for i in t.keep_idx]
    t.domain = name
    cache.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(t, cache)
    return t


def _toks(s: str) -> set[str]:
    return {w[:5] for w in re.findall(r"[a-z]{3,}", D.norm(s)) if w not in ("les", "des", "une", "sur", "langage")}


def eval_labels(t: Teacher) -> dict[int, set[int]]:
    """Index de question (dans t.Q) -> sections attendues. Évaluation seulement."""
    out = {}
    if any(t.refs.values()):
        for i, q in enumerate(t.Q):
            r = t.refs.get(q.exam)
            if r:
                out[i] = {int(x[1:]) for x in r}
        return out
    titles = [_toks(s.title) for s in t.sections]
    for i, q in enumerate(t.Q):
        m = re.search(r"[^.\n]*\b(porte|traite|aborde)\b[^.]*\.", q.situation[:600].replace("\n", " "))
        if not m:
            continue
        sent = _toks(m.group(0))
        hit = {si for si, tt in enumerate(titles) if tt and tt <= sent}
        if hit:
            out[i] = hit
    return out
