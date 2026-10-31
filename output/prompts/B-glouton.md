# Plan B-glouton (banque)

Notion : glouton (Algorithmique) — banque de questions isolées
Extraits du cours :
> [Algorithmique > Programmation dynamique > 1. Retour sur l'algorithme glouton]
> Nous avons vu en Première un algorithme capable de donner une combinaison de pièces pour rendre la somme ```somme```.
> 
> Cet algorithme fonctionnait de manière gloutonne : on cherche à rendre à chaque fois la plus grosse pièce possible.
> 
>     Compléter la fonction ```rendu_glouton``` qui prend en paramètres une liste de pièces ```pieces``` (classées dans l'ordre **croissant**) et la somme à rendre ```somme``` et qui renvoie **le nombre minimal** de pièces qu'il faut rendre.
> 
>     ```python linenums='1'
>     def rendu_glouton(pieces, somme):
>         i =  ... # (1)
>         nb_pieces = ...
>         while ... > ...:
>             if ... >> rendu_glouton([1, 2, 5], 12)
>     3
>     ``` 
> 
>     
> 
> Nous savons que cet algorithme est optimal sous certaines conditions sur la composition des pièces. Par exemple le système des euros (1, 2, 5, 10, 20, 50, 100, 200) rend l'algorithme glouton optimal (on dit que le
> [Programmation > Pratiques de programmation > 4.2 Revoilà les ```assert```]
> Utiliser des ```assert``` permet d'écrire très simplement les tests précédents.
> 
> Reprenons notre fonction ```valeur_absolue()```. Sa fonction test  ```test_valeur_absolue()``` peut s'écrire :
> 
> ```python
> def test_valeur_absolue():
>     assert valeur_absolue(-3) == 3
>     assert valeur_absolue(0) == 0
>     assert valeur_absolue(7) == 7
> 
> ```
> 
> **Exercice :**  
> Écrire une fonction ```maxi(liste)``` qui renvoie le plus grand élément de la liste ```liste``` passée en paramètre (de préférence sans utiliser la fonction ```max()``` ...).  
> Vous écrirez **d'abord** une fonction ```test_maxi()``` avant d'écrire la fonction ```maxi(liste)```
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, fonction
    style réel : « 4. Recopier et compléter les lignes 2 et 4 du code ci -après de la fonction
poids_total qui prend en paramètre une liste d'objets de la classe Colis et
qui renvoie le poids total de l'ensemble des colis de cette liste. »
- slot 2 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « 1. Écrire la méthode passer_transit de la classe Colis qui permet de
mettre l'état du colis à la valeur 'transit'. »
- slot 3 | archétype=complexite / explication / évaluer | Bloom=évaluer | formulations typiques : cout, nombre comparaisons, comparaisons, tri
    style réel : « 14. Préciser le tri utilisé dans la question précédente, ainsi que son coût d'exécution
en temps dans le pire des cas selon le nombre 𝑛𝑛 de sommets (constant,
logarithmique soit en log2(𝑛𝑛), linéaire soit en 𝑛𝑛, quasi-li »

Le champ id vaut « B-glouton ».