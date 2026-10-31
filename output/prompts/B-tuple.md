# Plan B-tuple (banque)

Notion : tuple (Programmation) — banque de questions isolées
Extraits du cours :
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
> [Structures de données > Les listes > Les listes]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 5 - Les listes
> Objectifs :
> ▷ Distinguer des structures par le jeu des méthodes qui les caractérisent.
> ▷ Choisir une structure de données adaptée à la situation à modéliser.
> ▷ Distinguer la recherche d'une valeur dans une liste et dans un dictionnaire.
> 1 Introduction
> Historique
> Le langage de programmationLisp (inventé parJohn McCarthy en 1958) a été un des premiers langages
> de programmation à introduire cette notion de liste (Lisp signifie list processing).
> Lisp qui fait partie de la plus ancienne famille de langages de programmation à la fois impératifs et
> fonctionnels, est devenu dans les années 1970-80 le langage de choix pour la recherche en intelligence
> artificielle. Ils sont aujourd'hui utilisés dans de nombreux domaines, de la programmation Web à la
> finance.
> Python abuse du terme liste qu'il utilise pour ce qui sont destableaux dyna
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 4. On définit une date comme un tuple :
(nom_jour,numero_jour, numero_mois,annee) .

22-NSIJ1G11 Page 3 sur 14 »
- slot 2 | archétype=justifier_choix / explication / évaluer | Bloom=évaluer | formulations typiques : justifier, recursive, citer, fonction
    style réel : « 2. Justifier que le couple (2, 3) n'en est pas une. »
- slot 3 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « b. Supposant l'import réalisé, écrire une fonction distance_points(a,b) qui
prend en argument deux tuples a et b représentant les coordonnées de deux
points et renvoie la distance qui les sépare. »

Le champ id vaut « B-tuple ».