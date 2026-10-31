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
> [Structures de données > Graphes > Introduction]
> Exercice 3 du sujet 0 version A - 2024
> 
>     
> 
>     
> 
>     {{
>     correction(True,
>     """
> \"Correction Q3.\" 
>         La matrice d'adjacence de G1 est :
>         $\\pmatrix{
>         0 & 4 & 0 & 0 & 4 & 0 & 0  \\\\
>         4 & 0 & 0 & 0 & 0 & 7 & 5  \\\\ 
>         0 & 0 & 0 & 4 & 8 & 0 & 0  \\\\
>         0 & 0 & 4 & 0 & 6 & 8 & 0  \\\\ 
>         4 & 0 & 8 & 6 & 0 & 0 & 0  \\\\
>         0 & 7 & 0 & 8 & 0 & 0 & 3  \\\\ 
>         0 & 5 & 0 & 0 & 0 & 3 & 0  \\\\
>         }$  
>     """
>     )
>     }}
> 
>     {{
>     correction(True,
>     """
> \"Correction Q4.\" 
>         ```python linenums='1'
>         G2 = {'A': ['B', 'C', 'H'],
>               'B': ['A', 'I'],
>               'C': ['A', 'D', 'E'],
>               'D': ['C', 'E'],
>               'E': ['C', 'D', 'G'],
>               'F': ['G', 'I'],
>               'G': ['E', 'F', 'H'],
>               'H': ['A', 'G', 'I'],
>               'I': ['B', 'F', 'H']
>              }
>  

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C6 : Exécuter mentalement une requête ou instruction suivante — L'élève lit une requête SQL ou une commande donnée et indique ce qu'elle renvoie. On évalue la capacité à simuler l'exécution.
    gabarit : Donner les valeurs renvoyées par la requête suivante : [requête].
    exemple réel (autre notion) : « b. Donner le résultat de la requête suivante :Code 1 SELECT nom, telephone FROM Equipe WHERE id_equipe = 5; »
    exemple réel (autre notion) : « 6. Expliquer par une phrase ce que renvoie la méthode mystere. »
    support S8 : Phrases courtes isolées — Fragments brefs d'une phrase (hypothèse de scénario, consigne courte). Aucun matériau fourni ; groupe défini par la brièveté.
    exemple de support (autre notion) : « 12. Expliquer comment les tables Centre et Personnel sont mises en relation. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C1 : Écrire la fonction ou commande nommée — L'élève produit un code précis (fonction, méthode, commande shell) dont le nom est imposé. On évalue la justesse et la syntaxe du code écrit.
    gabarit : Écrire la [fonction|méthode|commande] [nom] qui [comportement attendu].
    exemple réel (autre notion) : « 3. Donner en langage SQL la requête d'insertion qui permet d'inscrire, avec le numéro 13862, la patiente dénommée Ninette Bélanger résidant à La Rochelle. »
    exemple réel (autre notion) : « 9. À la date du 20 mars 2025, Alice a décidé de lister tous les mots de passe qui n'ont pas été renouvelés depuis plus d'un an. Écrire la requête SQL permettant de donner la liste des id_site concernés. »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 5. Écrire une méthode tracer_chemin de la classe Chemin qui affiche une représentation graphique d'un itinéraire. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C15 : Recopier et compléter un élément — L'élève recopie puis complète une fonction, un résultat ou une table partiellement donnés. On évalue la capacité à combler les trous correctement.
    gabarit : Recopier et compléter [la fonction|le tableau] [nom] [donné ci-dessous].
    exemple réel (autre notion) : « 4. Recopier et compléter le code de la méthode depiler précédente. Lorsque le tube est vide, la méthode depiler doit renvoyer -1. »
    exemple réel (autre notion) : « 6. Recopier et compléter la fonction semi_marathon. »
    support S5 : Besoin formulé pour requête SQL — Phrase décrivant en langage naturel l'information à extraire d'une base. L'élève la convertit en requête SQL.
    exemple de support (autre notion) : « 6. L'interblocage est la situation où plusieurs processus s ont bloqués car chacun attend qu'une ressource détenue par un autre se libère. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 9. Décrire les nouvelles modifications à apporter à la table de routage du robot 91.  EN_MOjgzNT7QzNjAc0ND7UzMsTYxMj4A2NTAAwMDjAxNBjIx »
    détail du cours à évaluer (Arbres) : « Si on adopte le vocabulaire des graphes, un arbre est un graphe non orienté, connexe, sans cycle, et dans lequel un nœud joue le rôle de racine. »

Le champ id vaut « I-graphe ».