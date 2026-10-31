"""Rédaction des questions par le LLM (Opus 5.5, effort low).

Deux chemins :
  api     : appel direct à l'API Anthropic (nécessite ANTHROPIC_API_KEY)
  agents  : export des consignes dans output/prompts/*.md ; des agents Claude Code
            (Opus 5.5, effort low) écrivent output/generated/<id>.json
Les deux produisent le même format JSON (OUTPUT_SCHEMA).
"""
from __future__ import annotations

import json
import os
import sys

from .config import LLM_EFFORT, LLM_MODEL, OUT

PROMPTS = OUT / "prompts"
GENERATED = OUT / "generated"
for p in (PROMPTS, GENERATED):
    p.mkdir(parents=True, exist_ok=True)

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "exercices": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "numero": {"type": "integer"},
                "titre": {"type": "string"},
                "contexte": {"type": "string"},
                "questions": {"type": "array", "items": {
                    "type": "object",
                    "properties": {
                        "slot": {"type": "integer"},
                        "notion": {"type": "string"},
                        "enonce": {"type": "string"},
                        "points": {"type": "number"},
                        "reponse_attendue": {"type": "string"},
                    },
                    "required": ["slot", "notion", "enonce", "points", "reponse_attendue"],
                    "additionalProperties": False,
                }},
            },
            "required": ["numero", "titre", "contexte", "questions"],
            "additionalProperties": False,
        }},
    },
    "required": ["id", "exercices"],
    "additionalProperties": False,
}

SYSTEM = """Tu es concepteur de sujets du baccalauréat, spécialité NSI (Terminale).
Tu rédiges des questions NOUVELLES à partir d'un plan produit par une analyse statistique
de 83 sujets officiels (2021-2026) et du cours. Le plan fixe, question par question :
la notion visée, l'archétype (forme de la question), le niveau de Bloom, la position et le barème.

Règles :
- Respecte le plan dans l'ordre : une question par « slot », même notion, même archétype.
- Style officiel : consignes à l'infinitif (« Écrire une fonction… », « Justifier… »),
  code Python 3 complet et exécutable, lignes de code numérotées quand on demande de compléter,
  requêtes SQL standard, tableaux en Markdown.
- Le contexte d'exercice est original (pas de copie des exemples réels, qui ne servent qu'au ton).
- Chaque question est autonome dans sa formulation mais s'appuie sur le contexte de l'exercice ;
  quand le plan dit « dépend de la précédente », réutilise explicitement le résultat ou la
  fonction de la question précédente.
- Reste strictement dans le programme de Terminale NSI (extraits de cours fournis).
- reponse_attendue : corrigé bref mais exact (code complet si c'est du code).
- En mode banque, chaque question porte son propre mini-contexte dans « enonce » ; un seul
  exercice numéro 0 regroupe les questions.
Réponds uniquement avec le JSON demandé."""


def render_prompt(plan: dict) -> str:
    lines = [f"# Plan {plan['id']} ({plan['type']})", ""]
    if plan["type"] == "sujet":
        lines.append(plan["format"])
        for ex in plan["exercices"]:
            lines += ["", f"## Exercice {ex['numero']} ({ex['points']} points)",
                      f"Notions : {', '.join(ex['notions'])} — domaines : {', '.join(ex['domaines'])}",
                      f"Pistes de contexte (mots fréquents d'anciens scénarios, à réinventer) : {', '.join(ex['idee_de_contexte'])}",
                      "Extraits du cours :"]
            for c in ex["cours"]:
                lines.append(f"> [{c['ref']}]\n> " + c["texte"][:700].replace("\n", "\n> "))
            lines.append("Questions à rédiger :")
            for q in ex["questions"]:
                lines.append(
                    f"- slot {q['slot']} | notion={q['notion']} | archétype={q['archetype']} | Bloom={q['bloom_cible']} | "
                    f"{q['points']} pt | position={q['position_cible']} | dépend de la précédente={'oui' if q['depend_de_la_precedente'] else 'non'} | "
                    f"formulations typiques : {', '.join(q['formulations_typiques'])}")
                for ex_ in q["exemples_reels_de_style"]:
                    lines.append(f"    style réel : « {ex_[:220].strip()} »")
    elif plan["type"] == "inedit":
        lines += [f"Notion : {plan['notion']} ({plan['domaine']}) — questions JAMAIS POSÉES aux annales", "",
                  "Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les "
                  "manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des "
                  "vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que "
                  "les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une "
                  "vraie question. Ou bien le slot vise un détail du cours jamais interrogé.", "",
                  "Règles propres à ce mode :",
                  "- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, "
                  "schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.",
                  "- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : "
                  "imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.",
                  "- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.",
                  "", "Extraits du cours :"]
        for c in plan["cours"]:
            lines.append(f"> [{c['ref']}]\n> " + c["texte"][:900].replace("\n", "\n> "))
        lines.append("")
        lines.append("Questions à rédiger (points = 1 par défaut) :")
        for q in plan["questions"]:
            c = q["consigne"]
            lines += ["", f"- slot {q['slot']} | {q['mode']} | {q['nouveaute']} | position visée : {q['position']}",
                      f"    manière de demander {c['id']} : {c['nom']}" + (f" — {c['geste']}" if c["geste"] else "")]
            if c["gabarit"]:
                lines.append(f"    gabarit : {c['gabarit']}")
            for e in q["exemples_de_consigne_autres_notions"]:
                lines.append(f"    exemple réel (autre notion) : « {e[:240]} »")
            if q["mode"] == "combinaison_inedite":
                s = q["support"]
                lines.append(f"    support {s['id']} : {s['nom']}" + (f" — {s['geste']}" if s["geste"] else ""))
                for e in q["exemple_de_support_autre_notion"]:
                    lines.append(f"    exemple de support (autre notion) : « {e[:260]} »")
            else:
                lines.append(f"    détail du cours à évaluer ({q['lecon']}) : « {q['atome_du_cours']} »")
    else:
        lines += [f"Notion : {plan['notion']} ({plan['domaine']}) — banque de questions isolées", "Extraits du cours :"]
        for c in plan["cours"]:
            lines.append(f"> [{c['ref']}]\n> " + c["texte"][:900].replace("\n", "\n> "))
        lines.append("Questions à rédiger (exercice numéro 0, points = 1 par défaut) :")
        for q in plan["questions"]:
            lines.append(f"- slot {q['slot']} | archétype={q['archetype']} | Bloom={q['bloom_cible']} | formulations typiques : {', '.join(q['formulations_typiques'])}")
            for ex_ in q["exemples_reels_de_style"]:
                lines.append(f"    style réel : « {ex_[:220].strip()} »")
    lines += ["", f"Le champ id vaut « {plan['id']} »."]
    return "\n".join(lines)


def export_prompts(plans: list[dict]) -> list[str]:
    ids = []
    for pl in plans:
        (PROMPTS / f"{pl['id']}.md").write_text(render_prompt(pl), encoding="utf-8")
        ids.append(pl["id"])
    (PROMPTS / "_system.md").write_text(SYSTEM, encoding="utf-8")
    (PROMPTS / "_schema.json").write_text(json.dumps(OUTPUT_SCHEMA, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[ok] {len(ids)} consignes -> {PROMPTS}")
    return ids


def generate_api(plans: list[dict]) -> None:
    """Chemin API direct : Opus 5.5, effort low, sortie JSON contrainte par schéma."""
    import anthropic

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY absent : utiliser le chemin « agents » (voir README).")
    client = anthropic.Anthropic()
    for pl in plans:
        out = GENERATED / f"{pl['id']}.json"
        if out.exists():
            continue
        with client.messages.stream(
            model=LLM_MODEL,
            max_tokens=32000,
            system=SYSTEM,
            messages=[{"role": "user", "content": render_prompt(pl)}],
            output_config={"effort": LLM_EFFORT, "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA}},
        ) as stream:
            msg = stream.get_final_message()
        if msg.stop_reason == "refusal":
            print(f"  ! {pl['id']} refusé")
            continue
        if msg.stop_reason == "max_tokens":
            print(f"  ! {pl['id']} tronqué")
            continue
        text = next(b.text for b in msg.content if b.type == "text")
        out.write_text(json.dumps(json.loads(text), ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  · {pl['id']} ({msg.usage.output_tokens} tokens)")
