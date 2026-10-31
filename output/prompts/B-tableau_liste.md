# Plan B-tableau_liste (banque)

Notion : tableau_liste (Programmation) — banque de questions isolées
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
> [Structures de données > Dictionnaires > Exercices sur les dictionnaires]
> On considère la liste suivante :
> 
>     ```lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']``` 
> 
>     Quel est le **chiffre** qui revient le plus fréquemment dans cette liste ?
> 
>      
>     {{
>     correction(True,
>     """
> \"Correction\" 
>         ```python linenums='1'
>         lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053',
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, fonction
    style réel : « 4. Compléter le code de la fonction plus_grande_base_exhaustive.
 1 def plus_grande_base_exhaustive(carte):
 2 n = len(carte)
 3 # les tailles vont de n à 1, de -1 en -1
 4 for taille in range(n, 0, -1):
 5 i = 0
 6 whil »
- slot 2 | archétype=autre / explication / créer | Bloom=créer | formulations typiques : ecrire, python, proposer, permettant
    style réel : « 23. return L

Dans cette fonction, les entiers i1 et i2 représentent respectivement les indices des
éléments des listes L1 et L2 que l'on souhaite comparer :
• Si aucun des deux indices n'est valide, la boucle while est »
- slot 3 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 6. Dans ce parcours, on manipule la liste Python nommée listeS uniquement à
l'aide d'appels de la forme listeS.append(sommet) et listeS.pop(0).
Donner la structure de données correspondant à ces manipulations. »
- slot 4 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « 2. Écrire une fonction moitie_gauche(tab) qui prend en argument un tableau tab et
renvoie un nouveau tableau contenant la moitié gauche de tab. Si le nombre d'éléments
de tab est impair, l'élément du centre se trouve dan »

Le champ id vaut « B-tableau_liste ».