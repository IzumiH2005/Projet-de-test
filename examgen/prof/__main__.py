"""python -m examgen.prof {profil,plan,probable,check} --sujets DIR --cours DIR --out DIR

Tout d'un coup, pour n'importe quelle matière (anciens sujets + cours suffisent) :
  python -m examgen.prof tout --nom eco --sujets data/sources/droit_stmg --cours data/eco/cours
profil -> prévision (preuve comme en vrai) -> programme sur tout le cours -> plans -> rédaction
(API ou prompts) avec boucle vérifier-corriger -> contrôle -> livrable."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib

from . import check, plan, redige
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
    ap.add_argument("cmd", choices=["profil", "plan", "probable", "check", "redige", "tout"])
    ap.add_argument("--nom", default=None, help="nom de la matière (registre data/domaines.json)")
    ap.add_argument("--sujets", default="data/sources/droit_stmg")
    ap.add_argument("--cours", default="data/droit/cours")
    ap.add_argument("--out", default="output/droit")
    ap.add_argument("--refit", action="store_true")
    ap.add_argument("--plans", default="plans.json")
    a = ap.parse_args()
    if a.cmd == "tout":
        return tout(a)
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
    elif a.cmd == "redige":
        t = load(a)
        ps = json.loads((Path(a.out) / a.plans).read_text(encoding="utf-8"))
        prob = a.plans != "plans.json"
        print(redige.run(t, ps, Path(a.out), a.nom or Path(a.out).name, gen_sub="generated_probables" if prob else "generated"))
    else:
        t = load(a)
        ps = json.loads((Path(a.out) / a.plans).read_text(encoding="utf-8"))
        prob = a.plans != "plans.json"
        s = check.run(t, ps, Path(a.out) / ("generated_probables" if prob else "generated"),
                      Path(a.out) / ("validation_probables.json" if prob else "validation.json"))
        t.save(Path(a.out))
        print(json.dumps(s, ensure_ascii=False))


def tout(a):
    import subprocess
    import sys

    from ..meta import domain
    from . import forecast
    nom = a.nom or Path(a.cours).parent.name
    if a.sujets and a.cours and nom not in ("droit", "nsi"):
        domain.register(nom, a.sujets, a.cours)
    s, c = domain.DOMAINS[nom]
    a.sujets, a.cours, a.out = s, c, str(domain.out_dir(nom))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    print(f"[1/6] profil du professeur ({nom})")
    t = load(a)
    print("[2/6] plans d'exercices sur tout le cours")
    ps = plan.write(t, out)
    print("[3/6] prévision, preuve comme en vrai, programme")
    rep = forecast.run(nom)
    pp = plan.Planner(t).probables(rep)
    (out / "plans_probables.json").write_text(json.dumps(pp, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print("[4/6] rédaction (boucle vérifier-corriger)")
    for plans, sub in ((pp, "generated_probables"), (ps, "generated")):
        print("   ", redige.run(t, plans, out, nom, gen_sub=sub))
    print("[5/6] contrôle")
    for plans, sub, v in ((ps, "generated", "validation.json"), (pp, "generated_probables", "validation_probables.json")):
        if any((out / sub).glob("*.json")):
            print("   ", sub, json.dumps(check.run(t, plans, out / sub, out / v), ensure_ascii=False))
    t.save(out)
    print("[6/6] livrable")
    subprocess.run([sys.executable, str(Path(__file__).resolve().parents[2] / "scripts" / "build_livrable.py")], check=False)
    nv = rep["preuve_sur_les_nouveautes"]
    print(f"fini : {len(rep['programme'])} chapitres au programme ; nouveautés couvertes {nv.get('nouvelles_couvertes_par_le_quart_retenu')} "
          f"(hasard {nv.get('hasard')})")


if __name__ == "__main__":
    main()
