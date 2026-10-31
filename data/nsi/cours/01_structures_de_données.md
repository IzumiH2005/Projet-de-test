# Structures de données

## Listes Piles Files

### 0. Préambule : interface ≠ implémentation

Les structures que nous allons voir peuvent s'envisager sous deux aspects :

- le côté utilisateur, qui utilisera une interface pour manipuler les données.
- le côté concepteur, qui aura choisi une implémentation pour construire la structure de données.

    - Le volant et les pédales d'une voiture constituent une partie de son **interface**.
    - L'**implémentation** va désigner tous les mécanismes techniques qui sont mis en œuvre pour que (par exemple) le mouvement de rotation du volant aboutisse à un changement de direction des roues.
    - La standardisation des interfaces fait qu'un utilisateur peut passer sans problème d'une voiture à une autre, même si l'implémentation est complètement différente.

    

Nous avons déjà abordé ces deux aspects lors de la découverte de la Programmation Orientée Objet. Le principe d'encapsulation fait que l'utilisateur n'a qu'à connaître l'existence des méthodes disponibles, et non pas le contenu technique de celle-ci. Cela permet notamment de modifier le contenu technique (l'implémentation) sans que les habitudes de l'utilisateur (l'interface) ne soient changées.

### 1.1 À chaque donnée sa structure

En informatique comme dans la vie courante, il est conseillé d'adapter sa manière de stocker et de traiter des données en fonction de la nature de celles-ci :

- Le serveur d'un café, chargé de transporter les boissons du comptoir aux tables des clients, n'utilisera pas un sac en plastique pour faire le transport : il préfèrera un plateau. 
- Le chercheur de champignons, lui, n'utilisera pas un plateau pour stocker ses trouvailles : il préfèrera un panier.
- Pour stocker des chaussettes, on préfèrera les entasser dans un tiroir (après les avoir appairées), plutôt que de les suspendre à des cintres. 

De même en informatique, pour chaque type de données, pour chaque utilisation prévue, une structure particulière de données se revèlera (peut-être) plus adaptée qu'une autre.

#### 1.1.1 Données linéaires
Intéressons nous par exemple aux **données linéaires**. Ce sont des données qui ne comportent pas de *hiérarchie* : toutes les données sont de la même nature et ont le même rôle. 
Par exemple, un relevé mensuel de températures, la liste des élèves d'une classe, un historique d'opérations bancaires... 

Ces données sont «plates», n'ont pas de sous-domaines : la structure de **liste** paraît parfaitement adaptée. 

Lorsque les données de cette liste sont en fait des couples (comme dans le cas d'une liste de noms/numéros de téléphone), alors la structure la plus adaptée est sans doute celle du **dictionnaire**.

Les listes et les dictionnaires sont donc des exemples de structures de **données linéaires**.

#### 1.1.2 Données non-linéaires
Même si ce n'est pas l'objet de ce cours, donnons des exemples de structures adaptées aux données non-linéaires :

Si une liste de courses est subdivisée en "rayon frais / bricolage / papeterie" et que le rayon frais est lui-même séparé en "laitages / viandes / fruits & légumes", alors une structure d'**arbre** sera plus adaptée pour la représenter. Les structures arborescentes seront vues plus tard en Terminale.

Enfin, si nos données à étudier sont les relations sur les réseaux sociaux des élèves d'une classe, alors la structure de **graphe** s'imposera d'elle-même. Cette structure sera elle-aussi étudiée plus tard cette année.

### 1.2 Comment seront traitées ces données linéaires ? Introduction des listes, des piles et des files

La nature des données ne fait pas tout. Il faut aussi s'intéresser à la manière dont on voudra les traiter :

- À quelle position les faire entrer dans notre structure ?
- À quel moment devront-elles en éventuellement en sortir ?
- Veut-on pouvoir accéder rapidement à n'importe quel élément de la structure, ou simplement au premier ? ou au dernier ?

Lorsque ces problématiques d'entrée/sortie n'interviennent pas, la structure «classique» de liste est adaptée. Mais lorsque celle-ci est importante, il convient de différencier la structure de **pile** de celle de **file**.

#### 1.2.1 Les piles (*stack*)

Une structure de **pile** (penser à une pile d'assiette) est associée à la méthode **LIFO** (Last In, First Out) :
les éléments sont empilés les uns au-dessus des autres, et on ne peut toujours dépiler que l'élément du haut de la pile. Le dernier élément à être arrivé est donc le premier à être sorti.

**Exemples de données stockées sous forme de pile** 

- lors de l'exécution d'une fonction récursive, le processeur empile successivement les appels à traiter : seule l'instruction du haut de la pile peut être traitée.

- dans un navigateur internet, la liste des pages parcourues est stockée sous forme de pile : la fonction «Back» permet de «dépiler» peu à peu les pages précédemment parcourues : 

- lors d'un Devoir Surveillé, la dernière copie remise sur le bureau du professeur est (souvent) la première corrigée.

#### 1.2.2 Les files (*queue*)

Une structure de **file** (penser à une file d'attente) est associée à la méthode **FIFO** (First In, First Out) :
les éléments sont enfilés les uns à la suite des autres, et on ne peut toujours défiler que l'élément du haut de la file. Le premier élément à être arrivé est donc le premier à en sortir. Sinon ça râle dans la file d'attente.

**Exemples de données stockées sous forme de file :** 

- les documents envoyés à l'imprimante sont traitées dans une file d'impression.
- la «queue» à la cantine est (normalement) traitée sous forme de file.

#### 1.2.3 Le problème du stockage : transformer les piles en files
Dans les entrepôts de stockage, comme dans les rayons d'un supermarché, la structure naturelle est celle de la **pile** : les gens attrapent l'élément situé devant eux («en haut de la pile»). Si les employés du supermarché remettent en rayon les produits plus récents sur le dessus de la pile, les produits au bas de la pile ne seront jamais choisis et périmeront.  
Ils doivent donc transformer la pile en file : lors de la mise en rayon de nouveaux produits, ceux-ci seront placés derrière («au bas de la file») afin que partent en priorité les produits à date de péremption plus courte.
On passe donc du LIFO au FIFO.  

Certains dispositifs permettent de le faire naturellement :  
Ci-dessous, une file... de piles (électriques). Le chargement par le haut du distributeur fait que celle qui sera sortie (en bas) sera celle qui aura été rentrée en premier (par le haut). Ce FIFO est donc provoqué naturellement par la gravité (et un peu d'astuce).

On notera que cette problématique est universelle : voir par exemple ce site.

Après avoir présenté rapidement ces trois types de données linéaires, nous allons maintenant les étudier plus en détail, et proposer pour chacune d'elles une interface et plusieurs implémentations.

### 2.1 Définition générale

Une liste est un ensemble ordonné d'objets. Généralement, ces données seront de même type, mais ce n'est pas structurellement obligatoire.

### 2.2 Les listes chaînées *(linked lists)*

Lorsque l'implémentation de la liste fait apparaître une chaîne de valeurs, chacune pointant vers la suivante, on dit que la liste est une liste **chaînée**.

**Implémentation choisie :**

- Une liste est caractérisée par un ensemble de cellules.
- Le lien (on dira souvent le «pointeur») de la variable est un lien vers la première cellule, qui renverra elle-même sur la deuxième, etc.
- Chaque cellule contient donc une valeur et un lien vers la cellule suivante.
- Une liste peut être vide (la liste vide est notée ```x``` ou bien ```None``` sur les schémas)

Une conséquence de cette implémentation sous forme de liste chaînée est la non-constance du temps d'accès à un élément de liste : pour accéder au 3ème élément, il faut obligatoirement passer par les deux précédents.

**À retenir :** dans une liste chaînée, le temps d'accès aux éléments n'est pas constant.

### 2.3 Exemple d'implémentation minimale d'une liste chaînée

```python linenums='1'
    class Cellule :
        def __init__(self, contenu, suivante):
            self.contenu = contenu
            self.suivante = suivante
    ```

Cette implémentation rudimentaire permet bien la création d'une liste :

```python
>>> lst = Cellule(3, Cellule(5, Cellule(1,None)))
```

La liste créée est donc :   

Mais plus précisément, on a :

    Retrouvez comment accéder aux éléments 3, 5 et 1.

    

On pourra remarquer que l'interface proposée à l'utilisateur n'est pas des plus pratiques...

### 2.4 Et les listes de Python ???

Nous connaissons déjà les listes de Python :

```python
>>> maliste = [3, 1, -1, 42]
```

Et nous connaissons aussi (un peu) l'interface de ce type ```list```, notamment avec les méthodes ```append()``` ou ```reverse()```.  
Néanmoins, l'implémentation qui a été choisie par les concepteurs de Python de ce type ```list``` fait que le celui-ci se rapproche plus d'un **tableau dynamique**. 

**Dans un tableau dynamique :**

- le temps d'accès à n'importe quel élément est rapide. Ce temps d'accès est constant quelque soit l'élément : on dit que l'accès est en $O(1)$.
- l'insertion d'un élément au début ou au milieu de la liste est lente : cela oblige à décaler tous les éléments à droite de celui-ci. Le temps pris par l'insertion est proportionnel au nombre d'éléments à déplacer : on dit que l'insertion est en $O(n)$.

**Dans une liste chaînée :**

- le temps d'accès à n'importe quel élément peut être lent (proportionnel à la position de l'élément dans la liste). Le temps d'accès est en $O(n)$.
- l'insertion d'un élément à l'intérieur de la liste est rapide : il y a simplement à modifier la valeur du lien de la cellule à gauche de l'endroit d'insertion. L'action d'insérer est donc en $O(1)$. Toutefois, avant d'arriver à l'endroit d'insertion, il faut avoir parcouru toutes les cellules précédentes ! Le temps total d'insertion est donc lui aussi linéaire, en $O(n)$.

Nous nous servirons parfois du type ```list``` de Python dans la suite de ce cours, mais il ne faut pas oublier qu'il n'est pas un «vrai» type ```list```.

### 2.5 Un exemple d'interface pour les listes

Imaginons que nous possédons une interface offrant les fonctionnalités suivantes :

- ```Liste()``` : crée une liste vide.
- ```est_vide``` : indique si la liste est vide. (renvoie un booléen)
- ```ajoute_tete``` : insère un élément (passé en paramètre) en tête de liste. (ne renvoie rien)
- ```renvoie_tete``` : renvoie la valeur de l'élément en tête de liste ET le supprime de la liste.

    On considère l'enchaînement d'opérations ci-dessous. Écrire à chaque étape l'état de la liste ```lst``` et la valeur éventuellement renvoyée. On considèrera que la tête de la liste est à gauche.
    ```python
    1. lst = Liste()      
    2. lst.ajoute_tete(3)
    3. lst.ajoute_tete(5) 
    4. lst.ajoute_tete(1) 
    5. lst.renvoie_tete() 
    6. lst.est_vide()     
    7. lst.ajoute_tete(2) 
    8. lst.renvoie_tete() 
    9. lst.renvoie_tete() 
    10. lst.renvoie_tete()
    11. lst.est_vide()    
    ```

### 3. Les piles

Comme expliqué précédemment, une pile travaille en mode LIFO (Last In First Out).
Pour être utilisée, l'interface d'une pile doit permettre a minima :

- la création d'une pile vide
- l'ajout d'un élément dans la pile (qui sera forcément au dessus). On dira qu'on **empile**.
- le retrait d'un élément de la pile (qui sera forcément celui du dessus) et le renvoi de sa valeur. On dira qu'on **dépile**.

### 3.1 Utilisation d'une interface de pile

On considère l'enchaînement d'opérations ci-dessous. Écrire à chaque étape l'état de la pile ```p``` et la valeur éventuellement renvoyée.

    Bien comprendre que la classe ```Pile()``` et ses méthodes n'existent pas vraiment. Nous *jouons* avec son interface.

    On prendra pour convention que la tête de la pile est à droite.

    ```python
    1. p = Pile() 
    2. p.empile(3)   
    3. p.empile(5)  
    4. p.est_vide()  
    5. p.empile(1)  
    6. p.depile()  
    7. p.depile() 
    8. p.empile(9)  
    9. p.depile()  
    10. p.depile() 
    11. p.est_vide() 
    ```

### 3.2 Implémentation(s) d'une pile

L'objectif est de créer une classe ```Pile```. L'instruction  ```Pile()```  créera une pile vide. Chaque objet ```Pile``` disposera des méthodes suivantes :

- ```est_vide``` : indique si la pile est vide (renvoie un booléen)
- ```empile``` : insère un élément (passé en paramètre) en haut de la pile. Ne renvoie rien.
- ```depile``` : renvoie la valeur de l'élément en haut de la pile ET le supprime de la pile.

Ces 3 méthodes sont essentielles et se retrouveront systématiquement dans chaque interface. Nous y ajouterons, uniquement par commodité, la méthode suivante :

- ```__repr__``` : permet d'afficher la pile sous forme agréable (par ex : ```|3|6|2|5|```)

#### 3.2.1 À l'aide du type ```list``` de Python 
{#

    Créer la classe ```Pile```   ci-dessus. 
    
    Le type ```list``` de Python est parfaitement adapté. Des renseignements intéressants à son sujet peuvent être trouvés ici.

#}

    Créer la classe ```Pile```   ci-dessus. 
    
    Le type ```list``` de Python est parfaitement adapté. Des renseignements intéressants à son sujet peuvent être trouvés ici.

 
    **Correction :heart: :heart: :heart:** 

    ```python linenums='1'
    class Pile:
        def __init__(self):
            self.data = []
        
        def est_vide(self):
            return len(self.data) == 0       
    
        def empile(self,x):
            self.data.append(x)

        def depile(self):
            if self.est_vide():
                print('Vous avez essayé de dépiler une pile vide !')
                return None
            else :
                return self.data.pop() 
    ```
    

#### 3.2.2 À l'aide d'une liste chaînée et de la classe  ```Cellule``` créée au 2.3

Au **2.3** nous avons créé la classe  ```Cellule``` :

```python linenums='1'
class Cellule :
    def __init__(self, contenu, suivante):
        self.contenu = contenu
        self.suivante = suivante
```

    À l'aide cette classe, re-créer une classe ```Pile``` disposant exactement de la même interface que dans l'exercice précédent. 

    

**À retenir :** 
pour l'utilisateur, les interfaces du 3.2.1 et 3.2.2 sont strictement identiques. Il ne peut pas savoir, en les utilisant, quelle est l'implémentation qui est derrière.

### 3.3 Application des piles

Simulez une gestion de l'historique de navigation internet, en créant une classe ```Nav``` qui utilisera une pile.
    Attention, il ne faut pas réinventer la classe ```Pile```, mais uniquement s'en servir !
    
    Exemple d'utilisation :
    ```python 
    >>> n = Nav()
    >>> n.visite('lemonde.fr')
    page actuelle : lemonde.fr
    >>> n.visite('google.fr')
    page actuelle : google.fr
    >>> n.visite('lyceemauriac.fr')
    page actuelle : lyceemauriac.fr
    >>> n.back()
    page quittée : lyceemauriac.fr
    >>> n.back()
    page quittée : google.fr
    ```

### 4. Les files

Comme expliqué précédemment, une file travaille en mode FIFO (First In First Out).
Pour être utilisée, une interface de file doit proposer a minima :

- la création d'une file vide
- l'ajout d'un élément dans la file. On dira qu'on **enfile**.
- le retrait d'un élément de la file et le renvoi de sa valeur. On dira qu'on **défile**.

La représentation la plus courante d'une file se fait horizontalement, en enfilant par la gauche et en défilant par la droite :

### 4.1 Utilisation d'une interface de file

On considère l'enchaînement d'opérations ci-dessous. Écrire à chaque étape l'état de la file ```f``` et la valeur éventuellement renvoyée.
    Par convention, on enfilera **à gauche** et on défilera **à droite**.
    ```python
    1. f = File()
    2. f.enfile(3) 
    3. f.enfile(5)
    4. f.est_vide()
    5. f.enfile(1) 
    6. f.defile() 
    7. f.defile()
    8. f.enfile(9) 
    9. f.defile() 
    10. f.defile()
    11. f.est_vide() 
    ```

### 4.2 Implémentation d'une file

L'objectif est de créer une classe ```File```, disposant des méthodes suivantes :

- ```est_vide``` : indique si la file est vide. (renvoie un booléen)
- ```enfile``` : insère un élément (passé en paramètre) en queue de file. (ne renvoie rien)
- ```defile``` : renvoie la valeur de l'élément en tête de la file ET le supprime de la file.

Nous y ajouterons comme précédemment la méthode facultative suivante :

- ```__repr__``` : permet d'afficher la file sous forme agréable (par ex : ```|3|6|2|5|```)

    Créer la classe ci-dessus. Là encore, le type ```list```  de Python est peut être utilisé.
    
    Penser à aller voir ici les méthodes des objets de types ```list```, notamment la méthode ```insert```.

    

**Remarque :**  
Notre implémentation répond parfaitement à l'interface qui était demandée. Mais si le «cahier des charges» obligeait à ce que les opérations ```enfile()``` et ```defile()``` aient lieu en temps constant (en $O(1)$), notre implémentation ne conviendrait pas.  

En cause : notre méthode ```enfile()``` agit en temps linéaire  ($O(n)$) et non pas en temps constant. L'utilisation de la structure de «liste» de Python (les *tableaux dynamiques*) provoque, lors de l'instruction ```self.data.insert(0, x)``` un redimensionnement de la liste. Le tableau doit être agrandi et chaque élément doit être recopié dans la case suivante. Ceci nous coûte un temps linéaire.

### 4.3 Implémentation d'une file avec deux piles

Comment créer une file avec 2 piles ?  
L'idée est la suivante : on crée une pile d'entrée et une pile de sortie. 

- quand on veut enfiler, on empile sur la pile d'entrée.
- quand on veut défiler, on dépile sur la pile de sortie.
- si celle-ci est vide, on dépile entièrement la pile d'entrée dans la pile de sortie.

    Créer une file avec deux piles.

    

---

    - Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
    - Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.
    - Cours du DIU-EIL, David RENAULT, Université de Bordeaux.

---

### Introduction

Exercice 5 du sujet Centres Étrangers 1 - 2021

    Exercice 1 du sujet La Réunion J2 - 2022

    Exercice 2 du sujet Métropole Candidats Libres J1 - 2021

    Exercice 5 du sujet Amérique du Nord J1 - 2021

    Exercice 2 du sujet Centres Étrangers J1 - 2022

    Exercice 3 du sujet Centres Etrangers J1 - 2023

    Jeu du Simon

    Cet exercice est basé sur l'énigme n°5 d'Advent Of Code 2018.

    Le but est de réduire le plus possible une chaîne de caractères (comme ```dabAcCaCBAcCcaDA``` ) en obéissant à la règle suivante :

        Dès que deux lettres identiques mais de casse différente (majuscule-minuscule ou minuscule-majuscule) sont côte à côte dans la chaîne, on les supprime de la chaîne.

    Exemple : 
    ```
    dabAcCaCBAcCcaDA  On enlève le premier 'cC'.
    dabAaCBAcCcaDA    Cela donne naissance à un 'Aa', qu'on enlève.
    dabCBAcCcaDA      On enlève alors 'cC' (ou 'Cc', cela revient au même).
    dabCBAcaDA        Plus aucune simplification n'est possible.
    ```

    La chaîne de caractères qu'il va falloir simplifier contient ... 50000 caractères.

    #### 1. Élaboration d'une fonction utile

    On rappelle que la fonction ```ord``` renvoie le code ASCII d'une lettre. En comparant les codes ASCII de deux lettres identiques mais de casse différentes, en déduire une fonction ```simplifiable``` qui prend en paramètres deux lettres ```l1``` et ```l2``` et qui renvoie un booléen indiquant si ces deux lettres sont simplifiables. 

    *Exemples d'utilisation :*
    ```python
    >>> simplifiable('c', 'C')
    True
    >>> simplifiable('C', 'c')
    True
    >>> simplifiable('C', 'C')
    False
    ```

        ```python linenums='1'
        def simplifiable(l1, l2):
            return abs(ord(l1) - ord(l2)) == 32
        ```

    #### 2. Une seule simplification de la chaîne de caractères

    Écrire une fonction ```simplifie``` qui prend en paramètre une chaîne de caractère ```s``` et qui renvoie cette même chaîne de caractères, ayant été simplifiée une fois au maximum.

    Principe : on parcourt la chaîne et dès qu'on trouve une simplification à faire, on simplifie la chaîne et on la renvoie immédiatement.

    *Exemples d'utilisation :*
    ```python
    >>> simplifie('dabAcCaCBAcCcaDA')
    'dabAaCBAcCcaDA'
    >>> simplifie('dabAaCBAcCcaDA')
    'dabCBAcCcaDA'
    >>> simplifie('dabCBAcCcaDA')
    'dabCBAcaDA'
    >>> simplifie('dabCBAcaDA')
    'dabCBAcaDA'
    ```

    Pour information, on rappelle la technique de *slicing* de chaîne de caractères :
    ```python
    >>> ch = 'abcde'
    >>> ch[:2]
    'ab'
    >>> ch[2:]
    'cde'
    ```

        ```python linenums='1'
        def simplifie(s):
            for i in range(len(s) - 1):
                if simplifiable(s[i+1], s[i]):
                    return s[:i] + s[i+2:]
            return s
        ```

    #### 3. Résolution du problème

    Après vous être demandé comment savoir facilement qu'une chaîne n'était plus simplifiable, proposer une fonction ```reduction``` qui prend en paramètre une chaîne ```s``` et qui renvoie cette chaîne ```s``` une fois effectuées **toutes** les simplifications possibles.

    *Exemple d'utilisation :*
    ```python
    >>> reduction('dabAcCaCBAcCcaDA')
    'dabCBAcaDA'
    ```

        ```python linenums='1'
        def reduction(s):
            fini = False
            while not fini:
                s_temp = s
                s = simplifie(s)
                if len(s_temp) == len(s):
                    fini = True
            return s
        ```

    #### 4. Le vrai énoncé d'Advent of Code

    Dans cette énigme n°5, la réponse à donner est le nombre de caractères de la chaîne une fois simplifiée. Ce qui ne devrait pas nous poser de problème.

    Par contre, la chaîne ```'dabAcCaCBAcCcaDA'``` sur laquellle nous avons travaillé n'est qu'un exemple...
    La **vraie** chaîne contient 50000 caractères : vous pouvez télécharger le fichier la contenant ici : input.txt

    Anecdotique ? Pas vraiment...

    Effectuez la réduction de cette chaîne avec votre programme précédent. Que remarquez-vous ?

        ```python linenums='1'
        s = open('input.txt').read()

        def simplifiable(l1, l2):
            return abs(ord(l1) - ord(l2)) == 32

        def simplifie(s):
            for i in range(len(s) - 1):
                if simplifiable(s[i+1], s[i]):
                    return s[:i] + s[i+2:]
            return s

        def reduction(s):
            fini = False
            while not fini:
                s_temp = s
                s = simplifie(s)
                if len(s_temp) == len(s):
                    fini = True
            return s

        print(len(reduction(s)))
        ```
        
        Le résultat (9371) est loooong à nous parvenir ! (30 secondes sur ma machine)
    

    #### 5. Sauvé par une pile

    Cet exercice peut être résolu **beaucoup** plus efficacement grâce à l'utilisation d'une pile... mais comment ?

    Vous pouvez utiliser l'implémentation de pile disponible ici.

        Pour chaque lettre de la chaîne :
        
        - si la pile est vide, on empile cette lettre
        - sinon, on regarde si la lettre est simplifiable avec la lettre du haut de la pile :
            - si oui, on supprime cette lettre du haut de la pile et on passe à la lettre suivante de la chaîne
            - si non, on empile cette lettre sur la pile, et on passe à la suivante.

        ```python linenums='1'
        s = open('input.txt').read()
        class Pile:
            def __init__(self):
                self.data = []

            def est_vide(self):
                return len(self.data) == 0       

            def empile(self,x):
                self.data.append(x)

            def depile(self):
                if self.est_vide():
                    print('Vous avez essayé de dépiler une pile vide !')
                    return None
                else :
                    return self.data.pop()

            def taille(self):
                Q = Pile()
                n = 0
                while not self.est_vide():
                    Q.empile(self.depile())
                    n += 1
                while not Q.est_vide():
                    self.empile(Q.depile())
                return n

        p = Pile() 

        def simplifiable(l1, l2):
            return abs(ord(l1) - ord(l2)) == 32

        for lettre in s:
            if p.est_vide():
                p.empile(lettre)
            else:
                sommet = p.depile()
                if not simplifiable(sommet, lettre):
                    p.empile(sommet)
                    p.empile(lettre)

        print(p.taille())
   
        ```

        Le résultat est cette fois immédiat : 0.04 secondes sur ma machine, soit environ 1000 fois plus rapide que le code précédent.
ex2J2ME32024">"

    Exercice 2 du sujet Métropole J2 - Septembre 2024  

    On pourra utiliser la classe ```Pile``` ci-dessous :

    ```python linenums='1'
    class Pile:
        def __init__(self):
            self.data = []

        def est_vide(self):
            return len(self.data) == 0       

        def empile(self,x):
            self.data.append(x)

        def depile(self):
            if self.est_vide():
                return None
            else :
                return self.data.pop()

        def affiche(self):
            p_temp = Pile()
            print('---')
            while not self.est_vide():
                v = self.depile()
                print('|' + str(v) + '|')
                p_temp.empile(v)
            print('---')
            while not p_temp.est_vide():
                self.empile(p_temp.depile())
    ```
        

    **Q2**. 
    ```python linenums='1'
    def produire_jeu(n):
        resultat = Pile()
        for i in range(...):
            resultat.empile(...)
        return resultat

    ```

    

    **Q3**. 
    ```python linenums='1'
    def scinder_jeu(p, n):
        m1 = Pile()
        m2 = Pile
        for i in range(n):
            m1.empile(p.depile())
        for i in range(n):
            m2.empile(p.depile())
        return m1, m2
    ```
    

    

    

    Pour les questions **6.** et **7.**, on pourra utiliser la fonction ```identiques``` ci-dessous :

    ```python linenums='1'
    def identiques(p1, p2):
        p1_copie = Pile()
        p1_sauv = Pile()
        while not p1.est_vide():
            v = p1.depile()
            p1_copie.empile(v)
            p1_sauv.empile(v)

        p2_copie = Pile()
        p2_sauv = Pile()
        while not p2.est_vide():
            v = p2.depile()
            p2_copie.empile(v)
            p2_sauv.empile(v)    

        while not p1_sauv.est_vide():
            p1.empile(p1_sauv.depile())

        while not p2_sauv.est_vide():
            p2.empile(p2_sauv.depile())

        while not p1_copie.est_vide() and not p2_copie.est_vide():
            n1 = p1_copie.depile()
            n2 = p2_copie.depile()
            if n1 != n2:
                return False
        if not p1_copie.est_vide() or not p2_copie.est_vide():
            return False
        return True
    ```

    

    {{
    correction(True,
    """
\"Correction Q7.\" 
        ```python linenums='1'
        def ordre_faro(n):
            p_origine = produire_jeu(n)
            p = faro(produire_jeu(n), n)
            i = 1
            while not identiques(p, p_origine):
                p = faro(p, n)
                i += 1
            return i
        ```   

        Voir aussi https://en.wikipedia.org/wiki/Faro_shuffle     
    """
    )
    }}

    Exercice 2 du sujet Métropole J1 - 2025 
ex1J2AN2022">"
    Exercice 1 du sujet Amérique du Nord J2 - 2022 
ex3J2PO2025">"
    Exercice 3 du sujet Polynésie J2 - 2025 

    

    

    

    

    ```python
    def chaine_vers_tab(mot):
        tab_lettres = ...
        for ... in ... :
            tab_lettres....
        return tab_lettres
    ```

    

    ```python
    def distance(mot1, mot2):
        tab = chaine_vers_tab(mot1)
        for lettre in mot2:
            if lettre in tab:
                tab.remove(lettre)
        return len(tab)
    ```

    

    ```python
    def renvoie_voisins(mot):
        tab_voisins = ...
        for voisin_possible in ... :
            if ... :
                tab_voisins....
        return ...
    ```

    ```python
    TAB_MOTS = ['gars', 'mars', 'mors', 'ours', 'purs']
    ```

    

    {{
    correction(True,
    """
\"Correction Q8\"
        - 3ème tour :
        On défile ```mors```. Les voisins de ```mors``` sont ```mars``` et ```ours```. ```mars``` est déjà dans ```parent```. Ainsi on obtient :​
        ```python
        parent = {'mars' : None,'gars':'mars,'mors':'mars', 'ours':'mors'}
        file_voisins = ['ours']
        ```
        ​
        - 4ème tour :
        On défile ```ours```. Les voisins de ```ours``` sont ```mors``` et ```purs```, ```mors``` est déjà dans ```parent```.
        On enfile ```purs```. Ainsi on obtient :
        ```python
        parent = {'mars' : None, 'gars ': 'mars', 'mors ' : 'mars',
        'ours':'mors', 'purs': 'ours'}}
        ```

        - 5ème tour :
        La variable ```mot``` est ```ours``` qui est le mot final. La boucle s'arrête et renvoie le dictionnaire ```parent```.   
        
    """
    )
    }}

    ```python
    def renvoie_pile(parent, mot_final):
        ma_pile = Pile()
        mot = mot_final
        while mot != ... :
            ma_pile....
            mot = ...
        return ma_pile
    ```

    

    ```python
    def construit_chemin(ma_pile):
        tab = ...
        while ...:
            mot = ...
            tab....
        return tab
    ```

## Dictionnaires

### 0. Notion de tableau associatif

Un **tableau associatif** est un type abstrait de données (au même titre que les listes, piles, files, vues précédemment). Ce type abstrait de données a la particularité de ne pas être totalement linéaire (ou «plat») puisqu'il associe des **valeurs** à des **clés**.  

Il est habituellement muni des opérations suivantes :

- ajout d'une nouvelle valeur associée à une nouvelle clé (on parlera de nouveau couple clé-valeur)
- modification d'une valeur associée à une clé existante
- suppression d'un couple clé-valeur
- récupération de la valeur associée à une clé donnée.

Un répertoire téléphonique est un exemple de tableau associatif :

- les clés sont les noms
- les valeurs sont les numéros de téléphone

En Python, le **dictionnaire** est une structure native de tableau associatif.

### 1.1 Protocole de mesure

Le but est de créer une liste et un dictionnaire de même taille (arbitraire), et de comparer ensuite le temps de recherche d'un élément n'appartenant pas à ces deux structures.

**Q1.** Créer une fonction ```fabrique_liste``` qui prend en paramètre un entier ```nb``` et qui renvoie une liste composée de tous les entiers de ```0``` à ```nb-1```.

**Q2.** Créer une fonction ```fabrique_dict``` qui prend en paramètre un entier ```nb``` et qui renvoie dictionnaire composé de paires qui associent à toutes les clés ```k```  de ```0``` à ```nb-1``` leur propre valeur ```k```. 

{{
correction(True,
"""
\"Correction\" 
    ```python
    def fabrique_dict(nb):
        dct = {k:k for k in range(nb)}
        return dct
    ```

"""
)
}}

**Q3.** Créer une fonction ```mesures``` qui prend en paramètre un entier ```nb``` et qui :

- Créé une liste et un dictionnaire de taille ```nb``` à l'aide des fonctions précédentes.
- Mesure la recherche d'une valeur inexistante dans la liste, et affiche le temps de recherche.
- Mesure la recherche d'une valeur inexistante dans le dictionnaire, et affiche le temps de recherche.

Cette recherche d'une valeur inexistante s'appelle recherche *dans le pire des cas*.

    Il est impératif d'utiliser le mot-clé ```in``` propre à Python afin de bénéficier des avantages (ou inconvénients) de chacune des deux structures.

    Si on cherche notre élément en parcourant «à la main» la totalité de la structure, on aura forcément un temps de recherche proportionnel au nombre d'éléments de la structure (et donc une complexité linéaire).

    En utilisant le mot-clé ```in```, on va laisser Python gérer tout seul la recherche.

Pour davantage de précision, on pourra dans un second temps effectuer plusieurs mesures et faire une moyenne des temps obtenus.

Pour rappel, l'import du module ```time``` permet d'appeler la fonction ```time.time()```. 

{{
correction(True,
"""
\"Correction\" 
    ```python linenums='1'
    import time

    def fabrique_liste(nb):
        lst = [k for k in range(nb)]
        return lst

    def fabrique_dict(nb):
        dct = {k:k for k in range(nb)}
        return dct

    def mesures(nb):
        lst = fabrique_liste(nb)
        d = fabrique_dict(nb)
        
        tps_total = 0
        for _ in range(10):
            t0 = time.time()
            test = 'a' in lst # on cherche une donnée inexistante
            delta_t = time.time() - t0
            tps_total += delta_t
        tps_moyen_lst = tps_total / 10

        tps_total = 0
        for _ in range(10):
            t0 = time.time()
            test = 'a' in d # on cherche une donnée inexistante
            delta_t = time.time() - t0
            tps_total += delta_t
        tps_moyen_d = tps_total / 10
        
        print(f'temps pour une liste de taille {nb}       : {tps_moyen_lst}')
        print(f'temps pour un dictionnaire de taille {nb} : {tps_moyen_d}')
    ``` 
"""
)
}}

**Q4.** Effectuer des mesures avec différentes valeurs de ```nb```.

### 1.2 Mesures

Nous allons effectuer 3 mesures, avec une taille de liste et de dictionnaire augmentant d'un facteur 10 à chaque fois.

```python
>>> mesures(10**4)
temps pour une liste de taille 10000       : 0.00023534297943115235
temps pour un dictionnaire de taille 10000 : 1.6689300537109374e-07
>>> mesures(10**5)
temps pour une liste de taille 100000       : 0.0012505292892456056
temps pour un dictionnaire de taille 100000 : 4.5299530029296873e-07
>>> mesures(10**6)
temps pour une liste de taille 1000000       : 0.012522673606872559
temps pour un dictionnaire de taille 1000000 : 2.384185791015625e-07
```

- la recherche dans une liste prend un ordre de grandeur à chaque fois : elle est environ 10 fois plus grande quand la taille de la liste est 10 fois plus grande.
- la recherche dans le dictionnaire reste dans le même ordre de grandeur ($10^{-7}$ secondes).

On remarque donc que le temps moyen de recherche dans un **dictionnaire** est remarquablement **constant**.  
Il ne dépend pas du nombre d'éléments du dictionnaire dans lequel on cherche. On dit qu'il est en $O(1)$.

### 1.3 Conclusion

Il y a donc une différence fondamentale à connaître entre les temps de recherche d'un élément à l'intérieur :

    - d'une **liste** : temps **proportionnel** à la taille de la liste (ordre de complexité linéaire, $O(n)$)
    - d'un **dictionnaire** : temps **constant**, indépendant de la taille du dictionnaire (ordre de complexité constant, $O(1)$)

Attention : en ce qui concerne **les temps d'accès** à un élément, la structure de tableau dynamique des listes de Python fait que ce temps d'accès est aussi en temps constant (comme pour les dictionnaires). On voit alors que les listes Python ne sont pas des *listes chaînées*, où le temps d'accès à un élément est directement proportionnel à la position de cet élément dans la liste.

### 1.4 One more thing...

Intéressons-nous maintenant à ce qui semble être un peu trop miraculeux : une recherche en temps constant, quelque soit la taille du dictionnaire ?
Mesurons cette fois non pas la recherche dans le dictionnaire, mais la création de celui-ci :

```python linenums='1'
def mesures(nb):
    tps_total = 0
    for _ in range(10):
        t0 = time.time()
        lst = fabrique_liste(nb)
        delta_t = time.time() - t0
        tps_total += delta_t
    tps_moyen_lst = tps_total / 10

    tps_total = 0
    for _ in range(10):
        t0 = time.time()
        d = fabrique_dict(nb)
        delta_t = time.time() - t0
        tps_total += delta_t
    tps_moyen_d = tps_total / 10

    print(f"temps pour liste de taille {nb}           : {tps_moyen_lst}")
    print(f"temps pour un dictionnaire de taille {nb} : {tps_moyen_d}")
```

```python
>>> mesures(10**5)
temps pour liste de taille 100000           : 0.004771041870117188
temps pour un dictionnaire de taille 100000 : 0.012260651588439942
>>> mesures(10**6)
temps pour liste de taille 1000000           : 0.04549875259399414
temps pour un dictionnaire de taille 1000000 : 0.14215753078460694
>>> mesures(10**7)
temps pour liste de taille 10000000           : 0.4727184295654297
temps pour un dictionnaire de taille 10000000 : 1.302360200881958
```

La création des deux structures semble de complexité linéaire, mais elle est surtout **bien plus grande** pour un dictionnaire que pour une liste... Pourquoi ?

Parce que pour bénéficier plus tard d'une recherche en temps constant, la création du dictionnaire demande beaucoup de calculs...

Petit détour par les fonctions de hachage :

### 2. Fonctions de hachage  *(hors-programme)*

Tout ce qui suit est hors-programme de Terminale, mais permet de comprendre comment Python arrive à faire de la recherche en temps constant quelle que soit la taille du dictionnaire.

Il est important de se rappeler qu'un dictionnaire n'est pas **ordonné** (contrairement à l'objet «dictionnaire» de la vie courante, où chaque mot est classé suivant l'ordre alphabétique). 

On n'accède pas à une valeur suivant sa position, mais suivant sa clé.

Dans une liste, lorsqu'on veut savoir si un élément appartient à une liste (problème de la *recherche d'élément*), il n'y a pas (dans le cas général) de meilleure méthode que le parcours exhaustif de tous les éléments de la liste jusqu'à (éventuellement) trouver la valeur cherchée.

Dans un dictionnaire, on pourrait s'imaginer qu'il va falloir parcourir toutes les clés et regarder les valeurs correspondantes. Il n'en est rien.  
Pour comprendre cela nous allons faire un petit détour par les **fonctions de hachage.**

### 2.1 Vérification de l'intégrité

Lorsque vous téléchargez un fichier important et que vous souhaitez vérifier qu'il n'a pas été corrompu lors du téléchargement (ou avant), vous avez parfois la possibilité de vérifier l'intégrité de votre fichier téléchargé, en calculant une «empreinte» de votre fichier et en la comparant avec celle que vous êtes censée obtenir :

Voilà par exemple ce qui apparaît sur la page de téléchargement d'une iso d'ubuntu 18.04 :

La clé MD5 proposée pour chaque fichier est le résultat ce que **doit** donner le fichier (ici une iso d'environ 1,9 Go) lorsqu'il est «haché» par la fonction MD5. Dans notre cas, si nous téléchargeons 
```ubuntu-18.04.3-desktop-amd64.iso```, nous devons calculer l'empreinte du fichier téléchargé et vérifier que nous obtenons bien ```72491db7ef6f3cd4b085b9fe1f232345``` :

Essayons :

La clé calculée sur l'ordinateur correspond bien à celle indiquée sur le site de téléchargement : le fichier est intègre.

    Téléchargez le fichier banniere.png et dans un Terminal, calculez son empreinte MD5 :

    ```
    eleve@linux:~/ md5sum banniere.png
    2895bae45eb0ab36a2a8324c0208ad95  banniere.png

    ```
    
    Si votre fichier ```banniere.png``` a été convenablement téléchargé, votre empreinte devra être égale à ```2895bae45eb0ab36a2a8324c0208ad95```.

### 2.2 Mécanisme de la fonction de hachage

Quelle que soit la taille du fichier donné en entrée, la fonction MD5 va le réduire à un mot de 128 bits.
Ce mot binaire de 128 bits est représenté par une chaîne de 32 caractères (en hexadécimal, de 0 à f). Il y a donc $2^{128}$ (de l'ordre de $10^{39}$) empreintes MD5 différentes, ce qui rend quasiment impossible le fait d'avoir un mauvais fichier qui donnerait (par un très très mauvais hasard) la bonne empreinte.

Le mécanisme effectif de calcul de la fonction MD5 est très complexe : une explication en est donnée ici.

Il est évidemment **impossible** de revenir en arrière et de recréer le fichier original à partir de l'empreinte MD5. Dans le cas contraire, cela voudrait dire qu'on est capable de compresser *sans perte* un fichier de 1,9 Go en une chaîne de 128 bits. Cette impossibilité de trouver une fonction réciproque à la fonction de hachage est très importante en cryptographie.

En effet, les simples chaînes de caractères peuvent aussi être transformées par une fonction de hachage :

*(on pourra aussi jouer avec le fabuleux site https://gchq.github.io/CyberChef du GHCQ)*

Quel est l'intérêt de hacher une chaîne de caractère ? La conservation des mots de passe !!!

### 2.3 Le stockage des mots de passe

Les sites qui nécessitent une authentification par login / mot de passe ne conservent pas en clair les mots de passe sur leur serveur. La moindre compromission de leur serveur serait en effet dramatique. Ce qui est conservé est l'empreinte du mot de passe après son passage par une fonction de hachage.  
Par exemple, un site où notre mot de passe serait ```vive la NSI``` conserverait dans ses bases de données l'empreinte ```e74fb2f94c052bbf16cea4a795145e35```.  
À chaque saisie du mot de passe côté client, l'empreinte est recalculée (côté serveur), puis comparée avec l'empreinte stockée. 
Lors du transit du mot de passe, le chiffrement effectué par le protocole ```https``` assure la protection en cas d'interception.
De cette façon, si le serveur est compromis, la non-réversibilité de la fonction de hachage assure que le mot de passe ne peut pas être retrouvé par les attaquants.

### 2.4 La non-réversibilité de la fonction de hachage  (vraiment ?)

Prenons notre empreinte MD5 ```e74fb2f94c052bbf16cea4a795145e35``` et allons fureter du côté de (par exemple) https://md5.gromweb.com/

Notre empreinte ne résiste pas bien longtemps...  

Calculez l'empreinte de ```FrançoisMauriacFTW``` et demandez au site de tenter de l'inverser. Que constatez-vous ? 

Les empreintes des mots de passe les plus fréquents sont stockées dans des tables (qu'on appelle *rainbow tables* ou *tables arc-en-ciel*) qui rendent possibles le déchiffrage de ces empreintes.

Pour contrer cela, les cryptographes rajoutent des caractères avant hachage (le *sel*), et choisissent surtout des bonnes fonctions de hachage. MD5 et SHA-1 ne sont plus utilisées, on préfère maintenant SHA-256 (voir ici).

### 3. Retour aux dictionnaires

Quel est le lien entre les fonctions de hachage et les  dictionnaires ??? 

L'idée essentielle est que chaque clé est hachée pour donner une empreinte unique, qui est ensuite transformée en un indice de positionnement dans un tableau.

Le dictionnaire :

```python
d = {"pommes":3, "poires":0, "bananes":5}
```

serait donc par exemple implémenté dans un tableau comme celui-ci :

On peut remarquer que ce tableau laisse beaucoup de cases vides.

Si je souhaite ensuite accéder à l'élément ```d["kiwis"]``` :

- le hash de la chaîne ```"kiwis"``` est calculé. Par exemple, ```4512d2202```.
- l'indice de la position (éventuelle) de la clé ```"kiwis"``` dans mon dictionnaire est calculé à partir de ce hash ```4512d2202```. Dans notre exemple, cela pourrait donner l'indice 3.
- Python accède **directement** à cet indice du tableau :
    - si la valeur de la clé sur cette ligne du tableau est None, cela signifie que ```"kiwis"``` n'est pas une clé existante du tableau. C'est notre cas ici car il n'y a rien à la ligne 3.
    - si la valeur de la clé sur cette ligne du tableau est bien ```"kiwis"```, la valeur correspondante est renvoyée.

En résumé, Python sait toujours où aller chercher un élément de son dictionnaire : soit il le trouve à l'endroit calculé, soit il n'y a rien à cet endroit calculé, ce qui veut dire que l'élément ne fait pas partie du dictionnaire. 

Par ce mécanisme, l'accès à un élément du dictionnaire se fait toujours en temps **constant**.

Il existe une manière de «voir» que Python utilise une fonction de hachage pour implémenter un dictionnaire :

```python
mondico = {}

### une liste peut-elle être une clé ?

mondico[[2,5]] = "loulou"
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

     in 
          8 
          9 # une liste peut-elle être une clé ?
    - 10 mondico[[2,5]] = "loulou"
    

    TypeError: unhashable type: 'list'

Le message d'erreur est explicite : le type ```list``` que nous avons voulu utiliser comme clé n'est pas hachable, car c'est un type d'objet pouvant être modifié a posteriori tout en gardant la même référence (on dit que c'est un objet **mutable**):

```python
a = [3, 6, 8]
print(id(a))
a.append(12)
print(id(a))
```

    139646950377032
    139646950377032

Ce changement de valeur tout en gardant la même référence détruirait le principe associant à une clé unique une position unique dans le tableau implémentant le dictionnaire.

Ce problème ne se pose pas si la variable désigne une chaîne de caractères, ou un nombre :

```python
a = 2020
print(id(a))
a += 1
print(id(a))

```

    139646916523440
    139646916523504

Un variable contenant un entier est donc un objet **immuable** car si on modifie la valeur de l'entier, la référence de la variable changera aussi. Comme un dictionnaire a besoin d'avoir des clés dont les références soient définitives, seuls les objets **immuables** peuvent donc servir de clés dans les dictionnaires.

### Exercices sur les dictionnaires

On considère la liste suivante :

    ```lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']``` 

    Quel est le **chiffre** qui revient le plus fréquemment dans cette liste ?

     
    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']

        occ = {}
        maxi = 0
        for nombre in lst:
            for chiffre in nombre:
                if chiffre in occ:
                    occ[chiffre] += 1
                else:
                    occ[chiffre] = 1
                if occ[chiffre] > maxi:
                    maxi = occ[chiffre]
                    chiffre_max = chiffre

        print(chiffre_max, 'est le chiffre le plus fréquent')
        print('il apparait', maxi, 'fois')

        ```        
    """
    )
    }}

    Exercice 2 du sujet Centres Etrangers J1 2021

    {{
    correction(True,
    """
\"Correction Q1.a. \" 
        ```flotte[26]``` renvoie  ```{'type' : 'classique', 'etat' : 1, 'station' : 'Coliseum'}```
    """
    )
    }}

    Créer une fonction ```inverse_md5``` qui va chercher dans un dictionnaire (construit préalablement) le mot correspondant au hash donné en paramètre.

    À quel mot de passe correspond le hash ```33da7a40473c1637f1a2e142f4925194``` ?

    **Exemple :** 
    ```
    >>> inverse_md5('0571749e2ac330a7455809c6b0e7af90')
    >>> 'sunshine'
    ```

    **Aide :**

    - liste de 1000 mots de passe fréquents : ici
    - comment lire / convertir le contenu d'un fichier dans une liste de ```string``` :
    ```python
    lst = open("monfichier.txt").read().splitlines()
    ```
    - comment calculer du MD5 en Python : 
    ```python
    import hashlib
    result = hashlib.md5('azerty'.encode())
    print(result.hexdigest())
    ```

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        import hashlib

        lst = open('extraitrockyou.txt').read().splitlines()
        inv_hash = {}
        for mdp in lst:
            hsh = hashlib.md5(mdp.encode()).hexdigest()
            inv_hash[hsh] = mdp

        def inverse_md5(hsh):
            return inv_hash[hsh]
        ```
    """
    )
    }}

    Le nombre d’occurrences d’un caractère dans une chaîne de caractère est le nombre
    d’apparitions de ce caractère dans la chaîne.

    Exemples :

    - le nombre d’occurrences du caractère `‘o’` dans `‘bonjour’` est 2 ;
    - le nombre d’occurrences du caractère `‘b’` dans `‘Bébé’` est 1 ;
    - le nombre d’occurrences du caractère `‘B’` dans `‘Bébé’` est 1 ;
    - le nombre d’occurrences du caractère `‘ ‘` dans `‘Hello world !’` est 2.

    On cherche les occurrences des caractères dans une phrase. On souhaite stocker ces
    occurrences dans un dictionnaire dont les clefs seraient les caractères de la phrase et
    les valeurs le nombre d’occurrences de ces caractères.

    Par exemple : avec la phrase `'Hello world !'` le dictionnaire est le suivant :

    `{'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}`

    *L’ordre des clefs n’a pas d’importance.*

    Écrire une fonction `nbr_occurrences` prenant comme paramètre une chaîne de
    caractères `chaine` et renvoyant le dictionnaire des nombres d’occurrences des
    caractères de cette chaîne.    

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        def nbr_occurrences(chaine):
            nb_occ = {}
            for caractere in chaine:
                if caractere in nb_occ:
                    nb_occ[caractere] += 1
                else:
                    nb_occ[caractere] = 1
            return nb_occ
        ```
    """
    )
    }}

    Écrire une fonction `ajoute_dictionnaires` qui prend en paramètres deux
    dictionnaires `d1` et `d2` dont les clés sont des nombres et renvoie le dictionnaire `d` défini de
    la façon suivante :

    - Les clés de `d` sont celles de `d1` et celles de `d2` réunies.
    - Si une clé est présente dans les deux dictionnaires `d1` et `d2`, sa valeur associée
    dans le dictionnaire `d` est la somme de ses valeurs dans les dictionnaires `d1` et `d2`.
    - Si une clé n’est présente que dans un des deux dictionnaires, sa valeur associée
    dans le dictionnaire `d` est la même que sa valeur dans le dictionnaire où elle est
    présente.

    Exemples :

    ```python
    >>> ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11})
    {1: 5, 2: 16, 3: 11}
    >>> ajoute_dictionnaires({}, {2: 9, 3: 11})
    {2: 9, 3: 11}
    >>> ajoute_dictionnaires({1: 5, 2: 7}, {})
    {1: 5, 2: 7}
    ```

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        def ajoute_dictionnaires(d1, d2):
            d = {}
            for cle in d1:
                d[cle] = d1[cle]
            for cle in d2:
                if cle in d:
                    d[cle] += d2[cle]
                else:
                    d[cle] = d2[cle]
            return d
        ```
    """
    )
    }}
ex1J2AN2025">"

    Exercice 1 du sujet Amérique du Nord J2 2025

    **Partie A**

        

        

    ```python linenums='1'
    def nb_occurrences(tab, i):
        '''
        Renvoie un dictionnaire qui associe, à chaque élément
        apparaissant dans tab entre la position 3i
        incluse et la position 3(i + 1) exclue,
        son nombre d'occurrences.
        >>> nb_occurrences([0, 0, 1, 1, 0, 1, 0, 1, 1], 1)
        {1: 2, 0: 1}
        '''
        nb_occ = {}
        for j in range(3 * i, 3 * (i + 1)):
            x = tab[j]
            if x in nb_occ:
                ...
            else:
                ...
        return nb_occ

    ```

    {{
    correction(True,
    """
\"Correction Q3 \"
        ```python linenums='1'
        def nb_occurrences(tab, i):
            '''
            Renvoie un dictionnaire qui associe, à chaque élément
            apparaissant dans tab entre la position 3i
            incluse et la position 3(i + 1) exclue,
            son nombre d'occurrences.
            >>> nb_occurrences([0, 0, 1, 1, 0, 1, 0, 1, 1], 1)
            {1: 2, 0: 1}
            '''
            nb_occ = {}
            for j in range(3 * i, 3 * (i + 1)):
                x = tab[j]
                if x in nb_occ:
                    nb_occ[x] += 1
                else:
                    nb_occ[x] = 1
            return nb_occ

        ```
        
    """
    )
    }} 

    ```python linenums='1'
    def majorite(dict):
        '''
        Renvoie une clé du dictionnaire dict pour laquelle la
        valeur associée est la plus grande.
        Précondition : dict est un dictionnaire dont toutes
        les valeurs sont positives.
        '''
        cle_max = None
        valeur_max = -1
        for cle in dict.keys():
            ...
                ...
                ...
        return cle_max
    ```

     

    **Partie B**

      

    

      

    **Partie C**

      

    ```python linenums='1'

    hamming_4_7 = [
    [0,0,0,0,0,0,0], [1,1,0,1,0,0,1],
    [0,1,0,1,0,1,0], [1,0,0,0,0,1,1],
    [1,0,0,1,1,0,0], [0,1,0,0,1,0,1],
    [1,1,0,0,1,1,0], [0,0,0,1,1,1,1],
    [1,1,1,0,0,0,0], [0,0,1,1,0,0,1],
    [1,0,1,1,0,1,0], [0,1,1,0,0,1,1],
    [0,1,1,1,1,0,0], [1,0,1,0,1,0,1],
    [0,0,1,0,1,1,0], [1,1,1,1,1,1,1]]

    def corriger_erreur(code_recu):
        if code_recu in hamming_4_7:
            return code_recu
        else:
            # Copie du code reçu créée par compréhension
            code = ...
            for indice in range(7):
                # Inversion du bit d'indice courant
                code[indice] = (code[indice] + 1) ...
                if code in hamming_4_7:
                    return code
                else:
                    # Réinit. du bit d'indice courant
                    code[indice] = ...
    ```

    Tests :
    ```python
    >>> corriger_erreur([1,1,0,1,0,0,1])
    [1, 1, 0, 1, 0, 0, 1]
    >>> corriger_erreur([1,0,1,0,0,0,0])
    [1, 1, 1, 0, 0, 0, 0]
    ```

     

      

    ```python linenums='1'
    def decode(arbre, code, i):
        '''
        Descend dans l'arbre binaire arbre en lisant le
        tableau code à partir de l'indice i et renvoie
        le mot étiquetant la feuille atteinte.
        Précondition : arbre est un arbre binaire
        de hauteur len(code) - i
        '''
        if i == len(code):
            return arbre.etiquette
        if code[i] == 0:
            return decode(...)
        if code[i] == 1:
            return decode(...)
    ```

## Arbres

### 1.1 Vocabulaire

Un arbre est une structure hiérarchique de données, composée de nœuds. Si on adopte le vocabulaire des graphes, un arbre est un graphe non orienté, connexe, sans cycle, et dans lequel un nœud joue le rôle de racine.

- Chaque **nœud** a exactement un seul **nœud père**, à l'exception du nœud **racine** qui est le seul nœud à ne pas avoir de père. (oui, **la** racine d'une arbre est **en haut**)

- Chaque nœud peut avoir un nombre quelconque de **fils**, dont il est le père.
- Les nœuds qui n'ont pas de fils sont appelés les **feuilles** (ou nœuds externes).
- Les nœuds qui ne sont pas des feuilles sont des **nœuds internes**.
- Le nom de chaque nœud est appelé son **étiquette**.

**Exemples :**
dans l'arbre ci-dessus,

- C est la racine, E, Z A et G sont les feuilles.
- K est le père de A et G.
- F est le père de Z.
- C est le père de B et K
- B est le père de E et F.

### 1.2 Exemples d'arbres

#### 1.2.1 La famille royale britannique (avant le 08 septembre 2022)

Redessinez de manière plus schématique cet arbre. Pour quelle raison cet arbre a-t-il été modifié par rapport à sa version orginale (voir ici ), qui laissait apparaître les parents de chaque enfant ?

#### 1.2.2 Le DOM d'une page web
DOM : Document Object Model

#### 1.2.3 L'arborescence d'un disque dur
Les systèmes Unix (MacOS ou GNU/Linux) organisent leur disque dur suivant l'arborescence ci-dessous :

    Quelque part à l'intérieur des dossiers contenus dans l'archive dossiers.zip se trouve un fichier ```tresor.txt```. Quel secret renferme-t-il ?

    Attention, cette recherche est à faire uniquement en ligne de commande :

    - ```ls``` : pour lister les dossiers et fichiers d'un répertoire
    - ```cd Dossier``` : pour se rendre dans le repértoire ```Dossier```
    - ```cd ..``` : pour remonter d'un niveau dans l'arborescence
    - ```unzip monarchive.zip``` : pour décompresser une archive
    - ```cat monfichier.txt``` : pour lire le contenu d'un fichier dans le terminal 
    - ```tree``` : pour afficher l'arborescence du répertoire courant
    - ```sudo apt install monprog``` : pour installer le programme ```monprog``` si celui-ci est manquant.

### 1.3 Caractéristiques d'un arbre

#### 1.3.1 Outils numériques de description

    - la **taille** d'un arbre est son nombre total de nœuds. Ici, elle vaut 8.

    - l'**arité** d'un nœud est son nombre de fils. Ici, l'arité de B vaut 2, celle de F vaut 1, celle de Z vaut 0.

    - la **profondeur** d'un nœud est le nombre de nœuds de son chemin le plus court vers la racine. 
    Ici, la profondeur de G est 3 (G-K-C), la profondeur de B est 2 (B-C), la profondeur de Z est 4 (Z-F-B-C), la profondeur de C est 1.

    - la **hauteur** d'un arbre est la profondeur de son nœud le plus profond. 
    Ici, la hauteur de l'arbre est 4.  
        Nous prendrons comme **convention** que :  
        - si un arbre est réduit à **un seul nœud-racine**, sa hauteur sera **1**.
        - si un arbre est **vide**, sa hauteur est **0**.

*Cette convention est celle adoptée dans le sujet 0 publié le 15/12/2020. Attention, dans certains ouvrages, l'arbre vide a pour hauteur -1, et donc l'arbre réduit à un seul nœud a pour hauteur 0, donc notre arbre aurait avec cette convention une hauteur 3.*

#### 1.4 Arbres binaires

    Un arbre binaire est un arbre dont chaque nœud possède **au plus** deux fils.

L'arbre généalogique de la famille royale britannique n'est pas un arbre binaire. 

L'arbre ci-dessous est lui un arbre binaire.

#### 1.4.1 Sous-arbres d'un arbre binaire

Chaque nœud d'un arbre binaire ne pouvant pas avoir plus de 2 fils, il est possible de séparer le «dessous» de chaque nœud en deux sous-arbres (éventuellement vides) : le **sous-arbre gauche** et le **sous-arbre droit**.

- Les deux sous-arbres représentés ici sont les sous-arbres du nœud-racine T. 
- Le nœud O admet comme sous-arbre gauche le nœud H et comme sous-arbre droit le nœud N.
- Les feuilles P, H et N ont pour sous-arbre gauche et pour sous-arbre droit l'**arbre vide**.

#### 1.4.3 Cas des arbres binaires complets

On rencontre très souvent des arbres binaires dits **complets** parce qu'aucun des fils gauche ou droit n'est manquant.

**Taille d'un arbre complet de hauteur $h$ :**
$1 + 2 + 2^2 + 2^3 + \dots + 2^{h-1} = 2^{h} - 1$

*preuve* : ceci est la somme $S$ des $h$ premiers termes d'une suite géométrique de raison 2 et de premier terme 1, d'où $S= \frac{1-2^{h}}{1-2} = 2^{h} -1$.

Un arbre complet de hauteur $h$ (en prenant la convention que l'arbre vide a pour hauteur 0) a donc une taille égale à $2^{h}-1$.

**Remarque :** On en déduit une inégalité classique sur l'encadrement de la taille $t$ d'un arbre binaire (non nécessairement complet) de hauteur $h$ :

$$h \leqslant t \leqslant 2^{h}-1$$

### 2. Parcours d'arbres

Les arbres étant une structure hiérarchique, leur utilisation implique la nécessité d'un **parcours** des valeurs stockées. Par exemple pour toutes les récupérer dans un certain ordre, ou bien pour en chercher une en particulier.  

Il existe plusieurs manières de parcourir un arbre.

### 2.1 Parcours en largeur d'abord (BFS)

*BFS : Breadth First Search*
 
    Le parcours en largeur d'abord est un parcours étage par étage (de haut en bas) et de gauche à droite.

L'ordre des lettres parcourues est donc T-Y-O-P-H-N.

Les trois parcours que nous allons voir maintenant sont des parcours en **profondeur d'abord**, ou **DFS** (*Depth First Search*). Ce qui signifie qu'un des deux sous-arbres sera totalement parcouru avant que l'exploration du deuxième ne commence.

### 2.2 Parcours préfixe

Le parcours **préfixe** est un parcours **en profondeur d'abord**. 

    (parfois aussi appelé *préordre*)

    - Chaque nœud est visité **avant** que ses fils le soient.
    - On part de la racine, puis on visite son fils gauche (et éventuellement le fils gauche de celui-ci, etc.) avant de remonter et de redescendre vers le fils droit.

L'ordre des lettres parcourues est donc T-Y-P-O-H-N.

### 2.3 Parcours infixe

Le parcours **infixe** est aussi un parcours en profondeur d'abord.
 
    (parfois aussi appelé *en ordre*)

    - Chaque nœud est visité **après son fils gauche mais avant son fils droit**.
    - On part donc de la feuille la plus à gauche et on remonte par vagues sucessives. Un nœud ne peut pas être visité si son fils gauche ne l'a pas été.

L'ordre des lettres parcourues est donc P-Y-T-H-O-N.

### 2.4 Parcours postfixe

Le parcours **postfixe** est aussi un parcours en profondeur d'abord.

    (parfois aussi appelé **post-ordre** ou encore **suffixe**)

    - Chaque nœud est visité **après** ses fils le soient.
    - On part donc de la feuille la plus à gauche, et on ne remonte à un nœud père que si ses fils ont tous été visités. 

L'ordre des lettres parcourues est donc P-Y-H-N-O-T.

### 2.5 Comment ne pas se mélanger entre le pré / in / post fixe ?

- *pré* veut dire *avant*
- *in* veut dire *au milieu*
- *post* veut dire *après*

Ces trois mots-clés parlent de la place du **père** par rapport à ses fils. 
Ensuite, il faut toujours se souvenir qu'on traite le fils gauche avant le fils droit.

- préfixe : le père doit être le premier par rapport à ses fils.
- infixe : le père doit être entre son fils gauche (traité en premier) et son fils droit.
- postfixe : le père ne doit être traité que quand ses deux fils (gauche d'abord, droite ensuite) l'ont été.

Un parcours préfixe commencera toujours par la racine, alors qu'un parcours postfixe finira toujours par la racine. Dans un parcours infixe, la racine sera «au milieu» (pas nécessairement parfaitement).

        Donner le rendu de chaque parcours :

        1. Parcours en largeur 
        2. Parcours préfixe
        3. Parcours infixe
        4. Parcours postfixe

        largeur : 1 2 3 4 5 6 7 8 9

        préfixe : 1 2 4 5 7 8 3 6 9

        infixe : 4 2 7 5 8 1 3 9 6

        postfixe : 4 7 8 5 2 9 6 3 1

        Donner le rendu de chaque parcours :

        1. Parcours en largeur 
        2. Parcours préfixe
        3. Parcours infixe
        4. Parcours postfixe

        largeur : 9 8 7 6 2 5 1 4 3

        préfixe : 9 8 6 2 1 7 5 4 3

        infixe : 6 8 1 2 9 7 4 5 3

        postfixe : 6 1 2 8 4 3 5 7 9

### 3.1 En utilisant la Programmation Orientée Objet

Le but est d'obtenir l'interface ci-dessous.

Il est à remarquer que ce que nous allons appeler «Arbre» est en fait un nœud et ses deux fils gauche et droit.

    ```python
    >>> a = Arbre(4) # pour créer l'arbre dont le nœud a pour valeur 4,
                # et dont les sous-arbres gauche et droit sont None
    >>> a.left = Arbre(3) # pour donner la valeur 3 au nœud du sous-arbre gauche de a
    >>> a.right = Arbre(1) # pour donner la valeur 1 au nœud du sous-arbre droit de a
    >>> a.right.data # pour accéder à la valeur du fils droit de a
    ```

    Dessinez l'arbre créé par les instructions suivantes :
    ```python
    >>> a = Arbre(4)
    >>> a.left = Arbre(3)
    >>> a.right = Arbre(1)
    >>> a.right.left = Arbre(2)
    >>> a.right.right = Arbre(7)
    >>> a.left.left = Arbre(6)
    >>> a.right.right.left = Arbre(9)
    ```

    

        

**:star: Implémentation :star:**

⯈ **Principe** : nous allons créer une classe ```Arbre```, qui contiendra 3 attributs : 

- ```data``` : la valeur du nœud (de type ```Int```)
- ```left``` : le sous-arbre gauche (de type ```Arbre```)
- ```right``` : le sous-arbre droit (de type ```Arbre```).

Par défaut, les attributs ```left ``` et ```right``` seront à ```None```, qui représentera l'arbre vide (ce qui n'est pas très rigoureux, car ```None``` n'est pas de type ```Arbre```...).

⯈ **Encapsulation ou pas ???** : 

Afin de respecter le paradigme de la Programmation Orientée Objet, nous devrions jouer totalement le jeu de l'**encapsulation** en nous refusant d'accéder directement aux attributs.

Pour cela  il faut construire des méthodes permettant d'accéder à ces attributs (avec des **getters**, ou **accesseurs** en français) ou de les modifier (avec des **setters**, ou **mutateurs** en français) .

#### 3.1.1 Implémentation avec encapsulation

    ```python linenums='1'
    class Arbre:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def set_left(self, sousarbre): # mutateur
            self.left = sousarbre

        def set_right(self, sousarbre): # mutateur
            self.right = sousarbre  

        def get_left(self): # accesseur
            return self.left

        def get_right(self): # accesseur
            return self.right

        def get_data(self): # accesseur
            return self.data
    ```

L'implémentation précédente permet d'utiliser les instructions de l'exercice précédent et de vérifier que l'arbre a bien été créé.

```python
>>> a = Arbre(4)
>>> a.set_left(Arbre(3))
>>> a.set_right(Arbre(1))
>>> a.get_right().set_left(Arbre(2))
>>> a.get_right().set_right(Arbre(7))
>>> a.get_left().set_left(Arbre(6))
>>> a.get_right().get_right().set_left(Arbre(9))
```

```python
>>> a
   
```

```python
>>> a.get_right().get_left().get_data()
   2
```

#### 3.1.1 Implémentation sans encapsulation

    ```python linenums='1'
    class Arbre:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    ```

C'est déjà fini !

```python
a = Arbre(4)
a.left = Arbre(3)
a.right = Arbre(1)
a.right.left = Arbre(2)
a.right.right = Arbre(7)
a.left.left = Arbre(6)
a.right.right.left = Arbre(9)
```

```python
>>> a
   
```

```python
>>> a.right.left.data
   2
```

On voit que l'implémentation avec accès direct aux attributs est beaucoup plus simple et rapide. Néanmoins, elle peut être considérée comme incorrecte dans certains langages qui obligent à passer par des accesseurs ou mutateurs pour lire ou modifier les attributs.

#### 3.1.2 Représentation graphique en console

La méthode ```__repr__``` suivante (qui n'est pas à connaître) permet d'avoir un semblant de représentation graphique de l'arbre en console :

```python linenums='1'
def __repr__(self, indent = 0):
    val = self.data
    s = ' '*2*indent + '|' + '_' + str(val) + '\n'
    if self.left is not None:
        s += self.left.__repr__(indent + 1)
    if self.left is None and self.right is not None:
        s += ' '*(2*indent+2) + '|' + '_' + 'None' + '\n'     

    if self.right is not None:
        s += self.right.__repr__(indent + 1)
    if self.right is None and self.left is not None:
        s += ' '*(2*indent+2) + '|' + '_' + 'None' + '\n'  
   
    return s
```

La représentation de cet arbre :

donnera alors :

```python
>>> a
|_4
  |_3
    |_6
    |_None
  |_1
    |_2
    |_7
      |_9
      |_None
```

### 3.2 Implémentation à partir de tuples imbriqués

Un arbre peut se représenter par le tuple ```(valeur, sous-arbre gauche, sous-arbre droit)```.
    L'arbre ci-dessous :
    
    est représenté par le tuple :

    ```python
    >>> a = (2, (8, (6,(),()), (9,(),())), (1, (7, (),()), ()))
    ```

Le sous-arbre gauche est alors ```a[1]``` et le sous-arbre droit est ```a[2]```.

```python
>>> a[1]
(8, (6, (), ()), (9, (), ()))
>>> a[2]
(1, (7, (), ()), ())
```

    

    Écrire le tuple représentant l'arbre ci-dessous.

### 3.3 Implémentation à partir d'une «simple» liste

De manière plus surprenante, il existe une méthode pour implémenter un arbre binaire (qui est une structure hiérarchique) avec une liste (qui est une structure linéaire). 
Ceci peut se faire par le biais d'une astuce sur les indices :

**Les fils du nœud d'indice i sont placés aux indice 2i+1 et 2i+2**.

Cette méthode est connue sous le nom de «méthode d'Eytzinger», et utilisée notamment en généalogie pour numéroter facilement les individus d'un arbre généalogique.

**Exemple :**

Pour comprendre facilement la numérotation, il suffit de s'imaginer l'arbre complet (en rajoutant les fils vides) et de faire une numérotation en largeur, niveau par niveau :

    Si on note Δ le sous-arbre vide, dessiner l'arbre représenté par la liste :
    ```python
    a = [3, 4, Δ, 7, 5]
    ```       
        
    

**Remarque :** parfois (comme dans le sujet 0...) la racine de l'arbre est placée à l'indice 1. Dans ce cas, les fils du nœud d'indice i sont placés aux indices 2i et 2i+1.

### 4. Utilisation de l'implémentation : parcours, taille...

Dans toute la suite, sauf mention contraire, on utilisera l'implémentation en Programmation Orientée Objet, en version sans encapsulation (la plus simple).
Nous allons créer des fonctions renvoyant les différents parcours d'un arbre, ou encore sa taille, sa hauteur, son nombre de feuilles... Toutes ses fonctions exploiteront la structure **récursive** d'un arbre.

**Rappel de l'implémentation :**

```python linenums='1'
class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

```

### 4.1 Parcours préfixe, infixe, postfixe

Dans un premier temps nous allons écrire ces parcours de manière récursive. Nous souhaitons afficher les sommets, donc nous utiliserons ```print```. Et deux appels récursifs... 

#### 4.1.1 Parcours préfixe

{#

    ```python
    def prefixe(arbre):
        ...
    ```
#}

    ```python linenums='1'
    def prefixe(arbre):
        if arbre is None :
            return None
        print(arbre.data, end = '-')
        prefixe(arbre.left)
        prefixe(arbre.right)

    ```

Exemple avec l'arbre 

```python linenums='1'
a = Arbre(9)
a.left = Arbre(8)
a.right = Arbre(7)
a.left.left = Arbre(6)
a.left.right = Arbre(2)
a.right.right = Arbre(5)
a.left.right.left = Arbre(1)
a.right.right.left = Arbre(4)
a.right.right.right = Arbre(3)
```

```python
>>> prefixe(a)
9-8-6-2-1-7-5-4-3-
```

#### 4.1.2 Parcours infixe
{#

    ```python
    def infixe(arbre):
        ...
    ```
#}

    ```python
    def infixe(arbre):
        if arbre is None :
            return None
        infixe(arbre.left)
        print(arbre.data, end = '-')
        infixe(arbre.right)
    ```

```python
>>> infixe(a)
6-8-1-2-9-7-4-5-3-
```

#### 4.1.3 Parcours postfixe
{#

    ```python
    def postfixe(arbre):
        ...
    ```
#}

    ```python
    def postfixe(arbre):
        if arbre is None :
            return None
        postfixe(arbre.left)
        postfixe(arbre.right)
        print(arbre.data, end = '-')
    ```

```python
>>> postfixe(a)
6-1-2-8-4-3-5-7-9-
```
 
    - Regardez et appréciez cette vidéo.
    - À l'aide de la vidéo, codez le parcours infixe en itératif.

### 4.2 Calcul de la taille d'un arbre

Rappel : la taille d'un arbre est le nombre de ses nœuds.

{#

    ```python
    def taille(arbre):
        ...

 ```
#} 

    ```python
    def taille(arbre):
        if arbre is None:
            return 0
        return 1 + taille(arbre.left) + taille(arbre.right)
    ```

Exemple avec l'arbre 

```python linenums='1'
a = Arbre(9)
a.left = Arbre(8)
a.right = Arbre(7)
a.left.left = Arbre(6)
a.left.right = Arbre(2)
a.right.right = Arbre(5)
a.left.right.left = Arbre(1)
a.right.right.left = Arbre(4)
a.right.right.right = Arbre(3)
```

```python
>>> taille(a)
9
```

### 4.3 Calcul de la hauteur d'un arbre

Rappel : on prendra comme convention que l'arbre vide a pour hauteur 0.
{#

    ```python
    def hauteur(arbre):
        ...
    ```
#}

    ```python
    def hauteur(arbre):
        if arbre is None:
            return 0
        else:
            return 1 + max(hauteur(arbre.left), hauteur(arbre.right))
    ```

```python
>>> hauteur(a)
4
```

### 4.4 Calcul du nombre de feuilles d'un arbre

Rappel : une feuille est un nœud d'arité 0, autrement dit sans fils gauche ni fils droit.

{#

    ```python
    def nb_feuilles(arbre):
        ...
    ```

#}

    ```python
    def nb_feuilles(arbre):
        if arbre is None:
            return 0
        if (arbre.left is None) and (arbre.right is None):
            return 1
        return nb_feuilles(arbre.left) +  nb_feuilles(arbre.right)
    ```

```python
>>> nb_feuilles(a)
4
```

### 4.5 Recherche d'une valeur dans un arbre

On renverra ```True``` ou ```False``` en fonction de la présence ou non de la valeur dans l'arbre.

{#

    ```python
    def recherche(arbre, valeur):
        ...
  
    ```
#}

    ```python
    def recherche(arbre, valeur):
        if arbre is None:
            return False
        if arbre.data ==  valeur:
            return True
        return recherche(arbre.left, valeur) or recherche(arbre.right, valeur)
    ```

    

```python
>>> recherche(a, 2)
True
>>> recherche(a, 45)
False
```

### 4.6 Parcours en largeur

Le parcours en largeur (BFS) est le plus simple à faire visuellement : mais il est plus difficile à coder que les parcours préfixe, infixe, postfixe.  
Il est nécessaire d'utiliser une **file**  :

- On place l'arbre dans la file.
- Tant que la file n'est pas vide, on procède comme suit :
    - On défile, donc on récupère l'arbre situé en haut de la file.  
    - Si cet arbre n'est pas vide :
        - On garde son étiquette.
        - On enfile son sous-arbre gauche, puis son sous-arbre droit.

On importera l'objet ```Queue()``` du module ```queue``` de Python, qui permet de  :

- créer une file vide avec ```file = Queue()```
- défiler un élément par ```file.get()```
- enfiler l'élément ```a``` par ```file.put(a)```
- savoir si la file est vide par le booléen ```file.empty()```

```python

### ne pas oublier de remonter plus haut dans le document pour relancer la classe Arbre

a = Arbre(8)
a.left = Arbre(4)
a.right = Arbre(5)
a.left.left = Arbre(2)
a.left.right = Arbre(1)
a.right.right = Arbre(3)
```

    ```python
    from queue import Queue

    def BFS(arbre):        
        file = Queue()
        file.put(arbre)
        sol = []
        while not file.empty():
            a = file.get()
            if a is not None :
                sol.append(a.data)
                file.put(a.left)
                file.put(a.right)
        return sol
    ```

```python
>>> BFS(a)
[8, 4, 5, 2, 1, 3]
```

### 5. Arbres binaires de recherche (ABR)

Un **arbre binaire de recherche** est un arbre binaire dont les valeurs des nœuds (valeurs qu'on appelle étiquettes, ou clés) vérifient la propriété suivante :

    - l'étiquette d'un nœud est **supérieure ou égale** à celle de **chaque** nœud de son **sous-arbre gauche**.
    - l'étiquette d'un nœud est **strictement inférieure** à celle du **chaque** nœud de son **sous-arbre droit**.

À noter que l'arbre 3 (qui est bien un ABR) est appelé **arbre filiforme**. 

L'arbre 5 n'est pas un ABR à cause de la feuille 9, qui fait partie du sous-arbre gauche de 3 sans lui être inférieure.

**Remarque :** on pourrait aussi définir un ABR comme un arbre dont le parcours infixe est une suite croissante.

### 5.1 Déterminer si un arbre est un ABR

Employer une méthode récursive imposerait de garder en mémoire dans l'exploration des sous-arbres la valeur maximale ou minimale. Nous allons plutôt utiliser la remarque précédente, et nous servir du parcours infixe.

Méthode : récupérer le parcours infixe dans une liste, et faire un test sur cette liste.

    ```python linenums='1'
    def infixe(arbre, s = None):
        if s is None:
            s = []
        if arbre is None :
            return None
        infixe(arbre.left, s)
        s.append(arbre.data)
        infixe(arbre.right, s)
        return s

    def est_ABR(arbre):
        '''renvoie un booléen indiquant si arbre est un ABR'''
        parcours = infixe(arbre)
        return parcours == sorted(parcours) # on regarde si le parcours est égal au parcours trié 

    ```

```python

### arbres-tests

#arbre n°4
a = Arbre(5)
a.left = Arbre(2)
a.right = Arbre(7)
a.left.left = Arbre(0)
a.left.right = Arbre(3)
a.right.left = Arbre(6)
a.right.right = Arbre(8)

#arbre n°5
b = Arbre(3)
b.left = Arbre(2)
b.right = Arbre(5)
b.left.left = Arbre(1)
b.left.right = Arbre(9)
b.right.left = Arbre(4)
b.right.right = Arbre(6)

```

```python
>>> est_ABR(a)
True
>>> est_ABR(b)
False
```

### 5.2 Rechercher une clé dans un ABR

Un arbre binaire de taille $n$ contient $n$ clés (pas forcément différentes). Pour savoir si une valeur particulière fait partie des clés, on peut parcourir tous les nœuds de l'arbre, jusqu'à trouver (ou pas) cette valeur dans l'arbre. Dans le pire des cas, il faut donc faire $n$ comparaisons.

Mais si l'arbre est un ABR, le fait que les valeurs soient «rangées» va considérablement améliorer la vitesse de recherche de cette clé, puisque la moitié de l'arbre restant sera écartée après chaque comparaison.

{#

    
    ```python
    def recherche_ABR(arbre, valeur):
        ...

    ```
#}

    
    ```python
    def recherche_ABR(arbre, valeur):
        if arbre is None :
            return False
        if arbre.data == valeur :
            return True
        if valeur >> recherche_ABR(a, 8)
True
>>> recherche_ABR(a, 12)
False
```

### 5.3  Coût de la recherche dans un ABR équilibré

Imaginons un arbre équilibré de taille $n$. Combien d'étapes faudra-t-il, dans le pire des cas, pour trouver (ou pas) une clé particulière dans cet arbre ?

Après chaque nœud, le nombre de nœuds restant à explorer est divisé par 2. On retrouve là le principe de recherche dichotomique, vu en classe de Première (voir ici).

S'il faut parcourir tous les étages de l'arbre avant de trouver (ou pas) la clé recherchée, le nombre de nœuds parcourus est donc égal à la hauteur $h$ de l'arbre.

Pour un arbre complet, cette hauteur vérifie la relation $2^h -1= n$. et donc $2^h = n+1$.

$h$ est donc le «nombre de puissance de 2» que l'on peut mettre dans $n+1$. Cette notion s'appelle le logarithme de base 2 et se note $\log_2$.

Par exemple, $\log_2(64)=6$ car $2^6=64$.

Le nombre maximal de nœuds à parcourir pour rechercher une clé dans un ABR équilibré de taille $n$ est donc de l'ordre de $\log_2(n)$, ce qui est très performant !

Pour un arbre contenant 1000 valeurs, 10 étapes suffisent. Mais pour un arbre contenant un milliard de valeurs, seules 30 étapes suffisent !

Cette **complexité logarithmique** est un atout essentiel de la structure d'arbre binaire de recherche.

### 5.4  Insertion dans un ABR

L'insertion d'une clé va se faire au niveau d'une feuille, donc au bas de l'arbre. Dans la version récursive de l'algorithme d'insertion, que nous allons implémenter, il n'est pourtant pas nécessaire de descendre manuellement dans l'arbre jusqu'au bon endroit : il suffit de distinguer dans lequel des deux sous-arbres gauche et droit doit se trouver la future clé, et d'appeler récursivement la fonction d'insertion dans le sous-arbre en question.

**Algorithme :**

- Si l'arbre est vide, on renvoie un nouvel objet Arbre contenant la clé.
- Sinon, on compare la clé à la valeur du nœud sur lequel on est positionné :
    - Si la clé est inférieure à cette valeur, on va modifier le sous-arbre gauche en le faisant pointer vers ce même sous-arbre une fois que la clé y aura été injectée, par un appel récursif.
    - Si la clé est supérieure, on fait la même chose avec l'arbre de droite.
    - on renvoie le nouvel arbre ainsi créé.

{#

    ```python
    def insertion(arbre, cle):
        ...
    ```

#}

    ```python
    def insertion(arbre, cle):
        if arbre is None :
            return Arbre(cle)    
        if cle >> infixe(a)
0-2-3-5-6-7-8-
>>> a = insertion(a,4)

>>> infixe(a)
0-2-3-4-5-6-7-8-
```

La valeur 4 a donc bien été insérée au bon endroit.

---

    - Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.

### Introduction

Exercice 2 du sujet Nouvelle-Calédonie J2 2022  

    *2020, sujet 0*

    **Question  1**

    Déterminer la taille et la hauteur de l’arbre binaire suivant :
    

    

    **Question 2**  

    On décide de numéroter en binaire les nœuds d’un arbre binaire de la façon suivante :  

    - la racine correspond à 1 ;
    - la numérotation pour un fils gauche s’obtient en ajoutant le chiffre 0 à droite au numéro de son
    père ;
    - la numérotation pour un fils droit s’obtient en ajoutant le chiffre 1 à droite au numéro de son
    père ;  

    Par exemple, dans l’arbre ci-dessous, on a utilisé ce procédé pour numéroter les nœuds A, B, C, E et
    F .

    

    **a**. Dans l’exemple précédent, quel est le numéro en binaire associé au nœud G ?
    
    **b**. Quel est le nœud dont le numéro en binaire vaut 13 en décimal ?
    
    **c**. En notant $h$ la hauteur de l’arbre, sur combien de bits seront numérotés les nœuds les plus en
    bas ?
    
    **d**. Justifier que pour tout arbre de hauteur $h$ et de taille $n \geqslant 2$, on a :
    $h\leqslant n \leqslant 2^h-1$
    

    **Question 3**  
    Un arbre binaire est dit complet si tous les niveaux de l’arbre sont remplis.
    

    On décide de représenter un arbre binaire complet par un tableau de taille n + 1, où n est la taille de
    l’arbre, de la façon suivante :  

    - La racine a pour indice 1 ;
    - Le fils gauche du nœud d’indice $i$ a pour indice $2 \times i$ ;
    - Le fils droit du nœud d’indice $i$ a pour indice $2 \times i + 1$ ;
    - On place la taille $n$ de l’arbre dans la case d’indice 0.

    Répondre aux questions suivantes :  

    **a**. Déterminer le tableau qui représente l’arbre binaire complet de l’exemple précédent.
    
    **b**. On considère le père du nœud d’indice $i$ avec $i \geqslant 2$. Quel est son indice dans le tableau ?
    

    **Question 4**  

    On se place dans le cas particulier d’un arbre binaire de recherche complet où les nœuds
    contiennent des entiers et pour lequel la valeur de chaque noeud est supérieure à celles des
    noeuds de son fils gauche, et inférieure à celles des noeuds de son fils droit.

    Écrire une fonction `recherche` ayant pour paramètres un arbre `arbre` et un élément `element`. Cette
    fonction renvoie `True` si `element` est dans l’arbre et `False` sinon. L’arbre sera représenté par un tableau
    comme dans la question précédente.

    *2021, Métropole sujet 1*

    Dans cet exercice, les arbres binaires de recherche ne peuvent pas comporter plusieurs fois la
    même clé. De plus, un arbre binaire de recherche limité à un nœud a une hauteur de 1.
    On considère l’arbre binaire de recherche représenté ci-dessous (figure 1), où `val` représente un entier :

    

    **1.a** Donner le nombre de feuilles de cet arbre et préciser leur valeur (étiquette).  
    

    **1.b** Donner le sous arbre-gauche du nœud 23.
    

    **1.c** Donner la hauteur et la taille de l’arbre.
    
    **1.d** Donner les valeurs entières possibles de `val` pour cet arbre binaire de recherche.
    
    On suppose, pour la suite de cet exercice, que `val` est égal à 16.

    **2.** On rappelle qu’un parcours infixe depuis un nœud consiste, dans l’ordre, à faire un parcours
    infixe sur le sous arbre-gauche, afficher le nœud puis faire un parcours infixe sur le sous-arbre
    droit.    
    Dans le cas d’un parcours suffixe, on fait un parcours suffixe sur le sous-arbre gauche puis un
    parcours suffixe sur le sous-arbre droit, avant d’afficher le nœud.

    **a.** Donner les valeurs d’affichage des nœuds dans le cas du parcours infixe de l’arbre.  
    
    **b**. Donner les valeurs d’affichage des nœuds dans le cas du parcours suffixe de l’arbre.
    

    **3.** On considère la classe `Noeud` définie de la façon suivante en Python :

    

    **a.** Représenter l’arbre construit suite à l’exécution de l’instruction suivante :

    ```python 
    racine = Noeud(18)
    racine.insere_tout([12, 13, 15, 16, 19, 21, 32, 23])
    ```
    
    **b.** Écrire les deux instructions permettant de construire l’arbre de la figure 1. On rappelle que
    le nombre `val` est égal à 16.
    
    **c.** On considère l’arbre tel qu’il est présenté sur la figure 1. Déterminer l’ordre d’exécution des
    blocs (repérés de 1 à 3) suite à l’application de la méthode `insere(19)` au nœud racine
    de cet arbre.
        

    **4.** Écrire une méthode `recherche(self, v)` qui prend en argument un entier `v` et renvoie la
    valeur `True` si cet entier est une étiquette de l’arbre, `False` sinon.

    *2021, Métropole Candidats Libres 2*

    On rappelle qu’un arbre binaire est composé de nœuds, chacun des nœuds possédant
    éventuellement un sous-arbre gauche et éventuellement un sous-arbre droit. Un nœud
    sans sous-arbre est appelé feuille. La taille d’un arbre est le nombre de nœuds qu’il
    contient ; sa hauteur est le nombre de nœuds du plus long chemin qui joint le nœud racine
    à l’une des feuilles. Ainsi la hauteur d’un arbre réduit à un nœud, c’est-à-dire la racine,
    est 1.

    Dans un arbre binaire de recherche, chaque nœud contient une clé, ici un nombre entier,
    qui est :

    - strictement supérieure à toutes les clés des nœuds du sous-arbre gauche ;
    - strictement inférieure à toutes les clés des nœuds du sous-arbre droit.

    Un arbre binaire de recherche est dit « bien construit » s’il n’existe pas d’arbre de hauteur
    inférieure qui pourrait contenir tous ses nœuds.

    On considère l’arbre binaire de recherche ci-dessous.

    

    **1.a.** Quelle est la taille de l’arbre ci-dessus ?  

    **1.b.** Quelle est la hauteur de l’arbre ci-dessus ?

    

    **2.** Cet arbre binaire de recherche n’est pas « bien construit ». Proposer un arbre
    binaire de recherche contenant les mêmes clés et dont la hauteur est plus petite
    que celle de l’arbre initial.

    
    

    **3.** Les classes Noeud et Arbre ci-dessous permettent de mettre en œuvre en Python
    la structure d’arbre binaire de recherche. La méthode `insere` permet d’insérer
    récursivement une nouvelle clé.

    ```python linenums='1'
    class Noeud :    
        def __init__(self, cle):
            self.cle = cle
            self.gauche = None
            self.droit = None
            
        def insere(self, cle):
            if cle  self.cle :
                if self.droit == None :
                    self.droit = Noeud(cle)
                else :
                    self.droit.insere(cle)
                    
    class Arbre :        
        def __init__(self, cle):
            self.racine = Noeud(cle)

        def insere(self, cle):
            self.racine.insere(cle)

    ```

    Donner la représentation de l’arbre codé par les instructions ci-dessous.

    ```python
    a = Arbre(10)
    a.insere(20)
    a.insere(15)
    a.insere(12)
    a.insere(8)
    a.insere(4)
    a.insere(5)
    ```
    

    **4.** Pour calculer la hauteur d’un arbre non vide, on a écrit la méthode ci-dessous dans
    la classe Noeud.

    ```python
    def hauteur(self):
        if self.gauche == None and self.droit == None:
            return 1
        if self.gauche == None:
            return 1 + self.droit.hauteur()
        elif self.droit == None:
            return 1 + self.gauche.hauteur()
        else:
            hg = self.gauche.hauteur()
            hd = self.droit.hauteur()
            if hg > hd:
                return hg + 1
            else:
                return hd + 1

    ```
    Écrire la méthode `hauteur` de la classe `Arbre` qui renvoie la hauteur de
    l’arbre.

    

    **5.** Écrire les méthodes `taille` des classes `Noeud` et `Arbre` permettant de calculer
    la taille d’un arbre.

    

    **6.** On souhaite écrire une méthode `bien_construit` de la classe `Arbre` qui
    renvoie la valeur `True` si l’arbre est « bien construit » et `False` sinon.

    On rappelle que la taille maximale d’un arbre binaire de recherche de hauteur $ℎ$
    est $2^h - 1$.

    **6.a** Quelle est la taille minimale, notée `min` d’un arbre binaire de recherche
    « bien construit » de hauteur $ℎ$ ?

    {{
    correction(True,
    """
\"Correction\" 
        **6.a.** La configuration minimale d'un arbre bien construit de hauteur $h$ peut être :

        
        
        La taille minimale ```min``` est donc égale à $2^{h-1}$.
        
    """
    )
    }}
 

    **6.b** Écrire la méthode ```bien_construit``` demandée.

    {{
    correction(True,
    """
\"Correction\" 
        **6.b.** Intuitivement, un arbre est *mal construit* si sa hauteur est trop grande par rapport à sa taille (trop *étiré*).

        Donc un arbre est *mal construit* si sa taille est trop petite par rapport à sa hauteur.

        Donc un arbre de taille $t$ et de hauteur $h$ est *mal construit* si $t = 2**(h-1)
        ```        
    """
    )
    }}

    *2021, Polynésie*

    Cet exercice traite principalement du thème « algorithmique, langages et
    programmation » et en particulier les arbres binaires de recherche. La première partie
    aborde les arbres en mode débranché via l'application d'un algorithme sur un exemple.
    La suivante porte sur la programmation orientée objet. La dernière partie fait le lien avec
    les algorithmes de tri.

    **Partie A : Étude d'un exemple**

    Considérons l'arbre binaire de recherche ci-dessous :

    

    **Q1.** Indiquer quelle valeur a le nœud racine et quels sont les fils de ce nœud.

    

    **Q2.** Indiquer quels sont les nœuds de la branche qui se termine par la feuille qui a pour
    valeur 3.

    

    **Q3.** Dessiner l’arbre obtenu après l’ajout de la valeur 6.

    

        
    **Partie B : Implémentation en Python**

    Voici un extrait d’une implémentation en Python d'une classe modélisant un arbre binaire
    de recherche.

    ```python linenums='1'
    class ABR:
        """Implémentation d’un arbre binaire de recherche (ABR)"""
        def __init__(self, valeur=None):
            self.valeur = valeur
            self.fg = None
            self.fd = None

        def estVide(self):
            return self.valeur == None

        def insererElement(self, e):
            if self.estVide():
                self.valeur = e
            else:
                if e  self.valeur:
                    if self.fd:
                        self.fd.insererElement(e)
                    else:
                        self.fd = ABR(e)
    ```

    **Q1.** Expliquer le rôle de la fonction `__init__`.

    

    **Q2.** Dans cette implémentation, expliquer ce qui se passe si on ajoute un élément déjà
    présent dans l’arbre.

    

    **Q3.** Recopier et compléter les pointillés ci-dessous permettant de
    créer l’arbre de la partie A.
    ```python
    arbre = ABR(.......... )
    arbre.insererElement(2)
    arbre.insererElement(.......... )
    arbre.insererElement(7)
    arbre.insererElement(.......... )
    ```

    
   

    **Partie C : Tri par arbre binaire de recherche**

    On souhaite trier un ensemble de valeurs entières distinctes grâce à un arbre binaire de
    recherche. Pour cela, on ajoute un à un les éléments de l’ensemble dans un arbre
    initialement vide. Il ne reste plus qu’à parcourir l’arbre afin de lire et de stocker dans un
    tableau résultat les valeurs dans l’ordre croissant.

    **Q1.** Donner le nom du parcours qui permet de visiter les valeurs d’un arbre binaire de
    recherche dans l’ordre croissant.

    

    **Q2.** Comparer la complexité de cette méthode de tri avec celle du tri par insertion ou
    du tri par sélection.

    *2021, Centres Étrangers, sujet 1*

    Un arbre binaire est soit vide, soit un nœud qui a une valeur et au plus deux fils (le
    sous-arbre gauche et le sous-arbre droit).

    

    - X est un nœud, sa valeur est X.valeur
    - G1 est le fils gauche de X, noté X.fils_gauche
    - D1 est le fils droit de X, noté X.fils_droit

    Un arbre binaire de recherche est ordonné de la manière suivante :

    Pour chaque nœud X,

    - les valeurs de tous les nœuds du sous-arbre gauche sont **strictement
    inférieures** à la valeur du nœud X
    - les valeurs de tous les nœuds du sous-arbre droit sont **supérieures ou égales** à
    la valeur du nœud X.

    Ainsi, par exemple, toutes les valeurs des nœuds G1, G2 et G3 sont strictement
    inférieures à la valeur du nœud X et toutes les valeurs des nœuds D1, D2 et D3 sont
    supérieures ou égales à la valeur du nœud X.

    Voici un exemple d'arbre binaire de recherche dans lequel on a stocké dans cet ordre
    les valeurs : ```[26, 3, 42, 15, 29, 19, 13, 1, 32, 37, 30]``` 

    L'étiquette d'un nœud indique la valeur du nœud suivie du nom du nœud.
    Les nœuds ont été nommés dans l'ordre de leur insertion dans l'arbre ci-dessous.

    `'29, noeud04'` signifie que le nœud nommé `noeud04` possède la valeur 29.

    

    **Q1.** On insère la valeur 25 dans l'arbre, dans un nouveau nœud nommé nœud11.

    Recopier l'arbre binaire de recherche étudié et placer la valeur 25 sur cet arbre
    en coloriant en rouge le chemin parcouru.

    Préciser sous quel nœud la valeur 25 sera insérée et si elle est insérée en fils
    gauche ou en fils droit, et expliquer toutes les étapes de la décision.

    

    **Q2.** Préciser toutes les valeurs entières que l’on peut stocker dans le nœud fils
    gauche du nœud04 (vide pour l'instant), en respectant les règles sur les arbres
    binaires de recherche.

    

    **Q3.** Voici un algorithme récursif permettant de parcourir et d'afficher les valeurs de
    l'arbre :

    ```python
    Parcours(A)  # A est un arbre binaire de recherche
        Afficher(A.valeur)
        Parcours(A.fils_gauche)
        Parcours(A.fils_droit)
    ```

    **Q3.a.** Écrire la liste de toutes les valeurs dans l'ordre où elles seront affichées.
    

    **Q3.b.** Choisir le type de parcours d'arbres binaires de recherche réalisé parmi les
    propositions suivantes : Préfixe, Suffixe ou Infixe.

    

    **Q4.** En vous inspirant de l’algorithme précédent, écrire un algorithme Parcours2
    permettant de parcourir et d'afficher les valeurs de l'arbre A dans l'ordre
    croissant.

    

    Exercice 3 du sujet Centres Etrangers J2 - 2023

    

    

    

    

    

    

    

    

    

    

    - Fichier des mots français : gutenberg.txt
    - Instruction pour créer une liste à partir du fichier :
    ```python
    liste_mots_francais = open('gutenberg.txt').read().splitlines()
    ```
ex1J2ME2025">"
    Exercice 1 du sujet Métropole J2 2025
    
    

    

    

    

    

    

    

    ```python
    def creer_dico_occ(texte):
        '''renvoie un dictionnaire dont les clés sont les
        symboles de texte et les valeurs associées leur
        nombre d'occurences dans texte'''
        dico = {}
        for symbole in texte:
            if symbole in dico:
                dico[symbole] = ...
            else:
                dico[symbole] = ...
        return dico
    ```
    {{
    correction(True,
    """
\"Correction Q8\" 
        ```python
        def creer_dico_occ(texte):
            '''renvoie un dictionnaire dont les clés sont les
            symboles de texte et les valeurs associées leur
            nombre d'occurences dans texte'''
            dico = {}
            for symbole in texte:
                if symbole in dico:
                    dico[symbole] = dico[symbole] + 1
                else:
                    dico[symbole] = 1
            return dico
        ```
        
    """
    )
    }}

    

    ```python
    def separe(tab):
        moitie = somme_occ(tab) // 2
        somme = 0
        i = 0
        while moitie > somme:
            somme = somme + tab[i][1]
            i = i + 1
        tab1 = [tab[k] for k in range(0, i)]
        tab2 = [tab[k] for k in range(i, len(tab))]
        return tab1, tab2

    def shannon(symbole, tab):
        '''renvoie l'écriture binaire associée à symbole
        dans le tableau trié tab'''
        if len(tab) == 1:
            return ''
        else:
            t1, t2 = separe(tab)
            if symbole in [elt[0] for elt in t1]:
                return '1' + ...
            else:
                return '0' + ...
    ```
    

    

    Pour la question 12, vous pouvez utiliser la fonction ```creer_tab_trie``` ci-dessous :

    ```python
    def creer_tab_trie(dico):
        lst = []
        for cle in dico:
            lst.append((cle, dico[cle]))
        lst_triee = sorted(lst, key=lambda x:x[1])
        return lst_triee
    ```
ex3J1AN2022">"
    Exercice 3 du sujet Amérique du Nord J1 2022

## Graphes

### 1. Présentation du problème

Considérons le labyrinthe suivant :

Affectons une lettre à chaque case de ce labyrinthe.

Notre objectif est de trouver comment aller **de A en P**.

### 2. Modélisation par un graphe

Dessiner le graphe (dont les noeuds seront des lettres) qui modélise ce labyrinthe.

    Proposer deux «formes» possibles pour ce graphe.

### 3. Implémentation du graphe en Python

En utilisant la classe ```Graphe``` créée en cours, implémenter le graphe de ce labyrinthe.

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        class Graphe:
            def __init__(self, liste_sommets):
                self.liste_sommets = liste_sommets
                self.adjacents = {sommet : [] for sommet in liste_sommets}

            def ajoute_arete(self, sommetA, sommetB):
                self.adjacents[sommetA].append(sommetB)
                self.adjacents[sommetB].append(sommetA)

            def voisins(self, sommet):
                return self.adjacents[sommet]

            def sont_voisins(self, sommetA, sommetB):
                return sommetB in self.adjacents[sommetA]

        g = Graphe(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'])
        g.ajoute_arete('A', 'E')
        g.ajoute_arete('E', 'F')
        g.ajoute_arete('F', 'B')
        g.ajoute_arete('B', 'C')
        g.ajoute_arete('C', 'G')
        g.ajoute_arete('G', 'H')
        g.ajoute_arete('H', 'D')
        g.ajoute_arete('G', 'K')
        g.ajoute_arete('F', 'J')
        g.ajoute_arete('J', 'I')
        g.ajoute_arete('I', 'M')
        g.ajoute_arete('M', 'N')
        g.ajoute_arete('N', 'O')
        g.ajoute_arete('O', 'K')
        g.ajoute_arete('K', 'L')
        g.ajoute_arete('L', 'P')
        ```    
    """
    )
    }}

### 4. Recherche du plus court chemin

En utilisant la fonction ```recherche_chemin``` du cours, établir le plus court chemin pour aller de A vers P dans ce labyrinthe.

    {{
    correction(False,
    """
\"Correction\" 
        ```python linenums='1'
        def recherche_chemin(g, depart, arrivee):
            '''
            Parcours en largeur du graphe g en partant du sommet depart,
            qui s'arrête dès que le sommet arrivee est atteint.
            Renvoie alors le chemin du depart vers arrivee.
            '''
            traites = []
            decouverts = [depart]
            en_attente = [depart]
            parent = {}
            while en_attente != [] :
                sommet = en_attente.pop(0)
                voisins = g.voisins(sommet)
                for voisin in voisins:
                    if voisin not in decouverts:
                        decouverts.append(voisin)
                        en_attente.append(voisin)
                        parent[voisin] = sommet
                        if voisin == arrivee:
                            return remonte_chemin(depart, arrivee, parent)
                traites.append(sommet)
            return 'non trouvé'  

        def remonte_chemin(depart, arrivee, parent):
            sommet = arrivee
            chemin = arrivee
            while sommet != depart:
                sommet = parent[sommet]
                chemin = sommet + chemin
            return chemin
        ```

        ```python
        >>> recherche_chemin(g, 'A', 'P')
        'AEFBCGKLP'
        ```    
    """
    )
    }}

### 5. Conclusion

Sur un labyrinthe un peu plus imposant, voici l'illustration de notre méthode de résolution :

- le parcours en largeur part découvrir les cases dans toutes les directions.
- lorsque la case cherchée (ici, la rouge) est trouvée, on remonte à chaque case précédente grâce au dictionnaire ```parent```, et ainsi le chemin de sortie du labyrinthe est généré. 
 
Code de cette animation (en Pygame)

### 6. Annexe : et pourquoi pas en DFS ?

Les parcours BFS et DFS ont tous deux la propriété de parcourir **la totalité** du graphe (ils sont même conçus pour cela). Cela a permis au parcours BFS de nous fournir une solution au labyrinthe (dont on a démontré qu'elle était la plus courte).

Que penser de la solution qui sera donnée par le DFS ?

#### 6.1 Dans un labyrinthe parfait

Voici un code où la solution est d'abord recherchée par BFS (cases explorées en bleu clair, chemin trouvé marqué en bleu), puis en DFS (cases explorées en rose, chemin trouvé marqué en rouge).

anim_laby_DFSvsBFS_laby_parfait.py :arrow_down:

Que remarquez-vous ???

#### 6.2 Dans un labyrinthe non parfait

Changeons de code pour un labyrinthe *dégénéré* :

anim_laby_DFSvsBFS_laby_degenere.py :arrow_down:

Que remarquez-vous ???

    Notre labyrinthe conçu de manière aléatoire possède une propriété remarquable (due à son algorithme de construction) : chaque case peut être reliée à une autre par **un chemin unique**. On dit de ces labyrinthes qu'ils sont **parfaits**.

    Donc, dans notre code du 6.1 (labyrinthe parfait), le DFS va lui aussi trouver le chemin le plus court... puisqu'il y en a qu'un seul ! De plus, la méthode d'exploration en profondeur va de plus rendre le DFS plus rapide que le BFS, quasiment tout le temps. Ce qui fait que pour un labyrinthe parfait, le DFS est plus intéressant que le BFS.

    Mais si le labyrinthe n'est plus parfait (code du 6.2), le DFS va trouver une solution qui ne sera pas obligatoirement la meilleure... S'il y a plusieurs solutions possibles, absolument rien ne garantit que la première solution trouvée par le DFS (sur laquelle il s'arrêtera) sera la meilleure !

### Graphes

*Ce cours est en très grande partie inspiré du cours de Cédric Gouygou , du lycée Marguerite de Valois d'Angoulême (16)*

### 1. Notion de graphe et vocabulaire

Le concept de graphe permet de résoudre de nombreux problèmes en mathématiques comme en informatique. C'est un outil de représentation très courant, et nous l'avons déjà rencontré à plusieurs reprises, en particulier lors de l'étude de réseaux.

### 1.1 Exemples de situations

#### 1.1.1 Réseau informatique

 

#### 1.1.2 Réseau de transport
 

#### 1.1.3 Réseau social
 

#### 1.1.4 Généralisation
Une multitude de problèmes concrets d'origines très diverses peuvent donner lieu à des modélisations par des graphes : c'est donc une structure essentielle en sciences, qui requiert un formalisme mathématique particulier que nous allons découvrir. 
 

L'étude de la théorie des graphes est un champ très vaste des mathématiques : nous allons surtout nous intéresser à l'implémentation en Python d'un graphe et à différents problèmes algorithmiques qui se posent dans les graphes.

### 1.2 Vocabulaire

En général, un graphe est un ensemble d'objets, appelés *sommets* ou parfois *nœuds* (*vertex* or *nodes* en anglais) reliés par des *arêtes* ou *arcs* ((*edges* en anglais)).
Ce graphe peut être **non-orienté** ou **orienté** .

#### 1.2.1 Graphe non-orienté
 

Dans un graphe **non-orienté**, les *arêtes* peuvent être empruntées dans les deux sens, et une *chaîne* est une suite de sommets reliés par des arêtes, comme C - B - A - E par exemple. La *longueur* de cette chaîne est alors 3, soit le nombre d'arêtes.

Les sommets B et E sont *adjacents* au sommet A, ce sont les *voisins* de A.

**Exemple de graphe non-orienté** : le graphe des relations d'un individu sur Facebook est non-orienté, car si on est «ami» avec quelqu'un la réciproque est vraie.

#### 1.2.2 Graphe orienté

 

Dans un graphe **orienté**, les *arcs* ne peuvent être empruntés que dans le sens de la flèche, et un *chemin* est une suite de sommets reliés par des arcs, comme B → C → D → E par exemple.

Les sommets C et D sont *adjacents* au sommet B (mais pas A !), ce sont les *voisins* de B.

**Exemple de graphe orienté** : le graphe des relations d'un individu sur Instagram est orienté, car on peut «suivre» quelqu'un sans que cela soit réciproque.

#### 1.2.3 Graphe pondéré

 

Un graphe est **pondéré** (ou valué) si on attribue à chaque arête une valeur numérique (la plupart du temps positive), qu'on appelle *mesure*, *poids*, *coût* ou *valuation*.

Par exemple:

- dans le protocole OSPF, on pondère les liaisons entre routeurs par le coût;
- dans un réseau routier entre plusieurs villes, on pondère par les distances.

#### 1.2.4 Connexité

Un graphe est **connexe** s'il est d'un seul tenant: c'est-à-dire si n'importe quelle paire de sommets peut toujours être reliée par une chaîne. Autrement un graphe est connexe s'il est «en un seul morceau».

Par exemple, le graphe précédent est connexe. Mais le suivant ne l'est pas: il n'existe pas de chaîne entre les sommets A et F par exemple.

 

Il possède cependant deux **composantes connexes** : le sous-graphe composé des sommets A, B, C, D et E d'une part et le sous-graphe composé des sommets F, G et H.

### 2. Modélisations d'un graphe

Pour modéliser un graphe, il faut établir par convention une manière de donner les renseignements suivants :

- qui sont les sommets ?
- pour chaque sommet, quels sont ses voisins ? (et éventuellement quel poids porte l'arête qui les relie)

### 2.1 Représentation par matrice d'adjacence

- On classe les sommets (en les numérotant, ou par ordre alphabétique).
    - on représente les arêtes (ou les arcs) dans une matrice, c'est-à-dire un tableau à deux dimensions où on inscrit un 1 en ligne `i` et colonne `j` si les sommets de rang `i` et de rang `j` sont **voisins** (dits aussi *adjacents*).

    Ce tableau s'appelle une **matrice d'adjacence** (on aurait très bien pu l'appeler aussi *matrice de voisinage*).

#### 2.1.1 Graphe non orienté

Dans ce graphe non orienté, comme B est voisin de C, C est aussi voisin de B, ce qui signifie que l'arête qui relie B et C va donner lieu à deux "1" dans la matrice, situé de part et d'autre de la diagonale descendante (un mathématicien parlera de matrice *symétrique*).

#### 2.1.2 Graphe orienté

Comme le graphe est orienté, la matrice n'est pas forcément symétrique (il faudrait que tous les liens soient réciproques pour qu'elle le soit).
#### 2.1.3 Graphe pondéré

Il peut exister de la même manière des graphes pondérés **et** orientés.

#### 2.1.4 Exercices

    Soit un ensemble d'amis connectés sur un réseau social quelconque. Voici les interactions qu'on a recensées :

    - André est ami avec Béa, Charles, Estelle et Fabrice,
    - Béa est amie avec André, Charles, Denise et Héloïse,
    - Charles est ami avec André, Béa, Denise, Estelle, Fabrice et Gilbert,
    - Denise est amie avec Béa, Charles et Estelle,
    - Estelle est amie avec André, Charles et Denise,
    - Fabrice est ami avec André, Charles et Gilbert,
    - Gilbert est ami avec Charles et Fabrice,
    - Héloïse est amie avec Béa.
    
    **Q1.** Représenter le graphe des relations dans ce réseau social (on désignera chaque individu par l'initiale de son prénom). Il est possible de faire en sorte que les arêtes ne se croisent pas !

    

        
    **Q2.** Donner la matrice d'adjacence de ce graphe.

    {{
    correction(True,
    """
\"Correction\" 
        $\\pmatrix{
        0 & 1 & 1 & 0 & 1 & 1 & 0 & 0 \\\\
        1 & 0 & 1 & 1 & 0 & 0 & 0 & 1 \\\\
        1 & 1 & 0 & 1 & 1 & 1 & 1 & 0 \\\\
        0 & 1 & 1 & 0 & 1 & 0 & 0 & 0 \\\\
        1 & 0 & 1 & 1 & 0 & 0 & 0 & 0 \\\\
        1 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\\\
        0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 \\\\
        0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\\\
        }$        
    """
    )
    }}

    Construire les graphes correspondants aux matrices d'adjacence suivantes:

    **Q1.** $M_1 =\pmatrix{
        0&1&1&1&1\\
        1&0&1&0&0\\
        1&1&0&1&0\\
        1&0&1&0&1\\
        1&0&0&1&0\\
        }$

    
        
    **Q2.** $M_2=\pmatrix{
        0&1&1&0&1\\
        0&0&1&0&0\\
        0&0&0&1&0\\
        1&0&0&0&1\\
        0&0&0&0&0\\
        }$
    
    

        

    **Q3.** $M_3=\pmatrix{
        0&5&10&50&12\\
        5&0&10&0&0\\
        10&10&0&8&0\\
        50&0&8&0&100\\
        12&0&0&100&0\\
        }$    

    

        

#### 2.1.5 Implémentation Python des matrices d'adjacence

    Une matrice se représente naturellement par une liste de listes.

    **Exemple:**
    La matrice $M_1 =\pmatrix{
        0&1&1&1&1\\
        1&0&1&0&0\\
        1&1&0&1&0\\
        1&0&1&0&1\\
        1&0&0&1&0\\
        }$, associée au graphe 

    sera représentée par la variable ```G``` suivante :

    ```python
    G = [[0, 1, 1, 1, 1],
          [1, 0, 1, 0, 0],
          [1, 1, 0, 1, 0],
          [1, 0, 1, 0, 1],
          [1, 0, 0, 1, 0]]
    ```

**Complexité en mémoire et temps d'accès :**

- Pour un graphe à $n$ sommets, la complexité en mémoire (appelée aussi *complexité spatiale*) de la représentation matricielle est en $O(n^2)$.

- Tester si un sommet est isolé (ou connaître ses voisins) est en $O(n)$ puisqu'il faut parcourir une ligne, mais tester si deux sommets sont adjacents (voisins) est en $O(1)$, c'est un simple accès au tableau.

La modélisation d'un graphe par sa matrice d'adjacence est loin d'être la seule manière de représenter un graphe : nous allons voir une autre modélisation, par **liste d'adjacence**.

### 2.2 Représentation par listes d'adjacence

- On associe à chaque sommet sa liste des voisins (c'est-à-dire les sommets adjacents). On utilise pour cela un dictionnaire dont les clés sont les sommets et les valeurs les listes des voisins.

    - Dans le cas d'un graphe orienté on associe à chaque sommet la liste des *successeurs* (ou bien des *prédécesseurs*, au choix).

    Par exemple, le graphe  sera représenté par le dictionnaire :

    ```python linenums='1'
    G = {'A': ['B', 'C', 'D', 'E'],
         'B': ['A', 'C'],
         'C': ['A', 'B', 'D'],
         'D': ['A', 'C', 'E'],
         'E': ['A', 'D']
        }
    ```

**Complexité en mémoire et temps d'accès :**

- Pour un graphe à $n$ sommets et $m$ arêtes, la complexité spatiale de la représentation en liste d'adjacence est en $O(n+m)$. C'est beaucoup mieux qu'une matrice d'adjacence lorsque le graphe comporte peu d'arêtes (i.e. beaucoup de 0 dans la matrice, non stockés avec des listes).

- Tester si un sommet est isolé (ou connaître ses voisins) est en $O(1)$ puisqu'on y accède immédiatement, mais tester si deux sommets sont adjacents (voisins) est en $O(n)$ car il faut parcourir la liste.

#### 2.2.1 Exercices

    Construire les graphes correspondants aux listes d'adjacence suivantes.

    **Q1.** 
    ```python
    G1 = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'E', 'F'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['B', 'E']
         }
    ```

    

    **Q2.** 
    ```python
    G2 = {
    'A': ['B'],
    'B': ['C', 'E'],
    'C': ['B', 'D'],
    'D': [],
    'E': ['A']
         }

    ```

### 2.3 Représentation uniquement avec des listes.

Ainsi qu'il est fait dans le sujet 21.2 de la BNS 2024, le graphe ci-dessus peut être représenté par la liste de listes suivante :

```python
adj = [[1, 2], [0, 3], [0], [1], [5], [4]]
```

### 3.1 Interface souhaitée

Nous voulons que le graphe  puisse être créé grâce aux instructions suivantes :

```python
g = Graphe(['A', 'B', 'C', 'D', 'E'])
g.ajoute_arete('A', 'B')
g.ajoute_arete('A', 'C')
g.ajoute_arete('A', 'D')
g.ajoute_arete('A', 'E')
g.ajoute_arete('B', 'C')
g.ajoute_arete('C', 'D')
g.ajoute_arete('D', 'E')
```

Nous souhaitons aussi pouvoir tester si deux sommets sont voisins avec la méthode ```sont_voisins``` :

```python
>>> g.sont_voisins('E', 'A')
True
>>> g.sont_voisins('E', 'B')
False
```

Enfin, nous voulons pouvoir obtenir facilement la liste de tous les voisins d'un sommet avec la méthode ```voisins```:
```python
>>> g.voisins('C')
['A', 'B', 'D']
```

### 3.2 Conseils d'implémentation

L'objet de type ```Graphe``` aura comme attributs :

- une liste ```liste_sommets``` (donnée en paramètre dans la méthode constructeur) 
- un dictionnaire ```adjacents```, où chaque sommet se verra attribuer une liste vide lors de la méthode constructeur.

### 3.3 Implémentation

{#

    ```python linenums='1'
    class Graphe:
        def __init__(self, liste_sommets):
            ...
            ...

        def ajoute_arete(self, sommetA, sommetB):
            ...
            ...
            
        def voisins(self, sommet):
            return ...

        def sont_voisins(self, sommetA, sommetB):
            return ...
    ```
#}

    ```python linenums='1'
    class Graphe:
        def __init__(self, liste_sommets):
            self.liste_sommets = liste_sommets
            self.adjacents = {sommet : [] for sommet in liste_sommets}

        def ajoute_arete(self, sommetA, sommetB):
            self.adjacents[sommetA].append(sommetB)
            self.adjacents[sommetB].append(sommetA)
            
        def voisins(self, sommet):
            return self.adjacents[sommet]

        def sont_voisins(self, sommetA, sommetB):
            return sommetB in self.adjacents[sommetA]
    ```

### 4.    Parcours de graphes

Un parcours de graphe est un algorithme consistant à explorer **tous** les sommets d'un graphe de proche
    en proche à partir d'un sommet initial. Ces parcours sont notamment utilisés pour rechercher un plus court chemin (et donc dans les GPS) ou pour trouver la sortie d'un labyrinthe...

    :warning: Parcourir simplement le dictionnaire ou la matrice d’un
    graphe n’est pas considéré comme un
    parcours de graphe. :warning:

    Tous les parcours suivent plus ou moins le même algorithme de base :

    - On visite un sommet ```A``` . On crée une structure ```S```  qui contiendra au départ uniquement le sommet ```A``` .

    - Tant que ```S``` n’est pas vide :
    
        - on choisit un sommet ```s```  de ```S``` (on dit qu'on «visite» ```s```);
        - on ajoute à ```S``` tous les voisins de ```s``` **pas encore visités**.

    Contrairement à un parcours d'arbre, où un nœud ne peut pas être fils de deux nœuds différents, un sommet **peut** être voisin de deux sommets différents.

    Il est donc nécessaire de mémoriser les sommets déja visités ou découverts (on dira qu'un sommet est découvert lorsqu'on l'ajoute à ```S```).

Le choix de la structure de l'ensemble ```S``` est prépondérant:

- Si on choisit une **file** (FIFO): on visitera les sommets dans l'ordre d'arrivée, donc les plus proches du sommet précédent. On obtient donc un *parcours en largeur* :arrow_right: **BFS** (Breadth-First Search).
- Si on choisit une **pile** (LIFO): on visitera d'abord les derniers sommets arrivés, donc on parcourt le graphe en visitant à chaque étape un voisin du précédent. On obtient donc un *parcours en profondeur* :arrow_right: **DFS** (Depth-First Search).

### 4.1 Le parcours en largeur (BFS, Breadth First Search)

#### 4.1.1 Principe

**Exemple de parcours en largeur, avec B comme sommet de départ:**

**Codes couleur :**

- **vert** : les sommets non encore traités.
- **rouge** : le sommet en cours de traitement.
- **orange** : la file d'attente des sommets qui seront bientôt traités. On y rajoute à chaque fois les voisins du sommet en cours de traitement, uniquement **si ils n'ont pas encore été découverts**.
- **noir** : les sommets traités.

#### 4.1.2 Algorithme BFS

On utilise :

- une liste `#!py traites` qui recueille les sommets visités (c'est-à-dire qu'on a fini de traiter, après avoir ajouté ses voisins dans la file d'attente) et qui sera renvoyée à la fin de l'algorithme;
- une liste `#!py decouverts` qui contient les sommets découverts au fur et à mesure du parcours;
- une **file** `#!py en_attente` qui contient les sommets découverts mais non encore visités. On utilisera au choix une classe `File` écrite plus tôt dans l'année ou tout simplement une `#!py list` en utilisant `#!py pop(0)` (pour défiler) et `#!py append()` (pour enfiler).

En début d'algorithme, seul le sommet de départ `#!py depart` donné en paramètre est découvert. La fonction `BFS` renvoie la liste des sommets dans l'ordre de visite lors du parcours en largeur.

{#

    ```python linenums='1'
    def BFS(g, depart):
        '''
        Effectue un parcours en largeur du graphe g en partant du sommet depart,
        et renvoie la liste des sommets visités dans l'ordre du parcours.
        '''
        traites = []
        decouverts = [...]
        en_attente = [...]
        while ... != [] :
            sommet = ...
            voisins = ...
            for voisin in ...:
                if ... not in ...:
                    ....append(...)
                    ....append(...)
            ....append(...)
        return ...

    ```
#}

    ```python linenums='1'
    def BFS(g, depart):
        '''
        Effectue un parcours en largeur du graphe g en partant du sommet depart,
        et renvoie la liste des sommets visités dans l'ordre du parcours.
        '''
        traites = []
        decouverts = [depart]
        en_attente = [depart]
        while en_attente != [] :
            sommet = en_attente.pop(0)
            voisins = g.voisins(sommet)
            for voisin in voisins:
                if voisin not in decouverts:
                    decouverts.append(voisin)
                    en_attente.append(voisin)
            traites.append(sommet)
        return traites

    ```

    La liste ```decouverts``` contient tous les sommets qui ont été :

    - soit traités (auquel cas ils sont dans la liste ```traites```)
    - soit en attente (auquel cas ils sont dans la liste ```en_attente```)

    Le test de la ligne 13  `#!py if voisin not in decouverts:` permet donc de ne pas mettre en file d'attente un voisin qui est (ou a été) déjà en file d'attente. 

    À chaque instant, la file ```en_attente``` contient des sommets à la distance ```k+1``` et à la distance ```k``` du point de départ :

    

    Grâce à la classe ```Graphe``` du 3.3, ce graphe s'implémente par :

    ```python linenums='1'
    g = Graphe(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    g.ajoute_arete('A', 'B')
    g.ajoute_arete('A', 'C')
    g.ajoute_arete('B', 'D')
    g.ajoute_arete('D', 'C')
    g.ajoute_arete('B', 'E')
    g.ajoute_arete('D', 'E')
    g.ajoute_arete('E', 'F')
    g.ajoute_arete('E', 'G')
    g.ajoute_arete('F', 'G')
    g.ajoute_arete('G', 'H')
    ```
    
    **Q1.** Donner le parcours en largeur de ```g```  grâce à l'algorithme BFS, si le sommet de départ est B. Cela correspond au parcours présenté par le gif de début de paragraphe.

    
  

    **Q2.** Deviner le parcours en largeur de départ D, puis de départ G. Vérifier grâce à votre algorithme.

### 4.1.3 Application du BFS : recherche du plus court chemin

L'algorithme BFS découvre les sommets «par cercles concentriques» autour du point de départ (ainsi que le montre la structure de la file d'attente). On découvre d'abord tous les sommets à la distance 1 du point de départ, puis à la distance 2, puis 3, etc.

Un sommet situé à la distance 5 sera découvert en tant que voisin d'un sommet à la distance 4, qui lui-même aura été découvert grâce à un sommet à la distance 3, qui lui-même...

On comprend donc que si on arrive à se souvenir du sommet «parent» de chaque sommet (celui qui lui a permis d'être découvert), on pourra alors reconstituer un chemin permettant de remonter au point de départ.

Nous allons pour cela nous servir d'une structure de dictionnaire pour associer à chaque sommet son sommet-parent.

Il faudra ensuite une fonction pour recréer le chemin.

    - Comment est-on sûr qu'un chemin va être trouvé entre deux sommets A et B ?

    Si le graphe est connexe, tout parcours BFS au départ de A va parcourir l'intégralité du graphe, et donc passera par B à un moment. Un chemin sera donc forcément trouvé entre A et B.

    - Comment est-on sûr que ce chemin trouvé est **le plus court** ?

    La découverte des sommets par cercles concentriques entre A et B nous assure qu'on ne peut pas rater le point B : s'il est à la distance ```k``` de A, il sera forcément visité puisque tous les sommets à la distance ```k``` vont passer par la liste d'attente, après les sommets de distance ```k-1``` et avant les sommets de distance ```k+1```.
    
    Lorsqu'on remontera de B vers A en passant par les sommets parents successifs, il ne peut y avoir qu'un seul sommet par «couche» : le chemin sera donc exactement de longueur ```k```, il sera donc minimal. 

{#  
    ```python linenums='1'
    def recherche_chemin(g, depart, arrivee):
        '''
        Parcours en largeur du graphe g en partant du sommet depart,
        qui s'arrête dès que le sommet arrivee est atteint.
        Renvoie alors le chemin du depart vers arrivee.
        '''
        traites = []
        decouverts = [depart]
        en_attente = [depart]
        parent = {}
        while en_attente != [] :
            sommet = en_attente.pop(0)
            voisins = g.voisins(sommet)
            for voisin in voisins:
                if voisin not in decouverts:
                    decouverts.append(voisin)
                    en_attente.append(voisin)
                    parent[...] = ...
                    if voisin == arrivee:
                        return remonte_chemin(depart, arrivee, parent)
            traites.append(sommet)
        return "non trouvé"  

    def remonte_chemin(depart, arrivee, parent):
        sommet = arrivee
        chemin = arrivee
        while sommet != ...:
            sommet = parent[...]
            chemin = ... + chemin
        return chemin
    ```
#}
    

 
    ```python linenums='1'
    def recherche_chemin(g, depart, arrivee):
        '''
        Parcours en largeur du graphe g en partant du sommet depart,
        qui s'arrête dès que le sommet arrivee est atteint.
        Renvoie alors le chemin du depart vers arrivee.
        '''
        traites = []
        decouverts = [depart]
        en_attente = [depart]
        parent = {}
        while en_attente != [] :
            sommet = en_attente.pop(0)
            voisins = g.voisins(sommet)
            for voisin in voisins:
                if voisin not in decouverts:
                    decouverts.append(voisin)
                    en_attente.append(voisin)
                    parent[voisin] = sommet
                    if voisin == arrivee:
                        return remonte_chemin(depart, arrivee, parent)
            traites.append(sommet)
        return "non trouvé"  

    def remonte_chemin(depart, arrivee, parent):
        sommet = arrivee
        chemin = arrivee
        while sommet != depart:
            sommet = parent[sommet]
            chemin = sommet + chemin
        return chemin
    ```

    
    Tester le code précédent pour trouver le plus court chemin entre A et G, entre H et C, entre B et G...

### 4.2 Le parcours en profondeur (DFS, Depth First Search)

#### 4.2.1 Parcours DFS récursif

Le parcours en profondeur est un parcours où on va aller «le plus loin possible» sans se préoccuper des autres voisins non visités : on va visiter le premier de ses voisins non traités, qui va faire de même, etc. Lorsqu'il n'y a plus de voisin, on revient en arrière pour aller voir le dernier voisin non visité.

Dans un labyrinthe, ce parcours s'explique très bien : on prend tous les chemins sur la droite jusqu'à rencontrer un mur, auquel cas on revient au dernier embranchement et on prend un autre chemin, puis on repart à droite, etc.

C'est un parcours qui s'écrit naturellement de manière **récursive** :

{#

    ```python linenums='1'
    def DFSrec(g, traites, actuel):
        traites.append(...)
        for voisin in ...:
            if voisin not in ...:
                DFSrec(g, ..., ...)
        return traites
    ```
#}

    ```python linenums='1'
    def DFSrec(g, traites, actuel):
        traites.append(actuel)
        for voisin in g.voisins(actuel):
            if voisin not in traites:
                DFSrec(g, traites, voisin)
        return traites
    ```

    
    
    **Q1.** Donner (de tête) le parcours DFS de ce graphe en partant de A.  
    Rappel : les voisins sont donnés par ordre alphabétique. Le premier voisin de A est donc B.

    **Q2.** Vérifier avec le code précédent. 

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        class Graphe:
            def __init__(self, liste_sommets):
                self.liste_sommets = liste_sommets
                self.adjacents = {sommet : [] for sommet in liste_sommets}

            def ajoute_arete(self, sommetA, sommetB):
                self.adjacents[sommetA].append(sommetB)
                self.adjacents[sommetB].append(sommetA)

            def voisins(self, sommet):
                return self.adjacents[sommet]

            def sont_voisins(self, sommetA, sommetB):
                return sommetB in self.adjacents[sommetA]

        g = Graphe(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        g.ajoute_arete('A', 'B')
        g.ajoute_arete('A', 'C')
        g.ajoute_arete('B', 'D')
        g.ajoute_arete('D', 'C')
        g.ajoute_arete('B', 'E')
        g.ajoute_arete('D', 'E')
        g.ajoute_arete('E', 'F')
        g.ajoute_arete('E', 'G')
        g.ajoute_arete('F', 'G')
        g.ajoute_arete('G', 'H')

        def DFSrec(g, traites, actuel):
            traites.append(actuel)
            for voisin in g.voisins(actuel):
                if voisin not in traites:
                    DFSrec(g, traites, voisin)
            return traites

        ```
    
        ```python
        >>> DFSrec(g, [], 'A')
        ['A', 'B', 'D', 'C', 'E', 'F', 'G', 'H']
        ```        
    """
    )
    }}

    **Q3.** Reprendre les questions précédentes en changeant le sommet de départ.

#### 4.2.2 Parcours DFS itératif

Il «suffit» de remplacer la file du parcours BFS par une **pile**. Ainsi, on partira visiter le voisin tout juste ajouté à la *file d'attente* (qui porte maintenant très mal son nom, puisque c'est devenu une pile).

{#

    ```python linenums='1'
    def DFS_iteratif(graphe, start):
        traites = ...
        en_attente = ...
        while ... != []:
            actuel = ...
            if ... not in ...:
                voisins = g.voisins(actuel)[::-1]
                for ... in ...:
                    if ... not in ...:
                        ....append(...)
                ....append(...)
        return ...
    ```
#}

    ```python linenums='1'
    def DFS_iteratif(graphe, start):
        traites = []
        en_attente = [start]
        while en_attente != []:
            actuel = en_attente.pop()
            if actuel not in traites:
                voisins = g.voisins(actuel)[::-1]
                for voisin in voisins:
                    if voisin not in traites:
                        en_attente.append(voisin)
                traites.append(actuel)
        return traites
    ```

**Remarques :**

- À la ligne 7, on inverse l'ordre des voisins (avec l'astuce ```[::-1]```)  pour que ce code renvoie le même parcours que le parcours récursif (sinon c'est le dernier voisin ajouté qui sera dépilé). Cela n'est pas obligatoire : il n'y a pas «un seul» parcours DFS (tout comme il n'y a pas qu'un seul BFS). Ce qui les caractérise est la **méthode de découverte**, plus que l'implémentation proprement dite.

- Contrairement au BFS, il est possible d'empiler un sommet déjà découvert (on vérifie juste qu'il n'ait pas déjà été traité). Vous pouvez vous en apercevoir en écrivant l'état de la pile lors du parcours DFS itératif du graphe de l'exercice 6.

### Introduction

Exercice 3 du sujet 0 version A - 2024

    

    

    {{
    correction(True,
    """
\"Correction Q3.\" 
        La matrice d'adjacence de G1 est :
        $\\pmatrix{
        0 & 4 & 0 & 0 & 4 & 0 & 0  \\\\
        4 & 0 & 0 & 0 & 0 & 7 & 5  \\\\ 
        0 & 0 & 0 & 4 & 8 & 0 & 0  \\\\
        0 & 0 & 4 & 0 & 6 & 8 & 0  \\\\ 
        4 & 0 & 8 & 6 & 0 & 0 & 0  \\\\
        0 & 7 & 0 & 8 & 0 & 0 & 3  \\\\ 
        0 & 5 & 0 & 0 & 0 & 3 & 0  \\\\
        }$  
    """
    )
    }}

    {{
    correction(True,
    """
\"Correction Q4.\" 
        ```python linenums='1'
        G2 = {'A': ['B', 'C', 'H'],
              'B': ['A', 'I'],
              'C': ['A', 'D', 'E'],
              'D': ['C', 'E'],
              'E': ['C', 'D', 'G'],
              'F': ['G', 'I'],
              'G': ['E', 'F', 'H'],
              'H': ['A', 'G', 'I'],
              'I': ['B', 'F', 'H']
             }
        ```
    """
    )
    }}

        ```python linenums='1'
        G2 = {'A': ['B', 'C', 'H'],
            'B': ['A', 'I'],
            'C': ['A', 'D', 'E'],
            'D': ['C', 'E'],
            'E': ['C', 'D', 'G'],
            'F': ['G', 'I'],
            'G': ['E', 'F', 'H'],
            'H': ['A', 'G', 'I'],
            'I': ['B', 'F', 'H']
            }

        tab_itineraires = []
        def cherche_itineraires(G, start, end, chaine=[]):
            chaine = chaine + [start]
            if start == end:
                return chaine
            for u in G[start]:
                if u not in chaine:
                    nchemin = cherche_itineraires(G, u, end, chaine)
                    if len(nchemin) != 0:
                        tab_itineraires.append(nchemin)
            return []

        def itineraires_court(G, dep, arr):
            cherche_itineraires(G, dep, arr)
            tab_court = ...
            mini = float('inf')
            for v in tab_itineraires:
                if len(v) >> voisins_entrants([[1, 2], [2], [0], [0]], 0)
    [2, 3]
    >>> voisins_entrants([[1, 2], [2], [0], [0]], 1)
    [0]
    ```

    Dans cet exercice, on considère un graphe non orienté représenté sous forme de listes
    d’adjacence. On suppose que les sommets sont numérotés de 0 à n-1.

    Ainsi, le graphe suivant:

    

    sera représenté par la liste d’adjacence suivante:

    `adj = [[1, 2], [0, 3], [0], [1], [5], [4]]`

    On souhaite déterminer les sommets accessibles depuis un sommet donné dans le graphe.
    Pour cela, on va procéder à un parcours en profondeur du graphe.

    Compléter la fonction suivante.

    ```python linenums='1'
    def parcours(adj, x, acc):
        '''Réalise un parcours en profondeur récursif
        du graphe donné par les listes d'adjacence adj 
        depuis le sommet x en accumulant les sommets
        rencontrés dans acc'''
        if x ...: 
            acc.append(x)
            for y in ...: 
                parcours(adj, ...) 

    def accessibles(adj, x):
        '''Renvoie la liste des sommets accessibles dans le
        graphe donné par les listes d'adjacence adj depuis
        le sommet x.'''
        acc = []
        parcours(adj, ...) 
        return acc
    ```

    Exemples :
    ```python
    >>> accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0)
    [0, 1, 2, 3]
    >>> accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4)
    [4, 5]    
    ```

    Exercice 2 du sujet Concours GEIPI 2024.

    Codes du sujet :
    
    ```python linenums='1'
    sentiers = [('Briana', 'La Concorde', 'Grand Palais', 100),
                ('Teddy', 'Grand Palais', 'Trocadéro', 550),
                ('Elaine', 'La Concorde', 'Trocadéro', 200),
                ('Lucie', 'Grand Palais', 'Champ de Mars', 512),
                ('Sydney', 'Trocadéro', 'Champ de Mars', 100)]

    def creer_dico_arcs_sortants(sentiers):
        arcs_sortants = ...
        for (n, p1, p2, d) in sentiers:
            if ... not in arcs_sortants:
                arcs_sortants[ ... ] = []
            arcs_sortants[ ... ].append((p1, n, d))
            if ... not in ... :
                arcs_sortants[ ... ] = []
            arcs_sortants[ ... ].append( ... )
        return arcs_sortants

    from math import inf # la constante inf représente (+ infini)
    def plus_proche(a_visiter):
        min = ...
        proche = ''
        for (p, (poids, pred, sent)) in a_visiter.items():
            if ... 

    ### 1. Préambule

    À chaque étape il faut choisir le sommet qui est associé à la distance la plus petite. Nous allons pour cela devoir ordonner une liste **par son deuxième élément**.

    Par exemple, vous voulons transformer la liste 

    ```python
    [["A", 3], ["B", 2], ["C", 8], ["D", 1]]
    ```

    en
    ```python
    [["D", 1], ["B", 2], ["A", 3], ["C", 8]]
    ```

    Il faut pour cela procéder en 2 étapes.

    :right_arrow: Créer une fonction ```deuxieme``` qui prend en paramètre un tableau ```lst``` de type `List` et qui renvoie le deuxième élément de ```lst```. 

    *Exemple d'utilisation*
    ```python
    >>> simpsons = ['Bart', 'Lisa', 'Maggie']
    >>> deuxieme(simpsons)
    'Lisa'
    ```

    

    Grâce à cette fonction ```deuxieme```, nous allons utiliser la fonction ```sorted```, qui prend en paramètre une liste à trier et une fonction de tri.

    **Exemple :**

    ```python
    >>> mylist = [["A", 3], ["B", 2], ["C", 8]]
    >>> mynewlist = sorted(mylist, key=deuxieme)
    >>> mynewlist
    [['B', 2], ['A', 3], ['C', 8]]
    ```

        Python permet en fait de faire cela de manière beaucoup plus rapide, avec les fonctions ```lambda```, qui sont comme des fonctions créées à la volée sans avoir besoin de les nommer :
        ```python
        >>> mylist = [["A", 3], ["B", 2], ["C", 8]]
        >>> mynewlist = sorted(mylist, key=lambda x:x[1])
        >>> mynewlist
        [['B', 2], ['A', 3], ['C', 8]]
        ```
    
    ### 2. Algorithme de Dijkstra

    ```python linenums='1'
    g = {
        'A': {'B': 12, 'D': 14},
        'B': {'A': 12, 'F': 9, 'G': 16},
        'C': {'E': 13, 'F': 10},
        'D': {'A': 14, 'E': 10},
        'E': {'D': 10, 'C': 13, 'F': 16, 'H': 10},
        'F': {'B': 9, 'C': 10, 'E': 16, 'H': 11},
        'G': {'B': 16, 'H': 11},
        'H': {'E': 10, 'F': 11, 'G': 11}
    }

    def deuxieme(lst):
        return ...

    def classe_file(lst):
        return ...

    def remonte_chemin(parent, start, end):
        s = end
        actuel = end
        while actuel != start:
            actuel = parent[actuel]
            s = actuel + s
        return s

    def dijkstra(g, start, end):
        distance = {k:10**6 for k in g}
        distance[start] = 0
        parent = {}
        file = [(start, 0)]
        while file != []:
            file = ... #(1)
            actuel, dist = ... #(2)
            for voisin in ... : #(3)
                new_dist = ... + ... #(4)
                if new_dist < distance[voisin]:
                    distance[voisin] = ... #(5)
                    parent[voisin] = ... #(6)
                    file.append((..., ...)) #(7)
        return remonte_chemin(parent, start, end), distance[end]

    ```

    1. On classe la file de sorte que le 1er élément soit le sommet ayant la plus petite distance.
    2. On sort de la liste ce premier élément, et on récupère le nom du sommet et sa distance associée.
    3. Les voisins du sommet ```actuel``` sont les clés du dictionnaire associé au sommet ```actuel```.
    4. La nouvelle distance (potentielle) est la somme de la distance actuelle et de la distance entre ```actuel``` et ```voisin```.
    5. On met à jour la distance.
    6. On met à jour le parent.
    7. On remet dans la file le sommet ```voisin``` ainsi que sa nouvelle distance associée.

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        g = {
            'A': {'B': 12, 'D': 14},
            'B': {'A': 12, 'F': 9, 'G': 16},
            'C': {'E': 13, 'F': 10},
            'D': {'A': 14, 'E': 10},
            'E': {'D': 10, 'C': 13, 'F': 16, 'H': 10},
            'F': {'B': 9, 'C': 10, 'E': 16, 'H': 11},
            'G': {'B': 16, 'H': 11},
            'H': {'E': 10, 'F': 11, 'G': 11}
        }

        def deuxieme(lst):
            return lst[1]

        def classe_file(lst):
            return sorted(lst, key=deuxieme)

        def remonte_chemin(parent, start, end):
            s = end
            actuel = end
            while actuel != start:
                actuel = parent[actuel]
                s = actuel + s
            return s

        def dijkstra(g, start, end):
            distance = {k:10**6 for k in g}
            distance[start] = 0
            parent = {}
            file = [(start, 0)]
            while file != []:
                file = classe_file(file)
                actuel, dist = file.pop(0)
                for voisin in g[actuel]:
                    new_dist = dist + g[actuel][voisin]
                    if new_dist < distance[voisin]:
                        distance[voisin] = new_dist
                        parent[voisin] = actuel
                        file.append((voisin, new_dist))
            return remonte_chemin(parent, start, end), distance[end]

        ```
    """
    )
    }}

## Structures donnees

### Structures donnees

Terminale - Spécialité NSI IFS Singapour
Chapitre 4 - Les structures de données
Objectifs :
▷ Remettre en mémoire les structures de données vues enPremière
▷ Montrer qu'il existe plusieurs implémentations possibles
1 Introduction
En informatique, on manipule essentiellement des données. Lorsqu'elles sont simples comme desnombres,
des chaînes de caractères ou des booléens, on peut les stocker dans des variables qui seront typées en
fonction de la nature de la donnée.
2 Définition
A retenir!
Une structure de données est une organisation logique des données permettant de simplifier ou
d'accélérer leur traitement.
3 Exemple
Par exemple, si on a écrit un code avec les affectations suivantes :
1 n = 4
2 p = -5
3 r = 0.7
4 phrase = 'hello'
5 test = True
Python est un langage avec untypage dynamique, c'est-à-dire que le type de la variable est automa-
tiquement déterminé la première fois qu'elle est déclarée.
Ainsi, on obtient en retour les types des variables suivants :
1 >>> type(n)
2 <class 'int'>
3 >>> type(p)
4 <class 'int'>
5 >>> type(r)
6 <class 'float'>
7 >>> type(phrase)
8 <class 'str'>
9 >>> type(test)
10 <class 'bool'>
En revanche, lorsque l'on a besoin de manipuler un grand nombre de données (de même type ou non),
on utilise desstructures de données comme les tuples, les listes, les tableaux ou les dictionnaires.
4 Utilisation d'une structure de données
Rappel
Les chaînes de caractères, lestuples et leslistes sont desséquences, c'est-à-dire des suites ordon-
nées d'éléments indexés par une suite d'entiers.
T. Rahobisoa 1/6 SD01 - Structures de données
Terminale - Spécialité NSI IFS Singapour
On rappelle que :
▷ Les chaînes de caractères et les tuples sont non mutables (on ne peut les modifier).
▷ Les listes sont mutables.
▷ Un tableau est une liste de liste.
▷ Les tuples et les listes peuvent contenir des éléments de n'importe quel type, y compris d'autres
tuples, listes ou encore des dictionnaires...
▷ Les chaînes de caractères , listes et tuples sont appelés des types construits . Ils possèdent un
certain nombre de méthodes qui permettent d'agir sur l'objet (ajout, suppression, tris, ..., etc. )
▷ Dans un dictionnaire, les éléments sont indexés par des clés et sont modifiables.
5 Application
On voudrait stocker dans une seule variable, pour un élève les données suivantes :
▷ Nom : Terieur
▷ Prénom : Alain
▷ Date de naissance : 01/01/2005
▷ Programmation : 12
▷ Algorithmique : 10
▷ Projet : 15
Pour ce faire, il y a plusieurs possibilités. On pourrait utiliser :
- un tuple (les données ne seront pas modifiables) :
1 eleve1 = ('Terieur', 'Alain', '01/01/2005', 12,10,15)
- un tuple contenant des listes (modifiables) :
1 eleve1 = (['Terieur', 'Alain', '01/01/2005'], [12,10,15])
- un dictionnaire :
1 eleve1 = {'Nom' : 'Terieur', 'Prenom' : 'Alain', 'Date' : '01/01/2005',
'Programmation' : 12, 'Algorithmique' : 10, 'Projet' : 15}
Ou encore une liste, ou une liste de listes, ou une liste de tuples, ..., etc.
T. Rahobisoa 2/6 SD01 - Structures de données
Terminale - Spécialité NSI IFS Singapour
Si maintenant on souhaite, le faire pour une classe entière, on pourra stocker les données dans une
variable :
classe1 = [eleve1,eleve2,...]
On peut créer une fonction qui calcule la moyenne d'un élève :
1 def moyenne(eleve : dict)-> float:
2 ''' Fonction qui calcule la moyenne(float) des notes
3 Entrees :
4 cles(type) -> Nom(str), Prenom(str), Date(str),
Programmation(float), Algorithmique(float), Projet(float)
5 Retour : moy(float)
6 '''
7 moy = (eleve['Programmation'] + eleve['Algorithmique'] +
eleve['Projet'])/3
8
9 return moy
10
11 #----------- Programme principal -----------------
12
13 eleve1 = {'Nom' : 'Terieur', 'Prenom' : 'Alain', 'Date' : '01/01/2005',
'Programmation' : 12, 'Algorithmique' : 10, 'Projet' : 15}
14
15 print('moyenne de ', eleve1['Prenom'], eleve1['Nom'], ' : ',
moyenne(eleve1))
On obtient alors :
»> moyenne de Alain Terieur : 12.33333333333334
On pourra créer une variable contenant les moyennes de chaque élève, les moyennes de chaque matière
et par exemple créer des classements suivant des critères.
6 Méthode
Le cahier des charges :
▷ Stocker les données (nom, prénom, date de naissance, notes) pour les élèves d'une classe.
▷ Calculer et stocker leur moyenne.
▷ Calculer et stocker la moyenne générale de chaque matière.
Choix de la structure de données :
▷ Pour un élève
▷ Pour la classe
Implémentation : Attention, votre implémentation ne doit pas modifier le cahier des charges ni le
choix de la structure de données.
▷ Enregistrement des données
▷ Implémentation des fonctions
7 Conclusion
A retenir!
Il n'y a pasunicité de la représentation concrète des données, l'important ce sont les données pas
leur représentation!
T. Rahobisoa 3/6 SD01 - Structures de données
Terminale - Spécialité NSI IFS Singapour
8 Exercices
Exercice 1 :
1. Implémenter le cahier des charges précédent pour une classe contenant les 3 élèves suivants :
Nom : Terieur Nom : Neymar Nom: Duff
Prénom : Alain Prénom : Jean Nom: John
Date : 01/01/2005 Date : 01/07/2006 Date : 01/11/2007
Programmation : 12 Programmation : 7 Programmation : 13
Algorithmique : 10 Algorithmique : 14 Algorithmique : 8
Projet : 15 Projet : 11 Projet : 17
Les données seront déjà structurées et notre classe de 3 élèves pourrait être enregistrée sous la forme
d'un fichiercsv comme suit :
1 Nom,Prenom,Date,Programmation,Algorithmique,Projet
2 Terieur,Alain,01/01/2005,12,10,15
3 Neymar,Jean,01/07/2006,7,14,11
4 Duff,John,01/11/2007,13,8,17
On peut alors récupérer ce fichier dans un programme, pour réaliser les calculs souhaités. On ob-
tiendra comme précédemment une liste de dictionnaires contenant les données des élèves, cependant
les notes seront de typestr.
1 import csv
2
3 reader = csv.DictReader(open('eleves.csv', 'r'), encoding = 'utf-8')
4 classe = []
5
6 for row in reader:
7 classe.append(dict(row))
8
9 print(classe)
2. Avec un éditeur de texte (par exempleNotepad ++), créer le fichiereleves.csv , puis réaliser un
programme qui affiche les résultats suivants :
1 moyenne de Alain Terieur : 12.33333333334
2 moyenne de Jean Neymar : 10.66666666666
3 moyenne de John Duff : 12.66666666666
4 moyenne de programmation : 10.666666666
5 moyenne de algorithmique : 10.666666666
6 moyenne de Projet : 14.333333333333334
Vous devriez pouvoir utiliser les fonctions écrites à la question 1 en forçant les notes à être lues
comme des nombresfloat.
T. Rahobisoa 4/6 SD01 - Structures de données
Terminale - Spécialité NSI IFS Singapour
Exercice 2 : Ajouter un nombre
Ecrire une fonctionajout_nombre(,nL) qui ajoute un entiern à chaque élément d'une listeL La liste et
le nombre à ajouter seront passés en paramètres.
Exemple :
> L = [1,2,3,4,5]
> ajout_nombre(L,3)
[4, 5, 6, 7, 8]
Exercice 3 : Entier ↣ Tuple
Écrire une fonction entier_tuple(n) qui renvoie sous forme de tuple les chiffres d'un nombre entier
positif n passé en paramètre.
Exemple :
> n = 123456
> entier_tuple(n)
(1,2,3,4,5,6)
Exercice 4 : Tuple ↣ Entier
Écrire une fonctiontuple_entier(t) qui renvoie sous forme d'entier le tuplet passé en paramètre.
Exemple :
> t = (1,2,3,4,5,6)
> tuple_entier(t)
123456
Exercice 5 : Supression doublon
Écrire une fonctionsupprime_doublon(L) qui supprime les éléments en double d'une listeL passée en
paramètre.
Exemple :
> L = [1,2,5,8,6,2,5,9,1,8,8]
> supprime_doublon(L)
[1, 2, 5, 8, 6, 9]
Exercice 6 : concaténation de listes
Écrire une fonctionconcatene_listes(L1,L2) qui concatène sans doublons deux listes d'entiersL1 et
L2 passées en paramètre.
Exemple :
> L1 = [13, 15, 12, 17, 15 ]
> L2 = [18, 15, 14, 13, 19, 20]
> concatene_listes(L1,L2)
[13, 15, 12, 17, 18, 14, 19, 20]
T. Rahobisoa 5/6 SD01 - Structures de données
Terminale - Spécialité NSI IFS Singapour
Exercice 7 : D'une liste à un dictionnaire
1. Ecrire en Python une fonction liste_en_dico(liste) qui admet en argument une liste de la
forme [clé1, valeur1, clé2, valeur2, ...] et qui retourne le dictionnaire correspondant de
la forme :clé1 : valeur 1, clé2 : valeur2, ...
Vous pouvez tester votre programme avec la liste ci-dessous :
Capitales = ['France', 'Paris', 'Angleterre', 'Londres', 'Espagne', 'Madrid', 'Allemagne',
'Berlin']
2. Ecrire un DocString pour cette fonction.
Exercice 8 : Fabricant de tee-shirts
Un fabricant décide de créer des tee-shirts dont la taille peut-être : XS , S, M, L, XL, XXL.
A chaque taille son prix; il adopte le principe suivant : 8€ pour la taille XS et il ajoute 2€ en passant à
la taille supérieure, jusqu'au XXL.
1. Implémenter en Python, ces informations dans la structure de données la mieux adaptée.
Ce même fabricant décide de changer sa façon de fixer les prix de revente des tee-shirts. Ceux dont
la taille est XS sont toujours à 8€, mais cette fois-ci, pour passer d'une taille à la suivante, il ajoute
au prix de la taille inférieure la moitié de sa racine carrée.
Par exemple, pour obtenir le prix de la taille S, il fait :8 +
√
2. Ecrire un fonction pythonprix(liste) qui admet en argument la liste des tailles et retourne les
tailles et le prix dans une structure de données adaptée.
T. Rahobisoa 6/6 SD01 - Structures de données

## Les listes

### Les listes

Terminale - Spécialité NSI IFS Singapour
Chapitre 5 - Les listes
Objectifs :
▷ Distinguer des structures par le jeu des méthodes qui les caractérisent.
▷ Choisir une structure de données adaptée à la situation à modéliser.
▷ Distinguer la recherche d'une valeur dans une liste et dans un dictionnaire.
1 Introduction
Historique
Le langage de programmationLisp (inventé parJohn McCarthy en 1958) a été un des premiers langages
de programmation à introduire cette notion de liste (Lisp signifie list processing).
Lisp qui fait partie de la plus ancienne famille de langages de programmation à la fois impératifs et
fonctionnels, est devenu dans les années 1970-80 le langage de choix pour la recherche en intelligence
artificielle. Ils sont aujourd'hui utilisés dans de nombreux domaines, de la programmation Web à la
finance.
Python abuse du terme liste qu'il utilise pour ce qui sont destableaux dynamiques munis de méthodes d'accès
typiques des listes. Nous nous intéressons ici à ce que les informaticiens appellent vraiment deslistes.
2 Définition
A retenir!
Une liste est une structure de données permettant de regrouper des données.
Elle est composée de 2 parties :
▷ sa tête notée car (qui signifiecontent of address register ), qui correspond au premier élément
ajouté à la liste.
▷ sa queue notée cdr (qui signifiecontent of decrement registe r), qui correspond au reste de la
liste.
3 Opération sur les listes
Voici les opérations qui peuvent être effectuées sur une liste :
▷ créer une liste vide (souvent notéenil)
▷ tester si une liste est vide
▷ ajouter un élément en tête de liste
▷ supprimer la tête d'une liste et renvoyer cette tête
▷ compter le nombre d'éléments présents dans une liste
▷ un constructeur, historiquement appelé cons, qui permet d'obtenir une nouvelle liste à partir d'une liste
et d'un élément(L1 = cons(x,L))
Il est possible "d'enchaîner" lescons et d'obtenir ce genre de structure :cons(x, cons(y, cons(z,L)))
T. Rahobisoa 1/6 SD02 - Les listes
Terminale - Spécialité NSI IFS Singapour
4 Représentation graphique
Voici la représentation schématique d'une liste comportant, dans cet ordre, les trois éléments1, 2 et 4 :
La liste est constituée de troiscellules, représentées ici par des rectangles.
Chaque cellule possède :
— une première partie nomméecar , qui contient l'entier correspondant
— une deuxième partie, nommée cdr , qui contient un lien vers la cellule suivante.
On a donc affaire à une chaîne de cellules qu'on appelle plus couramment uneliste chaînée.
Le champ cdr de la dernière cellule renvoie vers une liste vide, conventionnellement représentée par un hachu-
rage. On notera que le premier champ d'une cellule contient ici un entier (car on considère une liste d'entiers)
alors que le deuxième est une liste, c'est-à-dire un lien vers une autre cellule.
Nous venons de définir les contours de la structure de liste. Celle-ci est un concept ("une vue de l'esprit") de ce
qu'est une liste. On dit que c'est un untype abstrait de données .
5 Implémentation
Pour implémenter cette structure de liste chaînée, peu importe le langage utilisé, il faut que l'implémentation
permette de retrouver les fonctions qui ont été définies pour le type abstrait.
5.1 Implémentation n °1
En utilisant destuples pour implémenter la structure de liste.
T. Rahobisoa 2/6 SD02 - Les listes
Terminale - Spécialité NSI IFS Singapour
Ce qui donne les fonctionsPython suivantes :
1 def vide () :
2 return None
3
4 def cons (x , L ) :
5 return (x , L )
6
7 def a j o u t e E n T e t e (L , x ) :
8 return cons (x , L )
9
10 def estVide ( L ) :
11 return L is None
12
13 def compte ( L ) :
14 if estVide ( L ) :
15 return 0
16 else :
17 return 1 + compte ( L [1])
A faire 1 : Implémentation en tuples
1. Vérifier le bon fonctionnement de cette implémentation en exécutant les instructions ci-dessous et en
notant l'affichage obtenu.
▷ nil = vide()
▷ print(estVide(nil))
▷ L = cons(5,cons(4,cons(3,cons(2,cons(1,cons(0,nil))))))
▷ print(L)
▷ print(estVide(L))
▷ print(compte(L))
▷ L = ajouteEnTete(L,6)
▷ print(compte(L))
▷ print(L)
2. Ecrire une fonctionsupprEnTete(L) qui supprime l'en-tête de la liste passée en paramètre :
3. Tester si la fonction que vous venez d'écrire fonctionne en essayant les instructions ci-dessous et en notant
l'affichage obtenu.
▷ L = supprEnTete(L)
▷ print(L)
▷ print(compte(L))
4. Qu'en concluez-vous?
T. Rahobisoa 3/6 SD02 - Les listes
Terminale - Spécialité NSI IFS Singapour
5.2 Implémentation n °2
Maintenant, on va implémenter les listes chaînées en utilisant laprogrammation orientée objet à l'aide de deux
classes :
▷ la classe Cellule qui crée un objet (instance) cellule avec les attributscar et cdr
1 class Cellule :
2 def __init__ ( self , tete , queue ) :
3 self . car = tete
4 self . cdr = queue
▷ la classe Liste dont les instances (objets) seront de typeCellule, avec quelques méthodes :
1 class Liste :
2 def __init__ ( self , c ) :
3 self . cellule = c
4
5 def estVide ( self ) :
6 return self . cellule is None
7
8 def car ( self ) :
9 assert not ( self . cellule is None ) , ' Liste vide '
10 return self . cellule . car
11
12 def cdr ( self ) :
13 assert not ( self . cellule is None ) , ' Liste vide '
14 return self . cellule . cdr
▷ La fonction cons qui permet de construire la liste :
1 def cons ( tete , queue ) :
2 return Liste ( Cellule ( tete , queue ) )
Ainsi pour créer une la listeL = [5, 4, 3, 2, 1, 0] , il suffit d'exécuter les instructions :
1 nil = Liste ( None )
2 L = cons (5 , cons (4 , cons (3 , cons (2 , cons (1 , cons (0 , nil ) ) ) ) ) )
A faire 2 : 1. Tester les instructions suivantes et noter les résultats obtenus :
1 print ( L . estVide () )
2 print ( L . car () )
3 print ( L . cdr () . car () )
4 print ( L . cdr () . cdr () . car () )
2. Écrire l'instruction qui permet d'afficher le dernier élément de la liste.
T. Rahobisoa 4/6 SD02 - Les listes
Terminale - Spécialité NSI IFS Singapour
A faire 3 : Fonctions supplémentaires
1. Ajouter les deux fonctions suivantes :
1 def l o n g u e u r L i s t e ( L ) :
2 n = 0
3 while not ( L . estVide () ) :
4 n += 1
5 L = L . cdr ()
6 return n
1 def l i s t e E l e m e n t s ( L ) :
2 t = []
3 while not ( L . estVide () ) :
4 t . append ( L . car () )
5 L = L . cdr ()
6 return t
2. Que font-elles?
3. Que produit l'instruction ci-dessous?
1 L = cons (6 , L )
4. Écrire une fonctionajouteEnTete qui prend en paramètre une liste et un nombre et qui renvoie une liste
dans laquelle le nombre a été ajouté en entête.
5. Que produisent les instructions suivantes?
1 x = L . car ()
2 L = cons ( L . cdr () . car () ,L . cdr () . cdr () )
T. Rahobisoa 5/6 SD02 - Les listes
Terminale - Spécialité NSI IFS Singapour
6. Écrire une fonction supprEnTete qui prend en paramètre une liste et qui retourne son entête et la liste
amputée de l'entête.
6 Exercices
Dans les exercices ci-après, on suppose que l'on utilise l'implémentation de liste chaînée suivante :
1 class Cellule :
2 ''' une cellule d ' une liste chainee '''
3
4 def __init__ ( self ,v , s ) :
5 self . valeur = v
6 self . suivante = s
Exercice 1 : Ecrire une fonction listeN(n) qui reçoit en argument un entiern, supposé positif ou nul, et
renvoie la liste des entiers 1,2,..., n dans cet ordre. Si n = 0, la liste renvoyée est vide.
Exercice 2 : Ecrire une fonction affiche(n) qui affiche tous les éléments de la listelst, séparés par des
espaces, suivis d'un retour chariot. L'écrire en récursif puis en itératif avec une bouclewhile.
Exercice 3 : Ecrire une fonctionoccurences(x,lst) qui renvoie le nombre d'occurences de la valeurx dans
la liste lst. L'écrire en récursif puis en itératif avec une bouclewhile.
Exercice 4 : Ecrire une fonction trouve(x,lst) qui renvoie le rang de la première occurence dex dans la
liste lst. L'écrire en récursif puis en itératif avec une bouclewhile.
Exercice 5 : Ecrire une fonction identiques(l1,l2) qui renvoie un booléen indiquant si les listesl1 et l2
sont identiques, c'est-à-dire contiennent exactement les mêmes éléments, dans le même ordre.
Exercice 6 : Ecrire une fonction récursive inserer(x,lst) qui prend en argument un entierx et une liste
d'entiers lst, supposée triée par ordre croissant, et qui renvoie une nouvelle liste dans laquellex a été inséré à
sa place. Ainsi, insérer la valeur3 dans la liste[1,2,5,8] renvoie la liste[1,2,3,5,8].
Exercice 7 : En se servant de l'exercice précédent, écrire une fonction récursivetri_par_insertion(lst) qui
prend en argument une liste d'entierslst et renvoie une nouvelle liste, contenant les mêmes éléments et triée
par ordre croissant.
Exercice 8 : Ecrire une fonction liste_de_tableau(t) qui renvoie une liste qui contient les éléments du
tableau t, dans le même ordre. On suggère de l'écrire avec une bouclefor.
Exercice 9 : Ecrire une fonction derniere_cellule(lst) qui renvoie la dernière cellule de la listelst. On
suppose la listelst non vide.
T. Rahobisoa 6/6 SD02 - Les listes

## Les piles

### Les piles

Terminale - Spécialité NSI IFS Singapour
Chapitre 6 - Les piles
Objectifs :
▷ Connaître et comprendre le type abstrait pile.
▷ Modéliser puis simuler le comportement d'une pile.
▷ Distinguer les modes FIFO et LIFO des piles et des files.
1 Introduction
Dans ce chapitre nous allons décrire desstructures de données linéairesappelées piles. Il faut bien com-
prendrequelorsqu'onparledestructurededonnées,onparled'unereprésentation abstraitequin'estpasenlien
direct avec son implémentation qui peut être réalisée de diverses manières suivant le langage de programmation,
voire au sein d'un même langage de programmation.
2 Définition
A retenir!
En informatique, une pile (stack en anglais) est une structure de données fondée sur le principe du
dernier arrivé, premier sorti(ou LIFO pour Last In, First Out).
Cela signifie que les derniers éléments ajoutés à la pile seront les premiers à être récupérés.
Le fonctionnement est donc celui d'unepile d'assiettes: on ajoute des assiettes sur la pile, et on les récupère
dans l'ordre inverse, en commençant par la dernière ajoutée.
3 Exemples d'usage
Voici quelques exemples d'usage courant d'une pile :
▷ Dans un navigateur web, une pile sert àmémoriser l'historique des pages web visitées. L'adresse de
chaque nouvelle page visitée est empilée et l'utilisateur dépile l'adresse de la page précédente en cliquant
le bouton«Afficher la page précédente».
▷ L'évaluation desexpressions mathématiques en notation post-fixée(ou polonaise inverse) utilise
une pile.
▷ La fonction“Annuler” (en anglaisUndo) d'un logiciel (photo, traitement de texte, ..., etc.) mémorise
les dernières modifications effectuées dans une pile.
T. Rahobisoa 1/6 SD03 - Les piles
Terminale - Spécialité NSI IFS Singapour
4 Implémentation
Pour implémenter une structure de pile, on a besoin d'implémenter seulement un nombre réduit d'opérations
de bases qui sont :
▷ empiler : ajoute un élément sur la pile. Terme anglais correspondant :push
▷ dépiler : enlève un élément de la pile et le renvoie. En anglais :pop
▷ vide : renvoie vrai si la pile est vide, faux sinon
▷ remplissage : renvoie le nombre d'éléments dans la pile
La structure de pile est unconcept abstrait. Comment faire pour réaliser une pile dans la pratique?
L'idée principale étant que les fonctions de bases pourront être utilisées indépendamment de l'implémentation
choisie.
4.1 Implémentation n °1
Nous utiliserons une simple liste pour représenter la pile. Il se trouve que les méthodesappend et pop sur les
listes jouent déjà le rôle depush et pop sur les piles.
Voici les fonctions de base :
1 def pile () :
2 ''' Retourne une liste vide '''
3 return []
4
5 def vide ( p ) :
6 ''' Renvoie True si la pile est vide et False sinon '''
7 return p == []
8
9 def empiler (p , x ) :
10 ''' Ajoute l ' element x a la pile p '''
11 return p . append ( x )
12
13 def depiler ( p ) :
14 ''' Depile et renvoie l ' element au sommet de la pile p '''
15 assert not vide ( p ) , " Pile vide "
16 return p . pop ()
A faire 1 :Tester les instructions suivantes :
1 p = pile ()
2
3 for i in range (5) :
4 empiler (p ,2* i )
5
6 a = depiler ( p )
7 print ( a )
8 print ( vide ( p ) )
Expliquer les affichages obtenus :
T. Rahobisoa 2/6 SD03 - Les piles
Terminale - Spécialité NSI IFS Singapour
A faire 2 :Réaliser lesfonctions taille(p) et sommet(p) qui retournent respectivement la taille de la pile
et le sommet de la pile (sans le supprimer).
4.2 Implémentation n °2
Nous allons utiliser laPOO afin de créer une classePile pour implémenter cette structure.
1 class Pile :
2 ''' classe Pile , creation d ' une instance Pile avec une liste '''
3
4 def __init__ ( self ) :
5 ''' I n i t i a l i s a t i o n d ' une pile vide '''
6 self . L = []
7
8 def vide ( self ) :
9 ''' Teste si la pile est vide '''
10 return self . L == []
11
12 def depiler ( self ) :
13 ''' Depile la dernier element de la pile '''
14 assert not self . vide () , ' Pile vide '
15 return self . L . pop ()
16
17 def empiler ( self , x ) :
18 ''' Empile l ' element x en haut de la pile '''
19 return self . L . append ( x )
Tester les instructions suivantes :
1 p = Pile ()
2 for i in range (5) :
3 p . empiler (2* i )
4
5 print ( p . L )
6 a = p . depiler ()
7 print ( a )
8
9 print ( p . L )
10 print ( p . vide () )
A faire 3 :Réaliser lesméthodes taille(self) et sommet(self) qui retournent respectivement la taille de
la liste et le sommet de la liste (sans le supprimer).
T. Rahobisoa 3/6 SD03 - Les piles
Terminale - Spécialité NSI IFS Singapour
5 Exercices
Exercice 1 :On considère l'enchaînement d'opérations ci-dessous.
Écrire à chaque étape l'état de la pilep et la valeur éventuellement renvoyée. On prendra pour convention que
la tête de la pile est à droite.
p = Pile ()
p . empiler (3)
p . empiler (5)
p . vide ()
p . empiler (1)
p . depiler ()
p . depiler ()
p . empiler (9)
p . depiler ()
p . depiler ()
p . vide ()
Exercice 2 :Historique de navigation
Simulez une gestion de l'historique de navigation Internet, en créant une classe Nav qui utilisera une pile.
Attention, il ne faut pas réinventer la classePile, mais s'en servir!
Exemple d'utilisation :
>>> n = Nav ()
>>> n . visite ( ' lemonde . fr ')
page actuelle : lemonde . fr
>>> n . visite ( ' google . fr ')
page actuelle : google . fr
>>> n . visite ( ' ifs . edu . sg ')
page actuelle : ifs . edu . sg
>>> n . back ()
page quittee : ifs . edu . sg
>>> n . back ()
page quittee : google . fr
Exercice 3 :Vérificateur de parenthèses
La vérification du parenthésage est une étape importante lors de l'analyse d'une expression mathématique ou
informatique lors de l'interprétation dans un éditeur de code tel queThonny, EduPython ou Studio Code.
Par exemple '(())' et '(()())' sont valides mais pas'(()' ou '(()))'. Pour l'instant nous allons supposer
que les expressions sont uniquement composées de'(' et ')'.
Écrire une fonctionverif_parentheses(expression) qui prend un texte et renvoie un booléen qui indique si
l'expression est correcte au niveau des parenthèses.
Pour vérifier la validité d'une expression, nous allons utiliser une pile. Les parenthèses ouvrantes seront empilées
et elles seront dépilées lors de la lecture de parenthèses fermantes. Une expression est correcte si après avoir
lu toute l'expression, la pile est vide. Si une exception est levée lors de l'appel de la méthode dePile, votre
fonction doit la récuperer et renvoyerFalse.
>>> v e r i f _ p a r e n t h e s e s ( ' (((() ) ) ) ')
True
>>> v e r i f _ p a r e n t h e s e s ( ' (((() () ) ) ) ')
True
>>> v e r i f _ p a r e n t h e s e s ( ' (((() () ) ) ((() (() ) ) (() ) () ) ) ')
True
>>> v e r i f _ p a r e n t h e s e s ( ' (((() () ) ) (((((() ) ((() ) ) ) ) () (() ) ) () ) (() () () ) ) ) ')
False
>>> v e r i f _ p a r e n t h e s e s ( ' (((() () ) ) ((((() ) ((() ) ) ) ) () (() ) ) (() ) (() () () ) ) ) ')
False
T. Rahobisoa 4/6 SD03 - Les piles
Terminale - Spécialité NSI IFS Singapour
Exercice 4 :Vérificateur de parenthèses amélioré
Nous allons maintenant rajouter les accolades'{}' et les crochets'[]'.
Ainsi '([{}])' est valide mais pas'([{]})'. Modifier la fonctionverif_parentheses(expression) de l'exer-
cice précédent pour pouvoir utiliser ces nouveaux types de parenthèses. Il faut vérifier lorsqu'on dépile que la
parenthèse fermante correspont à la parenthèse ouvrante dépilée.
>>> v e r i f _ p a r e n t h e s e s ( ' { { } } [ [ ] ] ( ( ) ) ')
True
>>> v e r i f _ p a r e n t h e s e s ( ' { { [ ( [ ] [ { } ] ) ]([{}]) }} ')
True
>>> v e r i f _ p a r e n t h e s e s ( ' ([) ] ')
False
>>> v e r i f _ p a r e n t h e s e s ( ' { { [ ( [ ] [ { } ] ) ] [ ( { ( ( ( [ ] ) ) ) }[]]) }{{[{() }]}}} ')
False
>>> v e r i f _ p a r e n t h e s e s ( ' { { [ ( [ ] [ { } ] ) ]( [{ (( [] ) {{}}() ([]) ) ) }[]]) }{{[{() }]}}} ')
False
>>> v e r i f _ p a r e n t h e s e s ( ' { { [ ( [ ] [ { } ] ) ] ( [ { ( ( ( [ ] ) ) ) }[]]) }{{[{() }]}} ')
False
Exercice 5 :Sujet Bac 2022 (épreuve pratique n°16)
Cet exercice utilise des piles qui seront représentées en Python par des listes (de typelist).
On rappelle que :
— l'expression T1 = list(T) fait une copie deT indépendante de T
— l'expression x = T.pop() enlève le sommet de la pileT et le place dans la variablex
— l'expression T.append(v) place la valeurv au sommet de la pileT.
CompléterlecodePythondelafonction positifci-dessousquiprendunepile Tdenombresentiersenparamètre
et qui renvoie la pile des entiers positifs dans le même ordre, sans modifier la variableT.
1 def positif ( T ) :
2 T2 = ...( T )
3 T3 = ...
4 while T2 != []:
5 x = ...
6 if ... >= 0:
7 T3 . append (...)
8 T2 = []
9 while T3 != ...:
10 x = T3 . pop ()
11 ...
12 print ( 'T = ' ,T )
13 return T2
Exemple :
>>> positif ([ -1 ,0 ,5 , -3 ,4 , -6 ,10 ,9 , -8])
[0 , 5 , 4 , 10 , 9]
T. Rahobisoa 5/6 SD03 - Les piles
Terminale - Spécialité NSI IFS Singapour
Exercice 6 :Notation polonaise inverse
Historique
Lanotation polonaise inversenotéeNPI (en anglaisRPN pour Reverse Polish Notation), également
connue sous le nom denotation post-fixée, permet d'écrire de façon non ambiguë les formules arith-
métiques sans utiliser de parenthèses. Elle est dérivée de la notation polonaise utilisée pour la première
fois en 1924 par le mathématicien polonaisJan Łukasiewicz, la NPI a été inventée par le philosophe et
informaticien australien Charles Leonard Hamblindans le milieu des années 1950, pour permettre les
calculs sans faire référence à une quelconque adresse mémoire. À la fin des années 1960, elle a été diffusée
dans le public comme interface utilisateur avec les calculatrices de bureau deHewlett-Packard.
Exemple :
Voici une expression algébrique en notation infixée (celle que nous utilisons la plupart du temps) :((3 + 4)∗ 2)3
En notation post-fixée (NPI) cela donne :3 4 + 2 * 3 ∧
L'objectif est d'écrire un programme pour évaluer des expressions écrites en notation polonaise inverse.
Les expressions en NPI seront représentées par des tableaux contenant des entiers et des caractères.
Ainsi, l'expression précédente sera représentée par le tableau :expr = [3,4,'+',2,'*',3,' ∧']
Le principe
Une pile vide est créée; le tableau est parcouru de gauche à droite.
▷ Chaque nombre rencontré est empilé.
▷ Si l'élément rencontré est un opérateur, on dépile le sommet et le sous-sommet puis on empile le
résultat du calcul (sous-sommet "opération" sommet ).
▷ Si l'élément rencontré est une fonction (comme : p ), on dépile le sommet et on calcule la valeur
de la fonction pour le sommet, puis on empile le résultat
1. Donner les tableaux qui vont représenter les calculs suivants :
(a) 2 + 20 * 2
(b) 2 * (10 * 2 + 1)
(c) 10 + 20 + 12
(d) (10 + 4 / 2) * 2 + (3 * 3 * (4 / 2))
2. Écrire un programme Python qui permette d'implémenter le calcul d'expressions en NPI et le tester avec
les expressions précédentes.
Exercice 7 :Sujet Bac 2025 - Amérique du Sud (épreuve écrite)
Sur feuille ou dans unGoogle Doc, répondre aux questions de l'exercice 2 du sujet suivant.
T. Rahobisoa 6/6 SD03 - Les piles

## Les files

### Les files

Terminale - Spécialité NSI IFS Singapour
Chapitre 7 - Les files
Objectifs :
▷ Connaître et comprendre le type abstrait file.
▷ Modéliser puis simuler le comportement d'une file.
▷ Distinguer les modes FIFO et LIFO des piles et des files.
1 Introduction
Dans ce chapitre nous allons décrire desstructures de données linéairesappelées files. On rappelle qu'une
structure de données est une organisation logique des données permettant de simplifier ou d'accélérer leur
traitement.
Il faut bien comprendre que lorsqu'on parle de structure de données, on parle d'une représentationabstraite
qui n'est pas en lien direct avec son implémentation qui peut être réalisée de diverses manières suivant le langage
de programmation, voire au sein d'un même langage de programmation.
2 Définition
A retenir!
En informatique, unefile (appelée queue en anglais) est une structure de données basée sur le principe
« Premier entré, premier sorti », en anglaisFIFO (First In, First Out).
Cela signifie que les premiers éléments ajoutés à la file seront les premiers à être récupérés.
Lefonctionnementressembleàla queued'unecaissedesupermarchéparexemple.Ainsi,lespremièrespersonnes
à arriver sont les premières personnes à sortir de la file.
T. Rahobisoa 1/6 SD04 - Les files
Terminale - Spécialité NSI IFS Singapour
Warning!
Attention à ne pas confondre lapile qui utilise le principe duLIFO Last In, First Outavec lafile qui
utilise le principe duFIFO First In, First Out.
3 Exemples d'usage
En général, on utilise des files pour mémoriser temporairement des transactions qui doivent attendre pour être
traitées, comme par exemple :
▷ les serveurs d'impression, qui doivent traiter les requêtes dans l'ordre dans lequel elles arrivent, et les
insèrent dans une file d'attente (ou une queue).
▷ les moteurs multitâches, dans un système d'exploitation, qui doivent accorder du temps-machine à
chaque tâche, sans en privilégier aucune.
4 Implémentation
Pour implémenter une structure de file, on a besoin d'implémenter seulement un nombre réduit d'opérations de
bases qui sont :
▷ enfiler : ajoute un élément dans la file. Terme anglais correspondant :enqueue
▷ défiler : enlève un élément de la file et le renvoie. En anglais :dequeue
▷ vide : renvoie vrai si la file est vide, faux sinon
▷ remplissage : renvoie le nombre d'éléments dans la file
T. Rahobisoa 2/6 SD04 - Les files
Terminale - Spécialité NSI IFS Singapour
La structure de file est unconcept abstrait. Comment faire pour réaliser une pile dans la pratique?
L'idée principale étant que les fonctions de bases pourront être utilisées indépendamment de l'implémentation
choisie.
4.1 Implémentation n °1
Dans cette implémentation, nous utiliserons une simple liste Python pour représenter la file. On utilise donc
encore append(x) et pop(0) pour réaliser les méthodesenfiler et defiler.
Voici les fonctions de base :
1 def file():
2 ''' Retourne une liste vide'''
3 return []
4
5 def vide(f):
6 '''Renvoie True si la file est vide et False sinon'''
7 return f == []
8
9 def enfiler(f,x):
10 '''Ajoute l'element x a la file f'''
11 return f.append(x)
12
13 def defiler(f):
14 '''Eleve et renvoie le premier element de la file'''
15 assert not vide(f), "Pile vide"
16 return f.pop(0)
A faire 1 :Tester les instructions suivantes :
1 f=file()
2 for i in range(5):
3 enfiler(f,2*i)
4
5 print(f)
6 a=defiler(f)
7 print(a)
8 print(f)
9 print(vide(f))
Expliquer les affichages obtenus :
T. Rahobisoa 3/6 SD04 - Les files
Terminale - Spécialité NSI IFS Singapour
A faire 2 :Réaliser lesfonctions taille(f) et sommet(f) qui retournent respectivement la taille de la liste
et le premier élément de la liste (mais sans le supprimer!).
4.2 Implémentation n °2
Nous allons utiliser la POO afin de créer une classeFile pour implémenter cette structure. En vous inspirant
de ce que l'on a vu pour la classePile dans le chapitre précédent, compléter puis tester l'implémentation
ci-dessous :
1 class File:
2 '''classe File, creation d'une instance File avec une liste'''
3
4 def __init__(self):
5 '''Initialisation d'une file vide'''
6 ...
7
8 def vide(self):
9 '''Teste si la pile est vide'''
10 return ...
11
12 def defiler(self):
13 '''Defile'''
14 ...
15 ...
16
17 def enfiler(self,x):
18 '''Enfile l'element x dans la file'''
19 ...
20 ...
Écrire les instructions permettant de :
▷ créer une file
▷ la remplir avec les entiers0,2,4,6,8
▷ la faire afficher
▷ "défiler" la file en faisant afficher l'élément récupéré.
A faire 3 :Réaliser lesméthodes taille(self) et sommet(self) qui retournent respectivement la taille de
la liste et le premier élément de la liste (mais sans le supprimer!).
T. Rahobisoa 4/6 SD04 - Les files
Terminale - Spécialité NSI IFS Singapour
5 Exercices
Exercice 1 :Soit une fileF initialement vide.
On considère l'enchaînement d'opérations ci-dessous.
enfiler(F,6)
enfiler(F,3)
a = defiler(F)
enfiler(F,9)
b = taille(F)
enfiler(F,17)
c = defiler(F)
enfiler(F,2)
d = taille(F)
Donner le contenu de la fileF, la valeur dea, la valeur deb, la valeur dec et la valeur ded.
Exercice 2 :Soit le programme Python suivant :
1 pile = []
2 tab = [5,8,6,1,3,7]
3 pile.append(5)
4 pile.append(10)
5 pile.append(8)
6 pile.append(15)
7 for i in tab:
8 if i > 5:
9 pile.pop()
Donner l'état de la pilepile après l'exécution de ce programme.
Exercice 3 :On dispose d'unefile. Ecrire une fonction qui renvoie la file inversée (l'élément de la tête sera
situé à la queue et ainsi de suite). On utilisera une pile et seulement les méthodes associées aux piles et aux
files.
Exercice 4 :On dispose d'unepile. Ecrire une fonction qui renvoie lapile inversée(l'élément en haut de la
pile sera situé en bas de la pile et ainsi de suite). On utilisera une pile et seulement les méthodes associées aux
piles et aux files.
Exercice 5 :On dispose d'unefile contenant des entiers, écrire une fonction qui renvoie unefile où on aura
séparé les nombres pairs des impairs.
Exercice 6 :On dispose d'unepile contenant des entiers, écrire une fonction qui renvoie unepile où l'on aura
séparé les nombres pairs des impairs.
Exercice 7 :On dispose d'unepile contenant des entiers, écrire une fonction ou une méthode qui renvoie une
pile où l'on aura supprimé le premier élément entré.
Exercice 8 :On dispose d'unefile contenant des entiers, écrire une fonction ou une méthode qui renvoie une
file où l'on aura supprimé le dernier élément entré.
Exercice 9 :Utilisez ce simulateur pour cet exercice :https: // trahobisoa. github. io/ Simulateur_ pile_
file_ liste_ chainee/
1. Liste chaînée :Insérez successivement les valeurs 10, 20 et 30 en queue de liste.
Question : Observez l'animation. Comment les éléments (nœuds) sont-ils reliés entre eux, et vers quoi
pointe le dernier élément (la queue) de la liste?
2. Vers la file :Retirez ces éléments un par un par la tête de la liste et enfilez-les dans unefile. La valeur 10
se trouve-t-elle à l'avant (front) ou à l'arrière (back) de la file?
3. Vers la pile :Défilez tous les éléments de votre file un par un pour les empiler immédiatement dans une
pile. Où se trouve la valeur 10 (au sommet ou au fond)?
4. Dépilez tous les éléments un par un. Quel est l'ordre final de sortie? Que pouvez-vous conclure sur l'effet
d'un transfert d'une File vers une Pile sur une série de données?
T. Rahobisoa 5/6 SD04 - Les files
Terminale - Spécialité NSI IFS Singapour
Exercice 10 :Sujet Bac 2022 (Amérique du Nord)
Les interfaces des structures de données abstraitesPile et File sont proposées ci-dessous :
Structure de données abstraite : Pile
Opérations :
creer_pile_vide() renvoie une pile vide
est_vide(pile) renvoie True si pile est vide,False sinon
empiler(pile,element) ajoute element à la pile
depiler(pile) renvoie l'élément au sommet de la pile en le retirant de la pile
Structure de données abstraite : File
Opérations :
creer_file_vide() renvoie une file vide
est_vide(file) renvoie True si file est vide,False sinon
enfiler(file,element) ajoute element à la file
defiler(pile) renvoie le premier élément de la file en le retirant de la file
On considère la fileF suivante :
enfilement → "rouge", "vert", "jaune", "rouge", "jaune" → défilement
On utilisera uniquement les fonctions ci-dessus.
1. Quel sera le contenu de la pileP et de la fileF après l'exécution du programme Python suivant?
P = creer_pile_vide()
while not(est_vide(F)):
empiler(P, defiler(F))
2. Créer une fonctiontaille_file qui prend en paramètre une fileF et qui renvoie le nombre d'éléments
qu'elle contient. Après appel de cette fonction la fileF doit avoir retrouvé son état d'origine.
def taille_file(F):
"""File -> Int"""
...
3. Écrire une fonctionformer_pile qui prend en paramètre une fileF et qui renvoie une pileP contenant les
mêmes éléments que la file.
Le premier élément sorti de la file devra se trouver au sommet de la pile; le deuxième élément sorti de la
file devra se trouver juste en-dessous du sommet,..., etc.
4. Écrire une fonctionnb_elements qui prend en paramètres une fileF et un élémentelt et qui renvoie le
nombre de fois où elt est présent dans la fileF. Après appel de cette fonction la fileF doit avoir retrouvé
son état d'origine.
5. Écrire une fonction verifier_contenu qui prend en paramètres une fileF et trois entiers :nb_rouge,
nb_vert et nb_jaune. Cette fonction renvoie le booléenTrue si “rouge” apparaît au plusnb_rouge fois
dans la fileF, “vert” apparaît au plusnb_vert fois dans la fileF et “jaune” apparaît au plusnb_jaune
fois dans la fileF. Elle renvoieFalse sinon. On pourra utiliser les fonctions précédentes.
Exercice 11 :Le problème de Josèphe
Flavius Josèphe était un historien juif du premier siècle. Il participa aux révoltes contre les Romains et fut
assiégé avec quarante de ses compatriotes dans la forteresse deJotapata en 67 après J.C. Les 41 soldats (dont
Flavius Josèphe), cernés par des soldats romains, décident de se suicider. Ils se mettent en cercle, et un premier
soldat est choisi au hasard pour être exécuté; puis le troisième à partir de sa gauche est exécuté. Tant qu'il y a
des soldats, la sélection continue de la même façon.
Le but est de trouver à quelle place doit se tenir un soldat pour être le dernier. Josèphe, peu enthousiaste à
l'idée de mourir, parvint à trouver cette place. Quelle est-elle?
En utilisant une file trouver la position à choisir parmi les 41 soldats pour être le dernier éliminé.
T. Rahobisoa 6/6 SD04 - Les files

## Les arbres

### Les arbres

Terminale - Spécialité NSI IFS Singapour
Chapitre 11 - Les arbres
Objectifs :
▷ Identifier des situations nécessitant une structure de données arborescente.
▷ Connaître le vocabulaire des arbres : noeud, racine, feuille, hauteur, taille, ...,etc.
▷ Évaluer quelques mesures des arbres binaires (taille, encadrement de la hauteur, etc.).
1 Introduction
Il n'existe pas seulement une façonlinéaire de structurer les données comme avec les listes, les piles ou les files.
Nous pouvons également structurer des données de façonhiérarchique.
Par exemple, lorsqu'on utilise unarbre de classification des animaux:
Ou encore, lorsqu'on crée le très classiquearbre généalogique:
T. Rahobisoa 1/7 SD05 - Les arbres
Terminale - Spécialité NSI IFS Singapour
Parfois, on utilise même ce mode de représentation graphique pour l'apprentissage d'une langue.
Un arbre syntaxiquereprésente l'analyse d'une phrase à partir de règles de grammaire. Par exemple :
Il existe aussi desarbres lexicographiques. Appelé aussidictionnaire, il représente un ensemble de mots.
Les préfixes communs à plusieurs mots apparaissent une seule fois dans l'arbre.
Dans les systèmes d'exploitation (Windows, MacOS, Linux), le disque dur est représenté et organisé suivant
une arborescence comme ci-dessous :
T. Rahobisoa 2/7 SD05 - Les arbres
Terminale - Spécialité NSI IFS Singapour
On peut également représenter lesexpressions arithmétiques par des arbres étiquetés par des opérateurs,
des constantes et des variables.
La structure de l'arbre rend compte de la priorité des opérateurs et rend inutile tout parenthésage.
Quelle est l'expression arithmétique représentée par cet arbre?
Réponse :
En utilisant le même principe, représenter l'expression suivante :
( y
2 − t
)
× (75 + z)
Réponse :
Les arbres sont très utilisés en informatique, d'une part parce que les informations sont souventhiérarchisées
et peuvent se représenter naturellement sous une forme arborescente, et d'autre part, parce que les structures de
données arborescentes permettent de stocker des donnéesvolumineuses de façon que leur accès soitefficace.
T. Rahobisoa 3/7 SD05 - Les arbres
Terminale - Spécialité NSI IFS Singapour
2 Notions générales sur les arbres
On peut considérer un arbre comme une généralisation d'une liste car les listes peuvent être représentées par
des arbres. Plutôt que de chercher à définir ce qu'est un arbre, nous observerons quelques schémas :
Figure 1 – Représentation graphique d'une forêt
Figure 2 – Représentation graphique d'un arbre
Attention, la représentation graphique ci-dessous n'est pas celle d'un arbre car il existe un chemin d'un sommet
vers lui-même (appelé un cycle).
Figure 3 – Représentation graphique d'un cycle
Lorsqu'un sommet se distingue des autres, on le nommeracine de l'arbre et celui-ci devient alors unearbo-
rescence (par la suite on utilisera le mot arbre pour une arborescence).
Les 3 arbres ci-dessous représentent la même structure, cependant pour deux d'entre eux, un sommet peut être
désigné comme racine.
Figure 4 – Racines d'un arbre
Lorsqu'on dessine un arbre, on a l'habitude de le représenter avec la tête en bas, c'est-à-dire quela racine est
tout en haut, et les nœuds fils sont représentés en dessous du nœud père.
T. Rahobisoa 4/7 SD05 - Les arbres
Terminale - Spécialité NSI IFS Singapour
3 Définitions et vocabulaire
3.1 Etiquette
A retenir!
Un arbre dont tous les nœuds sont nommés est dit étiqueté. L'étiquette (ou nom du sommet) représente
la valeur du nœud ou bien l'information associée au nœud.
Ci-dessus un arbre étiqueté avec les entiers entre 2 et 8.
3.2 Racine, noeud, branche, feuille
A retenir!
▷ Un arbre est un ensemble organisé denœuds dans lequel chaque nœud a un père, sauf un nœud
que l'on appelle laracine.
▷ Si le nœud n'a pas de fils, on dit que c'est unefeuille.
▷ Les nœuds sont reliés par desbranches.
T. Rahobisoa 5/7 SD05 - Les arbres
Terminale - Spécialité NSI IFS Singapour
3.3 Hauteur d'un noeud
A retenir!
Lahauteur (ouprofondeur ouniveau) d'un nœud X est égale au nombre d'arêtes qu'il faut parcourir
à partir de la racine pour aller jusqu'au nœud X.
Par convention, la hauteur (ou profondeur) de la racine est égale à 0. Mais attention, la définition de la hauteur
d'un nœud varie en fonction des auteurs. Pour certains, la racine a une hauteur de 1.
Dans l'exemple ci-dessus la hauteur du noeud 9 est de 3 et celle du noeud 7 est de 2.
A retenir!
La hauteur (ou profondeur) d'un arbre est égale à la profondeur du nœud le plus profond.
Dans notre exemple, le nœud le plus profond est de profondeur 3, donc l'arbre est de profondeur 3.
Question 1 :Déterminer les profondeurs des arbres de l'introduction :
Réponses :
▷ Arbre de classification :
▷ Arbre généalogique :
▷ Arbre syntaxique :
▷ Arbre lexicographique :
▷ Arborescence de disque dur :
3.4 Taille d'un arbre
A retenir!
La taille d'un arbre est égale au nombre de nœuds de l 'arbre.
Dans notre exemple, l'arbre contient 10 nœuds, sa taille est donc de 10.
T. Rahobisoa 6/7 SD05 - Les arbres
Terminale - Spécialité NSI IFS Singapour
Question 2 :Déterminer les tailles des arbres de l'introduction :
Réponses :
▷ Arbre de classification :
▷ Arbre généalogique :
▷ Arbre syntaxique :
▷ Arbre lexicographique :
▷ Arborescence de disque dur :
3.5 Remarques
Le vocabulaire de lien entre nœuds de niveaux différents et reliés entre eux est emprunté à lagénéalogie.
Dans l'exemple précédent :
▷ 8 est le parent de 9 et de 10
▷ 6 est un enfant de 4
▷ 6 et 7 sont des noeuds frères
▷ 5 est un ancêtre de 9
▷ 10 est un descendant de 5
Un arbre dont tous les nœuds n'ont qu'un seul fils est en fait uneliste.
T. Rahobisoa 7/7 SD05 - Les arbres

## Les arbres binaires

### Les arbres binaires

Terminale - Spécialité NSI IFS Singapour
Chapitre 12 - Les arbres binaires
Objectifs :
▷ Connaître les algorithmes sur les arbres binaires
▷ Calculer la taille et la hauteur d'un arbre binaire
▷ Parcourir un arbre de différentes façons (ordres infixe, préfixe ou suffixe; ordre en largeur ou profondeur
d'abord).
1 Les arbres binaires
Parmi la forêt d'arbres possibles, on s'intéressera essentiellement aux arbres ditbinaires :
1.1 Définition
Définition
Un arbre binaire est un arbre dedegré 2dont les noeuds sont de degré 2au plus.
Vocabulaire :
Les enfants d'un noeud sont lusde gauche à droiteet sont appelés :fils gaucheet fils droit.
Par exemple, l'expressiona× b + c− (d + e) est représentée par l'arbre binaire ci-dessous :
Question 1 :Parmi les arbres du cours sur les arbres (chapitre 10), lesquels sont binaires?
Réponses :
1.2 Remarques
Les arbres binaires forment une structure de données qui peut se définir de façonrécursive.
A retenir!
Un arbre binaire est :
▷ Soit vide.
▷ Soit composé d'une racine portant une étiquette (clé) et d'une paire d'arbres binaires, appelés
sous-arbre gaucheet sous-arbre droit.
T. Rahobisoa 1/9 SD06 - Les arbres binaires
Terminale - Spécialité NSI IFS Singapour
2 Représentations d'un arbre
Les arbres binaires sont utilisés dans de très nombreuses activités informatiques. Mais comment cette structure
de données est-elleimplémentée?
2.0.1 Première méthode : avec un tableau
Par exemple :
r
a b
L 'idée est de représenter l 'arbre avec un tableau :r a b
La racine suivie de ses fils gauche et droit.
r
a
c d
b
e f
Puis on rajoute dans l'ordre les fils gauche et droit dea, puis ceux deb. r a b c d e f
Remarques :
▷ Chaque noeud se repère par son indice n dans la liste, son fils gauche se trouvant alors à l'indice
2n + 1 et son fils droit à l'indice2n + 2.
▷ b est à l'indice 2 son fils gauche se trouve alors à l'indice 5 et son fils droit à l'indice 6.
▷ Si un noeud n'a pas de fils on le précise en mettantNone à sa place.
Notre arbre est alors représenté par le tableau :
1 [r ,a ,b ,c ,d ,e ,f , None , None , None , None , None , None , None , None ]
Quelle taille doit avoir le tableau?
Cet arbre estcomplet (tous les noeuds internes ont deux fils).
Il possède 3 niveaux, sa hauteur ou profondeur est donc de 2.
Donc la taille du tableau sera de :20 + 21 + 22 + 23 = 2 4− 1 = 15
Il faut compter le nombre de noeuds, y compris les noeuds "fantômes" des feuilles.
T. Rahobisoa 2/9 SD06 - Les arbres binaires
Terminale - Spécialité NSI IFS Singapour
Exercice 1 :Tableau
r
a
c
h
d
i j
m
b
e
k
f
1. Quelle est la taille du tableau qui permet de représenter cet arbre?
Réponse :
2. Écrire le tableau représentant cet arbre :
Réponse :
3. Quelle propriété ont les indices des fils gauches et droits?
Réponse :
Exercice 2 :Tableau bis
Voici un tableau représentant un arbre binaire :
1 [ '* ' , ' - ' ,5 ,2 ,6 , None , None , None , None , None , None , None , None , None , None ]
1. Dessiner cet arbre. Que peut-il représenter?
Réponse :
T. Rahobisoa 3/9 SD06 - Les arbres binaires
Terminale - Spécialité NSI IFS Singapour
Voici un code Python qui crée la liste représentant l'arbre de l'exercice 1 :
1 def c r e a t i o n _ a r b r e (r , p r o f o n d e u r ) :
2 ''' r : la racine ( str ou int ) . la p r o f o n d e u r de l ' arbre ( int ) '''
3 Arbre = [ r ]+[ None for i in range (2**( p r o f o n d e u r +1) -2) ]
4 return Arbre
5
6 def i n s e r t i o n _ n o e u d ( arbre ,n , fg , fd ) :
7 ''' Insere les noeuds et leurs enfants dans l ' arbre '''
8 indice = arbre . index ( n )
9 arbre [2* indice +1] = fg
10 arbre [2* indice +2] = fd
11
12 # creation de l ' arbre
13 arbre = c r e a t i o n _ a r b r e ( " r " ,5)
14
15 # ajout des noeuds par niveau de gauche a droite
16 i n s e r t i o n _ n o e u d ( arbre , " r " ," a " ," b " )
17 i n s e r t i o n _ n o e u d ( arbre , " a " ," c " ," d " )
18 i n s e r t i o n _ n o e u d ( arbre , " b " ," e " ," f " )
19 i n s e r t i o n _ n o e u d ( arbre , " c " , None , " h " )
20 i n s e r t i o n _ n o e u d ( arbre , " d " ," i " ," j " )
21 i n s e r t i o n _ n o e u d ( arbre , " e " ," k " , None )
22 i n s e r t i o n _ n o e u d ( arbre , " f " , None , None )
23 i n s e r t i o n _ n o e u d ( arbre , " h " , None , None )
24 i n s e r t i o n _ n o e u d ( arbre , " i " , None , None )
25 i n s e r t i o n _ n o e u d ( arbre , " j " ," m " , None )
26 i n s e r t i o n _ n o e u d ( arbre , " k " , None , None )
27 i n s e r t i o n _ n o e u d ( arbre , " m " , None , None )
28
29 # pour verifier
30 print ( len ( arbre ) )
31 print ( arbre )
Voici une fonction qui retourne le parent d'un noeud s'il est dans l'arbre :
1 def parent ( arbre , p ) :
2 if p in arbre :
3 indice = arbre . index ( p )
4 if indice %2 == 0:
5 return arbre [( indice -2) //2]
6 else :
7 return arbre [( indice -1) //2]
2. Créer les fonctions suivantes :
▷ Une fonction qui retourne vrai si l'arbre est vide.
▷ Une fonction qui retourne les enfants d'un noeud.
▷ Deux fonctions qui retournent le fils gauche d'un noeud et son homologue le fils droit s'ils existent.
▷ Une fonction qui retourne vrai si le noeud est la racine de l 'arbre.
▷ Une fonction qui retourne vrai si le noeud est une feuille.
▷ Une fonction qui retourne vrai si le noeud a un frère gauche ou droit.
T. Rahobisoa 4/9 SD06 - Les arbres binaires
Terminale - Spécialité NSI IFS Singapour
2.0.2 Deuxième méthode : avec un tableau de tableaux
Comme vous l 'avez sans doute constaté, il est assez fastidieux de représenter un arbre avec un unique tableau
surtout pour un arbre très profond.
L 'idée est de représenter l'arbre avecun tableau contenant des tableaux.
Par exemple :
r
a b
Cet arbre se représente par le tableau suivant :
1 [ 'r ' ,[ 'a ' ,[] ,[]] ,[ 'b ' ,[] ,[]]]
Exercice 3 :Tableau de tableaux
r
a
c d
b
e f
1. Écrire le tableau représentant cet arbre :
Réponses :
Le code Python ci-dessous, construit l'arbre de l'exercice 1 de manièrerécursive.
▷ Les noeuds sont représentés par undictionnaire.
▷ L'arbre se construit depuis la racine en construisant les sous-arbres des fils gauche et droit.
1 def noeud ( nom , fg = None , fd = None ) :
2 return { ' racine ': nom , ' fg ': fg , ' fd ': fd }
3
4 # creation des noeuds
5 k = noeud ( 'k ')
6 f = noeud ( 'f ')
7 e = noeud ( 'e ' , k , None )
8 b = noeud ( 'b ' , e , f )
9 m = noeud ( 'm ')
10 j = noeud ( 'j ' , m , None )
11 i = noeud ( 'i ')
12 d = noeud ( 'd ' , i , j )
13 h = noeud ( 'h ')
14 c = noeud ( 'c ' , None , h )
15 a = noeud ( 'a ' , c , d )
16 racine = noeud ( 'r ' , a , b )
17
18 # creation de l ' arbre
19 def co ns tr ui t ( arbre ) :
20 if arbre == None :
21 return []
22 else :
T. Rahobisoa 5/9 SD06 - Les arbres binaires
Terminale - Spécialité NSI IFS Singapour
23 return
[ arbre [ ' racine '] , c on st ru it ( arbre [ ' fg ' ]) , c on st ru it ( arbre [ ' fd ' ]) ]
24
25 arbre1 = co ns tr ui t ( racine )
26 print ( arbre1 )
2. Avec la structure de données récursive ci-dessus, écrire :
▷ Une fonction qui retourne vrai si l'arbre est vide.
▷ Une fonction qui retourne les enfants d'un noeud.
▷ Deux fonctions qui retournent le fils gauche d'un noeud et son homologue le fils droit s'ils existent.
▷ Une fonction qui retourne vrai si le noeud est la racine de l 'arbre.
▷ Une fonction qui retourne vrai si le noeud est une feuille.
▷ Une fonction qui retourne vrai si le noeud a un frère gauche ou droit.
3 Algorithmes de parcours des arbres
Le parcours des arbres, en informatique, désigne les différentes méthodes permettant d'explorer et de visiter
les nœuds d'une structure arborescente. Il existe plusieurs types de parcours :
3.1 Le parcours en largeur
Le parcours d'un arbre en largeur consiste à :
— Partir de la racine.
— On visite ensuite son fils gauche.
— Puis, on visite son fils droit.
— Puis, on visite le fils gauche du fils gauche.
— Puis, on visite le fils droit du fils gauche.
— ..., etc.
Comme le montre le schéma ci-dessous :
L'idée est la suivante :
On utilise la structure de donnéesFile.
1. On met l'arbre dans la file.
2. Puis tant que la file n'est pas vide :
▷ On défile la file.
▷ On récupère sa racine.
▷ On enfile son fils gauche s'il existe.
▷ On enfile son fils droit s'il existe.
T. Rahobisoa 6/9 SD06 - Les arbres binaires
Terminale - Spécialité NSI IFS Singapour
Voici l'algorithme :
Algorithme 1 :Fonction parcours en largeur
Données :Arbre binaire
Sorties :liste
f← file vide
liste← liste vide
tant que f non videfaire
tmp← défiler f
On ajoute tmp[0] à liste
si tmp[1] n'est pas videalors
On enfile tmp[1]
si tmp[2] n'est pas videalors
On enfile tmp[2]
retourner liste
Exercice 4 :Implémenter cette fonction et tester avec l'arbre de l'exercice 1.
Vous devez obtenir :['r','a','b','c','d','e','f' 'h','i','j','k','m']
Vous pouvez utilise la classeFile utilisée dans un précédent chapitre.
3.2 Les parcours en profondeur
On se balade autour de l'arbre en suivant les pointillés :
Dans le schéma ci-dessus, on a rajouté desnoeuds fantômespour montrer que l'on peut considérer que chaque
noeud est visité3 fois:
▷ Une fois par la gauche
▷ Une fois par en dessous
▷ Une fois par la droite
A retenir!
On peut définir les parcours comme suit :
▷ Dans un parcourspréfixe, on liste le noeud lapremière foisqu'on le rencontre.
▷ Dans un parcoursinfixe, on liste le noeud laseconde foisqu'on le rencontre. Ce qui correspond
à : on liste chaque noeud ayant un fils gauche la seconde fois qu'on le voit et chaque noeud sans
fils gauche la première fois qu'on le voit.
▷ Dans un parcourssuffixe, on note le noeud ladernière foisqu'on le rencontre.
T. Rahobisoa 7/9 SD06 - Les arbres binaires
Terminale - Spécialité NSI IFS Singapour
Exercice 5 :Ecrire les sommets de l'arbre ci-dessus dans un parcourspréfixe, infixe et suffixe.
Réponses :
Exercice 6 :Voici 3 algorithmes récursifs, dire pour chacun d'entre eux à quel parcours il correspond.
Algorithme 2 :Fonction parcours(arbre)
Données :Arbre binaire
si l'arbre n'est pas videalors
parcours(sous-arbre gauche)
parcours(sous-arbre droit)
Afficher la racine de l'arbre
Réponse :
Algorithme 3 :Fonction parcours(arbre)
Données :Arbre binaire
si l'arbre n'est pas videalors
Afficher la racine de l'arbre
parcours(sous-arbre gauche)
parcours(sous-arbre droit)
Réponse :
Algorithme 4 :Fonction parcours(arbre)
Données :Arbre binaire
si l'arbre n'est pas videalors
parcours(sous-arbre gauche)
Afficher la racine de l'arbre
parcours(sous-arbre droit)
Réponse :
Exercice 7 :Implémenterlestroisfonctionsci-dessus: parcours_prefixe(), parcours_infixe()et parcours_suffixe()
et confirmer les réponses de l'exercice 5.
T. Rahobisoa 8/9 SD06 - Les arbres binaires
Terminale - Spécialité NSI IFS Singapour
4 Représentation avec une classe
Nous allons créer une classeNoeud dont les attributs d'instances seront :
▷ Le nom (ou valeur) de la racine.
▷ Son fils gauche (vide par défaut).
▷ Son fils droit (vide par défaut).
De plus on rajoute une méthode spécifique, qui permet d'afficher la racine du noeud avec la fonctionprint()
Ci-dessous la classeNoeud et la représentation de l'arbre :
1 class Noeud :
2
3 # Le c o n s t r u c t e u r
4 def __init__ ( self , value , left = None , right = None ) :
5 self . value = value
6 self . left = left
7 self . right = right
8
9 # Methode qui permet d ' afficher la valeur
10 # de la racine avec la fonction print
11 def __str__ ( self ) :
12 return str ( self . value )
13
14 k = Noeud ( 'k ')
15 f = Noeud ( 'f ')
16 e = Noeud ( 'e ' ,k , None )
17 b = Noeud ( 'b ' ,e , f )
18 m = Noeud ( 'm ')
19 j = Noeud ( 'j ' ,m , None )
20 i = Noeud ( 'i ')
21 d = Noeud ( 'd ' ,i , j )
22 h = Noeud ( 'h ')
23 c = Noeud ( 'c ' , None , h )
24 a = Noeud ( 'a ' ,c , d )
25
26 arbre = Noeud ( 'r ' ,a , b )
27 print ( arbre ) # affiche r
Remarque :
On aurait pu écrire la représentation de l'arbre sur une seule ligne mais c'est assez compliqué de ne pas se
perdre...
1 arbre = Noeud ( 'r ' , Noeud ( 'a ' , Noeud ( 'c ' , None , Noeud ( 'h ') ) , Noeud ( 'd ' , Noeud ( 'i ') ,
2 Noeud ( 'j ' , Noeud ( 'm ') , None ) ) ) , Noeud ( 'b ' , Noeud ( 'e ' , Noeud ( 'k ' , None , None ) , None ) ,
Noeud ( 'f ') ) )
Exercice 8 :Écrire une méthodeestFeuille() qui renvoie vrai si le noeud est une feuille et faux sinon.
Exercice 9 :Écrire une méthodehauteur() qui renvoie la hauteur de l'arbre.
Exercice 10 :Écrire les trois méthodes de parcours en profondeur de l'arbre :
— parcours_prefixe()
— parcours_infixe()
— parcours_suffixe()
Confirmer les réponses de l'exercice 5.
Exercice 11 :Faire l'exercice 4 du sujet de Bac 2022 suivant.
T. Rahobisoa 9/9 SD06 - Les arbres binaires

## ABR

### ABR

Terminale - Spécialité NSI IFS Singapour
Chapitre 13 - Les arbres binaires de recherche
Objectifs :
▷ Connaître le principe d'un arbre binaire de recherche
▷ Rechercher une clé dans un arbre de recherche, insérer une clé.
1 Introduction
Les arbres binaires de recherche(notés souventABR) sont des structures de données fondamentales en
informatique et en algorithmique. Ils sont largement utilisés dans de nombreuses applications informatiques
pour leur efficacité dans la recherche, l'insertion et la suppression de données.
On les utilise par exemple pour :
▷ l'implémentation des bases de données indexées
▷ les systèmes de gestion de fichiers
▷ les algorithmes de recherche et de tri
▷ les structures de recherche dans les compilateurs et analyseurs syntaxiques
2 Principe de l'ABR
Un arbre binaire de recherche (ABR)est une structure de donnée composée de noeuds (on parlera aussi
de clés).
A retenir!
Chaque noeud a au plus 2 enfants ordonnés d'une manière particulière :
— les enfantsà gauched'un noeud ont des valeursinférieures ou égalesà celle du noeud.
— les enfantsà droited'un noeud ont des valeursstrictement supérieuresà celle du noeud.
Et cela doit être vrai pour chaque noeud de l'arbre.
Par exemple :
6
8
9
3
1 4
52
7
Les ABR sont utiles dans le cas où l'on effectue desinsertions ou suppressions fréquentes d'éléments ou des
recherches fréquentes.
A retenir!
On parlera aussi d'unarbre équilibrés'il s'agit d'un arbre binaire tel que les deux sous-arbres partant
de chaque nœud autre qu'une feuille ontdes profondeurs différant au maximum de 1.
T. Rahobisoa 1/5 SD07 - Les ABR
Terminale - Spécialité NSI IFS Singapour
Exercice 1 :Préciser si les arbres ci-dessous sont desABR ou pas et s'il s'agit d'arbres équilibrés.
Réponse :
3 Comment construire un ABR ?
Par exemple, on souhaite représenter la liste de nombres[6,8,3,1,4,9,2,7,5]. On va suivre les étapes ci-
dessous en respectant lesrègles d'un ABRédictées précédemment.
Dans un premier temps on crée laracine de l'arbre :
6
Puis, on insère les noeuds successifs en commençant par lenoeud 8:
6
8
Puis, on insère lenoeud 3:
6
83
Puis, on insère lenoeud 1:
6
83
1
Puis, on insère lenoeud 4:
6
83
1 4
T. Rahobisoa 2/5 SD07 - Les ABR
Terminale - Spécialité NSI IFS Singapour
Puis, on insère lenoeud 9:
6
8
9
3
1 4
Puis, on insère lenoeud 2:
6
8
9
3
1 4
2
Puis, on insère lenoeud 7:
6
8
9
3
1 4
2
7
En insérant le derniernoeud 5, on obtient l'arbre binaire équilibré suivant :
6
8
9
3
1 4
52
7
T. Rahobisoa 3/5 SD07 - Les ABR
Terminale - Spécialité NSI IFS Singapour
4 Implémentation des arbres binaires de recherche
Pour implémenter un arbre binaire de recherche, nous allons utiliser une structure de classe. Nous travaillerons
avec le fichierabr.py ci-joint, qui contient une classeNoeud et de quoi faire afficher graphiquement les arbres
que nous construirons.
La classe Noeud possède 4 attributs :
— une valeur value
— un parent parent
— les deux enfants gauche et droite qui sontleft et right
Voici la classeabr.py que nous utiliserons :
1 class Noeud :
2 ''' Noeud d ' un arbre de re ch er ch e '''
3
4 def __init__ ( self , value , left = None , right = None ) :
5 ''' Le c o n s t r u c t e u r '''
6 self . value = value
7 self . left = left
8 self . right = right
9 self . parent = None
10
11 def __str__ ( self ) :
12 ''' Methode qui permet d ' afficher la valeur de la racine
13 avec la fonction print '''
14 return str ( self . value )
15
16
17 def e s t F e u i l l e ( self ) :
18 ''' Methode qui permet de savoir si le noeud est une feuille '''
19 if not self . left and not self . right :
20 return True
21 else :
22 return False
Exercice 2 :Compléter le code Python de la méthodeinsert() ci-dessous qui permet d'ajouter un nœud à
l'arbre binaire de recherche.
1 def insert ( self , valeur ) :
2 if . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . :
3 if self . left is None :
4 self . left = . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5 self . left . parent =
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6 else :
7 self . left . insert ( valeur )
8 elif . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . :
9 if self . right is None :
10 self . right = . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11 self . right . parent =
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12 else :
13 self . right . insert ( valeur )
T. Rahobisoa 4/5 SD07 - Les ABR
Terminale - Spécialité NSI IFS Singapour
Exercice 3 :Rajouter la méthodeinsert() de l'exercice précédent à la classeNoeud, puis tester le programme
suivant :
1 bst = Noeud (6)
2 bst . insert (8)
3 bst . insert (3)
4 bst . insert (1)
5 bst . insert (4)
6 bst . insert (9)
7 bst . insert (2)
8 bst . insert (7)
9 bst . insert (5)
10 g r a p h i c a r b r e ( bst )
Exercice 4 :Écrire une fonctioninsertion(arbre,val) qui réalise le même travail mais sans que ce soit une
méthode de classe.
1. Récupérer les méthodes des différents parcours (préfixe, infixe et suffixe).
2. Les faire fonctionner sur notre arbre.
3. Lequel d'entre eux affiche la liste triée?
Exercice 5 : Maximum
Écrire un programme qui utilise une structure d'ABR pour trouver le maximum d'une liste d'entier.
Exercice 6 : Minimum
Écrire un programme qui utilise une structure d'ABR pour trouver le minimum d'une liste d'entier.
Exercice 7 : Tri de liste
Écrire un programme qui utilise une structure d'ABR pour trier par ordre croissant une liste d'entier.
Exercice 8 : Recherche animal
Écrire un programme qui utilise une structure d'ABR pour rechercher une valeur dans la liste suivante :
L = ['chat','chien','souris','araignée','crapaud','grenouille','lézard','zèbre']
Un tel algorithme est de complexité logarithmique.
Exercice 9 : Chemin
Écrire un programme qui utilise une structure d'ABR pour afficher le chemin depuis la racine jusqu'à un noeud
donné.
Exercice 10 : Sujet de BAC
Faire l'exercice 1 du sujet de Bac 2021 suivant.
Exercice 11 : Sujet de BAC (bis)
Faire l'exercice 3 du sujet de Bac 2023 suivant.
T. Rahobisoa 5/5 SD07 - Les ABR

## Les graphes

### Les graphes

Terminale - Spécialité NSI IFS Singapour
Chapitre 20 - Les graphes
Objectifs :
▷ Modéliser des situations sous forme de graphes.
▷ Écrire les implémentations d'un graphe : matrice d'adjacence, liste de successeurs/prédécesseurs.
▷ Passer d'une représentation à une autre.
1 Introduction
Le concept de graphe permet de résoudre de nombreux problèmes en mathématiques comme en informatique.
C'est un outil de représentation très courant, et nous l'avons déjà rencontré à plusieurs reprises, en particulier
lors de l'étude de réseaux tels que :
— les réseaux informatiques,
— les réseaux sociaux,
— les réseaux de transport
Une multitude de problèmes concrets d'origines très diverses peuvent donner lieu à des modélisations par des
graphes : c'est donc une structure essentielle en sciences, qui requiert un formalisme mathématique particulier
que nous allons découvrir.
T. Rahobisoa 1/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
L'étude de la théorie des graphes est un champ très vaste des mathématiques : nous allons surtout nous intéresser
à l'implémentation en Python d'un graphe et à différents problèmes algorithmiques qui se posent dans les
graphes.
2 Notion de graphe
Imaginez un réseau social ayant 6 abonnés (A, B, C, D, E et F) où :
— A est ami avec B, C et D
— B est ami avec A et D
— C est ami avec A, E et D
— D est ami avec tous les autres abonnés
— E est ami avec C, D et F
— F est ami avec E et D
On peut représenter ce réseau social par un schéma où :
— chaque abonné est représenté par un cercle avec son nom.
— chaque relation"X est ami avec Y"par un segment de droite reliant X et Y
— "X est ami avec Y"et "Y est ami avec X"sont représentés par le même segment de droite.
Voici ce que cela donne avec le réseau social décrit ci-dessus :
B D
A
F
C E
Ce genre de figure s'appelle ungraphe.
Les cercles sont appelés dessommets ou parfoisnoeuds (vertex ou nodes en anglais) et les segments de droites
des arêtes ou parfois arcs (edges en anglais).
Comme vu précédemment, les graphes sont des objets mathématiques très utilisés, notamment en informatique
(schématisation des rues d'une ville, de cartes GPS ou de réseaux informatiques).
On peut utiliser des outils en ligne pour dessiner des graphes.
Exemple : https://csacademy.com/app/graph_editor
T. Rahobisoa 2/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
3 Définitions et terminologie
A retenir!
Onappellegrapheladonnéed'unensembledepointsappeléssommetsetd'unensembledelignesappelées
arêtes qui relient certains sommets entre eux.
▷ Le nombre de sommets d'un graphe s'appelle l'ordre du graphe .
▷ Deux sommets reliés entre eux par une arête sont ditsadjacents.
▷ Le degré d'un sommet est le nombre d'arêtes issues de ce sommet.
▷ Un sommet qui n'est adjacent à aucun autre sommet du graphe est ditisolé.
▷ Un graphe est dit complet si deux sommets quelconques distincts sont toujours adjacents. Autrement
dit, tous les sommets sont reliés deux à deux par une arête.
4 Exemples de graphes
Le graphe ci-contre est d'ordre 5 car il possède 5 sommets.
Les sommets A et B sont adjacents.
Les sommets D et E ne sont pas adjacents.
Le sommet C est isolé.
Le graphe ci-contre est complet d'ordre 3.
Le graphe ci-contre est complet d'ordre 4.
Exercice 1 : Application
1. Donner le degré des sommets du graphe sur le réseau social de l'introduction.
2. Donner son ordre.
3. Ce graphe est-il complet?
T. Rahobisoa 3/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
5 Différents types de graphes
Un graphe peut êtreorienté ou non-orienté.
Dans ungraphe non-orienté, chaque arête peut être parcourue dans les deux sens.
Dans un graphe orienté, chaque arête ne peut être parcourue que dans un seul sens indiqué par une flèche.
Un graphe (orienté ou non-orienté) peut contenir desboucles c'est-à-dire une arête dont l'origine et l'extrémité
correspondent au même sommet (on a par exemple une boucle B sur la représentation précédente).
Un graphe peut aussi êtrepondéré (ou valué) si on attribue à chaque arête une valeur numérique (la plupart
du temps positive), qu'on appelle mesure, poids, coût ou valuation.
Par exemple :
— dans le protocole OSPF, on pondère les liaisons entre routeurs par le coût;
— dans un réseau routier entre plusieurs villes, on pondère par les distances.
6 Propriétés de la somme des degrés
Propriété n°1
Le nombre d'arêtes est égal à la moitié de la somme des degrés des sommets.
Ce résultat s'explique assez facilement : en ajoutant les degrés de chaque sommet (c'est-à-dire le nombre d'arêtes
issues de ce sommet), on comptabilise deux fois chaque arête (une fois avec le sommet d'une extrémité et une
seconde fois avec le sommet de l'autre extrémité de l'arête).
On déduit donc de cette propriété que :
T. Rahobisoa 4/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
Propriété n°2
La somme des degrés des sommets est nécessairement paire et donc le nombre de sommets de degré
impair est pair.
Exercice 2 : Application
Vérifier ces deux propriétés sur le graphe du réseau social ci-dessous.
7 Matrice d'adjacence
On peut représenter un graphe par une matrice.
Considérons un graphe d'ordren (n ∈ N∗). On numérote ces sommets de 1 àn.
Définition
On appelle matrice d'adjacence associée à ce graphe la matrice A dont le termeaij vaut 1 si les
sommets sont reliés par une arête et 0 sinon.
En numérotant les sommets de ce graphe par ordre alphabétique, la matrice d'adjacence s'écrit donc comme
suit :


0 1 1 0 1
1 0 1 1 0
1 1 0 1 0
0 1 1 0 0
1 0 0 0 0


Propriété
Dans le cas d'un graphe non orienté, les coefficientsaij et aji sont égaux pour touti et j compris entre
1 etn.
Autrement dit, la matrice d'adjacence estsymétrique.
Dans le cas d'un graphe orienté, la matrice d'adjacence n'est pas a priori symétrique.
T. Rahobisoa 5/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
Exercice 3 : Application
1. Compléter la matrice d'adjacence ci-dessous à partir du réseau social de l'introduction.




2. Dessiner le graphe à partir de la matrice d'adjacence ci-dessous.
8 Chaîne et cycle
Considérons un graphe quelconque (orienté ou non orienté).
Vocabulaire
▷ On appellechaînetoute succession d'arêtes dont l'extrémité de l'une (sauf la dernière) est l'origine
de la suivante.
▷ Le nombre d'arêtes qui composent une chaîne est appelélongueur de la chaîne .
▷ On appelle chaîne fermée toute chaîne dont l'origine et l'extrémité coïncident.
▷ On appelle cycle toute chaîne fermée dont les arêtes sonttoutes distinctes.
Exemples :
Dans le graphe ci-contre :
E-A-C-B est une chaîne de longueur 3.
E-A-C-B-A-E est une chaîne fermée de longueur 5. Ce n'est pas un cycle
car l'arête A-E est parcourue deux fois.
D-B-A-C-D est un cycle de longueur 4.
Comment dénombrer le nombre de chaînes de longueur k ?
Considérons un graphe d'ordren (où n ∈ N∗). On numérote ses sommets de 1 àn.
En prenant l'exemple du graphe ci-dessus, on numérote les sommets de ce graphe par ordre alphabétique, sa
matrice d'adjacence s'écrit :


0 1 1 0 1
1 0 1 1 0
1 1 0 1 0
0 1 1 0 0
1 0 0 0 0


T. Rahobisoa 6/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
Matrice de chaînes de longueur k
Le terme aij de la matrice Ak (où k ∈ N∗) est égal au nombre de chaînes de longueurk reliant les
sommets i et j dans ce graphe.
Et on obtient :
A3 =


2 6 6 2 3
6 4 5 5 1
6 5 4 5 1
2 5 5 2 2
3 1 1 2 0


Il existe donc 5 chaînes de longueur 3 reliant le sommet B au sommet C car :a23 = a32 = 5
Exercice 4 : Application
1. Donner la matriceA3 pour le graphe du réseau social de l'introduction.
2. En déduire le nombre de chaînes de longueur 3 reliant A et F.pour le graphe du réseau social de l'intro-
duction.
9 Notion de connexité
Définition
Un graphe est ditconnexe si deux de ses sommets quelconques sont toujours reliés par une chaîne.
Le graphe ci-contre est connexe.
Le graphe ci-contre n'est pas connexe.
Définition
Un graphe estcomplet lorsque chacun de ses sommets est relié à tous les autres.
Un graphe complet est donc nécessairement connexe mais la réciproque est fausse comme le montre l'exemple
ci-dessus.
Exercice 5 : Application
Pour le graphe du réseau social de l'introduction, que peut-on dire de sa connexité?
T. Rahobisoa 7/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
10 Chaînes et cycles eulériens
Définition
On appelle chaîne eulérienne d'un graphe toute chaîne qui contient une fois et une seule toutes les
arêtes du graphe.
La chaîne M-P-Q-O-M-N-P-O-N est une chaîne eulérienne.
En effet, cette chaîne contient 8 arêtes toutes distinctes.
Exercice 6 : Application
Pour le graphe du réseau social de l'introduction, indiquer une chaîne eulérienne (si c'est possible).
Définition
On appelle cycle eulérien une chaîne eulérienne fermée.
Le cycle R-U-S-V-T-R est un cycle eulérien.
Exercice 7 : Application
Pour le graphe du réseau social de l'introduction, indiquer un cycle eulérien (si c'est possible).
Théorème d'Euler
Soit G un graphe connexe.
G admet uncycle eulérien si et seulement si tous les sommets de G sont de degré pair.
G admet unechaîne eulérienne (non fermée) si et seulement si le nombre de sommets de degré impair
dans G est 2.
Si tel est le cas, les extrémités de la chaîne eulérienne sont les deux sommets de degré impair.
Pour en savoir plus :
Il existe ainsi de nombreuses énigmes basées sur la théorie des graphes.
Par exemple, comment faire pour dessiner ces deux figures sans lever le crayon?
T. Rahobisoa 8/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
Il existe aussi le problème classique du dessin de l'enveloppe ou de la maison, parfois appelémaison de Saint-
Nicolas (de l'allemand« Haus vom Nikolaus »), est un jeu mathématique qui consiste à dessiner une enveloppe
(ou une maison) constituée de 8 segments sans lever le crayon ni repasser sur un trait déjà dessiné.
Visualiser la vidéo suivante pour comprendre lesparcours en largeur et en profondeur des graphes.
11 Exercices
Exercice 8 : Réseau social
Soit un ensemble d'amis connectés sur un réseau social quelconque. Voici les interactions qu'on a recensées :
— André est ami avec Béa, Charles, Estelle et Fabrice,
— Béa est amie avec André, Charles, Denise et Héloïse,
— Charles est ami avec André, Béa, Denise, Estelle, Fabrice et Gilbert,
— Denise est amie avec Béa, Charles et Estelle,
— Estelle est amie avec André, Charles et Denise,
— Fabrice est ami avec André, Charles et Gilbert,
— Gilbert est ami avec Charles et Fabrice,
— Héloïse est amie avec Béa.
1. Représenter le graphe des relations dans ce réseau social (on désignera chaque individu par l'initiale de
son prénom). Faire en sorte que les arêtes ne se croisent pas!
2. Donner la matrice d'adjacence de ce graphe.
Exercice 9 : Matrices d'adjacence => Graphes
Construire les graphes correspondants aux matrices d'adjacence suivantes :
1.
M1 =


0 1 1 1 1
1 0 1 0 0
1 1 0 1 0
1 0 1 0 1
1 0 0 1 0


2.
M2 =


0 1 1 0 1
0 0 1 0 0
0 0 0 1 0
1 0 0 0 1
0 0 0 0 0


3. Attention, ici il s'agit d'un graphe pondéré. Les nombres se trouvant enaij indiquent les poids des liaisons
(arêtes ou arcs) entre les sommets d'indicei et j.
T. Rahobisoa 9/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
M3 =


0 5 10 50 12
5 0 10 0 0
10 10 0 8 0
1 0 0 0 100
12 0 0 100 0


Exercice 10 : Listes d'adjacence
On associe à chaque sommet sa liste des voisins (c'est-à-dire les sommets adjacents). On utilise pour cela un
dictionnaire dont les clés sont les sommets et les valeurs les listes des voisins.
Dans le cas d'un graphe orienté on associe à chaque sommet la liste des successeurs (ou bien des prédécesseurs,
au choix).
Construire les graphes correspondants aux listes d'adjacence suivantes.
1. Dictionnaire 1 :
1 G1 = {
2 'A ' :[ 'B ' , 'C '] ,
3 'B ' :[ 'A ' , 'C ' , 'E ' , 'F '] ,
4 'C ' :[ 'A ' , 'B ' , 'D '] ,
5 'D ' :[ 'C ' , 'E '] ,
6 'E ' :[ 'B ' , 'D ' , 'F '] ,
7 'F ' :[ 'B ' , 'E ']
8 }
2. Dictionnaire 2 :
1 G2 = {
2 'A ' :[ 'B '] ,
3 'B ' :[ 'C ' , 'E '] ,
4 'C ' :[ 'B ' , 'D '] ,
5 'D ' :[] ,
6 'E ' :[ 'A ']
7 }
Exercice 11 : Graphe d'un réseau électrique
Un de vos amis travaille pour un distributeur d'électricité.
Il doit proposer à son supérieur une représentation du réseau reliant différentes villes. Comme il n'y arrive pas
trop, il voudrait que vous la lui fassiez.
Pour simplifier le problème, il a déjà renommé les villes en A, B, C, D, E et F. De plus, il vous donne les
informations suivantes :
— la ville A est reliée par un réseau électrique aux villes B, E et F,
— la ville B est reliée par un réseau électrique aux villes A, C et D,
— la ville C est reliée par un réseau électrique aux villes B, D, E et F,
— la ville D est reliée par un réseau électrique aux villes B, C et F,
— la ville E est reliée par un réseau électrique aux villes A, C et F,
— la ville F est relié par un réseau électrique aux villes A, C, D et E.
1. Proposer un graphe qui modélise la situation.
2. Ce graphe est-il complet? Pourquoi?
T. Rahobisoa 10/11 SD08 - Les graphes
Terminale - Spécialité NSI IFS Singapour
Exercice 12 : Représentation d'un graphe non orienté
Voici un ensemble des relations :
— A est ami avec tout le monde sauf G,
— B est ami avec A, D et H,
— C est ami avec A, F, G et H,
— D est ami avec A, B et H,
— E est ami avec A et H,
— F est ami avec A et C,
— G est ami avec C et H,
— H est ami avec A, B, C, D, E et G.
1. Représenter ce graphe et vérifier qu'il est non orienté.
2. Implémenter ce graphe sous la forme d'un dictionnaire de liste dans lequel chaque clé représente le nœud
étudié et les sommets adjacents sont représentés sous la forme d'une liste.
3. Écrire la matrice d'adjacence et vérifier qu'elle est symétrique (on utilisera l'ordre alphabétique pour
indexer les nœuds).
4. Implémenter la matrice en Python sous la forme d'une liste de listes.
T. Rahobisoa 11/11 SD08 - Les graphes
