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

FAM = {"popularite": "Popularité (déjà tombé souvent)", "logistique_12_generiques": "Logistique, 12 variables",
       "arbres_12_generiques": "Arbres boostés, 12 variables", "arbres_generiques_et_propres_a_la_matiere": "Arbres boostés + variables propres",
       "ensemble": "Moyenne des familles", "choisie_seule": "Famille choisie seule chaque année"}


NIV = ["incontournable", "probable", "peu ou jamais tombé, mais dans la manière du professeur", "à connaître"]


def _pool(D):
    """Tous les exercices déjà rédigés pour une matière : (id, titre, texte pour la similarité, questions)."""
    files = [("generated", D / "generated"), ("probables", D / "generated_probables")]
    if D.name == "nsi_prof":
        files = [("generated", OUT / "generated")]
    pool = []
    for _, d in files:
        for f in sorted(d.glob("*.json")) if d.exists() else []:
            g = json.loads(f.read_text(encoding="utf-8"))
            blocs = g.get("exercices") or [g]
            for x in blocs:
                qs = [{"enonce": q.get("enonce", ""), "reponse": q.get("reponse_attendue", ""), "points": q.get("points")} for q in x.get("questions", [])]
                if not qs:
                    continue
                kind = {"I": "Inédit", "B": "Banque", "S": "Sujet", "C": "Cas pratique", "E": "Série"}.get(g["id"][0], "Sujet probable")
                ctx = x.get("contexte") or x.get("situation") or ""
                nots = {LABELS.get(q.get("notion", ""), q.get("notion", "")) for q in x.get("questions", []) if q.get("notion")}
                pool.append({"id": g["id"] + (f"-{x['numero']}" if "numero" in x else ""), "type": kind, "titre": x.get("titre") or g.get("titre", ""),
                             "contexte": "" if ctx.startswith("Banque") else ctx[:1500], "questions": qs,
                             "_num": g["id"][1:] if g["id"][:1] in "CE" else None,
                             "_txt": " ".join([x.get("titre") or g.get("titre", "")] * 2 + [" ".join(nots)] * 3 + [ctx[:600]] + [q["enonce"] for q in qs])})
    return pool


def programme(D, pv, fac=None):
    """Tout le cours, chapitre par chapitre, avec les exercices qui s'y rapportent."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    prog, pool = pv.get("programme") or [], _pool(D)
    if not prog:
        return None
    ch_txt = [(r["titre"] + " ") * 3 + " ".join(k["texte"] for k in r["passages_cles"]) for r in prog]
    cache = ROOT / "data" / "cache" / f"prevision_{D.name.replace('_prof', '')}.joblib"
    if cache.exists():  # tout le texte du chapitre, pas seulement ses passages clés
        import joblib
        sys.path.insert(0, str(ROOT))
        t = joblib.load(cache)[0]
        ch_txt = [(r["titre"] + " ") * 3 + " ".join(t.pass_text[p] for p in range(len(t.pass_text)) if int(t.pass_sec[p]) == r["section"])
                  for r in prog]
    vec = TfidfVectorizer(sublinear_tf=True, strip_accents="unicode", min_df=1).fit(ch_txt + [e["_txt"] for e in pool])
    S = (vec.transform(ch_txt) @ vec.transform([e["_txt"] for e in pool]).T).toarray() if pool else None
    out = []
    for i, r in enumerate(prog):
        exs = []
        if S is not None:
            num = r["titre"].split(" ")[0]
            exact = [j for j, e in enumerate(pool) if e.get("_num") == num
                     or (e["titre"] and e["titre"].strip().lower() == r["titre"].strip().lower())]
            best = [j for j in S[i].argsort()[::-1] if S[i, j] >= 0.12 and j not in exact][: max(0, 4 - len(exact))]
            exs = [{k: v for k, v in pool[j].items() if not k.startswith("_")} for j in exact + best]
        if not exs and r["passages"] < 5:  # page d'introduction, rien à réviser
            continue
        k0 = r["passages_cles"]
        out.append({"titre": r["titre"], "niveau": r["niveau"], "rang": NIV.index(r["niveau"]) if r["niveau"] in NIV else 9,
                    "priorite": r["priorite"], "proba": r["proba"], "potentiel": r["potentiel"],
                    "tombe": r["annees_tombees"], "sur": r["sur"],
                    "cache": list(dict.fromkeys(w for k in k0 for w in k.get("evalue_sans_etre_dit", [])))[:8],
                    "nomme": list(dict.fromkeys(w for k in k0 for w in k.get("toujours_nomme", [])))[:5],
                    "manieres": [(fac or {}).get(m["facette"], m["nom"]) for m in (k0[0].get("manieres_de_demander") or [])][:3] if k0 else [],
                    "passages": [clean(k["texte"], 240) for k in k0[:2]],
                    "proches": list(dict.fromkeys(q["enonce"] for k in k0 for q in k.get("questions_passees_proches", [])))[:2],
                    "exercices": exs})
    return out


def probable():
    """Onglet « Le plus probable » : preuve sur les années passées, passages prévus, sujets probables."""
    out = []
    sys.path.insert(0, str(ROOT))
    from examgen.meta.domain import DOMAINS, out_dir
    noms = {"droit": "Droit (STMG)", "nsi": "NSI", "eco": "Économie (STMG)"}
    for k in DOMAINS:  # toutes les matières du registre
        D, nom = out_dir(k), noms.get(k, k.capitalize())
        if not (D / "previsions.json").exists():
            continue
        pv = json.loads((D / "previsions.json").read_text(encoding="utf-8"))
        pr = pv["preuve_comme_en_vrai"]
        fac = {}
        if (D / "profil.json").exists():
            prof = json.loads((D / "profil.json").read_text(encoding="utf-8"))
            fac = {i: clean(f["exemples"][0], 120) for i, f in enumerate(prof["manieres_de_demander"]["facettes"])}
        fams = [k for k in FAM if isinstance(pr.get(k), dict)]
        back = [{"famille": FAM[k], "cle": k, "auc": pr[k].get("auc"), "couv": pr[k].get("questions_couvertes"),
                 "pres": pr[k].get("questions_couvertes_a_un_passage_pres"), "ans": pr[k].get("par_annee", {})} for k in fams]
        pas = [{"section": x["section_titre"], "proba": x["probabilite"], "texte": clean(x["texte"], 260), "deja": x.get("deja_tombe"),
                "cache": x.get("evalue_sans_etre_dit", []), "nomme": x.get("toujours_nomme", []),
                "manieres": [{"ex": fac.get(m["facette"], m["nom"]), "part": m["part"]} for m in x.get("manieres_de_demander", [])],
                "proches": [q["enonce"] for q in x.get("questions_passees_proches", [])][:2]}
               for x in pv["passages_les_plus_probables"][:10]]
        plans = {}
        if (D / "plans_probables.json").exists():
            pl = json.loads((D / "plans_probables.json").read_text(encoding="utf-8"))
            plans = {p["id"]: p for p in (pl if isinstance(pl, list) else pl.get("plans", []))}
        vf = D / "validation_probables.json"
        val = json.loads(vf.read_text(encoding="utf-8")) if vf.exists() else {"resume": {}, "detail": []}
        vd = {r["id"]: r for r in val["detail"]}
        items = []
        for f in sorted((D / "generated_probables").glob("*.json")) if (D / "generated_probables").exists() else []:
            g = json.loads(f.read_text(encoding="utf-8"))
            p, v = plans.get(g["id"], {}), vd.get(g["id"], {})
            vq = {q["slot"]: q for q in v.get("questions", [])}
            items.append({"id": g["id"], "titre": g.get("titre", ""), "section": p.get("section_titre"), "partenaire": p.get("partenaire_titre"),
                          "proba": p.get("proba_annee_suivante"), "cache": (p.get("intention_cachee") or {}).get("evaluer_sans_le_dire", []),
                          "couverte": v.get("intention_cachee_couverte"), "situation": g.get("situation", ""),
                          "annexes": [{"titre": a.get("titre", ""), "texte": a.get("texte", "")} for a in g.get("annexes") or []],
                          "questions": [{"slot": q.get("slot"), "enonce": q.get("enonce", ""), "situation": q.get("situation", ""),
                                         "points": q.get("points"), "reponse": q.get("reponse_attendue", ""),
                                         "exige": vq.get(q.get("slot"), {}).get("intention_exigee_dans_le_corrige", []),
                                         "dit": vq.get(q.get("slot"), {}).get("intention_dite_dans_l_enonce", []),
                                         "ok": {k: vq.get(q.get("slot"), {}).get(k) for k in ("facette_ok", "section_ok", "articles_ok", "nouveaute_ok", "longueur_ok")}}
                                        for q in g.get("questions", [])]})
        out.append({"nom": nom, "annee": pv.get("annee_prevue"), "connues": pv.get("annees_connues"), "testees": pr.get("annees_testees"),
                    "n_pass": pr.get("passages_du_cours"), "n_prev": pr.get("passages_prevus"), "hasard": pr.get("hasard_questions_couvertes"),
                    "famille": FAM.get(pv.get("famille_choisie"), pv.get("famille_choisie")), "back": back, "passages": pas,
                    "items": items, "validation": val["resume"], "nouveautes": pv.get("preuve_sur_les_nouveautes"),
                    "auto": {"preuve": pv.get("preuve_auto_progression"),
                             "choix": {o: {"familles": [x.replace("_", " ") for x in (v.get("familles") or [])], "modele": v.get("modele")}
                                       for o, v in (pv.get("auto_progression") or {}).items()}},
                    "programme": programme(D, pv, fac)})
    return out or None


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
            "grand": r["intentions"].get("grande_echelle"),
            "boucle": {n: {"gen": v.get("boucle_intentions_alignement", []),
                           "familles": v.get("intentions_propres_a_la_matiere", {}).get("auc_par_famille", {}),
                           "choisie": v.get("intentions_propres_a_la_matiere", {}).get("famille_choisie"),
                           "auc": v.get("intentions_propres_a_la_matiere", {}).get("auc_famille_choisie_seule"),
                           "pop": v.get("intentions_propres_a_la_matiere", {}).get("auc_popularite"),
                           "regles": [x for x in v.get("intentions_propres_a_la_matiere", {}).get("regles_decouvertes", [])][:8],
                           "nvar": len(v.get("intentions_propres_a_la_matiere", {}).get("variables_propres_decouvertes", []))}
                       for n, v in r.get("auto_entrainement", {}).items() if v.get("boucle_intentions_alignement")}}


def main():
    ex = exams()
    qs, resume = questions()
    data = {"exams": ex, "questions": qs, "modele": model_summary(resume), "droit": droit(), "probable": probable(), "meta": meta()}
    tpl = (ROOT / "scripts" / "livrable_template.html").read_text(encoding="utf-8")
    html = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    (OUT / "livrable.html").write_text(html, encoding="utf-8")
    print(f"[ok] {len(ex)} sujets, {len(qs)} questions -> {OUT / 'livrable.html'} ({len(html) // 1024} Ko)")


if __name__ == "__main__":
    main()
