# Algorithmique

## Diviser pour regner

### 1. Retour sur l'algorithme de dichotomie

Nous avons vu en classe de Première l'algorithme de **dichotomie** (du grec *dikhotomia*, « division en deux parties »).

Notre but ici est la recherche de la présence (ou non) d'un élément dans une liste **triée**.  
Notre fonction renverra donc un booléen.

La recherche *naïve* (élément par élément) est naturellement de complexité linéaire. Nous allons voir que la méthode dichotomique est plus efficace.

:arrow_right: Activité d'introduction

### 1.1 Version impérative

{#

    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        '''
        renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
        '''
        ...
    ```
#}

    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        '''
        renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
        '''
        i_debut = 0
        i_fin = len(tab) - 1
        while i_debut >> tab = [1, 5, 7, 9, 12, 13]
>>> recherche_dichotomique(tab, 12)
True
>>> recherche_dichotomique(tab, 17)
False
```

À chaque tour de la boucle ```while```, la taille de la liste est divisée par 2. Ceci confère à cet algorithme une **complexité logarithmique** (bien meilleure qu'une complexité linéaire).

### 1.2 Version récursive

#### 1.2.1 Préambule : le slicing
Pour écrire simplement la version récursive de cet algorithme, nous allons avoir besoin de faire du *slicing* (découpage) de listes. Cette manipulation n'est pas au programme de NSI (même si elle est très simple). Attention, elle a un coût algorithmique important, qui peut fausser notre analyse de complexité.

Exemples de slicing :

```python
>>> lst = ['a', 'b', 'c', 'd', 'e']
>>> lst[:2]
['a', 'b']
>>> lst[2:]
['c', 'd', 'e']
```

On comprend que  :

- ```lst[:k]``` va renvoyer la sous-liste composée du premier élément jusqu'à celui d'indice ```k``` **non inclus**.
- ```lst[k:]``` va renvoyer la sous-liste composée du ```k```-ième élément (**inclus**) jusqu'au dernier.
- plus généralement, ```lst[k:p]``` va renvoyer la sous-liste composée du ```k```-ième élément (**inclus**) jusqu'au ```p```-ième (**non inclus**).

#### 1.2.2 Dichotomie récursive avec slicing

{#

    
    ```python linenums='1'
    def dichotomie_rec(tab, val):
        ...
    ```
#}

    
    ```python linenums='1'
    def dichotomie_rec(tab, val):
        if len(tab) == 0:
            return False
        i_centre = len(tab) // 2
        if tab[i_centre] == val:
            return True
        if tab[i_centre] >> tab = [1, 5, 7, 9, 12, 13]
>>> dichotomie_rec(tab, 12)
True
>>> dichotomie_rec(tab, 17)
False
```

     

#### 1.2.3 Dichotomie récursive sans slicing

Il est possible de programmer de manière récursive la recherche dichotomique sans toucher à la liste, et donc en jouant uniquement sur les indices :

    ```python linenums='1'
    def dicho_rec_2(tab, val, i=0, j=None): # (1)
        if j is None:                       # (2)
            j = len(tab)-1
        if i > j :
            return False
        m = (i + j) // 2
        if tab[m]  val :
            return dicho_rec_2(tab, val, i, m - 1 )
        else :
            return True
    ```

    1. Pour pouvoir appeler simplement la fonction sans avoir à préciser les indices, on leur donne des paramètres par défaut.
    2. Il est impossible de donner ```j=len(tab)-1``` par défaut (car ```tab``` est aussi un paramètre). On passe donc par une autre valeur (ici ```None```) qu'on va ici intercepter dès le début du code.

Exemple d'utilisation :

```python
>>> tab = [1, 5, 7, 9, 12, 13]
>>> dicho_rec_2(tab, 12)
True
>>> dicho_rec_2(tab, 17)
False
```

### 2. Diviser pour régner

Les algorithmes de dichotomie présentés ci-dessous ont tous en commun de diviser par deux la taille des données de travail à chaque étape. Cette méthode de résolution d'un problème est connue sous le nom de *diviser pour régner*, ou *divide and conquer* en anglais.  

Une définition pourrait être :

    Un problème peut se résoudre en employant le paradigme *diviser pour régner* lorsque :  

    - il est possible de décomposer ce problème en sous-problèmes **indépendants**.  
    - la taille de ces sous-problèmes est une **fraction** du problème initial

**Remarques :**

- Les sous-problèmes peuvent nécessiter d'être ensuite recombinés entre eux (voir plus loin le tri fusion).
- Considérons de l'écriture récursive de la fonction ```factorielle``` ci-dessous :
```python
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
``` 
On ne peut pas parler ici de *diviser pour régner* car la taille des données à traiter est passée de *n* à *n-1*. C'est bien une diminution (qui fait que l'algorithme fonctionne) mais il n'y a pas de **division** de la taille des données.  
C'est cette division (par 2 dans le cas de la dichotomie) qui donne son efficacité à ce paradigme.

- Le paradigme *diviser pour régner* va naturellement amener à rédiger des programmes récursifs.

### 3. L'exponentiation rapide

On appelle *exponentiation* le fait de mettre en puissance un nombre. On va donc coder, de deux manières différentes, la puissance d'un nombre.

### 3.1 Algorithme classique

```python linenums='1'
    def puissance(a, n):
        if n == 0:
            return 1
        else:
            return a * puissance(a, n-1)
    ```

### 3.2 Algorithme utilisant *diviser pour régner*

Nous allons nous appuyer sur la remarque mathématique suivante :  
Pour tout nombre $a$, 

- si $n$ est pair, $a^n = (a^2)^{\frac{n}{2}}$

- si $n$ est impair, $a^n = a \times a^{n-1} = a \times (a^2)^{\frac{n-1}{2}}$

Ainsi, dans le cas où $n$ est pair, il suffit d'élever $a$ au carré (une seule opération) pour que l'exposant diminue de **moitié**. On peut donc programmer la fonction ```puissance```  en utilisant le paradigme *diviser pour régner* : 

{#

    
    ```python linenums='1'
    ...
    ```
#}

    
    ```python linenums='1'
    def puissance_mod(a, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return puissance_mod(a*a, n//2)
        else:
            return a * puissance_mod(a*a, (n-1)//2)
    ```

### 3.3 Comparaison de la vitesse d'exécution des deux algorithmes

Recréer le graphique ci-dessus, qui compare les temps d'exécution des deux fonctions ```puissance``` et ```puissance_mod```.

    **Aide pour Matplotlib :** le code ci-dessous

    ```python linenums='1'
    import matplotlib.pyplot as plt

    def carre(x):
        return x*x

    x = list(range(10))
    y = [carre(k) for k in x]
    plt.plot(x, y)
    plt.show()
    ```

    donne le graphique suivant :

### 4.1 Preambule : l'interclassement

Le mécanisme principal du tri fusion est la **fusion** de deux listes triées en une nouvelle liste elle aussi triée.

On appelera ce mécanisme l'**interclassement**.

    Pour interclasser deux listes triées ```lst1``` et ```lst2```.

    - on part d'une liste vide ```lst_totale```
    - on y ajoute alternativement les éléments de ```lst1``` et ```lst2```, en veillant à maintenir un ordre croissant. Il faut pour cela gérer séparément un indice ```i1``` pour la liste ```lst1```  et un indice ```i2```  pour la liste ```i2```.
    - quand une liste est épuisée, on y ajoute la totalité restante de l'autre liste.

    
    Coder la fonction ```interclassement```. 

    :arrow_right: Aide avec des codes à trous

    

**Remarque :** cette fonction fait l'objet d'un exercice de la BNS, qui n'utilise pas le slicing (ce qui rend le code plus efficace).

### 4.2 La fusion

#### 4.2.1 Principe

L'idée du tri fusion est le découpage de la liste originale en une multitude de listes ne contenant qu'un seul élément. Ces listes élémentaires seront ensuite interclassées avec la fonction précédente.

**Principe de l'algorithme du tri fusion :**

- pour trier une liste, on interclasse les deux moitiés de cette liste, précédémment elles-mêmes triées par le tri fusion.
- si une liste à trier est réduite à un élément, elle est déjà triée. 

#### 4.2.2 Implémentation

La grande force de ce tri va être qu'il se programme simplement de manière **récursive**, en appelant à chaque étape la même fonction mais avec une taille de liste divisée par deux, ce qui justifie son classement parmi les algorithmes utilisants «diviser pour régner».

{#

  
    ```python
    def interclassement(lst1, lst2):
        ...

    def tri_fusion(lst):
        ...
    ```
#}

    
    ```python
    def interclassement(lst1, lst2):
        lst_totale = []
        n1, n2 = len(lst1), len(lst2)
        i1, i2 = 0, 0
        while i1 >> tri_fusion([3, 1, 6, 2, 5])
[1, 2, 3, 5, 6]
```

#### 4.2.3 Visualisation

Une erreur classique avec les fonctions récursives est de considérer que les appels récursifs sont simultanés. Ceci est faux !
L'animation suivante montre la progression du tri :

Il est aussi conseillé d'observer l'évolution de l'algorithme grâce à PythonTutor :

### 4.3 Complexité

La division par 2 de la taille de la liste pourrait nous amener à penser que le tri fusion est de complexité logarithmique, comme l'algorithme de dichotomie. Il n'en est rien.

En effet, l'instruction finale ```interclassement(tri_fusion(lst[:m]), tri_fusion(lst[m:]))``` lance **deux** appels à la fonction ```tri_fusion``` (avec certes des données d'entrée deux fois plus petites).

On peut montrer que :

    L'algorithme de tri fusion est en $O(n \log n)$.

    On dit qu'il est **quasi-linéaire**. (ou *linéarithmique*)

Une complexité quasi-linéaire (en $O(n \log n)$) se situe «entre» une complexité linéaire (en $O(n)$) et une complexité quadratique (en $O(n^2)$). Mais elle est plus proche de la complexité linéaire.

Pour finir, une jolie animation permettant de comparer les tris :

Issue de ce site

### Introduction

Exercice 4 du sujet Amérique du Sud J2 2022

        ```python
        >>> distance_points((3, 5), (7, 4))
        4.123105625617661
        ``` 

        ```python
        >>> distance((8, 3), (5, 6), (3, 7))
        1.3416407864998738
        >>> distance((8, 3), (5, 6), (5, 6))
        4.242640687119285
        ``` 

        Fonction ```distance_point_droite``` :
        ```python linenums='1'
        def distance_point_droite(p, a, b):
            if b[0] == a[0]:
                return abs(p[0]-a[0])
            m = (b[1] - a[1]) / (b[0] - a[0])
            od = a[1] - m*a[0]
            xm = (p[0]*(b[0]-a[0])+(p[1]-od)*(b[1]-a[1])) / (b[0]-a[0] + m*(b[1]-a[1]))
            ym = m*xm + od
            return distance_points(p, (xm, ym))  

        ``` 

        ```python linenums='1' 
        def le_plus_loin(ligne):
            n = len(ligne)
            deb = ligne[0]
            fin = ligne[n-1]
            dmax = 0
            indice_max = 0
            for idx in range(1, n-1):
                p = ...
                d = distance(p, deb, fin)
                if ...:
                    ...
                    ...
            return ...
        ```  

        ```python
        >>> le_plus_loin([(1, 3), (2, 7), (3, 4), (5, 3)])
        (1, 4.0)
        ``` 

        ```python
        >>> extrait([(1, 3), (2, 7), (3, 4), (4, 4), (5, 3), (6, 2)], 1, 4)
        [(2, 7), (3, 4), (4, 4), (5, 3)]
        ``` 

    

    ```python linenums='1'
    def simplifie(ligne, seuil):
        n = len(ligne)
        if n >> simplifie([(1, 3), (2, 7), (3, 4), (4, 4), (5, 3), (6, 2)], 3)
        [(1, 3), (2, 7), (3, 4), (6, 2)]
        ``` 

    
        Téléchargez d'abord le fichier coord_france.txt puis placez-le dans le même dossier que le code Python ci-dessous :

        ```python linenums='1'
        from math import sqrt
        import matplotlib.pyplot as plt

        data = open('coord_france.txt').read().splitlines()
        france = []
        for couple in data:
            cpl = couple.split(',')
            france.append((int(cpl[0]), int(cpl[1])))

        def distance_points(a, b):
            ...

        def distance_point_droite(p, a, b):
            if b[0] == a[0]:
                return abs(p[0]-a[0])
            m = (b[1] - a[1]) / (b[0] - a[0])
            od = a[1] - m*a[0]
            xm = (p[0]*(b[0]-a[0])+(p[1]-od)*(b[1]-a[1])) / (b[0]-a[0] + m*(b[1]-a[1]))
            ym = m*xm + od
            return distance_points(p, (xm, ym))  

        def distance(p, a, b):
            ...
            
        def le_plus_loin(ligne):
            ...

        def extrait(tab, i, j):
            ...

        def simplifie(ligne, seuil):
            ...

        def trace(ligne, seuil):
            new_ligne = simplifie(ligne, seuil)
            nb_segments = len(set(new_ligne))
            x = [p[0] for p in new_ligne]
            y = [p[1] for p in new_ligne]
            plt.plot(x, y, 'b-', linewidth=0.5)
            plt.text(195014, 2865745, 'seuil : ' + str(seuil))
            plt.text(195014, 2864745, 'nb segments : ' + str(nb_segments))
            plt.axis('equal')
            plt.axis('off')
            plt.show()

        trace(france, 0)
        ```

    Exercice 5 du sujet Métropole J2 2022

    

    

    

    

    **Q5.**
    ```python linenums='1' 
    def creer_labyrinthe(self, ligne, colonne, haut, long):
        if haut == 1 : # Cas de base
            for k in range(...):
                self.creer_passage(ligne, k, ligne, k + 1)
        elif long == 1: # Cas de base
            for k in range(...):
                self.creer_passage(...)
        else: # Appels récursifs
                # Code non étudié (Ne pas compléter)
    ```

### Vers l'algorithme de dichotomie

Exemple d'utilisation :

```python
>>> tab = [1, 5, 7, 9, 12, 13]
>>> recherche_dichotomique(tab, 12)
True
>>> recherche_dichotomique(tab, 17)
False
```

    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        ...
    ```

    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        '''
        renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
        '''
        ... = ...
        ... = ...
        while ... <= ... :
            ... = ...   
            ... = ...         
            if ... == ... :              
                return ...
            if ... < ...:                
                ... = ...         
            else :
                ... = ...
        return False
    ```

    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        '''
        renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
        '''
        i_debut = ...
        i_fin = ...
        while ... <= ... :
            i_centre = ...   
            val_centrale = ...         
            if ... == ... :              
                return ...
            if ... < ...:                
                i_debut = ...        
            else :
                i_fin = ...
        return False
    ```

    ```python linenums='1'
    def recherche_dichotomique(tab, val) :
        '''
        renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
        '''
        i_debut = ...
        i_fin = ...
        while ... <= ... :
            i_centre = (... + ...) // 2     
            val_centrale = tab[...]         
            if val_centrale == val:              
                return ...
            if val_centrale < val:                
                i_debut = ... + 1            
            else :
                i_fin = ... - 1
        return False
    ```

### Vers l'algorithme d'interclassement

Pour interclasser deux listes triées ```lst1``` et ```lst2```.

    - on part d'une liste vide ```lst_totale```
    - on y ajoute alternativement les éléments de ```lst1``` et ```lst2```, en veillant à maintenir un ordre croissant. Il faut pour cela gérer séparément un indice ```i1``` pour la liste ```lst1```  et un indice ```i2```  pour la liste ```lst2```.
    - quand une liste est épuisée, on y ajoute la totalité restante de l'autre liste.

Exemple d'utilisation :

```python
>>> interclassement([2, 4, 5, 13, 15, 19], [3, 7, 8, 10, 16])
[2, 3, 4, 5, 7, 8, 10, 13, 15, 16, 19]
```

    ```python linenums='1'
    def interclassement(lst1, lst2):
        ...
                           
    ``` 
 
    ```python linenums='1'
    def interclassement(lst1, lst2):
        i1 = ...
        i2 = ...
        lst_totale = ...
        while ...:
            if ...:
                lst_totale.append(...)
                ...
            else:
                lst_totale.append(...)
                ...
        return ... + ... + ...                        
    ``` 

    ```python linenums='1'
    def interclassement(lst1, lst2):
        i1 = ...
        i2 = ...
        lst_totale = ...
        while i1 !=... and i2 != ...:
            if ... < ...:
                lst_totale.append(...)
                ... += ...
            else:
                lst_totale.append(...)
                ... += ...
        return ... + ... + ...                           
    ``` 

    ```python linenums='1'
    def interclassement(lst1, lst2):
        i1 = ...
        i2 = ...
        lst_totale = ...
        while i1 != len(...) and i2 != len(...):
            if lst1[...] < lst2[...]:
                lst_totale.append(...)
                ... += 1
            else:
                lst_totale.append(lst2[...])
                ... += 1
        return lst_totale + lst1[...] + lst2[...]                      
    ```

### Diviser pour regner

Terminale - Spécialité NSI IFS Singapour
Chapitre 24 - Diviser pour régner
Objectifs :
▷ Ecrire un algorithme en utilisant la méthode"diviser pour régner".
1 Introduction
Nous avons vu en première deux algorithmes de tris assez naturels, mais peu efficaces : letri par insertionet
le tri par sélectionen classe de Première.
Cette année, nous allons étudier un algorithme beaucoup plus efficace et très utilisé, inventé parJohn Von
Neumann en 1945 : letri par fusion.
Cet algorithme nous permettra d'illustrer la méthodediviser pour régnerque nous avions également déjà
vue lors de larecherche dichotomiqueen classe de Première.
2 La dichotomie (rappels)
Nous avons vu en classe dePremièrel'algorithme dedichotomie. Ce mot, qui vient du grecdikhotomia, signifie
« division en deux parties ».
Notre but ici est la recherche de la présence (ou non) d'un élément dans une liste triée. Notre fonction renverra
donc un booléen.
La recherche naïve(élément par élément) est naturellement decomplexité linéaire. Nous allons voir que
la méthode dichotomique est plus efficace.
2.1 Version itérative
1 def r e c h e r c h e _ d i c h o t o m i q u e ( tab , val ) :
2 ''' renvoie True ou False suivant la presence de la valeur val dans le
tableau deja trie tab .
3 '''
4 i_debut = 0
5 i_fin = len ( tab ) - 1
6 while i_debut <= i_fin :
7 i_centre = ( i_debut + i_fin ) // 2 # on prend l ' indice central
8 v a l _ c e n t r a l e = tab [ i_centre ] # on prend la valeur centrale
9 # si la valeur centrale est la valeur cherchee
10 if v a l _ c e n t r a l e == val :
11 return True
12 # si la valeur centrale est trop petite
13 if v a l _ c e n t r a l e < val :
14 i_debut = i_centre + 1
15 # on ne prend pas la valeur centrale qui a deja ete testee
16 else :
17 i_fin = i_centre - 1
18 return False
Exemple d'utilisation :
>>> tab = [1 , 5 , 7 , 9 , 12 , 13]
>>> r e c h e r c h e _ d i c h o t o m i q u e ( tab ,12)
True
>>> r e c h e r c h e _ d i c h o t o m i q u e ( tab ,17)
False
T. Rahobisoa 1/9 ALGO04 - Diviser pour régner
Terminale - Spécialité NSI IFS Singapour
À chaque tour de la boucle while, la taille de la liste est divisée par 2. Ceci confère à cet algorithme une
complexité logarithmique(bien meilleure qu'unecomplexité linéaire).
2.2 Version récursive
2.2.1 Le slicing
Pour écrire simplement la version récursive de cet algorithme, nous allons avoir besoin de faire duslicing
(découpage) de listes.
Exemples deslicing :
>>> lst = [ 'a ' , 'b ' , 'c ' , 'd ' , 'e ']
>>> lst [:2]
[ 'a ' , 'b ']
>>> lst [2:]
[ 'c ' , 'd ' , 'e ']
On comprend que :
— lst[:k] va renvoyer la sous-liste composée du premier élément jusqu'à celui d'indicek non inclus.
— lst[k:] va renvoyer la sous-liste composée duk-ième élément (inclus) jusqu'au dernier.
— plusgénéralement, lst[k:p]va renvoyerla sous-listecomposéedu k-ième élément (inclus) jusqu'aup-ième
(non inclus).
2.2.2 Dichotomie récursive avec slicing
1 def d i c h o t o m i e _ r e c ( tab , val ) :
2 if len ( tab ) == 0:
3 return False
4 i_centre = len ( tab ) // 2
5 if tab [ i_centre ] == val :
6 return True
7 if tab [ i_centre ] < val :
8 return d i c h o t o m i e _ r e c ( tab [ i_centre + 1:] , val )
9 # On prend la partie droite de liste , juste apres l ' indice central
10 else :
11 return d i c h o t o m i e _ r e c ( tab [: i_centre ] , val )
12 # On prend la partie gauche de liste , juste avant l ' indice central
T. Rahobisoa 2/9 ALGO04 - Diviser pour régner
Terminale - Spécialité NSI IFS Singapour
Exemple d'utilisation :
>>> tab = [1 , 5 , 7 , 9 , 12 , 13]
>>> d i c h o t o m i e _ r e c ( tab ,12)
True
>>> d i c h o t o m i e _ r e c ( tab ,17)
False
2.2.3 Dichotomie récursive sans slicing
Il est possible de programmer de manière récursive la recherche dichotomique sans toucher à la liste, et donc en
jouant uniquement sur les indices :
1 def d i c h o _ r e c _ 2 ( tab , val , i =0 , j = None ) :
2 # Pour pouvoir appeler s i m p l e m e n t la fonction sans preciser les indices
3 # on leur donne des p a r a m e t r e s par defaut
4 if j is None :
5 j = len ( tab ) -1
6 if i > j :
7 return False
8 m = ( i + j ) // 2
9 if tab [ m ] < val :
10 return d i c h o _ r e c _ 2 ( tab , val , m +1 , j )
11 elif tab [ m ] > val :
12 return d i c h o _ r e c _ 2 ( tab , val ,i ,m -1)
13 else :
14 return True
Exemple d'utilisation :
>>> tab = [1 , 5 , 7 , 9 , 12 , 13]
>>> d i c h o _ r e c _ 2 ( tab ,12)
True
>>> d i c h o _ r e c _ 2 ( tab ,17)
False
3 Diviser pour régner
Les algorithmes de dichotomie ont tous en commun dediviser par deuxla taille des données de travailà
chaque étape.
Cette méthode de résolution d'un problème est connue sous le nom dediviser pour régner, ou divide and
conquer en anglais.
T. Rahobisoa 3/9 ALGO04 - Diviser pour régner
Terminale - Spécialité NSI IFS Singapour
A retenir!
Le principe de diviser pour régner consiste à ramener la résolution d'un problème surn données
à la résolution d'un problème sur la moitié des données et poursuivre ce découpage jusqu'à ce que le
problème devienne évident (par exemple trier un tableau d'une seule donnée).
Une fois que les solutions des sous problèmes ont été trouvées, on lescombine pour obtenir la solution
du problème complet.
▷ Diviser : découper un problème initial en sous-problèmes;
▷ Régner : résoudre les sous-problèmes (récursivement ou directement s'ils sont assez petits);
▷ Combiner : calculer une solution au problème initial à partir des solutions des sous-problèmes.
4 Le tri fusion
Ainsi l'algorithme detri fusion qui s'appuie sur le principe"diviser pour régner"permet de fusionner deux
tableaux déjà triés en un tableau trié.
Exemple :
Pour fusionner ces deux tableaux triés :
Etape par étape
Il suffit d'une itération sur les deux listes en même temps donc ici 5 itérations pour une liste de 7
éléments :
1. On considère 3 et 9, on place3, et on avance sur la 1ère liste.
2. On considère 27 et 9, on place9, et on avance sur la 2e liste.
3. On considère 27 et 10, on place10, ...
4. On considère 27 et 82, on place27, ...
5. On considère 38 et 82, on place38, ...
6. On considère 43 et 82, on place43, et on voit qu'on est arrivé au bout de la première liste.
7. On place maintenant tous les éléments restants de la deuxième liste.
Le découpage récursifd'un tableau jusqu'à arriver au cas terminal. On va donc séparer notre algorithme en
deux fonctions :
— une qui réalise lafusion
— l'autre qui réalise la récursion du tri c'est-à-dire ledécoupage.
T. Rahobisoa 4/9 ALGO04 - Diviser pour régner
Terminale - Spécialité NSI IFS Singapour
Ces deux opérations sont symbolisées sur l'illustration ci-dessous :
— rouge :division
— vert :fusion
4.1 L'algorithme de fusion (version itérative)
Voici l'algorithme de fusionde deux tableaux triés en un seul écrit en pseudo-code :
Algorithme 1 :Fonction fusion de 2 tableaux d'entiers triés
Entrées : T 1, T 2 : tableaux d'entiers triés
Sortie : T : tableau
i1← 0 // indice du 1er tableau
i2← 0 // indice du 2e tableau
T← [] // liste vide destinée à accueillir les éléments triés
tant quenon atteint la fin d'un des tableauxfaire
si T 1[i1]≤ T 2[i2] alors
Insérer T 1[i1] à la fin de tableau
Incrémenter i1
fin
sinon
Insérer T 2[i2] à la fin du tableau
Incrémenter i2
fin
fin
si i1 < longueur de T 1 alors
Insérer tous les éléments restants deT 1 à la fin du tableau
fin
sinon si i2 < longueur de T 2 alors
Insérer tous les éléments restants deT 2 à la fin de tableau
fin
return T
T. Rahobisoa 5/9 ALGO04 - Diviser pour régner
Terminale - Spécialité NSI IFS Singapour
4.2 L'algorithme de tri fusion
Voici l'algorithme récursif de tri fusion qui utilise la fonctionfusion définie précédemment.
En pseudo-code, on retrouve des techniques de découpage du tableau en deux avec des divisions entières//
vues dans la recherche dichotomique.
Algorithme 2 :Fonction tri_fusion
Entrées : T : tableau
Sortie : T : tableau trié
n← Longueur de T;
// Cas terminal: une liste de un élément est forcément triée
si n == 1 alors
return T;
fin
// Recursion sur les deux demi-tableaux sinon
T 1← liste des n//2 premiers éléments deT;
T 2← liste des n//2 derniers éléments deT;
// Renvoi de la fusion des deux tableaux triés
return fusion(tri_fusion(T 1), tri_fusion(T 2));
5 Conclusion
Nous avons vu dans ce chapitre un algorithme particulièrementélégantetefficacepour trier des éléments. Bien
sûr, dans la pratique des contraintes de mémoire peuvent intervenir, et là au contraire cet algorithme se révélera
peu performant, car l'utilisation de larécursivité et du tableau intermédiaire le rend trèsgourmand en
mémoire.
La méthode «diviser pour régner»est une méthode trèsefficace pour résoudre des problèmescomplexes en
les découpant en sous problèmes indépendants.
En revanche, elle devient inefficace si les sous-problèmes se chevauchent, et il conviendra alors d'utiliser la
technique de la« Programmation dynamique »vue précédemment au chapitre 22.
T. Rahobisoa 6/9 ALGO04 - Diviser pour régner
Terminale - Spécialité NSI IFS Singapour
6 Exercices
Exercice 1 :Dichotomie
Compléter le code incomplet ci dessous :
1 def r e c h e r c h e _ d i c h o t o m i q u e ( tab , val ) :
2 '''
3 renvoie True ou False suivant la presence de la valeur val
4 dans le tableau trie tab
5 '''
6 i_debut = ...
7 i_fin = ...
8 while ... <= ... :
9 i_centre = ...
10 v a l _ c e n t r a l e = ...
11 if ... == ... :
12 return ...
13 if ... < ...:
14 i_debut = ...
15 else :
16 i_fin = ...
17 return False
Pour tester :
>>> tab = [1 ,5 ,7 ,9 ,12 ,13]
>>> r e c h e r c h e _ d i c h o t o m i q u e ( tab ,12)
True
>>> r e c h e r c h e _ d i c h o t o m i q u e ( tab ,17)
False
Exercice 2 :L'algorithme de fusion
Implémenter en Python l'algorithme de fusiondu cours (algorithme 1).
Pour tester :
>>> fusion ([3 ,6 ,8] ,[2 ,5 ,7 ,12])
[2 ,3 ,5 ,6 ,7 ,8 ,12]
Exercice 3 :L'algorithme de tri fusion
Implémenter en Python l'algorithme de tri fusiondu cours (algorithme 2).
Pour tester :
>>> t r i _ f u s i o n ([0 ,25 ,36 ,41 ,1 ,465 ,2 ,3 ,987])
[0 ,1 ,2 ,3 ,25 ,36 ,41 ,465 , 987]
T. Rahobisoa 7/9 ALGO04 - Diviser pour régner
Terminale - Spécialité NSI IFS Singapour
Exercice 4 :L'algorithme de tri par insertion
Le tri par insertion est un algorithme efficace qui s'inspire de la façon dont on peut trier une poignée de cartes.
On commence avec une seule carte dans la main gauche (les autres cartes sont en tas sur la table) puis on pioche
la carte suivante et on l'insère au bon endroit dans la main gauche.
Voici une implémentation en Python de cet algorithme :
1 def t r i _ i n s e r t i o n ( liste ) :
2 """ tri par in se rt io n la liste en pa r am et re """
3 for i n d i c e _ c o u r a n t in range (1 , len ( liste ) ) :
4 e l e m e n t _ a _ i n s e r e r = liste [ i n d i c e _ c o u r a n t ]
5 i = i n d i c e _ c o u r a n t - 1
6 while i >= 0 and liste [ i ] > .... :
7 liste [...] = liste [...]
8 i = i -1
9 liste [ i +1] = e l e m e n t _ a _ i n s e r e r
1. Compléter les lignes 6 et 7 du code ci-dessus pour faire fonctionner le tri par insertion.
2. Tester la fonction avec la listenotes = [8, 7, 18, 14, 12, 9, 17, 3]
Exercice 5 :Sujet Bac - épreuve pratique : sujet n°28 - session 2021
On considère l'algorithme de tri de tableau suivant : à chaque étape, on parcourt depuis le début du tableau
tous les éléments non rangés et on place en dernière position le plus grand élément.
Exemple avec le tableau :t = [41, 55, 21, 18, 12, 6, 25]
— Étape 1 : on parcourt tous les éléments du tableau, on permute le plus grand élément avec le dernier. Le
tableau devient t = [41, 25, 21, 18, 12, 6, 55]
— Étape 2 : on parcourt tous les éléments sauf le dernier, on permute le plus grand élément trouvé avec
l'avant-dernier. Le tableau devient :t = [6, 25, 21, 18, 12, 41, 55]
— Et ainsi de suite...
Le code de la fonctiontri_iteratif qui implémente cet algorithme est donné ci- dessous :
1 def t r i _ i t e r a t i f ( tab ) :
2 for k in range (... , 0 , -1) :
3 imax = ...
4 for i in range (0 , ...) :
5 if tab [ i ] > ... :
6 imax = i
7 if tab [ imax ] > ... :
8 ... , tab [ imax ] = tab [ imax ] , ...
9 return tab
Compléter le code qui doit donner :
>>> t r i _ i t e r a t i f ([41 , 55 , 21 , 18 , 12 , 6 , 25])
[6 , 12 , 18 , 21 , 25 , 41 , 55]
On rappelle que l'instructiona, b = b, a échange les contenus dea et b.
T. Rahobisoa 8/9 ALGO04 - Diviser pour régner
Terminale - Spécialité NSI IFS Singapour
Exercice 6 :L'algorithme de tri par sélection
Comme dans la plupart des algorithmes de tri étudiés, nous allons travailleren place. Cela signifie que nous
ne travaillons que sur la liste initiale, sans en créer de nouvelles. Le tri par sélection sera fait en permutant des
éléments.
L'idée de l'algorithme (vu enPremière) est la suivante :
— on cherche le minimum de toute la liste, et on le place au tout début de la liste.
— on cherche maintenant le minimum de toute la liste SAUF le 1er terme, et on le place en 2ème position.
— on continue ainsi jusqu'à la fin.
Implémenter le tri par sélection en ne manipulant les indices des éléments de la liste.
Pour tester :
>>> ma_liste = [7 , 5 , 2 , 8 , 1 , 4]
>>> t r i _ s e l e c t i o n ( ma_liste )
>>> ma_liste
[1 , 2 , 4 , 5 , 7 , 8]
Exercice 7 :Sujet Bac - épreuve pratique : sujet n°43 - session 2023
La fonction tri_bulles prend en paramètre une listeT d'entiers non triés et renvoie la liste triée par ordre
croissant.
Le tri à bulles est un tri en place qui commence par placer le plus grand élément en dernière position en
parcourant la liste de gauche à droite et en échangeant au passage les éléments voisins mal ordonnés (si la
valeur de l'élément d'indicei a une valeur strictement supérieure à celle de l'indicei+1, ils sont échangés).
Le tri place ensuite en avant-dernière position le plus grand élément de la liste privée de son dernier élément
en procédant encore à des échanges d'éléments voisins. Ce principe est répété jusqu'à placer le minimum en
première position.
Exemple :pour trier la liste[7, 9, 4, 3] :
— première étape :7 et 9 ne sont pas échangés, puis9 et 4 sont échangés, puis9 et 3 sont échangés, la liste
est alors [7, 4, 3, 9]
— deuxième étape :7 et 4 sont échangés, puis7 et 3 sont échangés, la liste est alors[4, 3, 7, 9]
— troisième étape :4 et 3 sont échangés, la liste est alors[3, 4, 7, 9]
Compléter le code Python ci-dessous qui implémente la fonctiontri_bulles.
1 def t r i _ b u l l e s ( T ) :
2 ''' Renvoie le tableau T trie par ordre cr oi ss an t '''
3 n = len ( T )
4 for i in range (... ,... , -1) :
5 for j in range ( i ) :
6 if T [ j ] > T [...]:
7 ... = T [ j ]
8 T [ j ] = T [...]
9 T [ j +1] = temp
10 return T
Pour tester :
>>> t r i _ b u l l e s ([])
[]
>>> t r i _ b u l l e s ([9 , 3 , 7 , 2 , 3 , 1 , 6])
[1 , 2 , 3 , 3 , 6 , 7 , 9]
>>> t r i _ b u l l e s ([9 , 7 , 4 , 3])
[3 , 4 , 7 , 9]
T. Rahobisoa 9/9 ALGO04 - Diviser pour régner

## Programmation dynamique

### À la recherche du plus grand carré blanc

L'objectif est de trouver la taille du plus grand carré intégralement blanc que l'on peut dessiner dans l'image ci-dessous :

### 1. Prise en main

Télécharger l'image, puis creér une variable ```img``` grâce au package ```PIL```:

    ```python linenums='1'
    from PIL import Image
    img = Image.open('pgcb.bmp')
    ``` 

    On peut dès lors avoir accès à quelques informations :

    ```python
    >>> img.size
    (600, 600)
    ```
    L'image est donc de taille 600x600.

    ```python
    >>> img.getpixel((0, 0))
    (255, 255, 255)
    >>> img.getpixel((0, 358))
    (0, 0, 0)
    ```

    Le pixel de coordonnées (0, 0) est donc blanc, et le pixel (0, 358) est noir. 

    Écrire une fonction ```est_noir``` qui prend en paramètre les coordonnées d'un pixel ```x``` et ```y```   et qui renvoie ```True``` si ce pixel est noir, ```False``` sinon.

    *Exemple :*
    ```python
    >>> est_noir(0, 0)
    False
    >>> est_noir(0, 358)
    True
    ```

### 1.2 Recherche manuelle

Considérons le damier ci-dessous :

Pour chaque case, on va inscrire à l'intérieur la taille du plus grand carré blanc possible **dont la case est le coin inférieur droit**.

Par exemple :

Sur une case noire, on écrira le nombre 0.

    Recopier le damier et compléter toutes les cases, **en commençant en haut à gauche**.

    

Imaginons maintenant la situation suivante, sur un autre damier que vous ne pouvez pas voir en intégralité :

    Quelle est la valeur qu'il faut écrire à la place du point d'interrogation ?

### 2.1 Première écriture

On va écrire la fonction récursive ```pgcb```, qui prend en paramètre deux nombres ```x```  et ```y```  et qui renvoie la taille du plus grand carré blanc dont le pixel de coordonnées ```(x,y)``` est le coin inférieur droit.

Les cas de base seront :

- le pixel est noir : on renvoie 0
- le pixel est sur la ligne du haut ou la colonne de gauche : on renvoie 1

Pour le cas général, on s'inspirera de la partie précédente...

    Écrire le code de la fonction ```pgcb```. 

    ```python linenums='1'
    def pgcb(x, y):
        if ...:
            return 0
        
        if ...:
            return 1
        
        return ... + ...
    ```

    *Exemples d'utilisation :*
    ```python
    >>> pgcb(0,0)
    1
    >>> pgcb(3,2)
    3
    >>> pgcb(0,358)
    0
    ```

### 2.2 Amélioration de la fonction ```pgcb```

Si on teste la fonction avec le pixel de coordonnées ```(300, 300)```, le code ne renvoie aucun résultat et semble parti dans des calculs interminables.

La structure récursive du code doit nous pousser à la méfiance : ne saurions-nous pas en train de lui demander de calculer plusieurs fois la même chose ?

La réponse est oui : si on ne regarde par exemple que les pixels diagonaux, l'appel  ```pgcb(1, 1)``` aura lieu pour  ```pgcb(2, 2)```, mais aussi pour ```pgcb(3, 3)```, pour ```pgcb(4, 4)```, pour ```pgcb(5, 5)```... entre autres !

Pour éviter de refaire ces calculs, on va donc faire appel à la technique de ```mémoïsation```.

    Écrire la fonction ```pgcb_memo```, identique à la fonction ```pgcb``` mais qui mémoïse ses résultats. On pourra se servir d'une fonction englobante comme dans le cours sur Fibonacci.

    ```python linenums='1'
    def pgcb_memo(x, y):
        dict_memo = {}
        def pgcb(x, y):
            if ...:
                return 0
            if ...:
                return 1
            if ... in ...:
                return ...
            dict_memo[(x, y)] = ...
            return ...
        return pgcb(x, y)
    ```

    *Exemple :*
    ```python
    >>> pgcb_memo(300,300)
    21
    ```

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        def pgcb_memo(x, y):
            dict_memo = {}
            def pgcb(x, y):
                if est_noir(x, y):
                    return 0
                if x == 0 or y == 0:
                    return 1
                if (x, y) in dict_memo:
                    return dict_memo[(x, y)]
                dict_memo[(x, y)] = 1 + min(pgcb(x-1, y), pgcb(x, y-1), pgcb(x-1, y-1))
                return dict_memo[(x, y)]
            return pgcb(x, y)
        ```
    """
    )
    }}

### 3. Recherche du plus grand carré

Maintenant que notre fonction est efficace, nous pouvons partir à la recherche du pixel de l'image d'où peut se construire le plus grand carré blanc.

    Écrire une fonction ```total_pgcb``` qui va parcourir tous les pixels de l'image et renvoyer la taille du plus grand carré blanc qu'on puisse y inscrire, ainsi que les coordonnées du pixel inférieur droit de ce carré.

    *Exemple :*
    ```python
    >>> total_pgcb()
    (51, (370, 461))
    ``` 

    :warning: Dans la structure de votre code, penser à réutiliser le dictionnaire de mémoïsation...

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        def total_pgcb():
            dict_memo = {}
            def pgcb(x, y):
                if est_noir(x, y):
                    return 0
                
                if x == 0 or y == 0:
                    return 1
                
                if (x, y) in dict_memo:
                    return dict_memo[(x, y)]
                dict_memo[(x, y)] = 1 + min(pgcb(x-1, y), pgcb(x, y-1), pgcb(x-1, y-1))
                return dict_memo[(x, y)]
            
            maxi = 0
            for x in range(600):
                for y in range(600):
                    taille_pgcb = pgcb(x, y)
                    if taille_pgcb > maxi:
                        maxi = taille_pgcb
                        best_pixel = (x, y)
            return maxi, best_pixel
        ```
        On trouve donc :
        ```python
        >>> total_pgcb()
        (51, (370, 461))
        ``` 
        Voici la position de ce carré :

        
        

    """
    )
    }}

### 4. Bonus : méthode bottom-up

En s'inspirant de la manière dont on a rempli manuellement les cases au 1.2, écrire une fonction ```pgcb_bottom_up```.

    ```python linenums='1'
    def pgcb_bottom_up():
        memo = {}
        maxi = 0
        for x in range(600):
            for y in range(600):
                if ...:
                    memo[(x,y)] = ...
                elif ... or ...:
                    memo[(x,y)] = ...
                else:
                    memo[(x,y)] = ...
                if memo[(x,y)] > ...:
                    maxi = ...
                    best = ...
        return maxi, best
    ```

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        def pgcb_bottom_up():
            memo = {}
            maxi = 0
            for x in range(600):
                for y in range(600):
                    if est_noir(x, y):
                        memo[(x,y)] = 0
                    elif x == 0 or y == 0:
                        memo[(x,y)] = 1
                    else:
                        memo[(x,y)] = 1 + min(memo[(x-1, y)] , memo[(x-1, y-1)] , memo[(x, y-1)])
                    if memo[(x,y)] > maxi:
                        maxi = memo[(x,y)]
                        best = (x,y)
            return maxi, best
        ```
    """
    )
    }}

### Optimisation d'une somme dans une pyramide

Considérons la pyramide ci-dessous :

    

    En partant du sommet et en descendant jusqu'en bas en prenant soit à gauche soit à droite, quelle est la somme maximale que l'on peut obtenir ?

### 1. Quelques outils

:arrow_right: La pyramide ci-dessus sera implémentée par une liste de listes :

```python
pyr_exemple = [[3], [5, 4], [1, 2, 9], [2, 6, 5, 3], [5, 8, 9, 7, 9]]
```

:arrow_right: Pour générer une pyramide de hauteur ```n``` (composée d'entiers aléatoires entre 0 et 9) :

```python linenums='1'
from random import randint

def genere_pyr(n):
    pyr = []
    for k in range(1, n+1):
        lst = [randint(0,9) for _ in range(k)]
        pyr.append(lst)
    return pyr
```

:arrow_right: Pour afficher une pyramide en console :
```python linenums='1'
def affiche(pyr):
    for lst in pyr:
        print(" "*(len(pyr)-len(lst)) + " ".join(str(k) for k in lst))
```

    Créer puis afficher une pyramide de hauteur 10.

### 2.1 Liste de tous les parcours

La fonction ```liste_parcours```  ci-dessous renvoie la liste de tous les trajets possibles lors de la traversée de la pyramide ```pyr```. Ces parcours contiennent les **indices** des valeurs traversées lors du parcours.

```python linenums='1'
def liste_parcours(pyr):
    file = [[0]]
    parcours = []
    while file:
        trajet = file.pop(0)
        j = trajet[-1]
        trajet_left = trajet[::]
        trajet_right = trajet[::]
        niv = len(trajet)
        trajet_left.append(j)
        trajet_right.append(j+1)
        if len(trajet_left) == len(pyr):
            parcours.append(trajet_left)
        else:
            file.append(trajet_left)
        if len(trajet_right) == len(pyr):
            parcours.append(trajet_right)
        else:
            file.append(trajet_right)
    return parcours
```

    1. Observez la liste des trajets pour la pyramide ```pyr_exemple``` pour en comprendre la notation.
    2. Pour une pyramide de hauteur $n$, combien y a-t-il de trajets différents ? 
    3. Pour une pyramide de hauteur 41, que pensez-vous du nombre de trajets différents ?

    {{
    correction(True,
    """
\"Correction\" 
        Le nombre de trajets pour une hauteur $n$ est $2^{n-1}$.

        Pour une pyramide de hauteur 41, cela donne $2^{40}$, soit plus de mille milliards de chemins possibles...
    """
    )
    }}

### 2.2 Valeur d'un trajet

Écrire une fonction ```val_trajet``` qui prend en paramètres un trajet ```trajet``` et une pyramide ```pyr``` et qui renvoie la somme finale à l'issue de ce trajet.

    Exemple :
    ```python
    >>> val_trajet([0, 1, 1, 2, 2], pyr_exemple)
    23
    ```

### 2.3 Somme maximale par force brute

**Q1.** Écrire une fonction ```max_force_brute``` qui prend en paramètre une pyramide ```pyr``` et qui renvoie la somme maximale parmi tous les trajets possibles.

    

    **Q2.** Testez votre algorithme avec ```pyr_exemple```, ainsi qu'avec des pyramides de taille supérieure. Que se passe-t-il ?

### 3. Recherche par méthode gloutonne

Notre algorithme de force brute n'étant pas utilisable, il va falloir essayer d'être plus efficace. Pourquoi ne pas chercher une méthode gloutonne ?

*Rappel :*  lors du parcours d'une pyramide, les deux cases sous la case ```[i][j]``` sont la case ```[i+1][j]``` et ```[i+1][j+1]```.

    **Q1.** Compléter la fonction ```max_glouton``` ci-dessous qui calcule de manière gloutonne le «meilleur» trajet d'une pyramide ```pyr```. 

    ```python linenums='1'
    def max_glouton(pyr):
        s = pyr[0][0]
        j = 0
        for i in range(..., ...):
            v1 = ...
            v2 = ...
            if ... > ...:
                ... += ...
            else:
                ... += ...
                j = ...
        return s
    ```
  
    

    **Q2.** Observer et analyser le résultat donné par notre algorithme sur ```pyr_exemple```.

### 4. Recherche par méthode récursive

Observer le dessin suivant :
    

    **Q1.** En déduire une fonction ```max_recursif``` qui prendra en paramètre une pyramide ```pyr``` et qui calculera de manière récursive la somme maximale.

    Pour extraire les deux sous-pyramides gauche et droite, on pourra utiliser le code suivant :

    ```python linenums='1'
    def extract_sub_left_right(pyr):
        left = []
        right = []
        for k in range(1, len(pyr)):
            lst_left = [pyr[k][j] for j in range(k)]
            lst_right = [pyr[k][j+1] for j in range(k)]
            left.append(lst_left)
            right.append(lst_right)
        return left, right
    ```

    ```python linenums='1'
    def max_recursif(pyr):
        if len(pyr) == 1:
            return ...
        pyr_left, pyr_right = extract_sub_left_right(pyr)
        return ... + max(..., ...)
    ```

    

    **Q2.** Testez votre algorithme avec ```pyr_exemple```, ainsi qu'avec des pyramides de taille supérieure. Que se passe-t-il ?

### 5. Optimisation de la méthode récursive par programmation dynamique

La lenteur de l'algorithme précédent vient du fait que certains calculs sont redondants. 

Par exemple, le calcul du maximum de la pyramide rouge sera lancé en tant que sous-pyramide droite de la valeur 5, et en tant que sous-pyramide gauche de la valeur 4.

Si la pyramide initiale est grande, ces appels inutiles vont se multiplier et ralentir considérablement l'exécution du programme.

    Dans le code récursif suivant, chaque pyramide est identifiée par les coordonnées de son sommet, stockées dans le tuple ```pos``` .
    On va utiliser un dictionnaire ```dict_max``` qui associera à chaque sommet ```(i, j)``` la somme maximale de sa pyramide.

    Pour chaque sommet de coordonnées ```(i, j)``` :
    
    - si on est tout en bas de la pyramide, on renvoie la valeur du sommet de cette pyramide (réduite à une valeur).
    - sinon :
        - on interroge notre dictionnaire de stockage ```dict_max``` : est-ce qu'il contient parmi ses clés notre tuple ```(i, j)``` ? Si oui, on renvoie juste la valeur associée.
        - sinon, on calcule cette valeur par deux appels récursifs (sur les deux sous-pyramides), et on la stocke dans ```dict_max```, associée au tuple  ```(i, j)```, avant de la renvoyer.
    

    **Q1.** Compléter le code suivant :

    ```python linenums='1'
    dict_max = {}
    def max_rec_dynamique(pyr, pos=(0,0)):
        i, j = pos
        if i == len(pyr) - 1:
            return ...

        if ... in dict_max:
            return ...
        else:   
            dict_max[(i, j)] = ... + max(max_rec_dynamique(pyr, ...), max_rec_dynamique(pyr, ...))
            return ...
    ``` 

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        dict_max = {}
        def max_rec_dynamique(pyr, pos=(0,0)):
            i, j = pos
            if i == len(pyr) - 1:
                return pyr[i][j]

            if (i, j) in dict_max:
                return dict_max[(i, j)]
            else:   
                dict_max[(i, j)] = pyr[i][j] + max(max_rec_dynamique(pyr, (i+1, j)), max_rec_dynamique(pyr, (i+1, j+1)))
                return dict_max[(i, j)]        
        ```

    """
    )
    }}

    **Q2.** Testez votre algorithme avec ```pyr_exemple```, ainsi qu'avec des pyramides de taille supérieure. Que constatez-vous ?

### 6. Méthode bottom-up

Dans la figure ci-dessus, le chemin surligné est le chemin de longueur minimale entre A et C. 

    Ce chemin passe par B. 

    On peut donc en déduire que la portion de ce chemin entre B et C (portion rouge) est le chemin minimal entre B et C.

    > On peut le démontrer facilement *par l'absurde* : si le chemin rouge n'est pas le chemin minimal entre B et C, alors il en existe un autre qui est minimal (par exemple le violet). En emprutant ce chemin à partir de B, on pourrait donc construire entre A et C un chemin plus court que le chemin surligné, ce qui est impossible.

    De manière analogue, on peut affirmer ceci : si le chemin minimal passe par B, alors la portion de ce chemin minimal entre B et C est forcément le chemin rouge.

Nous allons exploiter une idée similaire pour maximiser le parcours dans notre pyramide.

Admettons que le parcours maximal passe par la valeur 6. Ensuite, ce parcours doit passer par 8 ou par 9. Comme ce parcours est maximal, il passera forcément par 9.

On peut donc en déduire que si le parcours arrive à cette valeur 6, alors cette valeur pourrait être remplacée par 15.

Faisons de même pour les autres valeurs de l'avant-dernière ligne :

En procédant de même pour les lignes supérieures, on trouve la valeur maximale de 30 :

    En s'inspirant de la méthode précédente, écrire une fonction ```max_iteratif``` qui prend une pyramide ```pyr``` en paramètre et qui renvoie la somme maximale des parcours de cette pyramide.

    Effectuer des tests pour apprécier l'efficacité de cette fonction.

    ```python linenums='1'
    def max_iteratif(pyr):
        for i in range(..., ..., ...):
            for j in range(...):
                pyr[i][j] = ... + max(..., ...)
        return pyr[...][...]
    ```

### Optimisation de rendu de monnaie

Nous allons nous intéresser au problème suivant :

    Étant donnés une liste de pièces ```pieces``` et une somme à rendre ```somme```, peut-on calculer le nombre minimal de pièces pour réaliser cette somme ?

**Remarques importantes :**

- Dans toute la suite, on considérera que la somme à rendre est un nombre entier positif, et que dans la liste de pièces se trouve la pièce de valeur 1. Ainsi, il est **toujours possible** de rendre la monnaie.
- Notez bien que tous nos futurs algorithmes vont chercher à donner **le nombre de pièces rendues** et pas la composition de celles-ci.

### 1. Retour sur l'algorithme glouton

Nous avons vu en Première un algorithme capable de donner une combinaison de pièces pour rendre la somme ```somme```.

Cet algorithme fonctionnait de manière gloutonne : on cherche à rendre à chaque fois la plus grosse pièce possible.

    Compléter la fonction ```rendu_glouton``` qui prend en paramètres une liste de pièces ```pieces``` (classées dans l'ordre **croissant**) et la somme à rendre ```somme``` et qui renvoie **le nombre minimal** de pièces qu'il faut rendre.

    ```python linenums='1'
    def rendu_glouton(pieces, somme):
        i =  ... # (1)
        nb_pieces = ...
        while ... > ...:
            if ... >> rendu_glouton([1, 2, 5], 12)
    3
    ``` 

    

Nous savons que cet algorithme est optimal sous certaines conditions sur la composition des pièces. Par exemple le système des euros (1, 2, 5, 10, 20, 50, 100, 200) rend l'algorithme glouton optimal (on dit que le système est *canonique*).

Mais si le système n'est pas canonique, l'algorithme glouton peut ne pas donner la meilleure solution :

```python
>>> rendu_glouton([1, 6, 10], 12)
3
```

Notre algorithme va trouver que $12 = 10 + 1 + 1$ et donc rendre 3 pièces, alors qu'il est possible de faire $12 = 6+6$ et ne rendre que 2 pièces.

### 2. Algorithme récursif

Il est possible de construire un algorithme optimal de manière récursive.

Il faut pour cela faire les observations suivantes :

- pour rappel, le rendu est toujours possible : dans le pire des cas, le nombre de pièces à rendre est égal à la somme de départ (rendu effectué à coups de pièces de 1)
- :star: Si ```p``` est une pièce de ```pieces```, le nombre minimal de pièces nécessaires (contenant ```p```) pour rendre la somme ```somme```   est égal à 1 + le nombre minimal de pièces nécessaires pour rendre la somme ```somme - p```. :star: 

Cette dernière observation est cruciale. Elle repose sur le fait qu'il suffit de ajouter 1 pièce (la pièce de valeur ```p```) à la meilleure combinaison qui rend ```somme - p``` pour avoir la meilleure combinaison qui rend ```somme``` (meilleure combinaison parmi celles contenant ```p```). 

On va donc passer en revue toutes les pièces ```p``` et mettre à jour à chaque fois le nombre minimal de pièces.

    Compléter la fonction ```rendu_recursif``` qui prend en paramètres une liste de pièces ```pieces``` et la somme à rendre ```somme``` et qui renvoie **le nombre minimal** de pièces qu'il faut rendre.

    ```python linenums='1'
    def rendu_recursif(pieces, somme):
        nb_pieces = ... # (1)
        if somme == 0:
            return ... # (2)
        for p in pieces:
            if ... >> rendu_recursif([1, 2, 5], 12)
3
>>> rendu_recursif([1, 6, 10], 12)
2
```

Il ne se laisse pas pièger comme l'algorithme glouton et rend bien en 2 pièces la somme 12.

Mais...

```python
>>> rendu_recursif([1, 6, 10], 107)
RecursionError: maximum recursion depth exceeded in comparison
```

:cry:

Le nombre d'appels récursifs de notre algorithme augmente exponentiellement avec la valeur de la somme à rendre : on se retrouve très rapidement avec des milliards d'appels récursifs, ce qui n'est pas gérable.

Ces appels récursifs ont lieu sur un nombre limité de valeurs : par construction de notre algorithme, si la somme à rendre est 100, il y aura beaucoup (beaucoup) d'appels vers 99, vers 98, vers 97... jusqu'à 0. 

On peut donc légitimement penser à **mémoïser** notre algorithme, en stockant les valeurs pour éviter de les recalculer.

### 3. Algorithme récursif memoïsé

Compléter la fonction ```rendu_recursif_memoise``` qui prend en paramètres une liste de pièces ```pieces``` et la somme à rendre ```somme``` et qui renvoie **le nombre minimal** de pièces qu'il faut rendre.

    On utilisera le dictionnaire ```memo_rendu``` dans lequel on associera à chaque somme ```somme``` son nombre de pièces minimal. 

    On procèdera de manière classique :

    - Soit la ```somme``` est disponible dans le dictionnaire, et on se contente de renvoyer la valeur associée.
    - Soit on la calcule (comme dans l'algorithme classique), puis on stocke le résultat dans le dictionnaire avant de le renvoyer.
    
    ```python linenums='1'
    memo_rendu = {}
    def rendu_recursif_memoise(pieces, somme):
        nb_pieces = somme
        if somme == 0:
            return 0
        if ... in ...:
            return ...
        for p in pieces:
            if p >> rendu_recursif_memoise([1, 6, 10], 107)
12
```

### 4. Algorithme *bottom-up*

Nous avions calculé le $F_n$, n-ième terme de la suite de Fibonacci en calculant d'abord $F_0$, $F_1$, $F_2$, ..., jusqu'à $F_{n-1}$ puis $F_n$.

En s'inspirant de cette méthode (*bottom-up*) nous allons ici calculer successivement tous les rendus minimaux jusqu'à ```somme``` avant de calculer le rendu minimal de ```somme```.

    Compléter la fonction ```rendu_bottom_up``` qui prend en paramètres une liste de pièces ```pieces``` et la somme à rendre ```somme``` et qui renvoie **le nombre minimal** de pièces qu'il faut rendre.    

    Nous stockerons chaque rendu dans un dictionnaire ```rendu```, initialisé à la valeur 0 pour la clé 0.

    ```python linenums='1'
    def rendu_bottom_up(pieces, somme):
        rendu = 
        for s in range(..., ...): # (1)
            rendu[s] = ... #(2)
            for p in pieces:
                if p >> rendu_bottom_up([1, 6, 10], 107)
12
```

Notre algorithme itératif est de complexité linéaire (par rapport à la variable ```somme```).

### 5. Bonus : construction d'une solution

Nos différents algorithmes avaient pour but de nous renvoyer le nombre minimal de pièces. Mais peut-on les modifier pour qu'ils renvoient la liste de pièces utilisées ?

Nous allons nous appuyer sur le dernier algorithme créé (par méthode *bottom-up*).

Il suffit de rajouter un dictionnaire *solutions* qui associera à chaque somme la liste des pièces nécessaires.

Lors du parcours de toutes les pièces, si un nouveau nombre minimal de pièces est trouvé pour la pièce ```p```, il faut rajouter la pièce ```p``` à la liste des solutions.

    Compléter la fonction ```rendu_solution``` qui prend en paramètres une liste de pièces ```pieces``` et la somme à rendre ```somme``` et qui renvoie **le nombre minimal** de pièces qu'il faut rendre.   

    ```python linenums='1'
    def rendu_solution(pieces, somme):
        rendu = {0:0}
        solution = {}
        solution[0] = []
        for s in range(1, somme+1):
            rendu[s] = s
            solution[s] = []
            for p in pieces:
                if p >> rendu_solution([1,6,10], 12)
[6, 6]
>>> rendu_solution([1,6,10], 107)
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 6, 1]
```

### 1.1 Simple et inefficace

Comme nous l'avons déjà vu ici,
la suite de Fibonacci définie par :

- $F_0 = 0$
- $F_1 = 1$
- $\forall n \in \mathbb{N}, F_{n+2} = F_{n+1}+F_n$

se programme récursivement par :

```python linenums='1'
def fibo(n):
    if n == 0 :
        return 0   
    elif n == 1 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
```

Ce code, d'une grande simplicité, est malheureusement très inefficace.

    Mesurer le temps de calcul de ```fibo(40)```.

     

En cause : la multitude des appels récursifs nous conduit à refaire des calculs déjà effectués.

Observons l'arbre d'appels de ```fibo(6)``` :

Le calcul de ```fibo(2)``` se retrouve ainsi 5 fois dans l'arbre.

Pour résoudre notre problème, nous l'avons divisé en problèmes plus petits, mais malheureusement pas indépendants. Une approche par diviser pour régner est donc impossible.

On dit que les problèmes se **recouvrent**, ce qui nous amène à refaire des choses déjà faites. 

Dans l'algorithme de dichotomie, ou du tri-fusion, les problèmes étaient indépendants et ne se recouvraient pas : on ne refaisait jamais deux fois la même chose. Ce n'est pas le cas ici.

### 1.2 Se souvenir des belles choses des calculs : la mémoïsation

Comment éviter de recalculer (par exemple) 5 fois ```fibo(2)``` ? En se souvenant que nous l'avons déjà calculé !

L'idée générale est donc de stocker le résultat de chaque calcul, par exemple dans un dictionnaire. Ainsi, à chaque demande de calcul :

- Soit le calcul a déjà été effectué : on a donc juste à le lire dans le dictionnaire.
- Soit le calcul n'a jamais été effectué : on l'effectue, et **on stocke le résultat dans le dictionnaire**.

    Compléter le code suivant :

    ```python linenums='1'
    dict_fibo = {0:0, 1:1}
    def fibo(n):
        if n in dict_fibo:
            return ...
        dict_fibo[n] = ... + ...
        return ...
    ```

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        dict_fibo = {0:0, 1:1}
        def fibo(n):
            if n in dict_fibo:
                return dict_fibo[n]
            dict_fibo[n] = fibo(n-1) + fibo(n-2)
            return dict_fibo[n]
        ```        
    """
    )
    }}

    ```python linenums='1'
    dict_fibo = {0:0, 1:1}
    def fibo(n):
        if n in dict_fibo:
            return dict_fibo[n]
        dict_fibo[n] = fibo(n-1) + fibo(n-2)
        return dict_fibo[n]
    ```
    :warning: le dictionnaire ```dict_fibo``` doit être **à l'extérieur** de la fonction, sinon il est réinitialisé à chaque appel récursif !

    Mesurer le temps de calcul de ```fibo(40)``` et comparer avec la mesure de l'exercice 1.

    {{
    correction(True,
    """
\"Correction\" 
        Le temps de calcul est maintenant de l'ordre de $10^{-5}$ secondes. C'est un million (!!!) de fois plus rapide que le code de l'exercice 1.
    """
    )
    }}

### 1.3 Quelques remarques

#### 1.3.1 :arrow_right: **Juste une brute-force plus efficace ?**

Notre technique de mémoïsation ne change pas vraiment la structure du programme : on continue de calculer toutes les valeurs intermédiaires, **mais on ne les calcule qu'une seule fois.**

#### 1.3.2 :arrow_right: **Suppression de la variable globale**

Dans le code précédent, le dictionnaire ```dict_fibo``` est à l'extérieur de la fonction. Un dictionnaire étant un type mutable, sa modification à l'intérieur de la fonction ne pose pas de problème. Toutefois, ce genre de pratique est déconseillé : si par exemple on appelle 2 fois la fonction ```fibo```, le dictionnaire n'est pas réinitialisé entre-temps (ce qui dans notre cas n'est pas problématique, mais cela pourrait l'être). Comment éviter cela ?

On peut utiliser une fonction *englobante* (appelée ici ```fibonacci``` ) :

```python linenums='1'
def fibonacci(n):
    dict_fibo = {0:0, 1:1}
    def fibo(n):
        if n in dict_fibo:
            return dict_fibo[n]
        dict_fibo[n] = fibo(n-1) + fibo(n-2)
        return dict_fibo[n]
    return fibo(n)
```

```python
>>> fibonacci(50)
12586269025
```

Remarquez la définition d'une fonction *à l'intérieur* d'une autre. Cela ne pose aucun problème, mais attention, cette fonction n'existe pas à l'extérieur de sa fonction englobante.

#### 1.3.3 :arrow_right: **Mémoïsation automatique en Python** *(HP)* :star: :star: :star:

La fonction ```lru_cache``` du module ```functools``` permet de mémoïser automatiquement une fonction récursive. Il suffit, juste avant d'écrire la fonction, de mettre la ligne ```@lru_cache``` (appelée *décorateur*). 

```python linenums='1'
import time
from functools import lru_cache

@lru_cache  #(1)
def fibo(n): #(2)
    if n == 0 :
        return 0   
    elif n == 1 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
    
t0 = time.time()
fibo(35)
print(time.time() - t0)
```

1. «décorateur» de la fonction
2. Ceci est notre VIEILLE fonction ```fibo```, extrêmement lente...

Essayez en commentant / décommentant la ligne 4... c'est magique !

### 1.4 De bas en haut

La structure récursive naturelle de la suite de Fibonacci nous a conduit vers un programme qui calcule (ou plutôt *appelle*) les valeurs *de haut en bas*. (méthode *top-down*)

Et si on commençait par le bas ?

C'est en fait ce que nous faisons naturellement : si nous devions calculer mentalement le 6ème terme de la suite de Fibonacci, on commencerait par calculer le 3ème, puis le 4ème, puis le 5ème et enfin le 6ème.

    Compléter le code ci-dessous :

    ```python linenums='1'
    def fibo(n):
        dict_fibo = {}
        dict_fibo[0] = ...
        dict_fibo[1] = ...
        for k in range(..., ...):
            dict_fibo[k] = dict_fibo[...] + dict_fibo[...]
        return dict_fibo[...]
    ```

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        def fibo(n):
            dict_fibo = {}
            dict_fibo[0] = 0
            dict_fibo[1] = 1
            for k in range(2, n+1):
                dict_fibo[k] = dict_fibo[k-1] + dict_fibo[k-2]
            return dict_fibo[n]
        ```        
    """
    )
    }}

Cette méthode itérative part du bas pour aller vers le haut. On parle de méthode *bottom-up*. 
De manière plus générale, cette méthode est basée sur le fait de résoudre des problèmes de petite taille, puis de plus en plus gros, jusqu'au problème final.

### 1.5 Bilan des méthodes employées

- Lors d'un calcul effectué de manière récursive, il peut arriver que de multiples appels récursifs soient identiques. Pour éviter de recalculer plusieurs fois la même chose, on peut stocker les résultats intermédiaires. On appelle cette technique la **mémoïsation**.  
    Cette technique minimise le nombre d'opérations et accélère grandement l'exécution du programme. Le prix à payer est l'utilisation d'une structure de stockage des valeurs intermédiaires, et donc une augmentation de la mémoire utilisée par le programme.

    - Lors d'un calcul effectué de manière itérative, il est parfois plus simple de commencer par une «petite» version du problème pour progressivement remonter vers la solution du problème global.

### 2.1 Optimisation d'une somme dans une pyramide

Considérons la pyramide ci-dessous :

    

    En partant du sommet et en descendant soit à gauche soit à droite, quel chemin donne la somme maximale en arrivant en bas ?

    

La suite : TP Pyramides

### 2.2 Problème du plus grand carré blanc

Considérons l'image ci-dessous :

    

    Quel est la taille du plus grand carré entièrement blanc qu'on puisse dessiner à l'intérieur de cette image ?

La suite : TP Plus Grand Carré Blanc

### 2.3 Optimisation du rendu de monnaie

Étant donnés une liste de pièces ```pieces``` et une somme à rendre ```somme```, peut-on calculer le nombre minimal de pièces pour réaliser cette somme ?

La suite : TP Rendu de monnaie

### Introduction

Exercice 1 du sujet 0 - version B 2024

    

    

    

    {{
    correction(False,
    """
\"Correction Q4.\" 
        Pour une pyramide de $n$ niveaux, il va y avoir $n-1$ choix de direction (droite ou gauche). Cela revient donc à écrire un mot binaire composé de $n-1$ chiffres (0 ou 1).

        Or le nombre de mots binaires de longueur $n-1$ est égal à $2^{n-1}$ donc une pyramide de n niveaux comportera $2^{n-1}$ conduits.
    """
    )
    }}

    

    

    

    

    

    {{
    correction(False,
    """
\"Correction Q10.\" 
        On pourrait utiliser la mémoïsation pour éviter la redondance des calculs, par exemple en utilisant un dictionnaire de clés ```(i,j)``` pour stocker les ```score_max(i,j,p)```.
       
        Exemple de code (non demandé) :
        ```python linenums='1'
        memo = {}
        def score_max(i, j, p):
            if i == len(p) - 1:
                return p[len(p)-1][j]
            if (i, j) not in memo:
                memo[(i,j)] = p[i][j] + max(score_max(i+1, j, p), score_max(i+1, j+1, p))
            return memo[(i,j)]
        ```

        
    """
    )
    }}

    *Largement inspiré du sujet 24.2 de la BNS 2024.*

    On considère un tableau non vide de nombre entiers, positifs ou négatifs, et on souhaite déterminer
    la plus grande somme possible de ses éléments consécutifs.

    Par exemple, dans le tableau `[1, -2, 3, 10, -4, 7, 2, -5]`, la plus grande
    somme est 18 obtenue en additionnant les éléments 3, 10, -4, 7, 2.

    Pour cela, on va résoudre le problème par programmation dynamique. 

    Le problème sera résolu en 2 temps.

    Dans un premier temps, si on note `tab` le
    tableau considéré et `i` un indice dans ce tableau, on va chercher à déterminer la plus grande somme possible de ses éléments consécutifs se terminant à
    l’indice `i`.
    Voici la méthode :

    Si on connait la plus grande somme possible de ses éléments consécutifs se terminant à
    l’indice `i-1`, on peut déterminer la plus grande somme possible de ses éléments consécutifs
    se terminant à l’indice `i` :

    - soit on obtient une plus grande somme en ajoutant `tab[i]` à cette somme précédente ;
    - soit on commence une nouvelle somme à partir de `tab[i]`.

    Dans un deuxième temps, il suffira de parcourir le tableau pour chercher la somme maximale d'éléments consécutifs.

    Compléter la fonction `somme_max` ci-dessous qui réalise cet algorithme.

    ```python linenums='1'
    def somme_max(tab):
        n = len(tab)
        sommes_max = [0]*n
        sommes_max[0] = tab[0]
        # on calcule la plus grande somme se terminant en i
        for i in range(1,n):
            if ... + ... > ...: 
                sommes_max[i] = ... 
            else:
                sommes_max[i] = ... 
        # on en déduit la plus grande somme de celles-ci
        maximum = 0
        for i in range(1, n):
            if ... > ...: 
                maximum = i

        return sommes_max[...] 
    ```

    Exemples :

    ```python
    >>> somme_max([1, 2, 3, 4, 5])
    15
    >> somme_max([1, 2, -3, 4, 5])
    9
    >>> somme_max([1, 2, -2, 4, 5])
    10
    >>> somme_max([1, -2, 3, 10, -4, 7, 2, -5])
    18
    ```

### Programmation dynamique

Terminale - Spécialité NSI IFS Singapour
Chapitre 22 - Programmation dynamique
Objectifs :
▷ Utiliser la programmation dynamique pour écrire un algorithme.
▷ Comprendre les exemples du rendu de monnaie et de l'alignement de séquences.
▷ Comparer un algorithme de force brute, un algorithme glouton et un algorithme en programmation dy-
namique sur le problème du rendu de monnaie.
▷ Montrer les conséquences sur le coût en mémoire des algorithmes de programmation dynamique
1 Introduction
On dispose de la grille2 × 3 ci-dessous.
Question : Combien de chemins mènent du coin supérieur gauche au coin inférieur droit, en se déplaçant
uniquement le long des traits horizontaux vers la droite et le long des traits verticaux vers le bas?
Et pour une grille10 × 10?
2 Principe de la programmation dynamique
La programmation dynamique est une technique créée parRichard Bellman dans les années 1950. À l'origine,
cette méthode algorithmique était utilisée pour résoudre des problèmes d'optimisation.
Repères historiques
Richard Bellman est un mathématicien américain, travaillant principalement dans la branche des ma-
thématiques appliquées. Il est l'inventeur de laprogrammation dynamique, qui résolut à son époque
de façon inespérée l'optimisation des sommes de fonctions monotones croissantes sous contraintes.
Le terme programmation désigne laplanification, et n'a pas de rapport avec les langages de programmation.
A retenir!
L'idée générale est de déterminer un résultat sur la base de calculs précédents.
Plus précisément, la programmation dynamique consiste à résoudre un problème :
— en ledécomposant en sous-problèmes,
— puis àrésoudre les sous-problèmesdes plus petits au plus grands
— en stockant les résultats intermédiaires.
3 La suite de Fibonacci
3.1 Rappels
On a déjà abordé cette suite lorsque nous avons parlé de la programmation récursive (Chapitre 1).
La suite de Fibonnacciest une suite de nombres dont chacun est la somme des deux précédents. Le premier
et le second nombres sont égaux à 0 et 1 respectivement.
T. Rahobisoa 1/7 ALGO02 - Programmation dynamique
Terminale - Spécialité NSI IFS Singapour
On obtient la suite de nombres :0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 ..., etc.
Mathématiquement, cette suite notéeFn est définie par :



F0 = 0
F1 = 1
Fn = Fn−1 + Fn−2 pour tout entiern ≥ 2
3.2 Version récursive naïve (et inefficace)
Nous avons déjà programmé une version récursive qui renvoie le terme de rangn de cette suite.
1 def fib ( n ) :
2 """ Version re cu rs iv e naive """
3 if n <= 1:
4 return n
5 else :
6 return fib (n -1) + fib (n -2)
Par exemple, voici l'arbre des appels récursifs si on lancefibo(5).
fib(5)
fib(4)
fib(3)
fib(2)
fib(1) fib(0)
fib(1)
fib(2)
fib(1) fib(0)
fib(3)
fib(2)
fib(1) fib(0)
fib(1)
On se rend compte qu'il y a beaucoup d'appels redondants:
— fib(1) a été lancé 5 fois,
— fib(2) a été lancé 3 fois,
— etc.
Ces redondances entraînent un nombre d'appels récursifs qui explose rapidement dès quen est élevé. Par
conséquent, les temps de calcul deviennent vite très élevés. Pire, dès quen est trop grand, l'algorithme ne
donnera jamais la réponse.
Par exemple, en utilisant un programme principal qui calcule et affiche le temps d'exécution :
1 s t a r t _ t i m e = time . time () # Debut du c h r o n o m e t r e
2 fib (25) # Code a mesurer
3 end_time = time . time () # Fin du c h r o n o m e t r e
4
5 e x e c u t i o n _ t i m e = end_time - s t a r t _ t i m e # Calcul du temps ecoule
6 print ( " Temps d ' e xe cu ti on : " , execution_time , " secondes " )
On obtient :
— si on exécutefibo(25), temps d'exécution :30 ms
— si on exécutefibo(35), temps d'exécution :3.62 s
— si on exécutefibo(40), temps d'exécution :36.77 s
T. Rahobisoa 2/7 ALGO02 - Programmation dynamique
Terminale - Spécialité NSI IFS Singapour
A retenir!
Il est possible de faire mieux, en évitant de refaire les calculs déjà effectués.
Pour cela, il fautstocker les résultats intermédiaires!
3.3 Version récursive avec mémoïsation
Une première approche est d'adapter l'algorithme récursif en stockant les résultats calculés dans un
tableau ou un dictionnaire.
Lors d'un appel, on commence par vérifier si on ne connaît pas déjà la réponse, auquel cas on la renvoie
directement, ce qui évite d'effectuer descalculs redondants.
Cela donne la fonctionfibo_memo suivante qui prend en paramètres un entiern et un dictionnaire memo que
l'on met à jour en stockant les résultats intermédiaires au fur et à mesure.
1 def fi bo _m em o (n , memo ) :
2 if n in memo : # si calcul deja effectue
3 return memo [ n ] # on renvoie d i r e c t e m e n t sa valeur
4 elif n <= 1:
5 memo [ n ] = n
6 return memo [ n ]
7 else :
8 memo [ n ] = fi bo _m em o (n -1 , memo ) + fi bo _m em o (n -2 , memo )
9 return memo [ n ]
Explications :
— Lignes 2 et 3 :si la valeur n est déjà dans le dictionnaire, c'est qu'on a déjà calculéFn et il suffit alors
de renvoyer sa valeurmem[n] (la valeur associée àn).
— Lignes 4 à 9 :quasiment identiques à la version récursive naïve à ceci près que l'on mémorise la valeur
dans le dictionnairememo avant de la renvoyer.
— De cette façon, dès qu'une valeurFn a été calculée, elle est ajoutée dans le dictionnaire comme la valeur
associée à n, ce qui permet de la réutiliser directement dès qu'on en a besoin.
Il n'y a plus qu'à lancer le premier appel avec un dictionnaire vide, c'est ce que fait la fonction fibo suivante.
1 def fibo ( n ) :
2 """ Version re cu rs iv e avec m e m o i s a t i o n """
3 F = {}
4 return fi bo _m em o (n , F )
Avec ceprocédé de mémoïsation, l'arbre des appels est considérablement réduit puisqu'il n'y a plus aucun
appel redondant.
Par exemple, l'arbre des appels récursifs en lançantfibo(5) se réduit à :
fib(5)
fib(4)
fib(3)
fib(2)
fib(1) fib(0)
fib(1)
fib(2)
fib(3)
fib(2)
fib(1) fib(0)
fib(1)
T. Rahobisoa 3/7 ALGO02 - Programmation dynamique
Terminale - Spécialité NSI IFS Singapour
On constate alors qu'avec cette version, les valeursFn sont calculées quasiment instantanément et que l'on peut
obtenir les valeursFn pour des grandes valeurs den.
On obtient :
— si on exécutefibo(25), temps d'exécution :0 ns
— si on exécutefibo(100), temps d'exécution :18.57 ns
— si on exécutefibo(850), temps d'exécution :2.04 ms
La méthode descendante
La version récursive avec mémoïsation correspond à une approche descendante, aussi appelée
haut-bas (ou top-down en anglais).
En effet, pour connaîtreFn , on lance l'appelfibo(n) qui déclenche ladescente d'appels récursifs
jusqu'aux cas de base pour lesquels on mémorise les résultats.
Dans un second temps, on remonte les appels tout en mémorisant leurs résultats pour ne pas résoudre
plusieurs fois le même problème.
Finalement, avec cette méthode, c'est lors de laremontée des appelsque leurs résultats sont mémorisés puis
réutilisés sur les problèmes plus grands. On peut alors se demander si on ne peut pas procéder directement du
plus petit sous-problème au plus grand (celui que l'on veut résoudre).
La réponse est oui! Une autre manière de résoudre le problème est d'utiliser uneapproche ascendante.
3.4 Version itérative ascendante
On parle aussi deméthode bas-haut, oubottom-up en anglais.
Il s'agit d'une méthode itérative dans laquelle on commence par calculer des solutions pour les sous-problèmes
les plus petis puis, de proche en proche, on arrivera à la taille voulue. Comme précédemment, on utilise le
principe de la mémoïsation pour stocker les résultats partiels.
Le calcul du termeFn de la suite de la Fibonacci n'est pas un problème d'optimisation, ainsi le calcul d'une
solution d'un problème à partir des solutions connues des sous-problèmes est simple puisqu'il n'y a aucun choix
à faire.
De manière générale, on utilise un tableau pour stocker les résultats au fur et à mesure.
T. Rahobisoa 4/7 ALGO02 - Programmation dynamique
Terminale - Spécialité NSI IFS Singapour
La méthode ascendante
Voici les étapes habituelles :
1. Création et initialisation du tableau :
— On a besoin d'un tableauF de taille n+1 qui va contenir les valeursF0, F1, ...,Fn dans cet
ordre.
— Pour cela on crée le tableau F avecn+1 zéros initialement.
— On peut stocker les valeurs déjà connues (F0 et F1 dans notre cas)
2. Utilisation de la formule de récurrence pour remplir le reste du tableau :
— La formule de récurrence donne la solution d'un sous-problème à partir de celles de sous-
problèmes plus petits et donc déjà traités! Ici on a pour2 ≤ i ≤ n : Fi = Fi−1 + Fi−2
— On peut donc remplir le tableau F en parcourant les indicespar ordre croissant: on va
mettre dans F[i] la valeur F[i-1] + F[i-2] que l'on connaît puisque ces deux valeurs ont
été calculés précédemment.
3. Le résultat est dans la dernière case du tableau : on la renvoie!
Cela donne la fonction suivante :
1 def fibo ( n ) :
2 """ Version it er at iv e a s c e n d a n t e """
3 F = [0]*( n +1)
4 F [0] = 0 # pas i n d i s p e n s a b l e car deja i n i t i a l i s e a 0
5 F [1] = 1
6 for i in range (2 , n +1) :
7 F [ i ] = F [i -1] + F [i -2]
8 return F [ n ]
Les performances sont semblables à la version récursive avec mémoïsation
On obtient, si on exécutefibo(850), un temps d'exécution :0 ns
3.5 Autres problèmes
Il existe de nombreux problèmes pouvant être résolus avec leparadigme de la programmation dynamique,
dont beaucoup de problèmes d'optimisation :
▷ problème du rendu de monnaie
▷ problème du sac-à-dos
▷ alignement de séquences
▷ problème du plus court chemin (algorithme deBellman-Ford utilisé par le protocole RIP)
▷ problèmes d'ordonnancement d'intervalles pondérés
▷ toutes sortes de problème d'affectation des ressources, ...,etc.
T. Rahobisoa 5/7 ALGO02 - Programmation dynamique
Terminale - Spécialité NSI IFS Singapour
4 Conclusion
▷ La programmation dynamique est une technique permettant d'améliorer l'efficacité d'un algorithme
en évitant lescalculs redondants.
▷ Pour cela, on utilise un tableau (ou un dictionnaire) pourstocker les résultats intermédiaireset
pouvoir les réutiliser sans les recalculer.
▷ Comme la méthode« diviser pour régner », la programmation dynamique permet résoudre un problème
à partir des solutions de sous-problèmes. Si ces derniers se « chevauchent » (s'ils sont non indépendants)
alors la programmation dynamique permettra d'éviter que les appels récursifs ne soient effectués plusieurs
fois. Ainsi, la programmation dynamique permet souvent d'améliorer des algorithmes récursifs.
A retenir!
Pour utiliser la programmation dynamique, on procède généralement ainsi :
1. définition des sous-problèmes
2. identification d'unerelation de récurrenceentre les solutions des sous-problèmes
3. mise en place d'unalgorithme récursif avec mémoïsationou d'unalgorithme itératif as-
cendant
4. résolution du problème original à partir des solutions des sous-problèmes
La programmation dynamique permet de résoudre de manière efficace de nombreux problèmes d'optimisation,
comme lerendu de monnaieou l'alignement de séquences, pour lesquels une solution récursive classique
est inefficace.
T. Rahobisoa 6/7 ALGO02 - Programmation dynamique
Terminale - Spécialité NSI IFS Singapour
5 Exercices
Exercice 1 :L'alignement de séquences
1. Regarder la vidéo suivante sur la programmation dynamique et l'alignement de séquences et répondre aux
questions ci-dessous dans leGoogle Doc.
2. Donner le principe de base de la programmation dynamique.
3. Dans quel domaine scientifique l'utilisation de la programmation dynamique a connu un grand essor?
4. Quel type de fonction utilise régulièrement la programmation dynamique?
5. Détailler le principe de la recherche de l'alignement de séquences.
6. Reprendrel'algorithmedecalculdela distancede Levenshteinetletesteraveclesséquences information
et informatique.
Exercice 2 :Epreuve pratique 2021 - Sujet n°7 - Ex 1
On s'intéresse à la suite d'entiers définie par :
— U1 = 1,
— U2 = 1,
— et, pour tout entier natureln, par U n + 2 = Un+1 + Un.
Elle s'appelle lasuite de Fibonnaci.
Écrire la fonctionfibonacci qui prend un entiern > 0 et qui renvoie l'élément d'indicen de cette suite.
On utilisera uneprogrammation dynamique(pas de récursivité!).
Exemples :
1 >>> f i bo na cc i (1)
2 1
3 >>> f i bo na cc i (2)
4 1
5 >>> f i bo na cc i (25)
6 75025
7 >>> f i bo na cc i (45)
8 1 1 3 4 9 0 3 1 7 0
Exercice 3 :Le rendu de monnaie
1. Regarder la vidéo suivante sur la programmation dynamique et le problème de rendu de monnaie et
répondre aux questions ci-dessous dans leGoogle Doc.
2. Écrire l'algorithme en Python du rendu de monnaie force brute (et fonction récursive).
3. Dessiner le début de l'arbre des possibilités de rendue de monnaie pour 76 cts. Montrer sur cet arbre qu'il
y a des redondances.
4. Écrire l'algorithme en Python du rendu de monnaie en programmation dynamique.
5. A l'aide de la fonctiontime() de la bibliothèque time de Python, évaluer le temps nécessaire pour votre
ordinateur pour calculer le nombre minimal de pièces à rendre pour la somme de 76 cts à l'aide des deux
algorithmes (questions 2 et 4)
6. Même chose avec 177 cts. Commenter.
T. Rahobisoa 7/7 ALGO02 - Programmation dynamique

## Recherche textuelle

### 1.1 Premier algorithme

codes à trous

{#

    
    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''
        

    ```
#}

    
    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''
        indices = []
        i = 0
        while i >> recherche_naive("une magnifique maison bleue", "maison")
[15]
>>> recherche_naive("une magnifique maison bleue", "nsi")
[]
>>> recherche_naive("une magnifique maison bleue", "ma")
[4, 15]
```

### 1.2 Modification de l'algorithme

Re-écrire l'algorithme précédent en s'arrêtant dès qu'une occurrence de ```motif``` est trouvée dans ```texte```.

    La fonction renverra uniquement un booléen.

### 1.3 Application à la recherche d'un motif dans un roman

Le Projet Gutenberg permet de télécharger légalement des ouvrages libres de droits dans différents formats.

Nous allons travailler avec le Tome 1 du roman _Les Misérables_ de Victor Hugo, à télécharger ici :arrow_down: au format ```txt```. 

#### 1.3.1 Récupération du texte dans une seule chaîne de caractères

```python linenums='1'
with open('Les_Miserables.txt') as f:
    roman = f.read().replace('\n', ' ')
```

#### 1.3.2 Vérification et mesure du temps de recherche

    
    À l'aide du module ```time```, mesurer le temps de recherche dans Les Misérables d'un mot court, d'une longue phrase (présente dans le texte), d'un mot qui n'existe pas. Que remarquez-vous ?

### 2. Vers l'algorithme de Boyer-Moore : et si on partait à l'envers ?

_Vous pouvez contrôler le déroulement de l'animation en la survolant avec la souris._

    Re-écrire l'algorithme de recherche naïve mais en démarrant de la fin du **motif** et non du début. 

    Certes, c'est pour l'instant très artificiel, mais :

### 2.1 Principe

L'idée est d'améliorer le code précédent (celui on parcourt le motif à l'envers) en **sautant** directement au prochain endroit potentiellement valide. 

Pour cela on regarde le caractère ```X```  du texte sur lequel on s'est arrêté (car ```X``` n'était pas égal au caractère de rang équivalent dans le motif):

- si ```X``` n'est pas dans le motif, il est inutile de se déplacer "de 1" : on retomberait tout de suite sur ```X```, c'est du temps perdu. On se décale donc juste assez pour dépasser ```X```.
- si ```X``` est dans le motif, on va regarder la place de la dernière occurence de ```X``` dans le motif et de déplacer de ce nombre, afin de faire coïncider le ```X``` du motif et le ```X``` du texte.

    

    _Vous pouvez contrôler le déroulement de l'animation en la survolant avec la souris._

### 2.2 Implémentation

#### 2.2.1 Fonction préparatoire
On va d'abord coder une fonction ```dico_lettres``` qui prend en paramètre un mot ```mot``` et qui renvoie un dictionnaire associant à chaque lettre de ```mot``` son dernier rang dans ```mot```. On exclut la dernière lettre, qui poserait un problème lors du décalage (on décalerait de 0...) 

    Écrire la fonction ```dico_lettres```.

    *Exemple d'utilisation :*

    ```python
    >>> dico_lettres("MAURIAC")
    {'M': 0, 'A': 5, 'U': 2, 'R': 3, 'I': 4}
    ```

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        def dico_lettres(mot):
            d = {}
            for i in range(len(mot)-1):
                d[mot[i]] = i
            return d
        ``` 
    """
    )
    }}

#### 2.2.2 Boyer-Moore-Horspool
  
codes à trous

{#

    
    ```python linenums='1'
    def dico_lettres(mot):
        

    def BMH(texte, motif):
        

    ```

#}

    
    ```python linenums='1'
    def dico_lettres(mot):
        d = {}
        for i in range(len(mot)-1):
            d[mot[i]] = i
        return d

    def BMH(texte, motif):
        dico = dico_lettres(motif)
        indices = []
        i = 0
        while i = 0 and texte[i+k] == motif[k]: #(1)
                k -= 1
            if k == -1: #(2)
                indices.append(i)
                i += 1 #(3)
            else:
                if texte[i+k] in dico: #(4)
                    i += max(k - dico[texte[i+k]], 1) #(5)
                else:
                    i += k+1 #(6)

        return indices

    ```

    1. On remonte le motif à l'envers, tant qu'il y a correspondance et qu'on n'est pas arrivés au début du motif
    2. Si on est arrivés à la valeur ```k=-1```, c'est qu'on a parcouru tout le mot : on l'a donc trouvé.
    3. On a trouvé le motif, mais attention, il ne faut pas trop se décaler sinon on pourrait rater d'autres occurences du motif (pensez à la recherche du motif «mama» dans le mot «mamamamama»). On se décale donc de 1.
    4. On s'est arrêté avant la fin, sur une lettre présente dans le mot : il va falloir faire un décalage intelligent.
    5. On décale juste de ce qu'il faut pour mettre en correspondance les lettres, en faisant attention à ne pas décaler d'un nombre négatif. Au pire, on décale de 1.
    6. La lettre n'est pas dans le motif : on se positionne juste après elle.

   
Exemple d'utilisation :
```python
>>> BMH("une magnifique maison bleue", "maison")
[15]
>>> BMH("une magnifique maison bleue", "nsi")
[]
>>> BMH("une magnifique maison bleue", "ma")
[4, 15]
```

    

    Reprendre les mesures effectuées sur Les Misérables, mais cette fois avec l'algorithme BMH. Que remarquez-vous ?  

    
    {{
    correction(True,
    """
\"Correction\" 
        ```python
        import time

        with open('Les_Miserables.txt') as f:
            roman = f.read().replace('\\n', ' ')

        def dico_lettres(mot):
            d = {}
            for i in range(len(mot)-1):
                d[mot[i]] = i
            return d

        def BMH(texte, motif):
            dico = dico_lettres(motif)
            indices = []
            i = 0
            while i = 0 and texte[i+k] == motif[k]: 
                    k -= 1
                if k == -1: 
                    indices.append(i)
                    i += 1
                else:
                    if texte[i+k] in dico: #(4)
                        i += max(k - dico[texte[i+k]], 1) 
                    else:
                        i += k+1 

            return indices

        t0 = time.time()
        motif = 'maison'
        print(BMH(roman, motif))
        print(time.time()-t0)

        t0 = time.time()
        motif = 'La chandelle était sur la cheminée et ne donnait que peu de clarté.'
        print(BMH(roman, motif))
        print(time.time()-t0)

        t0 = time.time()
        motif = 'parcoursup'
        print(BMH(roman, motif))
        print(time.time()-t0)
        ```

        retour console :

        ```python
        [7264, 9090, 9547, 9745, 10936, 17820, 23978, 38192, 41639, 41651, 41840, 42493, 48028, 48393, 51448, 53353, 70867, 72692, 72768, 75608, 77855, 108489, 115739, 130629, 132983, 138870, 143681, 144600, 153114, 155973, 158709, 160700, 163649, 169164, 169181, 171761, 171967, 182642, 186413, 190534, 219378, 220314, 224518, 225098, 227579, 296302, 345108, 345893, 346740, 349677, 359727, 362025, 389945, 395690, 434118, 438068, 457795, 457886, 464696, 469403, 501768, 514980, 520667, 520878, 520926, 520968, 522707, 529329, 598128, 601390, 645915]
        0.06359553337097168
        [651731]
        0.01853322982788086
        []
        0.037064313888549805
        ```

        On constate quelque chose de remarquable (et qui peut être à première vue contre-intuitif) : 

        **Plus le motif recherché est long, plus la recherche est rapide**.        
    """
    )
    }}

### Introduction

Questions 14 et 15 de l'exercice 3 du Sujet Métropole Septembre 2025

    ```python linenums='1'
    def recherche_seq(seq, chaine):
        """Renvoie l'indice du premier caractère de
        chaine où commence `seq` si la séquence `seq`
        se trouve dans la chaine de caractères chaine,
        -1 sinon
        Paramètres:
        seq : séquence à rechercher
        chaine : chaine d'ADN
        Renvoie:
        indice du premier caractère de seq dans
        la chaine, -1 sinon.
        """
        for i in range(len(chaine)-len(seq) + 1):
            j = 0
            while j < len(seq) and ...:
                j += 1
            if ...:
                return i
        return -1
    ```

### Vers Boyer-Moore-Horspool

L'idée est d'améliorer le code précédent (celui on parcourt le motif à l'envers) en **sautant** directement au prochain endroit potentiellement valide. 

Pour cela on regarde le caractère ```X```  du texte sur lequel on s'est arrêté (car ```X``` n'était pas égal au caractère de rang équivalent dans le motif):

- si ```X``` n'est pas dans le motif, il est inutile de se déplacer "de 1" : on retomberait tout de suite sur ```X```, c'est du temps perdu. On se décale donc juste assez pour dépasser ```X```.
- si ```X``` est dans le motif (sauf à la dernière place du motif !), on va regarder la place de la dernière occurence de ```X``` dans le motif et de déplacer de ce nombre, afin de faire coïncider le ```X``` du motif et le ```X``` du texte.

    

    _Vous pouvez contrôler le déroulement de l'animation en la survolant avec la souris._

On dispose de la fonction ```dico_lettres``` :
```python linenums='1'
def dico_lettres(mot):
    d = {}
    for i in range(len(mot)-1):
        d[mot[i]] = i
    return d
```

*Exemple d'utilisation de la fonction ```BMH``` :*

```python
>>> BMH("une magnifique maison bleue", "maison")
[15]
>>> BMH("une magnifique maison bleue", "nsi")
[]
>>> BMH("une magnifique maison bleue", "ma")
[4, 15]
```

    ```python linenums='1'
    def dico_lettres(mot):
        d = {}
        for i in range(len(mot)-1):
            d[mot[i]] = i
        return d

    def BMH(texte, motif):

    ```
 
    ```python linenums='1'
    def dico_lettres(mot):
        d = {}
        for i in range(len(mot)-1):
            d[mot[i]] = i
        return d

    def BMH(texte, motif):
        dico = ...
        indices = ...
        i = ...
        while ...:
            k = ...
            while ...: 
                ...
            if ...: 
                ...
                ...
            else:
                if ...: 
                    ...
                else:
                    ... 

        return ...

    ```

    ```python linenums='1'
    def dico_lettres(mot):
        d = {}
        for i in range(len(mot)-1):
            d[mot[i]] = i
        return d

    def BMH(texte, motif):
        dico = ...
        indices = ...
        i = ...
        while i = 0 and texte[...] == motif[...]: 
                k = ...
            if k == ...: 
                indices.append(...)
                i = ...
            else:
                if ... in dico: 
                    i += max(..., 1) 
                else:
                    i += ...

        return ...

    ```

### Vers la recherche textuelle naïve

Écrire une fonction ```recherche_naive``` qui prend en paramètres deux chaines de caractères ```texte``` et ```motif``` et qui renvoie la liste des indices (éventuellement vide) des occurrences de la chaîne `motif` dans la chaîne `texte`.

Exemple d'utilisation :
```python
>>> recherche_naive("une magnifique maison bleue", "maison")
[15]
>>> recherche_naive("une magnifique maison bleue", "nsi")
[]
>>> recherche_naive("une magnifique maison bleue", "ma")
[4, 15]
```

    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''

                           
    ``` 
 
    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''
        indices = ...
        i = ...
        while ...:
            ...
            while ...:
                ...
            if ...:
                ...
            ...

        return ...
                         
    ``` 

    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''
        indices = ...
        i = ...
        while i <= ...:
            k = ...
            while k < ... and ...:
                ...
            if ...:
                indices.append(...)
            i += ...

        return ...
                           
    ``` 

    ```python linenums='1'
    def recherche_naive(texte, motif):
        '''
        renvoie la liste des indices (éventuellement vide) des occurrences de
        de la chaîne `motif` dans la chaîne `texte`.
        '''
        indices = []
        i = 0
        while i <= ... - ...:
            k = ...
            while k < len(...) and texte[...] == motif[...]:
                k += ...
            if k == len(...):
                indices.append(...)
            i += ...

        return ...
                            
    ```

### Recherche textuelle

Terminale - Spécialité NSI IFS Singapour
Chapitre 23 - Recherche textuelle
Objectifs :
▷ Comprendre le principe de la recherche textuelle.
▷ Etudier l'algorithme deBoyer-Moore pour la recherche d'un motif dans un texte.
1 Introduction
Tout logiciel de traitement de texte possède une fonction de recherche textuelle, permettant de trouver un mot
ou une partie d'un mot (chaîne ou sous-chaîne). Il en est de même pour les navigateurs Internet.
Ainsi, le raccourci clavierCTRL+F permet de rechercher dans la page la chaine"mot".
Les algorithmes qui permettent de trouver unesous-chaîne de caractères dans une chaine de caractères plus
grande sont des "grands classiques" de l'algorithmique. On parle aussi de recherche d'unmotif dans un texte.
Voici un exemple. Soit le texte suivant :
"Les sanglots longs des violons de l'automne blessent mon coeur d'une langueur monotone. Tout suffocant et
blême, quand sonne l'heure, je me souviens des jours anciens et je pleure."
Question :le motif"vio" est-il présent dans le texte ci-dessus, si oui, en quelle(s) position(s)? La numérotation
d'une chaîne de caractères commence à0 et les espaces sont considérés comme des caractères.
Réponse :on trouve le motif"vio" en position23
La recherche de sous-chaîne dans une chaîne donnée est un problème important de l'informatique, puisque ses
applications sont nombreuses :
— pour lesmoteurs de recherches,
— pour l'utilisation des outils de recherche dans lestraitements de textesou navigateurs web,
— dans le domaine debio-informatique, pour la recherche de séquences données de nucléotides.
T. Rahobisoa 1/8 ALGO03 - Recherche textuelle
Terminale - Spécialité NSI IFS Singapour
2 La bio-informatique
Comme son nom l'indique, la bio-informatique est issue de la rencontre de l'informatique et de labiologie.
La récolte des données en biologie a connu une très forte augmentation ces 30 dernières années.
Pour analyser cette grande quantité de données de manière efficace, les scientifiques ont de plus en plus recourt
au traitement automatique de l'information, c'est-à-dire à l'informatique.
2.1 Analyse de l'ADN
Comme vous le savez déjà, l'information génétique présente dans nos cellules est portée par les molécules d'ADN.
Les molécules d'ADN sont, entre autres, composées de bases azotées ayant pour noms :
— Adénine (représenté par unA)
— Thymine (représenté par unT)
— Guanine (représenté par unG)
— Cytosine (représenté par unC)
L'information génétique est donc très souvent représentée par de très longues chaines de caractères, composées
des caractèresA, T, G et C. Exemple :CTATTCAGCAGTC...
Il est souvent nécessaire de détecter la présence de certains enchainements de bases azotées.
Par exemple, on peut se poser les questions suivantes :
— Trouve-t-on le tripletACG dans le brin d'ADN suivant?
— Si c'est le cas, en quelle position?
CAAGCGCACAAGACGCGGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGG
TTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCG
CAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAA
TAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTTGCTGTATGTTCCATGGTGGCCAATC
CGTCTCTTTTCGACAGCACGGCCAATTCTCCTAGGAAGCCAGCTCAATTTCAACGAAGTCGGCTGTTGAACAGCGAG
GTATGGCGTCGGTGGCTCTATTAGTGGTGAGCGAATTGAAATTCGGTGGCCTTACTTGTACCACAGCGATCCCTTCC
CACCATTCTTATGCGTCGTCTGTTACCTGGCTTGGCAT
Nous allons commencer par le premier algorithme qui nous vient à l'esprit : l'algorithme naïf.
T. Rahobisoa 2/8 ALGO03 - Recherche textuelle
Terminale - Spécialité NSI IFS Singapour
3 La recherche naïve
Un premier algorithme dit"naïf" qui utilise uneméthode itérative brutepermet de rechercher une sous-
chaine dans une chaine de caractères en parcourant le texte de gauche à droite. Il faut avancer dans le texte
caractère par caractère, puis si le caractère considéré correspond au premier caractère du mot, on comparera
les caractères suivants à ceux du mot.
3.1 Algorithme
Algorithme 1 :Fonction recherche_naive(texte, motif)
Entrées :Texte et Motif
Sortie : Liste des positions
m← longueur du motif // Longueur du motif
n← longueur du texte−m + 1 // Indice max de recherche
positions← [] // Liste des positions
pour i variant de 0 à n
si motif = texte[i...i + m] alors
ajouter i à la listepositions
fin
return positions
3.2 Exemple 1
L'une des citations les plus connues du chimiste et philosopheAntoine Laurent de Lavoisierest la suivante :
"rien ne se perd, rien ne se crée, tout se transforme".
Cherchons la chaine"rien" dans le texte de cette citation.
Le motif est trouvé dans le texte à deux reprises, on rajoute les index (0 et 17) à la liste des index puis on le
décale d'un cran vers la droite.
La recherche se termine lorsqu'on atteint le rang :longueur du texte - longueur du motif
3.3 Exemple 2
T. Rahobisoa 3/8 ALGO03 - Recherche textuelle
Terminale - Spécialité NSI IFS Singapour
Par exemple, on cherche la séquenceACG dans le brin d'ADN ci-dessus :
Déroulé (étape par étape)
1. On place le motif recherché au même niveau que les 3 premiers caractères de notre chaine, le
premier élément du motifne correspond pasau premier élément de la chaine (A et C), on décale
le motif d'un cran vers la droite.
2. Le premier élément du motifcorrespond au premier élément de la chaine (A et A) maispas le
second (C et A), on décale d'un cran vers la droite.
3. Le premier élément du motifcorrespond au premier élément de la chaine (A et A) maispas le
second (C et G), on décale d'un cran vers la droite.
4. Le premier élément du motifne correspond pasau premier élément de la chaine (A et G), on
décale d'un cran vers la droite.
5. Le premier élément du motifne correspond pasau premier élément de la chaine (A et C), on
décale d'un cran vers la droite.
6. On continue le processus jusqu'au moment où les 3 éléments du motif correspondent avec les 3
éléments de la chaine situés au même niveau.
Visualiser étape par étape le document suivant présentant l'algorithme naïf sur un autre exemple d'ADN.
3.4 Coût de l'algorithme naïf
Cet algorithme naïf, selon les situations, peut demander untrès grand nombre de comparaisons, ce qui
peut entraîner un très long temps de calcul avec des chaines très longues.
On suppose que l'on a une chaine de longueurN et un mot de longueurn.
L'exécution est relativementlente, la fonction doit testerN-n positions dans la chaine et pour chacune effectuer
jusqu'à n comparaisons.
La complexité de cet algorithme est donc dans le pire des casO((N− n)× n), soit O(n2), c'est-à-dire une
complexité quadratique.
Nous allons voir que l'algorithme deBoyer-Moorepermet de faire mieux en termes de comparaisons à effectuer.
Il est beaucoup plus efficace en utilisant la recherche à l'envers à partir de la fin du mot.
4 L'algorithme de Boyer-Moore-Horspool
Robert S. Boyeret J. Strother Mooresont connus pour leur contribution majeure à l'élaboration de l'algorithme
de rechercheBoyer-Moore. Diplômés de l'Université de Berkeleyen Californie, ces chercheurs ont marqué l'his-
toire avec leur algorithme novateur, publié en 1977 sous le titre"A Fast String Searching Algorithm".
Cette méthode efficace pour trouver toutes les occurrences d'un motif donné dans un texte est devenu un pilier
fondamental dans de nombreux domaines de l'informatique.
Il existe une version simplifiée, développée en 1980 parNigel Horspool, informaticien et professeur émérite à
l'Université de Victoriaen Colombie-Britannique (Canada), que nous allons présenter ici.
T. Rahobisoa 4/8 ALGO03 - Recherche textuelle
Terminale - Spécialité NSI IFS Singapour
L'algorithme deBoyer-Moore-Horspool(simplification de l'algorithme deBoyer-Moore), effectue lavérification
à l'envers, c'est-à-dire en partant non pas du début mais de lafin du motif.
4.1 Le principe
Etapes de l'algorithme
1. On aligne le mot (ou motif, oupattern en anglais) sous la chaine, en partant de la gauche.
2. On compare les lettres du mots avec celles correspondantes de la chaine, mais en partant de la fin
du mot (c'est contre-intuitif).
Trois cas peuvent alors se produire :
— Les lettres du mot et de la chainecorrespondent, on continue alors en remontant le motif de la
droite vers la gauche.
— les lettresne correspondent pas, et la lettre de la chaine n'est pas présente dans le motif. On
va alors décaler le motif vers la gauche d'un nombre de saut égal à sa longueur.
— les lettresne correspondent pas, et lalettre de la chaine est présente dans le motif. On
va alors décaler le motif de manière à faire correspondre la lettre de la chaine à celle du motif.
4.2 Exemple
Prenons un exemple :
Si l'algorithme cherche le motRECURSION dans un texte, il ne teste pas le premier, mais d'abordle dernier
caractère du motif( ici, le 9ème caractère du texte ).
Plusieurs situations peuvent alors se présenter :
1. si on trouve unN (dernier caractère du motif), on regarde si le8ème caractère est unO, puis le 7ème un
I,... jusqu'au 1er.
— Si tous les caractères correspondent, on a trouvé le motif.
— Si les autres caractères ne correspondent pas, on en déduit que le motif ne peut commencer au mieux
qu'en 10ème position du texte : l'algorithme décale le motif d'une longueur complète, et "saute" alors
directement à la18ème position pour rechercher unN.
Le N correspond, mais pas les caractères précédents : le motif ne peut donc se trouver que 9 positions (la
longueur du motif) plus à droite.
2. si on trouve en9ème position une lettre n'apparaissant pas dans le motif : cette situation est similaire à
la précédente, où l'on peut donc aussi décaler le motif d'une longueur complète : ainsi, on ne vérifie qu'un
seul caractère au lieu de dix.
3. si on trouve par exemple unI au lieu d'unN en 9ème position : il se peut que ce soit leI de RECURSION,
auquel cas leN serait 2 positions plus à droite : l'algorithme décale alors le motif de 2 positions pour faire
"coïncider" leI du motif et celui du texte, et recherche alors leN (puis éventuellement leO, leI...).
Dans cet algorithme, le décalage appliqué au motif n'est donc pas de 1 position, mais dépend du caractère
lu : dans le cas deRECURSION, +9 si le caractère est unN ou n'est pas dans le motif,+7 pour unE, +2 pour
un I,..., etc.
Si une même lettre apparaît plusieurs fois dans le motif, on retiendra logiquement le plus petit décalage
(donc celui correspond au caractère le plus à droite du motif ).
T. Rahobisoa 5/8 ALGO03 - Recherche textuelle
Terminale - Spécialité NSI IFS Singapour
L'algorithme décale donc beaucoup plus "vite"le motif vers la droite, et ce d'autant plus que le motif
est long : on arrive donc plus rapidement à la fin du texte, la complexité en temps est bien meilleure que
celle de la recherche naïve.
4. Visualiser sur la démo interactive suivante le fonctionnement de l'algorithme deBoyer-Moore.
5 Exercices
Exercice 1 :Fonctions natives de Python
1. Consulter la documentation de Python sur la méthodefind des chaînes de caractères.
2. Quel est le rôle de cette méthode?
3. Tester cette méthode sur les exemples suivants :
— 'numérique et sciences informatiques'.find('que')
— 'numérique et sciences informatiques'.find('nsi')
Note :Une autre méthode presque identique (str.index) lève une erreur lorsque le motif cherché ne se trouve
pas dans la chaîne.
Exercice 2 :Algorithme naïf
1. Regarder la capsule vidéo suivante (jusqu'à5'44")
2. Résumer le principe de l'algorithme de recherche textuelle naïve.
3. Un outil en ligne permet de visualiser un algorithme dit de "recherche naïve". Utiliser cet outil (en chan-
geant éventuellement le motif et la chaîne).
4. Sansutiliser findouindex,etàpartirdel' algorithme 1ducours,écrireunefonction recherche(motif,chaine)
qui renvoieTrue ou False suivant que la chaîne de caractèresmotif se trouve ou non danschaine.
5. Même question mais en renvoyant l'indice de la première position demotif dans chaine (si elle s'y trouve)
et -1 sinon.
6. Même question mais en renvoyant le nombre d'occurrences demotif trouvées danschaine.
7. Même question mais en renvoyant la liste des indices des occurrences demotif trouvées danschaine.
Exercice 3 :Mesure du nombre d'étapes
Pour répondre aux questions ci-dessous, vous utiliserez les outils interactifs suivants.
On veut rechercher le motifstring dans la chaînestupid_spring_string.
1. Combien d'étapes sont nécessaires avec l'algorithme naïf?
2. Appliquer l'algorithme deBoyer-Moore-Horspoolsur cette recherche. Combien d'étapes sont nécessaires?
3. Faire varier le motif et la chaîne (très longue) et comparer à nouveau le nombre d'étapes pour chacun des
algorithmes. Que peut-on conclure?
Exercice 4 :Mesure du temps de recherche
Le Projet Gutenberg permet de télécharger légalement des ouvrages libres de droits dans différents formats.
Nous allons travailler avec le Tome 1 du romanLes Misérablesde Victor Hugo, à télécharger ici au format.txt.
1. Récupérer le texte dans une seule chaîne de caractères en utilisant le code suivant :
1 with open('Les_Miserables.txt', encoding='utf-8'') as f:
2 roman = f.read().replace('\n', ' ')
2. À l'aide du moduletime, mesurer le temps de recherche dansLes Misérablesd'un mot court, d'une longue
phrase (présente dans le texte), d'un mot qui n'existe pas. Que remarquez-vous?
T. Rahobisoa 6/8 ALGO03 - Recherche textuelle
Terminale - Spécialité NSI IFS Singapour
Exercice 5 :Algorithme naïf inversé
Re-écrire l'algorithme de recherche naïve mais en démarrant de la fin du motif et non du début.
Exercice 6 :Fonction préparatoire
On va d'abord coder une fonctiondico_lettres qui prend en paramètre un motmot et qui renvoie un diction-
naire associant à chaque lettre de mot son dernier rang dansmot. On exclut la dernière lettre, qui poserait un
problème lors du décalage (on décalerait de 0...)
Écrire la fonctiondico_lettres.
Exemple d'utilisation :
1 >>> dico_lettres("MARINA BAY SANDS")
2 {'M': 0, 'A': 12, 'R': 2, 'I': 3, 'N': 13, ' ': 10, 'B': 7, 'Y': 9, 'S':
11, 'D': 14}
Exercice 7 :Algorithme de Boyer-Moore
Toujours à partir de la vidéo précédente, répondre aux questions ci-dessous :
1. Dans quelle(s) condition(s) de recherche textuelle peut-on décaler la recherche de plus d'un caractère?
2. En déduire pourquoi la recherche d'un mot dans un texte est un cas particulier permettant d'accélérer
notablement le traitement.
3. Décrire le fonctionnement de l'algorithme deBoyer-Moore.
4. Expliquer l'avantage du prétraitement dans cet algorithme.
5. Écrire la fonction décrite dans la vidéo permettant de retourner la table des sauts pour une clé donnée.
Cette fonctiontable_saut(cle) retournera un dictionnaire dont les clés seront les lettres de la clé, et les
valeurs le saut associé.
6. Indiquer le résultat obtenu avec votre fonction pour la clé« EXCELLENT ».
Exercice 8 :Algorithme de Boyer-Moore-Horspool
En utilisant la fonctiondico_lettres créée précédemment, compléter le code ci-dessous permettant d'implé-
menter l'agolrithme deBoyer-Moore-Horspool.
1 def dico_lettres(mot):
2 ...
3 return d
4
5 def BMH(texte, motif):
6 dico = dico_lettres(motif)
7 indices = []
8 i = 0
9 while i <= ... - ...:
10 k = ...
11 while k > 0 and texte[...] == motif[...]:
12 k = ...
13 if k == ...:
14 indices.append(...)
15 i = ...
16 else:
17 if ... in dico:
18 i += ... - ... - 1
19 else:
20 i += ...
21 return ...
T. Rahobisoa 7/8 ALGO03 - Recherche textuelle
Terminale - Spécialité NSI IFS Singapour
Exemple d'utilisation :
1 >>> BMH("une magnifique maison bleue", "maison")
2 [15]
3 >>> BMH("une magnifique maison bleue", "nsi")
4 []
5 >>> BMH("une magnifique maison bleue", "ma")
6 [4, 15]
Exercice 9 :Temps de recherche BMH
Reprendre les mesures effectuées surLes Misérables, mais cette fois avec l'algorithmeBoyer-Moore-Horspool.
Que remarquez-vous?
Exercice 10 :Epreuve pratique 2022 - Sujet n°6 - Exercice 2
La fonction recherche prend en paramètres deux chaines de caractèresgene et seq_adn et renvoieTrue si on
retrouve gene dansseq_adn et False sinon.
Compléter le code Python ci-dessous pour qu'il implémente la fonctionrecherche.
1 def recherche(gene, seq_adn):
2 n = len(seq_adn)
3 g = len(gene)
4 i = ...
5 trouve = False
6 while i < ... and trouve == ... :
7 j = 0
8 while j < g and gene[j] == seq_adn[i+j]:
9 ...
10 if j == g:
11 trouve = True
12 ...
13 return trouve
Exemples :
1 >>> recherche("AATC", "GTACAAATCTTGCC")
2 True
3 >>> recherche("AGTC", "GTACAAATCTTGCC")
4 False
T. Rahobisoa 8/8 ALGO03 - Recherche textuelle

## Algo parcours graphes

### Algo parcours graphes

Terminale - Spécialité NSI IFS Singapour
Chapitre 21 - Parcours de graphes
Objectifs :
▷ Implémenter en Python des algorithmes de parcours de graphes et de recherche de chemins dans un graphe.
▷ Utiliser ces fonctions Python pour résoudre un problème utilisant des graphes (navigation GPS, laby-
rinthes, mots voisins, ...,etc.)
1 Introduction
Un des premiers algorithmes que l'on doit savoir utiliser sur un graphe est celui de son parcours.
Parcourir un graphe , c'est visiter ses différents sommets, afin de pouvoir opérer une action tour à tour sur
eux. Tous comme pour les arbres, il est possible de réaliser deux types de parcours d'un arbre :
— le parcours en largeur : Breadth First Search
— le parcours en profondeur : Depth-First Search
Cependant, contrairement aux arbres :
— il n'y a pas de racine, donc on doit choisir à partir de quel noeud on part : lenoeud source.
— il peut y avoir un nombre quelconque d'arêtes, et il faut donc marquer les chemins déjà empruntés lors
du parcours.
2 Applications
Selon les actions opérées au cours d'un parcours, on peut détecter :
— des cycles dans le graphe,
— trouver le chemin le plus court entre deux sommets,
— calculer la distance entre deux sommets, ...,etc.
Les algorithmes sur les graphes sont très utilisés dans la vie courante, ils permettent par exemple :
— le routage des paquets de données dans un réseau;
— de trouver le chemin le plus court entre deux villes (utilisé par les GPS);
— de sortir d'un labyrinthe, ...,etc.
T. Rahobisoa 1/9 ALGO01 - Parcours des graphes
Terminale - Spécialité NSI IFS Singapour
3 Parcours en largeur
Regarder cette vidéo sur le parcours en largeur jusqu'à 7'03.
3.1 Principe du BFS ou Breadth-First Search
A partir d'un sommetS0, on explore tous ses voisins (ou successeurs), puis on explore tous les voisins de ces
voisins, et ainsi de suite. Le parcours balaie ainsi chaque "branche" au même rythme, d'où le nom de parcours
en largeur.
3.2 Algorithme
A retenir!
1. On choisit un sommet de départ
2. On l'enfile :
3. Tant que la file n'est pas vide :
— On défile son premier élément
— S'il n'a pas encore été visité on le marque et on enfile tous ses voisins non encore visités
— Sinon, on ne fait rien (on passe donc directement à l'itération suivante)
Exercice 1 : On effectue unparcours en largeur sur les graphe ci-dessous :
Figure 1 – Graphe 1
1. Donner l'ordre dans lequel les sommets sont explorés dans le graphe 1 à partir du sommet A.
2. Même question pour le graphe 2 ci-dessous.
3. Vérifier vos réponses pour G1 et G2 avec le siteGraphonline en allant dans la rubriqueAlgorithmes puis
Parcours en largeur.
T. Rahobisoa 2/9 ALGO01 - Parcours des graphes
Terminale - Spécialité NSI IFS Singapour
Figure 2 – Graphe 2
4 Parcours en profondeur
4.1 Principe du DFS ou Depth-First Search
A partir d'un sommetS0, on explore un de ses voisins (ou successeurs) et ainsi de suite. S'il n'y a plus de voisins,
on revient au sommet précédent et on passe à un autre de ses enfants. Cette façon de faire implique que chaque
"branche" est explorée jusqu'au bout, avant de revenir sur nos pas, d'où le nom de parcours en profondeur.
4.2 Algorithme
En stockant les sommets encore à visiter dans une pile, on s'assure que ce sont les derniers sommets découverts
qui vont être visités en premier (LIFO,Last In First Out ).
A retenir!
1. On choisit un sommet de départ
2. On l'empile
3. Tant que la pile n'est pas vide :
— On dépile son sommet
— S'il n'a pas encore été visité on le marque
— on étudie ses voisins :
si le voisin a déjà été visité, on l'ignore
si le voisin n'a pas encore été visité, on l'empile et on reprend à l'étape 2
— Sinon, on ne fait rien (on passe donc directement à l'itération suivante)
Regarder cette vidéo sur le parcours en profondeur jusqu'à 10'01.
T. Rahobisoa 3/9 ALGO01 - Parcours des graphes
Terminale - Spécialité NSI IFS Singapour
Exercice 2 : On effectue unparcours en profondeur sur les graphes ci-dessous :
Figure 3 – Graphe 1
1. Donner l'ordre dans lequel les sommets sont explorés dans le graphe 1 à partir du sommet A.
2. Même question pour le graphe 2 ci-dessus.
Figure 4 – Graphe 2
3. Même question pour le graphe 3 ci-dessous.
Figure 5 – Graphe 3
4. Vérifier vos réponses pour G1, G2 et G3 avec le siteGraphonline en allant dans la rubriqueAlgorithmes
puis Parcours en profondeur.
T. Rahobisoa 4/9 ALGO01 - Parcours des graphes
Terminale - Spécialité NSI IFS Singapour
5 Exercices
Dans les exercices ci-dessous, nous utiliserons pour représenter les graphes étudiés par leur liste d'adjacence
associée.
Exercice 3 : Parcours BFS
Ecrire le code d'une fonction parcours_en_largeur qui parcourt en largeur un graphe à partir du sommet
depart et dont sa liste d'adjacence est representée par un dictionnaire nommégraphe.
Cette fonction renverra la liste des sommets parcourus en partant du sommetdepart.
Compléter le script ci-dessous :
1 def p a r c o u r s _ e n _ l a r g e u r ( graphe , depart ) :
2 file = [ depart ]
3 parcours = ...
4 ...
5
6 return parcours
7
8 # Test
9 assert p a r c o u r s _ e n _ l a r g e u r ({ " A " : [ " B " , " D " , " E " ] , " B " : [ " A " , " C " ] , " C " :
[ " B " , " D " ] , " D " : [ " A " , " C " , " E " ] , " E " : [ " A " , " D " , " F " , " G " ] , " F " : [ " E " ,
" G " ] , " G " : [ " E " , " F " , " H " ] , " H " : [ " G " ]} , " A " ) == [ 'A ' , 'B ' , 'D ' , 'E ' ,
'C ' , 'F ' , 'G ' , 'H ']
Graphe du test :
Exercice 4 : BFS optimisé
Le coût d'une recherche dans une liste (pour tester si un sommet a déjà été visité) est beaucoup plus important
que le coût de la recherche dans un ensemble (hors programme NSI) ou dans un dictionnaire. (tables de hash)
Nous allons donc proposer une autre version pour améliorer l'efficacité de l'algorithme.
— Un sommet est "vu" lorsqu'il a été mis dans la listeparcours
— Un sommet est "en attente" lorqu'il est dans la file.
— Tous les autres sommets sont "pas vu".
Compléter le script suivant :
1 def p a r c o u r s _ l a r g e u r _ o p t ( graphe , depart ) :
2 file = [ depart ]
3 parcours = []
4 etat = { sommet : " pas vu " for sommet in graphe }
5 etat [ depart ] = " en attente "
6
7 while file != []:
8 sommet = file . pop (0)
9 parcours . append ( sommet )
10 etat [ sommet ] = ...
T. Rahobisoa 5/9 ALGO01 - Parcours des graphes
Terminale - Spécialité NSI IFS Singapour
11 for voisin in graphe [ sommet ]:
12 if etat [ voisin ] == ...:
13 ...
14 return parcours
15
16 # Test
17 assert p a r c o u r s _ l a r g e u r _ o p t ({ " A " : [ " B " , " D " , " E " ] , " B " : [ " A " , " C " ] , " C " :
[ " B " , " D " ] , " D " : [ " A " , " C " , " E " ] , " E " : [ " A " , " D " , " F " , " G " ] , " F " : [ " E " ,
" G " ] , " G " : [ " E " , " F " , " H " ] , " H " : [ " G " ]} , " A " ) == [ 'A ' , 'B ' , 'D ' , 'E ' ,
'C ' , 'F ' , 'G ' , 'H ']
Exercice 5 : Parcours DFS récursif
Le parcours en profondeur s'écrit naturellement de manièrerécursive :
— L'ensemble des sommets déjà visités est stocké dans un objet Python (liste, ou dictionnaire).
— La visite est relancée récursivement pour chaque voisin du sommet visité qui n'a pas déjà été visité.
Compléter le code de la fonctionrécursive parcours_profondeur qui parcourt en profondeur un graphe à
partir du sommetsommet et dont sa liste d'adjacence est representée par un dictionnaire nommégraphe.
Cette fonction renverra la liste des sommets parcourus en partant du sommetdepart.
1 def p a r c o u r s _ p r o f o n d e u r ( graphe , depart , vus = None ) :
2 if vus is None :
3 vus = []
4 vus . append ( depart )
5 for voisin in graphe [ depart ]:
6 ...
7 return vus
8
9 # Tests
10
11 assert p a r c o u r s _ p r o f o n d e u r ({ " A " : [ " B " , " D " , " E " ] , " B " : [ " A " , " C " ] , " C " :
[ " B " , " D " ] , " D " : [ " A " , " C " , " E " ] , " E " : [ " A " , " D " , " F " , " G " ] , " F " : [ " E " ,
" G " ] , " G " : [ " E " , " F " , " H " ] , " H " : [ " G " ]} , " A " ) == [ 'A ' , 'B ' , 'C ' , 'D ' ,
'E ' , 'F ' , 'G ' , 'H ']
Graphe du test :
Exercice 6 : DFS récursif optimisé
Le coût d'une recherche dans une liste (pour tester si un sommet a déjà été visité) est beaucoup plus important
que le coût de la recherche dans un ensemble (hors programme NSI), ou dans un dictionnaire.
Nous allons donc proposer une autre version pour améliorer l'efficacité de l'algorithme.
Compléter la versionrécursive optimisée de la fonctionprofondeur_opt, qui utilise un dictionnairevu pour
éviter les doublons :
T. Rahobisoa 6/9 ALGO01 - Parcours des graphes
Terminale - Spécialité NSI IFS Singapour
1 def p r o f o n d e u r _ o p t ( graphe , depart , vu = None , parcours = None ) :
2
3 if vu is None :
4 vu = { sommet : False for sommet in graphe }
5 if parcours is None :
6 parcours = []
7 vu [ depart ] = True
8 parcours . append (...)
9
10 for voisin in graphe [ depart ]:
11 if ...:
12 ...
13 return vu , parcours
14
15 # Tests
16 assert p r o f o n d e u r _ o p t ({ " A " : [ " B " , " D " , " E " ] , " B " : [ " A " , " C " ] , " C " : [ " B " ,
" D " ] , " D " : [ " A " , " C " , " E " ] , " E " : [ " A " , " D " , " F " , " G " ] , " F " : [ " E " , " G " ] ,
" G " : [ " E " , " F " , " H " ] , " H " : [ " G " ]} , " A " ) == ({ 'A ': True , 'B ': True , 'C ':
True , 'D ': True , 'E ': True , 'F ': True , 'G ': True , 'H ': True } , [ 'A ' , 'B ' ,
'C ' , 'D ' , 'E ' , 'F ' , 'G ' , 'H ' ])
Exercice 7 : DFS itératif avec pile
Comme nous l'avons vu dans la vidéo du cours, on peut aussi utiliser unepile.
Ecrire le code d'une fonction parcours_en_profondeur qui parcourt en profondeur un graphe à partir du
sommet depart et dont sa liste d'adjacence est representée par un dictionnaire nommégraphe
Cette fonction renverra la liste des sommets parcourus en partant du sommetdepart.
Compléter le script ci-dessous de façonitérative :
1 def p a r c o u r s _ e n _ p r o f o n d e u r ( graphe , depart ) :
2 pile = ...
3 parcours = []
4 ...
5 return parcours
6
7 # Tests
8 assert p a r c o u r s _ e n _ p r o f o n d e u r ({ " A " : [ " B " , " D " , " E " ] , " B " : [ " A " , " C " ] , " C " :
[ " B " , " D " ] , " D " : [ " A " , " C " , " E " ] , " E " : [ " A " , " D " , " F " , " G " ] , " F " : [ " E " ,
" G " ] , " G " : [ " E " , " F " , " H " ] , " H " : [ " G " ]} , " A " ) == [ 'A ' , 'E ' , 'G ' , 'H ' ,
'F ' , 'D ' , 'C ' , 'B ']
Graphe du test :
T. Rahobisoa 7/9 ALGO01 - Parcours des graphes
Terminale - Spécialité NSI IFS Singapour
Exercice 8 : DFS itératif optimisé
Le coût d'une recherche dans une liste (pour tester si un sommet a déjà été visité) est beaucoup plus important
que le coût de la recherche dans un ensemble (hors programme NSI), ou dans un dictionnaire.
Nous allons donc proposer une autre version pour améliorer l'efficacité de l'algorithme :
— Un sommet est "parcouru" lorsqu'il a été mis dans la liste parcours
— Un sommet est "en attente" lorqu'il est dans la pile.
— Tous les autres sommets sont "pas vu".
Compléter la version itérative optimisée de la fonctionprofondeur_opt, qui utilise un dictionnairevu pour
éviter les doublons :
1 def p a r c o u r s _ p r o f o n d e u r _ i t e r a t i f ( graphe , depart ) :
2 parcours = []
3 etat = { sommet : " pas vu " for sommet in graphe }
4 pile = [...]
5 etat [ depart ] = " en attente "
6 while len ( pile ) != 0: # ou pile != []
7 sommet = ...
8 parcours . append (...)
9 etat [ sommet ] = " parcouru "
10 voisins = ...
11 for voisin in ...:
12 if etat [ voisin ] == " pas vu " :
13 pile . append (...)
14 etat [ voisin ]= ...
15 return parcours
16
17 # Tests
18 assert p a r c o u r s _ p r o f o n d e u r _ i t e r a t i f ({ " A " : [ " B " , " D " , " E " ] , " B " : [ " A " , " C " ] ,
" C " : [ " B " , " D " ] , " D " : [ " A " , " C " , " E " ] , " E " : [ " A " , " D " , " F " , " G " ] , " F " :
[ " E " , " G " ] , " G " : [ " E " , " F " , " H " ] , " H " : [ " G " ]} , " A " ) == [ 'A ' , 'E ' ,
'G ' , 'H ' , 'F ' , 'D ' , 'C ' , 'B ']
Exercice 9 : Labyrinthe
Suivre les instructions de la page suivante en écrivant les fonctions manquantes pour résoudre le problème de
parcours dans un labyrinthe.
T. Rahobisoa 8/9 ALGO01 - Parcours des graphes
Terminale - Spécialité NSI IFS Singapour
Exercice 10 : Recherche de chemins dans un graphe
Sur la rive d'un fleuve se trouvent un loup,une chèvre,un chou et un passeur. Le problème consiste à tous les
faire passer sur l'autre rive à l'aide d'une barque,menée par le passeur,en respectant les règles suivantes :
— la chèvre et le chou ne peuvent pas rester sur la même rive sans le passeur;
— la chèvre et le loup ne peuvent pas rester sur la même rive sans le passeur;
— le passeur ne peut mettre qu'un seul "passager" avec lui.
On décide de représenter le passeur par la lettreP, la chèvre par la lettreC, le loup parL et le chou parX.
1. Représenter ce problème à l'aide d'un graphe où les sommets sont tous les états possibles sur la rive de
départ (par exemple,PLCX est un sommet représentant le fait que tous sont sur la rive de départ.)
2. Trouver une solution au problème en indiquant chacun des déplacements (si possible une solution avec le
moins de déplacements possibles).
3. Proposer une modélisation avec un graphe pour résoudre ce jeu.
Exercice 11 : Annales de Bac
Afin de s'entraîner pour l'épreuve écrite du Bac, faire les exercices suivants :
— Exercice 2, Amérique du Nord 2024, J1
— Exercice 1, Centre étrangers 2024, J1
— Exercice 2, Asie 2024, J1
— Exercice 2, Métropole 2024, J1
— Exercice 1, Polynésie 2024, J1
— Exercice 1, Polynésie 2024, J2
T. Rahobisoa 9/9 ALGO01 - Parcours des graphes

## explRechBMH

### explRechBMH

Recherche textuelle HORSPOOL
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
3 INDICES
T existe dans le motif
à gauche de la non
correspondance...
Il est situé à 3
lettres de la non
correspondance.
Cette fois on compare de
droite à gauche le motif et
le texte.
1 étape

Recherche textuelle HORSPOOL
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
1 INDICE
G existe dans le motif
à gauche de la non
correspondance...
Il est situé à 1
lettres de la non
correspondance.
2 étapes

Recherche textuelle HORSPOOL
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
1 INDICE
G existe dans le motif
QUELQUE PART à
droite de la non
correspondance...
Qu'il y en ait un
autre à gauche
importe peu.
3 étapes

Recherche textuelle HORSPOOL
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
4 INDICES
T existe dans le motif
à droite de la non
correspondance...
Il est situé à 4
lettres de la non
correspondance.
4 étapes

Recherche textuelle HORSPOOL
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
Relevé de
l'indice du texte
où débute le
motif reconnu
Éventuellement poursuite de
la recherche textuelle
5 étapes

## expl rech naive

### expl rech naive

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
1 étape

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
2 étapes

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
3 étapes

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
4 étapes

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
5 étapes

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
6 étapes

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
7 étapes

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
8 étapes

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
9 étapes

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
DECALAGE DE
UN INDICE
10 étapes

Recherche textuelle naïve
Texte :
Motif :
A A C A T A T G G G A T G C G A G G T C G T A G T
A T G C G A
Relevé de
l'indice du texte
où débute le
motif reconnu
Éventuellement poursuite de
la recherche textuelle
11 étapes
