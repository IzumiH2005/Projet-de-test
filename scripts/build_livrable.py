"""Construit output/livrable.html : les anciens sujets analysés + les questions générées.

Usage : python scripts/build_livrable.py   (après `python -m examgen.cli validate`)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from examgen import features as F  # noqa: E402

OUT = ROOT / "output"
CORPUS = ROOT / "data" / "corpus"
MODEL = ROOT / "data" / "model"

LABELS = {
    "poo": "Programmation objet", "pile": "Piles", "file": "Files", "liste_chainee": "Listes chaînées",
    "dictionnaire": "Dictionnaires", "arbre_binaire": "Arbres binaires", "abr": "Arbres binaires de recherche",
    "parcours_arbre": "Parcours d'arbres", "graphe": "Graphes", "parcours_graphe": "Parcours de graphes",
    "interface_tad": "Interface et TAD", "tableau_liste": "Tableaux / listes", "tuple": "Tuples",
    "matrice": "Matrices", "recursivite": "Récursivité", "modularite": "Modularité", "mise_au_point": "Tests et mise au point",
    "paradigmes": "Paradigmes", "calculabilite": "Calculabilité", "fonctions": "Fonctions", "chaines": "Chaînes de caractères",
    "representation_nombres": "Représentation des nombres", "tri": "Tris", "recherche_dichotomique": "Recherche dichotomique",
    "diviser_regner": "Diviser pour régner", "prog_dynamique": "Programmation dynamique", "glouton": "Algorithmes gloutons",
    "recherche_textuelle": "Recherche textuelle", "complexite": "Complexité", "k_ppv": "k plus proches voisins",
    "algo_simples": "Algorithmes simples", "modele_relationnel": "Modèle relationnel", "sql": "SQL", "sgbd": "SGBD",
    "processus": "Processus", "os_commandes": "Commandes du système", "routage": "Routage", "reseau_ip": "Réseau IP",
    "soc_architecture": "Architecture / SoC", "securite_crypto": "Sécurité et chiffrement", "web_http": "Web et HTTP",
    "donnees_tables": "Données en table",
}
DOMAIN = {c: d for c, (d, _) in F.CONCEPTS.items()}


def read_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8")]


def exam_link(src: str) -> tuple[str, str] | None:
    if src.startswith("sujetdebac/"):
        f = src.split("/", 1)[1]
        y = re.search(r"-(20\d\d)-", f).group(1)
        return f"https://www.sujetdebac.fr/annales-pdf/{y}/{f}", "sujetdebac.fr"
    if src.startswith("glassus_terminale_nsi/"):
        return "https://github.com/glassus/terminale_nsi/blob/main/" + quote(src.split("/", 1)[1]), "glassus (GitHub)"
    if src.startswith("trahobisoa_Terminale_NSI/"):
        return "https://github.com/trahobisoa/Terminale_NSI/blob/Cours/" + quote(src.split("/", 1)[1]), "trahobisoa (GitHub)"
    return None


def clean(t: str, n: int) -> str:
    t = re.sub(r"\s+", " ", t or "").strip()
    return t[:n] + ("…" if len(t) > n else "")


def exams():
    ex = [e for e in read_jsonl(CORPUS / "exams.jsonl") if e["type"] == "ecrit"]
    rows, seen = [], {}
    pref = {"sujetdebac.fr": 0, "glassus (GitHub)": 1, "trahobisoa (GitHub)": 2}
    for e in ex:
        ln = exam_link(e["source"])
        if not ln:
            continue  # documents d'enseignants : gardés pour l'entraînement, pas listés comme annales
        themes = [clean(x.get("theme_sentence") or "", 110) for x in e["exercises"]]
        qs = [q for x in e["exercises"] for q in x["questions"] if len(q["text"]) > 60]
        sample = [clean(q["text"], 260) for q in qs[:: max(1, len(qs) // 3)][:3]]
        r = {"annee": e["year"], "centre": e["center"] or "Centre non précisé", "jour": e["day"], "type": e["kind"],
             "n_ex": e["n_exercises"], "n_q": sum(len(x["questions"]) for x in e["exercises"]),
             "url": ln[0], "src": ln[1], "themes": [t for t in themes if t], "extraits": sample}
        key = (e["year"], e["center"], e["day"]) if e["center"] and e["day"] else e["source"]
        if key in seen:
            old = seen[key]
            if pref[r["src"]] < pref[old["src"]]:
                old.update(r)
            continue
        seen[key] = r
        rows.append(r)
    rows.sort(key=lambda r: (-r["annee"], r["type"] != "officiel", r["centre"], r["jour"] or 0))
    return rows


def questions():
    plans = {p["id"]: p for p in json.loads((OUT / "plans_inedit.json").read_text(encoding="utf-8"))}
    val = json.loads((OUT / "validation.json").read_text(encoding="utf-8"))
    vd = {(d["id"], d.get("exercice"), d.get("slot")): d for d in val["detail"]}
    out = []
    for f in sorted((OUT / "generated").glob("*.json")):
        g = json.loads(f.read_text(encoding="utf-8"))
        gid = g["id"]
        kind = {"I": "inedit", "B": "banque", "S": "sujet"}.get(gid[0], "autre")
        plan = plans.get(gid, {})
        pslots = {q["slot"]: q for q in plan.get("questions", [])}
        for x in g["exercices"]:
            for q in x["questions"]:
                v = vd.get((gid, x["numero"], q["slot"])) or vd.get((gid, None, q["slot"])) or {}
                ps = pslots.get(q["slot"], {}) if kind == "inedit" else {}
                n = q.get("notion", "")
                item = {"id": f"{gid}-{x['numero']}-{q['slot']}", "type": kind, "lot": gid, "notion": n,
                        "label": LABELS.get(n, n), "domaine": DOMAIN.get(n, "Autre"),
                        "titre": x.get("titre", ""), "contexte": x.get("contexte", "") if kind != "banque" else "",
                        "enonce": q["enonce"], "reponse": q.get("reponse_attendue", ""), "points": q.get("points"),
                        "checks": {k: v.get(k) for k in ("notion_ok", "consigne_top3_ok", "support_top3_ok", "plausible",
                                                           "combinaison_jamais_vue", "python_ok", "sql_ok", "quasi_copie")
                                   if k in v},
                        "nouveaute": v.get("nouveaute_sim_max")}
                if ps:
                    item.update({"mode": ps.get("mode"), "plausibilite": ps.get("plausibilite"),
                                 "position": ps.get("position"),
                                 "consigne": (ps.get("consigne") or {}).get("nom"),
                                 "support": (ps.get("support") or {}).get("nom"),
                                 "savoir": (ps.get("savoir") or {}).get("ref") if isinstance(ps.get("savoir"), dict) else None,
                                 "emprunts": [clean(t, 220) for t in (ps.get("exemples_de_consigne_autres_notions") or [])[:2]]})
                if kind == "sujet":
                    item["lot"] = f"Sujet généré {gid[1:]}"
                out.append(item)
    order = {"inedit": 0, "sujet": 1, "banque": 2}
    out.sort(key=lambda q: (order.get(q["type"], 3), q["domaine"], q["label"]))
    return out, val["resume"]


def model_summary(resume):
    d = json.loads((MODEL / "discovery.json").read_text(encoding="utf-8"))
    f = d["facettes"]
    before = ROOT / "output" / "avant_apres.json"
    ba = json.loads(before.read_text(encoding="utf-8")) if before.exists() else {}
    return {"exposition": d["corpus_d_exposition"], "nettoyage": d.get("auto_nettoyage", {}),
            "k_consigne": f["manieres_de_demander"]["k"], "k_support": f["types_de_support"]["k"],
            "stab_consigne": f["manieres_de_demander"].get("stabilite_finale"),
            "stab_support": f["types_de_support"].get("stabilite_finale"),
            "reglages": d.get("reglages_auto", {}), "cours": d.get("auto_apprentissage_cours", {}),
            "avant_apres": ba, "validation": resume}


def droit():
    """Onglet Droit : le profil appris du professeur, les cas générés et les annales lues."""
    D = OUT / "droit"
    if not (D / "profil.json").exists():
        return None
    prof = json.loads((D / "profil.json").read_text(encoding="utf-8"))
    plans = {p["id"]: p for p in json.loads((D / "plans.json").read_text(encoding="utf-8"))}
    val = json.loads((D / "validation.json").read_text(encoding="utf-8")) if (D / "validation.json").exists() else {"resume": {}, "detail": []}
    vd = {r["id"]: r for r in val["detail"]}
    items = []
    for f in sorted((D / "generated").glob("*.json")):
        g = json.loads(f.read_text(encoding="utf-8"))
        pl, v = plans.get(g["id"], {}), vd.get(g["id"], {})
        vq = {q["slot"]: q for q in v.get("questions", [])}
        items.append({"id": g["id"], "type": g.get("type") or pl.get("type"), "titre": g.get("titre", ""),
                      "section": pl.get("section_titre"), "partenaire": pl.get("partenaire_titre"),
                      "inedit": pl.get("inedit"), "proba": pl.get("proba_annee_suivante"), "freq": pl.get("frequence_passee"),
                      "situation": g.get("situation", ""),
                      "annexes": [{"titre": a.get("titre", ""), "texte": a.get("texte", ""), "source": a.get("source"),
                                   "ok": v["annexes"][i].get("ok") if i < len(v.get("annexes") or []) else None}
                                  for i, a in enumerate(g.get("annexes") or [])],
                      "questions": [{"slot": q.get("slot"), "situation": q.get("situation", ""), "enonce": q.get("enonce", ""),
                                     "points": q.get("points"), "reponse": q.get("reponse_attendue", ""),
                                     "checks": {k: vq.get(q.get("slot"), {}).get(k) for k in
                                                ("facette_ok", "section_ok", "articles_ok", "nouveaute_ok", "longueur_ok", "formule_rituelle")}}
                                    for q in g.get("questions", [])]})
    order = {"sujet_blanc": 0, "cas": 1, "exercices": 2}
    items.sort(key=lambda x: (order.get(x["type"], 3), [int(n) if n.isdigit() else 0 for n in re.findall(r"\d+", x["id"])]))
    ann = {}
    for f in sorted((ROOT / "data" / "sources" / "droit_stmg").glob("*.pdf")):
        m = re.match(r"stmg-spe-droit-economie-(\d{4})-(.+?)-(sujet|corrige)", f.stem)
        if not m:
            continue
        y, lieu, kind = m.groups()
        lieu = re.sub(r"-(officiel|sujet|corrige)$", "", lieu)
        r = ann.setdefault((y, lieu), {"annee": int(y), "lieu": lieu.replace("-", " ").capitalize(), "sujet": None, "corrige": None})
        r[kind] = f"https://www.sujetdebac.fr/annales-pdf/{y}/{f.name}"
    ann = sorted(ann.values(), key=lambda r: (-r["annee"], r["lieu"]))
    mf, ts = prof["manieres_de_demander"], prof["types_de_supports"]
    prof_out = {
        "corpus": prof["corpus"], "pertinence": {k: prof["pertinence_des_parties"][k] for k in ("parties_gardees", "parties_ecartees")},
        "alignement": prof["alignement_sur_le_cours"], "consigne_mots": prof["vocabulaire_de_consigne"].get("exemples_consigne", [])[:12],
        "facettes": [{"nom": f["nom"], "n": f["n"], "place": f["position_moyenne"], "ex": clean(f["exemples"][0], 200)} for f in mf["facettes"]],
        "squelette": prof["squelette"]["squelette_typique"], "par_partie": prof["squelette"]["questions_par_partie"],
        "verdict": prof["previsibilite_consigne"]["verdict"], "logloss": prof["previsibilite_consigne"]["log_loss_sujet_exclu"],
        "rituels": prof.get("formules_rituelles", {}),
        "supports": [{"nom": t["nom"], "n": t["n"], "titres": [clean(x, 80) for x in t["exemples_de_titres"][:2]],
                      "reprise": ts.get("taux_de_reprise_de_sources", {}).get(t["nom"]),
                      "dates": ts.get("part_de_documents_dates", {}).get(t["nom"])} for t in ts["types"]],
        "detail": {k: prof["niveau_de_detail"][k] for k in ("chars_par_point_p10_p50_p90", "references_citees_par_reponse_moyenne")},
        "correcteur": prof["niveau_de_detail"]["consignes_de_correction"][:5],
        "proba": list(prof["probabilite_annee_suivante"].items())[:8],
        "prev_sections": prof["previsibilite_sections"],
    }
    return {"profil": prof_out, "items": items, "validation": val["resume"], "annales": ann}


def meta():
    f = OUT / "meta" / "rapport.json"
    if not f.exists():
        return None
    r = json.loads(f.read_text(encoding="utf-8"))
    al = r["alignement"]["matiere_exclue"]
    per = r["intentions"]["par_matiere"]
    tasks = {n: {k: {kk: v.get(kk) for kk in ("score_sujets_exclus", "auc_popularite_du_passage", "log_loss_rang_seul", "log_loss_avec_relation_au_cours")}
                 for k, v in p["taches"].items()} for n, p in per.items()}
    types = {n: [{k: t[k] for k in ("n", "fort", "faible")} | {"ex": t["exemples"][0]} for t in sorted(p["types_d_intention"]["types"], key=lambda t: -t["n"])]
             for n, p in per.items()}
    impl = {n: [x for x in p["ce_qui_est_evalue_sans_etre_dit"] if x["mots"]][:3] for n, p in per.items()}
    return {"alignement": al, "universelles": [u for u in r["intentions"]["universelles"] if u["meme_sens"]],
            "taches": tasks, "types": types, "implicite": impl, "regle": r["alignement"]["regle_finale"],
            "auto": {n: v["generations"] for n, v in r.get("auto_entrainement", {}).items()},
            "avant_apres": r["intentions"].get("avant_apres_auto_entrainement", {}),
            "grand": r["intentions"].get("grande_echelle")}


def main():
    ex = exams()
    qs, resume = questions()
    data = {"exams": ex, "questions": qs, "modele": model_summary(resume), "droit": droit(), "meta": meta()}
    tpl = (ROOT / "scripts" / "livrable_template.html").read_text(encoding="utf-8")
    html = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    (OUT / "livrable.html").write_text(html, encoding="utf-8")
    print(f"[ok] {len(ex)} sujets, {len(qs)} questions -> {OUT / 'livrable.html'} ({len(html) // 1024} Ko)")


if __name__ == "__main__":
    main()
