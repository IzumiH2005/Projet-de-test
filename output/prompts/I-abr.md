# Plan I-abr (inedit)

Notion : abr (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Arbres > 5.3  Coût de la recherche dans un ABR équilibré]
> Imaginons un arbre équilibré de taille $n$. Combien d'étapes faudra-t-il, dans le pire des cas, pour trouver (ou pas) une clé particulière dans cet arbre ?
> 
> Après chaque nœud, le nombre de nœuds restant à explorer est divisé par 2. On retrouve là le principe de recherche dichotomique, vu en classe de Première (voir ici).
> 
> S'il faut parcourir tous les étages de l'arbre avant de trouver (ou pas) la clé recherchée, le nombre de nœuds parcourus est donc égal à la hauteur $h$ de l'arbre.
> 
> Pour un arbre complet, cette hauteur vérifie la relation $2^h -1= n$. et donc $2^h = n+1$.
> 
> $h$ est donc le «nombre de puissance de 2» que l'on peut mettre dans $n+1$. Cette notion s'appelle le logarithme de base 2 et se note $\log_2$.
> 
> Par exemple, $\log_2(64)=6$ car $2^6=64$.
> 
> Le nombre maximal de nœuds à parcourir pour rechercher une clé dans un ABR équilibré de taille $n$ est donc de l'ordre de $\log_2(n
> [Structures de données > ABR > ABR]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 13 - Les arbres binaires de recherche
> Objectifs :
> ▷ Connaître le principe d'un arbre binaire de recherche
> ▷ Rechercher une clé dans un arbre de recherche, insérer une clé.
> 1 Introduction
> Les arbres binaires de recherche(notés souventABR) sont des structures de données fondamentales en
> informatique et en algorithmique. Ils sont largement utilisés dans de nombreuses applications informatiques
> pour leur efficacité dans la recherche, l'insertion et la suppression de données.
> On les utilise par exemple pour :
> ▷ l'implémentation des bases de données indexées
> ▷ les systèmes de gestion de fichiers
> ▷ les algorithmes de recherche et de tri
> ▷ les structures de recherche dans les compilateurs et analyseurs syntaxiques
> 2 Principe de l'ABR
> Un arbre binaire de recherche (ABR)est une structure de donnée composée de noeuds (on parlera aussi
> de clés).
> A re

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 11. Coder la chaîne de caractères txt à l'aide du code de Huffman et de l'arbre construit à la question 6. »
    exemple réel (autre notion) : « 7. Écrire une fonction tri_sommets qui prend en paramètre un graphe graphe et qui ne renvoie que la liste des sommets du graphe graphe triés par degré décroissant. On pourra utiliser les fonctions définies dans les questions précédentes.  E »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 9. Dans la méthode defiler expliquer la ligne de code suivante :  assert not self.est_vide() »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : milieu d'exercice
    manière de demander C17 : Question directe « quelle est » — L'élève indique une valeur, une propriété ou un élément d'une structure. Réponse courte ; le groupe reste un peu hétérogène.
    gabarit : Quelle est la [valeur|propriété] de [objet] ?
    exemple réel (autre notion) : « 14. À partir de l'exemple précédent, déterminer la valeur de graphe['Paris']['Nantes'][1]. EN_OOTgzNT7QzNjAc0ND4UzMsTYxMj8A2NTAAwMDbAxNEjkx La fonction ratio_duree_distance ci-dessous prend en paramètre le dictionnaire graphe. Elle permet d »
    exemple réel (autre notion) : « a. Quelle est la taille minimale, notée ݐ_݊݅݉d'un arbre binaire de recherche " bien construit " de hauteur ℎ ? »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 7. Déterminer le nombre de comparaisons effectuées si on applique l'algorithme précédent à la chaine de caractères 'tab[2*(i + 4)] - tab[3]'. En déduire le nombre maximum de comparaisons effectuées si on applique l'algorithme précédent à une chaine de caractèr »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C18 : Tracer une boucle Python donnée — L'élève suit l'exécution d'un code avec boucles for/range pour en déduire une valeur ou un affichage. On évalue la trace d'exécution.
    gabarit : Déterminer la valeur de [variable] à l'issue des instructions suivantes : [code].
    exemple réel (autre notion) : « d. Représenter la pile p et la file f après l'exécution du code suivant. for i in range(2):  empiler(p, defiler(f)) »
    exemple réel (autre notion) : « 1. Expliquer ce que fait la fonction ci-dessous. def distance(IdCpt1, IdCpt2, listeFilms):  assert (type(listeFilms) is list) and (len(listeFilms) != 0)  somme_ecarts = 0  for film in listeFilms:  somme_ecarts += abs(nbEtoiles(film, IdCpt1) »
    support S14 : Prose avec parenthèses — Phrases contenant des parenthèses (couples, types, précisions). Artefact de ponctuation sans matériau commun.
    exemple de support (autre notion) : « 1. Expliquer le résultat obtenu lors de l'utilisation de la commande ping (on part du principe que la connexion physique entre les machines est fonctionnelle). »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 8. Calculer le coût de chacune de ces liaisons de communication. »
    détail du cours à évaluer (Arbres) : « Remarque : on pourrait aussi définir un ABR comme un arbre dont le parcours infixe est une suite croissante. »

Le champ id vaut « I-abr ».