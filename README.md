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

## Découverte non supervisée (`examgen/discovery.py`)

Ici, aucune liste de variables n'est écrite à la main. scikit-learn lit 3 102 questions : 2 668 d'écrit, 267 de pratique et 167 exercices du cours. Il en tire lui-même 95 variables, dont 80 sont stables d'un ré-échantillonnage à l'autre.

1. **Séparer la manière de demander du sujet**. Pour chaque mot, on mesure deux choses :
   - s'il est réparti sur tous les thèmes (entropie) ;
   - s'il revient en grappe dans un même exercice.

   Un mélange gaussien en 2D classe alors les mots en « mots de consigne » (967) ou « mots de contenu ». Aucun lexique n'est fourni au départ.
2. **Quatre vues apprises par NMF** :
   - le contenu ;
   - la consigne (le texte où les mots de contenu sont masqués) ;
   - la forme du support (code, nombres, listes, tableaux) ;
   - la mise en situation.

   Le nombre de variables de chaque vue est choisi par stabilité au bootstrap.
3. **Facettes**. Un KMeans, avec un nombre de groupes choisi par silhouette, dégage :
   - 25 manières de demander, par exemple « Prédire le résultat d'un appel », « Compléter des lignes numérotées », « Rôle d'une clé », « Interpréter le résultat d'une requête » ;
   - 8 types de support.

   Un agent Opus 5.5 low les a seulement nommées (`data/model/facet_names.json`).
4. **Grammaire des combinaisons**. Une régression logistique avec interactions apprend quelles combinaisons (notion × manière × support × position) existent vraiment. Elle les distingue de combinaisons corrompues, avec une AUC de 0,69 en validation croisée par sujet. Sur 8 400 combinaisons possibles, 1 313 ont déjà servi. **250 n'ont jamais été posées mais sont jugées aussi plausibles que de vraies questions.** Un filtrage collaboratif (PPMI + SVD) confirme ce transfert.
5. **Savoirs jamais évalués**. Le cours est découpé en 3 179 phrases, dont 477 déjà interrogées aux annales. Un apprentissage positif/non étiqueté (Elkan-Noto) estime quels détails sont évaluables et n'ont pourtant jamais été demandés.
6. **Dynamique des exercices** : 14 types de transition entre questions et 166 motifs de séquence plus fréquents que ne le prévoit Markov.
7. **Moteurs cachés**. Les variables découvertes améliorent la prédiction de la difficulté (R² 0,077 → 0,09 avec les variables manuelles). Elles reconnaissent aussi le format 2023 (AUC 0,77). Le modèle relève enfin les styles en hausse et en baisse, et les questions atypiques.

Résultats : `data/model/discovery.json` et `output/discovery/facettes.md`.

### Questions inédites (`examgen/inedit.py`)

Chaque plan inédit vise une notion et contient deux sortes de questions :
- **combinaison inédite** : une manière de demander ou un support jamais utilisés pour cette notion. Le style est montré par de vraies questions d'autres notions ; on imite la forme, pas le fond.
- **savoir jamais évalué** : un détail du cours que le modèle juge évaluable.

La validation remesure, sur le texte rédigé, la facette et le support (top-3), la plausibilité et la nouveauté de la combinaison.

```bash
python -m examgen.cli discover   # apprend les variables
python -m examgen.cli inedit     # 42 plans, 148 questions -> output/prompts/I-*.md
python -m examgen.cli validate
```

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

## Résultats des questions inédites (148 questions, 42 notions)

| Contrôle | Score |
|---|---|
| Manière de demander remesurée = celle du plan (top-3) | 71 % (exacte : 57 %) |
| Type de support remesuré = celui du plan (top-3) | 81 % |
| Combinaison (notion, manière, support) absente des annales écrites | 74 % |
| Notion reconnue (lexique / top-3 du classifieur) | 83 % / 62 % |
| Quasi-copies d'annales | 0 % |
| Python qui compile / SQL bien formé | 100 % / 100 % |
| Au-dessus de la plausibilité médiane des vraies questions | 31 % (référence : 50 %) |

Exemples :
- *recherche textuelle × « prédire le résultat d'un appel »* : « Donner la valeur renvoyée par cet appel. »
- *parcours d'arbre × « expliquer un fonctionnement »* : « Expliquer pourquoi le parcours infixe d'un ABR fournit ses valeurs dans l'ordre croissant. »
- *SoC, savoir jamais évalué* : « Quel élément d'un SoC permet à un smartphone de communiquer avec d'autres machines ? »

Limites :
- 9 des 25 manières de demander et 5 des 8 types de support sont jugés peu cohérents.
- La grammaire de plausibilité reste modeste (AUC 0,69).
- Une question inédite reste en moyenne un peu moins « typique » qu'une vraie question.

## Deuxième entraînement : plus de matière, auto-correction

Aucune variable n'a été ajoutée à la main. Le modèle a reçu plus de matière, et de nouveaux mécanismes lui permettent de se corriger seul.

**Nouvelle matière** (`scripts/fetch_sources.sh`, `examgen/ingest_extra.py`) :
- 96 sujets écrits officiels, dont ceux de [sujetdebac.fr](https://www.sujetdebac.fr) pour 2021–2026 ;
- [CodEx](https://codex.forge.apps.education.fr) : exercices avec étiquettes et difficulté ;
- une banque de QCM de Terminale ;
- 7 dépôts d'enseignants sur la Forge des communs numériques éducatifs.

Au total, environ 8 400 questions d'exposition.

**Mécanismes d'auto-correction** (`examgen/discovery.py`) :
- **Tri automatique.** Un classifieur sépare les vraies questions de la prose. Son seuil est choisi par F1 et il a écarté 1 303 unités.
- **Facettes stables.** Chaque groupe de k-means est rééchantillonné (Jaccard *clusterboot*). k est choisi par silhouette × stabilité, puis les groupes instables sont dissous en un seul tour. Les facettes sont apprises sur les sujets seulement, et les autres sources y sont projetées. Une première version avait fait s'effondrer les facettes (6 manières de demander) ; cette contrainte a corrigé le problème.
- **Réglages par validation croisée groupée.** La plausibilité et le classifieur de notions choisissent eux-mêmes leurs hyperparamètres.
- **Auto-apprentissage contrôlé.** Pseudo-étiquettes et auto-étiquetage du cours ne sont gardés que s'ils améliorent le score sur des sujets tenus à l'écart. Pour le cours, ce n'était pas le cas, et ils ont été refusés.
- **Validateur corrigé.** Il accepte les méthodes « à compléter » indentées et les lignes numérotées. Il ne vérifie plus le SQL cité dans une phrase.

| Mesure | Avant | Après |
|---|---|---|
| Sujets écrits / unités d'exposition | 83 / 3 102 | 96 / ≈ 8 400 |
| Manières de demander | 25 (silhouette 0,33) | 21 stables (0,37 ; stabilité 0,89) |
| Types de support | 8 | 16 stables (stabilité 0,89) |
| Notion top-3 (sujets tenus à l'écart) | 90,1 % | 95,6 % |
| Difficulté (R²) | 0,036 | 0,081 |
| Inédites : manière de demander respectée (top-3) | 71 % | 85 % |
| Inédites : notion reconnue (top-3) | 62 % | 74 % |
| Inédites : jugées plausibles | 31 % | 36 % |
| Inédites : combinaison jamais vue | 74 % | 77 % |
| Inédites : support respecté (top-3) | 81 % sur 8 types | 63 % sur 16 types |
| Python / SQL des corrigés | 100 % / 100 % | 98 % / 100 % |

La page `output/livrable.html` (construite par `python scripts/build_livrable.py`) regroupe les anciens sujets et les 368 questions générées, dont 163 inédites.

## Moteur générique : le « profil du professeur » (`examgen/prof`)

Il fonctionne pour n'importe quelle matière, à partir des anciens sujets (avec leurs corrigés si possible) et du cours. Rien n'est écrit à la main pour une matière donnée : le découpage repose uniquement sur la typographie (titres, numéros, « Annexe », barème). Tout le reste est appris :
- les parties pertinentes ;
- les manières de demander et leur ordre ;
- les formules rituelles ;
- les types d'annexes, recopiées ou inventées ;
- le niveau de détail par point ;
- les sections qui tombent ensemble ;
- la probabilité qu'une section tombe l'an prochain.

```
python -m examgen.prof profil --sujets DIR --cours DIR --out OUT   # profil appris
python -m examgen.prof plan   --sujets DIR --cours DIR --out OUT   # plans pour tout le cours
(agents rédacteurs : OUT/consignes_redacteur.md)
python -m examgen.prof check  --sujets DIR --cours DIR --out OUT   # validateur = récompense
python scripts/prof_revise.py prepare|keep_best|compare OUT        # boucle vérifier → réviser
```

**Pas besoin d'apprentissage par renforcement complet.** Le validateur appris joue le rôle de la récompense. Le rédacteur révise d'après ses retours, et une révision n'est gardée que si la note ne baisse pas (accepter/rejeter).

**Formules rituelles.** Le professeur repose les mêmes débuts de question d'un sujet à l'autre, comme « Développez l'argumentation juridique que… » (34 sujets). Ces tournures sont détectées automatiquement : un trigramme de début d'énoncé présent dans au moins 10 % des sujets. Les reprendre est admis. Recopier une ancienne situation, même avec d'autres noms, est refusé.

### Droit (bac STMG droit-économie)

Le corpus compte 38 sujets 2021–2026, 14 corrigés et le cours en 23 sections (programme Éduscol et articles des codes). Le moteur a gardé seul 43 parties juridiques et écarté 42 parties d'économie. Il a produit 49 documents (un cas et une série d'exercices par section, plus 3 sujets blancs), soit 196 questions et 124 annexes.

| Contrôle (196 questions) | 1re écriture | + formules rituelles | + révision |
|---|---|---|---|
| Manière de demander reconnue | 100 % | 100 % | 100 % |
| Section visée reconnue (top 3) | 87,8 % | 87,8 % | 93,4 % |
| Articles cités vérifiables | 100 % | 100 % | 100 % |
| Pas une copie | 77 % | 99,5 % | 100 % |
| Longueur du corrigé | 100 % | 100 % | 100 % |
| Annexes sources recopiées fidèlement | 100 % | 100 % | 100 % |
| Question qui passe tout | 69,4 % | 87,2 % | 93,4 % |

La colonne « 1re écriture » utilise l'ancien test de copie, qui confondait formules rituelles et copies ; la hausse de 77 % à 99,5 % vient de cette correction du contrôle, pas d'une réécriture. La révision a porté sur les 14 documents signalés : la section reconnue y passe de 57 % à 77 %, et les 14 révisions ont été gardées.

NSI : sur 45 questions révisées, 24 révisions ont été gardées et 21 rejetées. Le support reconnu sur l'ensemble des questions inédites passe de 63 % à 70 %.

Limites :
- la section n'est prédite qu'un peu mieux que par la popularité (AUC 0,635 contre 0,622) ;
- il n'y a que 14 corrigés ;
- les PDF scannés ne sont pas lus (pas d'OCR).

## Méta-apprentissage (`examgen/meta`)

`python -m examgen.meta.learn` → `output/meta/rapport.json` et `data/model/meta.json`.

- `align.py` : le moteur choisit seul sa façon de lire (règle apprise sur une matière, testée sur l'autre).
- `selftrain.py` : auto-entraînement par générations (v0 → v1 → …). Cohérence de partie, puis un élève entraîné sur le cours corrige son maître. Un garde-fou sans étiquette refuse les reculs. Droit 78 % → 87 %, NSI 77 % → 82 % (top 3, matière exclue). Appelé par `Teacher.align` quand les corrigés ne citent pas le cours.
- `intent.py` : environ 30 variables d'intention cours ↔ question, retenues par tâches auto-supervisées.
- `deep.py` : 312 variables générées, sélection par stabilité, transfert à froid entre matières.
