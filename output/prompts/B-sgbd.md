# Plan B-sgbd (banque)

Notion : sgbd (Bases de données) — banque de questions isolées
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
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier completer, fonction, recopier
    style réel : « 3. La figure 1 représente les trois premiers blocs d'une Blockchain. Expliquer
pourquoi la valeur de l'attribut bloc_precedent du bloc0 est None.
liste_transactions = [ »
- slot 2 | archétype=expliquer / explication / comprendre | Bloom=comprendre | formulations typiques : indiquer, expliquer, preciser, quel
    style réel : « 8. Parmi les propositions suivantes, indiquer celles qui font partie des rôles d'un
SGBD :
a) sécuriser les accès à la base de données ;
b) assurer l'alimentation électrique des serveurs ;
c) assurer la persistance des d »
- slot 3 | archétype=calcul_numerique / valeur / appliquer | Bloom=appliquer | formulations typiques : binaire, arbre, arbre binaire, calculer
    style réel : « 10. Écrire l'appel à la fonction calculer_solde permettant de calculer le solde
actuel de Alice »

Le champ id vaut « B-sgbd ».