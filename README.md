# examgen — générateur de questions NSI appris sur les annales

Le programme lit les anciens sujets du bac NSI (Terminale) et le cours. Il en apprend la façon dont les épreuves sont construites, puis fabrique des plans de questions. Un agent Opus 5.5 (effort *low*) rédige ces plans. Les modèles appris sur les annales contrôlent ensuite chaque question.

```
annales PDF + cours ──► ingest ──► features (~90 variables/question) ──► analysis (14 modèles)
                                                                              │
             questions.md ◄── validate ◄── agent Opus 5.5 low ◄── plans ◄── blueprint
```

## Corpus

Sources publiques hébergées sur GitHub, récupérées par `scripts/fetch_sources.sh` :

| Source | Contenu |
|---|---|
| [glassus/terminale_nsi](https://github.com/glassus/terminale_nsi) | cours (Markdown), annales écrites, sujets d'épreuve pratique |
| [trahobisoa/Terminale_NSI](https://github.com/trahobisoa/Terminale_NSI) | cours (PDF), annales écrites 2021–2026 |
| [Nota-yob/ECE-NSI-2024](https://github.com/Nota-yob/ECE-NSI-2024) | sujets d'épreuve pratique 2024 |

Après dédoublonnage, le corpus compte :
- 83 sujets écrits uniques (2 668 questions) ;
- 362 exercices pratiques ;
- 281 sections de cours (≈ 790 000 caractères).

## Ce que l'analyse extrait (`examgen/analysis.py`)

1. **Espace sémantique**. Questions et cours sont projetés dans un même espace TF-IDF, réduit par LSA (150 dimensions).
2. **Rattachement au cours**. Chaque notion du programme est reliée à ses sections de cours. Le modèle mesure aussi la part de chaque notion dans le cours et dans les épreuves.
3. **Archétypes de questions**. Un KMeans regroupe les questions selon leur forme et le début de leur consigne. Le nombre de groupes est choisi par silhouette.
4. **Affinité notion × archétype**. Elle indique quelles formes de question vont avec quelle notion. Les notions rares empruntent le profil de leur domaine (lissage bayésien hiérarchique).
5. **Chaîne de Markov**. Elle apprend l'enchaînement des archétypes et des niveaux de Bloom dans un exercice (ouvertures, transitions, fermetures).
6. **Graphe des notions**. Il repose sur la PMI des cooccurrences. On en tire les notions pivots (PageRank), les notions ponts (betweenness) et des blocs thématiques cachés (communautés).
7. **Modèle de difficulté**. Un Gradient Boosting prédit la position d'une question dans l'exercice. L'importance par permutation montre ce qui rend une question « de fin d'exercice ».
8. **Facteurs latents**. Une SVD sur les ~90 variables fait ressortir des facteurs latents.
9. **Règles d'association** (lift), par exemple « lire du SQL ⇒ écrire du SQL ».
10. **Tendances**. Fréquences pondérées par récence, pentes, prévision, et notions enseignées mais peu évaluées.
11. **Changement de format 2022 → 2023**. Comparaison par χ² et divergence de Jensen-Shannon.
12. **Logique d'un sujet**. Comment les domaines se répartissent entre exercices, et comment le Bloom, le code et les dépendances évoluent au fil d'un exercice.
13. **Scénarios d'exercices**. Un NMF dégage les contextes récurrents ; un Isolation Forest repère les questions atypiques.
14. **Classifieur texte → notions**. Une régression logistique *one-vs-rest* sert de validateur. Le Top-3 est correct dans 89 % des cas en validation croisée.

On y ajoute une typologie des exercices pratiques. Le rapport complet se trouve dans `output/rapport_analyse.md`.

## Génération

- `blueprint.py` tire chaque plan dans les lois apprises.
  - **Mode sujet** : 3 exercices de 6, 6 et 8 points. Les notions sont choisies par PMI, avec une pénalité si un domaine revient. Les questions suivent la chaîne de Markov combinée à l'affinité notion × archétype. Le plan fixe aussi la courbe de difficulté, les dépendances et le barème.
  - **Mode banque** : quelques questions par notion pour couvrir tout le programme, avec des archétypes variés.
- `llm.py` transforme chaque plan en consigne (`output/prompts/<id>.md`). Chaque consigne contient des extraits du cours, des exemples réels de style et une sortie JSON imposée (`_schema.json`).
- La rédaction se fait de deux façons :
  - `--backend agents` : des agents Claude Code Opus 5.5 en effort *low* rédigent `output/generated/<id>.json`. C'est le mode utilisé ici.
  - `--backend api` : appel direct à `claude-opus-5-5` avec `effort: low` et une sortie JSON structurée. Il faut définir `ANTHROPIC_API_KEY`.

## Validation (`validate.py`)

Chaque question générée repasse par la même chaîne que les vraies questions. On vérifie :
- la notion (classifieur, top-3) ;
- l'archétype et le type de tâche ;
- le niveau de Bloom ;
- la nouveauté (similarité maximale avec les 2 668 vraies questions ; au-delà de 0,92, c'est une quasi-copie) ;
- l'ancrage dans le cours ;
- le code Python du corrigé (il doit compiler) et la forme du SQL ;
- la courbe de difficulté (corrélation de Spearman).

## Utilisation

```bash
pip install -r requirements.txt
bash scripts/fetch_sources.sh
python -m examgen.cli all --sujets 2 --par-notion 4   # ingest + analyse + rapport + plans + consignes
python -m examgen.cli write --backend api             # ou faire rédiger par des agents
python -m examgen.cli validate                        # -> output/validation.json + output/questions.md
```

## Résultats de la première génération (205 questions, 2 sujets complets + banque)

| Contrôle | Score |
|---|---|
| Code Python des corrigés qui compile | 100 % |
| SQL bien formé | 100 % |
| Notion reconnue par le lexique du programme | 94 % |
| Notion dans le top-3 du classifieur | 75 % |
| Niveau de Bloom respecté (±1) | 75 % |
| Type de tâche respecté | 68 % |
| Quasi-copies d'annales | 1,5 % (3 questions) |
| Courbe de difficulté (Spearman moyen) | +0,34 |

Le classifieur reconnaît mal les notions rares dans les annales (sgbd, prog_dynamique, algo_simples, web_http). Il en a vu trop peu d'exemples pour bien les apprendre ; ce n'est pas un défaut des questions.
