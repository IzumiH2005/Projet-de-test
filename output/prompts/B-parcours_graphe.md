# Plan B-parcours_graphe (banque)

Notion : parcours_graphe (Algorithmique) — banque de questions isolées
Extraits du cours :
> [Algorithmique > Algo parcours graphes > Algo parcours graphes]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 21 - Parcours de graphes
> Objectifs :
> ▷ Implémenter en Python des algorithmes de parcours de graphes et de recherche de chemins dans un graphe.
> ▷ Utiliser ces fonctions Python pour résoudre un problème utilisant des graphes (navigation GPS, laby-
> rinthes, mots voisins, ...,etc.)
> 1 Introduction
> Un des premiers algorithmes que l'on doit savoir utiliser sur un graphe est celui de son parcours.
> Parcourir un graphe , c'est visiter ses différents sommets, afin de pouvoir opérer une action tour à tour sur
> eux. Tous comme pour les arbres, il est possible de réaliser deux types de parcours d'un arbre :
> — le parcours en largeur : Breadth First Search
> — le parcours en profondeur : Depth-First Search
> Cependant, contrairement aux arbres :
> — il n'y a pas de racine, donc on doit choisir à partir de quel noeud on part : lenoeud source.
> — il peut y avoir u
> [Structures de données > Graphes > 6. Annexe : et pourquoi pas en DFS ?]
> Les parcours BFS et DFS ont tous deux la propriété de parcourir **la totalité** du graphe (ils sont même conçus pour cela). Cela a permis au parcours BFS de nous fournir une solution au labyrinthe (dont on a démontré qu'elle était la plus courte).
> 
> Que penser de la solution qui sera donnée par le DFS ?
> 
> #### 6.1 Dans un labyrinthe parfait
> 
> Voici un code où la solution est d'abord recherchée par BFS (cases explorées en bleu clair, chemin trouvé marqué en bleu), puis en DFS (cases explorées en rose, chemin trouvé marqué en rouge).
> 
> anim_laby_DFSvsBFS_laby_parfait.py :arrow_down:
> 
> Que remarquez-vous ???
> 
> #### 6.2 Dans un labyrinthe non parfait
> 
> Changeons de code pour un labyrinthe *dégénéré* :
> 
> anim_laby_DFSvsBFS_laby_degenere.py :arrow_down:
> 
> Que remarquez-vous ???
> 
>     Notre labyrinthe conçu de manière aléatoire possède une propriété remarquable (due à son algorithme de construction) : ch
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « 15. Écrire le code de la fonction extraire_plus_longs_chemins qui prend en
paramètre une liste de chemins L_chemins et qui renvoie la liste des chemins
de L de longueur maximale. »
- slot 2 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 2. Donner la liste des six chemins possibles que peut emprunter ce paquet. »
- slot 3 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 1. Déterminer la taille et la hauteur de l'arbre donné en exemple en introduction (arbre de
décision en présence d'une jaunisse). »
- slot 4 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier completer, fonction, recopier
    style réel : « 9. Écrire la liste des sommets, dans l'ordre de leur visite, lors du parcours en
largeur du graphe du réseau routier de la figure 2 depuis le sommet 'V3'.
En supposant que toutes les arêtes ont le même poids, la fonction »

Le champ id vaut « B-parcours_graphe ».