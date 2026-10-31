# Plan I-recherche_dichotomique (inedit)

Notion : recherche_dichotomique (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Diviser pour regner > Diviser pour regner]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 24 - Diviser pour régner
> Objectifs :
> ▷ Ecrire un algorithme en utilisant la méthode"diviser pour régner".
> 1 Introduction
> Nous avons vu en première deux algorithmes de tris assez naturels, mais peu efficaces : letri par insertionet
> le tri par sélectionen classe de Première.
> Cette année, nous allons étudier un algorithme beaucoup plus efficace et très utilisé, inventé parJohn Von
> Neumann en 1945 : letri par fusion.
> Cet algorithme nous permettra d'illustrer la méthodediviser pour régnerque nous avions également déjà
> vue lors de larecherche dichotomiqueen classe de Première.
> 2 La dichotomie (rappels)
> Nous avons vu en classe dePremièrel'algorithme dedichotomie. Ce mot, qui vient du grecdikhotomia, signifie
> « division en deux parties ».
> Notre but ici est la recherche de la présence (ou non) d'un élément dans une liste triée. Notre fonction renv
> [Algorithmique > Diviser pour regner > 1.1 Version impérative]
> {#
> 
>     ```python linenums='1'
>     def recherche_dichotomique(tab, val) :
>         '''
>         renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
>         '''
>         ...
>     ```
> #}
> 
>     ```python linenums='1'
>     def recherche_dichotomique(tab, val) :
>         '''
>         renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
>         '''
>         i_debut = 0
>         i_fin = len(tab) - 1
>         while i_debut >> tab = [1, 5, 7, 9, 12, 13]
> >>> recherche_dichotomique(tab, 12)
> True
> >>> recherche_dichotomique(tab, 17)
> False
> ```
> 
> À chaque tour de la boucle ```while```, la taille de la liste est divisée par 2. Ceci confère à cet algorithme une **complexité logarithmique** (bien meilleure qu'une complexité linéaire).

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Analyser un code fourni — Un extrait de code (def numéroté) est donné, à compléter ou à exécuter mentalement ; on évalue la lecture de code et la compréhension de ce qu'il fait.
    gabarit : On considère le code suivant : [code]. [Compléter la ligne n / Donner ce qu'affiche l'appel [appel]].
    exemple réel (autre notion) : « 6. Compléter la fonction distance_totale :  1 def distance_totale(dep): 2 total = 0 3 for i in range(...): 4 ... 5 return total »
    exemple réel (autre notion) : « 8. On compléter la méthode sortir. 11 def sortir(self): 12 """Retire et renvoie le dernier élément de 13 liste_priorite""" 14 assert not self.est_vide 15 return self .liste_priorite.pop() »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 3. La requête SELECT forceVent, dirVent FROM observation NATURAL JOIN st ation WHERE nom = 'BOURAKE' AND date = '2023010214' ; permet d'obtenir la force et la direction du vent à BOURAKE le 2 janvier 2023 à 14h. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « d) Donner, en fonction de n, la complexité en temps de la fonction liste_segments. »
    exemple réel (autre notion) : « 1. a . Quelle est la taille de l'arbre ci-dessus ? »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 2. Pourquoi la requête ci-dessous provoque-t-elle une erreur ?  DELETE FROM Patientes WHERE numPatiente = 13858; »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C23 : Donner une information précise — Restitution courte (nom d'un algorithme, coût, adresse, masque, type) ; on évalue une connaissance ou un calcul ponctuel.
    gabarit : Donner le [nom/coût/valeur] [de l'élément] [dans le contexte].
    exemple réel (autre notion) : « 6. Donner le solde en nsicoin de Bob à l'issue du bloc2. »
    exemple réel (autre notion) : « 3. Donner les adresses IP attribuées, selon ce principe, aux routeurs C et F dans le réseau 10.42.0.16/30, ainsi que les adresses IP attribuées aux routeurs C et D dans le réseau 10.42.0.12/30. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « 13. Écrire la requête SQL permettant d'obtenir la table des numéros des comptes appartenant aux personnes portant le nom Richard Oise au moyen d'une jointure. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C7 : Dénombrer une quantité — L'élève calcule ou programme un comptage (machines d'un réseau, sauts, appels récursifs, occurrences) ; on évalue la maîtrise de ce qu'on compte et des bornes du comptage.
    gabarit : Déterminer le nombre de [éléments] [dans/lors de] [situation], ou écrire une fonction qui renvoie ce nombre.
    exemple réel (autre notion) : « c. (poids, taille) »
    détail du cours à évaluer (Diviser pour regner) : « Les algorithmes de dichotomie présentés ci-dessous ont tous en commun de diviser par deux la taille des données de travail à chaque étape. »

Le champ id vaut « I-recherche_dichotomique ».