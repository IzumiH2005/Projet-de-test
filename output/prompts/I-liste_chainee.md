# Plan I-liste_chainee (inedit)

Notion : liste_chainee (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Listes Piles Files > 2.3 Exemple d'implémentation minimale d'une liste chaînée]
> ```python linenums='1'
>     class Cellule :
>         def __init__(self, contenu, suivante):
>             self.contenu = contenu
>             self.suivante = suivante
>     ```
> 
> Cette implémentation rudimentaire permet bien la création d'une liste :
> 
> ```python
> >>> lst = Cellule(3, Cellule(5, Cellule(1,None)))
> ```
> 
> La liste créée est donc :   
> 
> Mais plus précisément, on a :
> 
>     Retrouvez comment accéder aux éléments 3, 5 et 1.
> 
>     
> 
> On pourra remarquer que l'interface proposée à l'utilisateur n'est pas des plus pratiques...
> [Structures de données > Les listes > Les listes]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 5 - Les listes
> Objectifs :
> ▷ Distinguer des structures par le jeu des méthodes qui les caractérisent.
> ▷ Choisir une structure de données adaptée à la situation à modéliser.
> ▷ Distinguer la recherche d'une valeur dans une liste et dans un dictionnaire.
> 1 Introduction
> Historique
> Le langage de programmationLisp (inventé parJohn McCarthy en 1958) a été un des premiers langages
> de programmation à introduire cette notion de liste (Lisp signifie list processing).
> Lisp qui fait partie de la plus ancienne famille de langages de programmation à la fois impératifs et
> fonctionnels, est devenu dans les années 1970-80 le langage de choix pour la recherche en intelligence
> artificielle. Ils sont aujourd'hui utilisés dans de nombreux domaines, de la programmation Web à la
> finance.
> Python abuse du terme liste qu'il utilise pour ce qui sont destableaux dyna

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C22 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes précisément numérotées d'une fonction à trous ; on évalue la compréhension de la logique locale du code et le respect de la spécification.
    gabarit : Recopier et compléter les lignes [n1] à [n2] de la fonction [nom] afin qu'elle [comportement].
    exemple réel (autre notion) : « 2. Recopier et compléter les lignes 6, 8, 10 et 11 de la fonction nb_points. »
    exemple réel (autre notion) : « 7. Recopier et compléter les lignes 4, 5, 6 et 9 de la méthode melanger donnée ci-dessous.  1 def melanger(self, n):  2 precedent = None  3 i = 0  4 while ... :  5 possibilites = ...  6 choix = ...  7 if choix != precedent :  8 self.jouer(c »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 1. Déchiffrer le message (6,2) (3,6) (3,5) (2,2) en utilisant la grille ci-dessus. Une façon simple de construire un tableau consiste à choisir un mot qu'on appellera clé, à écrire cette clé dans le tableau puis à compléter avec les autres lettres dans l'ordre »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : milieu d'exercice
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 3) Indiquer l'adresse IP de la passerelle donnant au serveur web l'accès à Internet.  Réseau services 192.168.254.2 192.168.254.1 Réseau local 192.168.0.254 Figure 3 192.168.254.1 192.168.254.2 »
    exemple réel (autre notion) : « a. Lors de l'exécution de maxi([2, 4, 9, 1]) une erreur est déclenchée. Identifier et corriger le problème. »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 5. Recopier et compléter les lignes manquantes pour définir le tableau t_routage pour qu'il modélise complètement la table de routage du routeur R1 (vous écrirez les numéros de lignes complétées).  1 t_routage = [ ((192, 168, 1, 0, 24), 'G0', 0),  2 ...,  3 .. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C6 : Établir ou lire une table de routage — Majoritairement réseau : dresser, compléter ou exploiter une table de routage selon un protocole (RIP/OSPF), ou identifier un chemin ; on évalue l'application d'un protocole à une topologie.
    gabarit : Donner la [table/chemin] [de l'élément] selon [protocole/règle], après [événement].
    exemple réel (autre notion) : « 9. Écrire alors une fonction table_routage(graphe, routeur) qui renvoie la table de routage du routeur passé en paramètre sous la forme d'un dictionnaire associant à chaque routeur destination la passerelle correspondante. On pourra utilise »
    exemple réel (autre notion) : « a. Donner la liste des routeurs avec lesquels le routeur A est directement relié. »
    support S0 : Énoncé en prose avec numéros — Support textuel ordinaire mêlant prose et nombres (routeurs, adresses, tailles) ; l'élève travaille à partir d'une mise en situation décrite, sans matériau structuré dominant.
    exemple de support (autre notion) : « 6. Donner une requête qui modifie en conséquence le prix de cet appartement. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C20 : Énoncés de mise en situation — Mélange d'énoncés introductifs et de questions descriptives (arbres, parité, interfaces) ; groupe défini par des tournures génériques plutôt que par un geste.
    gabarit : On considère [situation]. Indiquer [éléments] qui [propriété].
    exemple réel (autre notion) : « 2. La fonction logique OU EXCLUSIF, appelée XOR et représentée par le symbole ⊕, fournit une sortie égale à 1 si l'une ou l'autre des deux entrées vaut 1 mais pas les deux.  On donne ci -contre la table de vérité de la fonction XOR.  Si on  »
    détail du cours à évaluer (Les files) : « Liste chaînée :Insérez successivement les valeurs 10, 20 et 30 en queue de liste. »

Le champ id vaut « I-liste_chainee ».