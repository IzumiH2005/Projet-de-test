# Plan I-fonctions (inedit)

Notion : fonctions (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Dictionnaires > Exercices sur les dictionnaires]
> On considère la liste suivante :
> 
>     ```lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']``` 
> 
>     Quel est le **chiffre** qui revient le plus fréquemment dans cette liste ?
> 
>      
>     {{
>     correction(True,
>     """
> \"Correction\" 
>         ```python linenums='1'
>         lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053',
> [Programmation > Recursivite > Introduction]
> #Exercices
> 
>     Écrire une fonction récursive ```puissance``` qui prend en paramètres deux nombres ```x``` et ```n``` qui renvoie le nombre $x^n$.
> 
>     On rappelle que le PGCD (plus grand diviseur commun de deux nombres) vérifie la propriété suivante : si la division euclidienne de $a$ par $b$ s'écrit $a = b \times q + r$, alors $pgcd(a,b)=pgcd(b,r)$. 
> 
>     Cette propriété est à la base de l'algorithme d'Euclide
> 
>     Exemple : $pgcd(24,18)=pgcd(18,6)=pgcd(6,0)$, donc $pgcd(24,18)=6$
> 
>     Écrire une fonction récursive ```pgcd``` qui prend en paramètres deux nombres ```a``` et ```b``` et qui renvoie leur PGCD.
> 
>     La conjecture de Syracuse  (ou de Collatz) postule ceci :  
> 
>     *Prenons un nombre $n$ : si $n$ est pair, on le divise par 2, sinon on le multiplie par 3 puis on ajoute 1. On recommence cette opération tant que possible. Au bout d'un certain temps, on finira toujours par tomber

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : milieu d'exercice
    manière de demander C8 : Manipuler une base de données — Requêtes et modélisation sur une base relationnelle (supprimer, ajouter, interroger, proposer un schéma) ; on évalue la correspondance entre un besoin métier et les opérations SQL ou la structure de tables.
    gabarit : Donner la (les) requête(s) SQL permettant de [opération] dans la base de données [nom], [contrainte].
    exemple réel (autre notion) : « 9. Écrire, dans le bon ordre, les requêtes SQL qui permettent de mettre à jour la base de données en conséquence. On suppose que l'identifiant client 107 et que le code de commande 42366 n'ont pas encore été attribués dans la base de donnée »
    exemple réel (autre notion) : « 5. Le kimono numéro 25 a été déchiré lors d'un combat. Écrire les requêtes SQL permettant de le supprimer de la base de données. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 2.a) On considère la file V définie dans le code ci-dessous. Quel sera le contenu de V, F et de la variable val à la suite de ces instructions Python?  1 V = creer_file_vide()  2 val = defiler(F) 3 while not est_vide (F) and val != ‘Prioritaire'  4 enfiler (V, »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « 15. Expliquer ce qui se serait passé si on avait initialisé la variable memo avec uniquement des valeurs égales à -1. On rappelle que, pour gérer son stock, la scierie utilise un dictionnaire effectif qui associe à chaque longueur de planch »
    exemple réel (autre notion) : « 8. Expliquer, sans écrire de code mais en décrivant votre solution, comment modifier la fonction explore afin qu'elle renvoie la liste de tous les chemins solutions. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 10. Écrire la méthode itere_rip qui prend en paramètre le routeur self et met à jour sa table de routage lorsqu'il reçoit la table de routage de chacun des routeurs présents dans la liste de ses voisins. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 13. Écrire une fonction valeurs_chemin qui prend en paramètre chemin une liste de sommets et renvoie la liste de leurs valeurs. »
    exemple réel (autre notion) : « 11. Écrire une fonction somme qui prend comme paramètres une liste de 5 entiers et un masque (une liste de taille 5 de 0 et de 1) et qui renvoie la somme des chiffres du tableau correspondant au masque. Par exemple, somme([1, 5, 3, 4, 8], [ »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 3. Écrire une suite d'instructions permettant de créer une instance, nommée M, de la classe Maya qui modélise le nombre entier 3435. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C20 : Énoncés de mise en situation — Mélange d'énoncés introductifs et de questions descriptives (arbres, parité, interfaces) ; groupe défini par des tournures génériques plutôt que par un geste.
    gabarit : On considère [situation]. Indiquer [éléments] qui [propriété].
    exemple réel (autre notion) : « 3. Cette question porte sur la notion de clés étrangères. »
    détail du cours à évaluer (Arbres) : « Cette fonction renvoie True si element est dans l’arbre et False sinon. »

Le champ id vaut « I-fonctions ».