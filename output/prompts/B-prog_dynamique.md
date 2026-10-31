# Plan B-prog_dynamique (banque)

Notion : prog_dynamique (Algorithmique) — banque de questions isolées
Extraits du cours :
> [Algorithmique > Programmation dynamique > 2.3 Somme maximale par force brute]
> **Q1.** Écrire une fonction ```max_force_brute``` qui prend en paramètre une pyramide ```pyr``` et qui renvoie la somme maximale parmi tous les trajets possibles.
> 
>     
> 
>     **Q2.** Testez votre algorithme avec ```pyr_exemple```, ainsi qu'avec des pyramides de taille supérieure. Que se passe-t-il ?
> [Algorithmique > Programmation dynamique > 5. Optimisation de la méthode récursive par programmation dynamique]
> La lenteur de l'algorithme précédent vient du fait que certains calculs sont redondants. 
> 
> Par exemple, le calcul du maximum de la pyramide rouge sera lancé en tant que sous-pyramide droite de la valeur 5, et en tant que sous-pyramide gauche de la valeur 4.
> 
> Si la pyramide initiale est grande, ces appels inutiles vont se multiplier et ralentir considérablement l'exécution du programme.
> 
>     Dans le code récursif suivant, chaque pyramide est identifiée par les coordonnées de son sommet, stockées dans le tuple ```pos``` .
>     On va utiliser un dictionnaire ```dict_max``` qui associera à chaque sommet ```(i, j)``` la somme maximale de sa pyramide.
> 
>     Pour chaque sommet de coordonnées ```(i, j)``` :
>     
>     - si on est tout en bas de la pyramide, on renvoie la valeur du sommet de cette pyramide (réduite à une valeur).
>     - sinon :
>         - on interroge notre dictionnaire de stockage ```
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 2. On considère un entier taille strictement positif. Déterminer la somme des
valeurs de toutes les cellules d'un carré constructible de taille cases de côté. »
- slot 2 | archétype=ordonnancement / explication / comprendre | Bloom=comprendre | formulations typiques : processus, interblocage, situation, elu
    style réel : « 2. Donner les différents états possibles d'un processus. »
- slot 3 | archétype=definir_notion / explication / se souvenir | Bloom=se souvenir | formulations typiques : citer, signifie, definir, processus
    style réel : « a. Expliciter ce qu'est une adresse MAC (Media Access Control) ou adresse physique. »

Le champ id vaut « B-prog_dynamique ».