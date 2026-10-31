# Plan B-fonctions (banque)

Notion : fonctions (Programmation) — banque de questions isolées
Extraits du cours :
> [Programmation > Pratiques de programmation > 4.3 Le module ```doctest```]
> Le module ```doctest```  permet d'écrire les tests **à l'intérieur** de la docstring d'une fonction. 
> 
> Considérons une fonction dont le but est de compter les voyelles du mot passé en paramètre.
> 
> ```python
> def compte_voyelles(mot):
>     """
>     renvoie le nombre de voyelles du mot donné en paramètre.
>     >>> compte_voyelles("python")
>     2
>     >>> compte_voyelles("HTTP")
>     0
>     >>> compte_voyelles("eau")
>     3
>     """
>     voyelles = "aeiou"
>     total = 0
>     for lettre in mot:
>         if lettre in voyelles:
>             total += 1
>     return total
> ```
> 
> Observez bien la docstring : elle contient explicitement ce qu'on veut que renvoie le terminal lorsqu'on appellera la fonction.
> On écrit donc les trois chevrons ```>>>``` suivi de l'appel à la fonction, et à la ligne en dessous ce que nous espérons que la fonction nous renvoie.
> On peut écrire autant de tests que l'on veut.
> 
> Ensuite, en co
> [Structures de données > Listes Piles Files > Introduction]
> Exercice 5 du sujet Centres Étrangers 1 - 2021
> 
>     Exercice 1 du sujet La Réunion J2 - 2022
> 
>     Exercice 2 du sujet Métropole Candidats Libres J1 - 2021
> 
>     Exercice 5 du sujet Amérique du Nord J1 - 2021
> 
>     Exercice 2 du sujet Centres Étrangers J1 - 2022
> 
>     Exercice 3 du sujet Centres Etrangers J1 - 2023
> 
>     Jeu du Simon
> 
>     Cet exercice est basé sur l'énigme n°5 d'Advent Of Code 2018.
> 
>     Le but est de réduire le plus possible une chaîne de caractères (comme ```dabAcCaCBAcCcaDA``` ) en obéissant à la règle suivante :
> 
>         Dès que deux lettres identiques mais de casse différente (majuscule-minuscule ou minuscule-majuscule) sont côte à côte dans la chaîne, on les supprime de la chaîne.
> 
>     Exemple : 
>     ```
>     dabAcCaCBAcCcaDA  On enlève le premier 'cC'.
>     dabAaCBAcCcaDA    Cela donne naissance à un 'Aa', qu'on enlève.
>     dabCBAcCcaDA      On enlève alors 'cC' (ou 'Cc'
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « 2. Écrire une fonction former_pile qui prend en paramètre une ﬁle F et qui renvoie une pile P
contenant les mêmes éléments que la ﬁle. »
- slot 2 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, fonction
    style réel : « 6. Compléter la fonction distance_totale :
 1 def distance_totale(dep):
2 total = 0
3 for i in range(...):
4 ...
5 return total »
- slot 3 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier completer, fonction, recopier
    style réel : « 3. On s'intéresse ici à la fonction suivante écrite en Python où s est une chaîne de
caractères et n un entier naturel.

def produit(s, n):
 if n == 0:
 return [""]
 else:
 res = []
 for i in range(len(s)):
 res = res + »
- slot 4 | archétype=trace_execution / valeur / appliquer | Bloom=appliquer | formulations typiques : apres, apres execution, execution, renvoie
    style réel : « 4. Quel sera le résultat de l'appel generer_ordre('AXU7') ? »

Le champ id vaut « B-fonctions ».