# Plan I-modele_relationnel (inedit)

Notion : modele_relationnel (Bases de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Bases de données > Base de donnees relationnelles > Base de donnees relationnelles]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 8 - Les bases de données relationnelles
> Objectifs :
> ▷ Identifier les concepts définissant le modèle relationnel.
> ▷ Maîtriser les définitions de : relation, attribut, domaine, clé primaire, clé étrangère, schéma relationnel
> ▷ Exprimer les contraintes d'intégrité d'une base de données
> ▷ Savoir réaliser un schéma relationnel
> ▷ Savoir repérer les anomalies dans le schéma relationnel d'une base de données
> 1 Introduction
> Les bases de données sont aujourd'hui incontournables, car très peu d'informations restent encore stockées sur
> du papier. Nous avons vu en classe dePremière comment utiliser des données comme celle d'un tableur avec
> notamment l'utilisation du formatcsv.
> En effet, prenons l'exemple d'une table contenant quelques films :
> Titre Réalisateur Année Durée
> 2001 : A Space Odyssey Stanley Kubrick 1968 149
> Alien Ridley Scott 1979 117
> Blad
> [Bases de données > Modele relationnel > 3. Clé Primaire]
> Une clé primaire est un attribut (ou une réunion d'attributs) **dont la connaissance suffit à identifier avec certitude un unique enregistrement**.
> 
> Par exemple, la clé primaire de la relation des personnes nées en France pourrait être leur numéro de Sécurité Sociale.
> 
>  Observons, dans notre relation précédente, ce qui peut être une clé primaire et ce qui ne peut pas l'être.
> 
> - Titre : cet attribut pourrait jouer le rôle de clé primaire. En effet, notre table ne contient pas deux livres ayant le même titre.
> - Auteur : cet attribut pourrait jouer le rôle de clé primaire. En effet, notre table ne contient pas deux livres ayant le même auteur.
> - Éditeur : cet attribut ne peut **pas** jouer le rôle de clé primaire. En effet, la donnée de l'attribut «Actes Sud» renvoie vers 4 livres différents.
> - ISBN : (International Standard Book Number) cet attribut est un numéro unique spécifique à chaque

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C17 : Identifier le rôle d'une clé — Questions sur les clés primaires et étrangères (identifier, justifier, expliquer le rôle), parfois clés de chiffrement ; on évalue la compréhension des contraintes d'intégrité.
    gabarit : Indiquer la clé [primaire/étrangère] de la relation [nom] et préciser son rôle.
    exemple réel (autre notion) : « 2. Définir l'acronyme RAM. »
    exemple réel (autre notion) : « 8. Rappeler brièvement ce qu'est un algorithme de chiffrement asymétrique. On suppose à présent que Bob possède une clé publique et une clé privée. La clé publique de Bob est supposée connue par le serveur. »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 3. Étant donnée une liste pos représentant une position du taquin, donner une instruction, basée sur l'instruction assert, qui permet d'interrompre le programme si la taille de la liste pos n'est pas correcte (c'est -à-dire différente de 9). »

- slot 2 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 6. Déterminer la liste auxiliaire aux_B associée à la carte représentée par carte_B.  carte_B = [  [1, 1, 1, 1],  [0, 1, 1, 1],  [0, 1, 1, 1],  [1, 0, 1, 1], ] On considère une carte carte_C de taille 6 ainsi que la liste auxiliaire aux_C a »
    exemple réel (autre notion) : « 2. a. Donner la valeur renvoyée par l'appel A.est_triee(). »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 15. Indiquer quel sera l'effet de la requête suivante : INSERT INTO image VALUES (2923, 'Volcans du massif central', '', 400, 400, 1430); »

- slot 3 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C17 : Identifier le rôle d'une clé — Questions sur les clés primaires et étrangères (identifier, justifier, expliquer le rôle), parfois clés de chiffrement ; on évalue la compréhension des contraintes d'intégrité.
    gabarit : Indiquer la clé [primaire/étrangère] de la relation [nom] et préciser son rôle.
    exemple réel (autre notion) : « 14. Compléter la fonction cle qui permet de renvoyer la clé k d'un numéro de sécurité sociale en prenant pour paramètre le nombre n formé des 13 premiers chiffres du numéro de sécurité sociale. 1 def cle(n): 2 ... »
    détail du cours à évaluer (Modele relationnel) : « La cohérence entre les différentes tables d'une base de données est assurée par les clés étrangères : dans une table, la valeur d'un attribut qui est clé étrangère doit obligatoirement pouvoir être retrouvée dans la table dont cet attribut est clé primaire. »

Le champ id vaut « I-modele_relationnel ».