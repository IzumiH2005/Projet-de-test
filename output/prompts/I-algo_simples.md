# Plan I-algo_simples (inedit)

Notion : algo_simples (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Programmation objet > Programmation objet]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 3 - Programmation orientée objet
> Objectifs :
> ▷ Connaître le vocabulaire de la programmation objet : classes, attributs, méthodes, objets.
> ▷ Ecrire la définition d'une classe
> ▷ Accéder aux attributs et méthodes d'une classe.
> 1 Introduction
> Jusqu'à présent nous avons utilisé des objets dont le type est prédéfini :int, float, bool, str, list,
> tuple, dict. Sans le savoir, nous avons découvert les concepts de laprogrammation orientée objet
> ou POO. Ainsi, en classe de Première, nous avions déjà appris à utiliser des méthodes associées à ces
> types, comme :
> ma_liste.append(valeur)
> Comme de nombreux autres langages tels queJava ou C++, Python est un langage orienté objet .
> On peut donc dire que tout y estobjet. Une variable de typeint est en fait un objet de typeint donc
> construit à partir de la classeint. Idem pour lesfloat et str. Mais également
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

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C23 : Donner une information précise — Restitution courte (nom d'un algorithme, coût, adresse, masque, type) ; on évalue une connaissance ou un calcul ponctuel.
    gabarit : Donner le [nom/coût/valeur] [de l'élément] [dans le contexte].
    exemple réel (autre notion) : « 7. Écrire une requête qui permet d'afficher le type, la marque et le nom de l'agence pour l'ensemble des véhicules. »
    exemple réel (autre notion) : « 9. Donner, dans l'ordre, les numéros des balises rencontrées par ce sportif. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « d. La priorisation »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « 4. Quel est le rôle d'un switch ? »
    exemple réel (autre notion) : « Question 1 1. Dans le modèle relationnel, quel est l'intérêt de l'attributnum_eleve. »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « a. Parmi les quatre propositions suivantes, indiquer le type d'erreur affiché : • ZeroDivisionError • ValueError • TypeError • IndexError »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 16. Écrire une fonction valeur_max_stock qui prend en paramètre un dictionnaire effectif et qui renvoie la valeur maximale en euro que peut rapporter le stock à l'entreprise en optimisant le découpage de chaque planche afin qu'elle rapporte »
    exemple réel (autre notion) : « 8. Écrire une fonction Python infini, récursive, telle que l'appel infini(n) ne termine pour aucun entier n. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 10. Indiquer comment Bob peut déchiffrer le message que lui envoie Alice. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C19 : Déterminer un chemin ou élément — Questions de détermination (chemin d'un paquet, répertoire, sous-séquence, protocole) sans geste unique, souvent en réseau ; on évalue une déduction à partir du contexte.
    gabarit : Déterminer [le chemin/l'élément] [de A à B / vérifiant la condition] dans [situation].
    exemple réel (autre notion) : « 11. Nommer le tri utilisé. »
    détail du cours à évaluer (Routage) : « Ce protocole consiste à minimiser la somme des coûts des liaisons empruntées. »

Le champ id vaut « I-algo_simples ».