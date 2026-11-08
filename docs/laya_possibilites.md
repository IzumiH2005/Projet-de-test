# Laya : les possibilités théoriques de ses trois modes de réponse

Les trois modes de réponse de Laya sont les briques de base de tout programme. La différence : ils travaillent sur du langage, des images ou du son au lieu de nombres.

| Mode | Équivalent en programmation | Rôle |
|---|---|---|
| **noul** | `if` | une condition |
| **choice** | `switch` | un aiguillage |
| **score** | `<` / `>` | une mesure, une comparaison |

Tout système qui contient des conditions, des branches ou des classements peut donc avoir des briques « floues » décidées par Laya. Comme ses probabilités sont calibrées, on peut faire des calculs avec, pas seulement les lire.

## noul : la condition

- **Garde-fou** : un `if` sur du sens (« ce texte contient-il une menace ? ») au lieu d'un mot-clé.
- **Filtre** : garder ou rejeter des éléments dans un flux.
- **Vérification** : contrôler la sortie d'un autre modèle ou programme (« la réponse respecte-t-elle la consigne ? »).
- **Condition d'arrêt** : dans une boucle ou un agent, « l'objectif est-il atteint ? ».
- **Logique combinée** : on peut assembler des probabilités avec ET, OU et NON, donc construire des règles complexes à partir de questions simples.
- **Transformer n'importe quoi en données** : 30 questions oui/non donnent un vecteur de 30 nombres, que du ML classique (LightGBM, régression) peut exploiter. Les questions deviennent des caractéristiques.

## choice : l'aiguillage

- **Routage** : envoyer une entrée vers le bon module, outil ou humain.
- **Machine à états** : décider de la transition suivante (agent, dialogue, workflow).
- **Politique d'action** : choisir quoi faire parmi les actions possibles, ce qui en fait le cerveau rapide d'un agent.
- **Comparateur** : avec deux options (« lequel est le meilleur ? »), on obtient un tri, un tournoi ou un classement par paires.
- **Extraction** : choisir parmi des candidats (« quelle date est la date d'échéance ? »).
- **Distribution complète** : on peut aussi tirer au hasard selon ses probabilités, ou mesurer son hésitation (entropie).

## score : la mesure

- **Priorisation** : ordonner une file (urgence, risque, valeur).
- **Seuils** : déclencher une action à partir d'un niveau donné.
- **Reranking** : reclasser les résultats d'une recherche par pertinence.
- **Fonction de valeur** : dans une recherche (arbre de coups, planification), noter une position, comme le « value network » d'AlphaZero.
- **Juge ou récompense** : noter des sorties pour évaluer, ou pour entraîner un autre modèle par renforcement.

## Ce que la calibration ajoute partout

Ces propriétés sont transversales : elles valent pour les trois modes.

- **Décision par le coût** : avec une vraie probabilité, on décide selon le coût d'une erreur (agir seulement si p × gain > (1 − p) × perte).
- **Cascade** : Laya tranche les cas sûrs ; les incertains montent vers un modèle plus gros ou un humain. Coût minimal, qualité maximale.
- **Abstention et hors-distribution** : le système sait quand il ne sait pas, et peut aussi détecter qu'il voit quelque chose de nouveau (dérive des données).
- **Apprentissage actif** : on ne fait étiqueter que les cas où il hésite, donc moins d'annotation pour plus de progrès.
- **Questions adaptatives** : on choisit la question suivante selon ce qui réduit le plus l'incertitude, façon « jeu des 20 questions ».
- **Propagation d'incertitude** : on peut enchaîner plusieurs décisions dans un réseau probabiliste (bayésien) dont les nœuds sont des questions en langage naturel.

## En une phrase

Laya permet d'écrire des **programmes dont les conditions, les branches et les comparaisons sont exprimées en langage naturel** et portent sur du texte, des images ou du son. Chaque décision a un prix quasi nul et une confiance fiable, et le système peut dire « je passe la main ».
