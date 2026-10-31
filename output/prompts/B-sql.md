# Plan B-sql (banque)

Notion : sql (Bases de données) — banque de questions isolées
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
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « c. Suite à un changement, l'horaire d'arrivée du train n°7869 est programmé à 08 h 11.
Mettre à jour la base de données en conséquence. »
- slot 2 | archétype=ecrire_sql / sql / créer | Bloom=créer | formulations typiques : ecrire requete, requete, requete sql, ecrire
    style réel : « 7. Écrire une requête permettant d'obtenir la liste sans doublon des noms de
société ayant réservé une salle de réunion.
EN_NOzUzMD2M0ODAczOT0UzMmTYxMj5A2MDEO2OTjQ3OVTYx »
- slot 3 | archétype=ecrire_sql / sql / créer | Bloom=créer | formulations typiques : ecrire requete, requete, requete sql, ecrire
    style réel : « 10. Écrire une requête SQL permettant d'afficher la date de début, la date de fin et
la valeur du polluant PM10 pour la station "Mazagran". »
- slot 4 | archétype=trace_execution / valeur / appliquer | Bloom=appliquer | formulations typiques : apres, apres execution, execution, renvoie
    style réel : « a. Qu'affiche le premier print ? »

Le champ id vaut « B-sql ».