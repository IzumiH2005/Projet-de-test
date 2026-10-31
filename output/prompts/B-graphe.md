# Plan B-graphe (banque)

Notion : graphe (Structures de données) — banque de questions isolées
Extraits du cours :
> [Structures de données > Graphes > Introduction]
> Exercice 3 du sujet 0 version A - 2024
> 
>     
> 
>     
> 
>     {{
>     correction(True,
>     """
> \"Correction Q3.\" 
>         La matrice d'adjacence de G1 est :
>         $\\pmatrix{
>         0 & 4 & 0 & 0 & 4 & 0 & 0  \\\\
>         4 & 0 & 0 & 0 & 0 & 7 & 5  \\\\ 
>         0 & 0 & 0 & 4 & 8 & 0 & 0  \\\\
>         0 & 0 & 4 & 0 & 6 & 8 & 0  \\\\ 
>         4 & 0 & 8 & 6 & 0 & 0 & 0  \\\\
>         0 & 7 & 0 & 8 & 0 & 0 & 3  \\\\ 
>         0 & 5 & 0 & 0 & 0 & 3 & 0  \\\\
>         }$  
>     """
>     )
>     }}
> 
>     {{
>     correction(True,
>     """
> \"Correction Q4.\" 
>         ```python linenums='1'
>         G2 = {'A': ['B', 'C', 'H'],
>               'B': ['A', 'I'],
>               'C': ['A', 'D', 'E'],
>               'D': ['C', 'E'],
>               'E': ['C', 'D', 'G'],
>               'F': ['G', 'I'],
>               'G': ['E', 'F', 'H'],
>               'H': ['A', 'G', 'I'],
>               'I': ['B', 'F', 'H']
>              }
>  
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
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 17. Déterminer les affichages produits lors de l'exécution de l'appel suivant :
 mystere(graphe_airinfo, 'W', [], 0, 'B') »
- slot 2 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, lignes
    style réel : « 6. Compléter la méthode de la classe Region ci-dessous à partir de la ligne 6 :

1
2
3

4
5
6
def est_coloriee(self):
 '''
 Renvoie True si une couleur a été attribuée à cette
région et False sinon.
 : return (bool)
 ''' »
- slot 3 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « 10. Écrire le code d'une fonction Python liste_villes_proches qui permet de
répondre à la demande des voyageurs. Cette fonction prend en paramètres un
dictionnaire graphe représentant le graphe, une clé du dictionnaire v »
- slot 4 | archétype=autre / explication / créer | Bloom=créer | formulations typiques : fonction, deduire, ecrire, precedente
    style réel : « 9. Donner une explication au problème décrit ci-dessus. Vous pourrez vous
appuyer sur les tests donnés précédemment. »

Le champ id vaut « B-graphe ».