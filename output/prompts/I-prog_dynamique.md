# Plan I-prog_dynamique (inedit)

Notion : prog_dynamique (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Programmation dynamique > Introduction]
> Exercice 1 du sujet 0 - version B 2024
> 
>     
> 
>     
> 
>     
> 
>     {{
>     correction(False,
>     """
> \"Correction Q4.\" 
>         Pour une pyramide de $n$ niveaux, il va y avoir $n-1$ choix de direction (droite ou gauche). Cela revient donc à écrire un mot binaire composé de $n-1$ chiffres (0 ou 1).
> 
>         Or le nombre de mots binaires de longueur $n-1$ est égal à $2^{n-1}$ donc une pyramide de n niveaux comportera $2^{n-1}$ conduits.
>     """
>     )
>     }}
> 
>     
> 
>     
> 
>     
> 
>     
> 
>     
> 
>     {{
>     correction(False,
>     """
> \"Correction Q10.\" 
>         On pourrait utiliser la mémoïsation pour éviter la redondance des calculs, par exemple en utilisant un dictionnaire de clés ```(i,j)``` pour stocker les ```score_max(i,j,p)```.
>        
>         Exemple de code (non demandé) :
>         ```python linenums='1'
>         memo = {}
>         def score_max(i, j, p):
>             if i == len(p) - 1:
>           
> [Algorithmique > Programmation dynamique > Programmation dynamique]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 22 - Programmation dynamique
> Objectifs :
> ▷ Utiliser la programmation dynamique pour écrire un algorithme.
> ▷ Comprendre les exemples du rendu de monnaie et de l'alignement de séquences.
> ▷ Comparer un algorithme de force brute, un algorithme glouton et un algorithme en programmation dy-
> namique sur le problème du rendu de monnaie.
> ▷ Montrer les conséquences sur le coût en mémoire des algorithmes de programmation dynamique
> 1 Introduction
> On dispose de la grille2 × 3 ci-dessous.
> Question : Combien de chemins mènent du coin supérieur gauche au coin inférieur droit, en se déplaçant
> uniquement le long des traits horizontaux vers la droite et le long des traits verticaux vers le bas?
> Et pour une grille10 × 10?
> 2 Principe de la programmation dynamique
> La programmation dynamique est une technique créée parRichard Bellman dans les années 1950. À l'o

Questions à rédiger (points = 1 par défaut) :

- slot 1 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C7 : Dénombrer une quantité — L'élève calcule ou programme un comptage (machines d'un réseau, sauts, appels récursifs, occurrences) ; on évalue la maîtrise de ce qu'on compte et des bornes du comptage.
    gabarit : Déterminer le nombre de [éléments] [dans/lors de] [situation], ou écrire une fonction qui renvoie ce nombre.
    exemple réel (autre notion) : « 13. Sachant que le hash est écrit sur 256 bits, donner le calcul permettant d'obtenir le nombre de hash possibles. »
    détail du cours à évaluer (Programmation dynamique) : « Cette technique minimise le nombre d'opérations et accélère grandement l'exécution du programme. »

Le champ id vaut « I-prog_dynamique ».