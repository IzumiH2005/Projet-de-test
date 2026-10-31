# Plan B-recherche_dichotomique (banque)

Notion : recherche_dichotomique (Algorithmique) — banque de questions isolées
Extraits du cours :
> [Algorithmique > Diviser pour regner > 1.1 Version impérative]
> {#
> 
>     ```python linenums='1'
>     def recherche_dichotomique(tab, val) :
>         '''
>         renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
>         '''
>         ...
>     ```
> #}
> 
>     ```python linenums='1'
>     def recherche_dichotomique(tab, val) :
>         '''
>         renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
>         '''
>         i_debut = 0
>         i_fin = len(tab) - 1
>         while i_debut >> tab = [1, 5, 7, 9, 12, 13]
> >>> recherche_dichotomique(tab, 12)
> True
> >>> recherche_dichotomique(tab, 17)
> False
> ```
> 
> À chaque tour de la boucle ```while```, la taille de la liste est divisée par 2. Ceci confère à cet algorithme une **complexité logarithmique** (bien meilleure qu'une complexité linéaire).
> [Algorithmique > Diviser pour regner > 1.2 Version récursive]
> #### 1.2.1 Préambule : le slicing
> Pour écrire simplement la version récursive de cet algorithme, nous allons avoir besoin de faire du *slicing* (découpage) de listes. Cette manipulation n'est pas au programme de NSI (même si elle est très simple). Attention, elle a un coût algorithmique important, qui peut fausser notre analyse de complexité.
> 
> Exemples de slicing :
> 
> ```python
> >>> lst = ['a', 'b', 'c', 'd', 'e']
> >>> lst[:2]
> ['a', 'b']
> >>> lst[2:]
> ['c', 'd', 'e']
> ```
> 
> On comprend que  :
> 
> - ```lst[:k]``` va renvoyer la sous-liste composée du premier élément jusqu'à celui d'indice ```k``` **non inclus**.
> - ```lst[k:]``` va renvoyer la sous-liste composée du ```k```-ième élément (**inclus**) jusqu'au dernier.
> - plus généralement, ```lst[k:p]``` va renvoyer la sous-liste composée du ```k```-ième élément (**inclus**) jusqu'au ```p```-ième (**non inclus**).
> 
> #### 1.2.2 Dichotomie récursive avec 
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=table_routage / explication / appliquer | Bloom=appliquer | formulations typiques : routeur, routage, table routage, routeurs
    style réel : « 4. Bob envoie un message à Alice.
Énumérer dans l'ordre tous les routeurs par lesquels transitera ce message. »
- slot 2 | archétype=lire_sql / sql / appliquer | Bloom=appliquer | formulations typiques : requete, resultat, resultat requete, select
    style réel : « 3. Donner le résultat de la requête suivante en l'appliquant à l'extrait de la table
joueur donné dans l'énoncé.
 SELECT prenom FROM joueur WHERE ann_naiss < 1985 »
- slot 3 | archétype=definir_notion / explication / se souvenir | Bloom=se souvenir | formulations typiques : citer, signifie, definir, processus
    style réel : « 3. Définir la matrice d'adjacence du graphe G1 (en prenant les sommets dans
l'ordre alphabétique). »

Le champ id vaut « B-recherche_dichotomique ».