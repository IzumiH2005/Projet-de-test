# Plan I-arbre_binaire (inedit)

Notion : arbre_binaire (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Arbres > Introduction]
> Exercice 2 du sujet Nouvelle-Calédonie J2 2022  
> 
>     *2020, sujet 0*
> 
>     **Question  1**
> 
>     Déterminer la taille et la hauteur de l’arbre binaire suivant :
>     
> 
>     
> 
>     **Question 2**  
> 
>     On décide de numéroter en binaire les nœuds d’un arbre binaire de la façon suivante :  
> 
>     - la racine correspond à 1 ;
>     - la numérotation pour un fils gauche s’obtient en ajoutant le chiffre 0 à droite au numéro de son
>     père ;
>     - la numérotation pour un fils droit s’obtient en ajoutant le chiffre 1 à droite au numéro de son
>     père ;  
> 
>     Par exemple, dans l’arbre ci-dessous, on a utilisé ce procédé pour numéroter les nœuds A, B, C, E et
>     F .
> 
>     
> 
>     **a**. Dans l’exemple précédent, quel est le numéro en binaire associé au nœud G ?
>     
>     **b**. Quel est le nœud dont le numéro en binaire vaut 13 en décimal ?
>     
>     **c**. En notant $h$ la hauteur de l’arbre, sur combie
> [Structures de données > Arbres > 5. Arbres binaires de recherche (ABR)]
> Un **arbre binaire de recherche** est un arbre binaire dont les valeurs des nœuds (valeurs qu'on appelle étiquettes, ou clés) vérifient la propriété suivante :
> 
>     - l'étiquette d'un nœud est **supérieure ou égale** à celle de **chaque** nœud de son **sous-arbre gauche**.
>     - l'étiquette d'un nœud est **strictement inférieure** à celle du **chaque** nœud de son **sous-arbre droit**.
> 
> À noter que l'arbre 3 (qui est bien un ABR) est appelé **arbre filiforme**. 
> 
> L'arbre 5 n'est pas un ABR à cause de la feuille 9, qui fait partie du sous-arbre gauche de 3 sans lui être inférieure.
> 
> **Remarque :** on pourrait aussi définir un ABR comme un arbre dont le parcours infixe est une suite croissante.

Questions à rédiger (points = 1 par défaut) :

- slot 1 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C7 : Dénombrer une quantité — L'élève calcule ou programme un comptage (machines d'un réseau, sauts, appels récursifs, occurrences) ; on évalue la maîtrise de ce qu'on compte et des bornes du comptage.
    gabarit : Déterminer le nombre de [éléments] [dans/lors de] [situation], ou écrire une fonction qui renvoie ce nombre.
    exemple réel (autre notion) : « b. Justifier le fait qu'un appel de la forme A(n) avec n un nombre entier positif inférieur à 50, termine toujours. »
    détail du cours à évaluer (Arbres) : « On décide de représenter un arbre binaire complet par un tableau de taille n + 1, où n est la taille de l’arbre, de la façon suivante : »

Le champ id vaut « I-arbre_binaire ».