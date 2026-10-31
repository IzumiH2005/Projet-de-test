# Plan I-glouton (inedit)

Notion : glouton (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
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
> [Programmation > Pratiques de programmation > 4.2 Revoilà les ```assert```]
> Utiliser des ```assert``` permet d'écrire très simplement les tests précédents.
> 
> Reprenons notre fonction ```valeur_absolue()```. Sa fonction test  ```test_valeur_absolue()``` peut s'écrire :
> 
> ```python
> def test_valeur_absolue():
>     assert valeur_absolue(-3) == 3
>     assert valeur_absolue(0) == 0
>     assert valeur_absolue(7) == 7
> 
> ```
> 
> **Exercice :**  
> Écrire une fonction ```maxi(liste)``` qui renvoie le plus grand élément de la liste ```liste``` passée en paramètre (de préférence sans utiliser la fonction ```max()``` ...).  
> Vous écrirez **d'abord** une fonction ```test_maxi()``` avant d'écrire la fonction ```maxi(liste)```

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C22 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes précisément numérotées d'une fonction à trous ; on évalue la compréhension de la logique locale du code et le respect de la spécification.
    gabarit : Recopier et compléter les lignes [n1] à [n2] de la fonction [nom] afin qu'elle [comportement].
    exemple réel (autre notion) : « 4. Recopier et compléter sur la copie les lignes 5, 9 et 10 de la fonction separe_elements. »
    exemple réel (autre notion) : « 3. Recopier et compléter les lignes 2, 7, 9, 11 et 13 du code de la fonction dernier. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 11. Expliquer dans quel cas la fonction precede exécutera la dernière instruction return de la ligne 7. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 3. Écrire une fonction note_maxi qui prend en paramètre un dictionnaire dico (de même structure que dico_livres) et qui renvoie la note maximale. »
    exemple réel (autre notion) : « c) Écrire une fonction somme en langage Python qui prend un paramètre W du même type que la variable V et qui renvoie la somme des valeurs de W. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 7. Écrire une fonction comptes_dans_le_rouge qui prend en paramètre comptes une liste de comptes et qui renvoie la liste des comptes de cette liste dont le montant est strictement négatif. »

- slot 3 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : milieu d'exercice
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 18. Indiquer, en justifiant, laquelle de ces deux commandes a produit l'affichage :  4 packets transmitted, 4 received, 0% packet loss, time 3002ms »
    exemple réel (autre notion) : « 2. dossier = racine »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 7. Recopier et compléter la ligne 2 du code de la fonction select_tel. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C12 : Exploiter l'élément fourni ci-dessous — La consigne renvoie à un document joint (commandes, circuit, requêtes numérotées, classe, code) à sélectionner, compléter ou utiliser ; on évalue la lecture attentive du support plus qu'une notion précise.
    gabarit : Parmi les [éléments] ci-dessous, [sélectionner/compléter/utiliser] ceux qui permettent de [objectif].
    exemple réel (autre notion) : « 9. Recopier et compléter le schéma ci-dessous avec les processus P1 à P5 en utilisant les informations présentes dans le tableau ci-dessus et l'algorithme d'ordonnancement "par ordre de soumission". »
    détail du cours à évaluer (Programmation dynamique) : « Compléter la fonction _glouton ci-dessous qui calcule de manière gloutonne le "meilleur" trajet d'une pyramide »

Le champ id vaut « I-glouton ».