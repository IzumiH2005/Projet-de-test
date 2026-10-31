# Plan I-os_commandes (inedit)

Notion : os_commandes (Architecture, OS et réseaux) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Arbres > 1.2 Exemples d'arbres]
> #### 1.2.1 La famille royale britannique (avant le 08 septembre 2022)
> 
> Redessinez de manière plus schématique cet arbre. Pour quelle raison cet arbre a-t-il été modifié par rapport à sa version orginale (voir ici ), qui laissait apparaître les parents de chaque enfant ?
> 
> #### 1.2.2 Le DOM d'une page web
> DOM : Document Object Model
> 
> #### 1.2.3 L'arborescence d'un disque dur
> Les systèmes Unix (MacOS ou GNU/Linux) organisent leur disque dur suivant l'arborescence ci-dessous :
> 
>     Quelque part à l'intérieur des dossiers contenus dans l'archive dossiers.zip se trouve un fichier ```tresor.txt```. Quel secret renferme-t-il ?
> 
>     Attention, cette recherche est à faire uniquement en ligne de commande :
> 
>     - ```ls``` : pour lister les dossiers et fichiers d'un répertoire
>     - ```cd Dossier``` : pour se rendre dans le repértoire ```Dossier```
>     - ```cd ..``` : pour remonter d'un niveau dans 
> [Architecture, OS et réseaux > OS > OS]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 16 - Systèmes d'exploitation
> Objectifs :
> ▷ Utiliser les commandes de base en ligne de commande.
> ▷ Gérer les droits et permissions d'accès aux fichiers.
> 1 Introduction
> Dans ce chapitre, nous allons revoir les commandes de base en ligne de commande, vues en classe de1ère,
> notamment celles qui sont les plus utilisées dans les deuxsystèmes d'exploitation ou OS (Operating System)
> les plus courants :Windows et Linux.
> Pour cela, au fur et à mesure que l'on présente les commandes systèmes, vous devez les tester sur chacun des
> systèmes d'exploitation.
> 2 Environnement de travail
> 2.1 Interpréteur de commandes
> Windows Linux
> Interpréteur : Interpréteur :
> Les commandes sont tapées dans un terminal en
> mode texte.
> Les commandes sont tapées dans un terminal en
> mode texte.
> Pour démarrer l'interpréteur de commandes sous
> Windows,ilvoussuffitd'allerdanslemenu

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 4. Écrire une fonction recombiner qui prend en paramètres deux instances m1 et m2 de la classe Pile qui sont respectivement la première et la deuxième moitié d'un jeu de cartes et qui renvoie une instance de la classe Pile qui est le jeu ob »
    exemple réel (autre notion) : « 5. Compléter, en utilisant autant de lignes que nécessaire, la fonction case_vide qui prend en paramètre une liste d'entiers pos et qui renvoie l'indice de 0. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « b. Écrire la méthode bien_construit demandée. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C23 : Donner une information précise — Restitution courte (nom d'un algorithme, coût, adresse, masque, type) ; on évalue une connaissance ou un calcul ponctuel.
    gabarit : Donner le [nom/coût/valeur] [de l'élément] [dans le contexte].
    exemple réel (autre notion) : « 3. Donner le coût du chemin identifié dans la question 2. »
    exemple réel (autre notion) : « a) Indiquer le type de la variable V. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « 11. Écrire le schéma relationnel des deux nouvelles tables en indiquant clairement les clés primaires et les clés étrangères. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 9. Déterminer la valeur de routeur_m.table après l'appel routeur_m.m_a_j((172, 64, 0, 2), 1, vecteurs). »
    exemple réel (autre notion) : « 1. On considère la machine d'adresse IPv4 192.168.1.1/24 »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 5. Déterminer le nombre de comparaisons effectuées par l'appel à majo_abs1([1, 4, 1, 6, 1, 7, 2, 1, 1]). »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « 2.a) Dans un ABR, où se trouve le plus petit élément ? Justifier. »
    détail du cours à évaluer (Rappels reseaux) : « Avec un système d'exploitation de typeLinux ou MacOs, la commande similaire se nommetraceroute. 9.3 ping A retenir! ping est une commande permettant de tester l'accessibilité d'une autre machine à travers un réseau IP. »

Le champ id vaut « I-os_commandes ».