# Plan B-dictionnaire (banque)

Notion : dictionnaire (Structures de données) — banque de questions isolées
Extraits du cours :
> [Structures de données > Dictionnaires > 1.1 Protocole de mesure]
> Le but est de créer une liste et un dictionnaire de même taille (arbitraire), et de comparer ensuite le temps de recherche d'un élément n'appartenant pas à ces deux structures.
> 
> **Q1.** Créer une fonction ```fabrique_liste``` qui prend en paramètre un entier ```nb``` et qui renvoie une liste composée de tous les entiers de ```0``` à ```nb-1```.
> 
> **Q2.** Créer une fonction ```fabrique_dict``` qui prend en paramètre un entier ```nb``` et qui renvoie dictionnaire composé de paires qui associent à toutes les clés ```k```  de ```0``` à ```nb-1``` leur propre valeur ```k```. 
> 
> {{
> correction(True,
> """
> \"Correction\" 
>     ```python
>     def fabrique_dict(nb):
>         dct = {k:k for k in range(nb)}
>         return dct
>     ```
> 
> """
> )
> }}
> 
> **Q3.** Créer une fonction ```mesures``` qui prend en paramètre un entier ```nb``` et qui :
> 
> - Créé une liste et un dictionnaire de taille ```nb``` à l'aide des fon
> [Structures de données > Structures donnees > Structures donnees]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 4 - Les structures de données
> Objectifs :
> ▷ Remettre en mémoire les structures de données vues enPremière
> ▷ Montrer qu'il existe plusieurs implémentations possibles
> 1 Introduction
> En informatique, on manipule essentiellement des données. Lorsqu'elles sont simples comme desnombres,
> des chaînes de caractères ou des booléens, on peut les stocker dans des variables qui seront typées en
> fonction de la nature de la donnée.
> 2 Définition
> A retenir!
> Une structure de données est une organisation logique des données permettant de simplifier ou
> d'accélérer leur traitement.
> 3 Exemple
> Par exemple, si on a écrit un code avec les affectations suivantes :
> 1 n = 4
> 2 p = -5
> 3 r = 0.7
> 4 phrase = 'hello'
> 5 test = True
> Python est un langage avec untypage dynamique, c'est-à-dire que le type de la variable est automa-
> tiquement déterminé la première fois qu'elle
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / créer | Bloom=créer | formulations typiques : ecrire, python, proposer, permettant
    style réel : « 5. Proposer une autre solution pour éviter les problèmes d'identification des
candidats portant les mêmes prénoms et noms. Cette proposition devra
prendre en compte la sensibilité des données et être argumentée
succincte »
- slot 2 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « 4. On souhaite à présent créer un dictionnaire de chiffrement. Ecrire une fonction
dico_chiffrement(alphabet) qui prend en paramètre alphabet un tableau
de lettres et qui renvoie un dictionnaire de chiffrement dont les c »
- slot 3 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 8. Déterminer la valeur de l'expression graphe_airinfo['T']['P']. »
- slot 4 | archétype=autre / explication / créer | Bloom=créer | formulations typiques : fonction, deduire, ecrire, precedente
    style réel : « 9. Écrire en Python une fonction classement prenant en paramètre un
dictionnaire dont les clés sont les noms des candidats et les valeurs sont leurs
notes et qui, en utilisant la fonction enigme, renvoie la liste des cou »

Le champ id vaut « B-dictionnaire ».