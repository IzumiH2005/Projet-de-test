"""Point d'entrée.

  python -m examgen.cli ingest              # PDF / Markdown -> data/corpus
  python -m examgen.cli analyze             # 14 modèles -> data/model + rapport
  python -m examgen.cli plan --sujets 2 --par-notion 4
  python -m examgen.cli write --backend api|agents
  python -m examgen.cli validate
  python -m examgen.cli all                 # tout sauf la rédaction par agents
"""
from __future__ import annotations

import argparse
import json

from .config import OUT


def main():
    ap = argparse.ArgumentParser(prog="examgen")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ingest")
    sub.add_parser("analyze")
    p = sub.add_parser("plan")
    p.add_argument("--sujets", type=int, default=2)
    p.add_argument("--par-notion", type=int, default=4)
    p.add_argument("--seed", type=int, default=42)
    w = sub.add_parser("write")
    w.add_argument("--backend", choices=["api", "agents"], default="agents")
    sub.add_parser("validate")
    sub.add_parser("report")
    a = sub.add_parser("all")
    a.add_argument("--sujets", type=int, default=2)
    a.add_argument("--par-notion", type=int, default=4)
    args = ap.parse_args()

    if args.cmd in ("ingest", "all"):
        from . import ingest
        ingest.run()
    if args.cmd in ("analyze", "all"):
        from . import analysis, report
        analysis.run()
        report.run()
    if args.cmd == "report":
        from . import report
        report.run()
    if args.cmd in ("plan", "all"):
        from . import blueprint, llm
        plans = blueprint.make_plans(args.sujets, args.par_notion, getattr(args, "seed", 42))
        llm.export_prompts(plans)
    if args.cmd == "write":
        from . import llm
        plans = json.loads((OUT / "plans.json").read_text(encoding="utf-8"))
        if args.backend == "api":
            llm.generate_api(plans)
        else:
            llm.export_prompts(plans)
            print("Consignes prêtes : faire rédiger chaque output/prompts/<id>.md par un agent Opus 5.5 (effort low)"
                  " qui écrit output/generated/<id>.json au format output/prompts/_schema.json.")
    if args.cmd == "validate":
        from . import validate
        validate.run()
        validate.render_markdown()


if __name__ == "__main__":
    main()
