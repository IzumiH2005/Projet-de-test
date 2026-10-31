# Plan B-parcours_arbre (banque)

Notion : parcours_arbre (Algorithmique) — banque de questions isolées
Extraits du cours :
> [Structures de données > Arbres > 2.1 Parcours en largeur d'abord (BFS)]
> *BFS : Breadth First Search*
>  
>     Le parcours en largeur d'abord est un parcours étage par étage (de haut en bas) et de gauche à droite.
> 
> L'ordre des lettres parcourues est donc T-Y-O-P-H-N.
> 
> Les trois parcours que nous allons voir maintenant sont des parcours en **profondeur d'abord**, ou **DFS** (*Depth First Search*). Ce qui signifie qu'un des deux sous-arbres sera totalement parcouru avant que l'exploration du deuxième ne commence.
> [Structures de données > Arbres > 2.5 Comment ne pas se mélanger entre le pré / in / post fixe ?]
> - *pré* veut dire *avant*
> - *in* veut dire *au milieu*
> - *post* veut dire *après*
> 
> Ces trois mots-clés parlent de la place du **père** par rapport à ses fils. 
> Ensuite, il faut toujours se souvenir qu'on traite le fils gauche avant le fils droit.
> 
> - préfixe : le père doit être le premier par rapport à ses fils.
> - infixe : le père doit être entre son fils gauche (traité en premier) et son fils droit.
> - postfixe : le père ne doit être traité que quand ses deux fils (gauche d'abord, droite ensuite) l'ont été.
> 
> Un parcours préfixe commencera toujours par la racine, alors qu'un parcours postfixe finira toujours par la racine. Dans un parcours infixe, la racine sera «au milieu» (pas nécessairement parfaitement).
> 
>         Donner le rendu de chaque parcours :
> 
>         1. Parcours en largeur 
>         2. Parcours préfixe
>         3. Parcours infixe
>         4. Parcours postfixe
> 
>         largeur : 1 
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 2. On rappelle qu'un parcours infixe depuis un nœud consiste, dans l'ordre, à faire un parcours
infixe sur le sous arbre-gauche, afficher le nœ ud puis faire un parcours infixe sur le sous-arbre
droit. »
- slot 2 | archétype=calcul_numerique / valeur / appliquer | Bloom=appliquer | formulations typiques : binaire, arbre, arbre binaire, calculer
    style réel : « 2. On donne l'arbre binaire suivant :

Indiquer, parmi les quatre différents parcours d'arbre ci-dessous celui qui permet d'obtenir
la succession des symboles correspondant à la notation NPI suivante :
20 11 3 + 5 2 + / »
- slot 3 | archétype=justifier_choix / explication / analyser | Bloom=analyser | formulations typiques : expliquer, pourquoi, expliquer pourquoi, quoi
    style réel : « 6. Expliquer pourquoi il est pertinent d'utiliser un parcours en largeur plutôt qu'un
parcours en profondeur pour réaliser l'exploration permettant d'obtenir une
chaine la plus courte possible. »

Le champ id vaut « B-parcours_arbre ».