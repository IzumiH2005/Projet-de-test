"""Validation des questions générées par les modèles appris sur les annales.

Pour chaque question : on la repasse dans la même chaîne d'extraction que les vraies questions puis
  - notion   : le classifieur texte -> notions place-t-il la notion visée dans son top 3 ?
  - forme    : l'archétype prédit (KMeans) est-il celui du plan, ou au moins le même type de tâche ?
  - Bloom    : le verbe de consigne donne-t-il le niveau visé (à ±1) ?
  - nouveauté: similarité max avec les 2 668 vraies questions (> 0.92 = quasi-copie)
  - ancrage  : similarité max avec les sections du cours
  - code     : le code Python du corrigé compile-t-il ? le code SQL a-t-il une forme valide ?
  - difficulté (sujets) : la position prédite par le modèle croît-elle avec la position voulue ?
"""
from __future__ import annotations

import ast
import json
import re
from collections import defaultdict

import joblib
import numpy as np
from scipy.stats import spearmanr

from . import features as F
from .config import MODEL_DIR, OUT
from .llm import GENERATED


def code_blocks(text: str) -> list[str]:
    blocks = re.findall(r"```(?:python|py)?\s*\n(.*?)```", text, re.S)
    if blocks:
        return blocks
    # sans balises : on garde le texte à partir de la première ligne qui ressemble à du code
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if re.match(r"\s*(def |class |from \w+ import|import \w+)", l)), None)
    return ["\n".join(lines[start:])] if start is not None else []


def python_ok(code: str) -> bool | None:
    code = re.sub(r"^\s*\d{1,3}\s{1,4}", "", code, flags=re.M) if re.search(r"^\s*\d{1,3}\s+(def|class|return|if|for|while)", code, re.M) else code
    if re.search(r"\b(SELECT|INSERT|UPDATE|DELETE)\b", code):
        return None
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


def sql_ok(text: str) -> bool | None:
    q = re.findall(r"((?:SELECT|INSERT|UPDATE|DELETE)\b.*?(?:;|$))", text, re.S | re.I)
    if not q:
        return None
    for s in q:
        s_up = s.upper()
        if s_up.startswith("SELECT") and " FROM " not in s_up.replace("\n", " "):
            return False
        if s.count("(") != s.count(")") or s.count("'") % 2:
            return False
    return True


def run() -> dict:
    m = joblib.load(MODEL_DIR / "models.joblib")
    plans = {}
    for name in ("plans.json", "plans_inedit.json"):
        if (OUT / name).exists():
            plans.update({p["id"]: p for p in json.loads((OUT / name).read_text(encoding="utf-8"))})
    fm = obs = ref = None
    if any(p["type"] == "inedit" for p in plans.values()) and (MODEL_DIR / "discovery_models.joblib").exists():
        from .discovery import FacetModel
        fm = FacetModel()
        dd = joblib.load(MODEL_DIR / "discovery_data.joblib")
        obs = {(n, int(c), int(s_)) for u, c, s_ in zip(dd["units"], dd["fs"], dd["fu"]) if u["src"] == "ecrit" for n in u["main"][:1]}
        ref = json.loads((MODEL_DIR / "discovery.json").read_text(encoding="utf-8"))["grammaire_des_combinaisons"]["plausibilite_mediane_des_vraies_questions"]
    gen = {}
    for f in sorted(GENERATED.glob("*.json")):
        try:
            g = json.loads(f.read_text(encoding="utf-8"))
            gen[g.get("id", f.stem)] = g
        except json.JSONDecodeError:
            print(f"  ! JSON invalide : {f.name}")
    vec, svd = m["vec"], m["svd"]
    km, clf, classes = m["km"], m["clf"], m["clf_classes"]
    Lq, Lc = m["Lq"], m["Lc"]
    results = []
    for pid, g in gen.items():
        plan = plans.get(pid)
        if not plan:
            continue
        plan_ex = {ex["numero"]: ex for ex in plan["exercices"]} if "exercices" in plan else {0: plan}
        for ex in g["exercices"]:
            pex = plan_ex.get(ex["numero"]) or next(iter(plan_ex.values()))
            pslots = {q["slot"]: q for q in pex["questions"]}
            qs = sorted(ex["questions"], key=lambda q: q["slot"])
            fake = {"id": pid, "type": "ecrit", "year": 2026, "center": "généré", "n_exercises": 3,
                    "exercises": [{"number": ex["numero"], "points": None, "theme_sentence": None,
                                   "preamble": ex["contexte"], "raw": ex["contexte"] + "\n" + "\n".join(q["enonce"] for q in qs),
                                   "questions": [{"label": str(q["slot"]), "text": q["enonce"],
                                                  "context_before": ex["contexte"][-400:] if plan["type"] in ("sujet", "inedit") else ""} for q in qs]}]}
            rows = F.build_question_table([fake])
            for r in rows:
                r["main"] = F.main_concepts(r)
            if not rows:
                continue
            texts = [r["text"] + "\n" + r["context"][-300:] for r in rows]
            X = vec.transform(texts)
            L = svd.transform(X)
            L /= np.linalg.norm(L, axis=1, keepdims=True) + 1e-9
            Xf, _ = F.feature_matrix(rows)
            stems = [" ".join(F.norm(r["text"]).split()[:18]) for r in rows]
            St = m["stem_svd"].transform(m["stem_vec"].transform(stems))
            Z = np.hstack([m["form_scaler"].transform(Xf[:, m["form_cols"]]), 3.0 * St / (np.linalg.norm(St, axis=1, keepdims=True) + 1e-9)])
            arch_pred = km.predict(Z)
            proba = clf.predict_proba(X)
            pos_pred = m["gb"].predict(np.hstack([Xf[:, m["gb_keep"]], L[:, :30]]))
            nov = (L @ Lq.T).max(1)
            grd = (L @ Lc.T).max(1)
            for i, (q, r) in enumerate(zip(qs, rows)):
                ps = pslots.get(q["slot"], {})
                target = ps.get("notion", q.get("notion"))
                top3 = [classes[j] for j in np.argsort(-proba[i])[:3]]
                a_plan = ps.get("archetype_id")
                info = m["arch_info"].get(a_plan, {}) if a_plan is not None else {}
                plan_task = info.get("taches", [[None]])[0][0]
                lvl_target = {"se souvenir": 1, "comprendre": 2, "appliquer": 3, "analyser": 4, "évaluer": 5, "créer": 6}.get(ps.get("bloom_cible"), None)
                pys = [python_ok(c) for c in code_blocks(q["reponse_attendue"])]
                pys = [p for p in pys if p is not None]
                sq = sql_ok(q["reponse_attendue"]) if target in ("sql", "modele_relationnel", "sgbd") else None
                results.append({
                    "id": pid, "type": plan["type"], "exercice": ex["numero"], "slot": q["slot"],
                    "notion": target, "notion_top3": top3,
                    "notion_ok": (target in top3) if target in classes else None,
                    "notion_lexique_ok": target in r["concepts"] or target in r["ex_concepts"],
                    "archetype_plan": a_plan, "archetype_predit": int(arch_pred[i]),
                    "archetype_ok": (int(arch_pred[i]) == a_plan) if a_plan is not None else None,
                    "tache_ok": (r["task"] == plan_task or m["arch_info"][int(arch_pred[i])]["taches"][0][0] == plan_task) if plan_task is not None else None,
                    "bloom_plan": lvl_target, "bloom_mesure": r["bloom"],
                    "bloom_ok": abs(r["bloom"] - lvl_target) <= 1 if lvl_target is not None else None,
                    "nouveaute_sim_max": round(float(nov[i]), 3), "quasi_copie": bool(nov[i] > 0.92),
                    "ancrage_cours": round(float(grd[i]), 3),
                    "python_ok": all(pys) if pys else None, "sql_ok": sq,
                    "position_cible": ps.get("position_cible"), "position_predite": round(float(pos_pred[i]), 3),
                })
                if plan["type"] == "inedit" and fm is not None:
                    fc = fm.facets(r["text"], r["context"])
                    c_plan, s_plan = ps.get("consigne_id"), ps.get("support_id")
                    pl = fm.plausibility(target, fc["consigne"], fc["support"], ps.get("position_bin", 1))
                    results[-1].update({
                        "mode": ps.get("mode"), "consigne_plan": c_plan, "consigne_mesuree": fc["consigne"],
                        "consigne_ok": fc["consigne"] == c_plan if c_plan is not None else None,
                        "consigne_top3_ok": fc["rang_consigne"][c_plan] < 3 if c_plan is not None else None,
                        "support_ok": fc["support"] == s_plan if s_plan is not None else None,
                        "support_top3_ok": fc["rang_support"][s_plan] < 3 if s_plan is not None else None,
                        "plausibilite_mesuree": round(pl, 3), "plausible": pl >= ref,
                        "combinaison_jamais_vue": (target, fc["consigne"], fc["support"]) not in obs,
                    })
    summary = summarize(results)
    (OUT / "validation.json").write_text(json.dumps({"resume": summary, "detail": results}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    return summary


def rate(rs, key):
    v = [r.get(key) for r in rs if r.get(key) is not None]
    return round(float(np.mean(v)), 3) if v else None


def summarize(results: list[dict]) -> dict:
    out = {"questions_validees": len(results)}
    for k in ("notion_ok", "notion_lexique_ok", "archetype_ok", "tache_ok", "bloom_ok", "python_ok", "sql_ok", "quasi_copie"):
        out[k] = rate(results, k)
    ined = [r for r in results if r["type"] == "inedit"]
    if ined:
        out["inedit"] = {"n": len(ined), **{k: rate(ined, k) for k in (
            "notion_ok", "notion_lexique_ok", "consigne_ok", "consigne_top3_ok", "support_ok", "support_top3_ok",
            "plausible", "combinaison_jamais_vue", "quasi_copie", "python_ok", "sql_ok")},
            "nouveaute_sim_max_moyenne": round(float(np.mean([r["nouveaute_sim_max"] for r in ined])), 3),
            "par_mode": {md: {"n": len(rs), "consigne_top3_ok": rate(rs, "consigne_top3_ok"), "notion_ok": rate(rs, "notion_ok")}
                         for md in {r["mode"] for r in ined} for rs in [[r for r in ined if r["mode"] == md]]}}
    out["nouveaute_sim_max_moyenne"] = round(float(np.mean([r["nouveaute_sim_max"] for r in results])), 3) if results else None
    out["ancrage_cours_moyen"] = round(float(np.mean([r["ancrage_cours"] for r in results])), 3) if results else None
    by_ex = defaultdict(list)
    for r in results:
        if r["type"] == "sujet" and r["position_cible"] is not None:
            by_ex[(r["id"], r["exercice"])].append(r)
    rhos = []
    for rs in by_ex.values():
        if len(rs) >= 4:
            rho = spearmanr([r["position_cible"] for r in rs], [r["position_predite"] for r in rs]).correlation
            if not np.isnan(rho):
                rhos.append(rho)
    out["difficulte_spearman_moyen"] = round(float(np.mean(rhos)), 3) if rhos else None
    per_type = defaultdict(list)
    for r in results:
        per_type[r["type"]].append(r)
    out["par_type"] = {t: {"n": len(rs), "notion_ok": rate(rs, "notion_ok"), "tache_ok": rate(rs, "tache_ok"), "bloom_ok": rate(rs, "bloom_ok")} for t, rs in per_type.items()}
    weak = defaultdict(list)
    for r in results:
        weak[r["notion"]].append(r["notion_ok"])
    out["notions_mal_reconnues"] = sorted(((n, round(float(np.mean([v for v in vs if v is not None])), 2)) for n, vs in weak.items() if any(v is not None for v in vs) and np.mean([v for v in vs if v is not None]) < 0.6), key=lambda t: t[1])
    return out


def render_markdown() -> None:
    """Fichier lisible : toutes les questions générées."""
    lines = ["# Questions générées (NSI Terminale)", ""]
    for f in sorted(GENERATED.glob("*.json")):
        g = json.loads(f.read_text(encoding="utf-8"))
        lines.append(f"## {g['id']}")
        for ex in g["exercices"]:
            if ex["numero"]:
                lines += [f"### Exercice {ex['numero']} — {ex['titre']}", "", ex["contexte"], ""]
            else:
                lines += [f"### {ex['titre']}", ""]
            for q in sorted(ex["questions"], key=lambda q: q["slot"]):
                lines += [f"**Q{q['slot']}** ({q['points']} pt, {q['notion']}) {q['enonce']}", "",
                          "<details><summary>Corrigé</summary>", "", q["reponse_attendue"], "", "</details>", ""]
    (OUT / "questions.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"[ok] {OUT / 'questions.md'}")
