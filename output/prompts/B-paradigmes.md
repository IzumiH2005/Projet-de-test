# Plan B-paradigmes (banque)

Notion : paradigmes (Programmation) — banque de questions isolées
Extraits du cours :
> [Algorithmique > Diviser pour regner > 1. Retour sur l'algorithme de dichotomie]
> Nous avons vu en classe de Première l'algorithme de **dichotomie** (du grec *dikhotomia*, « division en deux parties »).
> 
> Notre but ici est la recherche de la présence (ou non) d'un élément dans une liste **triée**.  
> Notre fonction renverra donc un booléen.
> 
> La recherche *naïve* (élément par élément) est naturellement de complexité linéaire. Nous allons voir que la méthode dichotomique est plus efficace.
> 
> :arrow_right: Activité d'introduction
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
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « 1. Écrire la fonction echange(tab, i, j) qui prend en arguments une liste
Python tab et deux indices i, j , et réalise sur place l'échange des valeurs
dans tab à ces indices. La fonction ne renvoie rien. »
- slot 2 | archétype=complexite / complexite / analyser | Bloom=analyser | formulations typiques : complexite, temps, complexite temps, cout temps
    style réel : « 3. Quelle est l'ordre de grandeur de la complexité en temps de l'algorithme obtenu ? »
- slot 3 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier completer, fonction, recopier
    style réel : « 8. Compléter la fonction prog_dyn ci-dessous qui prend en paramètre une
pyramide p, et qui renvoie le score maximal pour un conduit dans p. Pour cela,
on construit une pyramide s remplie de 0 de la même taille et la remp »

Le champ id vaut « B-paradigmes ».