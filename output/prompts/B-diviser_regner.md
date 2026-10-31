# Plan B-diviser_regner (banque)

Notion : diviser_regner (Algorithmique) — banque de questions isolées
Extraits du cours :
> [Algorithmique > Diviser pour regner > 4.1 Preambule : l'interclassement]
> Le mécanisme principal du tri fusion est la **fusion** de deux listes triées en une nouvelle liste elle aussi triée.
> 
> On appelera ce mécanisme l'**interclassement**.
> 
>     Pour interclasser deux listes triées ```lst1``` et ```lst2```.
> 
>     - on part d'une liste vide ```lst_totale```
>     - on y ajoute alternativement les éléments de ```lst1``` et ```lst2```, en veillant à maintenir un ordre croissant. Il faut pour cela gérer séparément un indice ```i1``` pour la liste ```lst1```  et un indice ```i2```  pour la liste ```i2```.
>     - quand une liste est épuisée, on y ajoute la totalité restante de l'autre liste.
> 
>     
>     Coder la fonction ```interclassement```. 
> 
>     :arrow_right: Aide avec des codes à trous
> 
>     
> 
> **Remarque :** cette fonction fait l'objet d'un exercice de la BNS, qui n'utilise pas le slicing (ce qui rend le code plus efficace).
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
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 16. e2 = L2[i2]
17.
18.
19.
20.
21.
22. »
- slot 2 | archétype=expliquer / explication / comprendre | Bloom=comprendre | formulations typiques : indiquer, expliquer, preciser, quel
    style réel : « 3. Parmi les quatre propositions A, B, C et D ci-dessous, donnant un parcours en
largeur d'abord de l'arbre, une seule est correcte. Indiquer laquelle. »
- slot 3 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 10. i2 = i2 + 1 »

Le champ id vaut « B-diviser_regner ».