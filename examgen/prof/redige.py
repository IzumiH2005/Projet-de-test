"""Rédaction générique, pour n'importe quelle matière, puis boucle « vérifier → corriger ».

Rien n'est propre à une matière : les consignes du rédacteur sont tirées du profil appris
(manières de demander, supports recopiés ou inventés, longueur des corrigés, intention cachée).
Chaque exercice rédigé passe au contrôle (check.Checker) ; ce que le contrôle reproche est
renvoyé au rédacteur, jusqu'à `tours` fois.

Deux chemins, même format de sortie (<out>/generated/<id>.json) :
  api     : appel direct à l'API Anthropic si ANTHROPIC_API_KEY est définie ;
  agents  : sinon, un prompt complet par plan dans <out>/prompts/<id>.md (avec les reproches
            du dernier contrôle s'il y en a), à faire rédiger par un agent.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

import numpy as np

from ..config import LLM_MODEL
from . import check
from .plan import teacher_brief

FORMAT = """{
  "id": "<id du plan>",
  "type": "<type du plan>",
  "titre": "titre court",
  "situation": "texte de la situation (cas et sujet complet)",
  "annexes": [{"titre": "Annexe 1 – …", "texte": "…", "source": "cours|documents_reels|invente"}],
  "questions": [
    {"slot": 1, "situation": "(exercices seulement : mini-cas de 3 à 6 lignes)",
     "enonce": "…", "points": 2, "reponse_attendue": "…", "articles_cites": []}
  ]
}"""


def consignes(t, name: str) -> str:
    """Consignes du rédacteur, écrites à partir de ce que le modèle a appris du professeur."""
    ck = check.Checker(t, [])
    nom = lambda f: "« " + (t.sup_facets[f].get("exemples_de_titres") or [t.sup_facets[f]["nom"]])[0][:70] + " »"
    recopie = [nom(f) for f, r in ck.src_rate.items() if r > 0.5]
    invente = [nom(f) for f, r in ck.src_rate.items() if r <= 0.5]
    d = t.detail_stats
    refs = d.get("references_citees_par_reponse_moyenne", 0) or 0
    sym = np.mean([len(re.findall(r"[(){}\[\]=<>;:_#]", q.stem)) / max(1, len(q.stem)) for q in t.Q]) if t.Q else 0
    L = [f"# Consignes du rédacteur ({name})", "",
         "Tu écris comme le professeur qui a conçu les anciens sujets. Le PROFIL ci-dessous est ce qu'un modèle",
         "scikit-learn a appris de lui. Pour chaque plan, tu rends un JSON au format donné à la fin.", "",
         "## Penser comme le professeur",
         "- Étudie `anciens_sujets_proches` : comment il pose une situation, annonce les documents, tourne chaque",
         "  question et ce que son corrigé attend. Ne recopie jamais une situation ancienne.",
         "- Pour chaque `questions[slot]`, reprends la manière de demander de la facette : imite la tournure de",
         "  ses `exemples_reels` (même verbe de consigne, même construction), sans les copier.",
         "- Le contenu vient de `cours` (et `cours_partenaire`) : la question fait travailler les notions de la",
         "  section visée. Si `inedit` est vrai, la section n'est jamais ou presque tombée : écris la question",
         "  qu'il pourrait poser, avec sa façon de faire.",
         "- Si le plan a une `intention_cachee` : la question la plus lourde porte sur `passage_vise` ;",
         "  l'énoncé ne nomme PAS les notions de `evaluer_sans_le_dire`, le corrigé les exige.", "",
         "## Documents"]
    if recopie:
        L.append(f"- Types que ce professeur reprend tels quels ({'; '.join(recopie)}) : recopie mot pour mot un texte fourni"
                 " dans `cours` ou `documents_reels` (coupe avec « […] »). N'invente ni texte, ni date, ni référence.")
    if invente:
        L.append(f"- Types qu'il fabrique pour le cas ({'; '.join(invente)}) : invente-les, cohérents avec la situation ;"
                 " un document chiffré inventé porte la mention « données fictives ».")
    L.append("- Indique pour chaque document `source` : `cours`, `documents_reels` ou `invente`.")
    L += ["", "## Corrigé",
          "- Écris le corrigé comme les siens, longueur `longueur_cible_car` (dans `longueur_reponse_car`)."]
    if refs >= 0.3:
        L.append("- `articles_cites` : seulement des références présentes dans les textes fournis.")
    if sym > 0.03:
        L.append("- Code et notations : complets, exacts et exécutables quand c'est du code.")
    L += ["", "## Format (JSON valide, rien d'autre)", "```json", FORMAT, "```",
          "Pour le type `exercices`, chaque question a sa courte `situation`. Garde les `slot` et `points` du plan."]
    return "\n".join(L)


def _user(plan: dict, revision: list[str] | None) -> str:
    u = "PLAN\n```json\n" + json.dumps(plan, ensure_ascii=False, indent=1, default=float) + "\n```"
    if revision:
        u += "\n\nLe contrôle automatique a relevé dans ta version précédente :\n" + "\n".join(f"- {r}" for r in revision) + \
             "\nRéécris l'exercice complet en corrigeant ces points."
    return u


def _parse(txt: str) -> dict:
    m = re.search(r"\{.*\}", txt, re.S)
    return json.loads(m.group(0)) if m else {}


def _ask(client, system: str, user: str) -> str:
    msgs = [{"role": "user", "content": user}]
    with client.messages.stream(model=LLM_MODEL, max_tokens=16000, system=system, messages=msgs,
                                thinking={"type": "adaptive"}) as s:
        m = s.get_final_message()
    return "".join(b.text for b in m.content if b.type == "text")


def run(t, plans: list[dict], out: Path, name: str, tours: int = 2, gen_sub: str = "generated", log=print) -> dict:
    out = Path(out)
    gen, pr = out / gen_sub, out / "prompts"
    gen.mkdir(parents=True, exist_ok=True)
    system = consignes(t, name) + "\n\n" + teacher_brief(t)
    (out / "consignes_redacteur_auto.md").write_text(system, encoding="utf-8")
    ck = check.Checker(t, plans)
    key = os.environ.get("ANTHROPIC_API_KEY")
    stats = {"plans": len(plans), "chemin": "api" if key else "agents", "corriges_par_la_boucle": 0, "ok_au_premier_jet": 0}
    if not key:
        pr.mkdir(parents=True, exist_ok=True)
        n = 0
        for p in plans:
            f = gen / f"{p['id']}.json"
            rev = None
            if f.exists():  # déjà rédigé : on renvoie seulement ce que le contrôle reproche
                try:
                    rev = ck.check_item(json.loads(f.read_text(encoding="utf-8")))["revision"] or None
                except (ValueError, KeyError):
                    rev = ["JSON invalide"]
                if not rev:
                    continue
            (pr / f"{p['id']}.md").write_text(f"{system}\n\n{_user(p, rev)}\n\nÉcris le résultat dans `{f}`.\n", encoding="utf-8")
            n += 1
        stats["prompts"] = n
        log(f"  {stats['prompts']} prompts -> {pr} (pas de clé API : à faire rédiger par un agent)")
        return stats
    import anthropic
    client = anthropic.Anthropic()
    for p in plans:
        rev, g = None, {}
        for k in range(tours + 1):
            try:
                g = _parse(_ask(client, system, _user(p, rev)))
            except (ValueError, anthropic.APIError) as e:
                rev = [f"réponse illisible : {e}"]
                continue
            g["id"] = p["id"]
            rev = ck.check_item(g)["revision"]
            if not rev:
                stats["ok_au_premier_jet" if k == 0 else "corriges_par_la_boucle"] += 1
                break
        (gen / f"{p['id']}.json").write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"  {p['id']} : {'ok' if not rev else f'{len(rev)} reproche(s) restants'}")
    return stats
