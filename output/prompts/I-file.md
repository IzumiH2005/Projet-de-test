# Plan I-file (inedit)

Notion : file (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Listes Piles Files > 4.1 Utilisation d'une interface de file]
> On considère l'enchaînement d'opérations ci-dessous. Écrire à chaque étape l'état de la file ```f``` et la valeur éventuellement renvoyée.
>     Par convention, on enfilera **à gauche** et on défilera **à droite**.
>     ```python
>     1. f = File()
>     2. f.enfile(3) 
>     3. f.enfile(5)
>     4. f.est_vide()
>     5. f.enfile(1) 
>     6. f.defile() 
>     7. f.defile()
>     8. f.enfile(9) 
>     9. f.defile() 
>     10. f.defile()
>     11. f.est_vide() 
>     ```
> [Structures de données > Arbres > 4.6 Parcours en largeur]
> Le parcours en largeur (BFS) est le plus simple à faire visuellement : mais il est plus difficile à coder que les parcours préfixe, infixe, postfixe.  
> Il est nécessaire d'utiliser une **file**  :
> 
> - On place l'arbre dans la file.
> - Tant que la file n'est pas vide, on procède comme suit :
>     - On défile, donc on récupère l'arbre situé en haut de la file.  
>     - Si cet arbre n'est pas vide :
>         - On garde son étiquette.
>         - On enfile son sous-arbre gauche, puis son sous-arbre droit.
> 
> On importera l'objet ```Queue()``` du module ```queue``` de Python, qui permet de  :
> 
> - créer une file vide avec ```file = Queue()```
> - défiler un élément par ```file.get()```
> - enfiler l'élément ```a``` par ```file.put(a)```
> - savoir si la file est vide par le booléen ```file.empty()```
> 
> ```python

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C8 : Manipuler une base de données — Requêtes et modélisation sur une base relationnelle (supprimer, ajouter, interroger, proposer un schéma) ; on évalue la correspondance entre un besoin métier et les opérations SQL ou la structure de tables.
    gabarit : Donner la (les) requête(s) SQL permettant de [opération] dans la base de données [nom], [contrainte].
    exemple réel (autre notion) : « 4. On dispose des fonctions :  empiler(p,elt) qui empile l'élément elt dans la pile p,  depiler(p) qui renvoie le sommet de la pile p si p n'est pas vide et le supprime,  pile_vide(p) qui renvoie True si la pile p est vide, False si la p »
    exemple réel (autre notion) : « 2. Écrire, dans le langage SQL, des requêtes d'interrogation sur la base de données restaurant permettant de réaliser les tâches suivantes : a. Afficher les noms et les avis des clients ayant effectué une réservation pour la date du '2021-0 »
    support S6 : Texte avec parenthèses explicatives — Support riche en parenthèses (signatures, précisions, sous-questions (a)(b)) ; l'élève doit tenir compte des précisions et des paramètres annoncés.
    exemple de support (autre notion) : « a) Internet b) VGA c) Ethernet d) HDMI  5) On souhaite déterminer le parcours minimisant le coût total des liaisons traversées. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C24 : Compléter une fonction à trous — L'élève recopie et complète une fonction ou une table entière (parfois à partir d'une ligne donnée) ; on évalue l'achèvement d'un code partiellement fourni.
    gabarit : Recopier et compléter la fonction [nom] (à partir de la ligne [n]) qui [comportement].
    exemple réel (autre notion) : « 1. Recopier et compléter le code de la ligne 28 afin d'instancier la balise portant le numéro 12. »
    exemple réel (autre notion) : « 2. Donner la plus petite valeur de cible que la ligne [6,4,5,8,2] peut atteindre. Donner aussi la plus grande valeur de cible que la ligne peut atteindre. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 4. Recopier et compléter les lignes 10 à 12 de la méthode soutenir, en respectant sa documentation. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C22 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes précisément numérotées d'une fonction à trous ; on évalue la compréhension de la logique locale du code et le respect de la spécification.
    gabarit : Recopier et compléter les lignes [n1] à [n2] de la fonction [nom] afin qu'elle [comportement].
    exemple réel (autre notion) : « 2. Les lignes 11 et 12 de cette description du graphe ne sont pas complètes. Recopier et compléter le code des lignes 11 et 12. »
    exemple réel (autre notion) : « 12. Recopier et compléter les lignes 4, 6 et 7 du code de la fonction precede. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 12. Recopier et compléter la fonction plus_court donnée ci-dessous. La fonction plus_court prend pour paramètres un graphe G, un sommet de départ depart et un sommet d'arrivée arrivee ; elle renvoie un des chemins les plus courts sous la forme d'une liste de s »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C20 : Énoncés de mise en situation — Mélange d'énoncés introductifs et de questions descriptives (arbres, parité, interfaces) ; groupe défini par des tournures génériques plutôt que par un geste.
    gabarit : On considère [situation]. Indiquer [éléments] qui [propriété].
    exemple réel (autre notion) : « 2. Donner les différents états possibles d'un processus. »
    détail du cours à évaluer (Listes Piles Files) : « Pour être utilisée, une interface de file doit proposer a minima : »

Le champ id vaut « I-file ».