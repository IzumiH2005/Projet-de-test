# Plan I-dictionnaire (inedit)

Notion : dictionnaire (Structures de données) — questions JAMAIS POSÉES aux annales

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

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C10 : Écrire ou corriger le code — L'élève écrit, recopie ou modifie le code d'une méthode ou fonction nommée, parfois pour corriger un comportement fautif ; on évalue l'implémentation et la gestion d'un cas d'erreur.
    gabarit : Écrire le code de la [méthode/fonction] [nom] qui [comportement]. / Modifier le code de [nom] pour que [comportement corrigé].
    exemple réel (autre notion) : « 5. Écrire le code de la méthode nombre_TdB de la classe Paquet qui renvoie le nombre total de "têtes de bœuf" contenus sur les cartes de ce paquet. »
    exemple réel (autre notion) : « 3. Écrire le tableau par ordre décroissant des nombres d'occurrences de chaque caractère du texte Perrine, puis dessiner l'arbre de codage correspondant. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 10. Écrire une fonction gerer qui récupère le processus en cours d'exécution p ainsi que la liste des files d'attente liste_files et qui implémente le programme donné en début d'énoncé pour gérer les processus. 1 def gerer(p, liste_files): 2 ... »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « 1. Expliquer pourquoi on fait cette hypothèse. »
    exemple réel (autre notion) : « 18. Expliquer en quoi la réalisation de ce projet pourrait être problématique. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « 6. Susie a fait une erreur de saisie en insérant le nom du lac, elle a écrit ‘Lc d Anterne'. Donner la requête permettant de corriger cette erreur. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 7. On considère la rue composée des maisons situées aux abscisses [0, 2, 3, 4, 5, 7, 9, 10.5, 11.5]. Recopier et compléter le schéma ci-dessous en indiquant l'emplacement des antennes selon cette nouvelle stratégie. On suppose que le rayon  »
    exemple réel (autre notion) : « c) Expliquer l'erreur suivante : >>> point_A = (3, 4) >>> point_A[0] 3 >>> point_A[0] = 2 »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 11. Dessiner, en indiquant le poids sur chaque arête, le graphe représentant le réseau aérien de la compagnie Droidevant. On dit qu'un graphe est connexe s'il existe un chemin entre chaque paire de sommets, autrement dit, si pour tout sommet s1 et pour tout so »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C17 : Identifier le rôle d'une clé — Questions sur les clés primaires et étrangères (identifier, justifier, expliquer le rôle), parfois clés de chiffrement ; on évalue la compréhension des contraintes d'intégrité.
    gabarit : Indiquer la clé [primaire/étrangère] de la relation [nom] et préciser son rôle.
    exemple réel (autre notion) : « 1. Pour chiffrer un message, on convertit chacun de ses caractères en binaire (à l'aide du format Unicode), et on réalise l'opération XOR bit à bit avec la clé.  Après conversion en binaire, et avant que l'opération XOR bit à bit avec la cl »
    détail du cours à évaluer (Dictionnaires) : « modification d'une valeur associée à une clé existante »

Le champ id vaut « I-dictionnaire ».