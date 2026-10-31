# Plan I-pile (inedit)

Notion : pile (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Listes Piles Files > 1.2 Comment seront traitées ces données linéaires ? Introduction des listes, des piles et des files]
> La nature des données ne fait pas tout. Il faut aussi s'intéresser à la manière dont on voudra les traiter :
> 
> - À quelle position les faire entrer dans notre structure ?
> - À quel moment devront-elles en éventuellement en sortir ?
> - Veut-on pouvoir accéder rapidement à n'importe quel élément de la structure, ou simplement au premier ? ou au dernier ?
> 
> Lorsque ces problématiques d'entrée/sortie n'interviennent pas, la structure «classique» de liste est adaptée. Mais lorsque celle-ci est importante, il convient de différencier la structure de **pile** de celle de **file**.
> 
> #### 1.2.1 Les piles (*stack*)
> 
> Une structure de **pile** (penser à une pile d'assiette) est associée à la méthode **LIFO** (Last In, First Out) :
> les éléments sont empilés les uns au-dessus des autres, et on ne peut toujours dépiler que l'élément du haut de la pile. Le dernier élément à être arrivé est donc le premier à
> [Structures de données > Les files > Les files]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 7 - Les files
> Objectifs :
> ▷ Connaître et comprendre le type abstrait file.
> ▷ Modéliser puis simuler le comportement d'une file.
> ▷ Distinguer les modes FIFO et LIFO des piles et des files.
> 1 Introduction
> Dans ce chapitre nous allons décrire desstructures de données linéairesappelées files. On rappelle qu'une
> structure de données est une organisation logique des données permettant de simplifier ou d'accélérer leur
> traitement.
> Il faut bien comprendre que lorsqu'on parle de structure de données, on parle d'une représentationabstraite
> qui n'est pas en lien direct avec son implémentation qui peut être réalisée de diverses manières suivant le langage
> de programmation, voire au sein d'un même langage de programmation.
> 2 Définition
> A retenir!
> En informatique, unefile (appelée queue en anglais) est une structure de données basée sur le principe
> « P

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C18 : Programmer sur un tableau d'entiers — Exercices pratiques où l'élève programme une fonction parcourant un tableau de nombres (recherche, tri, vérification) avec exemples ; on évalue l'algorithmique de base et le passage des tests.
    gabarit : Écrire une fonction [nom] qui prend en paramètre un tableau [tab] de [type] et qui renvoie [résultat]. Exemples : [assertions].
    exemple réel (autre notion) : « 4. Préciser à quoi correspond la somme des nombres d'occurrences. »
    exemple réel (autre notion) : « 1. Le tableau donné en annexe 1 indique, sur chaque ligne, le périphérique sélectionné, l'adresse à laquelle il souhaite accéder et l'opération à effectuer sur cette adresse. Compléter dans la dernière colonne de cette annexe, à rendre avec »
    support S6 : Texte avec parenthèses explicatives — Support riche en parenthèses (signatures, précisions, sous-questions (a)(b)) ; l'élève doit tenir compte des précisions et des paramètres annoncés.
    exemple de support (autre notion) : « 3. Supposons que le processus p1 demande la table traçante alors qu'elle est en cours d'utilisation par le processus p3. Parmi les états suivants, quel sera l'état du processus p1 tant que la table traçante n'est pas disponible :  a) élu b) bloqué c) prêt d) t »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « 3. Expliquer l'intérêt de vérifier, avant la validation du form ulaire, le format des informations saisies (par exemple qu'il n'y a pas de chiffre dans le nom ou qu'il y a bien un @ dans l'adresse de courriel). »
    exemple réel (autre notion) : « 6. Expliquer pourquoi la fonction cherche_itineraires peut être qualifiée de fonction récursive. »
    support S6 : Texte avec parenthèses explicatives — Support riche en parenthèses (signatures, précisions, sous-questions (a)(b)) ; l'élève doit tenir compte des précisions et des paramètres annoncés.
    exemple de support (autre notion) : « 2. Le code SQL suivant a été utilisé pour créer la relation Films. Donner le domaine (c'est-à-dire le type) des attributs IdFilm et Description. CREATE TABLE Films ( IdFilm INT AUTO_INCREMENT PRIMARY KEY, Titre VARCHAR(20), Description VARCHAR(150), Realisateu »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « a. déplacer le fichier "saxo.mp3" du dossier "documents" vers le dossier "musiques" ? »
    exemple réel (autre notion) : « 4. Combien de fois la boucle est-elle exécutée avec le mot " routeur " ? Proposer une amélioration de l'algorithme de la fon ction palindrome1 que l'on appellera palindrome2 permettant d'éviter les tours de boucle inutiles. Justifier votre  »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 14. Le protocole de routage qui semble être utilisé est RIP, p uisque avec OSPF R1-R5-R4-R3 serait plus court que R1-R3. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C20 : Énoncés de mise en situation — Mélange d'énoncés introductifs et de questions descriptives (arbres, parité, interfaces) ; groupe défini par des tournures génériques plutôt que par un geste.
    gabarit : On considère [situation]. Indiquer [éléments] qui [propriété].
    exemple réel (autre notion) : « c. Combien peut-on connecter de machines sur ce sous-réseau ?  Les adresses IP des interfaces des routeurs sont do nnées suivant la stratégie suivante: Le dernier octet (O4) a pour valeur décim ale le numéro du routeur. »
    détail du cours à évaluer (Listes Piles Files) : « Comme expliqué précédemment, une pile travaille en mode LIFO (Last In First Out). »

Le champ id vaut « I-pile ».