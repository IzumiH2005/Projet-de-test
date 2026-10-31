# Plan I-tuple (inedit)

Notion : tuple (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
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
> [Structures de données > Structures donnees > Structures donnees]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 4 - Les structures de données
> Objectifs :
> ▷ Remettre en mémoire les structures de données vues enPremière
> ▷ Montrer qu'il existe plusieurs implémentations possibles
> 1 Introduction
> En informatique, on manipule essentiellement des données. Lorsqu'elles sont simples comme desnombres,
> des chaînes de caractères ou des booléens, on peut les stocker dans des variables qui seront typées en
> fonction de la nature de la donnée.
> 2 Définition
> A retenir!
> Une structure de données est une organisation logique des données permettant de simplifier ou
> d'accélérer leur traitement.
> 3 Exemple
> Par exemple, si on a écrit un code avec les affectations suivantes :
> 1 n = 4
> 2 p = -5
> 3 r = 0.7
> 4 phrase = 'hello'
> 5 test = True
> Python est un langage avec untypage dynamique, c'est-à-dire que le type de la variable est automa-
> tiquement déterminé la première fois qu'elle

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 8. Écrire en langage Python une fonction récursive calcul_somme(arbre). »
    exemple réel (autre notion) : « 4. Ecrire une fonction creation_dossiers(tab) qui prend en paramètre un tableau de chaînes de caractères et qui crée et mod ifie les droits des dossiers au nom de ces chaines de caractères avec l es mêmes droits que le sous-dossier TURING_A »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 5. Écrire une fonction chaine_evalue qui prend en paramètres un plateau et une chaine, et renvoie la valeur associée à une telle chaîne. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : milieu d'exercice
    manière de demander C17 : Question directe « quelle est » — L'élève indique une valeur, une propriété ou un élément d'une structure. Réponse courte ; le groupe reste un peu hétérogène.
    gabarit : Quelle est la [valeur|propriété] de [objet] ?
    exemple réel (autre notion) : « 5. Donner et justifier la valeur renvoyée par la fonction couper pour le tableau de caractères suivant.  [('n', 4), ('a', 2), ('o', 2), ('S', 1), ('h', 1), ('-', 1), ('F', 1)] Afin d'implémenter les arbres de codage, on se munit de la clas »
    exemple réel (autre notion) : « 8. La fonction parcoursGraphe renvoie une liste parcours. Indiquer la valeur renvoyée par l'appel de fonction : parcoursGraphe(s1)  On cherche maintenant le site le plus populaire, celui dont la valeur de popularité est la plus grande. »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 1. Recopier et compléter le tableau suivant, en indiquant la valeur des paramètres lors des appel récursifs, pour un appel initial sous_listes([9, 3, 7 ], [[]]).  EN_OOTgzNT7QzNjAc0ND8UzMsTYxMj0A2NTAAwMDzAxNOjIx  Évolution des paramètres lors des appels récurs »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « b. Décrire quel peut être le rôle de la fonction mystere. »
    exemple réel (autre notion) : « 2. Quel est l'identifiant du processus parent à l' origine de tous les processus concernant le navigateur Web (chromium-browser) ? »
    support S11 : Texte contenant des tirets — Matériau marqué par des tirets (mots composés, puces, listes chaînées). Artefact typographique mêlant fonctions récursives et énigmes.
    exemple de support (autre notion) : « 3. On décide de parcourir cet arbre pour obtenir la liste des identifiants dans l'ordre lexicographique. Recopier la lettre correspondant au parcours à utiliser parmi les propositions suivantes : A - Parcours en largeur d'abord B - Parcours en profondeur dans  »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 9. Donner la requête SQL permettant d'obtenir uniquement les id et les lieux (colonne lieu) des trails dont la distance dépasse 50 km. »
    détail du cours à évaluer (Routage) : « Un vecteur de distance est un couple (adresse, distance). »

Le champ id vaut « I-tuple ».