# Plan I-fonctions (inedit)

Notion : fonctions (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Recursivite > Recursivite]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 2 - Récursivité
> Objectifs :
> ▷ Écrire un programme récursif
> ▷ Analyser le fonctionnement d'un programme récursif.
> ▷ Connaître des exemples relevant de domaines variés utilisant la récursivité
> 1 Introduction
> La récursivité, à la fois en informatique et dans la vie courante, trouve son utilité dans la résolution
> de problèmes de façon élégante de problèmes complexes en les décomposant en cas de base et en sous-
> problèmes gérables.
> La récursivité trouve son application dans une variété de domaines informatiques, tels que la program-
> mation, la conception d'algorithmes, la modélisation de données et même dans la création de structures
> récursives comme les arbres et les listes chaînées.
> 2 Définition
> A retenir!
> La récursivité est une méthode de résolution de problèmes qui consiste à décomposer le problème
> en sous-problèmes identiques de plus en p
> [Programmation > Recursivite > Introduction]
> #Exercices
> 
>     Écrire une fonction récursive ```puissance``` qui prend en paramètres deux nombres ```x``` et ```n``` qui renvoie le nombre $x^n$.
> 
>     On rappelle que le PGCD (plus grand diviseur commun de deux nombres) vérifie la propriété suivante : si la division euclidienne de $a$ par $b$ s'écrit $a = b \times q + r$, alors $pgcd(a,b)=pgcd(b,r)$. 
> 
>     Cette propriété est à la base de l'algorithme d'Euclide
> 
>     Exemple : $pgcd(24,18)=pgcd(18,6)=pgcd(6,0)$, donc $pgcd(24,18)=6$
> 
>     Écrire une fonction récursive ```pgcd``` qui prend en paramètres deux nombres ```a``` et ```b``` et qui renvoie leur PGCD.
> 
>     La conjecture de Syracuse  (ou de Collatz) postule ceci :  
> 
>     *Prenons un nombre $n$ : si $n$ est pair, on le divise par 2, sinon on le multiplie par 3 puis on ajoute 1. On recommence cette opération tant que possible. Au bout d'un certain temps, on finira toujours par tomber

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C17 : Question directe « quelle est » — L'élève indique une valeur, une propriété ou un élément d'une structure. Réponse courte ; le groupe reste un peu hétérogène.
    gabarit : Quelle est la [valeur|propriété] de [objet] ?
    exemple réel (autre notion) : « 4. Le primeur souhaite connaître le poids de tout son stock. Quelle requête doit-il écrire ? »
    exemple réel (autre notion) : « 4. Quelle commande permet d'interrompre un processus dans un système d'exploitation de type UNIX ? a. stop b. interrupt c. end d. kill »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 7. Déterminer, en justifiant, la valeur maximale que peut rapporter une planche de 4 m. »

- slot 2 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 1. Sur le document réponse 1 de l'exercice 4, encadrer to us les sous-réseaux présents dans le réseau global sur le document réponse. »
    détail du cours à évaluer (Arbres) : « Cette fonction renvoie True si element est dans l’arbre et False sinon. »

Le champ id vaut « I-fonctions ».