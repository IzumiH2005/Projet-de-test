# Plan B-complexite (banque)

Notion : complexite (Algorithmique) — banque de questions isolées
Extraits du cours :
> [Structures de données > Dictionnaires > 1.3 Conclusion]
> Il y a donc une différence fondamentale à connaître entre les temps de recherche d'un élément à l'intérieur :
> 
>     - d'une **liste** : temps **proportionnel** à la taille de la liste (ordre de complexité linéaire, $O(n)$)
>     - d'un **dictionnaire** : temps **constant**, indépendant de la taille du dictionnaire (ordre de complexité constant, $O(1)$)
> 
> Attention : en ce qui concerne **les temps d'accès** à un élément, la structure de tableau dynamique des listes de Python fait que ce temps d'accès est aussi en temps constant (comme pour les dictionnaires). On voit alors que les listes Python ne sont pas des *listes chaînées*, où le temps d'accès à un élément est directement proportionnel à la position de cet élément dans la liste.
> [Algorithmique > Diviser pour regner > Diviser pour regner]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 24 - Diviser pour régner
> Objectifs :
> ▷ Ecrire un algorithme en utilisant la méthode"diviser pour régner".
> 1 Introduction
> Nous avons vu en première deux algorithmes de tris assez naturels, mais peu efficaces : letri par insertionet
> le tri par sélectionen classe de Première.
> Cette année, nous allons étudier un algorithme beaucoup plus efficace et très utilisé, inventé parJohn Von
> Neumann en 1945 : letri par fusion.
> Cet algorithme nous permettra d'illustrer la méthodediviser pour régnerque nous avions également déjà
> vue lors de larecherche dichotomiqueen classe de Première.
> 2 La dichotomie (rappels)
> Nous avons vu en classe dePremièrel'algorithme dedichotomie. Ce mot, qui vient du grecdikhotomia, signifie
> « division en deux parties ».
> Notre but ici est la recherche de la présence (ou non) d'un élément dans une liste triée. Notre fonction renv
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / créer | Bloom=créer | formulations typiques : fonction, deduire, ecrire, precedente
    style réel : « 8. Écrire une fonction est_bien_parenthesee qui prend en paramètre une chaine
de caractères et qui implémente l'algorithme précédent. »
- slot 2 | archétype=autre / explication / créer | Bloom=créer | formulations typiques : ecrire, python, proposer, permettant
    style réel : « 6. Proposer une version itérative, non récursive, suite3 du calcul des termes de la
suite Un. »
- slot 3 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 5. Donner un exemple de chaine de caractères pour laquelle bon_compte renvoie
True alors qu'elle n'est pas bien parenthésée. »
- slot 4 | archétype=complexite / complexite / analyser | Bloom=analyser | formulations typiques : complexite, temps, complexite temps, cout temps
    style réel : « b. Indiquer sans justification la complexité en temps de calcul de cet algorithme pour un mot
de longueur n.
Remarque : on ne comptera que les comparaisons de caractères. »

Le champ id vaut « B-complexite ».