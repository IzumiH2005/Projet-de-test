# Plan B-liste_chainee (banque)

Notion : liste_chainee (Structures de données) — banque de questions isolées
Extraits du cours :
> [Structures de données > Listes Piles Files > 2.2 Les listes chaînées *(linked lists)*]
> Lorsque l'implémentation de la liste fait apparaître une chaîne de valeurs, chacune pointant vers la suivante, on dit que la liste est une liste **chaînée**.
> 
> **Implémentation choisie :**
> 
> - Une liste est caractérisée par un ensemble de cellules.
> - Le lien (on dira souvent le «pointeur») de la variable est un lien vers la première cellule, qui renverra elle-même sur la deuxième, etc.
> - Chaque cellule contient donc une valeur et un lien vers la cellule suivante.
> - Une liste peut être vide (la liste vide est notée ```x``` ou bien ```None``` sur les schémas)
> 
> Une conséquence de cette implémentation sous forme de liste chaînée est la non-constance du temps d'accès à un élément de liste : pour accéder au 3ème élément, il faut obligatoirement passer par les deux précédents.
> 
> **À retenir :** dans une liste chaînée, le temps d'accès aux éléments n'est pas constant.
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
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=definir_notion / explication / se souvenir | Bloom=se souvenir | formulations typiques : citer, signifie, definir, processus
    style réel : « 7. Donner des instructions permettant de construire les trois maillons m1, m0 et m8
et la liste chaînée représentés ci -dessus. On nommera la liste chaînée
ma_liste. »
- slot 2 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, lignes
    style réel : « 3. Recopier et compléter les pointillés pour que la fo nction réponde à la
demande. »
- slot 3 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 9. Donner une instruction permettant de transformer ma_liste en la liste
chaînée représentée ci-dessous :

On souhaite à présent une fonction tri_dictatorial_chaine qui prend en
paramètre une instance de liste chaînée ch »

Le champ id vaut « B-liste_chainee ».