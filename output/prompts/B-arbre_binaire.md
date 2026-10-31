# Plan B-arbre_binaire (banque)

Notion : arbre_binaire (Structures de données) — banque de questions isolées
Extraits du cours :
> [Structures de données > Les arbres binaires > Les arbres binaires]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 12 - Les arbres binaires
> Objectifs :
> ▷ Connaître les algorithmes sur les arbres binaires
> ▷ Calculer la taille et la hauteur d'un arbre binaire
> ▷ Parcourir un arbre de différentes façons (ordres infixe, préfixe ou suffixe; ordre en largeur ou profondeur
> d'abord).
> 1 Les arbres binaires
> Parmi la forêt d'arbres possibles, on s'intéressera essentiellement aux arbres ditbinaires :
> 1.1 Définition
> Définition
> Un arbre binaire est un arbre dedegré 2dont les noeuds sont de degré 2au plus.
> Vocabulaire :
> Les enfants d'un noeud sont lusde gauche à droiteet sont appelés :fils gaucheet fils droit.
> Par exemple, l'expressiona× b + c− (d + e) est représentée par l'arbre binaire ci-dessous :
> Question 1 :Parmi les arbres du cours sur les arbres (chapitre 10), lesquels sont binaires?
> Réponses :
> 1.2 Remarques
> Les arbres binaires forment une structure de données
> [Structures de données > Arbres > 1.3 Caractéristiques d'un arbre]
> #### 1.3.1 Outils numériques de description
> 
>     - la **taille** d'un arbre est son nombre total de nœuds. Ici, elle vaut 8.
> 
>     - l'**arité** d'un nœud est son nombre de fils. Ici, l'arité de B vaut 2, celle de F vaut 1, celle de Z vaut 0.
> 
>     - la **profondeur** d'un nœud est le nombre de nœuds de son chemin le plus court vers la racine. 
>     Ici, la profondeur de G est 3 (G-K-C), la profondeur de B est 2 (B-C), la profondeur de Z est 4 (Z-F-B-C), la profondeur de C est 1.
> 
>     - la **hauteur** d'un arbre est la profondeur de son nœud le plus profond. 
>     Ici, la hauteur de l'arbre est 4.  
>         Nous prendrons comme **convention** que :  
>         - si un arbre est réduit à **un seul nœud-racine**, sa hauteur sera **1**.
>         - si un arbre est **vide**, sa hauteur est **0**.
> 
> *Cette convention est celle adoptée dans le sujet 0 publié le 15/12/2020. Attention, dans certains ouvr
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=expliquer / explication / comprendre | Bloom=comprendre | formulations typiques : indiquer, expliquer, preciser, quel
    style réel : « 2. On souhaite parcourir l'arbre. Indiquer l'ordre de visite des nœuds lors d'un parcours en largeur. »
- slot 2 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, fonction
    style réel : « 4. Recopier et compléter la fonction liste_joueurs qui prend pour argument un arbre de com-
pétition arb et qui renvoie un tableau contenant les participants au tournoi, chaque nom ne
devant ﬁgurer qu'une seule fois dans »
- slot 3 | archétype=expliquer / explication / comprendre | Bloom=comprendre | formulations typiques : indiquer, expliquer, preciser, quel
    style réel : « 3. Parmi les quatre propositions A, B, C et D ci-dessous, donnant un parcours en
largeur d'abord de l'arbre, une seule est correcte. Indiquer laquelle. »
- slot 4 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, lignes
    style réel : « 12. Recopier et compléter les lignes 4, 6 et 7 du code de la fonction precede. »

Le champ id vaut « B-arbre_binaire ».