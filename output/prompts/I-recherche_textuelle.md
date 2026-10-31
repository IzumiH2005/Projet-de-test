# Plan I-recherche_textuelle (inedit)

Notion : recherche_textuelle (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Recherche textuelle > Recherche textuelle]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 23 - Recherche textuelle
> Objectifs :
> ▷ Comprendre le principe de la recherche textuelle.
> ▷ Etudier l'algorithme deBoyer-Moore pour la recherche d'un motif dans un texte.
> 1 Introduction
> Tout logiciel de traitement de texte possède une fonction de recherche textuelle, permettant de trouver un mot
> ou une partie d'un mot (chaîne ou sous-chaîne). Il en est de même pour les navigateurs Internet.
> Ainsi, le raccourci clavierCTRL+F permet de rechercher dans la page la chaine"mot".
> Les algorithmes qui permettent de trouver unesous-chaîne de caractères dans une chaine de caractères plus
> grande sont des "grands classiques" de l'algorithmique. On parle aussi de recherche d'unmotif dans un texte.
> Voici un exemple. Soit le texte suivant :
> "Les sanglots longs des violons de l'automne blessent mon coeur d'une langueur monotone. Tout suffocant et
> blême, qu
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

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « d. ligne 5 : compléter l'adresse IP décimale du réseau 1.  Adresse IP (V4) du PC3 Ligne 1 172 150 4 30 »
    exemple réel (autre notion) : « 1. (a) Onconsidèrelaﬁle Fsuivante: déﬁlementenﬁlement "rouge""vert""jaune""rouge""jaune" Quel sera le contenu de la pile P et de la ﬁle F après l'exécution du programme Python suivant? 1 P = creer_pile_vide () 2 while not ( est_vide ( F )): »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 7. Écrire une méthode generer_demineur qui permet de mettre à jour l'attribut grille_demineur pour que chaque cellule ne contenant pas de mine, contienne le nombre de mines qui lui sont voisines.  Par exemple :  >>> demineur_nsi = demineur(6, 6, 0.278) >>> d »

- slot 2 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « a. Expliquer quel(s) problème(s) peuvent apparaître si on décide d'ajouter uniquement un attribut tarif_horaire à la relation prestations. »
    détail du cours à évaluer (Recherche textuelle) : « Re-écrire l'algorithme précédent en s'arrêtant dès qu'une occurrence de »

Le champ id vaut « I-recherche_textuelle ».