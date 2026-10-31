# Plan I-sql (inedit)

Notion : sql (Bases de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Bases de données > Langage SQL > 2. Création et modification d'une base de données]
> _rappel_ : 
> 
> L'objectif est de créer la table suivante :
> 
> | id | Nom | Maths | Anglais | NSI |
> |:-----:|:-----:|:-------:|:----:|:----:|
> | 1 | Alice | 16 | 11 | 17 |
> | 2 | Bob  | 12 | 15 | 10 |
> | 3 | Charles | 9 | 11 | 18 |
> 
> #### 2.1 Exemple 15 
> 
> *La création d'une table n'est pas explicitement au programme de NSI. Personne ne sait vraiment pourquoi*
> 
>     - **Commande :** 
>     ```sql
>     CREATE TABLE Table_notes (
>             Id INTEGER PRIMARY KEY,
>             Nom TEXT,
>             Maths INTEGER,
>             Anglais INTEGER,
>             NSI INTEGER
>             );
>     ``` 
>     - **Remarque :**  
>     C'est l'utilisateur qui spécifie, éventuellement, quel attribut sera une clé primaire.
> 
>     - **Résultat :**  
>     Dans DB Browser, il faut avoir au préalable créé une nouvelle base de données.
> 
> #### 2.2 Exemple 16 
> 
>     - **Commande :** 
>     ```sql
>     INSERT INTO Table_notes 
>     VALUES (1,
> [Bases de données > SQL > SQL]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 9 - Le langage SQL
> Objectifs :
> ▷ Identifier les composants d'une requête.
> ▷ Savoir utiliser des requêtes d'interrogation et de mise à jour d'une base de données.
> ▷ Construire des requêtes d'interrogation à l'aide des clauses du langage SQL :SELECT, FROM, WHERE, JOIN.
> ▷ Construire des requêtes d'insertion et de mise à jour à l'aide de :UPDATE, INSERT, DELETE.
> 1 Introduction
> Dans le chapitre précédent sur le modèle relationnel, nous avons découvert la structure mathématique des bases
> de données. Maintenant que nous avons vu comment celles-ci sont organisées, nous allons interagir avec elles.
> Les SGBD jouent le rôle d'interface entre l'être humain et la base de données. Par l'intermédiaire de requêtes,
> l'utilisateur vaconsulter ou mettre à jourla base de données.
> Le langage utilisé pour communiquer avec le SGBD est lelangage SQL, (pour Struc

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C18 : Programmer sur un tableau d'entiers — Exercices pratiques où l'élève programme une fonction parcourant un tableau de nombres (recherche, tri, vérification) avec exemples ; on évalue l'algorithmique de base et le passage des tests.
    gabarit : Écrire une fonction [nom] qui prend en paramètre un tableau [tab] de [type] et qui renvoie [résultat]. Exemples : [assertions].
    exemple réel (autre notion) : « 1. On considère la fonction somme(n) qui reçoit en paramètre un entier n strictement positif et renvoie le résultat du calcul 1 +   +   + ⋯ +   . 1| def somme(n) : 2| total = 0 3| for i in range(n) : 4| total = total + 1/i 5| return to »
    exemple réel (autre notion) : « b. Écrire une fonction parcours_maladies(arb) qui n'affiche que les feuilles de l'arbre binaire non vide arb passé en argument, ce qui correspond aux maladies possiblement induites par l'arbre de décision. »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 3. Ecrire un programme qui : • demande de saisir la clé de chiffrement • crée un objet de classe CodeCesar • demande de saisir le texte à chiffrer • affiche le texte chiffré en appelant la méthode cryptage »

- slot 2 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C8 : Manipuler une base de données — Requêtes et modélisation sur une base relationnelle (supprimer, ajouter, interroger, proposer un schéma) ; on évalue la correspondance entre un besoin métier et les opérations SQL ou la structure de tables.
    gabarit : Donner la (les) requête(s) SQL permettant de [opération] dans la base de données [nom], [contrainte].
    exemple réel (autre notion) : « 2. À partir d'un entiern, on construit une liste dek entiers en utilisant l'image étudiée dans la »
    détail du cours à évaluer (Langage SQL) : « La base de données locations.db contient les tables Agences , Locations , Vehicules . »

Le champ id vaut « I-sql ».