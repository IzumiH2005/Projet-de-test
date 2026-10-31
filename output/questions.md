# Questions générées (NSI Terminale)

## B-abr
### Arbres binaires de recherche

**Q1** (1 pt, abr) Dans une médiathèque, les numéros d'inventaire des livres sont stockés dans un arbre binaire de recherche équilibré contenant environ 1 000 000 de numéros. Expliquer pourquoi la recherche d'un numéro dans cet arbre nécessite au plus une vingtaine de comparaisons, alors qu'une recherche dans une liste non triée peut en nécessiter un million.

<details><summary>Corrigé</summary>

À chaque nœud on ne poursuit que dans un seul sous-arbre, ce qui divise environ par 2 le nombre de nœuds restant. Le nombre de comparaisons est au plus la hauteur de l'arbre, de l'ordre de log2(n) ≈ 20 pour n = 10^6 (2^20 ≈ 10^6). Dans une liste non triée, il faut au pire examiner les n éléments.

</details>

**Q2** (1 pt, abr) On utilise la classe Noeud suivante :
```python
class Noeud:
    def __init__(self, v, g=None, d=None):
        self.valeur = v
        self.gauche = g
        self.droit = d
```
Un arbre vide est représenté par None.
Recopier et compléter les lignes 4 et 6 de la fonction `contient` qui prend en paramètres un arbre binaire de recherche `abr` et une valeur `v`, et renvoie True si `v` est présente dans l'arbre, False sinon.
```python
1 def contient(abr, v):
2     if abr is None:
3         return False
4     if ....... :
5         return True
6     elif ....... :
7         return contient(abr.gauche, v)
8     else:
9         return contient(abr.droit, v)
```

<details><summary>Corrigé</summary>

Ligne 4 : `if abr.valeur == v :`
Ligne 6 : `elif v < abr.valeur :`

</details>

**Q3** (1 pt, abr) On utilise la classe Noeud suivante :
```python
class Noeud:
    def __init__(self, v, g=None, d=None):
        self.valeur = v
        self.gauche = g
        self.droit = d
```
Un arbre vide est représenté par None.
On considère l'arbre binaire de recherche `a` obtenu en insérant successivement les valeurs 12, 7, 18, 3, 9, 15, 21, et la fonction :
```python
def somme_inf(abr, x):
    if abr is None:
        return 0
    if abr.valeur < x:
        return abr.valeur + somme_inf(abr.gauche, x) + somme_inf(abr.droit, x)
    return somme_inf(abr.gauche, x)
```
Calculer la valeur renvoyée par `somme_inf(a, 13)`.

<details><summary>Corrigé</summary>

Les valeurs strictement inférieures à 13 sont 12, 7, 3, 9 : la fonction renvoie 31.

</details>

## B-algo_simples
### Algorithmes simples

**Q1** (1 pt, algo_simples) On considère la fonction suivante, appliquée à une liste non vide d'entiers :
```python
def mystere(t):
    m = t[0]
    for e in t:
        if e > m:
            m = e
    return m
```
Indiquer ce que renvoie `mystere([4, 11, 2, 11, 7])` et expliquer le rôle de cette fonction.

<details><summary>Corrigé</summary>

Elle renvoie 11 : la fonction renvoie le maximum de la liste, en parcourant tous les éléments et en conservant la plus grande valeur rencontrée.

</details>

**Q2** (1 pt, algo_simples) Un club de randonnée enregistre ses sorties dans une table `Sortie(id, lieu, distance_km, denivele)`. Écrire une requête SQL qui renvoie le lieu et la distance des sorties dont le dénivelé dépasse strictement 800 m, triées par distance décroissante.

<details><summary>Corrigé</summary>

SELECT lieu, distance_km FROM Sortie WHERE denivele > 800 ORDER BY distance_km DESC;

</details>

**Q3** (1 pt, algo_simples) Recopier et compléter les lignes 3 et 5 de la fonction `compte` qui prend en paramètres une liste `t` et une valeur `x`, et renvoie le nombre d'occurrences de `x` dans `t`.
```python
1 def compte(t, x):
2     n = 0
3     for ....... :
4         if e == x:
5             .......
6     return n
```

<details><summary>Corrigé</summary>

Ligne 3 : `for e in t :`
Ligne 5 : `n = n + 1`

</details>

## B-arbre_binaire
### Arbres binaires

**Q1** (1 pt, arbre_binaire) Un arbre binaire a pour racine A ; A a pour fils gauche B et pour fils droit C ; B a pour fils gauche D ; C a pour fils gauche E et pour fils droit F. On convient que la hauteur d'un arbre réduit à sa racine vaut 1. Indiquer la taille, la hauteur et les feuilles de cet arbre.

<details><summary>Corrigé</summary>

Taille 6, hauteur 3, feuilles : D, E, F.

</details>

**Q2** (1 pt, arbre_binaire) On utilise la classe Noeud suivante :
```python
class Noeud:
    def __init__(self, v, g=None, d=None):
        self.valeur = v
        self.gauche = g
        self.droit = d
```
Un arbre vide est représenté par None.
Recopier et compléter la ligne 4 de la fonction `taille` qui renvoie le nombre de nœuds d'un arbre binaire.
```python
1 def taille(a):
2     if a is None:
3         return 0
4     return .......
```

<details><summary>Corrigé</summary>

Ligne 4 : `return 1 + taille(a.gauche) + taille(a.droit)`

</details>

**Q3** (1 pt, arbre_binaire) On reprend l'arbre de racine A (fils gauche B, fils droit C ; B a pour fils gauche D ; C a pour fils E à gauche et F à droite). Préciser l'ordre de visite des nœuds lors d'un parcours préfixe, puis lors d'un parcours infixe, en expliquant la règle utilisée.

<details><summary>Corrigé</summary>

Préfixe (racine, gauche, droit) : A B D C E F. Infixe (gauche, racine, droit) : D B A E C F.

</details>

**Q4** (1 pt, arbre_binaire) On utilise la classe Noeud suivante :
```python
class Noeud:
    def __init__(self, v, g=None, d=None):
        self.valeur = v
        self.gauche = g
        self.droit = d
```
Un arbre vide est représenté par None.
Recopier et compléter les lignes 3 et 5 de la fonction `nb_feuilles` qui renvoie le nombre de feuilles d'un arbre binaire.
```python
1 def nb_feuilles(a):
2     if a is None:
3         return .......
4     if a.gauche is None and a.droit is None:
5         return .......
6     return nb_feuilles(a.gauche) + nb_feuilles(a.droit)
```

<details><summary>Corrigé</summary>

Ligne 3 : `return 0`
Ligne 5 : `return 1`

</details>

## B-calculabilite
### Calculabilité, processus

**Q1** (1 pt, calculabilite) Un programme Python peut être passé en paramètre à une autre fonction, comme une donnée (par exemple son texte source). Indiquer un exemple de logiciel courant qui prend un programme en entrée et expliquer en quoi cela illustre le fait qu'un programme est aussi une donnée.

<details><summary>Corrigé</summary>

Exemples : un interpréteur Python, un compilateur, un antivirus, un système d'exploitation. Ils lisent le texte d'un programme comme une donnée qu'ils analysent, traduisent ou exécutent : code et données ont la même nature.

</details>

**Q2** (1 pt, calculabilite) Un élève propose d'écrire une fonction `arret(prog, x)` qui renvoie True si le programme `prog` s'arrête sur l'entrée `x` et False sinon, quel que soit `prog`. Expliquer pourquoi une telle fonction ne peut pas exister.

<details><summary>Corrigé</summary>

C'est le problème de l'arrêt, indécidable (Turing). Si `arret` existait, on construirait `paradoxe(p)` qui boucle indéfiniment si `arret(p, p)` vaut True et s'arrête sinon ; `paradoxe(paradoxe)` s'arrêterait si et seulement s'il ne s'arrête pas : contradiction.

</details>

**Q3** (1 pt, calculabilite) Deux processus P1 et P2 utilisent une imprimante R1 et un scanner R2. P1 obtient R1 puis demande R2 ; pendant ce temps P2 obtient R2 puis demande R1. Expliquer la situation obtenue, préciser l'état de chaque processus et proposer une solution pour l'éviter.

<details><summary>Corrigé</summary>

C'est un interblocage : P1 attend R2 détenue par P2 et P2 attend R1 détenue par P1 ; les deux processus sont bloqués indéfiniment. Solution : imposer le même ordre d'acquisition des ressources (R1 puis R2) à tous les processus.

</details>

## B-chaines
### Chaînes de caractères

**Q1** (1 pt, chaines) En Python, on exécute `s = 'bonjour'` puis `s[0] = 'B'`. Indiquer ce qui se produit et expliquer pourquoi. Préciser comment obtenir la chaîne 'Bonjour'.

<details><summary>Corrigé</summary>

Une erreur TypeError est levée : les chaînes sont immuables (non mutables). On crée une nouvelle chaîne : `s = 'B' + s[1:]`.

</details>

**Q2** (1 pt, chaines) Écrire une fonction `est_palindrome` qui prend en paramètre une chaîne de caractères `mot` et renvoie True si le mot se lit de la même façon dans les deux sens, False sinon. Par exemple `est_palindrome('kayak')` renvoie True.

<details><summary>Corrigé</summary>

```python
def est_palindrome(mot):
    n = len(mot)
    for i in range(n // 2):
        if mot[i] != mot[n - 1 - i]:
            return False
    return True
```

</details>

**Q3** (1 pt, chaines) On considère la fonction :
```python
def f(s):
    r = ''
    for c in s:
        if c not in 'aeiouy':
            r = r + c
    return r
```
Donner la valeur renvoyée par `f('informatique')`.

<details><summary>Corrigé</summary>

'nfrmtq'

</details>

**Q4** (1 pt, chaines) Recopier et compléter les lignes 3 et 5 de la fonction `inverse` qui renvoie la chaîne `s` écrite à l'envers (par exemple `inverse('nsi')` renvoie 'isn').
```python
1 def inverse(s):
2     r = ''
3     for ....... :
4         
5         r = .......
6     return r
```

<details><summary>Corrigé</summary>

Ligne 3 : `for c in s :`
Ligne 5 : `r = c + r`

</details>

## B-complexite
### Complexité

**Q1** (1 pt, complexite) La fonction suivante teste si une liste contient deux éléments égaux :
```python
def doublon(t):
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] == t[j]:
                return True
    return False
```
En déduire une fonction `doublon_trie(t)` qui effectue le même test sur une liste `t` supposée triée dans l'ordre croissant, en ne parcourant la liste qu'une seule fois.

<details><summary>Corrigé</summary>

```python
def doublon_trie(t):
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    return False
```
Dans une liste triée, deux éléments égaux sont forcément voisins.

</details>

**Q2** (1 pt, complexite) Proposer une fonction Python `puissance(x, n)` permettant de calculer x^n (n entier positif) en utilisant le fait que x^n = (x^(n//2))^2 si n est pair, et x * (x^(n//2))^2 sinon, afin d'effectuer un nombre de multiplications de l'ordre de log2(n).

<details><summary>Corrigé</summary>

```python
def puissance(x, n):
    if n == 0:
        return 1
    p = puissance(x, n // 2)
    if n % 2 == 0:
        return p * p
    return x * p * p
```

</details>

**Q3** (1 pt, complexite) On effectue une recherche dichotomique de la valeur 37 dans la liste triée [3, 8, 12, 19, 25, 31, 37, 44, 50]. À chaque étape, on prend l'indice du milieu m = (g + d) // 2. Donner la liste des valeurs comparées à 37 et déterminer le nombre de comparaisons.

<details><summary>Corrigé</summary>

g=0,d=8 : m=4, valeur 25 ; g=5,d=8 : m=6, valeur 37 trouvée. Valeurs comparées : 25 puis 37, soit 2 étapes.

</details>

**Q4** (1 pt, complexite) On considère la fonction `doublon(t)` qui compare chaque élément `t[i]` à tous les éléments `t[j]` avec j > i (deux boucles imbriquées). Déterminer sa complexité en temps dans le pire des cas en fonction de la taille n de la liste, et la comparer à celle d'un parcours unique sur une liste triée.

<details><summary>Corrigé</summary>

Pire cas (aucun doublon) : (n-1) + (n-2) + ... + 1 = n(n-1)/2 comparaisons, soit une complexité quadratique O(n²). Le parcours unique d'une liste triée est linéaire O(n).

</details>

## B-dictionnaire
### Dictionnaires

**Q1** (1 pt, dictionnaire) Un primeur enregistre ses stocks dans le dictionnaire `stock = {'pomme': 40, 'poire': 12, 'kiwi': 0}`. Proposer des instructions Python permettant d'ajouter 25 bananes, d'augmenter de 10 le stock de poires et de supprimer l'entrée 'kiwi'.

<details><summary>Corrigé</summary>

```python
stock['banane'] = 25
stock['poire'] = stock['poire'] + 10
del stock['kiwi']
```

</details>

**Q2** (1 pt, dictionnaire) Écrire une fonction `frequences` qui prend en paramètre une chaîne de caractères `texte` et renvoie un dictionnaire associant à chaque caractère son nombre d'apparitions. Par exemple `frequences('abba')` renvoie `{'a': 2, 'b': 2}`.

<details><summary>Corrigé</summary>

```python
def frequences(texte):
    d = {}
    for c in texte:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    return d
```

</details>

**Q3** (1 pt, dictionnaire) On donne `notes = {'Ali': 14, 'Bea': 9, 'Chloe': 17, 'Dan': 9}` et le code :
```python
res = [k for k in notes if notes[k] >= 10]
```
Donner la valeur de `res`, puis déterminer la valeur de `len(notes)` et de `notes.get('Eva', 0)`.

<details><summary>Corrigé</summary>

res = ['Ali', 'Chloe'] ; len(notes) = 4 ; notes.get('Eva', 0) = 0.

</details>

**Q4** (1 pt, dictionnaire) On dispose de la fonction `frequences(texte)` de la question précédente, qui renvoie un dictionnaire associant à chaque caractère son nombre d'apparitions. En déduire une fonction `plus_frequent(texte)` qui renvoie le caractère le plus fréquent d'une chaîne non vide.

<details><summary>Corrigé</summary>

```python
def plus_frequent(texte):
    d = frequences(texte)
    meilleur = None
    for c in d:
        if meilleur is None or d[c] > d[meilleur]:
            meilleur = c
    return meilleur
```

</details>

## B-diviser_regner
### Diviser pour régner

**Q1** (1 pt, diviser_regner) On considère la fonction interclasser qui fusionne deux listes triées L1 et L2 en une liste triée.

```python
1 def interclasser(L1, L2):
2     res = []
3     i1, i2 = 0, 0
4     while i1 < len(L1) and i2 < len(L2):
5         if L1[i1] <= L2[i2]:
6             res.append(L1[i1])
7             i1 = i1 + 1
8         else:
9             ...
10            ...
11    while i1 < len(L1):
12        res.append(L1[i1])
13        i1 = i1 + 1
14    while ...:
15        ...
16        ...
17    return res
```

Recopier et compléter les lignes 9, 10, 14, 15 et 16.

<details><summary>Corrigé</summary>

9: res.append(L2[i2])
10: i2 = i2 + 1
14: while i2 < len(L2):
15: res.append(L2[i2])
16: i2 = i2 + 1

</details>

**Q2** (1 pt, diviser_regner) On applique le tri fusion à la liste [7, 3, 9, 1]. Parmi les propositions suivantes, une seule décrit correctement l'étape qui précède immédiatement la dernière fusion. Indiquer laquelle et expliquer.

A. [3, 7] et [1, 9]
B. [7, 3] et [9, 1]
C. [1, 3] et [7, 9]
D. [3] et [1, 7, 9]

<details><summary>Corrigé</summary>

A : la liste est coupée en deux moitiés [7, 3] et [9, 1], chacune triée récursivement en [3, 7] et [1, 9], puis ces deux moitiés triées sont interclassées pour donner [1, 3, 7, 9].

</details>

**Q3** (1 pt, diviser_regner) On donne la fonction tri_fusion suivante, qui utilise une fonction interclasser(L1, L2) renvoyant la fusion triée de deux listes triées.

```python
def tri_fusion(L):
    if len(L) <= 1:
        return L
    m = len(L) // 2
    return interclasser(tri_fusion(L[:m]), tri_fusion(L[m:]))
```

Donner le nombre total d'appels à tri_fusion (appel initial compris) lors de l'exécution de tri_fusion([5, 2, 8, 6]).

<details><summary>Corrigé</summary>

7 appels : 1 sur la liste de 4 éléments, 2 sur les listes de 2 éléments, 4 sur les listes d'un élément.

</details>

## B-donnees_tables
### Données en tables

**Q1** (1 pt, donnees_tables) Une médiathèque représente ses emprunts par une liste de dictionnaires, par exemple :

```python
emprunts = [{'titre': 'Dune', 'lecteur': 'Ali', 'jours': 12},
            {'titre': 'Ubik', 'lecteur': 'Zoé', 'jours': 30}]
```

Écrire une fonction en_retard qui prend en paramètre une telle liste et un entier duree_max, et qui renvoie la liste des titres dont la valeur associée à 'jours' est strictement supérieure à duree_max.

<details><summary>Corrigé</summary>

```python
def en_retard(emprunts, duree_max):
    res = []
    for e in emprunts:
        if e['jours'] > duree_max:
            res.append(e['titre'])
    return res
```

</details>

**Q2** (1 pt, donnees_tables) On considère la table suivante, stockée dans la variable releves (liste de dictionnaires) :

| ville | temp |
|---|---|
| Lyon | 14 |
| Brest | 11 |
| Nice | 19 |
| Lille | 9 |

Donner la valeur de l'expression `[r['ville'] for r in releves if r['temp'] >= 11]`.

<details><summary>Corrigé</summary>

['Lyon', 'Brest', 'Nice']

</details>

**Q3** (1 pt, donnees_tables) Pour trier une table de 10 000 élèves (liste de dictionnaires) selon la clé 'moyenne', un élève propose d'écrire son propre tri par sélection ; un autre propose `sorted(eleves, key=lambda e: e['moyenne'])`. Justifier quel choix est préférable.

<details><summary>Corrigé</summary>

sorted est préférable : il est déjà testé, plus court, et son coût est en O(n log n), alors que le tri par sélection est quadratique (O(n²)), soit environ 10^8 comparaisons pour 10 000 lignes.

</details>

## B-file
### Files

**Q1** (1 pt, file) Une file f contient des entiers. Recopier et compléter la fonction compter_pairs qui renvoie le nombre d'entiers pairs contenus dans f ; à la fin, f doit être vide.

```python
1 def compter_pairs(f):
2     n = 0
3     while ...:
4         x = ...
5         if ...:
6             n = n + 1
7     return n
```

<details><summary>Corrigé</summary>

```python
def compter_pairs(f):
    n = 0
    while not f.est_vide():
        x = f.defiler()
        if x % 2 == 0:
            n = n + 1
    return n
```

</details>

**Q2** (1 pt, file) Partant d'une file vide, on exécute : enfiler(4), enfiler(8), defiler(), enfiler(1), enfiler(6), defiler(). Donner le contenu de la file (de la tête vers la queue) et les valeurs renvoyées par les deux appels à defiler.

<details><summary>Corrigé</summary>

defiler renvoie 4 puis 8 ; la file contient 1 puis 6 (tête : 1).

</details>

**Q3** (1 pt, file) Une imprimante reçoit des travaux dans une file ; chaque travail est un entier représentant sa durée d'impression en secondes. Recopier et compléter la fonction duree_totale qui vide la file et renvoie la durée totale d'impression.

```python
1 def duree_totale(file_travaux):
2     t = 0
3     while ...:
4         t = ...
5     return t
```

<details><summary>Corrigé</summary>

```python
def duree_totale(file_travaux):
    t = 0
    while not file_travaux.est_vide():
        t = t + file_travaux.defiler()
    return t
```

</details>

## B-fonctions
### Fonctions

**Q1** (1 pt, fonctions) Écrire une fonction inverser_mots qui prend en paramètre une liste de chaînes de caractères et qui renvoie une nouvelle liste contenant les mêmes chaînes dans l'ordre inverse, sans utiliser reverse ni de tranche. Exemple : inverser_mots(['a', 'b', 'c']) renvoie ['c', 'b', 'a'].

<details><summary>Corrigé</summary>

```python
def inverser_mots(lst):
    res = []
    for i in range(len(lst) - 1, -1, -1):
        res.append(lst[i])
    return res
```

</details>

**Q2** (1 pt, fonctions) La liste etapes contient les distances en km parcourues chaque jour par un randonneur. Compléter la fonction distance_max qui renvoie la plus grande distance de la liste (supposée non vide).

```python
1 def distance_max(etapes):
2     m = ...
3     for i in range(...):
4         if ...:
5             m = etapes[i]
6     return m
```

<details><summary>Corrigé</summary>

```python
def distance_max(etapes):
    m = etapes[0]
    for i in range(1, len(etapes)):
        if etapes[i] > m:
            m = etapes[i]
    return m
```

</details>

**Q3** (1 pt, fonctions) La fonction mots_binaires(n) doit renvoyer la liste de tous les mots de longueur n formés des caractères '0' et '1'. Compléter la ligne 7.

```python
1 def mots_binaires(n):
2     if n == 0:
3         return ['']
4     res = []
5     for m in mots_binaires(n - 1):
6         for c in '01':
7             res = ...
8     return res
```

<details><summary>Corrigé</summary>

Ligne 7 : res = res + [m + c]

</details>

**Q4** (1 pt, fonctions) On considère la fonction suivante :

```python
def coder(mot):
    res = ''
    for c in mot:
        if c in 'aeiou':
            res = c + res
        else:
            res = res + c
    return res
```

Quel est le résultat de l'appel coder('route') ?

<details><summary>Corrigé</summary>

'euort' : étapes 'r', 'or', 'uor', 'uort', 'euort'.

</details>

## B-glouton
### Algorithmes gloutons

**Q1** (1 pt, glouton) On veut rendre la somme somme avec le moins de pièces possible, la liste pieces étant triée dans l'ordre décroissant (par exemple [10, 5, 2, 1]). Recopier et compléter les lignes 4 et 6 de la fonction gloutonne suivante qui renvoie la liste des pièces rendues.

```python
1 def rendu(pieces, somme):
2     res = []
3     i = 0
4     while ...:
5         if pieces[i] <= somme:
6             ...
7             somme = somme - pieces[i]
8         else:
9             i = i + 1
10    return res
```

<details><summary>Corrigé</summary>

Ligne 4 : while somme > 0:
Ligne 6 : res.append(pieces[i])

</details>

**Q2** (1 pt, glouton) Un camion de capacité cap (en kg) doit transporter des colis dont les masses sont données dans une liste masses. Écrire une fonction charger qui prend en paramètres masses et cap et qui applique la stratégie gloutonne suivante : on considère les colis du plus lourd au plus léger et on prend chaque colis s'il tient encore dans le camion. La fonction renvoie la liste des masses chargées.

<details><summary>Corrigé</summary>

```python
def charger(masses, cap):
    res = []
    for m in sorted(masses, reverse=True):
        if m <= cap:
            res.append(m)
            cap = cap - m
    return res
```

</details>

**Q3** (1 pt, glouton) Dans la fonction charger précédente, on trie d'abord les n masses puis on les parcourt une fois. Préciser le coût en temps dans le pire des cas de cette fonction en fonction de n, si le tri utilisé est le tri fusion, et justifier.

<details><summary>Corrigé</summary>

Quasi-linéaire, en O(n log n) : le tri fusion coûte O(n log n) et le parcours O(n), le tri domine.

</details>

## B-graphe
### Graphes

**Q1** (1 pt, graphe) On considère le graphe g = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']} et la fonction :

```python
def parcours(g, s, vus):
    vus.append(s)
    print(s)
    for v in g[s]:
        if v not in vus:
            parcours(g, v, vus)
```

Déterminer les affichages produits par l'appel parcours(g, 'A', []).

<details><summary>Corrigé</summary>

A, B, D, C, E (un par ligne) : parcours en profondeur.

</details>

**Q2** (1 pt, graphe) Une classe Reseau stocke un graphe dans l'attribut self.adj (dictionnaire de listes d'adjacence). Compléter la méthode suivante à partir de la ligne 6.

```python
1 def degre(self, s):
2     '''
3     Renvoie le nombre de voisins du sommet s.
4     : return (int)
5     '''
6     ...
```

<details><summary>Corrigé</summary>

```python
def degre(self, s):
    return len(self.adj[s])
```

</details>

**Q3** (1 pt, graphe) Un réseau de villes est représenté par un dictionnaire graphe associant à chaque ville la liste de ses voisines directes. Écrire une fonction a_deux_etapes qui prend en paramètres graphe et une ville v, et qui renvoie la liste (sans doublon) des villes situées à exactement deux arêtes de v (ni v, ni ses voisines directes).

<details><summary>Corrigé</summary>

```python
def a_deux_etapes(graphe, v):
    res = []
    for w in graphe[v]:
        for x in graphe[w]:
            if x != v and x not in graphe[v] and x not in res:
                res.append(x)
    return res
```

</details>

**Q4** (1 pt, graphe) On retire la condition `if v not in vus:` de la fonction parcours de la question 1. L'appel parcours(g, 'A', []) ne se termine plus normalement. Donner une explication à ce problème.

<details><summary>Corrigé</summary>

Le graphe contient des cycles (et toute arête est parcourue dans les deux sens) : sans test, A appelle B qui rappelle A, etc. Les appels récursifs sont infinis et Python lève une RecursionError.

</details>

## B-interface_tad
### Interface et types abstraits

**Q1** (1 pt, interface_tad) Une classe Pile est implémentée avec un attribut self.contenu de type list, le sommet étant le dernier élément. Écrire une méthode sommet de la classe Pile qui renvoie l'élément au sommet sans le retirer, et renvoie None si la pile est vide.

<details><summary>Corrigé</summary>

```python
def sommet(self):
    if len(self.contenu) == 0:
        return None
    return self.contenu[-1]
```

</details>

**Q2** (1 pt, interface_tad) On dispose de l'interface d'une file : creer_file(), est_vide(f), enfiler(f, x), defiler(f). En n'utilisant que cette interface, écrire une fonction longueur qui prend en paramètre une file f et renvoie son nombre d'éléments, la file devant retrouver son contenu initial dans le même ordre.

<details><summary>Corrigé</summary>

```python
def longueur(f):
    aux = creer_file()
    n = 0
    while not est_vide(f):
        enfiler(aux, defiler(f))
        n = n + 1
    while not est_vide(aux):
        enfiler(f, defiler(aux))
    return n
```

</details>

**Q3** (1 pt, interface_tad) Un programme utilise une pile uniquement via les fonctions empiler, depiler et est_vide. On change l'implémentation de la pile (liste Python remplacée par une liste chaînée). Expliquer pourquoi le programme n'a pas besoin d'être modifié.

<details><summary>Corrigé</summary>

Le programme ne dépend que de l'interface (les opérations et leur comportement), pas de la représentation interne ; l'interface étant conservée, le changement d'implémentation lui est invisible.

</details>

**Q4** (1 pt, interface_tad) Une base de données contient la relation Livre(id, titre, auteur, annee), id étant une clé primaire entière. Écrire une requête SQL permettant d'ajouter le livre d'identifiant 42, intitulé « Les Furtifs », écrit par Alain Damasio en 2019.

<details><summary>Corrigé</summary>

INSERT INTO Livre (id, titre, auteur, annee) VALUES (42, 'Les Furtifs', 'Alain Damasio', 2019);

</details>

## B-k_ppv
### Banque : k plus proches voisins

**Q1** (1 pt, k_ppv) Une application classe des fruits selon leur masse (en g) et leur diamètre (en cm). Les fruits connus sont : A (150, 7) pomme, B (160, 8) pomme, C (120, 6) citron, D (110, 5) citron, E (170, 7) pomme. On veut classer un nouveau fruit X (130, 6). Les distances euclidiennes de X aux fruits connus sont environ : A : 20,02 ; B : 30,07 ; C : 10,00 ; D : 20,02 ; E : 40,01. Donner les trois plus proches voisins de X, puis la classe attribuée à X par l'algorithme des k plus proches voisins avec k = 3.

<details><summary>Corrigé</summary>

Les trois plus proches voisins sont C (10,00), puis A et D (20,02 à égalité). Parmi eux : 2 citrons (C, D) et 1 pomme (A). X est classé citron.

</details>

**Q2** (1 pt, k_ppv) On applique l'algorithme des k plus proches voisins à un jeu de données de 100 éléments répartis en deux classes. Expliquer pourquoi on choisit généralement une valeur de k impaire, et indiquer ce qui se passe si l'on prend k = 100.

<details><summary>Corrigé</summary>

Avec deux classes, un k impair évite les égalités lors du vote majoritaire. Avec k = 100, tous les éléments sont voisins : le nouvel élément reçoit toujours la classe majoritaire du jeu de données, quelle que soit sa position, ce qui rend la prédiction sans intérêt.

</details>

**Q3** (1 pt, k_ppv) Dans un plan, on considère le point P (2, 3) et le point Q (5, 7). Calculer la distance euclidienne entre P et Q, puis écrire une fonction Python distance(p, q) qui prend deux tuples de coordonnées et renvoie leur distance euclidienne.

<details><summary>Corrigé</summary>

d = racine((5-2)² + (7-3)²) = racine(9 + 16) = 5.

from math import sqrt

def distance(p, q):
    return sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

</details>

## B-liste_chainee
### Banque : listes chaînées

**Q1** (1 pt, liste_chainee) On dispose de la classe Maillon (attributs valeur et suivant). Définir ce qu'est une liste chaînée, puis donner l'instruction permettant de construire la liste chaînée 4 -> 9 -> 2, nommée trajet.

<details><summary>Corrigé</summary>

Une liste chaînée est une suite de maillons, chacun contenant une valeur et un lien vers le maillon suivant (None pour le dernier) ; la liste est repérée par son premier maillon.

trajet = Maillon(4, Maillon(9, Maillon(2, None)))

</details>

**Q2** (1 pt, liste_chainee) On dispose de la classe Maillon (attributs valeur et suivant). Recopier et compléter les lignes 3 à 6 de la fonction somme qui renvoie la somme des valeurs d'une liste chaînée (None désigne la liste vide).

1 def somme(lst):
2     total = 0
3     m = ...
4     while ...:
5         total = ...
6         m = ...
7     return total

<details><summary>Corrigé</summary>

def somme(lst):
    total = 0
    m = lst
    while m is not None:
        total = total + m.valeur
        m = m.suivant
    return total

</details>

**Q3** (1 pt, liste_chainee) On dispose de la classe Maillon (attributs valeur et suivant) et de la liste chaînée trajet = Maillon(4, Maillon(9, Maillon(2, None))). Donner une instruction permettant de transformer trajet en la liste chaînée 4 -> 2, en supprimant le maillon de valeur 9.

<details><summary>Corrigé</summary>

trajet.suivant = trajet.suivant.suivant

</details>

## B-matrice
### Banque : matrices (listes de listes)

**Q1** (1 pt, matrice) Un graphe orienté à n sommets est représenté par sa matrice d'adjacence m (m[i][j] vaut 1 s'il existe un arc de i vers j, 0 sinon). Recopier et compléter la fonction nb_successeurs(m, i) qui renvoie le nombre de successeurs du sommet i.

1 def nb_successeurs(m, i):
2     nb = 0
3     for j in range(...):
4         if ...:
5             nb = ...
6     return nb

<details><summary>Corrigé</summary>

def nb_successeurs(m, i):
    nb = 0
    for j in range(len(m)):
        if m[i][j] == 1:
            nb = nb + 1
    return nb

</details>

**Q2** (1 pt, matrice) Une salle de cinéma est représentée par une matrice salle de booléens : salle[r][p] vaut True si la place p du rang r est occupée. Recopier et compléter les lignes 4 à 6 de la fonction places_libres(salle) qui renvoie le nombre total de places libres.

1 def places_libres(salle):
2     libres = 0
3     for r in range(len(salle)):
4         for p in ...:
5             if ...:
6                 libres = ...
7     return libres

<details><summary>Corrigé</summary>

def places_libres(salle):
    libres = 0
    for r in range(len(salle)):
        for p in range(len(salle[r])):
            if not salle[r][p]:
                libres = libres + 1
    return libres

</details>

**Q3** (1 pt, matrice) On considère la matrice suivante :

grille = [[3, 8, 1], [5, 0, 7], [2, 6, 4]]

Donner la valeur de grille[1][2], puis celle de grille[2][0] + grille[0][1].

<details><summary>Corrigé</summary>

grille[1][2] vaut 7 ; grille[2][0] + grille[0][1] = 2 + 8 = 10.

</details>

## B-mise_au_point
### Banque : mise au point des programmes

**Q1** (1 pt, mise_au_point) On souhaite calculer la moyenne des notes d'une liste. On exécute :

1 def moyenne(notes):
2     s = 0
3     for n in notes:
4         s = s + n
5     return s / len(notes)

>>> moyenne([])
ZeroDivisionError: division by zero

Expliquer ce qui a provoqué cette erreur et proposer une correction.

<details><summary>Corrigé</summary>

La liste est vide : len(notes) vaut 0, d'où une division par zéro ligne 5. Correction : ajouter au début une précondition, par exemple assert len(notes) > 0, "liste vide" (ou renvoyer None si la liste est vide).

</details>

**Q2** (1 pt, mise_au_point) On veut tester la fonction est_pair(n) qui renvoie True si l'entier n est pair, False sinon. Recopier et compléter les lignes 2 à 4 de la fonction de test suivante avec des assertions portant sur 0, 7 et -4.

1 def test_est_pair():
2     assert ...
3     assert ...
4     assert ...
5     print("tests réussis")

<details><summary>Corrigé</summary>

def test_est_pair():
    assert est_pair(0) == True
    assert est_pair(7) == False
    assert est_pair(-4) == True
    print("tests réussis")

</details>

**Q3** (1 pt, mise_au_point) On considère la fonction suivante, où n est un entier strictement positif :

def nb_chiffres(n):
    c = 0
    while n > 0:
        n = n // 10
        c = c + 1
    return c

Justifier que la boucle de cette fonction se termine.

<details><summary>Corrigé</summary>

n est un entier positif qui décroît strictement à chaque tour (n // 10 < n pour n > 0) : c'est un variant de boucle. Une suite d'entiers positifs strictement décroissante ne peut être infinie, donc n finit par valoir 0 et la condition n > 0 devient fausse.

</details>

## B-modele_relationnel
### Banque : modèle relationnel

**Q1** (1 pt, modele_relationnel) Une médiathèque utilise la relation Film(id_film, titre, annee, duree). En voici un extrait :

| id_film | titre | annee | duree |
|---|---|---|---|
| 1 | Orage | 1998 | 112 |
| 2 | Le Phare | 2005 | 95 |
| 3 | Minuit | 2012 | 130 |
| 4 | Sable | 2001 | 88 |

Donner le résultat de la requête : SELECT titre FROM Film WHERE annee > 2000 AND duree < 100

<details><summary>Corrigé</summary>

Le Phare et Sable.

</details>

**Q2** (1 pt, modele_relationnel) Dans une base de données d'une école, la relation Eleve possède un attribut code_postal. Indiquer quel domaine (type) il faut choisir pour cet attribut et expliquer pourquoi.

<details><summary>Corrigé</summary>

Une chaîne de caractères (TEXT/VARCHAR) : un entier supprimerait le zéro initial (01200 deviendrait 1200), et on ne fait aucun calcul sur un code postal.

</details>

**Q3** (1 pt, modele_relationnel) On considère les relations Adherent(id_adherent, nom, prenom) et Emprunt(id_emprunt, #id_adherent, date_emprunt). Indiquer ce qui différencie la clé primaire id_adherent de Adherent et la clé étrangère id_adherent de Emprunt, puis expliquer ce qui se passe si l'on insère un emprunt avec un id_adherent inexistant.

<details><summary>Corrigé</summary>

La clé primaire identifie de façon unique chaque adhérent (contrainte d'entité). La clé étrangère de Emprunt fait référence à une clé primaire d'Adherent et peut apparaître plusieurs fois. Insérer un id_adherent inexistant viole la contrainte de référence : le SGBD refuse l'insertion.

</details>

**Q4** (1 pt, modele_relationnel) Un club de randonnée enregistre ses sorties dans la relation Sortie(date, lieu, guide, distance_km). Un même guide peut encadrer plusieurs sorties, et plusieurs sorties peuvent avoir lieu le même jour. Lister les attributs de Sortie en précisant leur domaine, expliquer pourquoi aucun attribut seul ne peut être clé primaire, et proposer une solution.

<details><summary>Corrigé</summary>

date : DATE ; lieu : TEXT ; guide : TEXT ; distance_km : FLOAT (ou REAL). Ni date, ni guide, ni lieu, ni distance ne sont uniques. On ajoute un attribut artificiel id_sortie (INT), clé primaire.

</details>

## B-modularite
### Banque : modularité

**Q1** (1 pt, modularite) Une application de location de vélos utilise la classe suivante, définie dans le module location.py :

class Location:
    def __init__(self, client, velo, duree):
        self.client = client
        self.velo = velo
        self.duree = duree

Écrire les instructions, dans un autre fichier, qui importent la classe Location puis créent la location loc1 du vélo numéro 12 par la cliente Inès Martin pour une durée de 90 minutes.

<details><summary>Corrigé</summary>

from location import Location
loc1 = Location("Inès Martin", 12, 90)

</details>

**Q2** (1 pt, modularite) On souhaite simuler le lancer de n dés à six faces à l'aide de la fonction randint du module random (randint(a, b) renvoie un entier aléatoire entre a et b inclus). Recopier et compléter le code suivant.

1 from ... import ...
2 def lancers(n):
3     resultats = []
4     for i in range(n):
5         resultats.append(...)
6     return resultats

<details><summary>Corrigé</summary>

from random import randint
def lancers(n):
    resultats = []
    for i in range(n):
        resultats.append(randint(1, 6))
    return resultats

</details>

**Q3** (1 pt, modularite) Le module math fournit la fonction gcd(a, b) qui renvoie le PGCD de deux entiers. Pour un chiffrement affine, la clé a doit être première avec 26. Recopier et compléter les lignes 1 et 4 à 6 de la fonction cles_valides() qui renvoie la liste des entiers a entre 1 et 25 premiers avec 26.

1 from ... import ...
2 def cles_valides():
3     res = []
4     for a in range(...):
5         if ...:
6             ...
7     return res

<details><summary>Corrigé</summary>

from math import gcd
def cles_valides():
    res = []
    for a in range(1, 26):
        if gcd(a, 26) == 1:
            res.append(a)
    return res

</details>

## B-os_commandes
### Banque : commandes du système d'exploitation

**Q1** (1 pt, os_commandes) Sous Linux, l'utilisateur se trouve dans /home/lea, qui contient le dossier photos. Il exécute successivement : mkdir photos/ete, cd photos/ete, pwd. Indiquer ce qu'affiche la dernière commande.

<details><summary>Corrigé</summary>

/home/lea/photos/ete

</details>

**Q2** (1 pt, os_commandes) La commande ls -l affiche la ligne suivante : -rwxr-x--- 1 lea profs 2048 rapport.sh. Expliquer les droits dont disposent sur ce fichier le propriétaire, les membres du groupe et les autres utilisateurs.

<details><summary>Corrigé</summary>

Propriétaire lea : lecture, écriture, exécution (rwx). Groupe profs : lecture et exécution (r-x). Autres : aucun droit (---).

</details>

**Q3** (1 pt, os_commandes) Dans le dossier /home/lea, le fichier notes.txt est actuellement lisible et modifiable par tous. Proposer une suite de commandes Linux permettant de créer un dossier archives, d'y copier notes.txt, puis de faire en sorte que la copie ne soit lisible et modifiable que par son propriétaire.

<details><summary>Corrigé</summary>

mkdir archives
cp notes.txt archives/
chmod 600 archives/notes.txt   (ou chmod u=rw,go= archives/notes.txt)

</details>

**Q4** (1 pt, os_commandes) L'utilisateur se trouve dans le répertoire /home/lea/photos/ete. Donner le répertoire courant après chacune des commandes suivantes, exécutées successivement :
a) cd ..
b) cd ../..
c) cd ~

<details><summary>Corrigé</summary>

a) /home/lea/photos
b) /home
c) /home/lea

</details>

## B-paradigmes
### Paradigmes de programmation : diviser pour régner

**Q1** (1 pt, paradigmes) Une station météo enregistre des températures dans une liste Python non vide de nombres. On souhaite déterminer la température maximale selon la méthode « diviser pour régner ».

Écrire une fonction récursive `maximum(tab, debut, fin)` qui prend en paramètres une liste `tab` et deux indices `debut` et `fin` (avec `debut <= fin`) et qui renvoie la plus grande valeur de `tab` entre les indices `debut` et `fin` inclus, en découpant la portion en deux moitiés.

<details><summary>Corrigé</summary>

```python
def maximum(tab, debut, fin):
    if debut == fin:
        return tab[debut]
    milieu = (debut + fin) // 2
    m1 = maximum(tab, debut, milieu)
    m2 = maximum(tab, milieu + 1, fin)
    if m1 > m2:
        return m1
    return m2
```

</details>

**Q2** (1 pt, paradigmes) On recherche un livre par son numéro dans le catalogue trié d'une médiathèque contenant n livres, en utilisant la recherche dichotomique : à chaque étape, on compare le numéro cherché à celui du milieu de la zone restante, puis on ne conserve qu'une moitié.

Quel est l'ordre de grandeur de la complexité en temps de cette recherche dans le pire des cas ? Justifier, puis donner le nombre maximal de comparaisons pour un catalogue de 1 000 000 de livres.

<details><summary>Corrigé</summary>

La taille de la zone est divisée par 2 à chaque étape : il faut environ log2(n) étapes, la complexité est logarithmique, en O(log n). Pour n = 1 000 000, environ 20 comparaisons (2^20 ≈ 1 048 576).

</details>

**Q3** (1 pt, paradigmes) Le tri fusion repose sur une fonction `fusion` qui prend deux listes triées et renvoie une nouvelle liste triée contenant tous leurs éléments.

Recopier et compléter les lignes 6, 7 et 11 de la fonction suivante.

```python
1 def fusion(l1, l2):
2     resultat = []
3     i, j = 0, 0
4     while i < len(l1) and j < len(l2):
5         if l1[i] <= l2[j]:
6             ...
7             ...
8         else:
9             resultat.append(l2[j])
10            j = j + 1
11    return resultat + ... + ...
```

<details><summary>Corrigé</summary>

```python
def fusion(l1, l2):
    resultat = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            resultat.append(l1[i])
            i = i + 1
        else:
            resultat.append(l2[j])
            j = j + 1
    return resultat + l1[i:] + l2[j:]
```

</details>

## B-parcours_arbre
### Parcours d'arbres binaires

**Q1** (1 pt, parcours_arbre) On considère l'arbre binaire suivant, dont la racine est M : M a pour fils gauche D et pour fils droit S ; D a pour fils gauche B et pour fils droit G ; S a pour fils droit V ; B, G et V sont des feuilles.

On rappelle qu'un parcours infixe depuis un nœud consiste, dans l'ordre, à faire un parcours infixe du sous-arbre gauche, à afficher le nœud, puis à faire un parcours infixe du sous-arbre droit.

Donner la liste des nœuds dans l'ordre du parcours infixe, puis dans l'ordre du parcours préfixe.

<details><summary>Corrigé</summary>

Infixe : B, D, G, M, S, V.
Préfixe : M, D, B, G, S, V.

</details>

**Q2** (1 pt, parcours_arbre) L'expression arithmétique (8 - 3) * (4 + 6) est représentée par un arbre binaire dont la racine est `*`, de fils gauche `-` (fils 8 et 3) et de fils droit `+` (fils 4 et 6).

Indiquer, parmi les parcours en largeur, préfixe, infixe et postfixe, celui qui donne la notation polonaise inverse (NPI) de l'expression, écrire cette notation, puis calculer la valeur de l'expression.

<details><summary>Corrigé</summary>

Le parcours postfixe : 8 3 - 4 6 + *. Valeur : 5 × 10 = 50.

</details>

**Q3** (1 pt, parcours_arbre) Dans un arbre généalogique représenté par un arbre binaire, on cherche un ancêtre dont le nom est donné et l'on souhaite trouver celui qui est le plus proche de la racine (le moins de générations possible).

Expliquer pourquoi un parcours en largeur est plus adapté qu'un parcours en profondeur pour cette recherche.

<details><summary>Corrigé</summary>

Le parcours en largeur visite les nœuds étage par étage, par profondeur croissante : le premier nœud trouvé portant ce nom est donc à la profondeur minimale, et on peut s'arrêter. Un parcours en profondeur peut explorer tout un sous-arbre profond et trouver d'abord une occurrence plus éloignée de la racine, ce qui oblige à tout parcourir pour garantir le minimum.

</details>

## B-parcours_graphe
### Parcours de graphes

**Q1** (1 pt, parcours_graphe) Un réseau de pistes cyclables est représenté par un dictionnaire Python `g` qui associe à chaque carrefour la liste de ses voisins. Par exemple :

```python
g = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}
```

Écrire une fonction `parcours_profondeur(g, s)` qui prend en paramètres un graphe `g` et un sommet `s` et qui renvoie la liste des sommets dans l'ordre de leur visite lors d'un parcours en profondeur depuis `s` (les voisins sont examinés dans l'ordre de la liste).

<details><summary>Corrigé</summary>

```python
def parcours_profondeur(g, s, visites=None):
    if visites is None:
        visites = []
    visites.append(s)
    for v in g[s]:
        if v not in visites:
            parcours_profondeur(g, v, visites)
    return visites
```
Pour l'exemple depuis 'A' : ['A', 'B', 'D', 'C', 'E'].

</details>

**Q2** (1 pt, parcours_graphe) Un robot se déplace dans un entrepôt modélisé par un graphe non orienté de sommets E (entrée), R1, R2, R3 et S (sortie), dont les arêtes sont : E-R1, E-R2, R1-R2, R1-S, R2-R3, R3-S.

Donner la liste de tous les chemins élémentaires (sans passer deux fois par le même sommet) allant de E à S.

<details><summary>Corrigé</summary>

E-R1-S ; E-R1-R2-R3-S ; E-R2-R3-S ; E-R2-R1-S (4 chemins).

</details>

**Q3** (1 pt, parcours_graphe) On considère le graphe non orienté de sommets 1, 2, 3, 4, 5, 6 et d'arêtes : 1-2, 1-3, 2-4, 3-4, 4-5, 5-6.

Déterminer l'ordre de visite des sommets lors d'un parcours en largeur depuis le sommet 1 (voisins traités par ordre croissant), puis la distance (en nombre d'arêtes) entre 1 et 6.

<details><summary>Corrigé</summary>

Ordre : 1, 2, 3, 4, 5, 6. Distance de 1 à 6 : 4 (par exemple 1-2-4-5-6).

</details>

**Q4** (1 pt, parcours_graphe) Un graphe est représenté par un dictionnaire de listes d'adjacence. Recopier et compléter les lignes 5, 7 et 9 de la fonction suivante, qui renvoie la liste des sommets dans l'ordre d'un parcours en largeur depuis `depart`.

```python
1 def parcours_largeur(g, depart):
2     visites = [depart]
3     file = [depart]
4     while len(file) > 0:
5         s = ...
6         for v in g[s]:
7             if ...:
8                 visites.append(v)
9                 ...
10    return visites
```

<details><summary>Corrigé</summary>

```python
def parcours_largeur(g, depart):
    visites = [depart]
    file = [depart]
    while len(file) > 0:
        s = file.pop(0)
        for v in g[s]:
            if v not in visites:
                visites.append(v)
                file.append(v)
    return visites
```

</details>

## B-pile
### Les piles

**Q1** (1 pt, pile) Une pile est implémentée par une liste Python dont le sommet est le dernier élément ; `p.append(x)` empile x et `p.pop()` dépile et renvoie le sommet. On considère le programme :

```python
p = []
for x in [4, 7, 2, 9]:
    p.append(x)
a = p.pop()
b = p.pop()
p.append(a + b)
c = p.pop()
```

Donner le contenu de `p` ainsi que les valeurs de `a`, `b` et `c` après exécution de ce programme.

<details><summary>Corrigé</summary>

a = 9, b = 2, c = 11 et p = [4, 7].

</details>

**Q2** (1 pt, pile) On dispose d'une classe `Pile` munie des méthodes `est_vide()`, `empiler(x)` et `depiler()` (qui renvoie l'élément retiré), ainsi que d'un constructeur `Pile()` créant une pile vide.

Écrire une fonction `inverser(p)` qui prend en paramètre une pile `p` et qui renvoie une nouvelle pile contenant les mêmes éléments dans l'ordre inverse (l'ancien sommet se retrouve au fond). La pile `p` peut être vide après l'appel.

<details><summary>Corrigé</summary>

```python
def inverser(p):
    q = Pile()
    while not p.est_vide():
        q.empiler(p.depiler())
    return q
```

</details>

**Q3** (1 pt, pile) Un navigateur web mémorise les pages visitées afin de permettre le retour en arrière avec le bouton « Précédent ».

Rappeler le principe de fonctionnement d'une pile et expliquer pourquoi cette structure convient à l'historique du bouton « Précédent ».

<details><summary>Corrigé</summary>

Une pile fonctionne selon le principe LIFO (dernier arrivé, premier sorti) : on n'accède qu'au sommet, on empile et dépile au sommet. Le bouton « Précédent » doit ramener à la dernière page visitée, c'est-à-dire la dernière empilée : une pile convient donc.

</details>

## B-poo
### Programmation orientée objet

**Q1** (1 pt, poo) Une ludothèque gère ses jeux grâce à une classe `Jeu`. Un jeu possède un titre (chaîne), un nombre minimal de joueurs, un nombre maximal de joueurs et un attribut `disponible` qui vaut `True` à la création.

Recopier et compléter le code du constructeur de la classe `Jeu`.

```python
class Jeu:
    def __init__(self, titre, nb_min, nb_max):
        ...
```

<details><summary>Corrigé</summary>

```python
class Jeu:
    def __init__(self, titre, nb_min, nb_max):
        self.titre = titre
        self.nb_min = nb_min
        self.nb_max = nb_max
        self.disponible = True
```

</details>

**Q2** (1 pt, poo) Un arbre binaire est implémenté par la classe suivante, où un arbre vide est représenté par `None` :

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

a = Noeud(5, Noeud(3, Noeud(1)), Noeud(8, None, Noeud(9, Noeud(7))))
```

Donner la taille et la hauteur de l'arbre `a`. On considère que la hauteur d'un arbre réduit à un seul nœud vaut 1.

<details><summary>Corrigé</summary>

Taille : 6 nœuds (5, 3, 1, 8, 9, 7). Hauteur : 4 (chemin 5-8-9-7).

</details>

**Q3** (1 pt, poo) On définit la classe suivante pour un compte de cantine :

```python
class Compte:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

    def payer(self, montant):
        if montant <= self.solde:
            self.solde = self.solde - montant
            return True
        return False

    def crediter(self, montant):
        self.solde = self.solde + montant
```

On exécute : `c = Compte('Lina', 10)`, puis `c.payer(4)`, `c.payer(8)`, `c.crediter(5)`, `c.payer(8)`.

Recopier et compléter le tableau ci-dessous en ajoutant autant de lignes que nécessaire.

| Instruction | Valeur renvoyée | c.solde |
|---|---|---|
| c = Compte('Lina', 10) | — | 10 |

<details><summary>Corrigé</summary>

| Instruction | Valeur renvoyée | c.solde |
|---|---|---|
| c = Compte('Lina', 10) | — | 10 |
| c.payer(4) | True | 6 |
| c.payer(8) | False | 6 |
| c.crediter(5) | None | 11 |
| c.payer(8) | True | 3 |

</details>

**Q4** (1 pt, poo) On reprend une classe `Jeu` possédant les attributs `titre`, `nb_min`, `nb_max` et `disponible`.

Proposer une méthode `convient(self, n)` de la classe `Jeu` permettant de savoir si le jeu est disponible et jouable par un groupe de `n` joueurs, puis écrire une fonction `jeux_possibles(liste_jeux, n)` qui renvoie la liste des titres des jeux de `liste_jeux` qui conviennent à `n` joueurs.

<details><summary>Corrigé</summary>

```python
class Jeu:
    def __init__(self, titre, nb_min, nb_max):
        self.titre = titre
        self.nb_min = nb_min
        self.nb_max = nb_max
        self.disponible = True

    def convient(self, n):
        return self.disponible and self.nb_min <= n <= self.nb_max

def jeux_possibles(liste_jeux, n):
    return [j.titre for j in liste_jeux if j.convient(n)]
```

</details>

## B-processus
### Gestion des processus

**Q1** (1 pt, processus) Dans un système d'exploitation, un processus peut être dans l'état « prêt », « élu » ou « bloqué ».

Parmi les propositions ci-dessous, laquelle décrit correctement la situation d'un processus qui attend la fin d'une lecture sur le disque ?

a. Il est élu : il occupe le processeur pendant la lecture.
b. Il est prêt : il attend que l'ordonnanceur lui attribue le processeur.
c. Il est bloqué : il attend une ressource et ne peut pas être élu.
d. Il est terminé : le système le relancera plus tard.

<details><summary>Corrigé</summary>

Réponse c : le processus est bloqué en attente de la ressource ; une fois la lecture terminée, il repasse à l'état prêt.

</details>

**Q2** (1 pt, processus) On simule un ordonnancement de type « tourniquet » (Round Robin). Chaque processus est représenté par un couple `(pid, duree_restante)` et la liste d'attente est une liste Python dont le premier élément est le prochain processus élu. Le quantum vaut 2 unités de temps.

Recopier et compléter les lignes 5, 7 et 9 de la fonction suivante, qui renvoie la liste des PID dans l'ordre de leur terminaison.

```python
1 def tourniquet(attente):
2     termines = []
3     while len(attente) > 0:
4         pid, duree = attente.pop(0)
5         duree = ...
6         if duree > 0:
7             ...
8         else:
9             ...
10    return termines
```

<details><summary>Corrigé</summary>

```python
def tourniquet(attente):
    termines = []
    while len(attente) > 0:
        pid, duree = attente.pop(0)
        duree = duree - 2
        if duree > 0:
            attente.append((pid, duree))
        else:
            termines.append(pid)
    return termines
```

</details>

**Q3** (1 pt, processus) On considère deux ressources R1 et R2 et deux processus P1 et P2 dont les instructions sont :

| P1 | P2 |
|---|---|
| Demande R1 | Demande R2 |
| Demande R2 | Demande R1 |
| Libère R2 | Libère R1 |
| Libère R1 | Libère R2 |

L'ordonnanceur exécute d'abord la première instruction de P1, puis la première de P2, et ainsi de suite en alternance. Expliquer pourquoi cette exécution conduit à une situation d'interblocage, puis proposer une modification des programmes qui l'évite.

<details><summary>Corrigé</summary>

P1 obtient R1 puis P2 obtient R2. P1 demande ensuite R2 (détenue par P2) et se bloque ; P2 demande R1 (détenue par P1) et se bloque. Chacun attend une ressource détenue par l'autre : attente circulaire, interblocage. Solution : faire demander les ressources dans le même ordre (R1 puis R2) par les deux processus.

</details>

## B-prog_dynamique
### Programmation dynamique

**Q1** (1 pt, prog_dynamique) Un escalier comporte n marches ; on peut monter 1 ou 2 marches à chaque pas. On note `nb(n)` le nombre de façons différentes de monter les n marches, avec `nb(1) = 1` et `nb(2) = 2`, et pour n ≥ 3 : `nb(n) = nb(n-1) + nb(n-2)`.

Déterminer `nb(6)` en construisant le tableau des valeurs de `nb(1)` à `nb(6)`.

<details><summary>Corrigé</summary>

nb(1)=1, nb(2)=2, nb(3)=3, nb(4)=5, nb(5)=8, nb(6)=13.

</details>

**Q2** (1 pt, prog_dynamique) On reprend le problème de l'escalier : `nb(n) = nb(n-1) + nb(n-2)` avec `nb(1) = 1` et `nb(2) = 2`. Dans la version récursive naïve, le calcul de `nb(5)` provoque plusieurs appels identiques.

Donner l'ordre dans lequel les valeurs doivent être calculées dans une version ascendante (itérative) par programmation dynamique, et expliquer pourquoi cet ordre évite les calculs redondants.

<details><summary>Corrigé</summary>

On calcule nb(1), nb(2), puis nb(3), nb(4), …, nb(n) par indices croissants, en stockant chaque résultat dans un tableau. Chaque valeur ne dépend que de deux valeurs déjà calculées et stockées : chaque sous-problème est résolu une seule fois (complexité linéaire au lieu d'exponentielle).

</details>

**Q3** (1 pt, prog_dynamique) Définir ce qu'est la programmation dynamique et citer le nom de la technique qui consiste à mémoriser, dans une version récursive, les résultats déjà calculés.

<details><summary>Corrigé</summary>

La programmation dynamique est une méthode de résolution qui décompose un problème en sous-problèmes qui se chevauchent, résout chacun une seule fois et stocke leurs résultats pour les réutiliser. En version récursive, cette technique s'appelle la mémoïsation.

</details>

## B-recherche_dichotomique
### Recherche dichotomique

**Q1** (1 pt, recherche_dichotomique) Une médiathèque range les numéros de ses ouvrages dans le tableau trié t = [3, 8, 11, 15, 19, 24, 30, 37, 42]. On recherche la valeur 37 avec l'algorithme de recherche dichotomique suivant :

```python
1 def dichotomie(t, v):
2     debut = 0
3     fin = len(t) - 1
4     while debut <= fin:
5         milieu = (debut + fin) // 2
6         if t[milieu] == v:
7             return True
8         elif t[milieu] < v:
9             debut = milieu + 1
10        else:
11            fin = milieu - 1
12    return False
```

Énumérer dans l'ordre tous les indices milieu calculés lors de l'appel dichotomie(t, 37), ainsi que les valeurs t[milieu] correspondantes.

<details><summary>Corrigé</summary>

milieu = 4 (t[4] = 19), puis milieu = 6 (t[6] = 30), puis milieu = 7 (t[7] = 37) : la valeur est trouvée, la fonction renvoie True.

</details>

**Q2** (1 pt, recherche_dichotomique) Une base de données contient la table coureur(id, nom, temps) où temps est un temps de course en secondes. On extrait :

| id | nom | temps |
|----|-----|-------|
| 1 | Lina | 212 |
| 2 | Hugo | 198 |
| 3 | Sami | 245 |
| 4 | Zoé | 187 |
| 5 | Noé | 230 |

Donner le résultat de la requête suivante appliquée à cet extrait :

SELECT temps FROM coureur WHERE temps > 190 ORDER BY temps

puis indiquer le nombre de comparaisons avec t[milieu] effectuées par une recherche dichotomique de la valeur 230 dans le tableau Python obtenu (même algorithme qu'usuellement, milieu = (debut + fin) // 2).

<details><summary>Corrigé</summary>

Résultat : 198, 212, 230, 245 (dans cet ordre). Tableau [198, 212, 230, 245] : milieu = 1 (212 < 230), puis milieu = 2 (230 trouvé) : 2 comparaisons (2 tours de boucle).

</details>

**Q3** (1 pt, recherche_dichotomique) Définir la recherche dichotomique et citer la condition que doit vérifier le tableau pour qu'on puisse l'appliquer. Préciser sa complexité en fonction de la taille n du tableau.

<details><summary>Corrigé</summary>

La recherche dichotomique cherche une valeur en comparant avec l'élément du milieu de la zone de recherche, puis en ne conservant que la moitié pouvant contenir la valeur, jusqu'à la trouver ou obtenir une zone vide. Le tableau doit être trié. Complexité logarithmique, en O(log2(n)).

</details>

## B-recherche_textuelle
### Recherche textuelle

**Q1** (1 pt, recherche_textuelle) Pour préparer l'algorithme de Boyer-Moore-Horspool, on souhaite une fonction derniere_position(motif) qui renvoie un dictionnaire associant à chaque caractère du motif, sauf le dernier, l'indice de sa dernière apparition. Par exemple derniere_position('RADAR') renvoie {'R': 0, 'A': 3, 'D': 2}.

Recopier et compléter le code suivant :

```python
1 def derniere_position(motif):
2     d = ...
3     for i in range(...):
4         ... = i
5     return d
```

<details><summary>Corrigé</summary>

```python
def derniere_position(motif):
    d = {}
    for i in range(len(motif) - 1):
        d[motif[i]] = i
    return d
```

</details>

**Q2** (1 pt, recherche_textuelle) Écrire une fonction Python positions(motif, texte) qui renvoie la liste de tous les indices du texte à partir desquels le motif apparaît, en utilisant l'algorithme de recherche naïve (comparaison caractère par caractère). Par exemple positions('ab', 'abcabab') renvoie [0, 3, 5].

<details><summary>Corrigé</summary>

```python
def positions(motif, texte):
    res = []
    n, m = len(texte), len(motif)
    for i in range(n - m + 1):
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j = j + 1
        if j == m:
            res.append(i)
    return res
```

</details>

**Q3** (1 pt, recherche_textuelle) On considère la fonction suivante :

```python
def compte(motif, texte):
    c = 0
    for i in range(len(texte) - len(motif) + 1):
        if texte[i:i + len(motif)] == motif:
            c = c + 1
    return c
```

Donner le résultat de l'appel compte('ara', 'tarararam').

<details><summary>Corrigé</summary>

3 (occurrences aux indices 1, 3 et 5, qui se chevauchent).

</details>

## B-recursivite
### Récursivité

**Q1** (1 pt, recursivite) On considère la fonction récursive suivante :

```python
def f(n):
    if n <= 1:
        return 1
    return 2 * f(n - 1) + 1
```

Calculer les valeurs f(1), f(3) et f(5).

<details><summary>Corrigé</summary>

f(1) = 1, f(2) = 3, f(3) = 7, f(4) = 15, f(5) = 31.

</details>

**Q2** (1 pt, recursivite) Un robot doit monter un escalier en faisant des pas d'une ou de deux marches. On note m(n) le nombre de façons de monter n marches, avec m(1) = 1 et m(2) = 2. Énumérer toutes les façons de monter 4 marches (sous forme de suites de 1 et de 2), puis déterminer la relation de récurrence liant m(n) à m(n-1) et m(n-2).

<details><summary>Corrigé</summary>

1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 : m(4) = 5. Le premier pas est de 1 (reste n-1 marches) ou de 2 (reste n-2) : m(n) = m(n-1) + m(n-2).

</details>

**Q3** (1 pt, recursivite) Indiquer ce qu'est une fonction récursive et expliquer pourquoi une telle fonction doit comporter un cas de base.

<details><summary>Corrigé</summary>

Une fonction récursive est une fonction qui s'appelle elle-même. Le cas de base, traité sans appel récursif, garantit l'arrêt : sans lui les appels s'enchaîneraient indéfiniment (dépassement de la pile d'appels, RecursionError en Python).

</details>

**Q4** (1 pt, recursivite) On considère la fonction suivante :

```python
def miroir(s):
    if s == '':
        return ''
    return miroir(s[1:]) + s[0]
```

Que renvoie l'appel miroir('nsi') ? Détailler la suite des appels.

<details><summary>Corrigé</summary>

miroir('nsi') = miroir('si') + 'n' = (miroir('i') + 's') + 'n' = ((miroir('') + 'i') + 's') + 'n' = 'isn'.

</details>

## B-representation_nombres
### Représentation des nombres

**Q1** (1 pt, representation_nombres) Un capteur transmet une mesure sous la forme de l'octet 1011 0110. Donner la valeur décimale de cet octet s'il représente un entier naturel, puis sa valeur s'il représente un entier relatif codé en complément à deux sur 8 bits. Donner enfin son écriture hexadécimale.

<details><summary>Corrigé</summary>

Entier naturel : 128 + 32 + 16 + 4 + 2 = 182. Complément à deux : 182 - 256 = -74. Hexadécimal : B6.

</details>

**Q2** (1 pt, representation_nombres) Écrire une fonction binaire(n) qui prend en paramètre un entier naturel n et renvoie la chaîne de caractères de son écriture en base 2, obtenue par divisions successives par 2. Par exemple binaire(13) renvoie '1101' et binaire(0) renvoie '0'.

<details><summary>Corrigé</summary>

```python
def binaire(n):
    if n == 0:
        return '0'
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s
```

</details>

**Q3** (1 pt, representation_nombres) Un appareil stocke des entiers naturels sur 12 bits. Combien de valeurs différentes peut-il représenter ? Quelle est la plus grande valeur représentable ? Combien de bits faut-il au minimum pour représenter le nombre 1000 ?

<details><summary>Corrigé</summary>

2^12 = 4096 valeurs ; plus grande valeur 4095. Comme 2^9 = 512 ≤ 1000 < 1024 = 2^10, il faut 10 bits.

</details>

**Q4** (1 pt, representation_nombres) Pour ajouter de la redondance à un octet transmis, on ajoute un bit de parité valant 1 si l'octet contient un nombre impair de 1, et 0 sinon. Un élève propose :

```python
1 def bit_parite(octet):
2     nb = 0
3     for b in octet:
4         if b == 1:
5             nb = nb + 1
6     return nb // 2
```

où octet est une liste de huit 0 ou 1. Expliquer pourquoi cette fonction est incorrecte (on pourra donner l'écriture binaire de 7 sur 8 bits comme exemple) et corriger la ligne fautive.

<details><summary>Corrigé</summary>

7 s'écrit 00000111 : 3 bits à 1, on attend 1 mais nb // 2 renvoie 1 par hasard ; pour 01111111 (127, 7 bits à 1) elle renvoie 3, qui n'est pas un bit. Il faut le reste et non le quotient : ligne 6 : return nb % 2.

</details>

## B-reseau_ip
### Réseaux et adressage IP

**Q1** (1 pt, reseau_ip) Le réseau d'une entreprise utilise le protocole OSPF, avec un coût de liaison égal à 10^8 / d, où d est le débit en bit/s. Les liaisons sont : A-B en fibre à 1 Gbit/s, B-D à 100 Mbit/s, A-C à 10 Mbit/s, C-D à 1 Gbit/s. Calculer le coût de chaque liaison puis le coût total des routes A-B-D et A-C-D, et indiquer la route choisie par OSPF.

<details><summary>Corrigé</summary>

Coûts : A-B = 0,1 ; B-D = 1 ; A-C = 10 ; C-D = 0,1. A-B-D = 1,1 ; A-C-D = 10,1. OSPF choisit A-B-D.

</details>

**Q2** (1 pt, reseau_ip) Une machine a pour adresse IPv4 172.16.200.9. Donner la représentation binaire sur 8 bits de l'octet 200.

<details><summary>Corrigé</summary>

200 = 128 + 64 + 8 : 11001000.

</details>

**Q3** (1 pt, reseau_ip) Un lycée utilise le réseau 10.4.32.0/20. Identifier la partie fixe (partie réseau) des adresses IP de ce réseau, puis déterminer le nombre d'adresses utilisables pour des machines.

<details><summary>Corrigé</summary>

Les 20 premiers bits sont fixes : 10.4 et les 4 bits de poids fort du troisième octet (0010, car 32 = 0010 0000). Les adresses vont de 10.4.32.0 à 10.4.47.255. 12 bits pour les machines : 2^12 - 2 = 4094 adresses (on retire l'adresse réseau et l'adresse de diffusion).

</details>

**Q4** (1 pt, reseau_ip) Cinq routeurs sont reliés par les liaisons R1-R2, R2-R5, R1-R3, R3-R4, R4-R5 et R2-R4. Le routage utilise le protocole RIP. La liaison R2-R5 vient de se rompre. Indiquer un plus court chemin au sens de RIP de R1 vers R5, et le nombre de sauts.

<details><summary>Corrigé</summary>

R1-R2-R4-R5 ou R1-R3-R4-R5 : 3 sauts (avant la panne, R1-R2-R5 en 2 sauts).

</details>

## B-routage
### Routage

**Q1** (1 pt, routage) Un poste a la configuration suivante : adresse IP 192.168.5.40, masque 255.255.255.0, passerelle 192.168.6.1. Le routeur de son réseau local a l'adresse 192.168.5.1. Le poste communique avec son réseau local mais pas avec Internet. Identifier le paramètre mal configuré et proposer une correction.

<details><summary>Corrigé</summary>

La passerelle 192.168.6.1 n'appartient pas au réseau 192.168.5.0/24 : il faut indiquer la passerelle 192.168.5.1 (adresse du routeur).

</details>

**Q2** (1 pt, routage) Un réseau comporte les routeurs A, B, C, D, E reliés par les liaisons A-B, A-C, B-D, C-E, E-D et B-C. On utilise le protocole RIP. Indiquer deux routes qui permettent d'atteindre le routeur D depuis A et leur nombre de sauts, puis préciser celle retenue par RIP.

<details><summary>Corrigé</summary>

A-B-D : 2 sauts ; A-C-E-D : 3 sauts (ou A-C-B-D : 3 sauts). RIP retient A-B-D (minimum de sauts).

</details>

**Q3** (1 pt, routage) Un réseau est représenté par un dictionnaire d'adjacence, par exemple reseau = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}. Écrire une fonction sauts(reseau, depart) qui renvoie un dictionnaire associant à chaque routeur accessible le nombre minimal de sauts depuis depart (comme le calcule RIP), à l'aide d'un parcours en largeur. Ici sauts(reseau, 'A') renvoie {'A': 0, 'B': 1, 'C': 1, 'D': 2}.

<details><summary>Corrigé</summary>

```python
def sauts(reseau, depart):
    dist = {depart: 0}
    file = [depart]
    while file:
        r = file.pop(0)
        for v in reseau[r]:
            if v not in dist:
                dist[v] = dist[r] + 1
                file.append(v)
    return dist
```

</details>

**Q4** (1 pt, routage) Avec le protocole RIP, un routeur reçoit la table d'un voisin et met sa propre table à jour. Les tables sont des dictionnaires destination -> (passerelle, distance). Recopier et compléter les lignes 4 et 5 :

```python
1 def mise_a_jour(table, voisin, table_voisin):
2     for dest in table_voisin:
3         d = table_voisin[dest][1] + 1
4         if dest not in table or ... :
5             table[dest] = ...
6     return table
```

<details><summary>Corrigé</summary>

```python
def mise_a_jour(table, voisin, table_voisin):
    for dest in table_voisin:
        d = table_voisin[dest][1] + 1
        if dest not in table or d < table[dest][1]:
            table[dest] = (voisin, d)
    return table
```

</details>

## B-securite_crypto
### Sécurisation des communications

**Q1** (1 pt, securite_crypto) On chiffre un octet, représenté par une liste de huit 0 ou 1, en effectuant un XOR bit à bit avec une clé de même format. Recopier et compléter les lignes 4 et 5 de la fonction suivante :

```python
1 def chiffrer(octet, cle):
2     res = []
3     for i in range(8):
4         b = ...
5         res.append(...)
6     return res
```

<details><summary>Corrigé</summary>

```python
def chiffrer(octet, cle):
    res = []
    for i in range(8):
        b = (octet[i] + cle[i]) % 2
        res.append(b)
    return res
```
(on peut aussi écrire b = octet[i] ^ cle[i]).

</details>

**Q2** (1 pt, securite_crypto) Camille dispose d'un couple (clé publique, clé privée). Elle envoie à Malo un message accompagné d'une empreinte de ce message chiffrée avec sa clé privée. Décrire ce que doit réaliser Malo pour vérifier que le message vient bien de Camille et n'a pas été modifié, en justifiant.

<details><summary>Corrigé</summary>

Malo déchiffre l'empreinte avec la clé publique de Camille et calcule lui-même l'empreinte du message reçu. Si les deux coïncident, le message est intègre et vient de Camille, seule détentrice de la clé privée associée.

</details>

**Q3** (1 pt, securite_crypto) On utilise un chiffrement par décalage (chiffre de César) de clé 4 : chaque lettre majuscule est remplacée par la lettre située 4 rangs plus loin dans l'alphabet, Z étant suivi de A. Chiffrer la chaîne "ROUTEUR" puis indiquer comment le destinataire déchiffre le message.

<details><summary>Corrigé</summary>

"VSYXIYV". Le destinataire décale chaque lettre de 4 rangs vers la gauche (même clé : chiffrement symétrique).

</details>

**Q4** (1 pt, securite_crypto) Expliquer la différence de fonctionnement entre un chiffrement symétrique et un chiffrement asymétrique, puis préciser pourquoi le protocole HTTPS combine les deux.

<details><summary>Corrigé</summary>

Symétrique : une même clé secrète chiffre et déchiffre. Asymétrique : on chiffre avec la clé publique du destinataire et seul celui-ci déchiffre avec sa clé privée. HTTPS utilise l'asymétrique pour échanger de façon sûre une clé symétrique, puis le symétrique, beaucoup plus rapide, pour chiffrer les échanges.

</details>

## B-sgbd
### Banque de questions : SGBD

**Q1** (1 pt, sgbd) Une médiathèque stocke ses emprunts dans une base gérée par un SGBD. Un programme Python récupère le résultat d'une requête sous la forme d'une liste de tuples (titre, nb_emprunts), par exemple :
```python
resultat = [('Dune', 12), ('Ubik', 5), ('Solaris', 9)]
```
Recopier et compléter la fonction suivante, qui renvoie le titre le plus emprunté.
```python
1 def plus_emprunte(resultat):
2     meilleur = resultat[0]
3     for ligne in resultat:
4         if ...:
5             meilleur = ...
6     return ...
```

<details><summary>Corrigé</summary>

```python
def plus_emprunte(resultat):
    meilleur = resultat[0]
    for ligne in resultat:
        if ligne[1] > meilleur[1]:
            meilleur = ligne
    return meilleur[0]
```

</details>

**Q2** (1 pt, sgbd) Deux bibliothécaires modifient au même instant le nombre d'exemplaires disponibles d'un même livre dans la base de la médiathèque. Indiquer quel rôle du SGBD permet d'éviter une incohérence des données, et préciser deux autres rôles d'un SGBD.

<details><summary>Corrigé</summary>

La gestion des accès concurrents (le SGBD sérialise/verrouille les transactions). Autres rôles : sécuriser les accès (droits des utilisateurs), assurer la persistance des données, garantir l'intégrité (contraintes de clés, de domaine).

</details>

**Q3** (1 pt, sgbd) La table Emprunt d'une médiathèque contient 4 000 lignes. Un SGBD sans index doit lire toutes les lignes pour trouver un emprunt par son identifiant ; avec un index trié, il effectue une recherche dichotomique. Calculer le nombre maximal de comparaisons dans chacun des deux cas.

<details><summary>Corrigé</summary>

Sans index : 4 000 comparaisons. Avec recherche dichotomique : 12 comparaisons au plus (2^11 = 2048 < 4000 ≤ 4096 = 2^12).

</details>

## B-soc_architecture
### Banque de questions : architecture et systèmes d'exploitation

**Q1** (1 pt, soc_architecture) Un circuit combinatoire a deux entrées E1 et E2 et une sortie S = NON(E1 ET E2) (porte NAND). Donner la table de vérité complète de ce circuit, puis la valeur de S pour E1 = 1 et E2 = 0.

<details><summary>Corrigé</summary>

| E1 | E2 | S |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
Pour E1 = 1, E2 = 0 : S = 1.

</details>

**Q2** (1 pt, soc_architecture) Un ordonnanceur à tourniquet (round robin) gère une file de processus. Chaque processus est un dictionnaire {'pid': ..., 'reste': ...} où 'reste' est le nombre de quanta encore nécessaires. Recopier et compléter la fonction suivante qui renvoie la liste des PID dans l'ordre de leur terminaison.
```python
1 def tourniquet(file):
2     termines = []
3     while len(file) > 0:
4         p = file.pop(0)
5         p['reste'] = ...
6         if p['reste'] == 0:
7             termines.append(...)
8         else:
9             file.append(...)
10    return termines
```

<details><summary>Corrigé</summary>

```python
def tourniquet(file):
    termines = []
    while len(file) > 0:
        p = file.pop(0)
        p['reste'] = p['reste'] - 1
        if p['reste'] == 0:
            termines.append(p['pid'])
        else:
            file.append(p)
    return termines
```

</details>

**Q3** (1 pt, soc_architecture) Un processeur calcule 40 – 25 sur 8 bits en effectuant l'addition 40 + (–25), où –25 est codé en complément à deux. Donner le codage binaire sur 8 bits de –25, puis le résultat binaire de l'addition.

<details><summary>Corrigé</summary>

25 = 00011001 ; inversion : 11100110 ; +1 : 11100111 (–25). 40 = 00101000. 00101000 + 11100111 = 1 00001111 ; on ignore la retenue : 00001111 = 15.

</details>

**Q4** (1 pt, soc_architecture) Deux processus P1 et P2 utilisent une imprimante et un scanner. P1 a obtenu l'imprimante et demande le scanner ; P2 a obtenu le scanner et demande l'imprimante. Expliquer ce qu'il se passe et nommer cette situation.

<details><summary>Corrigé</summary>

Chaque processus attend une ressource détenue par l'autre sans libérer la sienne : ils restent bloqués indéfiniment. C'est un interblocage (deadlock).

</details>

## B-sql
### Banque de questions : langage SQL

**Q1** (1 pt, sql) Une base de festival contient la relation Concert(id_concert, groupe, scene, heure_debut). Suite à un changement, le concert n°14 aura lieu sur la scène "Plage" à 21:30. Écrire la requête mettant à jour la base de données en conséquence.

<details><summary>Corrigé</summary>

UPDATE Concert SET scene = 'Plage', heure_debut = '21:30' WHERE id_concert = 14;

</details>

**Q2** (1 pt, sql) Une base de covoiturage contient les relations Conducteur(id_cond, nom, ville) et Trajet(id_trajet, #id_cond, depart, arrivee, places). Écrire une requête permettant d'obtenir la liste sans doublon des noms des conducteurs ayant proposé un trajet à destination de "Lyon".

<details><summary>Corrigé</summary>

SELECT DISTINCT Conducteur.nom FROM Conducteur JOIN Trajet ON Conducteur.id_cond = Trajet.id_cond WHERE Trajet.arrivee = 'Lyon';

</details>

**Q3** (1 pt, sql) Une base météo contient la relation Releve(id_releve, station, date_releve, temperature). Écrire une requête SQL permettant d'afficher la date et la température des relevés de la station "Belvédère" dont la température dépasse 30, triés par température décroissante.

<details><summary>Corrigé</summary>

SELECT date_releve, temperature FROM Releve WHERE station = 'Belvédère' AND temperature > 30 ORDER BY temperature DESC;

</details>

**Q4** (1 pt, sql) On considère la table Livre :

| id | titre | annee |
|---|---|---|
| 1 | Ubik | 1969 |
| 2 | Dune | 1965 |
| 3 | Neuromancien | 1984 |
| 4 | Solaris | 1961 |

Donner le résultat de la requête : SELECT titre FROM Livre WHERE annee < 1970 AND id > 1;

<details><summary>Corrigé</summary>

Dune et Solaris.

</details>

## B-tableau_liste
### Banque de questions : tableaux et listes

**Q1** (1 pt, tableau_liste) Un capteur enregistre des températures dans un tableau temp. On cherche la longueur de la plus longue suite de valeurs consécutives strictement croissantes. Recopier et compléter la fonction.
```python
1 def plus_longue_hausse(temp):
2     meilleur = 1
3     courant = 1
4     for i in range(1, len(temp)):
5         if temp[i] > ...:
6             courant = ...
7         else:
8             courant = ...
9         if courant > meilleur:
10            meilleur = courant
11    return meilleur
```

<details><summary>Corrigé</summary>

```python
def plus_longue_hausse(temp):
    meilleur = 1
    courant = 1
    for i in range(1, len(temp)):
        if temp[i] > temp[i - 1]:
            courant = courant + 1
        else:
            courant = 1
        if courant > meilleur:
            meilleur = courant
    return meilleur
```

</details>

**Q2** (1 pt, tableau_liste) On dispose de deux tableaux triés dans l'ordre croissant L1 et L2. Proposer une fonction Python fusion(L1, L2) qui renvoie un nouveau tableau trié contenant tous les éléments de L1 et L2, en parcourant chaque tableau une seule fois à l'aide de deux indices i1 et i2.

<details><summary>Corrigé</summary>

```python
def fusion(L1, L2):
    L = []
    i1, i2 = 0, 0
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] <= L2[i2]:
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1
    return L + L1[i1:] + L2[i2:]
```

</details>

**Q3** (1 pt, tableau_liste) Dans un programme de gestion de pile de documents, on manipule une liste Python docs uniquement avec docs.append(d) et docs.pop(). Donner la structure de données correspondant à ces manipulations et la valeur renvoyée par docs.pop() après docs = [] ; docs.append('A') ; docs.append('B') ; docs.append('C').

<details><summary>Corrigé</summary>

Une pile (LIFO). docs.pop() renvoie 'C'.

</details>

**Q4** (1 pt, tableau_liste) Écrire une fonction moyenne_sans_extremes(notes) qui prend en argument un tableau notes d'au moins trois nombres et renvoie la moyenne des valeurs après avoir retiré une occurrence du minimum et une occurrence du maximum, sans modifier le tableau passé en paramètre.

<details><summary>Corrigé</summary>

```python
def moyenne_sans_extremes(notes):
    mini = notes[0]
    maxi = notes[0]
    total = 0
    for n in notes:
        total += n
        if n < mini:
            mini = n
        if n > maxi:
            maxi = n
    return (total - mini - maxi) / (len(notes) - 2)
```

</details>

## B-tri
### Banque de questions : algorithmes de tri

**Q1** (1 pt, tri) On considère la fonction suivante :
```python
def ranger(t):
    for i in range(len(t)):
        k = i
        for j in range(i + 1, len(t)):
            if t[j] < t[k]:
                k = j
        t[i], t[k] = t[k], t[i]
```
Parmi les propositions suivantes, choisir celle qui correspond au tri effectué : tri par insertion, tri par sélection, tri à bulles, tri fusion.

<details><summary>Corrigé</summary>

Tri par sélection : à chaque étape on cherche l'indice du minimum de la partie non triée et on l'échange avec t[i].

</details>

**Q2** (1 pt, tri) On applique le tri par insertion au tableau [7, 3, 9, 1]. Donner l'état du tableau après chacune des trois étapes d'insertion.

<details><summary>Corrigé</summary>

Après insertion de 3 : [3, 7, 9, 1] ; de 9 : [3, 7, 9, 1] ; de 1 : [1, 3, 7, 9].

</details>

**Q3** (1 pt, tri) Un tri fusion appelle tri_fusion(lst) avec m = len(lst) // 2, puis fusionne tri_fusion(lst[:m]) et tri_fusion(lst[m:]). Pour une liste de 16 éléments, déterminer combien de niveaux de découpage sont nécessaires pour arriver à des listes d'un élément, et indiquer en justifiant la complexité du tri fusion comparée à celle du tri par sélection.

<details><summary>Corrigé</summary>

4 niveaux (16 → 8 → 4 → 2 → 1, car 2^4 = 16). Chaque niveau coûte O(n) en fusions, d'où O(n log n), meilleur que le O(n²) du tri par sélection.

</details>

## B-tuple
### Banque de questions : tuples

**Q1** (1 pt, tuple) Dans un agenda, un rendez-vous est représenté par un tuple (jour, mois, heure, motif), par exemple rdv = (14, 3, 10, 'dentiste'). Donner l'expression Python permettant d'obtenir le motif de rdv, et indiquer ce qu'il se passe lors de l'exécution de rdv[2] = 11.

<details><summary>Corrigé</summary>

rdv[3] (ou rdv[-1]) vaut 'dentiste'. rdv[2] = 11 provoque une erreur TypeError : un tuple n'est pas modifiable (immuable).

</details>

**Q2** (1 pt, tuple) Un couple (a, b) d'entiers est dit « harmonieux » si a < b et si a divise b. Justifier que le couple (4, 10) n'est pas harmonieux, puis que (3, 12) l'est.

<details><summary>Corrigé</summary>

(4, 10) : 4 < 10 mais 10 % 4 = 2 ≠ 0, donc 4 ne divise pas 10. (3, 12) : 3 < 12 et 12 % 3 = 0.

</details>

**Q3** (1 pt, tuple) Un point du plan est représenté par un tuple (x, y). Écrire une fonction milieu(a, b) qui prend en argument deux tuples a et b et renvoie le tuple des coordonnées du milieu du segment [ab].

<details><summary>Corrigé</summary>

```python
def milieu(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
```

</details>

## B-web_http
### Banque de questions : web et HTTP

**Q1** (1 pt, web_http) Un serveur web reçoit des requêtes HTTP. On représente chaque requête par un tuple (methode, chemin, code_reponse). On exécute :
```python
requetes = [('GET', '/', 200), ('POST', '/login', 302), ('GET', '/admin', 403), ('GET', '/img.png', 404)]
nb = 0
for m, c, code in requetes:
    if m == 'GET' and code >= 400:
        nb = nb + 1
print(nb)
```
Donner la valeur affichée après exécution et expliquer la signification du code 404.

<details><summary>Corrigé</summary>

Affiche 2 (requêtes /admin et /img.png). Le code 404 signifie que la ressource demandée est introuvable sur le serveur.

</details>

**Q2** (1 pt, web_http) Un formulaire de connexion envoie un identifiant et un mot de passe. Proposer, en justifiant, la méthode HTTP (GET ou POST) et le protocole (HTTP ou HTTPS) à utiliser, puis expliquer brièvement comment HTTPS sécurise l'échange.

<details><summary>Corrigé</summary>

POST, car les données ne figurent pas dans l'URL, et HTTPS. HTTPS utilise un chiffrement asymétrique (clé publique du serveur, certificat) pour échanger une clé de session, puis un chiffrement symétrique de toutes les données échangées.

</details>

**Q3** (1 pt, web_http) Un site de réservation stocke ses données dans les relations Hotel(id_hotel, nom, ville) et Service(id_service, #id_hotel, libelle). Écrire une requête SQL permettant d'obtenir le nom des hôtels et leur ville qui proposent le service "spa".

<details><summary>Corrigé</summary>

SELECT Hotel.nom, Hotel.ville FROM Hotel JOIN Service ON Hotel.id_hotel = Service.id_hotel WHERE Service.libelle = 'spa';

</details>

## I-abr
### Exercice 1 — Mystère dans un ABR

Une médiathèque range les cotes numériques de ses ouvrages dans un arbre binaire de recherche. Un nœud est un objet de la classe Noeud (attributs valeur, gauche, droit ; None représente l'arbre vide).

```python
1 def mystere(a):
2     if a is None:
3         return None
4     if a.droit is None:
5         return a.valeur
6     return mystere(a.droit)
```

L'ABR contient les cotes 50 (racine), 30 et 70 (fils de 50), 20 et 40 (fils de 30), 60 et 80 (fils de 70).

**Q1** (1 pt, abr) Donner la valeur renvoyée par l'appel mystere(racine) puis expliquer en une phrase ce que calcule cette fonction pour un ABR quelconque.

<details><summary>Corrigé</summary>

80. La fonction descend toujours vers le fils droit : elle renvoie la plus grande valeur de l'ABR (None si l'arbre est vide).

</details>

### Exercice 2 — Compter les cotes d'un intervalle

On reprend la classe Noeud (attributs valeur, gauche, droit ; None pour l'arbre vide). La fonction demandée prend trois paramètres : un ABR a, un entier bas, un entier haut ; elle renvoie le nombre de valeurs v de l'arbre telles que bas <= v <= haut, en n'explorant un sous-arbre que s'il peut contenir de telles valeurs.

**Q2** (1 pt, abr) Écrire une fonction compte_intervalle(a, bas, haut) qui renvoie le nombre de valeurs de l'ABR a comprises entre bas et haut (inclus).

<details><summary>Corrigé</summary>

```python
class Noeud:
    def __init__(self, v, g=None, d=None):
        self.valeur, self.gauche, self.droit = v, g, d

def compte_intervalle(a, bas, haut):
    if a is None:
        return 0
    if a.valeur < bas:
        return compte_intervalle(a.droit, bas, haut)
    if a.valeur > haut:
        return compte_intervalle(a.gauche, bas, haut)
    return 1 + compte_intervalle(a.gauche, bas, haut) + compte_intervalle(a.droit, bas, haut)

r = Noeud(50, Noeud(30, Noeud(20), Noeud(40)), Noeud(70, Noeud(60), Noeud(80)))
assert compte_intervalle(r, 35, 65) == 3
```

</details>

### Exercice 3 — Index d'une base de données

Un SGBD indexe la colonne age d'une table à l'aide d'un ABR : c'est l'une des utilisations classiques des ABR (bases de données indexées). Les âges sont insérés dans l'ordre 41, 25, 63, 25, 30, 70 avec la règle du cours : une valeur inférieure ou égale à celle d'un nœud va dans son sous-arbre gauche, une valeur strictement supérieure dans son sous-arbre droit.

**Q3** (1 pt, abr) Donner la liste obtenue par le parcours infixe de l'ABR après ces six insertions, puis la hauteur de l'arbre (un arbre réduit à sa racine a une hauteur de 1).

<details><summary>Corrigé</summary>

Infixe : [25, 25, 30, 41, 63, 70]. Arbre : 41 → gauche 25 (dont le fils gauche est 25 et le fils droit 30), droite 63 → droit 70. Hauteur 3.

</details>

## I-algo_simples
### Exercice 1 — Relevés de température

Une station météo enregistre une température par heure dans une liste temp de n valeurs. Pour trouver la température maximale de la journée, le programme initialise une variable m avec temp[0], puis parcourt une seule fois les éléments restants en remplaçant m dès qu'il rencontre une valeur plus grande.

**Q1** (1 pt, algo_simples) Donner le nombre de comparaisons entre éléments effectuées par cet algorithme pour une liste de n valeurs, et sa complexité.

<details><summary>Corrigé</summary>

n - 1 comparaisons ; complexité linéaire O(n).

</details>

### Exercice 2 — Quel algorithme ?

Un élève propose quatre façons de calculer la moyenne d'une liste notes de n nombres :
- A : trier la liste puis prendre l'élément du milieu ;
- B : parcourir la liste en ajoutant chaque élément à un accumulateur s, puis renvoyer s / n ;
- C : renvoyer (max(notes) + min(notes)) / 2 ;
- D : pour chaque élément, parcourir toute la liste et additionner.

**Q2** (1 pt, algo_simples) Quelle proposition calcule correctement la moyenne avec un coût linéaire ? Justifier.

<details><summary>Corrigé</summary>

B : elle somme tous les éléments en un seul parcours (n additions, coût O(n)) puis divise par n. A donne la médiane, C le milieu de l'étendue, D est quadratique et ne donne pas la moyenne sans division supplémentaire.

</details>

### Exercice 3 — Plus longue série

Dans un jeu de pile ou face, les lancers sont stockés dans une liste de chaînes 'P' ou 'F'. On veut une fonction qui prend en paramètre une liste lancers, éventuellement vide, et renvoie la longueur de la plus longue suite de valeurs identiques consécutives, 0 pour une liste vide.

**Q3** (1 pt, algo_simples) Écrire une fonction plus_longue_serie(lancers) qui renvoie la longueur de la plus longue suite de valeurs identiques consécutives de lancers.

<details><summary>Corrigé</summary>

```python
def plus_longue_serie(lancers):
    if len(lancers) == 0:
        return 0
    meilleur = 1
    courant = 1
    for i in range(1, len(lancers)):
        if lancers[i] == lancers[i - 1]:
            courant += 1
        else:
            courant = 1
        if courant > meilleur:
            meilleur = courant
    return meilleur

assert plus_longue_serie(['P', 'F', 'F', 'F', 'P', 'P']) == 3
assert plus_longue_serie([]) == 0
```

</details>

### Exercice 4 — Itinéraire le moins coûteux

Le protocole OSPF choisit la route qui minimise la somme des coûts des liaisons empruntées. Les coûts entre routeurs sont donnés dans le dictionnaire : couts = {('A','B'): 10, ('B','D'): 10, ('A','C'): 1, ('C','D'): 50, ('C','B'): 1}. Les seules routes sans boucle de A vers D sont : A-B-D, A-C-D, A-C-B-D. Un algorithme simple calcule la somme des coûts de chaque route (somme par accumulation) puis garde le minimum.

**Q4** (1 pt, algo_simples) Déterminer la route de A vers D retenue par cet algorithme, en donnant le coût total de chaque route.

<details><summary>Corrigé</summary>

A-B-D : 20 ; A-C-D : 51 ; A-C-B-D : 1 + 1 + 10 = 12. Route retenue : A-C-B-D (coût 12).

</details>

## I-arbre_binaire
### Exercice 1 — Arbre complet en tableau

On représente un arbre binaire complet de taille n par un tableau t de taille n + 1 : t[0] contient n, la racine est en t[1], et le nœud d'indice i a son fils gauche à l'indice 2*i et son fils droit à l'indice 2*i + 1.

t = [7, 'A', 'B', 'C', 'D', 'E', 'F', 'G']

**Q1** (1 pt, arbre_binaire) Déterminer le nombre de feuilles de l'arbre représenté par t, puis écrire une fonction nb_feuilles(t) qui renvoie ce nombre pour un tel tableau.

<details><summary>Corrigé</summary>

4 feuilles (D, E, F, G). Un nœud i est une feuille si 2*i > n.
```python
def nb_feuilles(t):
    n = t[0]
    c = 0
    for i in range(1, n + 1):
        if 2 * i > n:
            c += 1
    return c

assert nb_feuilles([7, 'A', 'B', 'C', 'D', 'E', 'F', 'G']) == 4
```

</details>

## I-calculabilite
### Exercice 1 — Problèmes décidables ?

Voici une liste de problèmes :
- P1 : déterminer si un entier n donné est pair ;
- P2 : déterminer si un programme Python quelconque s'arrête sur une entrée donnée ;
- P3 : déterminer si une liste d'entiers donnée est triée ;
- P4 : déterminer si deux programmes quelconques calculent toujours le même résultat.

**Q1** (1 pt, calculabilite) Parmi les problèmes ci-dessus, sélectionner ceux qui sont décidables.

<details><summary>Corrigé</summary>

P1 et P3 (un algorithme qui termine toujours les résout). P2 (problème de l'arrêt) et P4 sont indécidables.

</details>

### Exercice 2 — Le problème de l'arrêt

En 1936, un mathématicien britannique a démontré qu'il n'existe aucun programme capable de dire, pour tout programme P et toute entrée e, si P s'arrête sur e. Sa démonstration raisonne par l'absurde : on suppose l'existence d'une fonction arret(P, e) puis on construit un programme qui contredit sa réponse.

**Q2** (1 pt, calculabilite) Donner le nom de ce mathématicien et le nom du problème dont il a démontré l'indécidabilité.

<details><summary>Corrigé</summary>

Alan Turing ; le problème de l'arrêt.

</details>

### Exercice 3 — Suite de Syracuse

On considère la fonction :

```python
def syracuse(n):
    etapes = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        etapes += 1
    return etapes
```

Personne n'a encore démontré que cette boucle termine pour tout entier n >= 1. Valeurs de test : 1, 3, 6.

**Q3** (1 pt, calculabilite) Donner les valeurs renvoyées par syracuse(1), syracuse(3) et syracuse(6).

<details><summary>Corrigé</summary>

syracuse(1) = 0 ; syracuse(3) = 7 (3,10,5,16,8,4,2,1) ; syracuse(6) = 8 (6,3,10,5,16,8,4,2,1).

</details>

### Exercice 4 — Un vérificateur universel

Une entreprise annonce un logiciel « Verif » qui, pour tout programme Python et toute entrée, indique en un temps fini si le programme finira par afficher « erreur ». L'indécidabilité est un concept fondamental en logique : certains problèmes ne peuvent être résolus par aucun algorithme.

**Q4** (1 pt, calculabilite) En étudiant cette annonce, dire si un tel logiciel peut exister. Justifier la réponse.

<details><summary>Corrigé</summary>

Non. Si Verif existait, on décide l'arrêt d'un programme P sur e en construisant Q qui exécute P(e) puis affiche « erreur » : Q affiche « erreur » si et seulement si P s'arrête. Verif résoudrait le problème de l'arrêt, qui est indécidable : contradiction.

</details>

## I-chaines
### Exercice 1 — Mot de passe valide

Un site impose les règles suivantes à un mot de passe mdp : longueur au moins 8, au moins une lettre majuscule, au moins un chiffre, aucun espace. La fonction renvoie True si toutes les règles sont respectées, False sinon.

**Q1** (1 pt, chaines) Écrire une fonction est_valide(mdp) qui renvoie True si la chaîne mdp respecte toutes les règles. Exemple : est_valide('Nsi2026ok') renvoie True.

<details><summary>Corrigé</summary>

```python
def est_valide(mdp):
    if len(mdp) < 8:
        return False
    maj = False
    chiffre = False
    for c in mdp:
        if c == ' ':
            return False
        if 'A' <= c <= 'Z':
            maj = True
        if '0' <= c <= '9':
            chiffre = True
    return maj and chiffre

assert est_valide('Nsi2026ok')
assert not est_valide('nsi2026ok')
assert not est_valide('Nsi 2026ok')
```

</details>

### Exercice 2 — Palindrome à compléter

On considère la fonction à trous suivante, qui doit renvoyer True si la chaîne s se lit de la même façon dans les deux sens :

```python
1 def est_palindrome(s):
2     i = 0
3     j = ...
4     while i < j:
5         if s[i] != s[j]:
6             return ...
7         i = i + 1
8         j = ...
9     return True
```

**Q2** (1 pt, chaines) Recopier et compléter les lignes 3, 6 et 8 de la fonction est_palindrome.

<details><summary>Corrigé</summary>

```python
def est_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True

assert est_palindrome('radar') and not est_palindrome('nsi')
```

</details>

### Exercice 3 — Bandeau de caractères

Une enseigne lumineuse affiche la chaîne s = 'TERMINALE' : la figure 1 la représente comme une rangée de 9 cases numérotées de 0 à 8, chaque case contenant un caractère (case 0 : 'T', case 8 : 'E'). Le programme d'affichage lit s[k] pour allumer la case k.

**Q3** (1 pt, chaines) En vous appuyant sur la figure 1, donner la valeur de s[4], de s[-1] et de s[2:5].

<details><summary>Corrigé</summary>

s[4] = 'I' ; s[-1] = 'E' ; s[2:5] = 'RMI'.

</details>

### Exercice 4 — Texte sur une seule chaîne

Avant une recherche textuelle, on récupère tout le texte d'un fichier dans une seule chaîne. Le contenu lu est fourni sous forme d'une liste de lignes, chacune terminée par '\n', par exemple lignes = ['Le chat\n', 'dort.\n'].

**Q4** (1 pt, chaines) Écrire une fonction texte_unique(lignes) qui renvoie une seule chaîne où les lignes sont mises bout à bout et chaque '\n' remplacé par une espace. Exemple : texte_unique(['Le chat\n', 'dort.\n']) renvoie 'Le chat dort. '.

<details><summary>Corrigé</summary>

```python
def texte_unique(lignes):
    texte = ''
    for ligne in lignes:
        for c in ligne:
            if c == '\n':
                texte = texte + ' '
            else:
                texte = texte + c
    return texte

assert texte_unique(['Le chat\n', 'dort.\n']) == 'Le chat dort. '
```

</details>

## I-complexite
### Exercice 1 — Compteur d'opérations

Une classe Compteur sert à mesurer le coût d'un algorithme. Elle possède un attribut nb (entier, initialisé à 0) et une méthode recherche(self, tab, x) : celle-ci parcourt la liste tab, incrémente nb à chaque comparaison avec x, renvoie True dès que x est trouvé, False sinon.

**Q1** (1 pt, complexite) Écrire la classe Compteur avec son constructeur et la méthode recherche décrite ci-dessus.

<details><summary>Corrigé</summary>

```python
class Compteur:
    def __init__(self):
        self.nb = 0

    def recherche(self, tab, x):
        for v in tab:
            self.nb += 1
            if v == x:
                return True
        return False

c = Compteur()
assert c.recherche([4, 8, 1], 7) is False and c.nb == 3
```

</details>

### Exercice 2 — Doubler la taille

Un programme de tri par sélection met 2 secondes pour trier une liste de 10 000 éléments. On sait que son coût est quadratique en la taille n de la liste, quel que soit l'ordre initial des éléments.

**Q2** (1 pt, complexite) Donner une estimation du temps nécessaire pour trier une liste de 20 000 éléments.

<details><summary>Corrigé</summary>

Environ 8 secondes : doubler n multiplie un coût en n² par 4.

</details>

### Exercice 3 — Dichotomie contre recherche séquentielle

On compare deux fonctions de recherche dans une liste triée de n entiers (n très grand) : recherche_seq(tab, x) (parcours de gauche à droite) et recherche_dicho(tab, x) (on coupe l'intervalle en deux à chaque étape). Pour n = 1 000 000, la première peut effectuer jusqu'à 1 000 000 de comparaisons, la seconde au plus une vingtaine.

**Q3** (1 pt, complexite) Expliquer pourquoi la recherche dichotomique n'effectue qu'une vingtaine de comparaisons dans le pire cas pour n = 1 000 000.

<details><summary>Corrigé</summary>

À chaque étape la taille de l'intervalle est divisée par 2 ; après k étapes il reste n/2^k éléments. Comme 2^20 ≈ 1 048 576 > 10^6, au plus environ 20 étapes suffisent : coût logarithmique O(log2 n).

</details>

### Exercice 4 — Classer des algorithmes

Trois algorithmes traitent une liste de n éléments :
- tri fusion : O(n log n) ;
- tri par insertion (pire cas) : O(n²) ;
- calcul du maximum : O(n).
Une complexité quasi-linéaire se situe entre une complexité linéaire et une complexité quadratique.

**Q4** (1 pt, complexite) Déterminer l'ordre des trois algorithmes, du plus rapide au plus lent pour n grand.

<details><summary>Corrigé</summary>

Maximum O(n), puis tri fusion O(n log n), puis tri par insertion O(n²).

</details>

## I-dictionnaire
### Exercice 1 — Dépouillement d'un vote

Lors de l'élection des délégués, chaque bulletin contient le prénom d'un candidat. Les bulletins sont rangés dans une liste de chaînes. Un élève propose la fonction suivante, qui doit renvoyer un dictionnaire associant à chaque candidat son nombre de voix :

```python
1 def compter_voix(bulletins):
2     resultats = {}
3     for nom in bulletins:
4         resultats[nom] = resultats[nom] + 1
5     return resultats
```

L'appel `compter_voix(['Lina', 'Hugo', 'Lina'])` provoque l'erreur `KeyError: 'Lina'`.

**Q1** (1 pt, dictionnaire) Modifier le code de la fonction compter_voix pour qu'elle renvoie le bon dictionnaire, y compris lorsqu'un candidat apparaît pour la première fois.

<details><summary>Corrigé</summary>

```python
def compter_voix(bulletins):
    resultats = {}
    for nom in bulletins:
        if nom in resultats:
            resultats[nom] = resultats[nom] + 1
        else:
            resultats[nom] = 1
    return resultats

assert compter_voix(['Lina', 'Hugo', 'Lina']) == {'Lina': 2, 'Hugo': 1}
```
L'erreur venait de la lecture de resultats[nom] alors que la clé nom n'existait pas encore.

</details>

### Exercice 2 — Contrôle des badges

Le portique d'un lycée de 2 000 élèves doit décider, à chaque passage, si un numéro de badge est autorisé. Le service informatique hésite entre deux représentations : une liste `badges` contenant les 2 000 numéros autorisés, testée avec `num in badges`, ou un dictionnaire `autorisations` dont les clés sont les numéros autorisés (valeur : le nom de l'élève), testé avec `num in autorisations`. Les passages sont très nombreux le matin.

**Q2** (1 pt, dictionnaire) Expliquer pourquoi le dictionnaire est préférable à la liste dans le cas de ce portique.

<details><summary>Corrigé</summary>

Le test `num in badges` sur une liste parcourt les éléments un par un : coût linéaire en la taille (jusqu'à 2 000 comparaisons). Un dictionnaire est une table de hachage : la clé est hachée pour accéder directement à son emplacement, le test d'appartenance se fait en temps constant en moyenne, indépendamment du nombre d'élèves. De plus le dictionnaire associe directement le nom à la clé.

</details>

### Exercice 3 — Relevés de températures

On dispose des relevés de températures (en degrés, entiers) suivants et du script :

```python
releves = [12, 15, 12, 9, 15, 12]
freq = {}
for t in releves:
    freq[t] = freq.get(t, 0) + 1
```

On rappelle que `d.get(cle, defaut)` renvoie `d[cle]` si la clé existe et `defaut` sinon.

**Q3** (1 pt, dictionnaire) Donner le contenu du dictionnaire freq après l'exécution de ce script.

<details><summary>Corrigé</summary>

{12: 3, 15: 2, 9: 1}

</details>

### Exercice 4 — Mise à jour d'un stock

Une épicerie représente son stock par un dictionnaire :

```python
stock = {'pomme': 12, 'poire': 5, 'kiwi': 20}
stock['poire'] = 8
```

**Q4** (1 pt, dictionnaire) Indiquer la clé concernée par la seconde instruction et préciser son rôle, puis donner le contenu de stock après cette instruction.

<details><summary>Corrigé</summary>

La clé est 'poire' : elle identifie de façon unique l'entrée du dictionnaire. Comme elle existe déjà, l'affectation ne crée pas de nouvelle entrée mais remplace la valeur associée (5 devient 8). stock = {'pomme': 12, 'poire': 8, 'kiwi': 20}.

</details>

## I-diviser_regner
### Exercice 1 — Maximum par dichotomie

On considère la fonction suivante (t est une liste non vide d'entiers, g et d sont des indices inclus avec g <= d) :

```python
def maximum(t, g, d):
    if g == d:
        return t[g]
    m = (g + d) // 2
    a = maximum(t, g, m)       # moitié gauche (indices g à m)
    b = maximum(t, m + 1, d)   # moitié droite (indices m+1 à d)
    if a > b:
        return a
    return b
```

**Q1** (1 pt, diviser_regner) Donner la valeur renvoyée par l'appel maximum([4, 9, 2, 7, 5], 2, 4) ainsi que la liste des couples (g, d) des appels récursifs effectués (appel initial compris).

<details><summary>Corrigé</summary>

Valeur renvoyée : 7. Appels : (2, 4), (2, 3), (2, 2), (3, 3), (4, 4).

</details>

### Exercice 2 — Exponentiation rapide

Pour calculer x puissance n (n entier positif), on utilise la méthode « diviser pour régner » suivante, implémentée par une fonction récursive expo(x, n) : si n vaut 0, le résultat est 1 ; sinon on calcule une seule fois p = expo(x, n // 2), puis on renvoie p * p si n est pair et p * p * x si n est impair. On appelle expo(2, 13).

**Q2** (1 pt, diviser_regner) Donner la valeur renvoyée par l'appel expo(2, 13) et la suite des valeurs de n prises par les appels successifs.

<details><summary>Corrigé</summary>

```python
def expo(x, n):
    if n == 0:
        return 1
    p = expo(x, n // 2)
    if n % 2 == 0:
        return p * p
    return p * p * x

assert expo(2, 13) == 8192
```
Valeurs de n : 13, 6, 3, 1, 0. Valeur renvoyée : 8192.

</details>

### Exercice 3 — Comparaison de tris

Une animation compare trois tris sur une liste de 100 000 entiers aléatoires : le tri par sélection (coût quadratique), le tri par insertion (coût quadratique dans le cas moyen) et le tri fusion, qui coupe la liste en deux, trie récursivement chaque moitié puis fusionne les deux moitiés triées.

**Q3** (1 pt, diviser_regner) Déterminer le tri qui termine le premier dans cette animation, en justifiant par sa complexité.

<details><summary>Corrigé</summary>

Le tri fusion : grâce à la stratégie diviser pour régner, il a une complexité en O(n log n), alors que les tris par sélection et par insertion sont en O(n²) ; pour n = 100 000, n log n ≈ 1,7 million contre n² = 10 milliards.

</details>

## I-donnees_tables
### Exercice 1 — Filtrer une table de licenciés

Un club sportif stocke ses licenciés dans une table, liste de dictionnaires de la forme `{'nom': 'Diallo', 'ville': 'Lyon', 'age': 16}`. La fonction suivante doit renvoyer la liste des noms des licenciés habitant la ville donnée en paramètre.

```python
1 def noms_par_ville(table, ville):
2     resultat = []
3     for ligne in table:
4         if ...:
5             ...
6     return resultat
```

**Q1** (1 pt, donnees_tables) Recopier et compléter les lignes 4 et 5 de la fonction noms_par_ville afin qu'elle respecte sa spécification.

<details><summary>Corrigé</summary>

```python
def noms_par_ville(table, ville):
    resultat = []
    for ligne in table:
        if ligne['ville'] == ville:
            resultat.append(ligne['nom'])
    return resultat
```

</details>

### Exercice 2 — Moyenne d'une colonne

Une table est représentée par une liste de dictionnaires ayant tous les mêmes clés (les attributs). On souhaite une fonction moyenne_attribut prenant deux paramètres : table, la liste de dictionnaires, attribut, une chaîne désignant un attribut à valeurs numériques ; elle renvoie la moyenne des valeurs de cet attribut, ou None si la table est vide.

**Q2** (1 pt, donnees_tables) Écrire une fonction moyenne_attribut(table, attribut) qui prend en paramètre une table et un nom d'attribut et qui renvoie la moyenne des valeurs de cet attribut (None si la table est vide).

<details><summary>Corrigé</summary>

```python
def moyenne_attribut(table, attribut):
    if len(table) == 0:
        return None
    total = 0
    for ligne in table:
        total = total + ligne[attribut]
    return total / len(table)

assert moyenne_attribut([{'x': 2}, {'x': 4}], 'x') == 3
assert moyenne_attribut([], 'x') is None
```

</details>

### Exercice 3 — Tri d'une table de mesures

Une table de mesures est donnée sous forme de liste de tuples (identifiant, valeur) :

```python
mesures = [(1, 14), (2, 9), (3, 21), (4, 9)]

def valeur(m):
    return m[1]

res = [m[0] for m in sorted(mesures, key=valeur, reverse=True)]
```

On rappelle que le tri de Python est stable : deux éléments de même clé gardent leur ordre initial.

**Q3** (1 pt, donnees_tables) Donner le contenu de la liste res après l'exécution de ce code.

<details><summary>Corrigé</summary>

[3, 1, 2, 4]

</details>

### Exercice 4 — Vérifier un fichier téléchargé

Un site d'open data propose le fichier `communes.csv` et indique son empreinte MD5 : `9e107d9d372bb6826bd81d3542a419d6`. Cette empreinte est le résultat que doit donner le fichier lorsqu'il est haché par la fonction MD5. Après téléchargement, Léa calcule l'empreinte MD5 de son fichier et obtient `e4d909c290d0fb1ca068ffaddf22cbd0`.

**Q4** (1 pt, donnees_tables) Le fichier téléchargé par Léa est-il identique au fichier proposé par le site ? Justifier.

<details><summary>Corrigé</summary>

Non : une même donnée donne toujours la même empreinte par la fonction de hachage ; les deux empreintes étant différentes, le fichier de Léa diffère de l'original (téléchargement incomplet ou altéré). Il faut le télécharger à nouveau.

</details>

## I-file
### Exercice 1 — File d'attente en base de données

Un guichet enregistre sa file d'attente dans la table `Attente(num, nom)` (num : entier, clé primaire, attribué dans l'ordre croissant d'arrivée ; nom : texte). La personne en tête de file est donc celle de plus petit numéro (et non celle de nom le plus petit).

**Q1** (1 pt, file) Donner la requête SQL permettant de défiler, c'est-à-dire de supprimer de la table Attente la personne en tête de file.

<details><summary>Corrigé</summary>

DELETE FROM Attente WHERE num = (SELECT MIN(num) FROM Attente);

</details>

### Exercice 2 — File avec deux piles

On implémente une file avec deux listes Python utilisées comme piles : `entree` reçoit les éléments enfilés (append), `sortie` fournit les éléments défilés (pop). Quand `sortie` est vide, on y transvase tous les éléments de `entree`.

```python
1 class File:
2     def __init__(self):
3         self.entree = []
4         self.sortie = []
5     def enfiler(self, x):
6         self.entree.append(x)
7     def defiler(self):
8         ...
```

On suppose que defiler n'est appelée que sur une file non vide.

**Q2** (1 pt, file) Recopier et compléter la méthode defiler à partir de la ligne 8, qui renvoie et retire l'élément le plus ancien de la file.

<details><summary>Corrigé</summary>

```python
class File:
    def __init__(self):
        self.entree = []
        self.sortie = []
    def enfiler(self, x):
        self.entree.append(x)
    def defiler(self):
        if self.sortie == []:
            while self.entree != []:
                self.sortie.append(self.entree.pop())
        return self.sortie.pop()

f = File()
for x in [1, 2, 3]:
    f.enfiler(x)
assert f.defiler() == 1 and f.defiler() == 2
```

</details>

### Exercice 3 — Taille d'une file

On dispose de l'interface : `creer_file_vide()`, `est_vide(f)`, `enfiler(f, x)`, `defiler(f)` (renvoie et retire la tête). La fonction taille doit renvoyer le nombre d'éléments de f, f devant retrouver son état initial à la fin.

```python
1 def taille(f):
2     aux = creer_file_vide()
3     n = 0
4     while not est_vide(f):
5         ...
6         ...
7     while not est_vide(aux):
8         ...
9     return n
```

**Q3** (1 pt, file) Recopier et compléter les lignes 5 à 8 de la fonction taille afin qu'elle renvoie le nombre d'éléments sans modifier la file f.

<details><summary>Corrigé</summary>

```python
from collections import deque
def creer_file_vide(): return deque()
def est_vide(f): return len(f) == 0
def enfiler(f, x): f.append(x)
def defiler(f): return f.popleft()

def taille(f):
    aux = creer_file_vide()
    n = 0
    while not est_vide(f):
        enfiler(aux, defiler(f))
        n = n + 1
    while not est_vide(aux):
        enfiler(f, defiler(aux))
    return n

f = deque([4, 5, 6])
assert taille(f) == 3 and list(f) == [4, 5, 6]
```

</details>

### Exercice 4 — Interface minimale d'une file

On considère les opérations suivantes : (a) créer une file vide, (b) tester si la file est vide, (c) enfiler un élément en queue, (d) défiler l'élément de tête, (e) trier la file, (f) accéder au i-ème élément, (g) inverser la file.

**Q4** (1 pt, file) Indiquer les opérations qui constituent a minima l'interface d'une file.

<details><summary>Corrigé</summary>

(a), (b), (c) et (d) : création d'une file vide, test de vacuité, enfiler et défiler (FIFO). Les opérations (e), (f), (g) ne font pas partie de l'interface minimale.

</details>

## I-fonctions
### Exercice 1 — De la fonction à la requête

Les élèves sont représentés en Python par une liste de dictionnaires et en base de données par la relation `Eleve(id, nom, classe, moyenne)`.

```python
def admis(eleves, classe):
    res = []
    for e in eleves:
        if e['classe'] == classe and e['moyenne'] >= 10:
            res.append(e['nom'])
    return res
```

**Q1** (1 pt, fonctions) Donner la requête SQL permettant d'obtenir, dans la base, le même résultat que l'appel admis(eleves, 'TG2').

<details><summary>Corrigé</summary>

SELECT nom FROM Eleve WHERE classe = 'TG2' AND moyenne >= 10;

</details>

### Exercice 2 — Effet de bord

La fonction ajoute_bonus prend deux paramètres : notes, une liste de nombres, b, un nombre ; elle ajoute b à chaque élément de notes, modifie la liste en place, ne contient aucune instruction return.

```python
def ajoute_bonus(notes, b):
    for i in range(len(notes)):
        notes[i] = notes[i] + b

L = [8, 12]
r = ajoute_bonus(L, 2)
```

**Q2** (1 pt, fonctions) Expliquer pourquoi, après ces instructions, L vaut [10, 14] alors que r vaut None.

<details><summary>Corrigé</summary>

La liste est un objet mutable passé par référence : notes et L désignent la même liste, donc la modification en place est visible dans L (effet de bord). La fonction ne contenant pas de return, elle renvoie implicitement None, valeur affectée à r.

</details>

### Exercice 3 — Réutiliser une fonction

On dispose de la fonction suivante :

```python
def est_premier(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True
```

**Q3** (1 pt, fonctions) Écrire une fonction premiers_jusqua(n) qui prend en paramètre un entier n et qui renvoie la liste croissante des nombres premiers inférieurs ou égaux à n, en utilisant est_premier.

<details><summary>Corrigé</summary>

```python
def est_premier(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def premiers_jusqua(n):
    res = []
    for k in range(2, n + 1):
        if est_premier(k):
            res.append(k)
    return res

assert premiers_jusqua(10) == [2, 3, 5, 7]
assert premiers_jusqua(1) == []
```

</details>

### Exercice 4 — Recherche dans un arbre

On considère l'arbre binaire de recherche de racine 8, dont le fils gauche est 3 (fils gauche 1, fils droit 6) et le fils droit est 10 (sans fils gauche, fils droit 14). La fonction suivante renvoie True si element est dans l'arbre et False sinon :

```python
def appartient(arbre, element):
    if arbre is None:
        return False
    if element == arbre.valeur:
        return True
    if element < arbre.valeur:
        return appartient(arbre.gauche, element)
    return appartient(arbre.droit, element)
```

**Q4** (1 pt, fonctions) Indiquer les valeurs des nœuds visités lors de l'appel appartient(a, 7), où a est cet arbre, ainsi que la valeur renvoyée.

<details><summary>Corrigé</summary>

Nœuds visités : 8, 3, 6 (puis le sous-arbre droit vide de 6). Valeur renvoyée : False.

</details>

## I-glouton
### Exercice 1 — Rendu de monnaie

Une caisse automatique rend la monnaie avec les pièces de `pieces = [200, 100, 50, 20, 10, 5, 2, 1]` (en centimes, ordre décroissant). Elle choisit à chaque étape la plus grande pièce ne dépassant pas la somme restante.

```python
1 def rendu(somme, pieces):
2     rendues = []
3     i = 0
4     while somme > 0:
5         if ...:
6             ...
7             ...
8         else:
9             i = i + 1
10    return rendues
```

**Q1** (1 pt, glouton) Recopier et compléter les lignes 5 à 7 de la fonction rendu afin qu'elle renvoie la liste des pièces rendues selon la stratégie gloutonne.

<details><summary>Corrigé</summary>

```python
def rendu(somme, pieces):
    rendues = []
    i = 0
    while somme > 0:
        if pieces[i] <= somme:
            rendues.append(pieces[i])
            somme = somme - pieces[i]
        else:
            i = i + 1
    return rendues

assert rendu(263, [200, 100, 50, 20, 10, 5, 2, 1]) == [200, 50, 10, 2, 1]
```

</details>

### Exercice 2 — Planning d'une salle

Une salle de sport accueille des activités, chacune représentée par un tuple (debut, fin) d'heures entières. La fonction planning prend en paramètre activites, une liste de tuples, quelconque, éventuellement vide ; elle trie les activités par heure de fin croissante, choisit la première, puis retient chaque activité dont le début est supérieur ou égal à la fin de la dernière activité retenue ; elle renvoie la liste des activités retenues.

**Q2** (1 pt, glouton) Écrire une fonction planning(activites) qui prend en paramètre une liste de tuples (debut, fin) et qui renvoie la liste des activités retenues selon cette stratégie gloutonne.

<details><summary>Corrigé</summary>

```python
def fin(a):
    return a[1]

def planning(activites):
    retenues = []
    for a in sorted(activites, key=fin):
        if retenues == [] or a[0] >= retenues[-1][1]:
            retenues.append(a)
    return retenues

assert planning([(9, 12), (8, 10), (10, 11), (11, 13)]) == [(8, 10), (10, 11), (11, 13)]
assert planning([]) == []
```

</details>

### Exercice 3 — Sac à dos glouton

Un randonneur dispose d'un sac de capacité 10 kg. Les objets sont donnés par des tuples (masse, valeur) et triés par rapport valeur/masse décroissant :

```python
objets = [(2, 10), (5, 20), (4, 12), (3, 6)]

def sac(objets, capacite):
    total = 0
    for m, v in objets:
        if m <= capacite:
            capacite = capacite - m
            total = total + v
    return total
```

**Q3** (1 pt, glouton) Donner la valeur renvoyée par l'appel sac(objets, 10).

<details><summary>Corrigé</summary>

36 : on prend (2, 10) (reste 8), (5, 20) (reste 3), on ne peut pas prendre (4, 12), on prend (3, 6) (reste 0) ; total 10 + 20 + 6 = 36.

</details>

### Exercice 4 — Descente d'une pyramide

Une pyramide de nombres est représentée par une liste de listes : `p = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`. Depuis l'élément p[i][j], on peut descendre vers p[i+1][j] ou p[i+1][j+1]. La fonction suivante calcule de manière gloutonne la somme d'un « meilleur » trajet en choisissant à chaque étage le plus grand des deux voisins du dessous.

```python
1 def _glouton(p):
2     j = 0
3     somme = p[0][0]
4     for i in range(1, len(p)):
5         if p[i][j + 1] > p[i][j]:
6             ...
7         somme = somme + p[i][j]
8     return somme
```

Instructions proposées : (A) `j = j - 1` ; (B) `j = j + 1` ; (C) `i = i + 1` ; (D) `somme = somme + p[i][j + 1]`.

**Q4** (1 pt, glouton) Parmi les instructions (A) à (D), sélectionner celle qui complète la ligne 6, puis donner la valeur renvoyée par _glouton(p).

<details><summary>Corrigé</summary>

(B) j = j + 1. Trajet 3 → 7 → 4 → 9, valeur renvoyée 23.
```python
def _glouton(p):
    j = 0
    somme = p[0][0]
    for i in range(1, len(p)):
        if p[i][j + 1] > p[i][j]:
            j = j + 1
        somme = somme + p[i][j]
    return somme

assert _glouton([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) == 23
```

</details>

## I-graphe
### Exercice 1 — Réseau de pistes cyclables

Un graphe non orienté est représenté par un dictionnaire de listes d'adjacence :

```python
pistes = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}
```

Spécification de la fonction `ajouter_arete` : elle prend en paramètres un graphe g (dictionnaire), deux sommets s1 et s2, ajoute s2 aux voisins de s1 et s1 aux voisins de s2, crée un sommet absent avec une liste vide, et n'ajoute jamais un voisin déjà présent.

**Q1** (1 pt, graphe) Écrire la fonction ajouter_arete(g, s1, s2) permettant d'ajouter l'arête entre s1 et s2 en respectant la spécification.

<details><summary>Corrigé</summary>

def ajouter_arete(g, s1, s2):
    if s1 not in g:
        g[s1] = []
    if s2 not in g:
        g[s2] = []
    if s2 not in g[s1]:
        g[s1].append(s2)
    if s1 not in g[s2]:
        g[s2].append(s1)

</details>

### Exercice 2 — Chaîne la plus courte

On reprend le graphe non orienté des pistes cyclables : A–B, A–C, B–D, C–D, D–E (toutes les arêtes ont la même longueur).

**Q2** (1 pt, graphe) Donner une chaîne de longueur minimale reliant A à E, ainsi que sa longueur.

<details><summary>Corrigé</summary>

A - B - D - E (ou A - C - D - E), de longueur 3.

</details>

### Exercice 3 — Matrice d'adjacence symétrique

Un graphe à 4 sommets numérotés 0 à 3 est représenté par la matrice d'adjacence :

```python
M = [[0, 1, 1, 0],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [0, 1, 1, 0]]
```

**Q3** (1 pt, graphe) Expliquer pourquoi cette matrice permet d'affirmer que le graphe représenté est non orienté.

<details><summary>Corrigé</summary>

La matrice est symétrique : M[i][j] == M[j][i] pour tous i, j ; chaque arête i–j est donc présente dans les deux sens, ce qui caractérise un graphe non orienté.

</details>

### Exercice 4 — Ordre de visite en largeur

Graphe : `g = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}`. La fonction `parcours_largeur(g, depart)` renvoie la liste des sommets parcourus en partant du sommet depart, les voisins étant traités dans l'ordre des listes, à l'aide d'une file.

**Q4** (1 pt, graphe) Donner la liste renvoyée par parcours_largeur(g, 'B').

<details><summary>Corrigé</summary>

['B', 'A', 'D', 'C', 'E']

</details>

## I-interface_tad
### Exercice 1 — Une pile par son interface

On dispose d'un module implémentant le type abstrait Pile avec l'interface : `creer_pile()`, `est_vide(p)`, `empiler(p, x)`, `depiler(p)` (renvoie l'élément retiré).

```python
1 def mystere(p):
2     q = creer_pile()
3     while not est_vide(p):
4         empiler(q, depiler(p))
5     return q
```

La pile p contient, de la base au sommet, 1, 2, 3.

**Q1** (1 pt, interface_tad) Donner le contenu de la pile renvoyée par mystere(p), de la base au sommet, et préciser l'état de p après l'appel.

<details><summary>Corrigé</summary>

La pile renvoyée contient 3, 2, 1 (base → sommet) : 1 est au sommet. La pile p est vide.

</details>

### Exercice 2 — Choisir une interface

On propose les opérations suivantes pour un type abstrait :
- `creer()` : crée une structure vide
- `ajouter(s, x)` : ajoute x à la fin
- `retirer(s)` : retire et renvoie l'élément le plus anciennement ajouté
- `est_vide(s)` : teste si la structure est vide

**Q2** (1 pt, interface_tad) Quel type abstrait de données cette interface décrit-elle ? Justifier.

<details><summary>Corrigé</summary>

Une file : l'élément retiré est le premier entré (FIFO).

</details>

### Exercice 3 — Taille d'une file via l'interface

On ne peut utiliser que l'interface File : `creer_file()`, `est_vide(f)`, `enfiler(f, x)`, `defiler(f)`.

```python
1 def taille(f):
2     aux = creer_file()
3     n = 0
4     while not est_vide(f):
5         ...
6         ...
7     while not est_vide(aux):
8         ...
9     return n
```

**Q3** (1 pt, interface_tad) Recopier et compléter les lignes 5, 6 et 8 de la fonction taille afin qu'elle renvoie le nombre d'éléments de f, f étant restaurée à la fin.

<details><summary>Corrigé</summary>

5        enfiler(aux, defiler(f))
6        n = n + 1
8        enfiler(f, defiler(aux))

</details>

### Exercice 4 — Le SGBD comme interface

Une médiathèque stocke ses données dans la relation `Livre(id, titre, auteur, annee)`. Les bibliothécaires n'accèdent jamais directement aux fichiers de stockage : ils passent par le SGBD, qui joue le rôle d'interface entre l'humain et la base.

**Q4** (1 pt, interface_tad) Donner la requête SQL permettant d'ajouter le livre d'id 412, intitulé « Dune », de Frank Herbert, paru en 1965, puis expliquer en une phrase pourquoi l'utilisateur n'a pas à connaître l'organisation physique des données.

<details><summary>Corrigé</summary>

INSERT INTO Livre (id, titre, auteur, annee) VALUES (412, 'Dune', 'Frank Herbert', 1965);
Le SGBD est une interface : il traduit la requête en opérations sur le stockage, dont l'implémentation reste cachée.

</details>

## I-k_ppv
### Exercice 1 — Vote des voisins

On classe un fruit à partir de ses k plus proches voisins.

```python
1 def vote(voisins):
2     compte = {}
3     for (distance, classe) in voisins:
4         if classe in compte:
5             compte[classe] = compte[classe] + 1
6         else:
7             compte[classe] = 1
8     meilleure = None
9     for c in compte:
10        if meilleure is None or compte[c] > compte[meilleure]:
11            meilleure = c
12    return meilleure
```

**Q1** (1 pt, k_ppv) Donner la valeur renvoyée par vote([(1.2, 'pomme'), (0.8, 'poire'), (1.5, 'pomme')]).

<details><summary>Corrigé</summary>

'pomme'

</details>

### Exercice 2 — Sélection des k plus proches

```python
1 def distance(a, b):
2     return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5
3
4 def k_plus_proches(donnees, cible, k):
5     liste = []
6     for (point, classe) in donnees:
7         liste.append(( ... , classe))
8     liste.sort()
9     return ...
```
`donnees` est une liste de couples (point, classe), un point étant un tuple (x, y).

**Q2** (1 pt, k_ppv) Recopier et compléter les lignes 7 et 9 de la fonction k_plus_proches afin qu'elle renvoie la liste des k couples (distance, classe) les plus proches de cible.

<details><summary>Corrigé</summary>

7        liste.append((distance(point, cible), classe))
9    return liste[:k]

</details>

### Exercice 3 — Distance de Manhattan

On souhaite utiliser une autre distance pour l'algorithme des k plus proches voisins. Spécification : la fonction manhattan prend en paramètres deux points a et b, tuples de deux nombres (x, y), et renvoie la somme des valeurs absolues des différences de leurs coordonnées.

**Q3** (1 pt, k_ppv) Écrire une fonction manhattan(a, b) qui prend en paramètres deux points et qui renvoie leur distance de Manhattan.

<details><summary>Corrigé</summary>

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

</details>

## I-liste_chainee
### Exercice 1 — Longueur d'une liste chaînée

```python
1 class Maillon:
2     def __init__(self, valeur, suivant=None):
3         self.valeur = valeur
4         self.suivant = suivant
5
6 def longueur(m):
7     n = 0
8     while ... :
9         n = n + 1
10        m = ...
11    return n
```

**Q1** (1 pt, liste_chainee) Recopier et compléter les lignes 8 et 10 de la fonction longueur afin qu'elle renvoie le nombre de maillons de la liste commençant par m (m vaut None pour une liste vide).

<details><summary>Corrigé</summary>

8    while m is not None:
10        m = m.suivant

</details>

### Exercice 2 — Insertion en tête

On utilise la classe `Maillon(valeur, suivant)` et la fonction :

```python
def inserer_tete(m, x):
    return Maillon(x, m)

l = None
for x in [4, 7, 2]:
    l = inserer_tete(l, x)
```

**Q2** (1 pt, liste_chainee) Donner la suite des valeurs de la liste l, de la tête à la fin, après exécution de ce code.

<details><summary>Corrigé</summary>

2 -> 7 -> 4

</details>

### Exercice 3 — Parcours jusqu'au maillon

Une liste chaînée contient les valeurs 5, 12, 9, 30 et 41, dans cet ordre depuis la tête. On ne peut accéder à un maillon qu'en suivant les liens depuis la tête.

**Q3** (1 pt, liste_chainee) Donner le chemin de maillons suivi pour atteindre la valeur 30, et le nombre de liens empruntés.

<details><summary>Corrigé</summary>

5 -> 12 -> 9 -> 30 : 3 liens suivis.

</details>

### Exercice 4 — Insertions en queue

On considère une liste chaînée initialement vide. On y insère successivement les valeurs 10, 20 et 30 en queue de liste.

**Q4** (1 pt, liste_chainee) Indiquer les valeurs de la liste de la tête à la queue, puis indiquer la valeur contenue dans le maillon dont l'attribut suivant vaut None.

<details><summary>Corrigé</summary>

10 -> 20 -> 30 ; le maillon dont suivant vaut None contient 30.

</details>

## I-matrice
### Exercice 1 — Transposée

```python
def transposee(m):
    n = len(m)
    t = [[0] * n] * n
    for i in range(n):
        for j in range(n):
            t[j][i] = m[i][j]
    return t
```
Appliquée à [[1, 2], [3, 4]], cette fonction renvoie [[2, 4], [2, 4]] au lieu de [[1, 3], [2, 4]].

**Q1** (1 pt, matrice) Modifier le code de transposee pour qu'elle renvoie la transposée correcte d'une matrice carrée.

<details><summary>Corrigé</summary>

def transposee(m):
    n = len(m)
    t = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t[j][i] = m[i][j]
    return t

</details>

### Exercice 2 — Somme d'une diagonale

```python
1 def f(m):
2     s = 0
3     for i in range(len(m)):
4         s = s + m[i][len(m) - 1 - i]
5     return s
```

**Q2** (1 pt, matrice) Donner la valeur renvoyée par f([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).

<details><summary>Corrigé</summary>

15 (3 + 5 + 7)

</details>

### Exercice 3 — Maximum d'une matrice

```python
1 def maximum(m):
2     maxi = m[0][0]
3     for ligne in m:
4         ...
5             ...
6                 ...
7     return maxi
```

**Q3** (1 pt, matrice) Recopier et compléter la fonction maximum (à partir de la ligne 4) qui renvoie le plus grand élément d'une matrice non vide.

<details><summary>Corrigé</summary>

def maximum(m):
    maxi = m[0][0]
    for ligne in m:
        for x in ligne:
            if x > maxi:
                maxi = x
    return maxi

</details>

### Exercice 4 — Bloc AES

Le chiffrement AES travaille par blocs de 128 bits, répartis dans une matrice de 16 octets (matrice carrée de taille 4).

**Q4** (1 pt, matrice) Expliquer pourquoi une matrice carrée de taille 4 suffit exactement à contenir un bloc de 128 bits.

<details><summary>Corrigé</summary>

Une matrice 4×4 contient 16 cases ; chacune contient un octet de 8 bits ; 16 × 8 = 128 bits.

</details>

## I-mise_au_point
### Exercice 1 — Fonction testée par assertions

On fournit les tests suivants :

```python
assert compte_pairs([]) == 0
assert compte_pairs([1, 3, 5]) == 0
assert compte_pairs([2, 4, 7, 8]) == 3
```

```python
1 def compte_pairs(t):
2     n = 0
3     ...
```

**Q1** (1 pt, mise_au_point) Recopier et compléter la fonction compte_pairs (à partir de la ligne 3) qui renvoie le nombre d'éléments pairs de t, de sorte que tous les tests passent.

<details><summary>Corrigé</summary>

def compte_pairs(t):
    n = 0
    for x in t:
        if x % 2 == 0:
            n = n + 1
    return n

</details>

### Exercice 2 — Bug d'indice

```python
def dernier_positif(t):
    for i in range(len(t) - 1, 0, -1):
        if t[i] > 0:
            return i
    return -1
```

**Q2** (1 pt, mise_au_point) Donner la valeur renvoyée par dernier_positif([5, -2, -3]) et expliquer l'erreur révélée.

<details><summary>Corrigé</summary>

-1 ; l'indice 0 n'est jamais examiné car range(len(t)-1, 0, -1) s'arrête avant 0 : il faut range(len(t)-1, -1, -1), qui renverrait 0.

</details>

### Exercice 3 — Type d'erreur

Lors de l'exécution d'un programme, l'interpréteur affiche l'un des messages suivants :
- `IndexError: list index out of range`
- `TypeError: unsupported operand type(s) for +: 'int' and 'str'`
- `NameError: name 'totl' is not defined`

Le programme contient l'instruction `total = 3 + input('nombre ? ')`.

**Q3** (1 pt, mise_au_point) Quel message cette instruction provoque-t-elle ? Justifier.

<details><summary>Corrigé</summary>

TypeError : input renvoie une chaîne (str), qu'on ne peut pas additionner à un entier.

</details>

### Exercice 4 — Configuration manuelle des routes

Une entreprise configure à la main les tables de routage de ses routeurs. Le réseau : R1 relié à R2 et R3, R2 relié à R4, R3 relié à R4 ; le réseau 192.168.4.0/24 est derrière R4. L'administrateur a saisi dans R2 la route « 192.168.4.0/24 → passerelle R1 », et dans R1 la route « 192.168.4.0/24 → passerelle R2 ».

**Q4** (1 pt, mise_au_point) Donner le chemin suivi par un paquet partant de R1 vers 192.168.4.0/24 avec ces tables, et la route corrigée à saisir dans R2.

<details><summary>Corrigé</summary>

R1 → R2 → R1 → R2 … : boucle de routage (le paquet est détruit quand son TTL atteint 0). Dans R2 il faut saisir : 192.168.4.0/24 → passerelle R4.

</details>

## I-modele_relationnel
### Exercice 1 — Relevés de capteurs

Une station météo stocke ses relevés dans la relation Releve(id_capteur, horodatage, temperature). Voici quatre tuples :

| id_capteur | horodatage | temperature |
|---|---|---|
| 3 | 1200 | 14.5 |
| 3 | 1260 | 14.7 |
| 5 | 1200 | 13.9 |
| 5 | 1260 | 14.7 |

**Q1** (1 pt, modele_relationnel) Expliquer pourquoi ni id_capteur seul ni horodatage seul ne peut être clé primaire, puis proposer une clé primaire pour cette relation.

<details><summary>Corrigé</summary>

id_capteur seul : la valeur 3 apparaît deux fois ; horodatage seul : 1200 apparaît deux fois. Une clé primaire doit identifier chaque tuple de façon unique : on choisit le couple (id_capteur, horodatage).

</details>

### Exercice 2 — Contrôle d'unicité

Une table Eleve a pour clé primaire num_eleve. On représente en Python les valeurs de num_eleve qu'on tente d'insérer successivement par la liste [12, 7, 31, 7, 18, 12]. Le SGBD refuse toute insertion qui viole la contrainte de clé primaire.

**Q2** (1 pt, modele_relationnel) Donner la liste des valeurs effectivement insérées dans la table, dans l'ordre, et le nombre d'insertions refusées.

<details><summary>Corrigé</summary>

[12, 7, 31, 18] ; 2 insertions refusées (le second 7 et le second 12).

</details>

### Exercice 3 — Médiathèque

Schéma : Adherent(id_adh, nom, prenom) avec id_adh clé primaire ; Emprunt(id_emp, #id_adh, titre, date) où id_adh est clé étrangère vers Adherent. La table Adherent contient les id_adh 1, 2 et 4.

**Q3** (1 pt, modele_relationnel) La requête INSERT INTO Emprunt VALUES (10, 3, 'Dune', '2026-03-01'); est-elle acceptée ? Justifier à l'aide du rôle de la clé étrangère.

<details><summary>Corrigé</summary>

Non : la valeur 3 de la clé étrangère id_adh doit exister comme clé primaire dans Adherent, ce qui n'est pas le cas ; la contrainte d'intégrité référentielle est violée et l'insertion est refusée.

</details>

## I-modularite
### Exercice 1 — Module géométrie

Un module geometrie.py propose :
- aire_disque(r)
- perimetre_disque(r)
- _verifier_positif(x) (fonction interne)
- la constante PI = 3.14159

Un élève écrit dans un autre fichier : from geometrie import *

**Q1** (1 pt, modularite) Quelles fonctions sont rendues disponibles par cette instruction ? Justifier.

<details><summary>Corrigé</summary>

aire_disque, perimetre_disque et PI ; _verifier_positif n'est pas importée par import * car son nom commence par un tiret bas (convention de nom privé/interne). Elle reste accessible via import geometrie puis geometrie._verifier_positif.

</details>

### Exercice 2 — Chaîne de dépendances

Un projet comporte quatre modules. main importe interface et calcul ; interface importe affichage ; calcul importe outils ; affichage importe outils. Le module outils n'importe rien.

**Q2** (1 pt, modularite) Dresser la liste de tous les chemins d'import qui mènent du module main au module outils, puis indiquer quels modules sont touchés si l'on modifie outils.

<details><summary>Corrigé</summary>

Chemins : main → interface → affichage → outils et main → calcul → outils. Si outils change, affichage et calcul (directement), interface et main (indirectement) peuvent être affectés.

</details>

### Exercice 3 — Utiliser une API

On dispose du module pile.py suivant :
```python
1 def creer():
2     return []
3 def empiler(p, x):
4     p.append(x)
5 def depiler(p):
6     return p.pop()
7 def est_vide(p):
8     return p == []
```

**Q3** (1 pt, modularite) Écrire, dans un autre fichier, une fonction inverser(lst) qui renvoie la liste lst inversée en n'utilisant que les fonctions de l'interface du module pile.

<details><summary>Corrigé</summary>

```python
import pile

def inverser(lst):
    p = pile.creer()
    for x in lst:
        pile.empiler(p, x)
    res = []
    while not pile.est_vide(p):
        res.append(pile.depiler(p))
    return res
```

</details>

### Exercice 4 — Origine d'une fonction

Un script de chiffrement commence ainsi :
```python
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes
```
Plus loin, on lit : cle = get_random_bytes(16) puis n = bytes_to_long(b'NSI').

**Q4** (1 pt, modularite) Déterminer le chemin complet (paquetage et sous-module) d'où provient chacune des fonctions get_random_bytes et bytes_to_long.

<details><summary>Corrigé</summary>

get_random_bytes provient du sous-module Random du paquetage Crypto (Crypto.Random) ; bytes_to_long provient du module number du sous-paquetage Util de Crypto (Crypto.Util.number).

</details>

## I-os_commandes
### Exercice 1 — Simuler cd

On représente le répertoire courant par une chaîne de chemin absolu, par exemple '/home/alice/docs'. On veut simuler la commande cd : la fonction cd(courant, arg) prend le chemin courant, un argument arg qui vaut soit '..', soit le nom d'un sous-répertoire (sans '/'), et renvoie le nouveau chemin. cd('/', '..') renvoie '/'.

**Q1** (1 pt, os_commandes) Écrire la fonction cd(courant, arg) conforme à cette spécification.

<details><summary>Corrigé</summary>

```python
def cd(courant, arg):
    if arg == '..':
        if courant == '/':
            return '/'
        i = courant.rfind('/')
        return '/' if i == 0 else courant[:i]
    if courant == '/':
        return '/' + arg
    return courant + '/' + arg
```

</details>

### Exercice 2 — Droits d'un fichier

Sur un serveur Linux, la commande ls -l affiche la ligne : -rwxr-x--- 1 bob profs 2048 mars 3 notes.sh. L'utilisateur alice appartient au groupe profs, l'utilisatrice carla n'appartient pas à ce groupe.

**Q2** (1 pt, os_commandes) Donner la commande chmod en notation octale qui produit exactement ces droits, et indiquer si carla peut lire notes.sh.

<details><summary>Corrigé</summary>

chmod 750 notes.sh ; carla (autres) n'a aucun droit (---) : elle ne peut pas lire le fichier.

</details>

### Exercice 3 — Séquence de commandes

Le répertoire courant est /home/eve et il est vide. On exécute :
1. mkdir a b
2. cd a
3. touch f1.txt f2.txt
4. cd ..
5. mv a/f1.txt b
6. rm a/f2.txt
7. ls a b

**Q3** (1 pt, os_commandes) Donner l'état des répertoires a et b après la commande 6, puis l'affichage de la commande 7.

<details><summary>Corrigé</summary>

a est vide ; b contient f1.txt. ls a b affiche :
a:

b:
f1.txt

</details>

### Exercice 4 — Tester une machine

Un administrateur veut savoir si l'imprimante d'adresse 192.168.1.40 est joignable depuis son poste Linux, sans connaître le chemin suivi par les paquets.

**Q4** (1 pt, os_commandes) Quelle commande doit-il utiliser : ping ou traceroute ? Justifier.

<details><summary>Corrigé</summary>

ping 192.168.1.40 : ping teste l'accessibilité d'une machine sur un réseau IP ; traceroute sert à afficher les routeurs traversés, ce qui n'est pas demandé.

</details>

## I-paradigmes
### Exercice 1 — Deux versions d'un calcul

```python
1 def somme_carres_a(lst):
2     s = 0
3     for x in lst:
4         s = s + x * x
5     return s
6
7 def somme_carres_b(lst):
8     return sum(map(lambda x: x * x, lst))
```

**Q1** (1 pt, paradigmes) Indiquer le paradigme de chaque fonction en justifiant à l'aide des lignes du code, puis donner la valeur de somme_carres_b([1, 2, 3]).

<details><summary>Corrigé</summary>

somme_carres_a est impérative : variable s modifiée par affectations successives dans une boucle (lignes 2-4). somme_carres_b est fonctionnelle : pas d'affectation ni d'état modifié, composition de fonctions (map, lambda, sum, ligne 8). Valeur : 14.

</details>

### Exercice 2 — Version fonctionnelle

On veut écrire, dans le paradigme fonctionnel, une fonction compter(lst, x) : paramètres une liste lst et une valeur x, résultat le nombre d'occurrences de x dans lst, sans boucle ni affectation de variable, sans modifier lst, en utilisant la récursivité.

**Q2** (1 pt, paradigmes) Écrire la fonction compter(lst, x) respectant cette spécification.

<details><summary>Corrigé</summary>

```python
def compter(lst, x):
    if lst == []:
        return 0
    return (1 if lst[0] == x else 0) + compter(lst[1:], x)
```

</details>

### Exercice 3 — Caractéristiques

Propriétés d'un langage :
- les fonctions peuvent être passées en paramètre
- les données sont immuables
- pas d'effet de bord
- on décrit des classes, des attributs et des méthodes

**Q3** (1 pt, paradigmes) Quelle propriété de cette liste n'appartient pas au paradigme fonctionnel ? Justifier.

<details><summary>Corrigé</summary>

La dernière : classes, attributs et méthodes caractérisent le paradigme objet, pas le paradigme fonctionnel.

</details>

### Exercice 4 — Table des valeurs de Fibonacci

On veut calculer le n-ième terme de la suite de Fibonacci (F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2) de façon impérative, avec deux variables a et b initialisées à 0 et 1 et mises à jour par a, b = b, a + b à chaque tour de boucle.

**Q4** (1 pt, paradigmes) Dresser le tableau des valeurs de a et b après chacun des 5 premiers tours de boucle, puis écrire la fonction fibo_imperatif(n).

<details><summary>Corrigé</summary>

Tours 1 à 5 : (a,b) = (1,1), (1,2), (2,3), (3,5), (5,8).
```python
def fibo_imperatif(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

</details>

## I-parcours_arbre
### Exercice 1 — Feuilles de gauche à droite

Un arbre binaire est représenté par None (arbre vide) ou par un tuple (gauche, valeur, droit). On veut la fonction feuilles(a) : paramètre un arbre a, résultat la liste des valeurs des feuilles (nœuds sans enfant), dans l'ordre d'un parcours en profondeur de gauche à droite, liste vide si a est vide.

**Q1** (1 pt, parcours_arbre) Écrire la fonction feuilles(a).

<details><summary>Corrigé</summary>

```python
def feuilles(a):
    if a is None:
        return []
    g, v, d = a
    if g is None and d is None:
        return [v]
    return feuilles(g) + feuilles(d)
```

</details>

### Exercice 2 — Infixe et ABR

On considère un arbre binaire de recherche (ABR) (valeurs du sous-arbre gauche inférieures à la racine, celles du sous-arbre droit supérieures) et son parcours infixe (gauche, racine, droite).

**Q2** (1 pt, parcours_arbre) Expliquer pourquoi le parcours infixe d'un ABR fournit ses valeurs dans l'ordre croissant.

<details><summary>Corrigé</summary>

Par récurrence : le parcours infixe liste d'abord tout le sous-arbre gauche (valeurs plus petites, déjà triées par hypothèse), puis la racine, puis le sous-arbre droit (valeurs plus grandes, triées) ; la concaténation est donc triée.

</details>

### Exercice 3 — Reconnaître un parcours

Arbre : racine 8 ; enfants de 8 : 3 (gauche) et 10 (droit) ; enfants de 3 : 1 et 6 ; enfant droit de 10 : 14.
Listes proposées :
- 8, 3, 1, 6, 10, 14
- 1, 3, 6, 8, 10, 14
- 1, 6, 3, 14, 10, 8

**Q3** (1 pt, parcours_arbre) Quel parcours (préfixe, infixe ou suffixe) correspond à la troisième liste ? Justifier.

<details><summary>Corrigé</summary>

Suffixe : chaque nœud apparaît après ses deux sous-arbres (1, 6 avant 3 ; 14 avant 10 ; la racine 8 en dernier).

</details>

### Exercice 4 — Organigramme

Une entreprise représente son organigramme par un arbre binaire : la directrice Ana a pour subordonnés Bilal (gauche) et Chloé (droite) ; Bilal a pour subordonnés Dina et Elio ; Chloé a pour subordonné droit Fanny. On veut lister les employés niveau hiérarchique par niveau hiérarchique.

**Q4** (1 pt, parcours_arbre) Donner l'ordre de visite des employés par un parcours en largeur d'abord.

<details><summary>Corrigé</summary>

Ana, Bilal, Chloé, Dina, Elio, Fanny.

</details>

## I-parcours_graphe
### Exercice 1 — Parcours à analyser

On donne le graphe orienté g = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D', 'E'], 'D': ['F'], 'E': ['F'], 'F': []} et la fonction :
```python
1 def parcours(g, s):
2     vus = [s]
3     file = [s]
4     while file:
5         u = file.pop(0)
6         for v in g[u]:
7             if v not in vus:
8                 vus.append(v)
9                 file.append(v)
10    return vus
```

**Q1** (1 pt, parcours_graphe) Indiquer le type de parcours réalisé et donner la valeur renvoyée par parcours(g, 'A').

<details><summary>Corrigé</summary>

Parcours en largeur (file FIFO, ligne 5) ; renvoie ['A', 'B', 'C', 'D', 'E', 'F'].

</details>

### Exercice 2 — Degrés sortants

Un graphe orienté à n sommets numérotés de 0 à n-1 est donné par sa matrice d'adjacence m (liste de listes d'entiers 0 ou 1, m[i][j] == 1 s'il existe un arc de i vers j). Exemple : m = [[0, 1, 1], [0, 0, 1], [0, 0, 0]] (le sommet 0 a deux successeurs).

**Q2** (1 pt, parcours_graphe) Écrire une fonction puits(m) qui renvoie la liste des sommets sans successeur (ici [2]), en parcourant chaque ligne de la matrice.

<details><summary>Corrigé</summary>

```python
def puits(m):
    res = []
    for i in range(len(m)):
        if sum(m[i]) == 0:
            res.append(i)
    return res
```

</details>

### Exercice 3 — Accessibilité

Un graphe est représenté par un dictionnaire de listes de successeurs, par exemple g = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D', 'E'], 'D': ['F'], 'E': ['F'], 'F': []}. On veut la fonction accessible(g, s, t) : paramètres le graphe g, un sommet de départ s, un sommet d'arrivée t, résultat True si t est atteignable depuis s (True si s == t), False sinon, en utilisant un parcours en profondeur.

**Q3** (1 pt, parcours_graphe) Écrire la fonction accessible(g, s, t).

<details><summary>Corrigé</summary>

```python
def accessible(g, s, t):
    vus = set()
    pile = [s]
    while pile:
        u = pile.pop()
        if u == t:
            return True
        if u not in vus:
            vus.add(u)
            for v in g[u]:
                pile.append(v)
    return False
```

</details>

### Exercice 4 — Dépendances de processus

Le tableau ci-dessous décrit quatre processus : durée d'exécution (en cycles), instant d'arrivée (en cycles depuis 0), numéro de priorité, et processus dont il dépend (il ne peut démarrer qu'après la fin de celui-ci).

| Processus | Durée | Arrivée | Priorité | Dépend de |
|---|---|---|---|---|
| P1 | 3 | 0 | 2 | — |
| P2 | 2 | 1 | 1 | P1 |
| P3 | 4 | 1 | 3 | P1 |
| P4 | 1 | 2 | 1 | P2, P3 |

On modélise les dépendances par un graphe orienté (arc de X vers Y si Y dépend de X).

**Q4** (1 pt, parcours_graphe) À partir du tableau ci-dessus, donner la liste des successeurs de chaque sommet puis un ordre d'exécution des processus compatible avec toutes les dépendances.

<details><summary>Corrigé</summary>

Successeurs : P1 → [P2, P3] ; P2 → [P4] ; P3 → [P4] ; P4 → []. Ordre possible : P1, P2, P3, P4 (ou P1, P3, P2, P4).

</details>

## I-pile
### Exercice 1 — Hauteur maximale d'une pile

Un tableau d'entiers t décrit une suite d'opérations sur une pile initialement vide (chaque entier strictement positif signifie « empiler cet entier », chaque 0 signifie « dépiler » ; on suppose qu'on ne dépile jamais une pile vide). Exemple : pour t = [4, 7, 0, 2, 5, 0, 0, 9] la pile atteint au plus 3 éléments.

**Q1** (1 pt, pile) Écrire une fonction hauteur_max(t) (paramètre : un tableau d'entiers positifs ou nuls) qui renvoie le nombre maximal d'éléments présents simultanément dans la pile.

<details><summary>Corrigé</summary>

def hauteur_max(t):
    h = 0
    m = 0
    for x in t:
        if x == 0:
            h = h - 1
        else:
            h = h + 1
            if h > m:
                m = h
    return m

assert hauteur_max([4, 7, 0, 2, 5, 0, 0, 9]) == 3

</details>

### Exercice 2 — Annuler dans un éditeur

Un éditeur de texte mémorise chaque action de l'utilisateur (saisie, suppression, mise en gras) dans une structure historique ; la commande « Annuler » (Ctrl+Z) défait toujours l'action la plus récente non encore annulée (et peut être répétée plusieurs fois).

**Q2** (1 pt, pile) Expliquer pourquoi une pile, plutôt qu'une file, est la structure adaptée pour stocker l'historique des actions.

<details><summary>Corrigé</summary>

Annuler doit défaire d'abord la dernière action effectuée, puis l'avant-dernière, etc. : c'est le principe LIFO (dernier entré, premier sorti) de la pile ; une file (FIFO) renverrait la plus ancienne action, ce qui est incorrect.

</details>

### Exercice 3 — Choisir la structure

Pour chacune des situations suivantes, on hésite entre une pile et une file :
- a. l'impression de documents envoyés à une imprimante partagée ;
- b. le bouton « Page précédente » d'un navigateur web ;
- c. la vérification du bon parenthésage d'une expression.

**Q3** (1 pt, pile) Quelle structure (pile ou file) convient à chacune des situations a, b et c ? Justifier brièvement.

<details><summary>Corrigé</summary>

a. file (premier envoyé, premier imprimé, FIFO) ; b. pile (on revient à la dernière page visitée, LIFO) ; c. pile (chaque parenthèse fermante correspond à la dernière ouvrante non fermée, LIFO).

</details>

### Exercice 4 — Mode de fonctionnement d'une pile

On empile successivement les valeurs 3, 8 puis 5 dans une pile vide p, puis on exécute une fois depile(p).

**Q4** (1 pt, pile) Donner le nom (et la signification) du mode de fonctionnement d'une pile, puis la valeur renvoyée par depile(p).

<details><summary>Corrigé</summary>

Mode LIFO (Last In, First Out : dernier entré, premier sorti) ; depile(p) renvoie 5.

</details>

## I-poo
### Exercice 1 — Compter les instances

On dispose de la classe suivante (attention : compteur est un attribut de classe, partagé par toutes les instances) :

class Ticket:
    compteur = 0
    def __init__(self, nom):
        self.nom = nom
        Ticket.compteur = Ticket.compteur + 1

On exécute : t1 = Ticket('A') ; t2 = Ticket('B') ; t3 = t1 ; t4 = Ticket('C').

**Q1** (1 pt, poo) Donner la valeur de Ticket.compteur après ces instructions et le nombre d'objets Ticket distincts créés.

<details><summary>Corrigé</summary>

Ticket.compteur vaut 3 : trois objets ont été construits ; t3 = t1 ne crée pas d'objet (même référence).

</details>

### Exercice 2 — Identifiant d'un adhérent

Une médiathèque modélise ses adhérents par une classe Adherent dont les attributs sont numero, nom et prenom. Le numero est attribué à l'inscription, unique pour chaque adhérent, et jamais réutilisé. Plusieurs adhérents peuvent porter le même nom et le même prénom. Les objets Emprunt possèdent un attribut num_adherent.

**Q2** (1 pt, poo) Expliquer le rôle de l'attribut numero de la classe Adherent, et celui de l'attribut num_adherent d'un objet Emprunt.

<details><summary>Corrigé</summary>

numero identifie de façon unique un adhérent (comme une clé), car nom/prénom ne suffisent pas ; num_adherent référence l'adhérent emprunteur et relie l'emprunt à un unique objet Adherent.

</details>

### Exercice 3 — Méthode sur une chaîne

On considère la classe :

class Mot:
    def __init__(self, texte):
        self.texte = texte

**Q3** (1 pt, poo) Écrire une méthode est_palindrome(self) de la classe Mot qui renvoie True si l'attribut texte se lit de la même façon dans les deux sens, False sinon.

<details><summary>Corrigé</summary>

class Mot:
    def __init__(self, texte):
        self.texte = texte

    def est_palindrome(self):
        n = len(self.texte)
        for i in range(n // 2):
            if self.texte[i] != self.texte[n - 1 - i]:
                return False
        return True

assert Mot('radar').est_palindrome()
assert not Mot('route').est_palindrome()

</details>

### Exercice 4 — Hauteur d'un arbre objet

Un arbre binaire est représenté par la classe suivante ; l'arbre vide est représenté par None et la hauteur d'un arbre réduit à une feuille vaut 1 :

class Arbre:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

**Q4** (1 pt, poo) Écrire la méthode hauteur(self) de la classe Arbre qui renvoie la hauteur de l'arbre.

<details><summary>Corrigé</summary>

class Arbre:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

    def hauteur(self):
        hg = 0 if self.gauche is None else self.gauche.hauteur()
        hd = 0 if self.droit is None else self.droit.hauteur()
        return 1 + max(hg, hd)

a = Arbre(1, Arbre(2, Arbre(4)), Arbre(3))
assert a.hauteur() == 3

</details>

## I-processus
### Exercice 1 — Graphe d'attente

La figure 1 décrit la situation suivante : le processus P1 détient la ressource R1 et attend R2 ; le processus P2 détient R2 et attend R3 ; le processus P3 détient R3 et attend R1. Dans la figure 1, une flèche Pi → Rj signifie « Pi attend Rj » et Rj → Pi signifie « Rj est détenue par Pi ».

**Q1** (1 pt, processus) À partir de la figure 1, déterminer si les processus sont en situation d'interblocage. Justifier.

<details><summary>Corrigé</summary>

Oui : la figure contient le cycle P1 → R2 → P2 → R3 → P3 → R1 → P1 ; chaque processus attend une ressource détenue par le suivant, aucun ne peut progresser : interblocage.

</details>

### Exercice 2 — Chemin d'un processus

Un processus est créé puis passe à l'état prêt. L'ordonnanceur l'élit. Après 20 ms il demande une lecture disque, puis la lecture se termine, il est de nouveau élu et termine son exécution.

**Q2** (1 pt, processus) Donner la suite des états (prêt, élu, bloqué, terminé) par lesquels passe ce processus.

<details><summary>Corrigé</summary>

prêt → élu → bloqué → prêt → élu → terminé.

</details>

### Exercice 3 — Commande Unix

Sur un serveur Linux, un administrateur constate qu'un programme de calcul consomme toute la mémoire. Il exécute la commande ps qui affiche notamment la ligne « 4187 pts/0 00:12:41 calcul ». Il souhaite arrêter ce seul processus.

**Q3** (1 pt, processus) Donner la commande à saisir pour interrompre ce processus.

<details><summary>Corrigé</summary>

kill 4187 (4187 est le PID du processus calcul).

</details>

### Exercice 4 — Ordonnancement FIFO

Quatre processus arrivent tous à l'instant 0 dans la file et y sont placés dans l'ordre C1, C2, C3 et C4. Leurs durées d'exécution sont respectivement 4, 2, 3 et 1 unités de temps. L'ordonnanceur suit la politique « premier arrivé, premier servi », sans interruption.

**Q4** (1 pt, processus) Donner l'instant de fin d'exécution de chacun des quatre processus.

<details><summary>Corrigé</summary>

C1 : 4 ; C2 : 6 ; C3 : 9 ; C4 : 10.

</details>

## I-prog_dynamique
### Exercice 1 — Appels de Fibonacci

On considère la fonction récursive naïve :

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

En programmation dynamique (mémoïsation), chaque valeur fib(k) n'est calculée qu'une fois, ce qui minimise le nombre d'opérations.

**Q1** (1 pt, prog_dynamique) Dénombrer le nombre total d'appels à fib lors de l'exécution de fib(5) avec la version naïve, puis le nombre de valeurs distinctes calculées avec la version mémoïsée.

<details><summary>Corrigé</summary>

Version naïve : 15 appels (A(n)=1+A(n-1)+A(n-2), A(0)=A(1)=1 : A(2)=3, A(3)=5, A(4)=9, A(5)=15). Version mémoïsée : 6 valeurs distinctes fib(0) à fib(5).

</details>

## I-recherche_dichotomique
### Exercice 1 — Compléter la dichotomie

On donne la fonction à compléter :

1 def recherche(tab, val):
2     debut = 0
3     fin = len(tab) - 1
4     while debut <= fin:
5         milieu = (debut + fin) // 2
6         if tab[milieu] == val:
7             return True
8         elif tab[milieu] < val:
9             ...
10        else:
11            ...
12    return False

**Q1** (1 pt, recherche_dichotomique) Compléter les lignes 9 et 11 de la fonction recherche.

<details><summary>Corrigé</summary>

def recherche(tab, val):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == val:
            return True
        elif tab[milieu] < val:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return False

assert recherche([1, 5, 7, 9, 12, 13], 12)
assert not recherche([1, 5, 7, 9, 12, 13], 17)

</details>

### Exercice 2 — Tableaux candidats

On souhaite appliquer une recherche dichotomique sur l'un des tableaux suivants :
- t1 = [2, 9, 4, 11, 15]
- t2 = [3, 3, 8, 14, 20]
- t3 = [20, 14, 8, 3, 1]

**Q2** (1 pt, recherche_dichotomique) Sur quel(s) tableau(x) la recherche dichotomique croissante classique fonctionne-t-elle correctement ? Justifier.

<details><summary>Corrigé</summary>

Seulement t2 : il est trié dans l'ordre croissant (les doublons n'empêchent pas la recherche). t1 n'est pas trié, t3 est trié décroissant.

</details>

### Exercice 3 — Complexité

Un annuaire numérique contient un million de noms triés par ordre alphabétique. Le logiciel cherche un nom en comparant au nom situé au milieu de la zone restante, puis ne garde que la moitié pertinente.

**Q3** (1 pt, recherche_dichotomique) Donner le nom de cet algorithme et sa complexité en temps en fonction du nombre n de noms.

<details><summary>Corrigé</summary>

Recherche dichotomique ; complexité logarithmique O(log2 n).

</details>

### Exercice 4 — Nombre d'étapes

À chaque étape, la recherche dichotomique divise par deux la taille de la zone de travail. On l'applique à un tableau trié de 1000 éléments, la valeur cherchée étant absente.

**Q4** (1 pt, recherche_dichotomique) Dénombrer le nombre maximal de tours de boucle effectués.

<details><summary>Corrigé</summary>

10 tours au plus (2^9 = 512 < 1000 < 1024 = 2^10 ; la taille passe 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1).

</details>

## I-recherche_textuelle
### Exercice 1 — Positions d'un motif

On donne la fonction naïve :

def positions(texte, motif):
    res = []
    for i in range(len(texte) - len(motif) + 1):
        if texte[i:i + len(motif)] == motif:
            res.append(i)
    return res

On considère l'appel positions('1011010110', '101').

**Q1** (1 pt, recherche_textuelle) Donner la valeur renvoyée par cet appel.

<details><summary>Corrigé</summary>

[0, 3, 5]

</details>

### Exercice 2 — Arrêt à la première occurrence

On souhaite réécrire l'algorithme naïf de recherche d'un motif pour qu'il s'arrête dès qu'une occurrence du motif est trouvée (renvoyer sa position, ou -1).

**Q2** (1 pt, recherche_textuelle) Expliquer en quoi cette modification réduit le nombre de comparaisons, et écrire la fonction premiere(texte, motif).

<details><summary>Corrigé</summary>

On ne parcourt plus la suite du texte une fois l'occurrence trouvée : dans le meilleur cas, on économise presque tout le parcours.

def premiere(texte, motif):
    n, m = len(texte), len(motif)
    for i in range(n - m + 1):
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j = j + 1
        if j == m:
            return i
    return -1

assert premiere('abracadabra', 'cad') == 4
assert premiere('abc', 'z') == -1

</details>

## I-recursivite
### Exercice 1 — Somme des chiffres

Un club de calcul mental veut vérifier la somme des chiffres d'un entier naturel. On propose la fonction suivante :

```python
def somme_chiffres(n):
    if n < 10:
        return n
    return n % 10 + somme_chiffres(n // 10)
```

On appelle somme_chiffres(4071). Chaque appel récursif est empilé dans la pile d'appels.

**Q1** (1 pt, recursivite) Donner le nombre total d'appels de la fonction somme_chiffres effectués lors de l'appel somme_chiffres(4071), ainsi que la valeur renvoyée.

<details><summary>Corrigé</summary>

4 appels (4071, 407, 40, 4) ; valeur renvoyée : 12.

</details>

### Exercice 2 — Reste par soustractions

On souhaite calculer le reste de la division euclidienne de a par b (a ≥ 0, b > 0) sans utiliser l'opérateur %, à l'aide d'une fonction récursive _mod(a, b). On trace les appels successifs dans un tableau, à la manière d'une table de routage où chaque ligne indique l'appel courant et l'appel « suivant » :

| Appel courant | Appel suivant | Valeur renvoyée |
|---|---|---|
| _mod(17, 5) | _mod(12, 5) | ? |
| _mod(12, 5) | ? | ? |
| ? | ? | ? |
| _mod(2, 5) | aucun (cas de base) | 2 |

**Q2** (1 pt, recursivite) Écrire la fonction récursive _mod(a, b) puis recopier et compléter le tableau des appels pour _mod(17, 5).

<details><summary>Corrigé</summary>

```python
def _mod(a, b):
    if a < b:
        return a
    return _mod(a - b, b)

print(_mod(17, 5))  # 2
```
Tableau : _mod(17,5) -> _mod(12,5) -> 2 ; _mod(12,5) -> _mod(7,5) -> 2 ; _mod(7,5) -> _mod(2,5) -> 2 ; _mod(2,5) : cas de base, renvoie 2.

</details>

## I-representation_nombres
### Exercice 1 — Conversion en binaire

Un capteur transmet des entiers naturels compris entre 0 et 255 sur 8 bits. La fonction ci-dessous doit renvoyer la chaîne de 8 caractères '0'/'1' représentant n en binaire ; par exemple binaire8(13) renvoie '00001101'.

```
1 def binaire8(n):
2     s = ''
3     for i in range(8):
4         s = ... + s
5         n = ...
6     return s
```

**Q1** (1 pt, representation_nombres) Recopier et compléter les lignes 4 et 5 de la fonction binaire8.

<details><summary>Corrigé</summary>

```python
def binaire8(n):
    s = ''
    for i in range(8):
        s = str(n % 2) + s
        n = n // 2
    return s

print(binaire8(13))  # '00001101'
```

</details>

### Exercice 2 — Somme de flottants

On exécute en Python les instructions suivantes :

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.5 + 0.25
0.75
>>> 0.1 + 0.2 == 0.3
False
```

**Q2** (1 pt, representation_nombres) Expliquer pourquoi 0.5 + 0.25 est calculé exactement alors que 0.1 + 0.2 ne donne pas exactement 0.3.

<details><summary>Corrigé</summary>

Les flottants sont stockés en binaire sur un nombre fini de bits. 0.5 = 2^-1 et 0.25 = 2^-2 ont une écriture binaire finie, donc sont représentés exactement. 0.1 et 0.2 ont une écriture binaire infinie périodique : ils sont arrondis, et la somme des approximations diffère de l'approximation de 0.3.

</details>

### Exercice 3 — Codage d'une température

Une station météo doit stocker des températures entières comprises entre -40 °C et +60 °C. Le concepteur dispose de mots de 8 bits et hésite sur la façon de représenter les valeurs négatives.

**Q3** (1 pt, representation_nombres) Proposer une représentation sur 8 bits permettant de coder toutes ces températures, et donner le code de -40 avec cette représentation.

<details><summary>Corrigé</summary>

Par exemple le complément à deux sur 8 bits (de -128 à 127, suffisant). -40 : 40 = 00101000, inversion 11010111, +1 → 11011000. (Autre solution valable : décalage de +40, -40 codé 00000000.)

</details>

### Exercice 4 — Coût OSPF et débits

Dans un réseau utilisant OSPF, le coût d'une liaison est calculé par la formule coût = 10^8 / d, où d est le débit en bits/s. Les débits sont notés en puissances de 10 :
- A–B : 10^8 bit/s (Fast Ethernet)
- A–C : 10^7 bit/s
- C–B : 10^9 bit/s
- B–D : 10^7 bit/s
- C–D : 10^8 bit/s

**Q4** (1 pt, representation_nombres) Déterminer le coût de chaque liaison puis le chemin de coût minimal de A vers D.

<details><summary>Corrigé</summary>

Coûts : A–B = 1, A–C = 10, C–B = 0,1, B–D = 10, C–D = 1. Chemins : A-B-D = 11 ; A-C-D = 11 ; A-B-C-D = 1 + 0,1 + 1 = 2,1. Chemin minimal : A → B → C → D (coût 2,1).

</details>

## I-reseau_ip
### Exercice 1 — Nouvel ordinateur

Le réseau local d'un CDI a pour adresse 192.168.20.0/24. Le routeur utilise 192.168.20.254 et les postes existants vont de 192.168.20.1 à 192.168.20.30.

**Q1** (1 pt, reseau_ip) Proposer une adresse IP et un masque pour un nouvel ordinateur du CDI.

<details><summary>Corrigé</summary>

Par exemple 192.168.20.31 avec le masque 255.255.255.0 (toute adresse libre de 192.168.20.31 à 192.168.20.253 convient, ni .0 ni .255).

</details>

### Exercice 2 — Adresse sous forme de tableau

Dans un logiciel de supervision, une adresse IPv4 est représentée par un tableau de 4 entiers, par exemple [192, 168, 1, 37]. Le masque est représenté de la même façon, par exemple [255, 255, 255, 0]. L'adresse du réseau s'obtient en faisant, octet par octet, un ET logique (opérateur & en Python) entre l'adresse et le masque.

**Q2** (1 pt, reseau_ip) Écrire une fonction adresse_reseau(ip, masque) qui prend en paramètres deux tableaux de 4 entiers et renvoie le tableau de 4 entiers de l'adresse du réseau.

<details><summary>Corrigé</summary>

```python
def adresse_reseau(ip, masque):
    res = []
    for i in range(4):
        res.append(ip[i] & masque[i])
    return res

print(adresse_reseau([192, 168, 1, 37], [255, 255, 255, 0]))  # [192, 168, 1, 0]
```

</details>

### Exercice 3 — Configuration d'un poste

La commande ip addr exécutée sur un poste affiche notamment les informations suivantes :
- interface : eth0
- adresse : 172.16.5.12/22
- passerelle par défaut : 172.16.4.1
- adresse de diffusion : ?

**Q3** (1 pt, reseau_ip) À l'aide des informations ci-dessus, donner l'adresse du réseau et l'adresse de diffusion du réseau de ce poste.

<details><summary>Corrigé</summary>

/22 → masque 255.255.252.0. 5 = 000001|01 → troisième octet réseau 4. Réseau : 172.16.4.0 ; diffusion : 172.16.7.255.

</details>

### Exercice 4 — Masque et partie hôte

Une entreprise reçoit le réseau 10.4.0.0 avec le masque 255.255.240.0. Le cours rappelle qu'on associe une adresse IP et un masque pour savoir quelle partie de l'adresse identifie le réseau et quelle partie identifie la machine.

**Q4** (1 pt, reseau_ip) Donner la notation CIDR de ce masque, indiquer combien de bits identifient la machine, puis justifier le nombre maximal de machines adressables.

<details><summary>Corrigé</summary>

255.255.240.0 = /20. 32 - 20 = 12 bits pour la machine. 2^12 - 2 = 4094 machines (on retire l'adresse du réseau et celle de diffusion).

</details>

## I-routage
### Exercice 1 — Protocole à état de liens

Une collectivité relie ses médiathèques par des routeurs. L'administrateur souhaite que chaque routeur connaisse toute la topologie du réseau et choisisse les routes en tenant compte du débit des liaisons, et non du simple nombre de sauts.

**Q1** (1 pt, routage) Donner le nom du protocole de routage adapté à cette demande et le nom de l'algorithme de calcul de plus court chemin qu'il utilise.

<details><summary>Corrigé</summary>

OSPF ; algorithme de Dijkstra.

</details>

### Exercice 2 — Métrique RIP

Le routeur R1 utilise le protocole RIP. Il connaît les routes suivantes vers le réseau 10.8.0.0/16 :
- via R2 : 3 sauts
- via R3 : 2 sauts
- via R4 : 5 sauts

**Q2** (1 pt, routage) Donner le routeur choisi par R1 comme passerelle vers 10.8.0.0/16 et la métrique inscrite dans sa table.

<details><summary>Corrigé</summary>

R3, métrique 2.

</details>

### Exercice 3 — Réseau d'entreprise

Le réseau d'une entreprise comporte quatre routeurs reliés ainsi : R1–R2, R1–R3, R2–R4, R3–R4. Le réseau local LAN-A (192.168.1.0/24) est relié à R1 et le réseau LAN-B (192.168.4.0/24) est relié à R4. Le protocole RIP est utilisé ; la métrique est le nombre de sauts (routeurs à traverser) et, en cas d'égalité, on choisit la passerelle de plus petit numéro.

Table de R1 (extrait) :

| Destination | Passerelle | Métrique |
|---|---|---|
| 192.168.1.0/24 | directe | 0 |
| 192.168.4.0/24 | ? | ? |

**Q3** (1 pt, routage) Recopier et compléter la ligne de la table de routage de R1 vers le réseau 192.168.4.0/24.

<details><summary>Corrigé</summary>

192.168.4.0/24 | R2 | 2 (R1 → R2 → R4, égalité avec R3, on choisit R2).

</details>

## I-securite_crypto
### Exercice 1 — Chiffrement de César

On chiffre un message écrit en lettres majuscules (A à Z) et espaces par un décalage. La fonction cesar prend en paramètres une chaîne message et un entier cle compris entre 0 et 25, renvoie une nouvelle chaîne où chaque lettre est décalée de cle positions dans l'alphabet (Z suivi de A), laisse les espaces inchangés. On rappelle que ord('A') vaut 65 et que chr est la fonction réciproque de ord.

**Q1** (1 pt, securite_crypto) Écrire la fonction cesar(message, cle) et donner la valeur de cesar('ZOO', 3).

<details><summary>Corrigé</summary>

```python
def cesar(message, cle):
    res = ''
    for c in message:
        if c == ' ':
            res = res + c
        else:
            res = res + chr((ord(c) - 65 + cle) % 26 + 65)
    return res

print(cesar('ZOO', 3))  # 'CRR'
```

</details>

### Exercice 2 — Échange de clés

Alice veut envoyer un document volumineux à Bob de façon confidentielle. Elle chiffre le document avec une clé AES générée aléatoirement, puis chiffre cette clé AES avec la clé publique de Bob avant de tout lui envoyer.

**Q2** (1 pt, securite_crypto) Donner le nom de ce type de chiffrement combinant les deux méthodes, et la clé que Bob utilise pour retrouver la clé AES.

<details><summary>Corrigé</summary>

Chiffrement hybride ; Bob utilise sa clé privée.

</details>

### Exercice 3 — Choix de la clé

Bob possède une paire de clés RSA. Charlie veut lui envoyer un message que seul Bob pourra lire. Clés disponibles :
- clé publique de Bob
- clé privée de Bob
- clé publique de Charlie
- clé privée de Charlie

**Q3** (1 pt, securite_crypto) Quelle clé Charlie doit-il utiliser pour chiffrer son message ? Justifier.

<details><summary>Corrigé</summary>

La clé publique de Bob : seule la clé privée correspondante, connue de Bob uniquement, permet de déchiffrer.

</details>

### Exercice 4 — Partage d'une clé secrète

Une entreprise utilise un chiffrement symétrique pour protéger ses échanges avec 50 partenaires. Le cours précise qu'un chiffrement est dit symétrique lorsque la connaissance de la clé ayant servi au chiffrement permet de déchiffrer le message.

**Q4** (1 pt, securite_crypto) Expliquer pourquoi la transmission de la clé est le point faible de ce mode de chiffrement.

<details><summary>Corrigé</summary>

La même clé chiffre et déchiffre : si elle est interceptée lors de sa transmission, l'attaquant peut lire tous les messages. Il faut donc un canal sûr pour l'échanger avec chaque partenaire (50 clés distinctes), ce qui est difficile.

</details>

## I-sgbd
### Exercice 1 — Requête depuis Python

Un script interroge une base SQLite contenant la table eleve(id, nom, classe) remplie avec : (1, 'Lina', 'T1'), (2, 'Hugo', 'T2'), (3, 'Malo', 'T1').

```python
import sqlite3
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute("CREATE TABLE eleve (id INTEGER PRIMARY KEY, nom TEXT, classe TEXT)")
cur.executemany("INSERT INTO eleve VALUES (?, ?, ?)", [(1, 'Lina', 'T1'), (2, 'Hugo', 'T2'), (3, 'Malo', 'T1')])
cur.execute("SELECT nom FROM eleve WHERE classe = 'T1' ORDER BY nom DESC")
res = cur.fetchall()
```

**Q1** (1 pt, sgbd) Donner la valeur de la variable res après l'exécution de ce script.

<details><summary>Corrigé</summary>

[('Malo',), ('Lina',)]

</details>

### Exercice 2 — Propriétés d'un SGBD

Une médiathèque remplace ses fichiers tableurs par un système de gestion de base de données. On liste des services possibles :
- gestion des accès concurrents de plusieurs utilisateurs
- mise en forme graphique des cellules
- vérification des contraintes d'intégrité
- persistance et sécurisation des données

**Q2** (1 pt, sgbd) Quel service de la liste n'est pas assuré par un SGBD ? Justifier.

<details><summary>Corrigé</summary>

La mise en forme graphique des cellules : c'est une fonction de tableur ; un SGBD gère le stockage, l'intégrité, la concurrence et la sécurité des données, pas leur présentation.

</details>

### Exercice 3 — Transaction

On donne le code suivant, qui transfère des points entre deux comptes d'une base SQLite :

```
1 import sqlite3
2 conn = sqlite3.connect(':memory:')
3 cur = conn.cursor()
4 cur.execute("CREATE TABLE compte (id INTEGER PRIMARY KEY, points INTEGER CHECK (points >= 0))")
5 cur.execute("INSERT INTO compte VALUES (1, 10), (2, 5)")
6 conn.commit()
7 try:
8     cur.execute("UPDATE compte SET points = points + 20 WHERE id = 2")
9     cur.execute("UPDATE compte SET points = points - 20 WHERE id = 1")
10    conn.commit()
11 except sqlite3.IntegrityError:
12    conn.rollback()
```

**Q3** (1 pt, sgbd) Indiquer les points des comptes 1 et 2 à la fin de l'exécution en expliquant le rôle de la ligne 12.

<details><summary>Corrigé</summary>

La ligne 9 viole la contrainte CHECK (10 - 20 < 0) : exception, rollback annule aussi la ligne 8. Compte 1 : 10 points, compte 2 : 5 points. La ligne 12 garantit l'atomicité de la transaction.

</details>

### Exercice 4 — Langage d'un SGBD-R

La plupart des SGBD-R (R de relationnelle) utilisent le langage SQL, Structured Query Language. Un développeur d'application web interroge le SGBD de son site pour afficher la liste des produits.

**Q4** (1 pt, sgbd) Donner la signification de l'acronyme SGBD-R et préciser le rôle du langage SQL dans les échanges entre l'application et le SGBD.

<details><summary>Corrigé</summary>

Système de Gestion de Bases de Données Relationnelles. SQL est le langage de requêtes que l'application envoie au SGBD pour créer, lire, modifier ou supprimer des données ; le SGBD exécute la requête et renvoie le résultat.

</details>

## I-soc_architecture
### Exercice 1 — Composants d'un SoC

Un SoC de montre connectée est modélisé en Python par un dictionnaire associant à chaque composant intégré sa fonction :

```python
1| soc = {'CPU': 'calcul', 'GPU': 'affichage', 'RAM': 'memoire',
2|        'modem': 'communication', 'DSP': 'signal'}
3| def composants(soc, fonction):
4|     res = []
5|     for c in soc:
6|         if soc[c] == fonction:
7|             res.append(c)
8|     return res
```

**Q1** (1 pt, soc_architecture) Donner la valeur renvoyée par composants(soc, 'communication') et expliquer ce que fait la fonction composants.

<details><summary>Corrigé</summary>

['modem'] : la fonction renvoie la liste des composants du SoC qui assurent la fonction passée en paramètre.

</details>

### Exercice 2 — Consommation d'un SoC

Un SoC regroupe sur une même puce plusieurs composants. Les puissances consommées (en mW) par ses composants sont données dans la liste p = [450, 300, 120, 80, 50] (CPU, GPU, RAM, modem, contrôleur USB). On exécute :

```python
total = 0
for x in p[1:4]:
    total = total + x
```

**Q2** (1 pt, soc_architecture) Donner la valeur de total après l'exécution de ces instructions.

<details><summary>Corrigé</summary>

total = 300 + 120 + 80 = 500

</details>

### Exercice 3 — Avantages d'un SoC

On liste les propositions suivantes concernant un système sur puce (SoC) :
- a. il réduit la distance entre les composants ;
- b. il permet de remplacer facilement la mémoire vive par une barrette plus grande ;
- c. il consomme généralement moins d'énergie qu'un ensemble de composants séparés ;
- d. il nécessite obligatoirement un ventilateur.

**Q3** (1 pt, soc_architecture) Quelles propositions décrivent correctement un avantage d'un SoC ? Justifier.

<details><summary>Corrigé</summary>

a et c : les composants étant intégrés sur une même puce, les connexions sont plus courtes, ce qui accélère les échanges et réduit la consommation. b est faux (composants soudés/intégrés, non remplaçables), d est faux (faible dissipation, souvent refroidissement passif).

</details>

### Exercice 4 — Communication d'un smartphone

Le SoC d'un smartphone intègre notamment un CPU, un GPU, une mémoire, un contrôleur d'écran et des modules de communication sans fil.

**Q4** (1 pt, soc_architecture) Quel élément d'un SoC permet à un smartphone de communiquer avec d'autres machines ?

<details><summary>Corrigé</summary>

Le modem (et les contrôleurs radio Wi-Fi/Bluetooth) intégré au SoC, qui gère les communications réseau (4G/5G).

</details>

## I-sql
### Exercice 1 — Requêtes d'une médiathèque

Une médiathèque utilise la table Emprunt(id, titre, adherent, duree) où duree est le nombre de jours d'emprunt. Le responsable souhaite :
- connaître les titres empruntés plus de 21 jours ;
- trier ces titres par ordre alphabétique ;
- ne pas afficher de doublons.

**Q1** (1 pt, sql) Écrire une requête SQL répondant à l'ensemble de ces besoins.

<details><summary>Corrigé</summary>

SELECT DISTINCT titre FROM Emprunt WHERE duree > 21 ORDER BY titre;

</details>

### Exercice 2 — Agence de location

La base de données locations.db contient les tables Agences(id_agence, ville), Vehicules(immat, modele, id_agence) et Locations(id_loc, immat, date_debut, date_fin). L'attribut id_agence de Vehicules est une clé étrangère vers Agences, immat de Locations est une clé étrangère vers Vehicules.

**Q2** (1 pt, sql) Écrire une requête SQL donnant les immatriculations des véhicules loués au moins une fois, appartenant à l'agence de la ville 'Lyon'.

<details><summary>Corrigé</summary>

SELECT DISTINCT Vehicules.immat FROM Vehicules JOIN Agences ON Vehicules.id_agence = Agences.id_agence JOIN Locations ON Locations.immat = Vehicules.immat WHERE Agences.ville = 'Lyon';

</details>

## I-tableau_liste
### Exercice 1 — Liste chaînée de stations

Une ligne de bus est représentée par une liste chaînée de stations : chaque cellule contient un nom de station et une référence vers la cellule suivante. On accède aux stations depuis la tête.

**Q1** (1 pt, tableau_liste) Donner le nombre de cellules à parcourir pour atteindre la 5e station d'une liste chaînée, et comparer avec l'accès à l'élément d'indice 4 d'un tableau Python.

<details><summary>Corrigé</summary>

Il faut parcourir 5 cellules (coût linéaire), alors que l'accès t[4] dans un tableau se fait en temps constant.

</details>

### Exercice 2 — Moyenne des températures

Un capteur relève 24 températures par jour, stockées dans un tableau temp de 24 nombres. On veut calculer la moyenne :

```python
1| def moyenne(temp):
2|     s = ...
3|     for i in range(...):
4|         s = ...
5|     return s / len(temp)
```

**Q2** (1 pt, tableau_liste) Recopier et compléter les lignes 2, 3 et 4 de la fonction moyenne.

<details><summary>Corrigé</summary>

def moyenne(temp):
    s = 0
    for i in range(len(temp)):
        s = s + temp[i]
    return s / len(temp)

</details>

### Exercice 3 — Tableau de scores

Lors d'un tournoi, les scores des équipes sont rangés dans un tableau scores = [12, 7, 15, 9, 15, 3]. L'équipe numéro i a son score dans scores[i], la première équipe ayant le numéro 0. Le règlement indique que l'équipe ayant le plus grand score et le plus petit numéro l'emporte.

**Q3** (1 pt, tableau_liste) Donner le numéro de l'équipe gagnante et la valeur de scores[len(scores) - 1].

<details><summary>Corrigé</summary>

Équipe 2 (score 15, avant l'équipe 4) ; scores[5] = 3.

</details>

### Exercice 4 — Arbre binaire dans un tableau

Un arbre binaire de taille n est stocké dans un tableau : la case d'indice 0 contient n, la racine a pour indice 1, le fils gauche du nœud d'indice i a pour indice 2*i, le fils droit 2*i+1. On considère t = [5, 'A', 'B', 'C', 'D', 'E'].

**Q4** (1 pt, tableau_liste) Donner les fils du nœud 'B' et l'indice du père du nœud d'indice i (i > 1).

<details><summary>Corrigé</summary>

Fils de 'B' (indice 2) : 'D' (indice 4) et 'E' (indice 5). Le père du nœud d'indice i a pour indice i // 2.

</details>

## I-tri
### Exercice 1 — Classement d'un club

Un club de course stocke ses résultats dans une table Course(id, nom, temps). On souhaite obtenir les coureurs classés du plus rapide au plus lent, ce que l'on pourrait aussi faire en Python avec un tri fusion sur la liste des temps.

**Q1** (1 pt, tri) Écrire la requête SQL qui renvoie le nom et le temps des coureurs triés par temps croissant, puis donner le coût du tri fusion sur n éléments.

<details><summary>Corrigé</summary>

SELECT nom, temps FROM Course ORDER BY temps ASC; Le tri fusion a un coût en O(n log n).

</details>

## I-tuple
### Exercice 1 — Points d'un parcours

Un parcours est une liste de points représentés par des tuples (x, y) :

```python
parcours = [(0, 0), (3, 4), (3, 7)]
p = parcours[1]
x, y = p
parcours[2] = (x + 1, y)
```

**Q1** (1 pt, tuple) Donner le contenu de parcours après exécution et expliquer pourquoi l'instruction p[0] = 5 provoquerait une erreur.

<details><summary>Corrigé</summary>

[(0, 0), (3, 4), (4, 4)] ; un tuple est immuable, on ne peut pas modifier ses éléments (TypeError).

</details>

### Exercice 2 — Élève le plus âgé

Chaque élève est un tuple (nom, age) :

```python
1| def plus_age(eleves):
2|     meilleur = eleves[0]
3|     for e in eleves:
4|         if ...:
5|             meilleur = ...
6|     return meilleur[0]
```

**Q2** (1 pt, tuple) Recopier et compléter les lignes 4 et 5 pour que la fonction renvoie le nom de l'élève le plus âgé.

<details><summary>Corrigé</summary>

def plus_age(eleves):
    meilleur = eleves[0]
    for e in eleves:
        if e[1] > meilleur[1]:
            meilleur = e
    return meilleur[0]

</details>

### Exercice 3 — Bornes d'une liste

La fonction bornes prend en paramètre une liste non vide d'entiers L, parcourt la liste une seule fois, et renvoie un tuple (mini, maxi) contenant la plus petite et la plus grande valeur de L.

**Q3** (1 pt, tuple) Écrire la fonction bornes.

<details><summary>Corrigé</summary>

def bornes(L):
    mini = L[0]
    maxi = L[0]
    for x in L:
        if x < mini:
            mini = x
        if x > maxi:
            maxi = x
    return (mini, maxi)

</details>

### Exercice 4 — Vecteurs de distance

Dans le protocole RIP, un routeur envoie à ses voisins des vecteurs de distance, couples (adresse, distance). Le routeur R reçoit de son voisin les vecteurs [('10.0.1.0', 2), ('10.0.2.0', 0)].

**Q4** (1 pt, tuple) Justifier le choix d'un tuple pour représenter un vecteur de distance, puis donner les vecteurs que R enregistre pour ces réseaux.

<details><summary>Corrigé</summary>

Un vecteur est une donnée fixe de deux composantes hétérogènes qu'on ne modifie pas : le tuple, immuable, convient. R ajoute 1 à chaque distance : ('10.0.1.0', 3) et ('10.0.2.0', 1).

</details>

## I-web_http
### Exercice 1 — Analyse d'une URL

Une URL est une chaîne de la forme 'protocole://hote/chemin', par exemple 'https://www.lycee.fr/index.html'. La fonction protocole prend en paramètre une URL url, parcourt ses caractères jusqu'au premier ':', et renvoie la chaîne formée des caractères précédents.

**Q1** (1 pt, web_http) Écrire la fonction protocole.

<details><summary>Corrigé</summary>

def protocole(url):
    res = ''
    i = 0
    while url[i] != ':':
        res = res + url[i]
        i = i + 1
    return res

</details>

### Exercice 2 — Paramètres GET

Lors de l'envoi d'un formulaire en méthode GET, les paramètres sont placés dans l'URL :

```python
def requete_get(page, params):
    """params est un dictionnaire {nom: valeur}"""
    morceaux = []
    for nom in params:
        ...
    return page + '?' + '&'.join(morceaux)
```

**Q2** (1 pt, web_http) Recopier et compléter la fonction requete_get pour que requete_get('recherche.php', {'q': 'nsi', 'p': '2'}) renvoie 'recherche.php?q=nsi&p=2'.

<details><summary>Corrigé</summary>

def requete_get(page, params):
    morceaux = []
    for nom in params:
        morceaux.append(nom + '=' + params[nom])
    return page + '?' + '&'.join(morceaux)

</details>

### Exercice 3 — Codes de réponse HTTP

Un serveur web a renvoyé les codes de réponse suivants : codes = [200, 404, 200, 301, 500, 200]. On exécute :

```python
ok = [c for c in codes if c == 200]
erreurs = [c for c in codes if c >= 400]
```

**Q3** (1 pt, web_http) Donner les valeurs de len(ok) et de erreurs.

<details><summary>Corrigé</summary>

len(ok) = 3 ; erreurs = [404, 500]

</details>

### Exercice 4 — Clé de session HTTPS

Lors de l'établissement d'une connexion HTTPS, le client chiffre une clé K avec la clé publique du serveur et la lui envoie ; le serveur la déchiffre avec sa clé privée. À partir de ce moment-là, le client et le serveur sont en possession de la clé K.

**Q4** (1 pt, web_http) Expliquer le rôle de la clé K dans la suite des échanges et justifier pourquoi on n'utilise pas uniquement le chiffrement asymétrique.

<details><summary>Corrigé</summary>

K est une clé de chiffrement symétrique qui chiffre et déchiffre toutes les données échangées ; le chiffrement symétrique est bien plus rapide, l'asymétrique ne sert qu'à échanger K de façon sûre.

</details>

## S01
### Exercice 1 — Une station météo autonome

Une association installe des stations météo autonomes en montagne. Chaque station est construite autour d'un système sur puce (SoC) qui regroupe sur un même circuit un processeur multicœur, de la mémoire vive, un contrôleur Wi-Fi, un contrôleur USB et un processeur graphique (GPU). Un système d'exploitation de type UNIX y exécute plusieurs programmes : acquisition des capteurs, compression des relevés et envoi vers un serveur.

**Q1** (1.0 pt, soc_architecture) On donne le schéma simplifié de l'architecture de Von Neumann du processeur de la station :

```
+-------------------------+        +-------------+
|  (1)                    |<======>|    (3)      |
|  +-------+  +--------+  |  bus   +-------------+
|  |  (2)  |  | Unité  |  |
|  |       |  | de     |  |<======> (4) Entrées/Sorties
|  +-------+  |contrôle|  |
|             +--------+  |
+-------------------------+
```

Sur la copie, associer à chaque numéro (1), (2), (3) et (4) un des termes suivants : « Mémoire RAM », « Processeur », « Unité arithmétique et logique », « Périphériques ».

<details><summary>Corrigé</summary>

(1) Processeur ; (2) Unité arithmétique et logique ; (3) Mémoire RAM ; (4) Périphériques.

</details>

**Q2** (0.5 pt, soc_architecture) Expliquer pourquoi l'utilisation d'un système sur puce plutôt que de composants séparés sur une carte permet de réduire la consommation électrique de la station.

<details><summary>Corrigé</summary>

Les composants étant rapprochés sur une même puce, les connexions sont très courtes : moins d'énergie est dissipée pour transporter les signaux, et les composants sont gravés plus finement et peuvent être mis en veille individuellement. Cela réduit la consommation (et augmente la vitesse des échanges).

</details>

**Q3** (0.5 pt, processus) Le système d'exploitation de la station gère les processus prêts selon la règle « premier arrivé, premier servi ». Parmi les propositions suivantes, donner la structure de données la plus adaptée pour stocker ces processus en attente, en justifiant :
- Proposition 1 : Pile
- Proposition 2 : File
- Proposition 3 : Dictionnaire

<details><summary>Corrigé</summary>

Proposition 2 : la file, car elle suit le principe FIFO (premier entré, premier sorti) : le processus arrivé en premier est le premier retiré.

</details>

**Q4** (0.5 pt, soc_architecture) Le capteur de température transmet ses mesures codées sur 8 bits en complément à deux. Donner la valeur décimale de la mesure reçue 11111010.

<details><summary>Corrigé</summary>

Le bit de poids fort vaut 1 : nombre négatif. On inverse les bits (00000101) et on ajoute 1 : 00000110 = 6. La mesure vaut -6.

</details>

**Q5** (0.5 pt, processus) On considère trois processus soumis à l'instant 0 dans l'ordre A, C, E :

| Processus | Rôle | Durée (unités de temps) |
|---|---|---|
| A | acquisition | 2 |
| C | compression | 4 |
| E | envoi | 1 |

L'ordonnanceur utilise l'algorithme « premier arrivé, premier servi » (sans interruption). Donner l'instant de fin d'exécution de chaque processus.

<details><summary>Corrigé</summary>

A se termine à l'instant 2, C à l'instant 6, E à l'instant 7.

</details>

**Q6** (0.5 pt, processus) Avec les mêmes processus, l'ordonnanceur utilise désormais l'algorithme du tourniquet (Round Robin) avec un quantum de 1 unité de temps, la file initiale étant A, C, E. Donner la suite des processus élus à chaque unité de temps, puis l'instant de fin de C.

<details><summary>Corrigé</summary>

A, C, E, A, C, C, C. C se termine à l'instant 7 (A à 4, E à 3).

</details>

**Q7** (0.5 pt, processus) Le processus C attend la libération de la carte mémoire, détenue par le processus E, tandis que E attend le module Wi-Fi, détenu par C. Nommer cette situation et expliquer pourquoi aucun des deux processus ne peut repasser à l'état élu.

<details><summary>Corrigé</summary>

C'est un interblocage : chaque processus est bloqué en attente d'une ressource que l'autre ne libérera qu'après avoir obtenu la sienne ; ils restent donc indéfiniment à l'état bloqué.

</details>

**Q8** (0.5 pt, soc_architecture) Pour choisir le composant du SoC à solliciter, on dispose du dictionnaire suivant et de la fonction incomplète ci-dessous, qui renvoie le nom du composant le plus économe parmi ceux capables de réaliser la tâche :

```python
1 conso = {'CPU': 2.0, 'GPU': 3.5, 'DSP': 0.8}  # en watts
2 def plus_econome(composants):
3     meilleur = composants[0]
4     for c in composants:
5         if ..........:
6             meilleur = c
7     return meilleur
```

Recopier et compléter la ligne 5.

<details><summary>Corrigé</summary>

5         if conso[c] < conso[meilleur]:

</details>

**Q9** (0.5 pt, soc_architecture) Le processeur du SoC fonctionne à une fréquence de 1,5 GHz et exécute en moyenne une instruction par cycle. Calculer la durée, en millisecondes, nécessaire pour exécuter un programme de compression de 3 × 10^9 instructions sur un seul cœur.

<details><summary>Corrigé</summary>

Durée = 3 × 10^9 / 1,5 × 10^9 = 2 s, soit 2000 ms.

</details>

**Q10** (0.5 pt, soc_architecture) On souhaite écrire une fonction qui renvoie la liste des composants dont la consommation (dictionnaire conso de la question 8) est inférieure ou égale à un seuil donné.

```python
1 def sous_seuil(conso, seuil):
2     resultat = ..........
3     for nom in conso:
4         if ..........:
5             resultat.append(nom)
6     return resultat
```

Recopier et compléter les lignes 2 et 4.

<details><summary>Corrigé</summary>

2     resultat = []
4         if conso[nom] <= seuil:

</details>

**Q11** (0.5 pt, processus) La commande ps -ef exécutée sur la station affiche notamment :

| UID | PID | PPID | CMD |
|---|---|---|---|
| meteo | 412 | 1 | python3 acquisition.py |
| meteo | 518 | 412 | python3 compresse.py |
| meteo | 530 | 412 | python3 envoi.py |

Expliquer quel processus a lancé compresse.py et envoi.py, et indiquer lequel des deux a été créé en premier.

<details><summary>Corrigé</summary>

Leur PPID vaut 412 : ils ont été lancés par le processus acquisition.py. compresse.py (PID 518) a été créé avant envoi.py (PID 530), les PID étant attribués de façon croissante.

</details>

### Exercice 2 — La médiathèque de quartier

Une médiathèque gère ses prêts de jeux de société avec une base de données relationnelle et quelques scripts Python. La base contient les relations suivantes (clés primaires soulignées par #, clés étrangères précédées de *) :

- Jeu(#id_jeu, titre, editeur, age_min)
- Adherent(#id_adh, nom, prenom, ville)
- Pret(#id_pret, *id_jeu, *id_adh, date_sortie, date_retour)

Extrait de la table Jeu :

| id_jeu | titre | editeur | age_min |
|---|---|---|---|
| 1 | Kaskade | Ludiks | 8 |
| 2 | Polaris | Ludiks | 12 |
| 3 | Tamtam | Orbe | 6 |
| 4 | Basalte | Orbe | 10 |

**Q1** (0.5 pt, mise_au_point) Un script Python représente un jeu par un dictionnaire :

```python
jeu = {'titre': 'Kaskade', 'editeur': 'Ludiks', 'age_min': 8}
```

Donner l'expression qui s'évalue à True parmi les propositions suivantes :
- Proposition A : jeu[0] == 'Kaskade'
- Proposition B : jeu['age_min'] > 10
- Proposition C : 'editeur' in jeu
- Proposition D : jeu.titre == 'Kaskade'

<details><summary>Corrigé</summary>

Proposition C ('editeur' est une clé du dictionnaire). A provoque une KeyError, D une AttributeError, B vaut False.

</details>

**Q2** (0.5 pt, mise_au_point) On donne la liste suivante :

```python
stock = [['Kaskade', 3], ['Polaris', 1], ['Tamtam', 5]]
```

Donner les valeurs de stock[1] et de stock[2][1].

<details><summary>Corrigé</summary>

stock[1] vaut ['Polaris', 1] et stock[2][1] vaut 5.

</details>

**Q3** (0.5 pt, modele_relationnel) Donner le domaine (type) des attributs id_jeu et titre de la relation Jeu.

<details><summary>Corrigé</summary>

id_jeu : entier (INT) ; titre : chaîne de caractères (TEXT ou VARCHAR).

</details>

**Q4** (1.5 pt, modele_relationnel) a. Expliquer pourquoi l'attribut editeur ne peut pas être choisi comme clé primaire de la relation Jeu.
b. Expliquer le rôle de l'attribut id_jeu dans la relation Pret.
c. Expliquer pourquoi la requête suivante est refusée par le SGBD si aucun jeu n'a pour identifiant 9 :

```sql
INSERT INTO Pret VALUES (40, 9, 2, '2026-03-02', NULL);
```

<details><summary>Corrigé</summary>

a. Plusieurs jeux ont le même éditeur (Ludiks pour 1 et 2) : editeur ne permet pas d'identifier un unique enregistrement.
b. id_jeu est une clé étrangère de Pret qui fait référence à la clé primaire de Jeu : elle indique quel jeu est prêté.
c. La contrainte de référence (intégrité référentielle) impose que la valeur d'une clé étrangère existe dans la table référencée ; le jeu 9 n'existant pas, l'insertion est refusée.

</details>

**Q5** (1.0 pt, modele_relationnel) a. Écrire ce que renvoie la requête ci-dessous sur l'extrait de la table Jeu :

```sql
SELECT titre FROM Jeu WHERE editeur = 'Orbe' AND age_min >= 8;
```

b. Écrire une requête SQL permettant d'obtenir les titres des jeux accessibles dès 10 ans ou moins, classés par ordre alphabétique.

<details><summary>Corrigé</summary>

a. Basalte.
b. SELECT titre FROM Jeu WHERE age_min <= 10 ORDER BY titre;

</details>

**Q6** (1.0 pt, modele_relationnel) a. Le jeu Polaris a été rendu le 14 mars 2026 dans le cadre du prêt d'identifiant 37. Écrire une requête SQL permettant d'enregistrer ce retour.
b. Écrire une requête SQL permettant d'obtenir les noms et prénoms des adhérents ayant emprunté le jeu intitulé 'Tamtam'.

<details><summary>Corrigé</summary>

a. UPDATE Pret SET date_retour = '2026-03-14' WHERE id_pret = 37;
b. SELECT Adherent.nom, Adherent.prenom FROM Adherent JOIN Pret ON Adherent.id_adh = Pret.id_adh JOIN Jeu ON Pret.id_jeu = Jeu.id_jeu WHERE Jeu.titre = 'Tamtam';

</details>

**Q7** (1.0 pt, mise_au_point) La fonction suivante doit renvoyer la durée moyenne (en jours) d'une liste de durées de prêt :

```python
1 def duree_moyenne(durees):
2     total = 0
3     for d in durees:
4         total = total + d
5     return total / len(durees)
```

L'appel duree_moyenne([]) provoque une erreur.
a. Parmi les propositions suivantes, indiquer le type d'erreur affiché : ZeroDivisionError, ValueError, TypeError, IndexError.
b. Modifier la fonction pour qu'elle renvoie 0 lorsque la liste est vide.

<details><summary>Corrigé</summary>

a. ZeroDivisionError (len([]) vaut 0).
b.
```python
def duree_moyenne(durees):
    if len(durees) == 0:
        return 0
    total = 0
    for d in durees:
        total = total + d
    return total / len(durees)
```

</details>

### Exercice 3 — Le classement d'une course d'orientation

Lors d'une course d'orientation, les temps des équipes (en minutes) sont rangés dans un arbre binaire de recherche (ABR) : pour chaque nœud, les temps du sous-arbre gauche sont strictement inférieurs et ceux du sous-arbre droit supérieurs ou égaux. On utilise la classe Noeud suivante, un arbre vide étant représenté par None :

```python
1 class Noeud:
2     def __init__(self, temps, equipe):
3         self.temps = temps
4         self.equipe = equipe
5         self.gauche = None
6         self.droit = None
```

Par convention, la hauteur d'un arbre réduit à un nœud vaut 1 et celle de l'arbre vide vaut 0.

**Q1** (1.5 pt, poo) Recopier et compléter la méthode inserer de la classe Noeud, qui insère un nouveau nœud dans l'ABR dont self est la racine.

```python
1 def inserer(self, temps, equipe):
2     if temps < self.temps:
3         if self.gauche is None:
4             self.gauche = ..........
5         else:
6             ..........
7     else:
8         if self.droit is None:
9             self.droit = Noeud(temps, equipe)
10        else:
11            ..........
```

<details><summary>Corrigé</summary>

```python
def inserer(self, temps, equipe):
    if temps < self.temps:
        if self.gauche is None:
            self.gauche = Noeud(temps, equipe)
        else:
            self.gauche.inserer(temps, equipe)
    else:
        if self.droit is None:
            self.droit = Noeud(temps, equipe)
        else:
            self.droit.inserer(temps, equipe)
```

</details>

**Q2** (1.0 pt, arbre_binaire) On exécute les instructions suivantes, en utilisant la méthode de la question précédente :

```python
abr = Noeud(52, 'Lynx')
abr.inserer(47, 'Hiboux')
abr.inserer(61, 'Cerfs')
abr.inserer(39, 'Loutres')
abr.inserer(50, 'Chamois')
abr.inserer(70, 'Aigles')
abr.inserer(58, 'Renards')
```

Dessiner l'arbre obtenu en indiquant uniquement les temps.

<details><summary>Corrigé</summary>

Racine 52 ; fils gauche 47 (fils gauche 39, fils droit 50) ; fils droit 61 (fils gauche 58, fils droit 70).

</details>

**Q3** (0.5 pt, arbre_binaire) Donner la taille et la hauteur de l'arbre abr obtenu à la question 2.

<details><summary>Corrigé</summary>

Taille 7, hauteur 3.

</details>

**Q4** (0.5 pt, poo) Recopier et compléter la méthode taille de la classe Noeud, qui renvoie le nombre de nœuds de l'arbre de racine self.

```python
1 def taille(self):
2     t = 1
3     if self.gauche is not None:
4         t = t + ..........
5     if self.droit is not None:
6         t = t + ..........
7     return t
```

<details><summary>Corrigé</summary>

4         t = t + self.gauche.taille()
6         t = t + self.droit.taille()

</details>

**Q5** (0.5 pt, arbre_binaire) Indiquer quel parcours de l'ABR permet d'obtenir les équipes classées de la plus rapide à la plus lente, et expliquer pourquoi.

<details><summary>Corrigé</summary>

Le parcours infixe (gauche, racine, droite) : dans un ABR il visite les clés dans l'ordre croissant, donc des temps les plus courts aux plus longs.

</details>

**Q6** (0.5 pt, arbre_binaire) Donner la liste des temps dans l'ordre du parcours préfixe de l'arbre abr de la question 2.

<details><summary>Corrigé</summary>

52, 47, 39, 50, 61, 58, 70.

</details>

**Q7** (1.0 pt, arbre_binaire) On considère un arbre binaire R de hauteur 5 dont le sous-arbre gauche G est de hauteur 3. Déterminer la hauteur du sous-arbre droit D de R, puis le nombre maximal de nœuds que peut contenir R dans ces conditions.

<details><summary>Corrigé</summary>

h(R) = 1 + max(h(G), h(D)) = 5, et h(G) = 3, donc h(D) = 4. Nombre maximal : 1 + (2^3 - 1) + (2^4 - 1) = 1 + 7 + 15 = 23 nœuds.

</details>

**Q8** (0.5 pt, arbre_binaire) Donner la taille maximale d'un arbre binaire de hauteur h.

<details><summary>Corrigé</summary>

2^h - 1 nœuds.

</details>

**Q9** (0.5 pt, arbre_binaire) Donner la définition d'un arbre binaire de recherche, puis indiquer, en justifiant, si l'arbre de racine 52, de fils gauche 47 et de fils droit 45 est un ABR.

<details><summary>Corrigé</summary>

Un ABR est un arbre binaire où, pour chaque nœud, les clés du sous-arbre gauche sont inférieures à celle du nœud et celles du sous-arbre droit supérieures. Ici 45 < 52 est dans le sous-arbre droit : ce n'est pas un ABR.

</details>

**Q10** (0.5 pt, arbre_binaire) Déterminer, dans un ABR non vide, où se trouve le nœud contenant le meilleur temps, et donner le nombre de nœuds visités pour l'atteindre dans l'arbre abr de la question 2.

<details><summary>Corrigé</summary>

C'est le nœud le plus à gauche : on descend toujours vers le fils gauche depuis la racine. Dans abr : 52, 47, 39, soit 3 nœuds visités.

</details>

**Q11** (1.0 pt, poo) En s'appuyant sur la question précédente, écrire une méthode vainqueur de la classe Noeud qui renvoie le nom de l'équipe ayant réalisé le meilleur temps dans l'ABR de racine self. Donner ensuite l'instruction permettant d'afficher le vainqueur de abr.

<details><summary>Corrigé</summary>

```python
def vainqueur(self):
    noeud = self
    while noeud.gauche is not None:
        noeud = noeud.gauche
    return noeud.equipe
```
print(abr.vainqueur())  # affiche Loutres

</details>

## S02
### Exercice 1 — Réseau d'une station de recherche polaire

Une station de recherche polaire relie ses bâtiments par six routeurs R1 à R6. Le réseau du laboratoire, 192.168.10.0/24, est raccordé à R1 ; le réseau des capteurs météo, 172.16.0.0/16, est raccordé à R6.

Les liaisons et leur débit sont les suivants :

| Liaison | Débit |
|---|---|
| R1 - R2 | 100 Mbit/s |
| R1 - R3 | 1 Gbit/s |
| R2 - R4 | 1 Gbit/s |
| R3 - R4 | 10 Mbit/s |
| R3 - R5 | 1 Gbit/s |
| R5 - R6 | 1 Gbit/s |
| R4 - R6 | 1 Gbit/s |

Le réseau est modélisé en Python par un graphe donné sous forme de dictionnaire d'adjacence :

```python
reseau = {"R1": ["R2", "R3"], "R2": ["R1", "R4"],
          "R3": ["R1", "R4", "R5"], "R4": ["R2", "R3", "R6"],
          "R5": ["R3", "R6"], "R6": ["R4", "R5"]}
```

Une adresse IPv4 ou un masque est représenté par un tuple de quatre entiers, par exemple (192, 168, 10, 37).

**Q1** (0.5 pt, parcours_graphe) Écrire, dans l'ordre, les routeurs visités lors d'un parcours en largeur du graphe reseau depuis R1, les voisins étant explorés dans l'ordre des listes du dictionnaire.

<details><summary>Corrigé</summary>

R1, R2, R3, R4, R5, R6

</details>

**Q2** (0.5 pt, reseau_ip) Écrire une fonction adresse_reseau(ip, masque) qui prend en paramètres deux tuples de quatre entiers, une adresse IP et un masque, et qui renvoie le tuple représentant l'adresse du réseau (ET logique bit à bit, opérateur & en Python).

<details><summary>Corrigé</summary>

def adresse_reseau(ip, masque):
    return tuple(ip[i] & masque[i] for i in range(4))

</details>

**Q3** (0.5 pt, parcours_graphe) Écrire une fonction nb_liaisons(graphe) qui prend en paramètre un graphe non orienté représenté par un dictionnaire d'adjacence et qui renvoie le nombre de liaisons (arêtes) du graphe. Par exemple nb_liaisons(reseau) renvoie 7.

<details><summary>Corrigé</summary>

def nb_liaisons(graphe):
    total = 0
    for s in graphe:
        total = total + len(graphe[s])
    return total // 2

</details>

**Q4** (0.5 pt, reseau_ip) Donner la valeur renvoyée par adresse_reseau((192, 168, 10, 37), (255, 255, 255, 0)).

<details><summary>Corrigé</summary>

(192, 168, 10, 0)

</details>

**Q5** (0.5 pt, routage) Le protocole OSPF est utilisé avec un coût de liaison égal à 10^9 / d, où d est le débit en bit/s. Donner le coût d'une liaison à 1 Gbit/s, à 100 Mbit/s et à 10 Mbit/s.

<details><summary>Corrigé</summary>

1 Gbit/s : coût 1 ; 100 Mbit/s : coût 10 ; 10 Mbit/s : coût 100.

</details>

**Q6** (0.5 pt, routage) En utilisant les coûts de la question précédente, donner le chemin emprunté selon OSPF par un paquet allant du réseau du laboratoire vers le réseau des capteurs, ainsi que son coût total. Compléter la ligne correspondante de la table de routage de R1 (destination, passerelle, coût).

<details><summary>Corrigé</summary>

Chemin R1 - R3 - R5 - R6, coût 1 + 1 + 1 = 3. Ligne de R1 : 172.16.0.0/16 | passerelle R3 | coût 3.

</details>

**Q7** (0.5 pt, reseau_ip) Donner la représentation binaire sur 8 bits du nombre 172.

<details><summary>Corrigé</summary>

10101100

</details>

**Q8** (0.5 pt, reseau_ip) Recopier et compléter les lignes 4 et 5 de la fonction octet_binaire, qui renvoie la chaîne de 8 caractères représentant en binaire un entier n compris entre 0 et 255.

```
1 def octet_binaire(n):
2     resultat = ''
3     for i in range(8):
4         resultat = ...
5         n = ...
6     return resultat
```

<details><summary>Corrigé</summary>

def octet_binaire(n):
    resultat = ''
    for i in range(8):
        resultat = str(n % 2) + resultat
        n = n // 2
    return resultat

</details>

**Q9** (0.5 pt, reseau_ip) Déterminer le nombre maximal de machines pouvant recevoir une adresse dans le réseau 192.168.10.0/24. Justifier.

<details><summary>Corrigé</summary>

8 bits pour la partie machine : 2^8 = 256 adresses, moins l'adresse du réseau (.0) et celle de diffusion (.255), soit 254 machines (routeur R1 compris).

</details>

**Q10** (0.5 pt, routage) Le routeur R5 tombe en panne. Déterminer la nouvelle route OSPF de R1 vers le réseau des capteurs et donner la ligne modifiée de la table de routage de R1.

<details><summary>Corrigé</summary>

Chemins possibles : R1-R2-R4-R6 (10 + 1 + 1 = 12) et R1-R3-R4-R6 (1 + 100 + 1 = 102). Route retenue R1-R2-R4-R6. Ligne : 172.16.0.0/16 | passerelle R2 | coût 12.

</details>

**Q11** (0.5 pt, routage) Tous les routeurs fonctionnent à nouveau, mais on utilise désormais le protocole RIP. Indiquer la route entre R1 et R5 et la distance correspondante.

<details><summary>Corrigé</summary>

RIP minimise le nombre de sauts : R1 - R3 - R5, distance 2.

</details>

**Q12** (0.5 pt, parcours_graphe) Écrire une fonction nb_sauts(graphe, depart, arrivee) qui renvoie le nombre minimal de liaisons à traverser pour aller du routeur depart au routeur arrivee, en utilisant un parcours en largeur. On suppose le graphe connexe. Par exemple nb_sauts(reseau, 'R1', 'R6') renvoie 3.

<details><summary>Corrigé</summary>

def nb_sauts(graphe, depart, arrivee):
    distance = {depart: 0}
    file = [depart]
    while file:
        s = file.pop(0)
        if s == arrivee:
            return distance[s]
        for v in graphe[s]:
            if v not in distance:
                distance[v] = distance[s] + 1
                file.append(v)

</details>

### Exercice 2 — Le sentier des cairns

Un sentier de randonnée comporte n cairns numérotés de 1 à n. Un randonneur part du point 0 et avance à chaque pas d'un ou de deux cairns. On souhaite compter le nombre de façons différentes d'atteindre le cairn n, puis gérer les temps des randonneurs.

```python
def nb_facons(n):
    if n <= 1:
        return 1
    return nb_facons(n - 1) + nb_facons(n - 2)
```

Un module temps.py est également fourni :

```python
def en_secondes(minutes, secondes):
    return 60 * minutes + secondes

def formater(total):
    return str(total // 60) + ' min ' + str(total % 60) + ' s'
```

**Q1** (0.5 pt, recursivite) Rappeler ce qu'est une fonction récursive.

<details><summary>Corrigé</summary>

Une fonction qui s'appelle elle-même dans sa définition, avec un ou plusieurs cas de base qui arrêtent les appels.

</details>

**Q2** (0.5 pt, prog_dynamique) Énumérer les façons d'atteindre le cairn 4 et donner leur nombre.

<details><summary>Corrigé</summary>

1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 : 5 façons.

</details>

**Q3** (0.5 pt, prog_dynamique) On propose une version ascendante utilisant un tableau t où t[i] est le nombre de façons d'atteindre le cairn i. En s'appuyant sur la question précédente, recopier et compléter la ligne 5.

```
1 def nb_facons_dyn(n):
2     t = [1] * (n + 1)
3     for i in range(2, n + 1):
4         # à compléter
5         t[i] = ...
6     return t[n]
```

<details><summary>Corrigé</summary>

def nb_facons_dyn(n):
    t = [1] * (n + 1)
    for i in range(2, n + 1):
        t[i] = t[i - 1] + t[i - 2]
    return t[n]

</details>

**Q4** (0.5 pt, recursivite) La fonction nb_facons est-elle récursive ? Justifier.

<details><summary>Corrigé</summary>

Oui : dans son corps elle s'appelle elle-même (nb_facons(n - 1) et nb_facons(n - 2)).

</details>

**Q5** (0.5 pt, recursivite) Expliquer le rôle du test n <= 1 dans la fonction nb_facons.

<details><summary>Corrigé</summary>

C'est le cas de base : il renvoie directement 1 sans appel récursif, ce qui garantit l'arrêt des appels (terminaison).

</details>

**Q6** (0.5 pt, recursivite) Recopier et compléter les lignes 3 et 4 de la fonction récursive denivele(liste) qui renvoie la somme des éléments d'une liste de dénivelés.

```
1 def denivele(liste):
2     if len(liste) == 0:
3         return ...
4     return ...
```

<details><summary>Corrigé</summary>

def denivele(liste):
    if len(liste) == 0:
        return 0
    return liste[0] + denivele(liste[1:])

</details>

**Q7** (0.5 pt, modularite) Donner la valeur renvoyée par l'appel formater(en_secondes(2, 75)) des fonctions du module temps.

<details><summary>Corrigé</summary>

en_secondes(2, 75) vaut 195, donc '3 min 15 s'.

</details>

**Q8** (0.5 pt, modularite) Dans un autre fichier, on veut utiliser les fonctions du module temps. Recopier et compléter la ligne 1.

```
1 from ... import ...
2 print(formater(en_secondes(5, 30)))
```

<details><summary>Corrigé</summary>

from temps import en_secondes, formater

</details>

**Q9** (0.5 pt, prog_dynamique) Expliquer pourquoi nb_facons_dyn est bien plus rapide que nb_facons pour de grandes valeurs de n.

<details><summary>Corrigé</summary>

nb_facons recalcule de nombreuses fois les mêmes sous-problèmes (nombre d'appels exponentiel) ; nb_facons_dyn calcule chaque t[i] une seule fois et le mémorise : coût linéaire en n.

</details>

**Q10** (0.5 pt, recursivite) On supprime les deux premières lignes du corps de nb_facons. Expliquer ce qui se passe lors de l'appel nb_facons(3).

<details><summary>Corrigé</summary>

Sans cas de base, les appels se poursuivent avec n = 2, 1, 0, -1, ... sans jamais s'arrêter : la pile d'appels déborde et Python lève une RecursionError.

</details>

**Q11** (0.5 pt, modularite) On définit la classe Chrono. Recopier et compléter la ligne 5 pour que l'attribut total contienne la durée en secondes, en utilisant le module temps.

```
1 import temps
2 class Chrono:
3     def __init__(self, nom, minutes, secondes):
4         self.nom = nom
5         self.total = ...
```

<details><summary>Corrigé</summary>

self.total = temps.en_secondes(minutes, secondes)

</details>

**Q12** (0.5 pt, recursivite) En utilisant la classe Chrono de la question précédente, écrire une fonction récursive plus_rapide(chronos) qui prend en paramètre une liste non vide d'objets Chrono et renvoie le plus petit attribut total.

<details><summary>Corrigé</summary>

def plus_rapide(chronos):
    if len(chronos) == 1:
        return chronos[0].total
    m = plus_rapide(chronos[1:])
    if chronos[0].total < m:
        return chronos[0].total
    return m

</details>

### Exercice 3 — Catalogue d'une médiathèque

Une médiathèque range les codes de ses ouvrages dans un arbre binaire de recherche : pour chaque nœud, les codes du sous-arbre gauche sont strictement inférieurs et ceux du sous-arbre droit strictement supérieurs. Un arbre vide est représenté par None.

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
```

On insère successivement les codes 50, 30, 70, 20, 40, 60, 80, 45, ce qui donne l'arbre A :

```
        50
      /    \
    30      70
   /  \    /  \
  20  40  60  80
        \
         45
```

On convient que la hauteur d'un arbre réduit à sa racine vaut 1 et celle de l'arbre vide vaut 0.

**Q1** (1.0 pt, arbre_binaire) Donner la taille et la hauteur de l'arbre A.

<details><summary>Corrigé</summary>

Taille 8, hauteur 4.

</details>

**Q2** (1.0 pt, abr) Recopier et compléter les lignes 4, 6 et 8 de la fonction récursive contient(abr, code) qui renvoie True si code est présent dans l'ABR abr, False sinon.

```
1 def contient(abr, code):
2     if abr is None:
3         return False
4     if ...:
5         return True
6     if code < abr.valeur:
7         return ...
8     return ...
```

<details><summary>Corrigé</summary>

def contient(abr, code):
    if abr is None:
        return False
    if abr.valeur == code:
        return True
    if code < abr.valeur:
        return contient(abr.gauche, code)
    return contient(abr.droit, code)

</details>

**Q3** (2.0 pt, arbre_binaire) Écrire une fonction récursive hauteur(arbre) qui renvoie la hauteur d'un arbre binaire, avec la convention de l'énoncé.

<details><summary>Corrigé</summary>

def hauteur(arbre):
    if arbre is None:
        return 0
    return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))

</details>

**Q4** (1.0 pt, arbre_binaire) On remplace la feuille 45 par 55. Indiquer si l'arbre obtenu est encore un arbre binaire de recherche. Justifier.

<details><summary>Corrigé</summary>

Non : 55 se trouve dans le sous-arbre gauche de la racine 50 alors qu'il est supérieur à 50.

</details>

**Q5** (1.0 pt, parcours_arbre) Indiquer dans quel ordre sont visités les nœuds de l'arbre A lors d'un parcours en profondeur postfixe (suffixe).

<details><summary>Corrigé</summary>

20, 45, 40, 30, 60, 80, 70, 50

</details>

**Q6** (1.0 pt, arbre_binaire) Combien de nœuds sont examinés par la fonction contient lors de la recherche du code 45 dans l'arbre A ? Les citer.

<details><summary>Corrigé</summary>

4 nœuds : 50, 30, 40, 45.

</details>

**Q7** (1.0 pt, parcours_arbre) Donner la liste des codes obtenue par un parcours infixe de l'arbre A, puis la particularité de ce parcours pour un arbre binaire de recherche.

<details><summary>Corrigé</summary>

20, 30, 40, 45, 50, 60, 70, 80 : le parcours infixe d'un ABR donne les valeurs dans l'ordre croissant.

</details>
