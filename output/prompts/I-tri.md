# Plan I-tri (inedit)

Notion : tri (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Diviser pour regner > 4.2 La fusion]
> #### 4.2.1 Principe
> 
> L'idée du tri fusion est le découpage de la liste originale en une multitude de listes ne contenant qu'un seul élément. Ces listes élémentaires seront ensuite interclassées avec la fonction précédente.
> 
> **Principe de l'algorithme du tri fusion :**
> 
> - pour trier une liste, on interclasse les deux moitiés de cette liste, précédémment elles-mêmes triées par le tri fusion.
> - si une liste à trier est réduite à un élément, elle est déjà triée. 
> 
> #### 4.2.2 Implémentation
> 
> La grande force de ce tri va être qu'il se programme simplement de manière **récursive**, en appelant à chaque étape la même fonction mais avec une taille de liste divisée par deux, ce qui justifie son classement parmi les algorithmes utilisants «diviser pour régner».
> 
> {#
> 
>   
>     ```python
>     def interclassement(lst1, lst2):
>         ...
> 
>     def tri_fusion(lst):
>         ...
>     ```
> #}
> 
>     
>     ```python
> [Algorithmique > Diviser pour regner > 4.3 Complexité]
> La division par 2 de la taille de la liste pourrait nous amener à penser que le tri fusion est de complexité logarithmique, comme l'algorithme de dichotomie. Il n'en est rien.
> 
> En effet, l'instruction finale ```interclassement(tri_fusion(lst[:m]), tri_fusion(lst[m:]))``` lance **deux** appels à la fonction ```tri_fusion``` (avec certes des données d'entrée deux fois plus petites).
> 
> On peut montrer que :
> 
>     L'algorithme de tri fusion est en $O(n \log n)$.
> 
>     On dit qu'il est **quasi-linéaire**. (ou *linéarithmique*)
> 
> Une complexité quasi-linéaire (en $O(n \log n)$) se situe «entre» une complexité linéaire (en $O(n)$) et une complexité quadratique (en $O(n^2)$). Mais elle est plus proche de la complexité linéaire.
> 
> Pour finir, une jolie animation permettant de comparer les tris :
> 
> Issue de ce site

Questions à rédiger (points = 1 par défaut) :

- slot 1 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C8 : Manipuler une base de données — Requêtes et modélisation sur une base relationnelle (supprimer, ajouter, interroger, proposer un schéma) ; on évalue la correspondance entre un besoin métier et les opérations SQL ou la structure de tables.
    gabarit : Donner la (les) requête(s) SQL permettant de [opération] dans la base de données [nom], [contrainte].
    exemple réel (autre notion) : « b) Indiquer le type de parcours réalisé par l'algorithme VISITE.  EXERCICE 3 Cet exercice porte sur un schéma relationnel de bases de données et des requêtes SQL.  Pour élaborer un jeu vidéo sur le thème des chevaliers de la table ronde, on »
    détail du cours à évaluer (Langage SQL) : « À partir de ce point de départ et d'une base de données dont le diagramme est donné ci-dessous, il s'agit de trouver le meurtrier. »

Le champ id vaut « I-tri ».