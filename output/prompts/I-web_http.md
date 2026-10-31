# Plan I-web_http (inedit)

Notion : web_http (Architecture, OS et réseaux) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
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
> [Bases de données > Langage SQL > Exercices SQL interactifs]
> *Vous pourrez trouver de très nombreux exercices interactifs d'entraînement sur le site de Nicolas Reveret, à l'adresse https://nreveret.forge.apps.education.fr/exercices_bdd/*
> 
>     *Questions interactives à réaliser sur le site sqlzoo.net.*
> 
>     **Q1.** Travail sur SELECT, (base de données Nobel) :arrow_right: ici.
> 
>     
>         
> 
>     **Q2.** Travail sur SUM et COUNT, (base de données World) :arrow_right: ici. (jusqu'à la question 5.)
> 
>     
> 
>     **Q3.** Travail sur JOIN, (base de données Euro2012) :arrow_right: ici.
> 
>     Gestion d'un réseau d'agences de location de voitures.   
>     *D'après le travail de J. Le Coupanec (Académie de Rennes)*
> 
>     La base de données locations.db contient les tables ```Agences```,```Locations```, ```Vehicules```.
>     
> 
>     {!{ sqlide titre="**Requête :**"  base="T4_Bases_de_donnees/4.2_Langage_SQL/data/locations.db" }!}
> 
>         **Q1**. Visualisez toute la

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 11. Décrire ce qui garantit la terminaison de la fonction récursive shannon. »
    exemple réel (autre notion) : « d) Donner, en fonction de n, la complexité en temps de la fonction liste_segments. »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 8. Donner le code Python de la fonction sur_la_meme_ligne qui prend en paramètres un digramme et le carré de chiffrement créé par la fonction creer_carre, et qui renvoie True si les deux lettres du digramme sont sur la même ligne, ou False sinon.  Exemple (av »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « 2. On s'intéresse ici à la récupération d'informations issues de la base de données. »
    exemple réel (autre notion) : « 2. Donner les adresses des trois interfaces du routeur R5 permettant de transmettre ou de recevoir des données.  3. »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « f. Compléter la méthode de la classe Region ci-dessous à partir de la ligne 6.Code 1 def retire_couleur(self, couleur): 2 """ Region, str -> NoneType 3 Retire couleur du tableau des couleurs disponibles de la region self si la couleur est présente dans le tabe »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « 2. Recopier et compléter les lignes 8, 9 et 10 et compléter les pointillés avec le code manquant. »
    exemple réel (autre notion) : « 8. Compléter le script ci-dessous en recopiant les lignes 3, 7 et 9 sur votre copie : 1 from random import * 2 # créer les 104 cartes du jeu initial grâce à une liste par compréhension 3 jeu = [... for i in range (..., ...)] 4 # mélanger ce »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 5. Donner la hauteur de l'arbre de la Figure 3 et préciser dans le contexte de l'exercice ce qu'elle représente. On rappelle que dans le code ASCII, chaque symbole est codé sur un octet. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « a. Pourquoi cette instruction fonctionne-t-elle, con trairement à la précédente ?  Les fichiers et dossiers ont été effacés dans cet ordre : • fichier idee1.txt • dossier idees • fichier fond .png • fichier ico .png • dossier images • fichi »
    détail du cours à évaluer (Securisation) : « Problème :comment échanger cette clé entre le client et le serveur? »

Le champ id vaut « I-web_http ».