# Plan I-graphe (inedit)

Notion : graphe (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Graphes > 1.2 Vocabulaire]
> En général, un graphe est un ensemble d'objets, appelés *sommets* ou parfois *nœuds* (*vertex* or *nodes* en anglais) reliés par des *arêtes* ou *arcs* ((*edges* en anglais)).
> Ce graphe peut être **non-orienté** ou **orienté** .
> 
> #### 1.2.1 Graphe non-orienté
>  
> 
> Dans un graphe **non-orienté**, les *arêtes* peuvent être empruntées dans les deux sens, et une *chaîne* est une suite de sommets reliés par des arêtes, comme C - B - A - E par exemple. La *longueur* de cette chaîne est alors 3, soit le nombre d'arêtes.
> 
> Les sommets B et E sont *adjacents* au sommet A, ce sont les *voisins* de A.
> 
> **Exemple de graphe non-orienté** : le graphe des relations d'un individu sur Facebook est non-orienté, car si on est «ami» avec quelqu'un la réciproque est vraie.
> 
> #### 1.2.2 Graphe orienté
> 
>  
> 
> Dans un graphe **orienté**, les *arcs* ne peuvent être empruntés que dans le sens de la flèche, et un *chemin
> [Algorithmique > Algo parcours graphes > Algo parcours graphes]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 21 - Parcours de graphes
> Objectifs :
> ▷ Implémenter en Python des algorithmes de parcours de graphes et de recherche de chemins dans un graphe.
> ▷ Utiliser ces fonctions Python pour résoudre un problème utilisant des graphes (navigation GPS, laby-
> rinthes, mots voisins, ...,etc.)
> 1 Introduction
> Un des premiers algorithmes que l'on doit savoir utiliser sur un graphe est celui de son parcours.
> Parcourir un graphe , c'est visiter ses différents sommets, afin de pouvoir opérer une action tour à tour sur
> eux. Tous comme pour les arbres, il est possible de réaliser deux types de parcours d'un arbre :
> — le parcours en largeur : Breadth First Search
> — le parcours en profondeur : Depth-First Search
> Cependant, contrairement aux arbres :
> — il n'y a pas de racine, donc on doit choisir à partir de quel noeud on part : lenoeud source.
> — il peut y avoir u

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C0 : Écrire une méthode ou requête ciblée — L'élève produit une méthode de classe, une instruction ou une requête SQL qui réalise une opération précisément décrite ; on évalue la traduction exacte d'un besoin en code (conditions, attributs, tables).
    gabarit : Écrire la [méthode/requête/fonction] [nom] permettant de [effet attendu sur les données].
    exemple réel (autre notion) : « 7. Expliquer comment procéder pour déchiffrer un message lorsqu'on connaît la clé. On souhaite maintenant écrire, en Python, une fonction dechiffrement qui permet de déchiffrer un message chiffré par la méthode du masque jetable. »
    exemple réel (autre notion) : « 3. Écrire la fonction est_nombre_positif en utilisant est_chiffre. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 4. Dans cette partie, les requêtes utilisent des jointures entre tables. On supposera donc les numéros id_membre et id_objet non connus. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C6 : Établir ou lire une table de routage — Majoritairement réseau : dresser, compléter ou exploiter une table de routage selon un protocole (RIP/OSPF), ou identifier un chemin ; on évalue l'application d'un protocole à une topologie.
    gabarit : Donner la [table/chemin] [de l'élément] selon [protocole/règle], après [événement].
    exemple réel (autre notion) : « 2. Par lecture et analyse des relations de la base de donnée. »
    exemple réel (autre notion) : « 7. Donner la liste renvoyée par l'instruction sorted(etoiles). »
    support S7 : Consigne brève sans support — Question courte et autonome, sans matériau joint notable ; l'élève répond à partir de ses connaissances ou du contexte de l'exercice.
    exemple de support (autre notion) : « 2. Donner les quatre attributs formant la clé primaire pour la relation Mesure. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « b. Expliquer pourquoi on ne peut pas être certain que les données envoyées par une page web, depuis le navigateur d'un client, via plusieurs requêtes formulées en javascript, arrivent au serveur dans l'ordre dans lequel elles ont été émises »
    exemple réel (autre notion) : « b. La fonction choice([True, False]) peut renvoyer False un très grand nombre de fois consécutives. Expliquer pourquoi ce cas de figure amènerait à une erreur d'exécution. »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 1. Donner les affichages obtenus après l'exécution du code Python suivant. notes = [8, 7, 18, 14, 12, 9, 17, 3] notes[3] = 16 print(len(notes)) print(notes) »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C6 : Établir ou lire une table de routage — Majoritairement réseau : dresser, compléter ou exploiter une table de routage selon un protocole (RIP/OSPF), ou identifier un chemin ; on évalue l'application d'un protocole à une topologie.
    gabarit : Donner la [table/chemin] [de l'élément] selon [protocole/règle], après [événement].
    exemple réel (autre notion) : « 2. Donner les adresses IP des serveurs de la DMZ en respectant les consignes suivantes. • Serveur_web : première adresse IP du réseau • Serveur_BDD : deuxième adresse IP du réseau La configuration du poste PC_A1 est la suivante : • Adresse  »
    détail du cours à évaluer (Algo parcours graphes) : « Cette fonction renverra la liste des sommets parcourus en partant du sommetdepart. »

Le champ id vaut « I-graphe ».