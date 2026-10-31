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
