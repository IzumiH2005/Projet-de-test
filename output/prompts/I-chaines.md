# Plan I-chaines (inedit)

Notion : chaines (Programmation) — questions JAMAIS POSÉES aux annales

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

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C11 : Traiter des chaînes de caractères — Questions de programmation ou d'analyse portant sur des chaînes (parcours, inversion, validation, exemple qui fait échouer un test) ; on évalue la manipulation de caractères et d'indices.
    gabarit : Écrire une fonction [nom] qui prend en paramètre une chaîne de caractères [s] et renvoie [résultat]. Exemple : [nom]([entrée]) renvoie [sortie].
    exemple réel (autre notion) : « 7. Déterminer le nombre de comparaisons effectuées si on applique l'algorithme précédent à la chaine de caractères 'tab[2*(i + 4)] - tab[3]'. En déduire le nombre maximum de comparaisons effectuées si on applique l'algorithme précédent à un »
    exemple réel (autre notion) : « b. Indiquer sans justification la complexité en temps de calcul de cet algorithme pour un mot de longueur n. Remarque : on ne comptera que les comparaisons de caractères. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 1. Expliquer pourquoi, lorsqu'un formulaire contient une quanti té importante de données, il est préférable d'utiliser la méthode POST plutôt que GET. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C24 : Compléter une fonction à trous — L'élève recopie et complète une fonction ou une table entière (parfois à partir d'une ligne donnée) ; on évalue l'achèvement d'un code partiellement fourni.
    gabarit : Recopier et compléter la fonction [nom] (à partir de la ligne [n]) qui [comportement].
    exemple réel (autre notion) : « 4. Recopier et compléter la section de code que Bachir doit modifier pour répondre à l'annonce. »
    exemple réel (autre notion) : « 4. a. Donner le contenu des piles B et q à la fin de chaque itération de la boucle while de la ligne 5. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 8. Recopier et compléter les lignes 8, 9, 14 et 15 de la fonction calcule_aux qui prend en paramètre une liste de liste carte et renvoie la liste auxiliaire associée.  1 def calcule_aux(carte):  2 n = len(carte)  3 aux = [[0 for j in range(n)] for i in range(n »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C13 : Raisonner sur une figure — La question s'appuie sur une figure numérotée (arbre, réseau, arborescence, configuration) que l'élève lit, mesure ou complète ; on évalue la lecture d'une représentation graphique.
    gabarit : En vous appuyant sur la figure [n], [donner/justifier/compléter] [propriété de l'objet représenté].
    exemple réel (autre notion) : « 7. Justifier qu'il s'agit d'une fonction récursive. »
    exemple réel (autre notion) : « 9. Justifier que le code proposé ci-dessus ne permet pas de s'assurer que la contrainte d'un nombre maximal de routes contenues dans la liste est respectée.  EN_NOzUzMD2M0ODAczOT4UzMmTYxMj1A2MDEO2OTtQ0MDTcx On souhaite créer une classe Rout »
    support S0 : Énoncé en prose avec numéros — Support textuel ordinaire mêlant prose et nombres (routeurs, adresses, tailles) ; l'élève travaille à partir d'une mise en situation décrite, sans matériau structuré dominant.
    exemple de support (autre notion) : « 11. Donner une valeur possible de graphe_4_4[9] en supposant que graphe_4_4 est la liste d'adjacence représentant le graphe associé à une grille à 4 lignes et 4 colonnes. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C11 : Traiter des chaînes de caractères — Questions de programmation ou d'analyse portant sur des chaînes (parcours, inversion, validation, exemple qui fait échouer un test) ; on évalue la manipulation de caractères et d'indices.
    gabarit : Écrire une fonction [nom] qui prend en paramètre une chaîne de caractères [s] et renvoie [résultat]. Exemple : [nom]([entrée]) renvoie [sortie].
    exemple réel (autre notion) : « 3. Écrire une fonction compte_fermante qui prend en paramètre une chaine de caractères txt et qui renvoie le nombre de parenthèses fermantes qu'il contient. »
    détail du cours à évaluer (Recherche textuelle) : « #### 1.3.1 Récupération du texte dans une seule chaîne de caractères »

Le champ id vaut « I-chaines ».