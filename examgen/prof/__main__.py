"""python -m examgen.prof {profil,plan,check} --sujets DIR --cours DIR --out DIR"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib

from . import check, plan
from .profile import Teacher


def load(a) -> Teacher:
    cache = Path(a.out) / "teacher.joblib"
    if cache.exists() and not a.refit:
        return joblib.load(cache)
    t = Teacher(Path(a.sujets), Path(a.cours)).run()
    t.save(Path(a.out))
    joblib.dump(t, cache)
    return t


def main():
    ap = argparse.ArgumentParser(prog="examgen.prof")
    ap.add_argument("cmd", choices=["profil", "plan", "check"])
    ap.add_argument("--sujets", default="data/sources/droit_stmg")
    ap.add_argument("--cours", default="data/droit/cours")
    ap.add_argument("--out", default="output/droit")
    ap.add_argument("--refit", action="store_true")
    a = ap.parse_args()
    Path(a.out).mkdir(parents=True, exist_ok=True)
    if a.cmd == "profil":
        a.refit = True
        load(a)
    elif a.cmd == "plan":
        ps = plan.write(load(a), Path(a.out))
        print(f"{len(ps)} plans -> {a.out}/plans/")
    else:
        t = load(a)
        ps = json.loads((Path(a.out) / "plans.json").read_text(encoding="utf-8"))
        s = check.run(t, ps, Path(a.out) / "generated", Path(a.out) / "validation.json")
        t.save(Path(a.out))
        print(json.dumps(s, ensure_ascii=False))


if __name__ == "__main__":
    main()
