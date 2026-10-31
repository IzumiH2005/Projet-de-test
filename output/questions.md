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
### Exercice 1 — Bibliothèque de prix

Une librairie range les prix (en euros, entiers) de ses livres dans un arbre binaire de recherche (ABR). Un arbre vide est représenté par None. On dispose du code suivant :

```python
1 class Noeud:
2     def __init__(self, g, v, d):
3         self.gauche = g
4         self.valeur = v
5         self.droit = d
6
7 def inserer(arbre, v):
8     if arbre is None:
9         return Noeud(None, v, None)
10    if v < arbre.valeur:
11        arbre.gauche = inserer(arbre.gauche, v)
12    else:
13        arbre.droit = inserer(arbre.droit, v)
14    return arbre
```

**Q1** (1 pt, abr) Écrire une fonction compter_entre qui prend en paramètres un ABR arbre et deux entiers a et b (avec a <= b) et qui renvoie le nombre de clés de arbre comprises entre a et b inclus, en n'explorant un sous-arbre que s'il peut contenir de telles clés.

<details><summary>Corrigé</summary>

```python
def compter_entre(arbre, a, b):
    if arbre is None:
        return 0
    if arbre.valeur < a:
        return compter_entre(arbre.droit, a, b)
    if arbre.valeur > b:
        return compter_entre(arbre.gauche, a, b)
    return 1 + compter_entre(arbre.gauche, a, b) + compter_entre(arbre.droit, a, b)
```
Si la valeur du nœud est < a, seules les clés du sous-arbre droit peuvent convenir ; si elle est > b, seules celles du sous-arbre gauche.

</details>

### Exercice 2 — Insertions successives

On reprend la classe Noeud et la fonction inserer ci-dessous.

```python
1 class Noeud:
2     def __init__(self, g, v, d):
3         self.gauche = g
4         self.valeur = v
5         self.droit = d
6
7 def inserer(arbre, v):
8     if arbre is None:
9         return Noeud(None, v, None)
10    if v < arbre.valeur:
11        arbre.gauche = inserer(arbre.gauche, v)
12    else:
13        arbre.droit = inserer(arbre.droit, v)
14    return arbre
```

On exécute :

```python
abr = None
for v in [15, 8, 22, 4, 11, 19, 30, 9]:
    abr = inserer(abr, v)
```

| Expression | Valeur |
|---|---|
| abr.valeur | 15 |
| abr.gauche.valeur | 8 |
| abr.gauche.droit.gauche.valeur | ? |

**Q2** (1 pt, abr) Quelle est la valeur de abr.gauche.droit.gauche.valeur après l'exécution de ce code ?

<details><summary>Corrigé</summary>

9 : 9 < 15 donc à gauche de 15, 9 > 8 donc à droite de 8 (nœud 11), 9 < 11 donc fils gauche de 11.

</details>

### Exercice 3 — Arbre dégénéré

On considère la fonction hauteur ci-dessous (la hauteur d'un arbre vide vaut 0, celle d'un arbre réduit à sa racine vaut 1), ainsi que la fonction inserer d'un ABR (insertion à gauche si la clé est strictement inférieure, à droite sinon).

```python
def hauteur(arbre):
    if arbre is None:
        return 0
    return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))

abr = None
for k in range(1, 7):
    abr = inserer(abr, k * 10)
h = hauteur(abr)
```

(On rappelle que, pour un ABR équilibré de taille n, la hauteur est de l'ordre de log2(n).)

**Q3** (1 pt, abr) Déterminer la valeur de h à l'issue des instructions ci-dessus, puis expliquer ce que ce résultat implique pour le coût d'une recherche dans cet arbre.

<details><summary>Corrigé</summary>

Les clés 10, 20, 30, 40, 50, 60 sont insérées dans l'ordre croissant : chacune devient le fils droit de la précédente, l'arbre est un « peigne ». h = 6. La recherche d'une clé absente plus grande que 60 parcourt les 6 nœuds : le coût est linéaire en la taille (n étapes) au lieu d'être de l'ordre de log2(n) pour un ABR équilibré.

</details>

### Exercice 4 — Vérification par le parcours infixe

On considère l'arbre binaire suivant, décrit nœud par nœud :

- racine : 9, de fils gauche 5 et de fils droit 12 ;
- 5 a pour fils gauche 3 et pour fils droit 7 ;
- 7 a pour fils droit 10 ;
- 12 n'a pas de fils.

On rappelle qu'un arbre binaire est un ABR si et seulement si son parcours infixe donne une suite strictement croissante de clés (clés distinctes).

**Q4** (1 pt, abr) Donner le parcours infixe de cet arbre et indiquer, en tenant compte de ce parcours, si cet arbre est un arbre binaire de recherche.

<details><summary>Corrigé</summary>

Parcours infixe : 3, 5, 7, 10, 9, 12. La suite n'est pas croissante (10 précède 9) : ce n'est pas un ABR (10 est dans le sous-arbre gauche de 9 alors que 10 > 9).

</details>

## I-algo_simples
### Exercice 1 — Température maximale

Une station météo relève des températures (en °C) qui peuvent être négatives. On donne la fonction suivante :

```python
1 def maximum(t):
2     maxi = t[0]
3     for i in range(1, len(t)):
4         if t[i] > maxi:
5             maxi = t[i]
6     return maxi
```

**Q1** (1 pt, algo_simples) Expliquer le rôle de la ligne 2 de la fonction maximum et justifier pourquoi la remplacer par maxi = 0 rendrait la fonction incorrecte.

<details><summary>Corrigé</summary>

La ligne 2 initialise le maximum provisoire avec le premier élément du tableau (supposé non vide), qui est une valeur effectivement présente. Avec maxi = 0, si toutes les températures sont négatives (ex. [-3, -7, -1]), aucune n'est > 0 et la fonction renverrait 0 au lieu de -1.

</details>

### Exercice 2 — Relevés de capteurs

Un capteur stocke ses mesures dans un objet de la classe Releve :

```python
1 class Releve:
2     def __init__(self, lieu):
3         self.lieu = lieu
4         self.mesures = []
5
6     def ajouter(self, valeur):
7         self.mesures.append(valeur)
8
9     def moyenne(self):
10        ...
```

Exemple d'utilisation :

| Instruction | Effet |
|---|---|
| r = Releve('Lyon') | r.mesures vaut [] |
| r.ajouter(12) ; r.ajouter(18) | r.mesures vaut [12, 18] |
| r.moyenne() | renvoie 15.0 |

**Q2** (1 pt, algo_simples) Recopier et compléter la méthode moyenne de la classe Releve, qui renvoie la moyenne des mesures, ou None si aucune mesure n'a été enregistrée, sans utiliser la fonction sum.

<details><summary>Corrigé</summary>

```python
    def moyenne(self):
        if len(self.mesures) == 0:
            return None
        total = 0
        for m in self.mesures:
            total = total + m
        return total / len(self.mesures)
```

</details>

### Exercice 3 — Comptage d'occurrences

On souhaite disposer d'une fonction nb_occurrences qui prend en paramètres un tableau tab et une valeur x, et qui renvoie le nombre de fois où x apparaît dans tab. Par exemple nb_occurrences([3, 1, 3, 3, 2], 3) renvoie 3 et nb_occurrences([], 5) renvoie 0.

**Q3** (1 pt, algo_simples) Écrire la fonction nb_occurrences décrite ci-dessus, sans utiliser la méthode count.

<details><summary>Corrigé</summary>

```python
def nb_occurrences(tab, x):
    compteur = 0
    for element in tab:
        if element == x:
            compteur = compteur + 1
    return compteur
```

</details>

### Exercice 4 — Suite de Fibonacci

La suite de Fibonacci est définie ainsi : ses deux premiers termes sont F(0) = 0 et F(1) = 1, puis chaque terme successif est la somme des deux termes précédents. On considère le pseudo-code :

```
a ← 0
b ← 1
répéter n fois :
    a, b ← b, a + b
renvoyer a
```

**Q4** (1 pt, algo_simples) Donner les termes F(0) à F(9) de la suite, puis indiquer la valeur renvoyée par le pseudo-code pour n = 7 en tenant compte de la définition.

<details><summary>Corrigé</summary>

F(0) à F(9) : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. Le pseudo-code renvoie F(n) ; pour n = 7 il renvoie 13.

</details>

## I-arbre_binaire
### Exercice 1 — Arbre généalogique de chats

Un éleveur décrit l'arbre binaire de ses lignées ainsi :

- Tigre est la racine ; ses fils sont Mina (gauche) et Rex (droit) ;
- Mina a pour fils Lou (gauche) et Pixel (droit) ;
- Rex a pour seul fils Nala (droit) ;
- Nala a pour seul fils Zou (gauche) ;
- Lou, Pixel et Zou n'ont pas de fils.

On rappelle que la profondeur de la racine vaut 1.

**Q1** (1 pt, arbre_binaire) Quel est le nœud de plus grande profondeur dans cet arbre, et quelle est cette profondeur ? Justifier.

<details><summary>Corrigé</summary>

Zou, de profondeur 4 : chemin Zou - Nala - Rex - Tigre (4 nœuds). Les autres feuilles Lou et Pixel sont de profondeur 3.

</details>

### Exercice 2 — Arbre sous forme de tuples

On représente un arbre binaire non vide par un tuple (gauche, valeur, droit) (gauche et droit étant eux-mêmes des arbres), et l'arbre vide par None (convention : hauteur de l'arbre vide 0, hauteur d'une feuille 1). On considère :

```python
a = ((None, 'D', None), 'B', ((None, 'F', None), 'E', None)), 'A', (None, 'C', None)
```

(la variable a est donc un tuple de trois éléments).

**Q2** (1 pt, arbre_binaire) Quelle est la hauteur de l'arbre a ?

<details><summary>Corrigé</summary>

4 : le plus long chemin est A - B - E - F (4 nœuds).

</details>

### Exercice 3 — Classe Arbre

On définit un arbre binaire à l'aide de la classe suivante, l'arbre vide étant représenté par None. La taille d'un arbre est son nombre de nœuds.

```python
1 class Arbre:
2     def __init__(self, g, v, d):
3         self.gauche = g
4         self.valeur = v
5         self.droit = d
6
7     def taille(self):
8         t = 1
9         if self.gauche is not None:
10            ...
11        if self.droit is not None:
12            ...
13        return t
```

**Q3** (1 pt, arbre_binaire) Recopier et compléter les lignes 10 et 12 de la méthode taille pour qu'elle renvoie la taille de l'arbre.

<details><summary>Corrigé</summary>

```python
10            t = t + self.gauche.taille()
12            t = t + self.droit.taille()
```

</details>

### Exercice 4 — Taille et hauteur

On considère l'arbre binaire dont la racine R a deux fils S et T ; S a deux fils U et V ; T a un fils droit W ; W a un fils gauche X. On rappelle : la taille d'un arbre est le nombre de nœuds qu'il contient ; sa hauteur est le nombre de nœuds du plus long chemin qui joint le nœud racine à l'une des feuilles.

**Q4** (1 pt, arbre_binaire) Donner la taille et la hauteur de cet arbre.

<details><summary>Corrigé</summary>

Taille : 7 (R, S, T, U, V, W, X). Hauteur : 4 (chemin R - T - W - X).

</details>

## I-calculabilite
### Exercice 1 — Un programme comme donnée

En Python, une fonction est une donnée comme une autre : elle peut être passée en paramètre à une autre fonction. On souhaite une fonction appliquer_n qui prend en paramètres une fonction f, un entier n positif ou nul et une valeur x, et qui renvoie le résultat de n applications successives de f à partir de x. Par exemple, si double est définie par def double(y): return 2 * y, alors appliquer_n(double, 3, 1) renvoie 8.

**Q1** (1 pt, calculabilite) Écrire la fonction appliquer_n qui prend en paramètres f, n et x et qui renvoie f(f(...f(x)...)) avec n applications de f.

<details><summary>Corrigé</summary>

```python
def appliquer_n(f, n, x):
    resultat = x
    for _ in range(n):
        resultat = f(resultat)
    return resultat
```

</details>

### Exercice 2 — Le programme paradoxe

On suppose, par l'absurde, qu'il existe une fonction arret(prog, x) qui renvoie True si l'exécution de prog(x) se termine et False sinon. On construit la fonction paradoxe ci-dessous, de 6 lignes : elle doit boucler indéfiniment (lignes 3 et 4) lorsque arret affirme que prog appliqué à lui-même s'arrête, et renvoyer 1 (ligne 6) sinon.

```python
1 def paradoxe(prog):
2     if ...:
3         while ...:
4             pass
5     else:
6         return 1
```

**Q2** (1 pt, calculabilite) Recopier et compléter les lignes 2 et 3 de la fonction paradoxe.

<details><summary>Corrigé</summary>

```python
2     if arret(prog, prog):
3         while True:
```

</details>

### Exercice 3 — Un problème célèbre

Alan Turing a démontré en 1936 qu'aucun programme ne peut décider, pour tout programme et toute entrée, si l'exécution se termine.

**Q3** (1 pt, calculabilite) Donner le nom de ce problème et le qualificatif qui désigne un problème qu'aucun algorithme ne peut résoudre.

<details><summary>Corrigé</summary>

Le problème de l'arrêt ; il est dit indécidable (la fonction qui le résoudrait n'est pas calculable).

</details>

### Exercice 4 — Raisonnement par l'absurde

On reprend la fonction supposée halt(prog, x) (renvoie True si prog(x) termine, False sinon) et le programme :

```python
def sym(prog):
    if halt(prog, prog):
        while True:
            pass
    else:
        return 1
```

On étudie l'appel sym(sym).

**Q4** (1 pt, calculabilite) Décrire l'exécution de sym(sym) dans le cas où halt(sym, sym) renvoie False, puis expliquer la contradiction obtenue et conclure.

<details><summary>Corrigé</summary>

Si halt(sym, sym) renvoie False, sym(sym) exécute le else : l'exécution se termine correctement et renvoie 1. Donc sym(sym) termine, alors que halt affirmait le contraire : contradiction. (Symétriquement, si halt renvoie True, sym(sym) boucle à l'infini.) Dans les deux cas halt se trompe : une telle fonction halt ne peut pas exister, le problème de l'arrêt est indécidable.

</details>

## I-chaines
### Exercice 1 — Mots palindromes

Un jeu de lettres manipule des mots à l'aide de la classe Mot :

```python
class Mot:
    def __init__(self, texte):
        self.texte = texte
```

On souhaite ajouter une méthode est_palindrome qui renvoie True si l'attribut texte se lit de la même façon de gauche à droite et de droite à gauche, et False sinon. Par exemple Mot('kayak').est_palindrome() renvoie True et Mot('kayaks').est_palindrome() renvoie False.

**Q1** (1 pt, chaines) Écrire le code de la méthode est_palindrome de la classe Mot, sans utiliser de tranche (slicing).

<details><summary>Corrigé</summary>

```python
    def est_palindrome(self):
        n = len(self.texte)
        for i in range(n // 2):
            if self.texte[i] != self.texte[n - 1 - i]:
                return False
        return True
```

</details>

### Exercice 2 — Fonction mystère

On considère la fonction suivante :

```python
1 def mystere(mot):
2     res = ''
3     for c in mot:
4         if c not in 'aeiouy':
5             res = c + res
6     return res
```

**Q2** (1 pt, chaines) Quelle est la valeur renvoyée par l'appel mystere('python') ? Justifier en décrivant le rôle de la ligne 5.

<details><summary>Corrigé</summary>

'nhtp'. Les voyelles (ici 'y' et 'o') sont ignorées ; la ligne 5 ajoute chaque consonne au début de res, ce qui inverse leur ordre : p, t, h, n donnent successivement 'p', 'tp', 'htp', 'nhtp'.

</details>

### Exercice 3 — Manipulations élémentaires

Dans un programme de gestion de classes, on dispose de la variable s = 'Terminale'. On rappelle que les indices d'une chaîne commencent à 0, qu'un indice négatif compte à partir de la fin, et que les chaînes sont comparées dans l'ordre lexicographique.

**Q3** (1 pt, chaines) Donner la valeur de chacune des expressions suivantes : len(s), s[3], s[-1], s[0:4] et s < 'Test'.

<details><summary>Corrigé</summary>

len(s) = 9 ; s[3] = 'm' ; s[-1] = 'e' ; s[0:4] = 'Term' ; s < 'Test' vaut True (les deux premiers caractères 'Te' sont égaux, puis 'r' < 's').

</details>

### Exercice 4 — Préparer une recherche textuelle

Avant d'appliquer un algorithme de recherche textuelle, on veut récupérer tout le texte d'un fichier dans une seule chaîne de caractères. On rappelle qu'avec f = open(nom, 'r', encoding='utf-8'), f.readlines() renvoie la liste des lignes du fichier (chacune se terminant éventuellement par '\n'), et f.close() ferme le fichier.

**Q4** (1 pt, chaines) Écrire une fonction texte_complet qui prend en paramètres une chaîne nom_fichier et une chaîne separateur, et qui renvoie le contenu du fichier en une seule chaîne où chaque fin de ligne '\n' est remplacée par separateur.

<details><summary>Corrigé</summary>

```python
def texte_complet(nom_fichier, separateur):
    f = open(nom_fichier, 'r', encoding='utf-8')
    lignes = f.readlines()
    f.close()
    res = ''
    for ligne in lignes:
        if ligne.endswith('\n'):
            res = res + ligne[:-1] + separateur
        else:
            res = res + ligne
    return res
```

</details>

## I-complexite
### Exercice 1 — Recherche dans un tableau trié

On donne la classe suivante, dont l'attribut valeurs est une liste d'entiers triée dans l'ordre croissant :

```python
1 class TableauTrie:
2     def __init__(self, valeurs):
3         self.valeurs = valeurs
4
5     def contient(self, x):
6         debut = 0
7         fin = len(self.valeurs) - 1
8         while debut <= fin:
9             milieu = (debut + fin) // 2
10            if self.valeurs[milieu] == x:
11                return True
12            elif self.valeurs[milieu] < x:
13                ...
14            else:
15                ...
16        return False
```

**Q1** (1 pt, complexite) Recopier et compléter les lignes 13 et 15 de la méthode contient, puis donner sa complexité dans le pire des cas en fonction de la taille n de la liste.

<details><summary>Corrigé</summary>

```python
13                debut = milieu + 1
15                fin = milieu - 1
```
À chaque tour, l'intervalle de recherche est divisé par 2 : complexité logarithmique, en O(log2 n).

</details>

### Exercice 2 — Mesures expérimentales

Un laboratoire stocke des mesures dans une liste de dictionnaires mesures, à la manière d'une table de base de données mesure(algo, n, comparaisons), par exemple :

```python
mesures = [{'algo': 'insertion', 'n': 100, 'comparaisons': 4950},
           {'algo': 'fusion', 'n': 100, 'comparaisons': 541},
           {'algo': 'insertion', 'n': 200, 'comparaisons': 19900}]
```

Besoin : on veut obtenir, pour un algorithme donné, la liste des couples (n, comparaisons) correspondant à cet algorithme, comme le ferait la requête SELECT n, comparaisons FROM mesure WHERE algo = 'insertion';

**Q2** (1 pt, complexite) Écrire une fonction resultats qui prend en paramètres la liste mesures et une chaîne algo et qui renvoie la liste des tuples (n, comparaisons) des mesures concernant algo, dans l'ordre de la liste.

<details><summary>Corrigé</summary>

```python
def resultats(mesures, algo):
    res = []
    for m in mesures:
        if m['algo'] == algo:
            res.append((m['n'], m['comparaisons']))
    return res
```
resultats(mesures, 'insertion') renvoie [(100, 4950), (200, 19900)] : doubler n multiplie environ par 4 le nombre de comparaisons (coût quadratique).

</details>

### Exercice 3 — Classes de complexité

On considère les classes de complexité suivantes : constante, logarithmique, linéaire, quasi-linéaire, quadratique. On considère aussi les traitements suivants, sur une liste de taille n : l'accès à l'élément t[i], la recherche dichotomique dans une liste triée, la recherche du maximum, le tri fusion, le tri par insertion dans le pire des cas.

**Q3** (1 pt, complexite) Donner le nom de la classe de complexité correspondant à chacun des cinq traitements.

<details><summary>Corrigé</summary>

Accès t[i] : constante (O(1)) ; recherche dichotomique : logarithmique (O(log n)) ; maximum : linéaire (O(n)) ; tri fusion : quasi-linéaire (O(n log n)) ; tri par insertion pire cas : quadratique (O(n²)).

</details>

### Exercice 4 — Ordres de grandeur

On compare trois algorithmes traitant n = 1024 données, de complexités respectives O(n), O(n log2 n) et O(n²). On admet que le nombre d'opérations vaut exactement n, n × log2(n) et n² ; on rappelle que 2^10 = 1024.

**Q4** (1 pt, complexite) Calculer le nombre d'opérations de chaque algorithme pour n = 1024, puis ranger ces trois complexités de la plus efficace à la moins efficace en tenant compte de ces résultats.

<details><summary>Corrigé</summary>

n = 1024 ; n log2 n = 1024 × 10 = 10 240 ; n² = 1 048 576. Classement : linéaire, puis quasi-linéaire (O(n log n), qui se situe entre linéaire et quadratique), puis quadratique.

</details>

## I-dictionnaire
### Exercice 1 — Inventaire d'une ludothèque

Une ludothèque note chaque jour les identifiants (entiers) des jeux empruntés dans une liste Python, par exemple :
```python
emprunts = [12, 7, 12, 3, 7, 12]
```
On souhaite compter le nombre d'emprunts de chaque jeu à l'aide d'un dictionnaire dont les clés sont les identifiants et les valeurs les nombres d'emprunts.
```python
>>> compter_emprunts([12, 7, 12, 3, 7, 12])
{12: 3, 7: 2, 3: 1}
>>> compter_emprunts([])
{}
```

**Q1** (1 pt, dictionnaire) Écrire la fonction `compter_emprunts` qui prend en paramètre une liste d'entiers `emprunts` et renvoie le dictionnaire associant à chaque identifiant présent son nombre d'apparitions dans la liste.

<details><summary>Corrigé</summary>

```python
def compter_emprunts(emprunts):
    d = {}
    for j in emprunts:
        if j in d:
            d[j] = d[j] + 1
        else:
            d[j] = 1
    return d
```

</details>

### Exercice 2 — Un annuaire orienté objet

On donne la classe `Annuaire` ci-dessous, qui stocke des numéros de téléphone dans un dictionnaire dont les clés sont des noms (chaînes) et les valeurs des numéros (chaînes).
```python
1  class Annuaire:
2      def __init__(self):
3          self.contacts = {}
4
5      def ajouter(self, nom, numero):
6          self.contacts[nom] = numero
7
8      def chercher(self, nom):
9          if ...:
10             return ...
11         else:
12             return None
```
| nom | numero |
|---|---|
| 'Lina' | '0601020304' |
| 'Omar' | '0699887766' |

**Q2** (1 pt, dictionnaire) Recopier et compléter les lignes 9 et 10 de la méthode `chercher`, qui renvoie le numéro associé à `nom` s'il est présent dans l'annuaire et `None` sinon.

<details><summary>Corrigé</summary>

```python
    def chercher(self, nom):
        if nom in self.contacts:
            return self.contacts[nom]
        else:
            return None
```

</details>

### Exercice 3 — Des enregistrements comme dictionnaires

Une base de données de bibliothèque contient la relation Livre(isbn, titre, annee), dont la clé primaire est isbn (un identifiant unique de chaque livre). Pour traiter ces données en Python, on transforme chaque ligne en un dictionnaire, puis on range ces dictionnaires dans un dictionnaire `catalogue` indexé par la clé primaire :
```python
catalogue = {
    '978-2-07-036': {'titre': 'Dune', 'annee': 1965},
    '978-2-25-315': {'titre': 'Fondation', 'annee': 1951},
}
```

**Q3** (1 pt, dictionnaire) Quelle est la valeur de l'expression `catalogue['978-2-25-315']['annee']` ? Expliquer pourquoi l'attribut isbn convient comme clé de ce dictionnaire.

<details><summary>Corrigé</summary>

La valeur est `1951`. isbn est la clé primaire de la relation : chaque valeur est unique, donc deux livres ne peuvent pas avoir la même clé ; or les clés d'un dictionnaire doivent être uniques (et immuables, ce qu'est une chaîne).

</details>

### Exercice 4 — Mots de passe et hachage

Un site web conserve, côté serveur, un dictionnaire `comptes` associant à chaque identifiant d'utilisateur l'empreinte (le hash) de son mot de passe, et non le mot de passe lui-même. Lors de la connexion, l'utilisateur saisit son mot de passe dans un formulaire ; celui-ci transite sur le réseau jusqu'au serveur, qui calcule son empreinte et la compare à celle stockée dans `comptes`.

**Q4** (1 pt, dictionnaire) Indiquer quel protocole doit être utilisé pour que le mot de passe ne circule pas en clair sur le réseau, et préciser ce que ce protocole protège, en tenant compte du fait que le dictionnaire `comptes` ne contient que des empreintes.

<details><summary>Corrigé</summary>

Il faut utiliser HTTPS (HTTP sécurisé par TLS) : les échanges sont chiffrés pendant le transit, donc un attaquant qui intercepte les paquets ne lit pas le mot de passe. Le chiffrement ne protège que le transport ; le stockage est protégé séparément par le hachage : même si le dictionnaire `comptes` fuit, on n'y trouve que des empreintes, dont on ne peut pas retrouver facilement le mot de passe.

</details>

## I-diviser_regner
### Exercice 1 — Mesures de performances de tris

Un élève a chronométré deux algorithmes de tri sur des listes de tailles croissantes et a enregistré les résultats dans la table Mesure(id, algo, taille, duree_ms) :

| id | algo | taille | duree_ms |
|---|---|---|---|
| 1 | insertion | 1000 | 40 |
| 2 | fusion | 1000 | 3 |
| 3 | insertion | 10000 | 4100 |
| 4 | fusion | 10000 | 38 |

Il exécute la requête :
```sql
SELECT algo, duree_ms FROM Mesure WHERE taille = 10000 ORDER BY duree_ms;
```

**Q1** (1 pt, diviser pour régner) Quel est l'algorithme qui apparaît sur la première ligne du résultat de cette requête ? Justifier ce résultat à l'aide de la complexité des deux tris.

<details><summary>Corrigé</summary>

La requête renvoie (fusion, 38) puis (insertion, 4100) : la première ligne est le tri fusion. Le tri fusion, de type diviser pour régner, a une complexité en O(n log n), alors que le tri par insertion est en O(n²) dans le pire cas et en moyenne : quand la taille est multipliée par 10, sa durée est multipliée par environ 100, contre environ 13 pour le tri fusion.

</details>

### Exercice 2 — Recherche dichotomique récursive

On considère la fonction suivante, qui renvoie `True` si `x` est présent dans la liste triée `t` entre les indices `g` et `d` inclus, et `False` sinon.
```python
1  def cherche(t, x, g, d):
2      if g > d:
3          return False
4      m = (g + d) // 2
5      if t[m] == x:
6          return True
7      elif t[m] < x:
8          return cherche(t, x, m + 1, d)
9      else:
10         return cherche(t, x, g, m - 1)
```

**Q2** (1 pt, diviser pour régner) Expliquer le rôle des lignes 2 et 3 de la fonction `cherche`, et ce qui se passerait si on les supprimait.

<details><summary>Corrigé</summary>

Les lignes 2 et 3 constituent le cas de base : si g > d, la zone de recherche est vide et x n'est pas dans la liste, on renvoie False. Sans elles, quand x est absent, les appels récursifs continueraient avec une zone vide : on accéderait à des indices invalides (IndexError) ou la récursion ne s'arrêterait pas (RecursionError).

</details>

### Exercice 3 — Maximum d'une liste par diviser pour régner

On veut calculer le maximum d'une liste non vide d'entiers `t` (de type list) en appliquant la méthode diviser pour régner : on coupe la zone étudiée (délimitée par deux indices `g` et `d`, inclus) en deux moitiés, on calcule récursivement le maximum de chaque moitié (sous-problèmes), puis on combine les deux résultats (en gardant le plus grand).

**Q3** (1 pt, diviser pour régner) Écrire une fonction récursive `maximum` qui prend en paramètres une liste `t` et deux entiers `g` et `d` (avec 0 ≤ g ≤ d < len(t)) et qui renvoie le plus grand élément de `t[g..d]`, en suivant cette méthode.

<details><summary>Corrigé</summary>

```python
def maximum(t, g, d):
    if g == d:
        return t[g]
    m = (g + d) // 2
    m1 = maximum(t, g, m)
    m2 = maximum(t, m + 1, d)
    if m1 > m2:
        return m1
    return m2
```
Appel : `maximum(t, 0, len(t) - 1)`.

</details>

### Exercice 4 — Comparer les tris

Une animation compare visuellement, sur une même liste de 1000 entiers mélangés, le tri par sélection et le tri fusion. Chaque élément est représenté par une barre ; à chaque étape, l'animation montre les barres déplacées. Le tri fusion découpe la liste en deux moitiés, les trie récursivement, puis les fusionne.

**Q4** (1 pt, diviser pour régner) Décrire ce que l'on observe dans l'animation pour le tri fusion (ordre dans lequel des zones de la liste deviennent triées), et indiquer lequel des deux tris se termine le premier, en tenant compte de leurs complexités.

<details><summary>Corrigé</summary>

Pour le tri fusion, on voit d'abord apparaître de petits blocs triés (paires, puis groupes de 4, 8…) qui sont fusionnés en blocs de plus en plus grands, jusqu'à une moitié triée puis la liste entière. Le tri fusion se termine le premier : il est en O(n log n), contre O(n²) pour le tri par sélection (environ 10 000 opérations contre environ 500 000 pour n = 1000).

</details>

## I-donnees_tables
### Exercice 1 — Fiches d'élèves

Une table est représentée en Python par une liste de dictionnaires :
```python
eleves = [
    {'nom': 'Ines', 'classe': 'TG2', 'moyenne': 15.5},
    {'nom': 'Hugo', 'classe': 'TG1', 'moyenne': 9.0},
    {'nom': 'Sara', 'classe': 'TG2', 'moyenne': 12.0},
]
```

**Q1** (1 pt, données en tables) Donner la valeur renvoyée par l'instruction suivante : `[e['nom'] for e in eleves if e['classe'] == 'TG2' and e['moyenne'] > 13]`.

<details><summary>Corrigé</summary>

`['Ines']` (Sara est en TG2 mais sa moyenne 12.0 n'est pas strictement supérieure à 13).

</details>

### Exercice 2 — Sélection de lignes

On reprend une table représentée par une liste de dictionnaires (chaque dictionnaire a notamment une clé `'classe'`). La fonction `selection` doit renvoyer la liste des lignes de `table` dont la valeur associée à la clé `cle` vaut `valeur`.
```python
1  def selection(table, cle, valeur):
2      resultat = ...
3      for ligne in table:
4          if ...:
5              resultat.append(...)
6      return resultat
```

**Q2** (1 pt, données en tables) Recopier et compléter les lignes 2, 4 et 5 de la fonction `selection`.

<details><summary>Corrigé</summary>

```python
def selection(table, cle, valeur):
    resultat = []
    for ligne in table:
        if ligne[cle] == valeur:
            resultat.append(ligne)
    return resultat
```

</details>

### Exercice 3 — Moyenne d'une colonne

La fonction `moyenne_colonne` prend en paramètres une table `table` (liste non vide de dictionnaires) et une chaîne `cle` désignant une colonne numérique, et renvoie la moyenne des valeurs de cette colonne. Par exemple, avec la table `eleves` des questions précédentes, `moyenne_colonne(eleves, 'moyenne')` renvoie `12.166666666666666`.

**Q3** (1 pt, données en tables) Écrire la fonction `moyenne_colonne` décrite ci-dessus.

<details><summary>Corrigé</summary>

```python
def moyenne_colonne(table, cle):
    total = 0
    for ligne in table:
        total = total + ligne[cle]
    return total / len(table)
```

</details>

### Exercice 4 — Préparer l'export d'une table

On souhaite exporter une table au format CSV dans un fichier. Dans un terminal Linux, on se trouve dans le répertoire personnel, qui contient déjà un dossier `test2`. On veut d'abord créer dans ce dossier un fichier vide `videexemple.txt`, qui servira de modèle, sans quitter le répertoire courant.

**Q4** (1 pt, données en tables) Donner la commande shell permettant de créer ce fichier vide dans le dossier `test2`, puis la commande permettant de vérifier qu'il apparaît dans le contenu de ce dossier.

<details><summary>Corrigé</summary>

`touch test2/videexemple.txt` crée le fichier vide ; `ls test2` affiche le contenu du dossier (on doit y voir `videexemple.txt`).

</details>

## I-file
### Exercice 1 — File d'attente à la cantine

On modélise une file d'attente par une liste Python : on enfile en fin de liste avec `append` et on défile en tête avec `pop(0)`.
```python
f = []
for i in range(1, 6):
    f.append(i)
    if i % 2 == 0:
        f.pop(0)
```

**Q1** (1 pt, file) Déterminer la valeur de `f` à l'issue des instructions ci-dessus.

<details><summary>Corrigé</summary>

i=1 : [1] ; i=2 : [1, 2] puis défile 1 → [2] ; i=3 : [2, 3] ; i=4 : [2, 3, 4] puis défile 2 → [3, 4] ; i=5 : [3, 4, 5]. Donc `f = [3, 4, 5]`.

</details>

### Exercice 2 — Commandes en attente

Un site de vente enregistre les commandes dans une base de données avec la relation Commande(id_commande, client, date_heure, statut) (statut valant 'attente' ou 'traitee'). Les commandes en attente doivent être traitées dans leur ordre d'arrivée (première arrivée, première servie). Un programme récupère les commandes en attente puis les traite une par une.

**Q2** (1 pt, file) On cherche à traiter les commandes en attente dans la base. Expliquer pourquoi elles doivent être gérées comme une file, et donner la requête SQL qui les renvoie dans l'ordre où elles doivent être traitées.

<details><summary>Corrigé</summary>

Il faut traiter en premier la commande arrivée en premier : c'est le principe FIFO d'une file. Requête :
```sql
SELECT id_commande, client FROM Commande
WHERE statut = 'attente'
ORDER BY date_heure;
```

</details>

### Exercice 3 — Une file avec deux piles

On implémente une classe `File` à l'aide de deux listes Python utilisées comme piles : `self.entree` (où l'on empile les éléments enfilés) et `self.sortie` (d'où l'on dépile les éléments défilés).
```python
class File:
    def __init__(self):
        self.entree = []
        self.sortie = []

    def enfiler(self, x):
        self.entree.append(x)
```
La méthode `defiler` retire et renvoie l'élément le plus ancien de la file (supposée non vide) : si `self.sortie` est vide, on y transfère d'abord tous les éléments de `self.entree` en les dépilant un à un.

**Q3** (1 pt, file) Écrire le code de la méthode `defiler` de la classe `File` décrite ci-dessus.

<details><summary>Corrigé</summary>

```python
    def defiler(self):
        if self.sortie == []:
            while self.entree != []:
                self.sortie.append(self.entree.pop())
        return self.sortie.pop()
```

</details>

### Exercice 4 — Interface d'une file

Un développeur doit fournir une structure de file à ses collègues sans leur imposer l'implémentation (liste, deux piles, liste chaînée…). Il doit donc spécifier une interface.

**Q4** (1 pt, file) Indiquer les opérations que doit proposer a minima l'interface d'une file, en précisant pour chacune son rôle.

<details><summary>Corrigé</summary>

Créer une file vide ; tester si une file est vide (est_vide) ; enfiler (ajouter un élément en queue) ; défiler (retirer et renvoyer l'élément en tête, le plus ancien).

</details>

## I-fonctions
### Exercice 1 — Portée des variables

On considère le programme suivant :
```python
def f(x, y=2):
    z = x * y
    return z + 1

a = f(3)
b = f(3, 5)
```
| variable | valeur |
|---|---|
| a | ? |
| b | ? |

**Q1** (1 pt, fonctions) Quelle est la valeur de `a` et celle de `b` à l'issue de l'exécution ?

<details><summary>Corrigé</summary>

`a = 7` (y prend sa valeur par défaut 2 : 3*2+1) et `b = 16` (3*5+1).

</details>

### Exercice 2 — Recherche dans un arbre

Un arbre binaire est représenté par des objets de la classe `Noeud` ; l'arbre vide est `None`.
```python
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
```
On souhaite une fonction `appartient(arbre, element)` qui renvoie `True` si `element` est dans l'arbre et `False` sinon (l'arbre n'est pas forcément un arbre binaire de recherche).

**Q2** (1 pt, fonctions) Écrire la fonction récursive `appartient`, en tenant compte du cas de l'arbre vide.

<details><summary>Corrigé</summary>

```python
def appartient(arbre, element):
    if arbre is None:
        return False
    if arbre.valeur == element:
        return True
    return appartient(arbre.gauche, element) or appartient(arbre.droit, element)
```

</details>

## I-glouton
### Exercice 1 — Rendu de monnaie

On considère la fonction suivante qui rend la monnaie de manière gloutonne (la liste `pieces` est triée par ordre décroissant).
```python
1  def rendu(somme, pieces):
2      res = []
3      for p in pieces:
4          while somme >= p:
5              res.append(p)
6              somme = somme - p
7      return res
8
9  r = rendu(48, [20, 10, 5, 2, 1])
```

**Q1** (1 pt, algorithmes gloutons) Déterminer la valeur de `r` à l'issue de l'exécution de la ligne 9.

<details><summary>Corrigé</summary>

`[20, 20, 5, 2, 1]` (48 → 28 → 8 → 3 → 1 → 0).

</details>

### Exercice 2 — Remplir un sac

Une classe `Sac` modélise un sac à dos de capacité `capacite` (en kg). On donne :
```python
class Sac:
    def __init__(self, capacite):
        self.capacite = capacite
        self.contenu = []
```
La méthode `remplir` prend en paramètre une liste `objets` de couples (nom, masse) et ajoute au contenu du sac, de manière gloutonne, les objets pris par masse croissante tant que la masse totale ne dépasse pas la capacité ; elle renvoie la liste des noms ajoutés.

**Q2** (1 pt, algorithmes gloutons) Écrire le code de la méthode `remplir` de la classe `Sac` décrite ci-dessus.

<details><summary>Corrigé</summary>

```python
    def remplir(self, objets):
        tries = sorted(objets, key=lambda o: o[1])
        total = 0
        for nom, masse in tries:
            if total + masse <= self.capacite:
                self.contenu.append(nom)
                total = total + masse
        return self.contenu
```

</details>

### Exercice 3 — Choix d'activités

Une salle accueille des activités, chacune représentée par un couple (debut, fin) d'entiers (heures). Deux activités sont compatibles si l'une finit avant (ou au moment où) l'autre commence. La stratégie gloutonne consiste à choisir à chaque étape l'activité compatible qui finit le plus tôt.

**Q3** (1 pt, algorithmes gloutons) Écrire une fonction `planning` qui prend en paramètres une liste `activites` de couples (debut, fin) et un entier `ouverture` (heure d'ouverture de la salle) et qui renvoie la liste des activités choisies par cette stratégie (aucune ne commence avant `ouverture`).

<details><summary>Corrigé</summary>

```python
def planning(activites, ouverture):
    tries = sorted(activites, key=lambda a: a[1])
    choisies = []
    t = ouverture
    for debut, fin in tries:
        if debut >= t:
            choisies.append((debut, fin))
            t = fin
    return choisies
```

</details>

### Exercice 4 — Descente d'une pyramide

Une pyramide de nombres est représentée par une liste de listes : la ligne i contient i+1 entiers.
```python
p = [[3],
     [7, 4],
     [2, 4, 6],
     [8, 5, 9, 3]]
```
On part du sommet et, à chaque ligne, on descend vers l'un des deux nombres situés juste en dessous (indice j ou j+1). On cherche un trajet de somme maximale. La classe `Pyramide` a un attribut `self.lignes` contenant cette liste. La méthode `glouton` doit calculer de manière gloutonne un « meilleur » trajet : à chaque étape on descend vers le plus grand des deux voisins. Elle renvoie la somme obtenue.

**Q4** (1 pt, algorithmes gloutons) Écrire le code de la méthode `glouton` de la classe `Pyramide` décrite ci-dessus, puis donner sa valeur pour la pyramide `p`.

<details><summary>Corrigé</summary>

```python
    def glouton(self):
        j = 0
        somme = self.lignes[0][0]
        for i in range(1, len(self.lignes)):
            if self.lignes[i][j + 1] > self.lignes[i][j]:
                j = j + 1
            somme = somme + self.lignes[i][j]
        return somme
```
Pour p : 3 → 7 → 4 → 9 (4 > 2, puis 9 > 5), somme 23 (ici égale à l'optimum ; en général la méthode gloutonne n'est pas optimale).

</details>

## I-graphe
### Exercice 1 — Réseau de pistes cyclables

Le plan des pistes cyclables d'une commune est un graphe non orienté. Chaque arête est stockée une seule fois dans la table Piste(id_piste, depart, arrivee, longueur_km). Contenu de la table :

| id_piste | depart | arrivee | longueur_km |
|---|---|---|---|
| 1 | Gare | Mairie | 2 |
| 2 | Mairie | Lycee | 3 |
| 3 | Gare | Port | 4 |
| 4 | Port | Lycee | 1 |
| 5 | Lycee | Stade | 5 |

On considère la requête :
```sql
SELECT arrivee FROM Piste WHERE depart = 'Lycee'
UNION
SELECT depart FROM Piste WHERE arrivee = 'Lycee';
```

**Q1** (1 pt, graphe) Donner les valeurs renvoyées par la requête ci-dessus et expliquer en une phrase ce qu'elles représentent dans le graphe.

<details><summary>Corrigé</summary>

Valeurs renvoyées : Stade, Mairie, Port (ordre indifférent). Ce sont les voisins (sommets adjacents) du sommet Lycee ; leur nombre, 3, est le degré de Lycee.

</details>

### Exercice 2 — Degré maximal d'un graphe

Un graphe non orienté est représenté en Python par un dictionnaire de listes d'adjacence, par exemple :
```python
G = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B'], 'D': ['B']}
```
On souhaite connaître le sommet ayant le plus de voisins. La fonction sommet_max prend en paramètre un graphe G non vide sous cette forme et renvoie un sommet de degré maximal.

**Q2** (1 pt, graphe) Écrire la fonction sommet_max qui prend en paramètre un graphe G et renvoie un sommet de degré maximal.

<details><summary>Corrigé</summary>

```python
def sommet_max(G):
    meilleur = None
    for s in G:
        if meilleur is None or len(G[s]) > len(G[meilleur]):
            meilleur = s
    return meilleur
```
Avec l'exemple, sommet_max(G) renvoie 'B' (degré 3).

</details>

### Exercice 3 — Successeurs dans un graphe orienté stocké en base

Une application de covoiturage stocke les trajets proposés dans la table Trajet(id, ville_dep, ville_arr). Ce graphe est orienté : un trajet va de ville_dep à ville_arr. On souhaite obtenir la liste des villes que l'on peut atteindre directement depuis Nantes. Le programme Python suivant récupère les lignes de la table sous la forme d'une liste de tuples (id, ville_dep, ville_arr) puis construit la liste des successeurs d'une ville.
```python
1 REQUETE = "SELECT ... FROM Trajet WHERE ... ;"
2
3 def successeurs(lignes, ville):
4     res = []
5     for (ident, dep, arr) in lignes:
6         if ...:
7             res.append(...)
8     return res
```
La variable REQUETE doit contenir la requête SQL renvoyant les villes d'arrivée des trajets partant de Nantes ; la fonction successeurs, elle, fait le même travail en Python à partir de toutes les lignes de la table.

**Q3** (1 pt, graphe) Recopier et compléter la ligne 1 et la fonction successeurs donnée ci-dessus (lignes 6 et 7).

<details><summary>Corrigé</summary>

Ligne 1 : REQUETE = "SELECT ville_arr FROM Trajet WHERE ville_dep = 'Nantes';"
```python
def successeurs(lignes, ville):
    res = []
    for (ident, dep, arr) in lignes:
        if dep == ville:
            res.append(arr)
    return res
```

</details>

### Exercice 4 — Quand un graphe est un arbre

Un club de randonnée relie ses 5 refuges R1, R2, R3, R4, R5 par des sentiers (graphe non orienté) : R1–R2, R1–R3, R3–R4, R3–R5, R4–R5. On rappelle qu'un arbre, dans le vocabulaire des graphes, est un graphe non orienté, connexe, sans cycle, dans lequel un sommet joue le rôle de racine.

**Q4** (1 pt, graphe) Donner la liste des sentiers à supprimer, en nombre minimal, pour que le graphe devienne un arbre de racine R1 dont R3 a exactement deux fils, puis donner la propriété des arbres qui justifie ce nombre.

<details><summary>Corrigé</summary>

Le seul cycle est R3–R4–R5–R3. Il faut supprimer un seul sentier, et pour que R3 garde deux fils (R4 et R5) on supprime R4–R5. On obtient les 4 arêtes R1–R2, R1–R3, R3–R4, R3–R5 : graphe connexe, sans cycle. Justification : un arbre à n sommets possède exactement n − 1 arêtes, ici 5 − 1 = 4, donc on supprime 5 − 4 = 1 sentier.

</details>

## I-interface_tad
### Exercice 1 — File implémentée par deux piles

On donne la classe File ci-dessous, dont l'interface comporte est_vide, enfiler et defiler. Son implémentation interne utilise deux listes Python employées comme des piles ; l'utilisateur de la classe n'a pas à le savoir.
```python
 1 class File:
 2     def __init__(self):
 3         self.entree = []
 4         self.sortie = []
 5
 6     def est_vide(self):
 7         return self.entree == [] and self.sortie == []
 8
 9     def enfiler(self, x):
10         self.entree.append(x)
11
12     def defiler(self):
13         if self.sortie == []:
14             while ...:
15                 self.sortie.append(...)
16         return ...
```
La méthode defiler suppose la file non vide et renvoie l'élément le plus anciennement enfilé.

**Q1** (1 pt, interface_tad) Recopier et compléter les lignes 14, 15 et 16 de la méthode defiler.

<details><summary>Corrigé</summary>

```python
    def defiler(self):
        if self.sortie == []:
            while self.entree != []:
                self.sortie.append(self.entree.pop())
        return self.sortie.pop()
```

</details>

### Exercice 2 — Utiliser une pile sans connaître son implémentation

Un module fournit le type abstrait Pile par l'interface suivante : creer_pile() renvoie une pile vide ; est_vide(p) renvoie True si p est vide ; empiler(p, x) ajoute x au sommet ; depiler(p) retire et renvoie le sommet. On empile successivement 4, 7 puis 12 et on souhaite écrire, en n'utilisant que ces 4 fonctions, une fonction taille qui renvoie le nombre d'éléments d'une pile sans la modifier (ici 3).
```python
1 def taille(p):
2     q = creer_pile()
3     n = 0
4     while not est_vide(p):
5         empiler(q, ...)
6         n = ...
7     while not est_vide(q):
8         empiler(p, ...)
9     return n
```

**Q2** (1 pt, interface_tad) Recopier et compléter les lignes 5, 6 et 8 de la fonction taille.

<details><summary>Corrigé</summary>

Ligne 5 : empiler(q, depiler(p)) ; ligne 6 : n = n + 1 ; ligne 8 : empiler(p, depiler(q)). La seconde boucle remet les éléments dans p dans leur ordre initial.

</details>

### Exercice 3 — Une file de priorité vue par son interface

Une file de priorité est un type abstrait dont l'interface comporte : creer_fp() qui renvoie une file vide, est_vide_fp(f), inserer(f, element, priorite) et extraire_min(f) qui retire et renvoie l'élément de plus petite priorité (on suppose f non vide). On veut s'en servir pour trier des tâches sans connaître son implémentation.

**Q3** (1 pt, interface_tad) Écrire une fonction ordonner qui prend en paramètres une liste taches de chaînes de caractères et une liste priorites d'entiers de même longueur, et qui renvoie la liste des tâches rangées par priorité croissante en n'utilisant que l'interface de la file de priorité.

<details><summary>Corrigé</summary>

```python
def ordonner(taches, priorites):
    f = creer_fp()
    for i in range(len(taches)):
        inserer(f, taches[i], priorites[i])
    res = []
    while not est_vide_fp(f):
        res.append(extraire_min(f))
    return res
```

</details>

### Exercice 4 — Le SGBD comme interface

Une médiathèque gère la base Mediatheque, qui contient les tables Livre(isbn, titre, annee) et Emprunt(id, isbn, date_retour), isbn étant clé étrangère de Emprunt vers Livre. Les bibliothécaires n'écrivent jamais dans les fichiers de la base : ils envoient des requêtes SQL au SGBD. L'un d'eux exécute :
```sql
DELETE FROM Livre WHERE isbn = '978-2-07-036822-8';
```
alors qu'un emprunt de ce livre est encore enregistré. Le SGBD refuse la requête.

**Q4** (1 pt, interface_tad) On cherche à supprimer ce livre dans la base Mediatheque. Expliquer pourquoi le SGBD refuse la requête et en quoi ce refus illustre son rôle d'interface entre l'utilisateur et les données.

<details><summary>Corrigé</summary>

La ligne d'Emprunt référence ce isbn par une clé étrangère : la supprimer dans Livre violerait la contrainte d'intégrité référentielle, donc le SGBD rejette la requête. L'utilisateur n'accède pas directement aux données stockées : il formule une demande (SQL) et le SGBD, intermédiaire entre l'humain et la base, l'exécute ou la refuse en garantissant la cohérence (il faudrait d'abord supprimer l'emprunt correspondant).

</details>

## I-k_ppv
### Exercice 1 — Classifieur de fruits

Un maraîcher classe ses fruits à partir de deux mesures : masse (g) et diamètre (cm). On dispose de la classe suivante :
```python
class Classifieur:
    def __init__(self, exemples):
        # exemples : liste de tuples (masse, diametre, etiquette)
        self.exemples = exemples

    def distance(self, a, b):
        return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5
```
On souhaite ajouter une méthode k_voisins qui prend en paramètres un point p = (masse, diametre) et un entier k, et qui renvoie la liste des k exemples les plus proches de p, du plus proche au plus éloigné.

**Q1** (1 pt, k_ppv) Écrire le code de la méthode k_voisins de la classe Classifieur qui renvoie la liste des k exemples les plus proches du point p.

<details><summary>Corrigé</summary>

```python
    def k_voisins(self, p, k):
        triee = sorted(self.exemples, key=lambda e: self.distance(e, p))
        return triee[:k]
```
(Une version sans sorted, par tri par sélection ou insertion selon la distance, est acceptée.)

</details>

### Exercice 2 — Vote majoritaire

Après avoir calculé les voisins d'un nouveau fruit, on détermine sa classe par vote majoritaire avec le programme suivant :
```python
 1 voisins = [(150, 7, 'pomme'), (160, 8, 'orange'),
 2            (140, 7, 'pomme'), (170, 8, 'orange'),
 3            (155, 7, 'pomme')]
 4 k = 3
 5 votes = {}
 6 for i in range(k):
 7     etiq = voisins[i][2]
 8     if etiq in votes:
 9         votes[etiq] = votes[etiq] + 1
10     else:
11         votes[etiq] = 1
12 classe = max(votes, key=lambda e: votes[e])
```
La liste voisins est déjà triée par distance croissante.

**Q2** (1 pt, k_ppv) Déterminer la valeur de votes puis celle de classe à l'issue des instructions ci-dessus. Indiquer ce que deviendrait classe avec k = 4 en justifiant la difficulté rencontrée.

<details><summary>Corrigé</summary>

Avec k = 3 : votes = {'pomme': 2, 'orange': 1} et classe = 'pomme'. Avec k = 4 : votes = {'pomme': 2, 'orange': 2} : égalité ; max renvoie la première clé rencontrée de valeur maximale, ici 'pomme', mais le résultat dépend de l'ordre d'insertion et non des données : un k pair peut créer des égalités, d'où le choix d'un k impair pour deux classes.

</details>

### Exercice 3 — Effet du choix de k

Un jeu de données d'entraînement contient 9 points étiquetés : - 4 points « chat » très proches du point inconnu X (distances 1, 1,5, 2 et 2,5) ; - 5 points « chien » plus éloignés (distances 4, 4,5, 5, 5,5 et 6). On applique l'algorithme des k plus proches voisins au point X avec vote majoritaire.

**Q3** (1 pt, k_ppv) Quelle est la classe attribuée à X pour k = 3, puis pour k = 9 ? Justifier, et indiquer quel est l'inconvénient d'un k trop grand.

<details><summary>Corrigé</summary>

k = 3 : les 3 plus proches sont trois « chat » → « chat ». k = 9 : tous les points votent, 5 « chien » contre 4 « chat » → « chien ». Un k trop grand fait intervenir des points éloignés et non représentatifs : la prédiction tend vers la classe majoritaire du jeu entier.

</details>

## I-liste_chainee
### Exercice 1 — Longueur d'une liste chaînée

Une liste chaînée est construite à partir de cellules :
```python
1 class Cellule:
2     def __init__(self, valeur, suivante):
3         self.valeur = valeur
4         self.suivante = suivante
5
6 def longueur(lst):
7     n = ...
8     c = lst
9     while ...:
10        n = n + 1
11        c = ...
12    return n
```
La liste vide est représentée par None. Par exemple, la liste 8 → 3 → 15 est créée par l = Cellule(8, Cellule(3, Cellule(15, None))) et longueur(l) doit renvoyer 3.

**Q1** (1 pt, liste_chainee) Recopier et compléter les lignes 7, 9 et 11 de la fonction longueur.

<details><summary>Corrigé</summary>

Ligne 7 : n = 0 ; ligne 9 : while c is not None: ; ligne 11 : c = c.suivante.

</details>

### Exercice 2 — Suivre les maillons

Un lecteur audio enregistre sa file de lecture sous forme de liste chaînée, en utilisant la classe Cellule (attributs valeur et suivante, None marquant la fin). On exécute, dans l'ordre, les instructions suivantes, où chaque valeur est un numéro de morceau : l = Cellule(42, None), puis l = Cellule(17, l), puis l = Cellule(5, l), puis l.suivante.suivante = Cellule(99, l.suivante.suivante).

**Q2** (1 pt, liste_chainee) Donner la séquence des valeurs de la liste l, de la tête à la fin, à l'issue de ces instructions, puis la valeur de l.suivante.suivante.valeur.

<details><summary>Corrigé</summary>

Après les trois premières instructions : 5 → 17 → 42. La quatrième insère 99 après 17 : 5 → 17 → 99 → 42. l.suivante.suivante.valeur vaut 99.

</details>

### Exercice 3 — Insertion en fin de liste

On reprend la classe Cellule (attributs valeur et suivante). La fonction ci-dessous ajoute une valeur v à la fin d'une liste chaînée non vide lst.
```python
1 def ajouter_fin(lst, v):
2     c = lst
3     while c.suivante is not None:
4         c = c.suivante
5     c.suivante = Cellule(v, None)
```

**Q3** (1 pt, liste_chainee) Expliquer le rôle de la ligne 3 de la fonction ajouter_fin, et indiquer pourquoi la fonction échoue si lst vaut None.

<details><summary>Corrigé</summary>

La ligne 3 fait avancer c tant que la cellule courante a une suivante : la boucle s'arrête sur la dernière cellule, à laquelle on accroche la nouvelle cellule en ligne 5. Si lst vaut None, l'accès c.suivante provoque une erreur (AttributeError) car None n'a pas d'attribut suivante : la liste vide doit être traitée à part.

</details>

### Exercice 4 — Chaîne de cellules

Une liste chaînée est une chaîne de cellules : chaque cellule contient une valeur et l'adresse (la référence) de la cellule suivante ; la dernière référence vaut None. On considère la liste créée par l = Cellule('a', Cellule('b', Cellule('c', None))).

**Q4** (1 pt, liste_chainee) Dessiner la chaîne de cellules représentant l en tenant compte de la référence de fin, puis indiquer le nombre de cellules à parcourir pour accéder à la valeur 'c' depuis l.

<details><summary>Corrigé</summary>

Schéma : l → [ 'a' | • ] → [ 'b' | • ] → [ 'c' | None ]. Pour atteindre 'c', on part de la première cellule et on suit deux références (l.suivante.suivante) : on parcourt donc les 3 cellules ; l'accès au k-ième élément nécessite de suivre k − 1 liens, contrairement à un tableau (accès direct).

</details>

## I-matrice
### Exercice 1 — Classe Matrice

On donne la classe Matrice ci-dessous, qui représente une matrice d'entiers par une liste de listes (une liste par ligne).
```python
 1 class Matrice:
 2     def __init__(self, lignes):
 3         self.lignes = lignes
 4         self.n = len(lignes)
 5         self.p = len(lignes[0])
 6
 7     def transposee(self):
 8         res = []
 9         for j in range(...):
10             ligne = []
11             for i in range(...):
12                 ligne.append(...)
13             res.append(ligne)
14         return Matrice(res)
```
Par exemple Matrice([[1, 2, 3], [4, 5, 6]]).transposee().lignes vaut [[1, 4], [2, 5], [3, 6]].

**Q1** (1 pt, matrice) Recopier et compléter les lignes 9, 11 et 12 de la méthode transposee.

<details><summary>Corrigé</summary>

Ligne 9 : for j in range(self.p): ; ligne 11 : for i in range(self.n): ; ligne 12 : ligne.append(self.lignes[i][j]).

</details>

### Exercice 2 — Stocker une matrice dans une base

Un service météo stocke des relevés de température dans une matrice : ligne = station, colonne = jour. Pour l'enregistrer dans la base Meteo, on utilise la table Releve(station, jour, temperature), une ligne par case de la matrice :
```python
T = [[12, 14, 13],
     [9, 10, 11]]
```
| station | jour | temperature |
|---|---|---|
| 0 | 0 | 12 |
| 0 | 1 | 14 |
| 0 | 2 | 13 |
| 1 | 0 | 9 |
| 1 | 1 | 10 |
| 1 | 2 | 11 |

Un technicien propose station comme clé primaire de Releve.

**Q2** (1 pt, matrice) On cherche à enregistrer la matrice T dans la base Meteo. Expliquer pourquoi station ne peut pas être la clé primaire et proposer une clé primaire correcte.

<details><summary>Corrigé</summary>

station prend plusieurs fois la même valeur (0 apparaît 3 fois) : une clé primaire doit être unique pour chaque ligne, l'insertion échouerait. Une case de la matrice est identifiée par son couple (ligne, colonne) : la clé primaire est le couple (station, jour).

</details>

### Exercice 3 — Somme des colonnes

La fonction suivante prend une matrice M non vide (liste de listes de même longueur) et renvoie la liste des sommes de chaque colonne.
```python
1 def sommes_colonnes(M):
2     s = [0] * len(M[0])
3     for i in range(len(M)):
4         for j in range(len(M[0])):
5             s[j] = s[j] + M[i][j]
6     return s
```
Par exemple sommes_colonnes([[1, 2], [3, 4], [5, 6]]) renvoie [9, 12].

**Q3** (1 pt, matrice) Expliquer le rôle de la ligne 2 de la fonction sommes_colonnes et indiquer pourquoi on utilise len(M[0]) plutôt que len(M).

<details><summary>Corrigé</summary>

La ligne 2 crée la liste des accumulateurs, une case par colonne, toutes initialisées à 0. Le nombre de colonnes est la longueur d'une ligne, len(M[0]) ; len(M) est le nombre de lignes (3 dans l'exemple, alors qu'il y a 2 colonnes) et donnerait une liste de mauvaise taille, voire une erreur d'indice.

</details>

### Exercice 4 — Bloc AES

L'algorithme de chiffrement symétrique AES chiffre les données par blocs de 128 bits. Chaque bloc est réparti dans une matrice carrée de taille 4 contenant 16 octets, remplie colonne par colonne. On chiffre le message de 16 caractères ASCII "NSI-TERMINALE-24".

**Q4** (1 pt, matrice) Indiquer le caractère placé à la ligne 1, colonne 2 de la matrice (indices commençant à 0) en tenant compte du remplissage colonne par colonne, et justifier que 16 octets correspondent bien à 128 bits.

<details><summary>Corrigé</summary>

Remplissage par colonnes : la case (i, j) contient le caractère d'indice 4 × j + i, soit 4 × 2 + 1 = 9. Le caractère d'indice 9 de "NSI-TERMINALE-24" est 'N' (N0 S1 I2 -3 T4 E5 R6 M7 I8 N9). 16 octets × 8 bits = 128 bits.

</details>

## I-mise_au_point
### Exercice 1 — Assertion et modèle relationnel

Une base de données de location de vélos contient la table Velo(id_velo, modele, km) dont id_velo est la clé primaire. Avant toute insertion, un programme Python vérifie que l'identifiant n'est pas déjà utilisé ; ids est la liste des id_velo déjà présents dans la table.
```python
1 def preparer_insertion(ids, nouveau_id, modele):
2     assert nouveau_id not in ids, "identifiant déjà utilisé"
3     return (nouveau_id, modele, 0)
```

**Q1** (1 pt, mise_au_point) Expliquer le rôle de la ligne 2 de la fonction preparer_insertion et décrire ce qui se passe lors de l'appel preparer_insertion([1, 2, 3], 2, 'VTT').

<details><summary>Corrigé</summary>

La ligne 2 vérifie une précondition : la clé primaire doit rester unique. Si la condition est fausse, l'exécution s'arrête en levant une AssertionError avec le message « identifiant déjà utilisé ». Pour l'appel donné, 2 est déjà dans ids : AssertionError, aucun tuple n'est renvoyé et l'insertion qui violerait la contrainte de clé primaire est évitée.

</details>

### Exercice 2 — Jeu de tests

La fonction suivante doit renvoyer la mention correspondant à une note sur 20.
```python
def mention(note):
    if note >= 16:
        return 'TB'
    elif note >= 14:
        return 'B'
    elif note > 12:
        return 'AB'
    else:
        return 'Aucune'
```
Tableau des mentions attendues :

| note | mention |
|---|---|
| [16 ; 20] | TB |
| [14 ; 16[ | B |
| [12 ; 14[ | AB |
| [0 ; 12[ | Aucune |

**Q2** (1 pt, mise_au_point) Donner l'instruction assert correspondant à un test qui met en évidence l'erreur de cette fonction, puis la correction à apporter.

<details><summary>Corrigé</summary>

assert mention(12) == 'AB' échoue (la fonction renvoie 'Aucune'). Correction : remplacer elif note > 12: par elif note >= 12:.

</details>

### Exercice 3 — Trouver le bug par la trace

On souhaite calculer la moyenne des éléments d'une liste non vide.
```python
1 def moyenne(tab):
2     s = 0
3     for i in range(1, len(tab)):
4         s = s + tab[i]
5     return s / len(tab)
6
7 m = moyenne([10, 4, 7])
```

**Q3** (1 pt, mise_au_point) Déterminer la valeur de m à l'issue des instructions ci-dessus, puis indiquer la ligne erronée et la corriger.

<details><summary>Corrigé</summary>

La boucle commence à 1 : s = 4 + 7 = 11, donc m = 11 / 3 ≈ 3.67 au lieu de 7.0. Ligne 3 erronée ; correction : for i in range(len(tab)): (ou range(0, len(tab))).

</details>

### Exercice 4 — Configuration de routes statiques

Un administrateur configure à la main les tables de routage d'un réseau de 6 routeurs. Pour éviter les erreurs de saisie, il écrit un script qui vérifie chaque table : routes est un dictionnaire {destination: passerelle} et voisins est la liste des routeurs directement reliés.
```python
def verifier(routes, voisins):
    for dest in routes:
        assert routes[dest] in voisins, dest
```
Pour le routeur R1, voisins = ['R2', 'R3'] et routes = {'R4': 'R2', 'R5': 'R3', 'R6': 'R5'}.

**Q4** (1 pt, mise_au_point) Indiquer le résultat de verifier(routes, voisins) pour R1 en tenant compte du fait que la configuration manuelle d'un grand réseau est fastidieuse et source d'erreurs, et citer une solution pour éviter ces erreurs.

<details><summary>Corrigé</summary>

La passerelle 'R5' indiquée pour la destination R6 n'est pas un voisin de R1 : l'assertion échoue et lève AssertionError: R6 (erreur de configuration détectée). Sur un réseau complexe, on utilise plutôt un protocole de routage dynamique (RIP ou OSPF) qui construit automatiquement les tables.

</details>

## I-modele_relationnel
### Exercice 1 — Médiathèque : adhérents lyonnais

Une médiathèque utilise une base de données dont le schéma relationnel est :
- Adherent(<u>id_adh</u>, nom, prenom, ville)
- Livre(<u>id_livre</u>, titre, annee)
- Emprunt(<u>id_emp</u>, #id_adh, #id_livre, date_emp)

Les attributs soulignés sont des clés primaires, ceux précédés de # des clés étrangères (id_adh fait référence à Adherent, id_livre à Livre).

La médiathèque veut contacter ses adhérents de Lyon.

**Q1** (1 pt, modele_relationnel) Écrire une requête SQL permettant d'afficher le nom et le prénom des adhérents habitant à Lyon, triés par ordre alphabétique de nom.

<details><summary>Corrigé</summary>

SELECT nom, prenom FROM Adherent WHERE ville = 'Lyon' ORDER BY nom;

</details>

### Exercice 2 — Médiathèque : rôle d'un attribut

Une médiathèque utilise une base de données dont le schéma relationnel est :
- Adherent(<u>id_adh</u>, nom, prenom, ville)
- Livre(<u>id_livre</u>, titre, annee)
- Emprunt(<u>id_emp</u>, #id_adh, #id_livre, date_emp)

Les attributs soulignés sont des clés primaires, ceux précédés de # des clés étrangères (id_adh fait référence à Adherent, id_livre à Livre).

On s'intéresse à l'attribut id_adh de la relation Emprunt. Trois termes sont proposés :
a) clé primaire de la relation Emprunt ;
b) clé étrangère de la relation Emprunt ;
c) domaine de l'attribut.

**Q2** (1 pt, modele_relationnel) Donner la lettre (a, b ou c) du terme correspondant au rôle de l'attribut id_adh dans la relation Emprunt, puis donner le nom de la relation à laquelle il fait référence.

<details><summary>Corrigé</summary>

b) id_adh est une clé étrangère de Emprunt ; elle fait référence à la clé primaire id_adh de la relation Adherent.

</details>

### Exercice 3 — Médiathèque : comptage des emprunts

Une médiathèque utilise une base de données dont le schéma relationnel est :
- Adherent(<u>id_adh</u>, nom, prenom, ville)
- Livre(<u>id_livre</u>, titre, annee)
- Emprunt(<u>id_emp</u>, #id_adh, #id_livre, date_emp)

Les attributs soulignés sont des clés primaires, ceux précédés de # des clés étrangères (id_adh fait référence à Adherent, id_livre à Livre).

La table Emprunt contient les 6 enregistrements suivants :

| id_emp | id_adh | id_livre | date_emp |
|---|---|---|---|
| 1 | 3 | 12 | '2026-01-04' |
| 2 | 1 | 7 | '2026-01-05' |
| 3 | 3 | 7 | '2026-01-09' |
| 4 | 2 | 15 | '2026-01-12' |
| 5 | 3 | 15 | '2026-02-01' |
| 6 | 4 | 12 | '2026-02-03' |

**Q3** (1 pt, modele_relationnel) Donner la requête SQL qui renvoie le nombre d'emprunts effectués par l'adhérent d'identifiant 3, puis la valeur renvoyée sur les données ci-dessus.

<details><summary>Corrigé</summary>

SELECT COUNT(*) FROM Emprunt WHERE id_adh = 3;
Valeur renvoyée : 3 (emprunts 1, 3 et 5).

</details>

### Exercice 4 — Médiathèque : cohérence des tables

Une médiathèque utilise une base de données dont le schéma relationnel est :
- Adherent(<u>id_adh</u>, nom, prenom, ville)
- Livre(<u>id_livre</u>, titre, annee)
- Emprunt(<u>id_emp</u>, #id_adh, #id_livre, date_emp)

Les attributs soulignés sont des clés primaires, ceux précédés de # des clés étrangères (id_adh fait référence à Adherent, id_livre à Livre).

La table Adherent contient uniquement les adhérents d'identifiants 1, 2, 3 et 4. Les livres d'identifiants 7, 12 et 15 existent dans la table Livre. Un bibliothécaire exécute :

INSERT INTO Emprunt (id_emp, id_adh, id_livre, date_emp) VALUES (7, 9, 12, '2026-03-01');

**Q4** (1 pt, modele_relationnel) Indiquer, en tenant compte des contraintes de clé étrangère, si cette insertion est acceptée par le SGBD, et justifier.

<details><summary>Corrigé</summary>

L'insertion est refusée : id_adh est une clé étrangère qui doit faire référence à une valeur existante de la clé primaire id_adh de Adherent. Or aucun adhérent d'identifiant 9 n'existe ; la contrainte d'intégrité référentielle serait violée (id_livre = 12 existe bien, id_emp = 7 est nouveau).

</details>

## I-modularite
### Exercice 1 — Module de géométrie

Un élève a écrit un module geometrie.py, rangé dans le même dossier que son programme principal. Sa documentation indique qu'il fournit une constante PI, une fonction aire_disque(r), une fonction perimetre_disque(r), une fonction aire_rectangle(longueur, largeur) et une fonction aire_triangle(base, hauteur), toutes renvoyant un flottant.

Dans son programme principal, il ne souhaite utiliser que les fonctions aire_disque et aire_rectangle, en les appelant directement par leur nom, sans préfixe.

**Q1** (1 pt, modularite) Donner la ligne d'importation à écrire en tête du programme principal.

<details><summary>Corrigé</summary>

from geometrie import aire_disque, aire_rectangle

</details>

### Exercice 2 — Lancers de dés

On utilise la fonction randint du module random : randint(a, b) renvoie un entier aléatoire compris entre a et b inclus. On veut simuler n lancers d'un dé à 6 faces, numérotées de 1 à 6.

```python
1 import random
2
3 def lancer_des(n):
4     """Renvoie la liste des résultats de n lancers d'un dé à 6 faces."""
5     resultats = ...
6     for i in range(...):
7         resultats.append(random.randint(..., ...))
8     return resultats
```

**Q2** (1 pt, modularite) Recopier et compléter les lignes 5, 6 et 7 de la fonction lancer_des.

<details><summary>Corrigé</summary>

5     resultats = []
6     for i in range(n):
7         resultats.append(random.randint(1, 6))

</details>

### Exercice 3 — Un module pile

Le fichier pile.py ci-dessous constitue un module fournissant une classe Pile. Il est importé dans d'autres programmes par from pile import Pile.

```python
 1 class Pile:
 2     """Pile implémentée à l'aide d'une liste Python."""
 3     def __init__(self):
 4         self.contenu = []
 5
 6     def est_vide(self):
 7         """Renvoie True si la pile est vide, False sinon."""
 8         return ...
 9
10     def empiler(self, x):
11         """Ajoute x au sommet de la pile."""
12         self.contenu.append(x)
13
14     def depiler(self):
15         """Retire et renvoie l'élément au sommet de la pile non vide."""
16         return ...
```

**Q3** (1 pt, modularite) Recopier et compléter les lignes 8 et 16 des méthodes est_vide et depiler de la classe Pile.

<details><summary>Corrigé</summary>

 8         return len(self.contenu) == 0
16         return self.contenu.pop()

</details>

### Exercice 4 — Exploiter les docstrings

En Python, la docstring d'une fonction f est accessible par l'attribut f.__doc__ (qui vaut None si la fonction n'est pas documentée) ou par help(f). Par exemple :

```python
def carre(x):
    """Renvoie le carré du nombre x."""
    return x * x

>>> carre.__doc__
'Renvoie le carré du nombre x.'
```

**Q4** (1 pt, modularite) Écrire une fonction doc_contient qui prend en paramètres une fonction f et une chaîne mot, et qui renvoie True si la docstring de f contient mot, False sinon (y compris si f n'a pas de docstring).

<details><summary>Corrigé</summary>

def doc_contient(f, mot):
    doc = f.__doc__
    if doc is None:
        return False
    return mot in doc

# doc_contient(carre, 'carré') renvoie True ; doc_contient(carre, 'cube') renvoie False.

</details>

## I-os_commandes
### Exercice 1 — Se repérer dans l'arborescence

Lina travaille dans un terminal sous Linux. Après plusieurs commandes cd, elle ne sait plus dans quel répertoire elle se trouve.
Elle souhaite afficher le chemin absolu du répertoire courant avant de créer un nouveau dossier.

**Q1** (1 pt, os_commandes) Donner le nom de la commande permettant d'afficher le chemin absolu du répertoire courant.

<details><summary>Corrigé</summary>

pwd (print working directory).

</details>

### Exercice 2 — Droits d'un fichier

Le fichier rapport.txt appartient à Lina. Elle veut que son propriétaire puisse le lire, le modifier et l'exécuter, que les membres de son groupe puissent seulement le lire et l'exécuter, et que les autres utilisateurs n'aient aucun droit, c'est-à-dire obtenir les droits rwxr-x---.

**Q2** (1 pt, os_commandes) Écrire la commande chmod qui attribue au fichier rapport.txt exactement les droits rwxr-x---.

<details><summary>Corrigé</summary>

chmod 750 rapport.txt
(équivalent : chmod u=rwx,g=rx,o= rapport.txt ; 7 = rwx, 5 = r-x, 0 = ---).

</details>

### Exercice 3 — Remonter d'un niveau

Lina est dans le répertoire /home/lina/projets/nsi. Elle tape cd ..

**Q3** (1 pt, os_commandes) Quel est le répertoire courant après cette commande ? Justifier.

<details><summary>Corrigé</summary>

/home/lina/projets : cd .. remonte d'un niveau, vers le répertoire parent du répertoire courant.

</details>

### Exercice 4 — Tester une machine distante

Depuis son ordinateur sous Linux, Lina n'arrive pas à accéder à l'imprimante réseau d'adresse IP 192.168.1.20. Elle veut d'abord vérifier que cette machine est accessible à travers le réseau IP.

**Q4** (1 pt, os_commandes) Quelle est la commande complète que Lina doit taper pour tester l'accessibilité de l'imprimante ?

<details><summary>Corrigé</summary>

ping 192.168.1.20 (ping teste l'accessibilité d'une machine à travers un réseau IP ; traceroute donnerait en plus la liste des routeurs traversés).

</details>

## I-paradigmes
### Exercice 1 — Deux styles pour une même somme

On veut calculer la somme des carrés des éléments d'une liste d'entiers, par exemple 14 pour [1, 2, 3], d'abord en style impératif (lignes 1 à 5), puis en style fonctionnel sans variable modifiée (lignes 7 et 8).

```python
1 def somme_carres_imp(tab):
2     total = ...
3     for x in tab:
4         total = ...
5     return total
6
7 def somme_carres_fonc(tab):
8     return sum(...)
```

**Q1** (1 pt, paradigmes) Recopier et compléter les lignes 2, 4 et 8.

<details><summary>Corrigé</summary>

2     total = 0
4         total = total + x * x
8     return sum([x * x for x in tab])

</details>

### Exercice 2 — Programmation objet : un compte

Dans le paradigme objet, on modélise un compte bancaire par la classe suivante :

```python
class Compte:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
```

La méthode retirer prend en paramètre un montant positif ; si le solde est suffisant, elle le diminue de ce montant et renvoie True, sinon elle ne modifie rien et renvoie False.

**Q2** (1 pt, paradigmes) Écrire le code de la méthode retirer de la classe Compte.

<details><summary>Corrigé</summary>

    def retirer(self, montant):
        if self.solde >= montant:
            self.solde = self.solde - montant
            return True
        return False

</details>

### Exercice 3 — Fonction pure et boucles

On considère le programme suivant, qui combine une fonction pure et deux boucles impératives :

```python
1 def f(x):
2     return 2 * x + 1
3
4 res = []
5 for k in range(4):
6     res.append(f(k))
7 total = 0
8 for v in res:
9     total = total + v
```

**Q3** (1 pt, paradigmes) Déterminer les valeurs des variables res et total à l'issue de l'exécution de ce programme.

<details><summary>Corrigé</summary>

res = [1, 3, 5, 7] (f(0)=1, f(1)=3, f(2)=5, f(3)=7) et total = 1 + 3 + 5 + 7 = 16.

</details>

### Exercice 4 — Fibonacci impératif

La suite de Fibonacci est définie par F(0) = 0, F(1) = 1 et F(n) = F(n-1) + F(n-2) pour n ≥ 2. Une version récursive naïve est très lente ; on souhaite une version impérative, avec une boucle.

**Q4** (1 pt, paradigmes) Écrire une fonction fibo_imperatif qui prend en paramètre un entier n ≥ 0 et qui renvoie F(n), calculé de façon impérative (sans récursivité).

<details><summary>Corrigé</summary>

def fibo_imperatif(n):
    a, b = 0, 1
    for k in range(n):
        a, b = b, a + b
    return a

# fibo_imperatif(0) = 0, fibo_imperatif(10) = 55

</details>

## I-parcours_arbre
### Exercice 1 — Parcours infixe

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
```

L'arbre binaire de recherche A a pour racine 8 ; le fils gauche de 8 est 3 (fils gauche 1, fils droit 6) ; le fils droit de 8 est 10, qui a pour seul fils un fils droit 14.

```python
A = Noeud(8, Noeud(3, Noeud(1), Noeud(6)), Noeud(10, None, Noeud(14)))
```

La fonction infixe renvoie la liste des valeurs dans l'ordre infixe ; l'appel infixe(A) doit renvoyer [1, 3, 6, 8, 10, 14].

```python
1 def infixe(arbre):
2     if arbre is None:
3         return ...
4     return infixe(...) + [...] + infixe(...)
```

**Q1** (1 pt, parcours_arbre) Recopier et compléter les lignes 3 et 4 de la fonction infixe.

<details><summary>Corrigé</summary>

3         return []
4     return infixe(arbre.gauche) + [arbre.valeur] + infixe(arbre.droit)

</details>

### Exercice 2 — Nœuds d'une profondeur donnée

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
```

L'arbre binaire de recherche A a pour racine 8 ; le fils gauche de 8 est 3 (fils gauche 1, fils droit 6) ; le fils droit de 8 est 10, qui a pour seul fils un fils droit 14.

```python
A = Noeud(8, Noeud(3, Noeud(1), Noeud(6)), Noeud(10, None, Noeud(14)))
```

On convient que la racine est de profondeur 0 (ses fils de profondeur 1, etc.). Par exemple niveau(A, 2) renvoie [1, 6, 14] (lus de gauche à droite).

**Q2** (1 pt, parcours_arbre) Écrire une fonction niveau qui prend en paramètres un arbre binaire arbre (de type Noeud ou None) et un entier k, et qui renvoie la liste des valeurs des nœuds de profondeur k, de gauche à droite.

<details><summary>Corrigé</summary>

def niveau(arbre, k):
    if arbre is None:
        return []
    if k == 0:
        return [arbre.valeur]
    return niveau(arbre.gauche, k - 1) + niveau(arbre.droit, k - 1)

</details>

### Exercice 3 — Identifier un parcours

```python
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
```

L'arbre binaire de recherche A a pour racine 8 ; le fils gauche de 8 est 3 (fils gauche 1, fils droit 6) ; le fils droit de 8 est 10, qui a pour seul fils un fils droit 14.

```python
A = Noeud(8, Noeud(3, Noeud(1), Noeud(6)), Noeud(10, None, Noeud(14)))
```

Un programme parcourt l'arbre A en profondeur et affiche les valeurs dans l'ordre suivant : 1 6 3 14 10 8

**Q3** (1 pt, parcours_arbre) Choisir, en justifiant, le type de parcours réalisé parmi : préfixe, suffixe ou infixe.

<details><summary>Corrigé</summary>

Parcours suffixe (postfixe) : chaque nœud est affiché après ses deux sous-arbres (1 6 puis 3 ; 14 puis 10 ; la racine 8 en dernier). Ce n'est pas infixe (l'ordre n'est pas croissant) ni préfixe (la racine 8 n'est pas en premier).

</details>

## I-parcours_graphe
### Exercice 1 — Distances depuis l'entrée

Le graphe non orienté suivant représente des salles d'un musée reliées par des couloirs, sous forme de dictionnaire d'adjacence :

```python
G = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'],
     'D': ['B', 'C', 'F'], 'E': ['C', 'F'], 'F': ['D', 'E']}
```

Un parcours en largeur depuis A permet de calculer la distance (nombre minimal de couloirs) de A à chaque salle. On range ces distances dans une liste, dans l'ordre des salles ['A', 'B', 'C', 'D', 'E', 'F'] :

```python
distances = [0, 1, ..., ..., ..., ...]
```

**Q1** (1 pt, parcours_graphe) Recopier et compléter la liste distances donnée ci-dessus.

<details><summary>Corrigé</summary>

distances = [0, 1, 1, 2, 2, 3]
(B et C sont voisins de A ; D et E sont découverts depuis B ou C ; F depuis D ou E).

</details>

### Exercice 2 — Classe Graphe et parcours en largeur

```python
 1 class Graphe:
 2     def __init__(self):
 3         self.adj = {}
 4
 5     def ajouter_arete(self, s1, s2):
 6         if s1 not in self.adj:
 7             self.adj[s1] = []
 8         if s2 not in self.adj:
 9             self.adj[s2] = []
10         self.adj[s1].append(s2)
11         self.adj[s2].append(s1)
12
13     def largeur(self, depart):
14         visites = [depart]
15         file = [depart]
16         while ...:
17             s = file.pop(0)
18             for v in self.adj[s]:
19                 if ...:
20                     visites.append(v)
21                     ...
22         return visites
```

La méthode largeur renvoie la liste des sommets dans l'ordre de leur découverte par un parcours en largeur depuis depart ; la liste file joue le rôle de file.

**Q2** (1 pt, parcours_graphe) Recopier et compléter les lignes 16, 19 et 21 de la méthode largeur de la classe Graphe.

<details><summary>Corrigé</summary>

16         while len(file) > 0:
19                 if v not in visites:
21                     file.append(v)

</details>

### Exercice 3 — Reconstituer un chemin

Le graphe non orienté suivant représente des salles d'un musée reliées par des couloirs, sous forme de dictionnaire d'adjacence :

```python
G = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'],
     'D': ['B', 'C', 'F'], 'E': ['C', 'F'], 'F': ['D', 'E']}
```

Un parcours en largeur depuis A a produit le dictionnaire parents, qui associe à chaque sommet découvert le sommet qui a permis de le découvrir :

```python
parents = {'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'C', 'F': 'D'}
```

La fonction chemin prend en paramètres ce dictionnaire parents, le sommet de départ depart et un sommet arrivee, et renvoie la liste des sommets du chemin de depart à arrivee. Par exemple chemin(parents, 'A', 'F') renvoie ['A', 'B', 'D', 'F'].

**Q3** (1 pt, parcours_graphe) Écrire la fonction chemin.

<details><summary>Corrigé</summary>

def chemin(parents, depart, arrivee):
    ch = [arrivee]
    s = arrivee
    while s != depart:
        s = parents[s]
        ch.append(s)
    ch.reverse()
    return ch

</details>

### Exercice 4 — Couloirs pondérés

On pondère maintenant les couloirs du musée par leur longueur en mètres :

| Couloir | A-B | A-C | B-D | C-D | C-E | D-F | E-F |
|---|---|---|---|---|---|---|---|
| Longueur | 2 | 5 | 4 | 2 | 2 | 3 | 6 |

**Q4** (1 pt, parcours_graphe) Quel est le chemin reliant A et F qui a le plus petit coût (longueur totale) ? Justifier en donnant son coût.

<details><summary>Corrigé</summary>

A-B-D-F, de coût 2 + 4 + 3 = 9. Les autres chemins coûtent plus : A-C-D-F = 10, A-C-E-F = 13, A-B-D-C-E-F = 16.

</details>

## I-pile
### Exercice 1 — Pile de livres à ranger

Une bibliothécaire empile des livres sur un chariot. On utilise la classe suivante :

```python
class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return self.contenu == []

    def empiler(self, x):
        self.contenu.append(x)

    def depiler(self):
        return self.contenu.pop()
```

On exécute les instructions du tableau ci-dessous, dans l'ordre :

| Étape | Instruction |
|---|---|
| 1 | `p = Pile()` |
| 2 | `p.empiler('Hugo')` |
| 3 | `p.empiler('Zola')` |
| 4 | `p.empiler('Sand')` |
| 5 | `a = p.depiler()` |
| 6 | `p.empiler('Verne')` |
| 7 | `b = p.depiler()` |
| 8 | `c = p.depiler()` |

**Q1** (1 pt, pile) Quelle est la valeur de la variable `c` à l'issue de l'étape 8 ? Quel est alors le contenu de la pile `p` ?

<details><summary>Corrigé</summary>

`c` vaut 'Zola' (a = 'Sand', b = 'Verne'). La pile contient alors seulement 'Hugo'.

</details>

### Exercice 2 — Consulter le sommet

On reprend la classe `Pile` ci-dessous, dont le contenu est stocké dans une liste Python dont le dernier élément est le sommet.

```python
class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return self.contenu == []

    def empiler(self, x):
        self.contenu.append(x)

    def depiler(self):
        return self.contenu.pop()
```

La méthode `sommet` ne prend aucun paramètre (autre que `self`) et renvoie l'élément situé au sommet de la pile sans le retirer ; elle renvoie `None` si la pile est vide.

**Q2** (1 pt, pile) Écrire le code de la méthode `sommet` de la classe `Pile` qui renvoie l'élément au sommet de la pile sans modifier la pile.

<details><summary>Corrigé</summary>

```python
    def sommet(self):
        if self.est_vide():
            return None
        return self.contenu[-1]
```
(Variante acceptée : x = self.depiler(); self.empiler(x); return x.)

</details>

### Exercice 3 — Pile et boucle

On dispose de la classe `Pile` suivante :

```python
class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return self.contenu == []

    def empiler(self, x):
        self.contenu.append(x)

    def depiler(self):
        return self.contenu.pop()
```

On exécute les instructions :

```python
valeurs = [4, 7, 1, 9, 3]
p = Pile()
for i in range(len(valeurs)):
    if valeurs[i] % 2 == 1:
        p.empiler(valeurs[i])
resultat = []
while not p.est_vide():
    resultat.append(p.depiler())
```

**Q3** (1 pt, pile) Déterminer la valeur de la variable `resultat` à l'issue de ces instructions.

<details><summary>Corrigé</summary>

`resultat` vaut `[3, 9, 1, 7]` : seuls les impairs 7, 1, 9, 3 sont empilés, puis dépilés dans l'ordre inverse (LIFO).

</details>

### Exercice 4 — Annulation dans un éditeur

Un éditeur de texte enregistre chaque action de l'utilisateur dans une pile d'annulation. L'utilisateur effectue successivement les actions : « taper bonjour », « mettre en gras », « changer la police », « souligner ». Il appuie ensuite trois fois sur le bouton « Annuler », chaque appui annulant une action retirée de la pile.

**Q4** (1 pt, pile) Indiquer, dans l'ordre, les trois actions annulées, en tenant compte du mode de fonctionnement d'une pile, puis nommer ce mode (acronyme et signification).

<details><summary>Corrigé</summary>

Ordre d'annulation : « souligner », puis « changer la police », puis « mettre en gras ». Il reste « taper bonjour ». La pile fonctionne en mode LIFO : Last In, First Out (dernier arrivé, premier sorti).

</details>

## I-poo
### Exercice 1 — Objets persistés en base

Une application de gestion de vélos en libre-service utilise une classe `Velo` dont chaque instance possède les attributs `num`, `station` et `km`. Les objets sont sauvegardés dans une table `velo(num, station, km)` d'une base de données, chaque attribut d'objet correspondant à un attribut de la table.

**Q1** (1 pt, poo) Écrire une requête SQL permettant d'afficher le numéro des vélos de la station 'Gare' ayant parcouru plus de 1000 km.

<details><summary>Corrigé</summary>

```sql
SELECT num FROM velo WHERE station = 'Gare' AND km > 1000;
```

</details>

### Exercice 2 — Classe et table

On donne la classe Python et un extrait de la table `adherent` d'une base `club` :

```python
class Adherent:
    def __init__(self, id_adh, nom, age):
        self.id_adh = id_adh
        self.nom = nom
        self.age = age
```

| id_adh | nom | age |
|---|---|---|
| 1 | Lina | 16 |
| 2 | Tom | 17 |

L'attribut `id_adh` est la clé primaire de la table. Un programme crée l'objet `a = Adherent(2, 'Inès', 15)` puis tente d'exécuter `INSERT INTO adherent VALUES (2, 'Inès', 15);`.

**Q2** (1 pt, poo) On cherche à enregistrer l'objet `a` dans la base `club`. Expliquer pourquoi la création de l'objet réussit en Python alors que l'insertion échoue.

<details><summary>Corrigé</summary>

Python n'impose aucune contrainte d'unicité sur l'attribut id_adh : l'instanciation crée simplement un nouvel objet. En revanche, dans la base, id_adh est clé primaire et la valeur 2 existe déjà (Tom) : la contrainte d'unicité de la clé primaire (contrainte de relation) est violée, l'insertion est refusée.

</details>

### Exercice 3 — Filtrer des objets

Une classe `Film` possède les attributs `titre`, `annee` et `duree` (en minutes). Une classe `Catalogue` possède un attribut `films`, liste d'objets `Film`. On souhaite obtenir, sans base de données, l'équivalent du besoin « les titres des films sortis après l'an 2000 dont la durée est inférieure à 120 minutes ».

```python
class Film:
    def __init__(self, titre, annee, duree):
        self.titre = titre
        self.annee = annee
        self.duree = duree

class Catalogue:
    def __init__(self):
        self.films = []

    def ajouter(self, film):
        self.films.append(film)
```

**Q3** (1 pt, poo) Écrire le code de la méthode `courts_recents` de la classe `Catalogue` qui renvoie la liste des titres des films sortis strictement après 2000 et de durée strictement inférieure à 120 minutes.

<details><summary>Corrigé</summary>

```python
    def courts_recents(self):
        res = []
        for f in self.films:
            if f.annee > 2000 and f.duree < 120:
                res.append(f.titre)
        return res
```

</details>

### Exercice 4 — Insertion dans un arbre objet

On représente un arbre binaire de recherche par la classe suivante, où un arbre vide est représenté par `None` :

```python
class Arbre:
    def __init__(self, cle, gauche=None, droit=None):
        self.cle = cle
        self.gauche = gauche
        self.droit = droit

def inserer(a, cle):
    if a is None:
        return Arbre(cle)
    if cle < a.cle:
        a.gauche = inserer(a.gauche, cle)
    else:
        a.droit = inserer(a.droit, cle)
    return a

r = inserer(None, 8)
r = inserer(r, 3)
r = inserer(r, 11)
r = inserer(r, 5)
```

**Q4** (1 pt, poo) Donner la valeur de `r.cle`, de `r.gauche.droit.cle` ainsi que la nature de l'objet renvoyé par l'appel `inserer(None, 8)`.

<details><summary>Corrigé</summary>

`r.cle` vaut 8 ; `r.gauche.droit.cle` vaut 5 (3 à gauche de 8, 5 à droite de 3). L'appel `inserer(None, 8)` porte sur un arbre vide : il renvoie un nouvel objet `Arbre` contenant la clé 8 et deux sous-arbres vides (None).

</details>

## I-processus
### Exercice 1 — États d'un processus

Un processus peut se trouver dans l'un des trois états suivants :
- Prêt : il attend que l'ordonnanceur lui attribue le processeur ;
- Élu : il est en cours d'exécution ;
- Bloqué : il attend une ressource indisponible.

Le tableau suivant décrit des transitions, mais certaines cases sont manquantes :

| Événement | État de départ | État d'arrivée |
|---|---|---|
| l'ordonnanceur choisit le processus | Prêt | ... |
| le processus demande la lecture d'un fichier sur disque | ... | Bloqué |
| la lecture du fichier est terminée | Bloqué | ... |
| le quantum de temps est écoulé | Élu | ... |

**Q1** (1 pt, processus) Recopier et compléter le tableau des transitions donné ci-dessus.

<details><summary>Corrigé</summary>

Ligne 1 : Élu. Ligne 2 : Élu (départ). Ligne 3 : Prêt (un processus débloqué ne repasse pas directement Élu). Ligne 4 : Prêt.

</details>

### Exercice 2 — Commande ps

Sur un système Linux, la commande `ps -ef` affiche, pour chaque processus, l'utilisateur, le PID, le PPID, l'heure de lancement, le terminal et la commande. On obtient l'extrait suivant :

| UID | PID | PPID | CMD |
|---|---|---|---|
| root | 1 | 0 | /sbin/init |
| alice | 812 | 1 | bash |
| alice | 954 | 812 | python3 jeu.py |
| alice | 960 | 954 | python3 son.py |

**Q2** (1 pt, processus) Donner la valeur du PID du processus parent du processus `python3 son.py`, puis la commande de ce processus parent.

<details><summary>Corrigé</summary>

Le PPID de son.py est 954 ; ce processus parent est `python3 jeu.py`.

</details>

### Exercice 3 — Interblocage

Deux processus P1 et P2 utilisent deux ressources R1 (imprimante) et R2 (scanner).
a) P1 obtient R1, puis demande R2.
b) P2 obtient R2, puis demande R1.
Chaque processus ne libère une ressource qu'après avoir terminé son travail.

**Q3** (1 pt, processus) Quel est l'état de P1 et de P2 après les étapes a) et b) ? Quel est le nom de cette situation ? Justifier.

<details><summary>Corrigé</summary>

P1 et P2 sont tous deux dans l'état Bloqué : chacun attend une ressource détenue par l'autre, qui ne la libérera jamais. C'est un interblocage (deadlock).

</details>

### Exercice 4 — Ordonnancement FIFO

Quatre processus arrivent dans la file d'attente de l'ordonnanceur au même instant t = 0 et y sont placés dans l'ordre C1, C2, C3 et C4. Leurs durées d'exécution sont : C1 : 3 unités, C2 : 1 unité, C3 : 4 unités, C4 : 2 unités. L'ordonnanceur suit la politique « premier arrivé, premier servi » (FIFO), sans interruption.

**Q4** (1 pt, processus) Indiquer l'instant de fin de chacun des quatre processus en tenant compte de leur ordre d'arrivée dans la file.

<details><summary>Corrigé</summary>

C1 se termine à t = 3, C2 à t = 4, C3 à t = 8, C4 à t = 10.

</details>

## I-prog_dynamique
### Exercice 1 — Chemins dans une grille

On cherche le nombre de chemins allant du coin supérieur gauche au coin inférieur droit d'une grille de n lignes et m colonnes de cases, en se déplaçant le long des traits uniquement vers la droite ou vers le bas. On note c(i, j) le nombre de chemins menant au point d'intersection (i, j) ; on a c(i, 0) = c(0, j) = 1 et c(i, j) = c(i-1, j) + c(i, j-1).

La fonction `nb_chemins` prend en paramètres deux entiers `n` et `m` et renvoie le nombre de chemins, calculé par programmation dynamique ascendante à l'aide d'un tableau de (n+1) lignes et (m+1) colonnes.

**Q1** (1 pt, prog_dynamique) Écrire la fonction `nb_chemins` qui renvoie ce nombre de chemins en utilisant la programmation dynamique.

<details><summary>Corrigé</summary>

```python
def nb_chemins(n, m):
    c = [[1] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c[i][j] = c[i - 1][j] + c[i][j - 1]
    return c[n][m]
```
Par exemple nb_chemins(2, 3) renvoie 10.

</details>

### Exercice 2 — Rendu de monnaie

On dispose d'un système de pièces (une liste d'entiers strictement positifs contenant 1) et d'une somme à rendre (un entier positif). On veut le nombre minimal de pièces (chaque pièce pouvant être utilisée plusieurs fois). On note nb[s] ce minimum pour la somme s (avec nb[0] = 0).

**Q2** (1 pt, prog_dynamique) Écrire une fonction `rendu_min` qui prend en paramètres `pieces` (liste d'entiers) et `somme` (entier) et qui renvoie le nombre minimal de pièces, par programmation dynamique.

<details><summary>Corrigé</summary>

```python
def rendu_min(pieces, somme):
    nb = [0] * (somme + 1)
    for s in range(1, somme + 1):
        nb[s] = s  # avec uniquement des pièces de 1
        for p in pieces:
            if p <= s and nb[s - p] + 1 < nb[s]:
                nb[s] = nb[s - p] + 1
    return nb[somme]
```
Exemple : rendu_min([1, 4, 6], 8) renvoie 2 (4 + 4), alors que le glouton donne 3.

</details>

### Exercice 3 — Mémoïser dans une base

Un site de calcul stocke, dans une table `fibo(n, valeur)` de la base `cache` dont `n` est la clé primaire, les termes de la suite de Fibonacci déjà calculés. Pour calculer F(n), le programme cherche d'abord F(n-1) et F(n-2) dans la table ; s'ils y figurent, il calcule F(n) = F(n-1) + F(n-2) puis l'insère. La table contient actuellement les lignes (0, 0), (1, 1), …, (40, 102334155).

**Q3** (1 pt, prog_dynamique) On cherche à obtenir F(41) dans la base `cache`. Expliquer pourquoi ce calcul est immédiat, et le lien avec la programmation dynamique.

<details><summary>Corrigé</summary>

F(40) et F(39) sont déjà dans la table : il suffit de deux lectures et d'une addition (F(41) = 102334155 + 63245986 = 165580141), sans recalculer les sous-problèmes. C'est le principe de la programmation dynamique : déterminer un résultat à partir de résultats précédents mémorisés (mémoïsation), au prix d'un coût en mémoire.

</details>

## I-recherche_dichotomique
### Exercice 1 — Retrouver un numéro de dossard

Les 2000 dossards d'une course sont rangés dans une liste `tab` triée par ordre croissant. La fonction `recherche` renvoie l'indice du dossard `val` dans `tab`, ou -1 s'il est absent ; elle doit effectuer une recherche dichotomique.

```python
1  def recherche(tab, val):
2      debut = 0
3      fin = len(tab) - 1
4      while debut <= fin:
5          milieu = ...
6          if tab[milieu] == val:
7              return milieu
8          elif tab[milieu] < val:
9              debut = ...
10         else:
11             fin = ...
12     return -1
```

**Q1** (1 pt, recherche_dichotomique) Recopier et compléter les lignes 5, 9 et 11 de la fonction `recherche`.

<details><summary>Corrigé</summary>

Ligne 5 : `milieu = (debut + fin) // 2` ; ligne 9 : `debut = milieu + 1` ; ligne 11 : `fin = milieu - 1`.

</details>

### Exercice 2 — Annuaire trié

On donne la classe `Annuaire` dont l'attribut `noms` est une liste de chaînes triée par ordre alphabétique.

```python
1  class Annuaire:
2      def __init__(self, noms):
3          self.noms = sorted(noms)
4
5      def contient(self, nom):
6          g = 0
7          d = len(self.noms) - 1
8          while g <= d:
9              m = (g + d) // 2
10             if self.noms[m] == nom:
11                 return ...
12             elif self.noms[m] < nom:
13                 ...
14             else:
15                 ...
16         return ...
```

**Q2** (1 pt, recherche_dichotomique) Recopier et compléter les lignes 11, 13, 15 et 16 de la méthode `contient`, qui renvoie True si `nom` est présent, False sinon.

<details><summary>Corrigé</summary>

Ligne 11 : `return True` ; ligne 13 : `g = m + 1` ; ligne 15 : `d = m - 1` ; ligne 16 : `return False`.

</details>

### Exercice 3 — Nombre de comparaisons

On applique la recherche dichotomique dans une liste triée de 1024 éléments :
- à chaque tour de boucle, on compare la valeur cherchée à l'élément du milieu ;
- la zone de recherche est ensuite (environ) divisée par deux ;
- la recherche s'arrête si la valeur est trouvée ou si la zone est vide.

**Q3** (1 pt, recherche_dichotomique) Quel est le nombre maximal de tours de boucle nécessaires dans le pire cas ? Quel est le coût de cet algorithme en fonction de la taille n ? Justifier.

<details><summary>Corrigé</summary>

Au plus 11 tours (1024 = 2^10 : la zone passe de 1024 à 512, …, 1, soit 10 divisions puis un dernier tour). Le coût est logarithmique, en O(log2 n), car la taille est divisée par 2 à chaque étape.

</details>

### Exercice 4 — Index trié d'une base

La table `client` de la base `boutique` contient 1 000 000 de lignes. Le SGBD maintient un index : la liste des valeurs de la clé primaire `id_client` triée par ordre croissant, dans laquelle il cherche par dichotomie. Sans index, il parcourt les lignes une par une.

**Q4** (1 pt, recherche_dichotomique) On cherche à exécuter `SELECT * FROM client WHERE id_client = 734512;` dans la base `boutique`. Expliquer pourquoi l'index accélère la recherche, en donnant un ordre de grandeur du nombre de comparaisons dans chaque cas.

<details><summary>Corrigé</summary>

La dichotomie divise par deux la taille de la zone de recherche à chaque étape : environ log2(10^6) ≈ 20 comparaisons au plus, contre jusqu'à 1 000 000 pour un parcours séquentiel. L'index trié est nécessaire car la dichotomie ne fonctionne que sur des données triées.

</details>

## I-recherche_textuelle
### Exercice 1 — Rechercher un motif dans une base

Une base `bibli` contient la table `livre(id, titre, resume)`. On veut les livres dont le résumé contient le mot « dragon ». On compare deux solutions :

```sql
SELECT titre FROM livre WHERE resume LIKE '%dragon%';
```

```python
def contient(texte, motif):
    n, m = len(texte), len(motif)
    for i in range(n - m + 1):
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j = j + 1
        if j == m:
            return True
    return False
```

| id | titre | resume |
|---|---|---|
| 1 | Le Val | un Dragon garde la vallée |
| 2 | Braises | les dragons dorment |

**Q1** (1 pt, recherche_textuelle) On cherche à sélectionner les livres de la base `bibli` dont le résumé contient « dragon ». Indiquer le résultat de la fonction `contient` sur chacun des deux résumés, et expliquer le phénomène observé pour le livre 1.

<details><summary>Corrigé</summary>

contient('un Dragon garde la vallée', 'dragon') renvoie False ; contient('les dragons dorment', 'dragon') renvoie True. Pour le livre 1, la recherche naïve compare les caractères exactement : 'D' ≠ 'd', la recherche est sensible à la casse, donc le motif n'est pas trouvé (il faudrait par exemple comparer texte.lower()).

</details>

### Exercice 2 — Recherche naïve

On recherche le motif `motif` de longueur 3 dans un texte de longueur 12. La fonction `recherche_naive` renvoie la liste des positions de toutes les occurrences.

```python
1  def recherche_naive(texte, motif):
2      positions = []
3      for i in range(...):
4          j = 0
5          while j < len(motif) and ...:
6              j = j + 1
7          if ...:
8              positions.append(i)
9      return positions
```

**Q2** (1 pt, recherche_textuelle) Recopier et compléter les lignes 3, 5 et 7 de la fonction `recherche_naive`.

<details><summary>Corrigé</summary>

Ligne 3 : `for i in range(len(texte) - len(motif) + 1):` ; ligne 5 : `while j < len(motif) and texte[i + j] == motif[j]:` ; ligne 7 : `if j == len(motif):`. Exemple : recherche_naive('abracadabra', 'abr') renvoie [0, 7].

</details>

### Exercice 3 — Table des décalages

On donne la classe `Motif` utilisée par l'algorithme de Boyer-Moore-Horspool. La méthode `table_sauts` renvoie un dictionnaire associant à chaque caractère du motif, sauf le dernier, la distance entre sa dernière occurrence (hors dernière position) et la fin du motif.

```python
1  class Motif:
2      def __init__(self, chaine):
3          self.chaine = chaine
4
5      def table_sauts(self):
6          m = len(self.chaine)
7          d = {}
8          for i in range(...):
9              d[self.chaine[i]] = ...
10         return d
11
12     def saut(self, c):
13         d = self.table_sauts()
14         if c in d:
15             return d[c]
16         return ...
```

Par exemple `Motif('maman').table_sauts()` renvoie `{'m': 2, 'a': 1}`.

**Q3** (1 pt, recherche_textuelle) Recopier et compléter les lignes 8, 9 et 16 de la classe `Motif`, la méthode `saut` renvoyant la longueur du motif si le caractère n'y figure pas.

<details><summary>Corrigé</summary>

Ligne 8 : `for i in range(m - 1):` ; ligne 9 : `d[self.chaine[i]] = m - 1 - i` ; ligne 16 : `return len(self.chaine)`. Vérification : pour 'maman', m=5 : 'm'→4 puis 2, 'a'→3 puis 1, donc {'m': 2, 'a': 1}.

</details>

### Exercice 4 — Arrêt à la première occurrence

On dispose de la fonction suivante, qui compte les occurrences d'un motif :

```python
def compte(texte, motif):
    n, m = len(texte), len(motif)
    nb = 0
    for i in range(n - m + 1):
        if texte[i:i + m] == motif:
            nb = nb + 1
    return nb
```

**Q4** (1 pt, recherche_textuelle) Ré-écrire cet algorithme sous la forme d'une fonction `premiere` qui s'arrête dès qu'une occurrence du motif est trouvée et renvoie sa position, ou -1 en l'absence d'occurrence.

<details><summary>Corrigé</summary>

```python
def premiere(texte, motif):
    n, m = len(texte), len(motif)
    i = 0
    while i <= n - m:
        if texte[i:i + m] == motif:
            return i
        i = i + 1
    return -1
```
Exemple : premiere('banane', 'an') renvoie 1.

</details>

## I-recursivite
### Exercice 1 — Comptage récursif dans une liste

Une station météo enregistre chaque jour un code d'alerte entier. Les relevés sont stockés dans des listes Python. On veut compter le nombre de jours où un code donné apparaît, sans utiliser de boucle.

Exemples attendus :
```python
>>> compte([3, 1, 3, 3, 2], 3)
3
>>> compte([0, 2, 2], 1)
0
>>> compte([], 5)
0
```

**Q1** (1 pt, recursivite) Écrire une fonction récursive compte qui prend en paramètres une liste tab et une valeur x et qui renvoie le nombre d'occurrences de x dans tab.

<details><summary>Corrigé</summary>

```python
def compte(tab, x):
    if tab == []:
        return 0
    if tab[0] == x:
        return 1 + compte(tab[1:], x)
    return compte(tab[1:], x)
```
Cas de base : liste vide → 0 ; sinon on traite le premier élément et on appelle récursivement sur le reste.

</details>

### Exercice 2 — Longueur d'une liste chaînée

Un lecteur audio stocke sa file de lecture sous forme de liste chaînée. On dispose de la classe suivante :
```python
class Maillon:
    def __init__(self, titre, suivant=None):
        self.titre = titre
        self.suivant = suivant

    def longueur(self):
        ...
```
La méthode longueur ne prend pas d'autre paramètre que self et renvoie le nombre de maillons de la chaîne qui commence au maillon self (self compris). Par exemple, Maillon('A', Maillon('B', Maillon('C'))).longueur() renvoie 3.

**Q2** (1 pt, recursivite) Écrire le code récursif de la méthode longueur de la classe Maillon qui renvoie le nombre de maillons de la chaîne commençant à self.

<details><summary>Corrigé</summary>

```python
    def longueur(self):
        if self.suivant is None:
            return 1
        return 1 + self.suivant.longueur()
```

</details>

### Exercice 3 — Lecture d'une fonction récursive

On considère la fonction suivante :
```python
def mystere(n):
    if n <= 1:
        return n
    return mystere(n - 1) + 2 * mystere(n - 2)
```
On a commencé à remplir le tableau des valeurs renvoyées :

| n | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| mystere(n) | 0 | 1 | 1 | 3 | ... | ... |

**Q3** (1 pt, recursivite) Quelle est la valeur renvoyée par l'appel mystere(5) ? Justifier à l'aide du tableau.

<details><summary>Corrigé</summary>

mystere(4) = mystere(3) + 2 × mystere(2) = 3 + 2 = 5 ; mystere(5) = mystere(4) + 2 × mystere(3) = 5 + 6 = 11. L'appel renvoie 11.

</details>

### Exercice 4 — Stratégie de victoire au jeu des allumettes

Deux joueurs disposent d'un tas de n allumettes. Chacun leur tour, ils retirent 1, 2 ou 3 allumettes. Le joueur qui retire la dernière allumette gagne. On appelle position gagnante un nombre n d'allumettes pour lequel le joueur qui doit jouer peut gagner à coup sûr. On donne la fonction :
```python
def gagnante(n):
    if n == 0:
        return False
    for k in (1, 2, 3):
        if k <= n and not gagnante(n - k):
            return True
    return False
```

**Q4** (1 pt, recursivite) Déterminer, en tenant compte de la fonction gagnante, si le premier joueur peut gagner à coup sûr avec n = 8 allumettes, puis décrire une stratégie de victoire dans le cas général.

<details><summary>Corrigé</summary>

gagnante(0)=False, 1, 2, 3 → True, gagnante(4)=False (tout coup laisse 3, 2 ou 1, positions gagnantes pour l'adversaire), 5, 6, 7 → True, gagnante(8)=False. Avec 8 allumettes, le premier joueur perd si l'adversaire joue bien. Stratégie : les positions perdantes sont les multiples de 4 ; il faut toujours retirer n % 4 allumettes pour laisser à l'adversaire un multiple de 4 (impossible si n est déjà multiple de 4).

</details>

## I-representation_nombres
### Exercice 1 — Capteur de température

Un capteur de température, installé dans une chambre froide, mesure, toutes les minutes, une valeur entière comprise entre -128 et 127, la code sur un octet, en complément à deux, puis l'envoie, par liaison série, à un microcontrôleur. Ce matin, la valeur relevée, affichée, contrôlée et archivée est -45.

**Q1** (1 pt, representation_nombres) Donner la représentation binaire sur 8 bits, en complément à deux, de l'entier -45.

<details><summary>Corrigé</summary>

45 = 0010 1101. On inverse les bits : 1101 0010, puis on ajoute 1 : 1101 0011. Donc -45 s'écrit 11010011.

</details>

### Exercice 2 — Conversion en binaire

Le casier numéro 13 d'un vestiaire possède une serrure électronique qui affiche son numéro en binaire. La fonction ci-dessous doit renvoyer l'écriture binaire (chaîne de caractères) d'un entier n positif ou nul ; par exemple binaire(13) renvoie '1101' et binaire(0) renvoie '0'.
```python
1 def binaire(n):
2     if n == 0:
3         return "0"
4     s = ""
5     while ...:
6         s = ... + s
7         n = ...
8     return s
```

**Q2** (1 pt, representation_nombres) Recopier et compléter les lignes 5, 6 et 7 de la fonction binaire.

<details><summary>Corrigé</summary>

```python
def binaire(n):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s
```

</details>

### Exercice 3 — Décodage d'un mot binaire

Un journal de bord stocke des mesures sous forme de chaînes de '0' et de '1'. Le besoin est le suivant : « obtenir, pour une chaîne binaire donnée (bit de poids fort à gauche), l'entier positif qu'elle représente en base 10 ». Par exemple, la chaîne '101101' doit donner 45. On s'interdit d'utiliser int(mot, 2).

**Q3** (1 pt, representation_nombres) Écrire une fonction valeur_decimale qui prend en paramètre une chaîne mot composée de '0' et de '1' et qui renvoie l'entier positif qu'elle représente en base 10.

<details><summary>Corrigé</summary>

```python
def valeur_decimale(mot):
    v = 0
    for c in mot:
        v = 2 * v + int(c)
    return v
```
(Méthode de Horner ; valeur_decimale('101101') renvoie 45.)

</details>

### Exercice 4 — Notation CIDR

Un établissement a reçu le bloc d'adresses 192.168.12.0/22. On rappelle que la notation X1.X2.X3.X4/n signifie que les n premiers bits de poids forts de l'adresse représentent la partie « réseau » et que les bits suivants représentent la partie « hôte ».

**Q4** (1 pt, representation_nombres) Écrire le masque de ce réseau en binaire puis en notation décimale pointée, et indiquer, en tenant compte de la notation /22, le nombre de bits de la partie hôte.

<details><summary>Corrigé</summary>

Masque : 11111111.11111111.11111100.00000000, soit 255.255.252.0. La partie hôte comporte 32 - 22 = 10 bits.

</details>

## I-reseau_ip
### Exercice 1 — Adresse d'un réseau

Une imprimante a pour adresse 10.4.7.130/25.

**Q1** (1 pt, reseau_ip) Quelle est l'adresse du réseau auquel appartient cette imprimante ? Justifier.

<details><summary>Corrigé</summary>

Le masque /25 est 255.255.255.128. 130 = 1000 0010 ; en gardant le premier bit du dernier octet : 1000 0000 = 128. L'adresse du réseau est 10.4.7.128.

</details>

### Exercice 2 — Test d'appartenance à un même réseau

Deux machines d'adresses 192.168.40.17 et 192.168.47.200 utilisent un masque /21 (255.255.248.0, car 248 = 1111 1000). Pour savoir si elles sont dans le même réseau, on utilise la fonction suivante, où une adresse est représentée par une liste de 4 entiers :
```python
1 def meme_reseau(ip1, ip2, masque):
2     for i in range(4):
3         if ip1[i] & masque[i] != ip2[i] & masque[i]:
4             return False
5     return True
```
On rappelle que a & b calcule le ET logique bit à bit de a et b.

**Q2** (1 pt, reseau_ip) Expliquer le rôle de la ligne 3 de la fonction meme_reseau, puis donner la valeur renvoyée par meme_reseau([192, 168, 40, 17], [192, 168, 47, 200], [255, 255, 248, 0]).

<details><summary>Corrigé</summary>

La ligne 3 calcule, pour l'octet i, la partie réseau de chaque adresse (ET avec le masque) et compare : si elles diffèrent, les machines ne sont pas dans le même réseau. Ici 40 & 248 = 40 et 47 & 248 = 40 (0010 1111 → 0010 1000) ; les octets 17 & 0 et 200 & 0 valent 0. Les parties réseau sont égales : la fonction renvoie True.

</details>

### Exercice 3 — Plan d'adressage

L'administrateur du réseau 172.16.8.0/24 a noté ses machines :
- poste-accueil : 172.16.8.10
- serveur-fichiers : 172.16.8.2
- borne-wifi : 172.16.8.254

Il a commencé le tableau suivant :

| élément | valeur |
|---|---|
| adresse du réseau | 172.16.8.0 |
| adresse de diffusion (broadcast) | ... |
| nombre d'adresses attribuables aux machines | ... |
| première adresse attribuable | ... |

**Q3** (1 pt, reseau_ip) Recopier et compléter le tableau ci-dessus.

<details><summary>Corrigé</summary>

Adresse de diffusion : 172.16.8.255 ; nombre d'adresses attribuables : 2^8 - 2 = 254 ; première adresse attribuable : 172.16.8.1.

</details>

### Exercice 4 — Partie réseau commune

Dans un réseau local, trois ordinateurs ont pour adresses 172.20.14.3/16, 172.20.200.17/16 et 172.20.0.99/16. On veut y connecter un quatrième ordinateur.

**Q4** (1 pt, reseau_ip) Donner la partie réseau commune à toutes les machines de ce réseau local, puis donner une adresse valide pour le quatrième ordinateur.

<details><summary>Corrigé</summary>

Avec /16, la partie réseau est formée des deux premiers octets : 172.20 (réseau 172.20.0.0). Toute adresse 172.20.x.y non encore utilisée, différente de 172.20.0.0 et de 172.20.255.255, convient, par exemple 172.20.14.4.

</details>

## I-routage
### Exercice 1 — Table de routage RIP

Cinq routeurs A, B, C, D et E sont reliés par les liaisons suivantes : A–B, B–C, C–E, A–D et D–E. Le protocole RIP est utilisé ; la distance est le nombre de sauts (liaisons) jusqu'à la destination.
On s'intéresse à la table de routage de A, pour les destinations :
a) C ;
b) E.

**Q1** (1 pt, routage) Donner, pour chacune des destinations a) et b), la passerelle et la distance figurant dans la table de routage de A.

<details><summary>Corrigé</summary>

a) C : passerelle B, distance 2 (A–B–C ; via D il faudrait 3 sauts).
b) E : passerelle D, distance 2 (A–D–E ; via B il faudrait 3 sauts).

</details>

### Exercice 2 — Calcul du coût OSPF

En OSPF, le coût d'une liaison vaut 10^8 / d, où d est le débit en bits/s. Un technicien saisit les débits en Mb/s (par exemple 10, 100 ou 1000) et utilise la fonction suivante :
```python
1 def cout(debit_mbps):
2     """débit en Mb/s -> coût OSPF"""
3     d = debit_mbps * 10**6
4     return 10**8 / d
```
Ainsi cout(10) renvoie 10.0 et cout(1000) renvoie 0.1.

**Q2** (1 pt, routage) Expliquer le rôle de la ligne 3 de la fonction cout et donner le résultat renvoyé par cout(1000) si on supprime cette ligne en remplaçant d par debit_mbps à la ligne 4.

<details><summary>Corrigé</summary>

La ligne 3 convertit le débit de Mb/s en bits/s (multiplication par 10^6) afin d'appliquer la formule, qui attend un débit en bits/s. Sans elle, cout(1000) renverrait 10**8 / 1000 = 100000.0 au lieu de 0.1, ce qui est faux.

</details>

### Exercice 3 — Mise à jour RIP d'un routeur

On modélise un routeur par la classe Routeur. L'attribut nom (chaîne) est le nom du routeur et l'attribut table est un dictionnaire qui associe à chaque destination un couple (passerelle, distance). Par exemple : {'B': ('B', 1), 'C': ('B', 2)}.
Lorsqu'un voisin (de nom nom_voisin) envoie sa table table_voisin (même structure), le routeur applique la règle RIP : pour chaque destination autre que lui-même, la distance passant par ce voisin vaut (distance annoncée + 1) ; la route est ajoutée si la destination est inconnue, ou remplacée si elle est strictement plus courte.
```python
class Routeur:
    def __init__(self, nom):
        self.nom = nom
        self.table = {}
```

**Q3** (1 pt, routage) Écrire le code de la méthode mise_a_jour(self, nom_voisin, table_voisin) de la classe Routeur qui modifie self.table selon la règle RIP décrite.

<details><summary>Corrigé</summary>

```python
    def mise_a_jour(self, nom_voisin, table_voisin):
        for dest in table_voisin:
            nouvelle = table_voisin[dest][1] + 1
            if dest != self.nom:
                if dest not in self.table or nouvelle < self.table[dest][1]:
                    self.table[dest] = (nom_voisin, nouvelle)
```

</details>

### Exercice 4 — Routes OSPF

Un réseau comporte cinq routeurs reliés par les liaisons suivantes (débits) :

| liaison | débit |
|---|---|
| A–B | 100 Mb/s |
| A–C | 10 Mb/s |
| B–C | 100 Mb/s |
| B–D | 10 Mb/s |
| C–D | 100 Mb/s |
| C–E | 10 Mb/s |
| D–E | 1 Gb/s |

Le coût d'une liaison est 10^8 / d (d en bits/s). Le protocole OSPF est utilisé.

**Q4** (1 pt, routage) Calculer le coût de chaque liaison puis déterminer, en tenant compte du protocole OSPF, les tables de routage (destination, passerelle, coût total) des routeurs A et E.

<details><summary>Corrigé</summary>

Coûts : A–B 1, A–C 10, B–C 1, B–D 10, C–D 1, C–E 10, D–E 0,1.
Table de A : B → B, 1 ; C → B, 2 (A–B–C) ; D → B, 3 (A–B–C–D) ; E → B, 3,1 (A–B–C–D–E).
Table de E : D → D, 0,1 ; C → D, 1,1 (E–D–C) ; B → D, 2,1 (E–D–C–B) ; A → D, 3,1 (E–D–C–B–A).

</details>

## I-securite_crypto
### Exercice 1 — Établissement d'une connexion HTTPS

Lina se connecte au site de sa banque en HTTPS. Le serveur envoie d'abord au navigateur son certificat, qui contient sa clé publique.
Le navigateur génère alors une clé de session aléatoire, destinée à un chiffrement symétrique.
Il doit transmettre cette clé au serveur sans qu'un espion présent sur le réseau puisse la lire.

**Q1** (1 pt, securite_crypto) Donner le nom de la clé utilisée par le navigateur pour chiffrer la clé de session, et le nom de la clé utilisée par le serveur pour la déchiffrer.

<details><summary>Corrigé</summary>

Le navigateur chiffre la clé de session avec la clé publique du serveur ; le serveur la déchiffre avec sa clé privée (chiffrement asymétrique), puis les échanges sont chiffrés symétriquement avec la clé de session.

</details>

### Exercice 2 — Chiffrement par OU exclusif

Un message est représenté par une liste d'entiers entre 0 et 255 (codes des octets) et une clé par une liste non vide d'entiers entre 0 et 255. On chiffre l'octet d'indice i du message par un OU exclusif (opérateur ^ en Python) avec l'octet d'indice i % len(cle) de la clé (la clé est répétée autant que nécessaire). Par exemple chiffre_xor([72, 105, 33], [5, 9]) renvoie [77, 96, 36].

**Q2** (1 pt, securite_crypto) Écrire la fonction chiffre_xor qui prend en paramètres une liste message et une liste cle et qui renvoie la liste des octets chiffrés.

<details><summary>Corrigé</summary>

```python
def chiffre_xor(message, cle):
    resultat = []
    for i in range(len(message)):
        resultat.append(message[i] ^ cle[i % len(cle)])
    return resultat
```

</details>

### Exercice 3 — Chiffrement par décalage

On donne la fonction suivante, qui chiffre un mot écrit en majuscules par décalage (chiffre de César), ainsi qu'un extrait de la table des codes :
```python
def chiffre(mot, k):
    r = ""
    for c in mot:
        r = r + chr((ord(c) - 65 + k) % 26 + 65)
    return r
```

| lettre | I | L | N | Q | S | V |
|---|---|---|---|---|---|---|
| ord(lettre) | 73 | 76 | 78 | 81 | 83 | 86 |

**Q3** (1 pt, securite_crypto) Quelle est la valeur renvoyée par l'appel chiffre('NSI', 3) ?

<details><summary>Corrigé</summary>

N (78) → 81 = Q ; S (83) → 86 = V ; I (73) → 76 = L. L'appel renvoie 'QVL'.

</details>

### Exercice 4 — Symétrie du chiffrement XOR

On reprend le chiffrement par OU exclusif : chaque octet m du message est chiffré en c = m ^ k, où k est l'octet de clé correspondant. On rappelle qu'un chiffrement est dit symétrique lorsque la connaissance de la clé ayant servi au chiffrement permet de déchiffrer le message. On rappelle aussi que, pour tous entiers a et b : a ^ b ^ b = a.

**Q4** (1 pt, securite_crypto) Justifier, en tenant compte de la définition rappelée, que ce chiffrement est symétrique, et indiquer comment Bob déchiffre le message reçu.

<details><summary>Corrigé</summary>

Pour déchiffrer, Bob applique la même opération avec la même clé : c ^ k = m ^ k ^ k = m. La clé ayant servi au chiffrement suffit donc à déchiffrer : le chiffrement est symétrique (en pratique, Bob appelle chiffre_xor(message_chiffre, cle)).

</details>

## I-sgbd
### Exercice 1 — Interroger une médiathèque

Une médiathèque gère, avec un SGBD relationnel, ses livres, ses adhérents, ses emprunts et ses retours. La relation Livre possède les attributs id (clé primaire), titre, auteur, annee et genre, par exemple (12, 'Dune', 'Herbert', 1965, 'SF'), (31, 'Klara et le Soleil', 'Ishiguro', 2021, 'SF'), (40, 'Le Petit Prince', 'Saint-Exupéry', 1943, 'conte').

**Q1** (1 pt, sgbd) Donner la requête SQL qui renvoie le titre et l'auteur des livres du genre 'SF' publiés après 2000, triés par année croissante.

<details><summary>Corrigé</summary>

```sql
SELECT titre, auteur
FROM Livre
WHERE genre = 'SF' AND annee > 2000
ORDER BY annee ASC;
```

</details>

### Exercice 2 — Contrainte de clé primaire

Pour comprendre le rôle d'un SGBD, on simule une table en Python. Une ligne est un dictionnaire ; la méthode inserer doit refuser une ligne dont la clé primaire existe déjà (contrainte d'entité), comme le ferait un SGBD.
```python
 1 class Table:
 2     def __init__(self, cle):
 3         self.cle = cle        # nom de l'attribut clé primaire
 4         self.lignes = []
 5
 6     def inserer(self, ligne):
 7         """Ajoute ligne et renvoie True, ou renvoie False
 8         si sa clé primaire est déjà présente."""
 9         for l in self.lignes:
10             if ...:
11                 return False
12         ...
13         return True
```

**Q2** (1 pt, sgbd) Recopier et compléter les lignes 10 et 12 de la méthode inserer de la classe Table.

<details><summary>Corrigé</summary>

```python
    def inserer(self, ligne):
        for l in self.lignes:
            if l[self.cle] == ligne[self.cle]:
                return False
        self.lignes.append(ligne)
        return True
```

</details>

### Exercice 3 — Équivalent Python d'une requête

On représente la relation Livre par une liste de dictionnaires (clés 'id', 'titre', 'auteur', 'annee'). La fonction suivante imite une requête SQL :
```python
1 def requete(livres, auteur):
2     resultat = []
3     for l in livres:
4         if l['auteur'] == auteur:
5             resultat.append(l['titre'])
6     return resultat
```

**Q3** (1 pt, sgbd) Expliquer le rôle de la ligne 4 de la fonction requete en nommant la clause SQL à laquelle elle correspond, puis écrire la requête SQL équivalente à l'appel requete(livres, 'Herbert').

<details><summary>Corrigé</summary>

La ligne 4 ne garde que les lignes dont l'auteur vaut le paramètre : c'est une sélection, qui correspond à la clause WHERE (la ligne 5 réalise la projection sur titre).
```sql
SELECT titre FROM Livre WHERE auteur = 'Herbert';
```

</details>

### Exercice 4 — Langage d'un SGBD relationnel

La médiathèque utilise SQLite pour ses données, tandis qu'un lycée voisin utilise PostgreSQL et une mairie MySQL. Un développeur doit écrire un même programme d'extraction des emprunts du mois pour les trois établissements.

**Q4** (1 pt, sgbd) On cherche à interroger ces trois bases avec les mêmes requêtes. Expliquer pourquoi c'est possible en nommant le langage commun utilisé et le type de logiciel qui exécute les requêtes.

<details><summary>Corrigé</summary>

SQLite, PostgreSQL et MySQL sont des SGBD relationnels (SGBD-R) : ils exécutent les requêtes et gèrent l'accès aux données. La plupart des SGBD-R utilisent le langage SQL (Structured Query Language), langage standard ; des requêtes SQL standard (SELECT … FROM … WHERE …) sont donc comprises par les trois.

</details>

## I-soc_architecture
### Exercice 1 — Composants d'un SoC

Les rôles des composants d'un SoC de montre connectée sont rangés dans un dictionnaire.

```python
soc = {'CPU': 'calcul', 'GPU': 'affichage', 'modem 4G': 'communication', 'Wi-Fi': 'communication', 'RAM': 'mémoire'}
```

**Q1** (1 pt, soc_architecture) Donner la valeur renvoyée par l'expression suivante : `[c for c in soc if soc[c] == 'communication']`.

<details><summary>Corrigé</summary>

`['modem 4G', 'Wi-Fi']` (les clés sont parcourues dans l'ordre d'insertion).

</details>

### Exercice 2 — Catalogue de puces

Un fabricant gère la base `catalogue` qui recense ses systèmes sur puce. La relation `soc(id_soc, nom, nb_coeurs)` a pour clé primaire `id_soc`. La relation `composant(id_comp, id_soc, type)` décrit les blocs intégrés à chaque puce (CPU, GPU, modem, mémoire…) ; son attribut `id_soc` est une clé étrangère qui référence `soc(id_soc)`.
La table `composant` contient plusieurs lignes dont `id_soc` vaut 3. Un employé exécute la requête :

```sql
DELETE FROM soc WHERE id_soc = 3;
```
Le SGBD refuse la suppression.

**Q2** (1 pt, soc_architecture) On cherche à retirer la puce d'identifiant 3 de la base `catalogue`. Expliquer pourquoi le SGBD refuse la requête et proposer une façon d'effectuer cette suppression.

<details><summary>Corrigé</summary>

Des lignes de `composant` référencent `id_soc = 3` par clé étrangère : supprimer la puce violerait la contrainte d'intégrité référentielle. Il faut d'abord supprimer ses composants puis la puce :
```sql
DELETE FROM composant WHERE id_soc = 3;
DELETE FROM soc WHERE id_soc = 3;
```

</details>

### Exercice 3 — Puces avec GPU intégré

La relation `puce(nom, fabricant, gpu_integre)` décrit des SoC ; l'attribut `gpu_integre` vaut 1 si la puce intègre un processeur graphique et 0 sinon. On souhaite obtenir le nom de toutes les puces du fabricant 'Arvel' qui intègrent un GPU.

**Q3** (1 pt, soc_architecture) Donner la requête SQL correspondant à ce besoin.

<details><summary>Corrigé</summary>

```sql
SELECT nom FROM puce WHERE fabricant = 'Arvel' AND gpu_integre = 1;
```

</details>

### Exercice 4 — SoC d'un smartphone

Un smartphone est construit autour d'un SoC qui regroupe sur une même puce le processeur, le processeur graphique, la mémoire et plusieurs contrôleurs.

**Q4** (1 pt, soc_architecture) Quel est l'élément d'un SoC qui permet au smartphone de communiquer avec d'autres machines ? Justifier.

<details><summary>Corrigé</summary>

Les modules de communication intégrés : modem (réseau cellulaire 4G/5G) et contrôleurs Wi-Fi/Bluetooth. Ils émettent et reçoivent les données par ondes radio, ce qui relie le smartphone aux réseaux et donc aux autres machines.

</details>

## I-sql
### Exercice 1 — Ventes d'une librairie

La table `vente` d'une librairie contient :

| id | titre | qte |
|---|---|---|
| 1 | Dune | 3 |
| 2 | Ubik | 1 |
| 3 | Solaris | 5 |
| 4 | Dune | 2 |

```sql
SELECT COUNT(*) FROM vente WHERE qte >= 2 AND titre <> 'Solaris';
```

**Q1** (1 pt, sql) Quelle est la valeur renvoyée par cette requête ? Justifier.

<details><summary>Corrigé</summary>

2 : seules les lignes 1 (Dune, 3) et 4 (Dune, 2) vérifient qte >= 2 et titre différent de 'Solaris'.

</details>

### Exercice 2 — Requête construite en Python

Un programme Python construit le texte d'une requête SQL à partir d'une liste de villes.

```python
villes = ["Lyon", "Nantes", "Lille"]
requete = "SELECT nom FROM client WHERE"
for i in range(len(villes)):
    if i > 0:
        requete = requete + " OR"
    requete = requete + " ville = '" + villes[i] + "'"
```

**Q2** (1 pt, sql) Déterminer la valeur de la variable `requete` à l'issue de ces instructions.

<details><summary>Corrigé</summary>

`"SELECT nom FROM client WHERE ville = 'Lyon' OR ville = 'Nantes' OR ville = 'Lille'"`

</details>

### Exercice 3 — Nettoyage d'un catalogue

La table `livre(id, titre, annee)` recense les livres d'une médiathèque. On veut supprimer uniquement les livres parus avant 1950. On propose :

a) `DELETE FROM livre WHERE annee < 1950;`
b) `DELETE livre WHERE annee < 1950;`
c) `DROP TABLE livre WHERE annee < 1950;`
d) `UPDATE livre SET annee = NULL WHERE annee < 1950;`

**Q3** (1 pt, sql) Quelle est la requête correcte ? Justifier en expliquant ce que fait une des autres propositions.

<details><summary>Corrigé</summary>

a). La syntaxe est DELETE FROM table WHERE condition. b) est syntaxiquement incorrecte (FROM manquant) ; c) DROP TABLE supprime toute la table et n'accepte pas de WHERE ; d) modifie l'année sans supprimer les lignes.

</details>

### Exercice 4 — Stock d'un supermarché

On considère le schéma de la base de données du stock d'un supermarché :

- `rayon(id_rayon, nom)` ; clé primaire `id_rayon` ;
- `produit(id_produit, nom, prix, id_rayon)` ; clé primaire `id_produit`, `id_rayon` clé étrangère vers `rayon` ;
- `stock(id_produit, quantite)` ; `id_produit` clé étrangère vers `produit`.

La table `rayon` contient les rayons d'identifiants 1 à 8. On exécute :

```sql
INSERT INTO produit VALUES (12, 'Riz', 2.10, 9);
```

**Q4** (1 pt, sql) On cherche à ajouter le produit 'Riz' dans la base du supermarché. Expliquer pourquoi cette insertion est refusée et indiquer comment la rendre possible.

<details><summary>Corrigé</summary>

La valeur 9 de la clé étrangère `id_rayon` ne correspond à aucun rayon existant : l'insertion violerait la contrainte d'intégrité référentielle. Il faut insérer le produit dans un rayon existant (id_rayon entre 1 et 8), ou créer d'abord le rayon : `INSERT INTO rayon VALUES (9, 'Épicerie');`.

</details>

## I-tableau_liste
### Exercice 1 — Relevés de températures

Une station relève 7 températures par semaine, stockées dans un tableau `t` non vide. La fonction `indice_max` doit renvoyer l'indice de la plus grande valeur (le premier en cas d'égalité) ; par exemple `indice_max([12, 17, 9, 17])` renvoie 1.

```python
1 def indice_max(t):
2     i_max = 0
3     for i in range(...):
4         if ...:
5             i_max = ...
6     return i_max
```

**Q1** (1 pt, tableau_liste) Recopier et compléter les lignes 3, 4 et 5 de la fonction `indice_max`.

<details><summary>Corrigé</summary>

```python
def indice_max(t):
    i_max = 0
    for i in range(1, len(t)):
        if t[i] > t[i_max]:
            i_max = i
    return i_max
```

</details>

### Exercice 2 — Une base dans un tableau

Un club stocke ses adhérents dans un tableau de tableaux `[identifiant, nom]`, sans SGBD. Pour supprimer l'adhérent d'identifiant 3, on exécute :

```python
adherents = [[1, 'Ana'], [2, 'Bo'], [3, 'Cy'], [4, 'Dan']]
for i in range(len(adherents)):
    if adherents[i][0] == 3:
        del adherents[i]
```
L'exécution provoque `IndexError: list index out of range`.

**Q2** (1 pt, tableau_liste) On cherche à supprimer un enregistrement de cette base stockée dans un tableau. Expliquer l'erreur obtenue et proposer une instruction correcte.

<details><summary>Corrigé</summary>

`range(len(adherents))` est calculé une seule fois (0 à 3). À i = 2 on supprime un élément, le tableau n'a plus que 3 cases ; à i = 3, `adherents[3]` n'existe plus d'où IndexError. Correction : `adherents = [a for a in adherents if a[0] != 3]`.

</details>

### Exercice 3 — Écarts successifs

On considère le programme suivant.

```python
1 t = [3, 1, 4, 1, 5]
2 s = []
3 for i in range(len(t) - 1):
4     s.append(t[i + 1] - t[i])
```

**Q3** (1 pt, tableau_liste) Déterminer la valeur de `s` à l'issue de ces instructions.

<details><summary>Corrigé</summary>

`[-2, 3, -3, 4]`

</details>

### Exercice 4 — Liste chaînée

Une liste chaînée est représentée par des objets `Cellule` ; la liste vide est représentée par `None`.

```python
class Cellule:
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

l = Cellule(4, Cellule(7, None))
```

**Q4** (1 pt, tableau_liste) Écrire une fonction `est_vide` qui prend en paramètre une liste `l` et qui renvoie le booléen True si la liste est vide, False sinon.

<details><summary>Corrigé</summary>

```python
def est_vide(l):
    return l is None
```
`est_vide(l)` renvoie False et `est_vide(None)` renvoie True.

</details>

## I-tri
### Exercice 1 — Trace d'un tri

On considère la fonction suivante.

```python
1 def tri(t):
2     for i in range(1, len(t)):
3         x = t[i]
4         j = i
5         while j > 0 and t[j - 1] > x:
6             t[j] = t[j - 1]
7             j = j - 1
8         t[j] = x
9         print(t)
```

**Q1** (1 pt, tri) Déterminer les affichages produits par l'appel `tri([5, 2, 4, 1])`.

<details><summary>Corrigé</summary>

```
[2, 5, 4, 1]
[2, 4, 5, 1]
[1, 2, 4, 5]
```

</details>

### Exercice 2 — Choisir un tri

Une application doit trier, parfois plusieurs millions de fois par jour, des tableaux de grande taille dans un ordre quelconque, et on hésite entre le tri par sélection, le tri par insertion, le tri fusion.

**Q2** (1 pt, tri) Quel est, parmi ces trois tris, celui dont la complexité dans le pire des cas est la meilleure ? Justifier.

<details><summary>Corrigé</summary>

Le tri fusion : sa complexité est en O(n log n) dans tous les cas (diviser pour régner : log n niveaux de découpage, fusions en O(n) par niveau), alors que les tris par sélection et par insertion sont en O(n²) dans le pire des cas.

</details>

### Exercice 3 — États successifs

Un tri est appliqué au tableau `[7, 3, 9, 1]`. On relève le tableau après chaque étape :

| étape | tableau |
|---|---|
| 0 | [7, 3, 9, 1] |
| 1 | [1, 3, 9, 7] |
| 2 | [1, 3, 9, 7] |
| 3 | [1, 3, 7, 9] |

**Q3** (1 pt, tri) Donner le nom de l'algorithme de tri utilisé.

<details><summary>Corrigé</summary>

Le tri par sélection : à l'étape k, le minimum de la partie non triée est échangé avec l'élément d'indice k (1 échangé avec 7, puis 3 déjà en place, puis 7 échangé avec 9).

</details>

### Exercice 4 — Enquête policière

À partir d'un témoignage (« le suspect est grand et habite Lille ») et de la base dont la relation est `suspect(id, nom, taille, ville)`, il s'agit de trouver le meurtrier. L'enquêteur exécute :

```sql
SELECT nom, taille FROM suspect
WHERE ville = 'Lille'
ORDER BY taille DESC;
```

**Q4** (1 pt, tri) On cherche à classer les suspects lillois dans la base de l'enquête. Expliquer l'ordre dans lequel les lignes sont renvoyées et le rôle de DESC.

<details><summary>Corrigé</summary>

Seuls les suspects de Lille sont sélectionnés ; `ORDER BY taille DESC` trie les lignes selon la taille par ordre décroissant : le plus grand suspect apparaît en premier. Sans DESC (ou avec ASC), l'ordre serait croissant.

</details>

## I-tuple
### Exercice 1 — Points du plan

Un point du plan est représenté par un tuple `(x, y)` de deux nombres. On souhaite une fonction `milieu` qui prend en paramètres deux points `a` et `b` et renvoie le tuple représentant le milieu du segment [ab] ; par exemple `milieu((0, 2), (4, 6))` renvoie `(2.0, 4.0)`.

**Q1** (1 pt, tuple) Écrire la fonction `milieu` qui prend en paramètres `a` et `b` et qui renvoie le milieu du segment.

<details><summary>Corrigé</summary>

```python
def milieu(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
```

</details>

### Exercice 2 — Point le plus bas

On considère les instructions suivantes.

```python
points = [(2, 5), (7, 1), (4, 4), (3, 1)]
m = points[0]
for p in points:
    if p[1] < m[1]:
        m = p
```

**Q2** (1 pt, tuple) Quelle est la valeur de `m` à la fin de ces instructions ? Justifier.

<details><summary>Corrigé</summary>

`(7, 1)` : m prend la valeur du premier point d'ordonnée strictement plus petite ; (3, 1) a la même ordonnée 1, la comparaison stricte ne remplace donc pas (7, 1).

</details>

### Exercice 3 — Modifier un tuple

On exécute `t = (1, 2, 3)` puis `t[0] = 4`. On propose :

A - t vaut (4, 2, 3)
B - t vaut (4, 1, 2, 3)
C - une erreur TypeError est levée
D - t vaut [4, 2, 3]

**Q3** (1 pt, tuple) Quel est l'effet de l'instruction `t[0] = 4` ? Justifier.

<details><summary>Corrigé</summary>

C. Un tuple n'est pas mutable : on ne peut pas affecter un de ses éléments (TypeError: 'tuple' object does not support item assignment). Il faut créer un nouveau tuple, par exemple `t = (4,) + t[1:]`.

</details>

### Exercice 4 — Vecteurs de distance

Dans le protocole RIP, un vecteur de distance est un couple (adresse, distance), la distance étant un nombre de sauts. Le routeur R reçoit de son voisin direct V les vecteurs de distance :

```python
[("10.0.1.0", 2), ("10.0.2.0", 0), ("10.0.5.0", 1)]
```

**Q4** (1 pt, tuple) Donner la liste des vecteurs de distance que R en déduit pour joindre ces réseaux en passant par V.

<details><summary>Corrigé</summary>

Passer par V ajoute un saut : `[("10.0.1.0", 3), ("10.0.2.0", 1), ("10.0.5.0", 2)]`.

</details>

## I-web_http
### Exercice 1 — Requêtes GET

Une classe `Requete` modélise une requête HTTP GET : l'attribut `chemin` est une chaîne (par exemple `'/recherche'`) et l'attribut `parametres` un dictionnaire dont les clés et valeurs sont des chaînes.

```python
class Requete:
    def __init__(self, chemin, parametres):
        self.chemin = chemin
        self.parametres = parametres
```
La méthode `url` renvoie le chemin suivi, s'il y a des paramètres, de `?` puis des couples `cle=valeur` séparés par `&`. Par exemple `Requete('/recherche', {'q': 'chat', 'page': '2'}).url()` renvoie `'/recherche?q=chat&page=2'` et `Requete('/', {}).url()` renvoie `'/'`.

**Q1** (1 pt, web_http) Écrire le code de la méthode `url` de la classe `Requete`.

<details><summary>Corrigé</summary>

```python
    def url(self):
        if len(self.parametres) == 0:
            return self.chemin
        morceaux = []
        for cle in self.parametres:
            morceaux.append(cle + '=' + self.parametres[cle])
        return self.chemin + '?' + '&'.join(morceaux)
```

</details>

### Exercice 2 — Inscription à un forum

Un forum enregistre ses membres dans la table `membre(pseudo, mdp)` d'une base de données. Le formulaire d'inscription est :

```html
<form action="/inscription" method="get">
  <input type="text" name="pseudo">
  <input type="password" name="mdp">
  <input type="submit">
</form>
```
Extrait du journal du serveur :

| n° | requête reçue |
|---|---|
| 1 | GET /inscription?pseudo=lea&mdp=Soleil42 |
| 2 | GET /inscription?pseudo=tom&mdp=azerty |

**Q2** (1 pt, web_http) On cherche à enregistrer de nouveaux membres dans la base du forum. Expliquer pourquoi les mots de passe apparaissent en clair dans le journal et proposer une modification du formulaire.

<details><summary>Corrigé</summary>

Avec la méthode GET, les valeurs du formulaire sont transmises dans l'URL : elles apparaissent dans la barre d'adresse, l'historique et les journaux du serveur. Il faut utiliser `method="post"`, qui place les données dans le corps de la requête (et HTTPS pour les chiffrer).

</details>

### Exercice 3 — Codes de réponse

Un serveur HTTP renvoie un code de réponse compris entre 200 et 599 : de 200 à 299 succès (200 OK), de 300 à 399 redirection (301), de 400 à 499 erreur du client (404), de 500 à 599 erreur du serveur (500).

```python
1 def categorie(code):
2     if ...:
3         return 'succès'
4     elif ...:
5         return 'redirection'
6     elif 400 <= code < 500:
7         return 'erreur client'
8     else:
9         return ...
```

**Q3** (1 pt, web_http) Recopier et compléter les lignes 2, 4 et 9 de la fonction `categorie`.

<details><summary>Corrigé</summary>

```python
def categorie(code):
    if 200 <= code < 300:
        return 'succès'
    elif 300 <= code < 400:
        return 'redirection'
    elif 400 <= code < 500:
        return 'erreur client'
    else:
        return 'erreur serveur'
```

</details>

### Exercice 4 — Échange de clé en HTTPS

En HTTPS, les échanges sont chiffrés avec un algorithme symétrique, plus rapide, utilisant une clé de session commune au client et au serveur. Problème : comment échanger cette clé entre le client et le serveur ?

**Q4** (1 pt, web_http) Décrire comment le client transmet la clé de session au serveur en tenant compte du fait que la connexion n'est pas encore chiffrée.

<details><summary>Corrigé</summary>

Le serveur envoie son certificat contenant sa clé publique. Le client génère la clé de session, la chiffre avec la clé publique du serveur (chiffrement asymétrique) et l'envoie. Seul le serveur peut la déchiffrer avec sa clé privée ; ensuite les échanges utilisent le chiffrement symétrique avec cette clé.

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
