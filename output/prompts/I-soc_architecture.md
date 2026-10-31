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

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C6 : Exécuter mentalement une requête ou instruction suivante — L'élève lit une requête SQL ou une commande donnée et indique ce qu'elle renvoie. On évalue la capacité à simuler l'exécution.
    gabarit : Donner les valeurs renvoyées par la requête suivante : [requête].
    exemple réel (autre notion) : « 6. Écrire le résultat obtenu suite à l'exécution de la requête suivante si on l'applique sur les extraits des tables donnés.  SELECT nomSc FROM plante JOIN zone_geographique ON plante.zone = zone_geographique.num WHERE zone_geographique.zon »
    exemple réel (autre notion) : « e. Donner le résultat d'un parcours infixe sur l'arbre obtenu à la question 3.c. Expliquer pourquoi ce parcours permet d'affirmer que l'arbre est un arbre binaire de recherche. »
    support S8 : Phrases courtes isolées — Fragments brefs d'une phrase (hypothèse de scénario, consigne courte). Aucun matériau fourni ; groupe défini par la brièveté.
    exemple de support (autre notion) : « 3. Cette question porte sur la notion de clés étrangères. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « a. Indiquer le numéro du test (test 1 ou test 2) qui permet de vérifier qu'en fin de partie un participant égaré n'a pas rejoint par erreur la base adverse. »
    exemple réel (autre notion) : « 6. Expliquer l'erreur commise et proposer une solution. »
    support S4 : Prose multi-lignes sans forme distinctive — Texte d'énoncé courant sur plusieurs lignes, sujets divers (algorithmes, graphes, Huffman). Forme générique, pas de matériau spécifique.
    exemple de support (autre notion) : « 7. Reproduire le graphe ci -dessous puis ajouter une arête pour que le graphe devienne cohérent avec la table de routage d'Abi.   Figure 2. Relations entre les membres de l'association Frida rejoint l'association. Elle est amie avec Abi. À son arrivée dans l'a »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Donner le nom ou l'instruction — L'élève nomme un élément ou fournit une instruction ou un tuple précis. On évalue une réponse courte et exacte.
    gabarit : Donner le [nom|tuple|instruction] correspondant à [situation].
    exemple réel (autre notion) : « 6. Choisir parmi les tris proposés celui qui correspond à la fonction tri_liste : tri par insertion, tri par sélection, tri fusion, tri bulle. »
    exemple réel (autre notion) : « b. Déterminer le nom des deux joueurs qui sont les seuls à avoir joué dans le hangar. »
    support S5 : Besoin formulé pour requête SQL — Phrase décrivant en langage naturel l'information à extraire d'une base. L'élève la convertit en requête SQL.
    exemple de support (autre notion) : « 10. Écrire une requête SQL qui permet d'obtenir la liste des libellés des chapitres de la discipline ‘histoire'. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « 7. Pour un itinéraire de dimension 1 × 𝑛𝑛 justifier, éventuellement à l'aide d'un exemple, qu'il y a un seul chemin, c'est-à-dire que, quel que soit 𝑛𝑛 entier naturel, on a 𝑁𝑁(1, 𝑛𝑛) = 1. De même, 𝑁𝑁(𝑚𝑚, 1) = 1. »
    détail du cours à évaluer (SoC) : « Quel élément d'unSoC permet à un smartphone de communiquer avec d'autres machines? »

Le champ id vaut « I-soc_architecture ».