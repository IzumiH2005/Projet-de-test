# Plan I-matrice (inedit)

Notion : matrice (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Les graphes > Les graphes]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 20 - Les graphes
> Objectifs :
> ▷ Modéliser des situations sous forme de graphes.
> ▷ Écrire les implémentations d'un graphe : matrice d'adjacence, liste de successeurs/prédécesseurs.
> ▷ Passer d'une représentation à une autre.
> 1 Introduction
> Le concept de graphe permet de résoudre de nombreux problèmes en mathématiques comme en informatique.
> C'est un outil de représentation très courant, et nous l'avons déjà rencontré à plusieurs reprises, en particulier
> lors de l'étude de réseaux tels que :
> — les réseaux informatiques,
> — les réseaux sociaux,
> — les réseaux de transport
> Une multitude de problèmes concrets d'origines très diverses peuvent donner lieu à des modélisations par des
> graphes : c'est donc une structure essentielle en sciences, qui requiert un formalisme mathématique particulier
> que nous allons découvrir.
> T. Rahobisoa 1/11 SD08 - Les gr
> [Structures de données > Graphes > 2.1 Représentation par matrice d'adjacence]
> - On classe les sommets (en les numérotant, ou par ordre alphabétique).
>     - on représente les arêtes (ou les arcs) dans une matrice, c'est-à-dire un tableau à deux dimensions où on inscrit un 1 en ligne `i` et colonne `j` si les sommets de rang `i` et de rang `j` sont **voisins** (dits aussi *adjacents*).
> 
>     Ce tableau s'appelle une **matrice d'adjacence** (on aurait très bien pu l'appeler aussi *matrice de voisinage*).
> 
> #### 2.1.1 Graphe non orienté
> 
> Dans ce graphe non orienté, comme B est voisin de C, C est aussi voisin de B, ce qui signifie que l'arête qui relie B et C va donner lieu à deux "1" dans la matrice, situé de part et d'autre de la diagonale descendante (un mathématicien parlera de matrice *symétrique*).
> 
> #### 2.1.2 Graphe orienté
> 
> Comme le graphe est orienté, la matrice n'est pas forcément symétrique (il faudrait que tous les liens soient réciproques pour qu'elle le soi

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C10 : Écrire ou corriger le code — L'élève écrit, recopie ou modifie le code d'une méthode ou fonction nommée, parfois pour corriger un comportement fautif ; on évalue l'implémentation et la gestion d'un cas d'erreur.
    gabarit : Écrire le code de la [méthode/fonction] [nom] qui [comportement]. / Modifier le code de [nom] pour que [comportement corrigé].
    exemple réel (autre notion) : « 10. Écrire le code de la méthode ajouter_voisin. »
    exemple réel (autre notion) : « 5. Écrire le code de la méthode est_resultat pour la classe Feuille_resultat. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 3. Écrire une requête SQL permett ant de récupérer le libellé de s articles de la 2 1 - N S I J 2 P O 1 7 / 1 5 commande 1345. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Analyser un code fourni — Un extrait de code (def numéroté) est donné, à compléter ou à exécuter mentalement ; on évalue la lecture de code et la compréhension de ce qu'il fait.
    gabarit : On considère le code suivant : [code]. [Compléter la ligne n / Donner ce qu'affiche l'appel [appel]].
    exemple réel (autre notion) : « 7. Recopier et compléter le code de la fonction ajouter_file_prio.  1 def ajouter_file_prio(f, t, p):  2 f_aux = File()  3 while ...:  4 ...  5 ...enfiler(...)  6 while not ...:  7 ...  8 while not ...:  9 ... »
    exemple réel (autre notion) : « 14. Recopier et compléter sur votre copie le code python de la méthode minage_bloc. 1 def minage_bloc(self): 2 """modifie le nonce d'un bloc pour que son hash commence par '00' en énumérant tous les entiers naturels en partant de 0.""" 3 se »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 6. Recopier et compléter la fonction semi_marathon. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C24 : Compléter une fonction à trous — L'élève recopie et complète une fonction ou une table entière (parfois à partir d'une ligne donnée) ; on évalue l'achèvement d'un code partiellement fourni.
    gabarit : Recopier et compléter la fonction [nom] (à partir de la ligne [n]) qui [comportement].
    exemple réel (autre notion) : « 3. La variable jeu_caracteres de la fonction gen_mdp est une liste contenant tous les caractères autorisés pour fabriquer un nouveau mot de passe. Recopier et compléter la ligne 13 du code de la fonction gen_mdp, puis écrire les autres lign »
    exemple réel (autre notion) : « b. Recopier et compléter la ligne 7 du code de la fonction ins ci-dessous qui prend en paramètres une valeur v et un arbre binaire de recherche abr et qui renvoie l'arbre obtenu suite à l'insertion de la valeur v dans l'arbre abr. Les ligne »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « a) Recopier et compléter l'instruction Python suivante permettant de créer la liste d'attente initiale des processus donnés dans le tableau précédent (le processus PID 11 est à l'indice 0 de la liste d'attente) : liste_attente = [Processus(...,...), .......... »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « b. Expliquer comment construire un arbre binaire de hauteur h quelconque ayant h+1 nœuds. »
    détail du cours à évaluer (Cryptographie) : « chiffrement par bloc de 128 bits, répartis dans une matrice de 16 octets (matrice carrée de taille 4). »

Le champ id vaut « I-matrice ».