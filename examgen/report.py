"""Rapport d'analyse lisible (output/rapport_analyse.md) à partir de data/model/analysis.json."""
from __future__ import annotations

import json

from .config import MODEL_DIR, OUT


def fmt_pairs(pairs, n=10):
    return ", ".join(f"{a} ({b})" for a, b, *_ in pairs[:n])


def run():
    r = json.loads((MODEL_DIR / "analysis.json").read_text(encoding="utf-8"))
    c = r["corpus"]
    L = ["# Analyse des annales NSI (Terminale)", "",
         f"Corpus : {c['sujets_ecrits']} sujets écrits uniques ({c['exercices_ecrit']} exercices, {c['questions_ecrit']} questions), "
         f"{c['sujets_pratiques']} sujets pratiques ({c['exercices_pratique']} exercices), {c['sections_cours']} sections de cours.",
         f"Années : {c['annees']}", ""]

    a = r["archetypes"]
    L += [f"## 1. Archétypes de questions ({a['k_choisi']} formes, KMeans + silhouette)", "",
          "| # | archétype (tâche / format / Bloom) | n | position moy. | code | dépend d'avant | formulations |", "|---|---|---|---|---|---|---|"]
    for k, v in sorted(a["detail"].items(), key=lambda t: -t[1]["effectif"]):
        L.append(f"| {k} | {v['nom']} | {v['effectif']} | {v['position_moyenne']} | {v['avec_code']} | {v['depend_d_avant']} | {', '.join(v['formulations'][:4])} |")

    m = r["markov"]
    L += ["", "## 2. Enchaînement des questions (chaîne de Markov)", "",
          f"- Ouvertures typiques : {fmt_pairs(m['ouvertures_frequentes'], 4)}",
          f"- Fermetures typiques : {fmt_pairs(m['fermetures_frequentes'], 4)}",
          f"- Entropie moyenne des transitions : {m['entropie_moyenne_bits']} bits",
          "- Transitions les plus fortes :"]
    L += [f"  - {x} → {y} ({p})" for x, y, p in m["transitions_fortes"][:10]]

    g = r["graphe_notions"]
    L += ["", "## 3. Relations entre notions (graphe PMI)", "",
          f"- {g['notions_par_exercice_moyenne']} notions par exercice en moyenne",
          f"- Notions pivots (PageRank) : {fmt_pairs(g['notions_pivots_pagerank'], 8)}",
          f"- Notions ponts (betweenness) : {fmt_pairs(g['notions_ponts_betweenness'], 6)}",
          "- Associations fortes (PMI, nb d'exercices) :"]
    L += [f"  - {k.replace('|', ' + ')} : PMI {v}, {n} exercices" for k, v, n in g["associations_fortes_PMI"][:12]]
    L += ["- Blocs thématiques cachés (communautés) :"] + [f"  - {', '.join(b)}" for b in g["blocs_thematiques_caches"]]

    s = r["logique_des_sujets"]
    L += ["", "## 4. Logique de construction d'un sujet", "",
          f"- Recouvrement des domaines entre exercices d'un même sujet : {s['recouvrement_domaines_entre_exercices_d_un_sujet']} "
          f"(hasard : {s['recouvrement_si_exercices_tires_au_hasard']}) → {s['lecture']}",
          f"- Domaines couverts par sujet : {s['domaines_couverts_par_sujet_moyenne']} sur 5",
          f"- Barèmes d'exercices : {s['baremes_exercices']}",
          "- Courbe à l'intérieur d'un exercice :", "", "| position | Bloom moyen | part code | part dépendante | mots |", "|---|---|---|---|---|"]
    L += [f"| {k} | {v['bloom']} | {v['code']} | {v['dependance']} | {v['mots']} |" for k, v in s["courbe_dans_un_exercice"].items()]

    d = r["difficulte"]
    L += ["", "## 5. Difficulté (Gradient Boosting, cible = position relative)", "",
          f"- R² en validation croisée par sujet : {d['R2_validation_croisee_par_sujet']}",
          f"- Placé en début d'exercice : {fmt_pairs(d['placees_en_debut'], 6)}",
          f"- Placé en fin d'exercice : {fmt_pairs(d['placees_en_fin'], 6)}"]

    L += ["", "## 6. Facteurs latents (SVD sur ~90 variables)", ""]
    for f in r["facteurs_latents"][:6]:
        L.append(f"- F{f['facteur']} ({f['variance']}) : + {', '.join(f['pole_positif'][:4])}  /  − {', '.join(f['pole_negatif'][:4])}")
    L += ["", "## 7. Règles d'association (lift)", ""]
    L += [f"- {x} ⇒ {y} : lift {l}, P(B|A)={pba}" for x, y, _, l, pba, _ in r["regles_association"]["regles"][:15]]

    t = r["tendances"]
    L += ["", "## 8. Tendances et prévision", "",
          f"- En hausse : {fmt_pairs(t['en_hausse'], 6)}",
          f"- En baisse : {fmt_pairs(t['en_baisse'], 6)}",
          f"- Probabilité attendue par exercice (pondérée par récence) : {fmt_pairs(t['probabilite_attendue_par_exercice'], 12)}"]
    cv = r["cours_vs_epreuves"]
    L += [f"- Enseigné mais peu évalué : {fmt_pairs(cv['sous_evaluees_par_rapport_au_cours'], 8)}",
          f"- Très évalué par rapport au cours : {fmt_pairs(cv['sur_evaluees_par_rapport_au_cours'], 6)}"]

    g2 = r["regimes"]
    L += ["", "## 9. Changement de format 2022 → 2023", "",
          f"- χ² = {g2['chi2']} (p = {g2['p_value']:.1e}), Jensen-Shannon = {g2['jensen_shannon']}"]
    for k, v in g2["comparaison"].items():
        L.append(f"- {k} : {v}")

    L += ["", "## 10. Scénarios d'exercices (NMF)", ""]
    L += [f"- {', '.join(x['mots'][:6])} → {', '.join(n for n, _ in x['notions_associees'])}" for x in r["scenarios"]]
    p = r["epreuve_pratique"]
    L += ["", f"## 11. Épreuve pratique ({p['exercices_uniques']} exercices uniques)", ""]
    L += [f"- {x['effectif']} ex. : {', '.join(x['mots'][:5])} (ex1/ex2 : {x['exercice_1_ou_2']})" for x in p["typologie"]]
    cl = r["classifieur_notions"]
    L += ["", "## 12. Classifieur texte → notions (validateur)", "",
          f"- Top-3 correct en validation croisée : {cl['top3_hit_rate_cv']} ; micro-F1 : {cl['micro_f1_cv']}"]
    L += ["", "## 13. Questions atypiques (Isolation Forest)", ""]
    L += [f"- {q['annee']} {q['centre']} [{q['tache']}] {q['texte'][:150]}" for q in r["questions_atypiques"][:8]]
    (OUT / "rapport_analyse.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"[ok] {OUT / 'rapport_analyse.md'}")


if __name__ == "__main__":
    run()
