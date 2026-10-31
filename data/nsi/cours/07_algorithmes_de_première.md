# Algorithmes de Première

## T6 5 algos coeur

### 1. Factorielle récursive

```python linenums='1'
def factorielle(n):
    if n == 1:
        return 1
    else:
        return n * factorielle(n - 1)
```

### 3. Puissance récursive (simple)

```python linenums='1'
def puissance(x, n):
    if n == 0:
        return 1
    else:
        return x * puissance(x, n-1)
```

### 4. Puissance récursive (optimisée)

```python linenums='1'
def puissance(x, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return puissance(x*x, n//2)
        else :
            return x*puissance(x*x, (n-1)//2)
```

### 5. Tri par insertion

```python linenums='1'
def tri_insertion(lst):
    '''trie en place la liste lst donnée en paramètre'''
    for i in range(1, len(lst)):                 
        k = i                                    
        while k > 0 and lst[k-1] > lst[k] :      
            lst[k], lst[k-1] = lst[k-1], lst[k]      
            k = k - 1                               
```

voir cours

### 6. Tri par sélection

```python linenums='1'
def tri_selection(lst) :
    for i in range(len(lst)-1):
        indice_min = i
        for k in range(i+1, len(lst)) :
            if lst[k] < lst[indice_min]:
                indice_min = k
        lst[i], lst[indice_min] = lst[indice_min], lst[i]
```

voir cours

### 7. Dichotomie

```python
def recherche_dichotomique(lst, val) :
    indice_debut = 0
    indice_fin = len(lst) - 1
    while indice_debut <= indice_fin :
        indice_centre = (indice_debut + indice_fin) // 2     
        valeur_centrale = lst[indice_centre]            
        if valeur_centrale == val :          
            return indice_centre
        if valeur_centrale < val :             
            indice_debut = indice_centre + 1
        else :
            indice_fin = indice_centre - 1
    return None
        
```

voir cours
