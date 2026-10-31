# Consignes pour l'agent rédacteur (droit, STMG)

Tu écris comme le professeur qui a conçu les anciens sujets. Ce qu'un modèle scikit-learn a appris
de lui est dans `output/droit/brief.txt` : lis-le d'abord. Ensuite, pour chaque plan de ton lot
(`output/droit/plans/lot_XX.json`), écris un fichier `output/droit/generated/<id>.json`.

## Penser comme le professeur
- Étudie `anciens_sujets_proches` : comment il pose une situation (une entreprise ou des personnes
  nommées, un litige concret, des dates, des montants), comment il annonce les annexes, comment
  il tourne chaque question, ce que son corrigé attend et avec quel niveau de détail.
- Pour chaque `questions[slot]`, reprends la **manière de demander** de la facette indiquée : imite
  la tournure de ses `exemples_reels` (même verbe de consigne, même construction), sans les copier.
- Le contenu vient de `cours` (et de `cours_partenaire` pour un cas qui mêle deux sections) : la
  question doit faire travailler les notions et les articles de la section visée. Si `inedit` est
  vrai, la section n'est jamais ou presque tombée : invente la question qu'il pourrait poser sur
  ce thème, avec sa façon de faire.
- Situation et noms nouveaux : ne recopie jamais une situation ancienne.

## Annexes (respect des supports)
- Nombre d'annexes : `nb_annexes` pour un cas ou un sujet blanc ; 0 ou 1 pour les exercices.
- Articles de code, extraits de loi, décisions de justice (arrêts) : **recopie mot pour mot** un
  texte fourni dans `cours.articles`, `cours_partenaire.articles` ou `documents_reels` (tu peux
  couper avec « […] »). N'invente jamais un article ni un arrêt, ni sa date, ni sa référence.
- Documents propres au cas (extrait de contrat, règlement intérieur, courriel, statuts…) : tu
  peux les inventer, cohérents avec la situation, comme le fait le professeur.
- Indique pour chaque annexe `"source"` : `"cours"`, `"documents_reels"` ou `"invente"`.

## Réponses attendues (corrigé)
- Écris le corrigé comme ses corrigés : en l'espèce, fondement, principe, qualification, arguments.
- Longueur visée : `longueur_cible_car` caractères (dans l'intervalle `longueur_reponse_car`).
- `articles_cites` : seulement des articles présents dans les textes fournis (numéros seuls,
  ex. `"1240"`, `"L1121-1"`).

## Format JSON (un fichier par plan, UTF-8, JSON valide)
```json
{
  "id": "<id du plan>",
  "type": "<type du plan>",
  "titre": "titre court du cas",
  "situation": "texte de la situation (cas et sujet blanc)",
  "annexes": [{"titre": "Annexe 1 – …", "texte": "…", "source": "cours|documents_reels|invente"}],
  "questions": [
    {"slot": 1, "situation": "(exercices seulement : mini-cas de 3 à 6 lignes)",
     "enonce": "…", "points": 2, "reponse_attendue": "…", "articles_cites": ["1240"]}
  ]
}
```
Pour le type `exercices`, chaque question a sa propre courte `situation` et `annexes` peut être
vide. Garde exactement les `slot` et `points` du plan.

Vérifie à la fin que chaque fichier se lit avec `python -c "import json,sys; json.load(open(sys.argv[1]))" <fichier>`.
