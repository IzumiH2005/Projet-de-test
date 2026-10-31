# Plan I-poo (inedit)

Notion : poo (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Programmation objet > Programmation objet]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 3 - Programmation orientée objet
> Objectifs :
> ▷ Connaître le vocabulaire de la programmation objet : classes, attributs, méthodes, objets.
> ▷ Ecrire la définition d'une classe
> ▷ Accéder aux attributs et méthodes d'une classe.
> 1 Introduction
> Jusqu'à présent nous avons utilisé des objets dont le type est prédéfini :int, float, bool, str, list,
> tuple, dict. Sans le savoir, nous avons découvert les concepts de laprogrammation orientée objet
> ou POO. Ainsi, en classe de Première, nous avions déjà appris à utiliser des méthodes associées à ces
> types, comme :
> ma_liste.append(valeur)
> Comme de nombreux autres langages tels queJava ou C++, Python est un langage orienté objet .
> On peut donc dire que tout y estobjet. Une variable de typeint est en fait un objet de typeint donc
> construit à partir de la classeint. Idem pour lesfloat et str. Mais également
> [Programmation > Programmation Orientee Objet > 2.2 Création d'une classe]
> #### 2.2.1 (mauvaise) manière minimale
> Créons une classe «voiture». Il suffit d'écrire :
> 
> ```python
> class Voiture :
>     pass   #pass, car pour l'instant il n'y a rien dans la déclaration de la classe (et c'est mal)
> ```
> 
> La classe ```Voiture``` est créée.  
> Notez que par convention, le nom d'une classe commence toujours par une majuscule.  
> Pour créer une instance de cette classe, on écrit :
> 
> ```python
> >>> titine = Voiture()
> ```
> 
> ```titine``` est un objet, instance de la classe ```Voiture```.
> 
> ```python
> >>> type(titine)
> __main__.Voiture
> ```
> 
> On peut alors donner des attributs à cette instance :
> 
> ```python
> >>> titine.annee = 2018
> >>> titine.couleur = "verte"
> >>> titine.vitesse_max = 162
> ```
> 
> Mais arrêtons-là cette mauvaise méthode. Si on désire créer une classe «voiture», c'est pour créer un concept générique de voiture et d'en spécifier des caractéristiques communes  : l'année, la couleur

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C7 : Dénombrer une quantité — L'élève calcule ou programme un comptage (machines d'un réseau, sauts, appels récursifs, occurrences) ; on évalue la maîtrise de ce qu'on compte et des bornes du comptage.
    gabarit : Déterminer le nombre de [éléments] [dans/lors de] [situation], ou écrire une fonction qui renvoie ce nombre.
    exemple réel (autre notion) : « c. Donner le nombre maximal de machines que l'on peut connecter sur ce réseau. »
    exemple réel (autre notion) : « b. Indiquer le nombre maximum de machines que l'on pourra connecter sur ce réseau F. »
    support S6 : Texte avec parenthèses explicatives — Support riche en parenthèses (signatures, précisions, sous-questions (a)(b)) ; l'élève doit tenir compte des précisions et des paramètres annoncés.
    exemple de support (autre notion) : « 11. Recopier et compléter le schéma du réseau (Figure. 1) en ajoutant le routeur R7 et le réseau local N5. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C17 : Identifier le rôle d'une clé — Questions sur les clés primaires et étrangères (identifier, justifier, expliquer le rôle), parfois clés de chiffrement ; on évalue la compréhension des contraintes d'intégrité.
    gabarit : Indiquer la clé [primaire/étrangère] de la relation [nom] et préciser son rôle.
    exemple réel (autre notion) : « 7. Expliquer le rôle de l'attribut id_album de la table Chanson. »
    exemple réel (autre notion) : « 1. Expliquer le choix de num_dossard comme clé primaire pour la relation coureur. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « b. Donner une commande en langage SQL permettant d'obtenir l'ensemble des adresses IP ayant interrogé le site, sans doublon. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C11 : Traiter des chaînes de caractères — Questions de programmation ou d'analyse portant sur des chaînes (parcours, inversion, validation, exemple qui fait échouer un test) ; on évalue la manipulation de caractères et d'indices.
    gabarit : Écrire une fonction [nom] qui prend en paramètre une chaîne de caractères [s] et renvoie [résultat]. Exemple : [nom]([entrée]) renvoie [sortie].
    exemple réel (autre notion) : « b. Écrire une requête SQL donnant le numéro de télépho ne d'une cliente s'appelant "Grace Hopper".  3. Dans cette base de données, les dates DateArr , DateDep sont au format chaîne de caractères 'aaaa-mm-jj' . Par exemple, la chaîne '2020-1 »
    exemple réel (autre notion) : « 1. Recopier et compléter la ligne 4 de la fonction est_operateur. On souhaite maintenant écrire une fonction est_nombre qui prend en paramètre une chaîne de caractères s et qui renvoie si s correspond à un nombre (positif ou négatif). Par e »
    support S7 : Consigne brève sans support — Question courte et autonome, sans matériau joint notable ; l'élève répond à partir de ses connaissances ou du contexte de l'exercice.
    exemple de support (autre notion) : « 4. a. Vérifier ces inégalités sur l'arbre binaire de la question 1.a. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C6 : Établir ou lire une table de routage — Majoritairement réseau : dresser, compléter ou exploiter une table de routage selon un protocole (RIP/OSPF), ou identifier un chemin ; on évalue l'application d'un protocole à une topologie.
    gabarit : Donner la [table/chemin] [de l'élément] selon [protocole/règle], après [événement].
    exemple réel (autre notion) : « 14. Recopier et compléter , à l'aide des fonctions rechercher_chemins et chemin_valeur, les lignes de code suivantes qui permettent d'obtenir tous les chemins non prolongeables du jeu à 9 entiers représentés par la liste des valeurs de leur »
    détail du cours à évaluer (Arbres) : « Écrire la méthode hauteur de la classe Arbre qui renvoie la hauteur de l’arbre. »

Le champ id vaut « I-poo ».