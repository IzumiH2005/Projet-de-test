# Plan I-soc_architecture (inedit)

Notion : soc_architecture (Architecture, OS et réseaux) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Architecture, OS et réseaux > Processus > Processus]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 17 - Les processus
> Objectifs :
> ▷ Décrire la création d'un processus, l'ordonnancement de plusieurs processus par le système.
> ▷ Mettre en évidence le risque de l'interblocage (deadlock).
> 1 Introduction
> Dans les années 1970, les ordinateurs personnels n'étaient pas capables d'exécuter plusieurs tâches à la fois. On
> lançait un programme et on y restait jusqu'à ce que celui-ci "plante" ou se termine.
> Les systèmes d'exploitation récents (Windows, Linux ou MacOS par exemple) permettent d'exécuter plusieurs
> tâches simultanément - ou en tous cas, donner l'impression que celles-ci s'exécutent en même temps. C'est ce
> que l'on appelle lepseudo-parallélisme.
> A un instant donné, il n'y a donc pas un mais plusieurs programmes qui sont en cours d'exécution sur un
> ordinateur : on les nommeprocessus.
> Une des tâches du système d'exploitation est d'allouer 
> [Architecture, OS et réseaux > SoC > SoC]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 18 - Les systèmes sur puce
> Objectifs :
> ▷ Connaître quelques composants intégrés d'un système sur puce
> ▷ Identifier les principaux composants sur un schéma de circuit
> ▷ Comprendre les avantages de leur intégration en terme de vitesse et de consommation
> 1 Introduction
> La réduction de taille des éléments des circuits électroniques a conduit à l'avènement de systèmes sur puce.
> Ce SoC (pour System on a Chipen anglais) qui regroupe dans un seul circuit nombre de fonctions autrefois
> effectuées par des circuits séparés assemblés sur une carte électronique.
> Un tel système sur puce est conçu et mis au point de façon logicielle, ses briques électroniques sont accessibles
> par des API, comme pour les bibliothèques logicielles.
> 2 De l'ordinateur au smartphone/tablette
> Dans un ordinateur “classique” tel qu'un PC de bureau, le "hardware" est organisé aut

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Analyser un code fourni — Un extrait de code (def numéroté) est donné, à compléter ou à exécuter mentalement ; on évalue la lecture de code et la compréhension de ce qu'il fait.
    gabarit : On considère le code suivant : [code]. [Compléter la ligne n / Donner ce qu'affiche l'appel [appel]].
    exemple réel (autre notion) : « 2. On écrit une fonction voisins. def voisins(graphe, k): return graphe[k] »
    exemple réel (autre notion) : « 2. On considère la fonction maxi(L) qui prend comme paramètre une liste L de nombres et renvoie le plus grand nombre de cette liste : 1| def maxi(L) : 2| indice = 0 3| maximum = 0 4| while indice <= len(L) : 5| if L[indice] > maximum : 6| m »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « Question 3 Créer une fonction retourner ayant pour paramètres une pile P et un entier j. Cette fonc- tion inverse l'ordre desj derniers éléments empilés et ne renvoie rien. On pourra utiliser deux piles auxiliaires. Exemple : si P est la pile de laquestion 1(a »

- slot 2 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : milieu d'exercice
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 2. Donner les valeurs prises par la variable locale valeur lors de l'exécution de creer_jeu(9). »
    exemple réel (autre notion) : « 5. On reçoit le tableau suivant. 1 1 1 1 1 0 0 1 1  Sachant qu'une unique erreur de transmission s'est produite, recopier le tableau et entourer le bit qui a subi cette erreur (transformation d'un 0 en 1 ou d'un 1 en 0). »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 4. Depuis l'état e2 = [1, 1, 0, 1, 0, 0], on effectue un lancer de 5. Donner l'état qu'on obtient après le lancer et l'effet de la gravité. On souhaite écrire une fonction lancer_balle qui prend en paramètres un état etat de jonglage (comme décrit ci -dessus)  »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « 1. a. Cette fonction est-elle récursive ? Justifier. »
    exemple réel (autre notion) : « 5. Est-il possible qu'un ordinateur connecté au réseau du lycée possède la même adresse IP que l'élève à son domicile ?  ◦ Oui, à condition que les connexions n'aient pas lieu au même moment. ◦ Oui, car les adresses 192.168.x.x ne sont pas  »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « b. le nombre de commandes passées depuis le '2022-01-01' inclus. On précise que le type DATE permet de représenter une date par une chaîne de caractère au format 'AAAA-MM-JJ' et que ces dates peuvent être comparées à l'aide des opérateurs usuels (=, !=, >, <,  »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « b. De manière plus générale, que renvoie la fonction mystere pour une chaîne représentant un déplacement donné ? »
    détail du cours à évaluer (SoC) : « Quel élément d'unSoC permet à un smartphone de communiquer avec d'autres machines? »

Le champ id vaut « I-soc_architecture ».