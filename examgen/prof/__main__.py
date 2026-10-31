"""python -m examgen.prof {profil,plan,probable,check} --sujets DIR --cours DIR --out DIR"""
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
    ap.add_argument("cmd", choices=["profil", "plan", "probable", "check"])
    ap.add_argument("--sujets", default="data/sources/droit_stmg")
    ap.add_argument("--cours", default="data/droit/cours")
    ap.add_argument("--out", default="output/droit")
    ap.add_argument("--refit", action="store_true")
    ap.add_argument("--plans", default="plans.json")
    a = ap.parse_args()
    Path(a.out).mkdir(parents=True, exist_ok=True)
    if a.cmd == "profil":
        a.refit = True
        load(a)
    elif a.cmd == "plan":
        ps = plan.write(load(a), Path(a.out))
        print(f"{len(ps)} plans -> {a.out}/plans/")
    elif a.cmd == "probable":
        prev = json.loads((Path(a.out) / "previsions.json").read_text(encoding="utf-8"))
        ps = plan.Planner(load(a)).probables(prev)
        (Path(a.out) / "plans_probables.json").write_text(json.dumps(ps, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
        print(f"{len(ps)} plans probables -> {a.out}/plans_probables.json")
    else:
        t = load(a)
        ps = json.loads((Path(a.out) / a.plans).read_text(encoding="utf-8"))
        prob = a.plans != "plans.json"
        s = check.run(t, ps, Path(a.out) / ("generated_probables" if prob else "generated"),
                      Path(a.out) / ("validation_probables.json" if prob else "validation.json"))
        t.save(Path(a.out))
        print(json.dumps(s, ensure_ascii=False))


if __name__ == "__main__":
    main()
