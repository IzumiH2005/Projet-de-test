# Plan B-tri (banque)

Notion : tri (Algorithmique) — banque de questions isolées
Extraits du cours :
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
> [Algorithmique > Diviser pour regner > 4.3 Complexité]
> La division par 2 de la taille de la liste pourrait nous amener à penser que le tri fusion est de complexité logarithmique, comme l'algorithme de dichotomie. Il n'en est rien.
> 
> En effet, l'instruction finale ```interclassement(tri_fusion(lst[:m]), tri_fusion(lst[m:]))``` lance **deux** appels à la fonction ```tri_fusion``` (avec certes des données d'entrée deux fois plus petites).
> 
> On peut montrer que :
> 
>     L'algorithme de tri fusion est en $O(n \log n)$.
> 
>     On dit qu'il est **quasi-linéaire**. (ou *linéarithmique*)
> 
> Une complexité quasi-linéaire (en $O(n \log n)$) se situe «entre» une complexité linéaire (en $O(n)$) et une complexité quadratique (en $O(n^2)$). Mais elle est plus proche de la complexité linéaire.
> 
> Pour finir, une jolie animation permettant de comparer les tris :
> 
> Issue de ce site
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 5. Parmi les propositions suivantes, choisir celle qui correspond au type de tri
effectué par la fonction classer.
 tri par insertion
 tri par sélection
 tri à bulles
 tri fusion »
- slot 2 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 14. else: »
- slot 3 | archétype=expliquer / explication / évaluer | Bloom=évaluer | formulations typiques : justifiant, indiquer justifiant, indiquer, verifier
    style réel : « 4. Déterminer la valeur numérique prise par k lors de ce premier appel. Une
justification est attendue. »

Le champ id vaut « B-tri ».