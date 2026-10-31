# Plan I-sgbd (inedit)

Notion : sgbd (Bases de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Architecture, OS et réseaux > Gestion des processus > Introduction]
> **Partie A**
> 
>     Cette partie est un questionnaire à choix multiples (QCM).
>     Pour chacune des questions, une seule des quatre réponses est exacte.
> 
>     1. Parmi les commandes ci-dessous, laquelle permet d’afficher les processus en cours
>     d’exécution ?
>         - a. ```dir```
>         - b. ```ps``` 
>         - c. ```man``` 
>         - d.   ```ls```
>     2. Quelle abréviation désigne l’identifiant d’un processus dans un système d’exploitation de type UNIX ?
>         - a. PIX
>         - b. SIG 
>         - c. PID 
>         - d. SID
>     3. Comment s'appelle la gestion du partage de processeur entre les différents processus ?
>         - a. L'interblocage
>         - b. L'ordonnancement
>         - c. La planification
>         - d. La priorisation
>     4. Quelle commande permet d’interrompre un processus dans un système d’exploitation de type
>     UNIX ?
>         - a. ```stop```
>         - b. ```interrupt`
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

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « b. Indiquer l'adresse IP (Internet Protocol) de la passerelle par défaut du téléphone. »
    exemple réel (autre notion) : « a. Donner la clé primaire de la relation matchs. »
    support S10 : Prose riche en virgules — Phrases longues avec énumérations par virgules ou listes de choix. Artefact de ponctuation, contenus variés.
    exemple de support (autre notion) : « b. Modifier l'ordonnancement des processus pour, qu'à la fin, la valeur de la variable compteur soit égale à 98. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 1. Convertir les adresses suivantes en binaire sur 32 bits : – Adresse IP : 172.16.32.15 – Masque de sous-réseau : 255.255.240.0  Donner le résultat sous la forme :  Adresse IP : XXXXXXXX.XXXXXXXX.XXXXXXXX.XXXXXXXX  Masque : XXXXXXXX.XXXXXX »
    exemple réel (autre notion) : « 6. Compléter la méthode de la classe Region ci-dessous à partir de la ligne 6 :  1 2 3  4 5 6 def est_coloriee(self):  '''  Renvoie True si une couleur a été attribuée à cette région et False sinon.  : return (bool)  '''  ... »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 2. Écrire et expliquer ce que renvoie l'appel de la fonction ci-dessous:  nettoyage_datetime ('2024-06-27T23:36:01.000000Z') Tous les enregistrements de données de plusieurs radiosondes sont stockés dans la variable frames de type list dont un extrait est donn »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C11 : Analyser une ligne de code précise — L'élève explique ou corrige le rôle d'une ligne désignée dans un programme fourni. On évalue la lecture fine du code.
    gabarit : Expliquer le rôle de la ligne [n] de la fonction [nom].
    exemple réel (autre notion) : « 11. Sachant que dans la fonction mystere, la ligne 24 peut être remplacée par une ou plusieurs instructions, donner ce qu'il faut écrire pour que, lorsque c'est possible, ordre_realisation renvoie effectivement un ordre de réalisation des t »
    exemple réel (autre notion) : « 3. Recopier et compléter la ligne 4 du code de cette fonction creer_carre, en utilisant les opérateurs % (reste de la division entière) et // (division entière). »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 10. Recopier sur la copie et compléter les lignes 19 et 20 du code de la méthode adresse_suivante de la classe IPv4 , donné ci -dessous. La m éthode doit correspondre au docstring.  1 def adresse_suivante(self, adresse_max:str)->str:  2 """  3 Détermine l'adre »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « 1. Donner la structure de données de la variable contacts_fictifs. EN_NOjczNT7QzNjAc0ND7UzMsTYxMj0A2NTAAwMDdAxNMjcx »
    détail du cours à évaluer (Base de donnees relationnelles) : « La plupart desSGBD-R (R de relationnelle) utilisent le langageSQL, Structured Query Language. »

Le champ id vaut « I-sgbd ».