# Plan I-sql (inedit)

Notion : sql (Bases de données) — questions JAMAIS POSÉES aux annales

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
> [Bases de données > Langage SQL > 1.2. Opérations sur les données : sélection avec agrégation]
> Les requêtes effectuées jusqu'ici ont juste sélectionné des données grâce à différents filtres : aucune action à partir de ces données n'a été effectuée.  
> Nous allons maintenant effectuer des opérations à partir des données sélectionnées. On appelle ces opérations des **opérations d'agrégation**.
> 
> #### 1.2.1 Exemple 7 
> 
>     - **Commande :** 
>     ```sql
>     SELECT COUNT(*) AS total 
>     FROM livre
>     WHERE titre LIKE "%Astérix%";
>     ``` 
>     - **Traduction :** 
> 
>     On veut compter le nombre d'enregistrements de la tables livres comportant le mot "Astérix". Le résultat sera le seul élément d'une colonne nommée «total».
> 
>     - **Résultat :**   
> 
>     
> 
> #### 1.2.2 Exemple 8 
> 
>     - **Commande :** 
>     ```sql
>     SELECT SUM(annee) AS somme
>     FROM livre
>     WHERE titre LIKE "%Astérix%";
>     ``` 
>     - **Traduction :** 
> 
>     On veut additionner les années des livres de la tables livres com

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C17 : Question directe « quelle est » — L'élève indique une valeur, une propriété ou un élément d'une structure. Réponse courte ; le groupe reste un peu hétérogène.
    gabarit : Quelle est la [valeur|propriété] de [objet] ?
    exemple réel (autre notion) : « 2. Quelle abréviation désigne l'identifiant d'un processus dans un système d'exploitation de type UNIX ? a. PIX b. SIG »
    exemple réel (autre notion) : « 1. a. Quelle est la solution du problème si les éléments du tableau sont tous positifs ? »
    support S12 : Requêtes et syntaxe SQL — Code SQL fourni (SELECT, FROM, WHERE, UPDATE) ou rappel de syntaxe. L'élève lit, exécute mentalement ou s'en inspire.
    exemple de support (autre notion) : « 6. sinon si …………………… »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C18 : Tracer une boucle Python donnée — L'élève suit l'exécution d'un code avec boucles for/range pour en déduire une valeur ou un affichage. On évalue la trace d'exécution.
    gabarit : Déterminer la valeur de [variable] à l'issue des instructions suivantes : [code].
    exemple réel (autre notion) : « 9. if not voisin in parent: 10 parent[voisin] = mot 11. file_voisins.enfiler(voisin) 12. return parent On donne les résultats ci-dessous qui correspondent au graphe de la partie A :  >>> renvoie_voisins('mars') ['gars', 'mors'] >>> renvoie_ »
    exemple réel (autre notion) : « 3. Ceconstructeurautomobilepossèdesixsitesdeproductionquiéchangentdesdocumentsentre eux.Lessitesdeproductionsontreliésentreeuxparsixrouteurs A, B , C, D, E et F OndonnecidessouslestablesderoutagedesrouteursAàFobtenusavecleprotocoleRIP: Rout »
    support S7 : Chaînes et dictionnaires entre guillemets — Matériau contenant des chaînes entre guillemets : dictionnaires Python, propositions, noms. L'élève exploite ces littéraux pour dessiner, évaluer ou coder.
    exemple de support (autre notion) : « 9. Donner la liste du cercle d'amis de Lou. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « a. Quel algorithme de tri est ici implémenté ?  le tri fusion  le tri par insertion  le tri par sélection  le tri rapide »
    exemple réel (autre notion) : « 11. Indiquer dans quel ordre apparaitraient les mots -clés avec un parcours en profondeur infixe sur l'ABR illustré. »
    support S15 : Sous-questions lettrées a) b) — Énoncés découpés en items a), b), c) ou en options lettrées. L'élève traite chaque sous-question ou choisit une option.
    exemple de support (autre notion) : « b) Indiquer la commande qui a lancé le premier processus de firefox. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « b. Proposer un schéma relationnel qui permet d 'éviter ce(s) problème(s). On pourra donner la réponse sous la forme : Schéma relationnel : tarifs(premier attribut, deuxième attribut,…) prestations(premier attribut,…) clients(premier attribu »
    détail du cours à évaluer (Langage SQL) : « On considère ci-dessous le schéma de la base de données du stock d'un supermarché : »

Le champ id vaut « I-sql ».