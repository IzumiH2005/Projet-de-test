# Plan I-poo (inedit)

Notion : poo (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
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
> [Programmation > Programmation Orientee Objet > Exercices]
> **Q1.** Écrire une classe ```Eleve``` qui contiendra les attributs ```nom```, ```classe``` et ```note```.
>     
> 
>     **Q2.** Instancier trois élèves de cette classe.
>     
> 
>     **Q3.**  Écrire une fonction ```compare``` qui prend en paramètres deux élèves ```eleve1``` et ```eleve2``` qui renvoie le nom de l'élève ayant la meilleure note (on ne traitera pas à part le cas d'égalité).
> 
>         ```python
>         >>> riri = Eleve("Henri", "TG2", 12)
>         >>> fifi = Eleve("Philippe", "TG6", 15)
>         >>> loulou = Eleve("Louis", "TG1", 8)
>         >>> compare(riri, fifi)
>         'Philippe'
>         ```
> 
>     
>     Écrire une classe ```TriangleRect``` qui contiendra les attributs ```cote1```, ```cote2``` et ```hypotenuse```.
> 
>     La méthode constructeur ne prendra en paramètres que ```cote1``` et ```cote2```, l'attribut ```hypotenuse``` se calculera automatiquement.
> 
>         ```python
>         >>>

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C16 : Écrire une requête SQL — L'élève rédige une requête SQL répondant à un besoin formulé en langage naturel. On évalue sélection, jointures, filtres et tris.
    gabarit : Écrire une requête SQL permettant d'afficher [attributs] des [entités] [condition].
    exemple réel (autre notion) : « 1. Parmi les trois requêtes suivantes, écrites dans le langage SQL, laquelle renvoie les valeurs de tous les attributs des plats de la catégorie 'entrée' : R1 : SELECT nom, prix FROM Plat WHERE categorie = 'entrée'; R2 : SELECT * FROM Plat  »
    exemple réel (autre notion) : « c) Écrire une requête permettant de modiﬁer le tarif de location d'un nettoyeur à haute pression pour le passer à 15 € par jour au lieu de 20 € par jour. »
    support S8 : Phrases courtes isolées — Fragments brefs d'une phrase (hypothèse de scénario, consigne courte). Aucun matériau fourni ; groupe défini par la brièveté.
    exemple de support (autre notion) : « 3. Justifier que la boucle de la fonction précédente se termine. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « a. Proposer un schéma relationnel (sous forme de tableau) pour la table Statistique qui permette de stocker les informations relatives aux statistiques des joueuses dans la base de données, telles que présentées ci-dessus. Préciser la clé p »
    exemple réel (autre notion) : « 3. Écrire une requête SQL permettant de mettre à jour son état dans la base de données. »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « b) Indiquer ce que signifie le " mode ='r'" à la ligne 8. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 5. Donner le code de la fonction asc_desc. »
    exemple réel (autre notion) : « 9. Écrire un algorithme en pseudo-code de la fonction liste_stations. »
    support S5 : Besoin formulé pour requête SQL — Phrase décrivant en langage naturel l'information à extraire d'une base. L'élève la convertit en requête SQL.
    exemple de support (autre notion) : « 2. Expliquer pourquoi l'attribut habitat de la table papillon ne peut pas être une clé primaire. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 4. Donner la valeur associée à e1, e2 et e3 (si la chaine existe) »
    détail du cours à évaluer (Arbres) : « Si l'arbre est vide, on renvoie un nouvel objet Arbre contenant la clé. »

Le champ id vaut « I-poo ».