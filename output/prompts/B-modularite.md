# Plan B-modularite (banque)

Notion : modularite (Programmation) — banque de questions isolées
Extraits du cours :
> [Architecture, OS et réseaux > Cryptographie > Introduction]
> **Utilisation des bibliothèques cryptographiques du module ```sympy```.**
> 
>     Documentation : https://docs.sympy.org/latest/modules/crypto.html{target="_blank"}
> 
>     Décoder la phrase ```RYTVJKGCLJWRTZCVRMVTLEDFULCVHLZWRZKKFLKRMFKIVGCRTV```, sachant qu'elle a été chiffrée par décalage (*shift* en anglais...)
> 
>     **Chiffrage affine**
> 
>     Principe du chiffrage affine :
> 
>     - Chaque lettre est codée par son rang, en commençant à 0 (A->0, B->1, ..., Z->25)
>     - On applique à chaque rang la transformation affine 
>     $f(x) = (ax+b)\, \%26$
> 
>     où $a$ et $b$ sont deux nombres entiers. Attention, $a$ doit être premier avec 26.
> 
>         Deux nombres sont dits *premiers entre eux* si leur PGCD vaut 1. 
> 
>         Exemples :
>         
>         - 8 et 15 sont premiers entre eux (ils n'ont aucun diviseur commun autre que 1)
>         - 8 et 12 ne sont pas premiers entre eux (leur PGCD vaut 4).
> 
>     
> [Programmation > Programmation objet > Programmation objet]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 3 - Programmation orientée objet
> Objectifs :
> ▷ Connaître le vocabulaire de la programmation objet : classes, attributs, méthodes, objets.
> ▷ Ecrire la définition d'une classe
> ▷ Accéder aux attributs et méthodes d'une classe.
> 1 Introduction
> Jusqu'à présent nous avons utilisé des objets dont le type est prédéfini :int, float, bool, str, list,
> tuple, dict. Sans le savoir, nous avons découvert les concepts de laprogrammation orientée objet
> ou POO. Ainsi, en classe de Première, nous avions déjà appris à utiliser des méthodes associées à ces
> types, comme :
> ma_liste.append(valeur)
> Comme de nombreux autres langages tels queJava ou C++, Python est un langage orienté objet .
> On peut donc dire que tout y estobjet. Une variable de typeint est en fait un objet de typeint donc
> construit à partir de la classeint. Idem pour lesfloat et str. Mais également
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier completer, fonction, recopier
    style réel : « 6. Écrire la ou les instructions qui permettent de créer la course de la cliente
Jeanne Doe.
À l'aide de la bibliothèque Python datetime on peut calculer la différence de temps
en secondes entre deux dates à l'aide de la »
- slot 2 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier completer, fonction, recopier
    style réel : « 3. Le mélange de Fischer Yates est un algorithme permettant de permuter
aléatoirement les éléments d'une liste. On donne ci-dessous une mise en œuvre
récursive de cet algorithme en Python.

from random import randint
def »
- slot 3 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, fonction
    style réel : « 12. Recopier et compléter les lignes 7 à 13 du code ci-après de la fonction
generer_sac.
 1 from random import randint
 2 def generer_sac():
 3 '''
 4 renvoie un sac (8 entiers)
 5 : return (list) un sac
 6 '''
 7 sac = »

Le champ id vaut « B-modularite ».