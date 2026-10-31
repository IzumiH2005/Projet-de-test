# Plan I-chaines (inedit)

Notion : chaines (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Listes Piles Files > Introduction]
> Exercice 5 du sujet Centres Étrangers 1 - 2021
> 
>     Exercice 1 du sujet La Réunion J2 - 2022
> 
>     Exercice 2 du sujet Métropole Candidats Libres J1 - 2021
> 
>     Exercice 5 du sujet Amérique du Nord J1 - 2021
> 
>     Exercice 2 du sujet Centres Étrangers J1 - 2022
> 
>     Exercice 3 du sujet Centres Etrangers J1 - 2023
> 
>     Jeu du Simon
> 
>     Cet exercice est basé sur l'énigme n°5 d'Advent Of Code 2018.
> 
>     Le but est de réduire le plus possible une chaîne de caractères (comme ```dabAcCaCBAcCcaDA``` ) en obéissant à la règle suivante :
> 
>         Dès que deux lettres identiques mais de casse différente (majuscule-minuscule ou minuscule-majuscule) sont côte à côte dans la chaîne, on les supprime de la chaîne.
> 
>     Exemple : 
>     ```
>     dabAcCaCBAcCcaDA  On enlève le premier 'cC'.
>     dabAaCBAcCcaDA    Cela donne naissance à un 'Aa', qu'on enlève.
>     dabCBAcCcaDA      On enlève alors 'cC' (ou 'Cc'
> [Programmation > Pratiques de programmation > 4.3 Le module ```doctest```]
> Le module ```doctest```  permet d'écrire les tests **à l'intérieur** de la docstring d'une fonction. 
> 
> Considérons une fonction dont le but est de compter les voyelles du mot passé en paramètre.
> 
> ```python
> def compte_voyelles(mot):
>     """
>     renvoie le nombre de voyelles du mot donné en paramètre.
>     >>> compte_voyelles("python")
>     2
>     >>> compte_voyelles("HTTP")
>     0
>     >>> compte_voyelles("eau")
>     3
>     """
>     voyelles = "aeiou"
>     total = 0
>     for lettre in mot:
>         if lettre in voyelles:
>             total += 1
>     return total
> ```
> 
> Observez bien la docstring : elle contient explicitement ce qu'on veut que renvoie le terminal lorsqu'on appellera la fonction.
> On écrit donc les trois chevrons ```>>>``` suivi de l'appel à la fonction, et à la ligne en dessous ce que nous espérons que la fonction nous renvoie.
> On peut écrire autant de tests que l'on veut.
> 
> Ensuite, en co

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 5. Écrire le code de la méthode est_resultat pour la classe Feuille_resultat. »
    exemple réel (autre notion) : « 11. Écrire le code de la fonction scratch qui prend en paramètres un dictionnaire de performances dico et une année annee, et qui renvoie le meilleur temps (toutes catégories confondues) de cette année. On suppose que annee est une clé prés »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 13. Écrire une fonction valeurs_chemin qui prend en paramètre chemin une liste de sommets et renvoie la liste de leurs valeurs. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « b. Quel type de parcours a été réalisé par le système d'exploitation ? »
    exemple réel (autre notion) : « a. Expliquer dans quel cas cette méthode renvoie None. »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 2. Dans cette question uniquement, on considère que l'acheminement des colis de plus de 25 kg est refusé par le transporteur.  Recopier et modifier le code de la fonction ajouter_colis afin qu'elle ajoute le colis à la liste si son poids est inférieur ou égal  »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 7. Donner une requête qui renvoie le prix maximal d'un appartement situé dans un immeuble de la rue 'la mer'. »
    exemple réel (autre notion) : « 1. (a) Donner sans justiﬁcation la hauteur de cet arbre. (b) Donner sans justiﬁcation la valeur booléenne de l'expression"Allemagne" < "Portugal" . (c) Recopier l'arbre après l'ajout de"Allemagne", de "Portugal" et de "Luxembourg" dans cet  »
    support S4 : Prose multi-lignes sans forme distinctive — Texte d'énoncé courant sur plusieurs lignes, sujets divers (algorithmes, graphes, Huffman). Forme générique, pas de matériau spécifique.
    exemple de support (autre notion) : « 2. Indiquer l'état de chacun des trois processus P1, P2 et P3 dans cette situation. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 3) Écrire en langage Python une fonction surmax qui prend en paramètre listeV, du même type que la variable listeVilles, et renvoie la ville ayant la superficie la plus grande. On admet que deux villes n'ont pas la même superficie.  EXERCIC »
    détail du cours à évaluer (Recherche textuelle) : « #### 1.3.1 Récupération du texte dans une seule chaîne de caractères »

Le champ id vaut « I-chaines ».