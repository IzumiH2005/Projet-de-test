# Programmation

## Programmation Orientee Objet

### 1. Prise en main de Pygame

```python linenums='1'
import pygame, sys
import time
from pygame.locals import *

LARGEUR = 640
HAUTEUR = 480
RAYON = 20

pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
fenetre.fill([0,0,0])

x = 300
y = 200
dx = 4
dy = -3
couleur = (45, 170, 250)

while True:
    fenetre.fill([0, 0, 0])
    pygame.draw.circle(fenetre, couleur, (x, y), RAYON)

    x += dx
    y += dy

    pygame.display.update()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    time.sleep(0.1)

```

### 1.1  Rajout d'un rebond sur les parois

Modifiez le code précédent afin que la balle rebondisse sur chaque paroi (il suffit de modifier intelligemment les variables de vitesse ```dx``` et ```dy```).

### 1.3 Gestion de la collision entre les deux balles

**Q1.** À l'aide d'un schéma (papier-crayon !), mettez en évidence le test devant être réalisé pour détecter une collision.

    
    

**Q2.** Implémentez ce test (en créant pour cela une fonction ```distance``` )  et affichez "collision" en console lorsque les deux balles se touchent.

**Q3.** Pour donner l'illusion physique du rebond, échangez les valeurs respectives de ```dx``` et ```dy``` pour les deux balles.

### 2.1 la classe Balle

L'objectif est que la méthode constructeur dote chaque nouvelle balle de valeurs aléatoires : abscisse, ordonnée, vitesse, couleur...  

- Pour l'aléatoire, on pourra utiliser ```randint(a, b)``` qui renvoie un nombre pseudo-aléatoire entre ```a``` et ```b```.
Il faut pour cela importer la fonction, par ```from random import randint``` 

- Vous pouvez aussi doter votre classe ```Balle``` d'une méthode ```dessine``` (qui affiche la balle), ainsi qu'une méthode ```bouge``` qui la fait bouger. 

Créez cette classe et instanciez une balle.

### 2.3 Collision de toutes les balles

Il «suffit» , dans la méthode constructeur, de tester la collision de la balle ```self``` avec chacune des balles de notre ```sac_a_balles```.

### 3. Extensions

- Vous pouvez créer des balles de couleurs identiques, sauf une. Cette balle diffusera sa couleur à toutes les balles avec qui elle rentrera en collision.
- En la supprimant de la liste ```sac_a_balles```, vous pouvez faire disparaitre une balle.
- Vous pouvez créer une balle que vous déplacerez au clavier (voir ici pour la gestion des déplacements)
- ...
- Ce que je ne veux pas voir :

### 4. Organisation du projet

- 16/09/2026 : démarrage du projet et constitution des groupes
    - 03/11/2026 : remise du projet sur Capytale

    Cliquez ici.
    Servez-vous de cette feuille de projet pour y déposer les différentes versions de votre travail.
    Je pourrai ainsi le consulter au fur et à mesure de votre progression.

    - sur 10 points : note globale du projet.
    - sur 10 points : entretien individuel autour du code du projet. 

    - groupe A : Nathan - Elowan
    - groupe B : Amir -  Ethan
    - groupe C : Melissa - Sebastien - Emile
    - groupe D : Marko - Théo
    - groupe E : Youssef - Wanis - Lucas
    - groupe F : Joseph - Yohan - Solal
    - groupe G : Adam - Ayman
    - groupe H : Fidan - Hamza

### 0. Introduction

La POO est un **paradigme** de programmation, au même titre que la programmation impérative (que nous pratiquons déjà) ou la programmation fonctionnelle (qui sera évoquée cette année en Terminale), ou encore d'autres paradigmes (la liste est longue).  
Un paradigme de programmation pourrait se définir comme une _philosophie_ dans la manière de programmer : c'est un parti-pris revendiqué dans la manière d'aborder le problème à résoudre. Une fois cette décision prise, des outils spécifiques au paradigme choisi sont utilisés. 

    Imaginons 3 menuisiers qui ont pour mission de fabriquer chacun un meuble. 

    - Le premier pourra décider d'utiliser du collé-pointé : il assemblera les morceaux de bois en les collant puis utilisera des pointes. Ses outils seront le marteau et le pistolet à colle.
    - Le deuxième pourra décider de visser les morceaux de bois entre eux : son outil principal sera une visseuse.
    - Le troisième pourra décider de faire de l'assemblage par tenons et mortaises : son outil principal sera une défonceuse.

    Pour la réalisation de sa mission, chaque menuisier utilise un paradigme différent. 
    Qui utilise la meilleure méthode ? Cette question n'a pas vraiment de réponse : certaines méthodes sont plus rapides que d'autres, d'autres plus robustes, d'autres plus esthétiques...  
    Et pourquoi ne pas mélanger les paradigmes ? Rien n'interdit d'utiliser des pointes ET des vis dans la fabrication d'un meuble. 

La Programmation Orientée Objet sera (surtout à notre niveau) mélangée avec de la programmation impérative, de la programmation fonctionnelle... d'ailleurs vous avez déjà manipulé des objets sans le savoir :

### 1. Des objets déjà autour de nous

```python
>>> m = [4,5,2]
>>> type(m)
list
```

```m``` est une liste, ou plus précisément un **objet** de type ```list```. Et en tant qu'objet de type ```list```, il est possible de lui appliquer certaines fonctions prédéfinies (qu'on appelera **méthodes**) :

```python
>>> m.reverse()
```

La syntaxe utilisée (le . après le nom de l'objet) est spécifique à la POO. Chaque fois que vous voyez cela, c'est que vous êtes en train de manipuler des objets.  
Mais qu'a donc fait cette méthode ```reverse()``` ?   

```python
>>> m
[2, 5, 4]
```

Nous ne sommes pas surpris par ce résultat car la personne qui a programmé la méthode ```reverse()``` lui a donné un nom explicite.  
Comment a-t-elle programmé cette inversion des valeurs de la liste ? Nous n'en savons rien et cela ne nous intéresse pas. Nous sommes juste **utilisateurs** de cette méthode. 
L'objet de type ```list``` nous a été livré avec sa méthode ```reverse()``` (et bien d'autres choses) et nous n'avons pas à démonter la boîte pour en observer les engrenages : on parle de principe d'**encapsulation**.

On peut obtenir la liste de toutes les fonctions disponibles pour un objet de type ```list```, par la fonction ```dir``` :

```python
>>> dir(m)
['__add__',
'__class__',
'__contains__',
'__delattr__',
...
'clear',
'copy',
'count',
'extend',
'index',
'insert',
'pop',
'remove',
'reverse',
'sort']
```

Les méthodes encadrées par un double underscore __ sont des méthodes **privées**, a priori non destinées à l'utilisateur. Les méthodes **publiques**, utilisables pour chaque objet de type ```list```, sont donc ```append```, ```clear```, ...  

Comment savoir ce que font les méthodes ? Si elles ont été correctement codées (et elles l'ont été), elles possèdent une _docstring_, accessible par :

```python
>>> help(m.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> help(m.reverse)__doc__
Help on built-in function reverse:

reverse() method of builtins.list instance
    Reverse *IN PLACE*.
```

### 2.1 Vocabulaire : classe,  objet, instance de classe

Jusqu'ici nous avons employé uniquement le mot «objet». Il convient maintenant d'être plus précis.  

- On désignera par **classe** la structure de données définissant une catégorie générique d'objets. Dans le monde animal, _chat_ est une classe (nommée en réalité _félidé_ ). 
- Chaque élement de la classe _chat_ va se distinguer par des caractéristiques : un âge, une couleur de pelage, un surnom... (on appelera ces caractéristiques des **attributs**) et des fonctionnalités, comme la **méthode** ```attrape_souris```.  
- Lorsqu'on désigne un chat en particulier, on désigne alors un **objet** (bien réel) qui est une **instance** de la **classe** (abstraite) _chat_. 

Par exemple, 
l'**objet** Larry est une **instance** de la **classe** _chat_ . 

D'après Wikipedia, 

```python
larry.pelage = "blanc et tabby"
larry.surnom = "Chief Mouser to the Cabinet Office"
```

Toujours d'après Wikipedia, la méthode ```larry.attrape_souris``` est plutôt efficace.

### 2.2 Création d'une classe

#### 2.2.1 (mauvaise) manière minimale
Créons une classe «voiture». Il suffit d'écrire :

```python
class Voiture :
    pass   #pass, car pour l'instant il n'y a rien dans la déclaration de la classe (et c'est mal)
```

La classe ```Voiture``` est créée.  
Notez que par convention, le nom d'une classe commence toujours par une majuscule.  
Pour créer une instance de cette classe, on écrit :

```python
>>> titine = Voiture()
```

```titine``` est un objet, instance de la classe ```Voiture```.

```python
>>> type(titine)
__main__.Voiture
```

On peut alors donner des attributs à cette instance :

```python
>>> titine.annee = 2018
>>> titine.couleur = "verte"
>>> titine.vitesse_max = 162
```

Mais arrêtons-là cette mauvaise méthode. Si on désire créer une classe «voiture», c'est pour créer un concept générique de voiture et d'en spécifier des caractéristiques communes  : l'année, la couleur, la vitesse maximale... 

L'idée est donc qu'à la création (on dira plutôt à la **construction**) de chaque objet voiture, on va lui spécifier directement ses attributs :

#### 2.2.2 :heart: (bonne) manière : la méthode constructeur :heart:

La **méthode constructeur**, toujours appelée ```__init__()```, est une méthode (une «def») qui sera automatiquement appelée à la création de l'objet. Elle va donc le doter de tous les attributs de sa classe.

```python linenums="1"
class Voiture :
    def __init__(self, annee, coul, vmax) :
        self.annee = annee
        self.couleur = coul
        self.vitesse_max = vmax
        self.age = 2025 - self.annee
```

- le mot-clé ```self```, omniprésent en POO (d'autres langages utilisent ```this```), **fait référence à l'objet lui-même**, qui est en train d'être construit.
- pour construire l'objet, 3 paramètres seront nécessaires : ```annee```, ```coul``` et ```vmax```. Ils donneront respectivement leur valeur aux attributs ```annee```, ```couleur``` et ```vitesse_max```.
- dans cet exemple, les noms ```coul``` et ```vmax``` ont été utilisés pour abréger ```couleur``` et ```vitesse_max```, mais il est recommandé de garder les mêmes noms, même si ce n'est pas du tout obligatoire.

Construisons donc notre première voiture !

```python
>>> mon_bolide = Voiture(2012, "rouge", 190)
```

```python
>>> type(mon_bolide)
__main__.Voiture
```

```mon_bolide``` possède 4 attributs : 

- ```annee```, ```couleur``` et ```vitesse_max``` ont été donnés par l'utilisateur lors de la création.
- ```age``` s'est créé «tout seul» par l'instruction ```self.age = 2025 - self.annee```.

```python
>>> mon_bolide.annee
2012
>>> mon_bolide.couleur
'rouge'
>>> mon_bolide.vitesse_max
190
>>> mon_bolide.age
13
```

Observons les différentes étapes grâce à PythonTutor :
 

Bien sûr, on peut créer une autre voiture en suivant le même principe :

```python
>>> batmobile = Voiture(2036, "noire", 325)
>>> batmobile.couleur
'noire'
```

 
    Créer une classe ```Point``` permettant de créer un objet ```A``` , dont on récupèrera l'abscisse par la variable ```A.x``` et l'ordonnée par ```A.y```.

        ```python
        >>> A = Point(3, 5)
        >>> A.x
        3
        >>> A.y
        5
        ```

    

        

        

#### 2.2.4 Créer une méthode pour notre objet

```python linenums="1"
class Voiture :
    def __init__(self, annee, coul, vmax) :
        self.annee = annee
        self.couleur = coul
        self.vitesse_max = vmax
        self.age = 2025 - self.annee
    
    def petite_annonce(self) :
        print("À vendre voiture", self.couleur, "de", self.annee,\
             ", vitesse maximale", self.vitesse_max, "km/h.")
```

Remarque : le symbole ```\``` est utilisé ici pour couper une ligne trop longue.

```python
>>> batmobile = Voiture(2036, "noire", 325)
>>> batmobile.petite_annonce()
À vendre voiture noire de 2036 , vitesse maximale 325 km/h.
```

Nous aurions pu (ou dû) en profiter pour écrire une docstring pour notre méthode ```petite_annonce()``` :

```python
class Voiture :
    def __init__(self, annee, coul, vmax) :
        self.annee = annee
        self.couleur = coul
        self.vitesse_max = vmax
        self.age = 2025 - self.annee
    
    def petite_annonce(self) :
        """ Rédige automatiquement une petite annonce concernant le véhicule"""
        print("À vendre voiture", self.couleur, "de", self.annee,\
             ", vitesse maximale", self.vitesse_max, "km/h.")
```

```python
>>> batmobile = Voiture(2036, "noire", 325)
>>> help(batmobile.petite_annonce)
Help on method petite_annonce in module __main__:

petite_annonce() method of __main__.Voiture instance
    Rédige automatiquement une petite annonce concernant le véhicule
```

Que donne la commande ```dir``` pour notre objet ?

```python
dir(batmobile)
```

    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'age',
     'annee',
     'couleur',
     'petite_annonce',
     'vitesse_max']

On y retrouve donc à la fois les 4 attributs et l'unique méthode que nous avons créés pour notre objet.

    Reprendre la classe de l'exercice précédent et rajouter une méthode ```distance()``` qui renvoie la distance du point par rapport à l'origine du repère (dans un repère orthonormé).

        ```python
        >>> A = Point(3, 5)
        >>> A.distance()
        5.830951894845301
        ```

### 3. Compléments

#### 3.1 Hors-Programme : la méthode ```__repr__()``` 
La méthode ```__repr__()``` (les doubles underscores traduisent le fait que la méthode est *privée*) peut redéfinir la manière dont l'objet doit s'afficher lors qu'on le passe en paramètre à la fonction ```print()```, ou simplement lorsqu'on demande sa valeur en console.

Observons comment s'affiche un objet de type ```Fraction``` lorsque rien n'a été spécifié sur son affichage.

```python linenums='1'
class Fraction:
    def __init__(self, num, den):
        self.numerateur = num
        self.denominateur = den
        
```

```python
>>> a = Fraction(3,4)
>>> print(a)
 
```

C'est un peu décevant. Rajoutons donc une méthode ```__repr__()``` .

```python linenums='1'
class Fraction:
    def __init__(self, num, den):
        self.numerateur = num
        self.denominateur = den
    
    def __repr__(self):
        return str(self.numerateur) + "/" + str(self.denominateur)
```

```python
>>> a = Fraction(3, 4)
>>> print(a)
  3/4
>>> a
  3/4
```
Ce qui est nettement plus agréable !

    Modifier la méthode ```__repr__``` afin de n'afficher que le numérateur dans le cas où le dénominateur vaut 1.
    
    

#### 3.2 L'encapsulation poussée à bout : les ```getters``` et les ```setters```

Imaginons la classe suivante :

```python linenums='1'
class Joueur :
    def __init__(self, nom, club, age):
        self.nom = nom
        self.club = club
        self.age = age
```

Instancions le joueur Nans Ducuing
```python
>>> nducuing = Joueur("Nans DUCUING", "UBB", 34)
```

notre cobaye

##### 3.2.1 Les ```setters``` 

Supposons maintenant que ce joueur change de club, pour aller de l'UBB à Perpignan.

Il serait naturel de faire ceci :
```python
>>> nducuing.club = "Perpignan"
```

Cela marche bien, mais... C'est contraire à l'esprit de la Programmation Orientée Objet. Ce paradigme milite pour une encapsulation des objets, qui interdisent le plus possible l'accès direct à leurs attributs. 

Comment faire alors ? En proposant une méthode dont l'unique travail est d'aller effectuer une modification sur l'attribut :

```python linenums='1'
class Joueur :
    def __init__(self, nom, club, age):
        self.nom = nom
        self.club = club
        self.age = age
    
    def mutation(self, nouveau_club):
        self.club = nouveau_club
```

Le changement de club se fera maintenant par l'appel :
```python
>>> nducuing.mutation("Perpignan")
```

Ce type de méthode s'appelle un ```setter```. 

##### 3.2.2 Les ```getters``` 

Nous avons vu qu'aller modifier directement un attribut était défendu... mais peut-on simplement aller le *consulter* ?

Là encore, le concept d'encapsulation -poussé à l'extrême- peut nous l'interdire. 

Mais si 
```nducuing.club``` est interdit, comment savoir dans quel club joue notre joueur préféré ?

Une fois de plus, en construisant une méthode qui va nous renvoyer l'état actuel de son attribut ```club``` :

```python
class Joueur :
    def __init__(self, nom, club, age):
        self.nom = nom
        self.club = club
        self.age = age
    
    def mutation(self, nouveau_club):
        self.club = nouveau_club
        
    def get_club(self):
        return self.club
```

L'accès à l'attribut ```club``` de notre instance se fera donc maintenant par :

```python
>>> nducuing.get_club()
```

Ce type de méthode s'appelle un ```getter```. 

---

    - Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.

{#
DS01
#}

### Exercices

**Q1.** Écrire une classe ```Eleve``` qui contiendra les attributs ```nom```, ```classe``` et ```note```.
    

    **Q2.** Instancier trois élèves de cette classe.
    

    **Q3.**  Écrire une fonction ```compare``` qui prend en paramètres deux élèves ```eleve1``` et ```eleve2``` qui renvoie le nom de l'élève ayant la meilleure note (on ne traitera pas à part le cas d'égalité).

        ```python
        >>> riri = Eleve("Henri", "TG2", 12)
        >>> fifi = Eleve("Philippe", "TG6", 15)
        >>> loulou = Eleve("Louis", "TG1", 8)
        >>> compare(riri, fifi)
        'Philippe'
        ```

    
    Écrire une classe ```TriangleRect``` qui contiendra les attributs ```cote1```, ```cote2``` et ```hypotenuse```.

    La méthode constructeur ne prendra en paramètres que ```cote1``` et ```cote2```, l'attribut ```hypotenuse``` se calculera automatiquement.

        ```python
        >>> mon_triangle = TriangleRect(3,4)
        >>> mon_triangle.cote1
        3
        >>> mon_triangle.cote2
        4
        >>> mon_triangle.hypotenuse
        5.0
        ```

    **Q1.** Écrire une classe ```Chrono``` qui contiendra les attributs ```heures```, ```minutes``` et ```secondes```.
    

    **Q2.** Doter la classe d'une méthode ```affiche``` qui affichera le temps ```t```.
    {{
    correction(True,
    """
\"Correction\" 
        ```python
        class Chrono:
            def __init__(self, h, m, s):
                self.heures = h
                self.minutes = m
                self.secondes = s   

            def affiche(self):
                print('Il est {} heures, {} minutes et {} secondes'.format(self.heures, self.minutes, self.secondes))   
        ```
    """
    )
    }}    

    **Q3.** Doter la classe d'une méthode ```avance``` qui prend en paramètre un temps ```s``` en secondes et qui fait avancer le temps ```t``` de ```s``` secondes.

    {{
    correction(True,
    """
\"Correction\" 
        ```python
        class Chrono:
            def __init__(self, h, m, s):
                self.heures = h
                self.minutes = m
                self.secondes = s   

            def affiche(self):
                print('Il est {} heures, {} minutes et {} secondes'.format(self.heures, self.minutes, self.secondes))   

            def avance(self, s):
                self.secondes += s

                # il faut ajouter les minutes supplémentaires si les secondes
                # dépassent 60
                self.minutes += self.secondes // 60

                # il ne faut garder des secondes que ce qui n'a pas servi
                # à fabriquer des minutes supplémentaires
                self.secondes = self.secondes % 60

                # il faut ajouter les heures supplémentaires si les minutes
                # dépassent 60
                self.heures += self.minutes // 60

                # il ne faut garder des minutes que ce qui n'a pas servi
                # à fabriquer des heures supplémentaires
                self.minutes = self.minutes % 60
        ```
    """
    )
    }}  

        ```python
        >>> t = Chrono(17, 25, 38)
        >>> t.heures
        17
        >>> t.minutes
        25
        >>> t.secondes
        38
        >>> t.affiche()
        'Il est 17 heures, 25 minutes et 38 secondes'
        >>> t.avance(27)
        >>> t.affiche()
        'Il est 17 heures, 26 minutes et 5 secondes'
        ```

        On pourra utiliser les opérateurs :
        
        - ```%```, qui calcule le reste d'une division euclidienne.
        - ```//```, qui calcule le quotient d'une division euclidienne.

    Écrire une classe ```Player``` qui :

    - ne prendra aucun argument lors de son instanciation.
    - affectera à chaque objet créé un attribut ```energie``` valant 3 par défaut. 
    - affectera à chaque objet créé un attribut ```alive``` valant ```True``` par défaut.
    - fournira à chaque objet une méthode ```blessure``` qui diminue l'attribut ```energie``` de 1.
    - fournira à chaque objet une méthode ```soin``` qui augmente l'attribut ```energie``` de 1.
    - si l'attribut ```energie``` passe à 0, l'attribut ```alive``` doit passer à ```False``` et ne doit plus pouvoir évoluer.

        ```python
        >>> mario = Player()
        >>> mario.energie
        3
        >>> mario.soin()
        >>> mario.energie
        4
        >>> mario.blessure()
        >>> mario.blessure()
        >>> mario.blessure()
        >>> mario.alive
        True
        >>> mario.blessure()
        >>> mario.alive
        False
        >>> mario.soin()
        >>> mario.alive
        False
        >>> mario.energie
        0
        ```

        
        Créer une classe ```CompteBancaire``` dont la méthode constructeur recevra en paramètres :

        - un attribut ```titulaire``` stockant le nom du propriétaire.
        - un attribut ```solde``` contenant le solde disponible sur le compte.  
        
        Cette classe contiendra deux méthodes ```retrait``` et ```depot``` qui permettront de retirer ou de déposer de l'argent sur le compte. 

            ```python
            >>> compteGL = CompteBancaire("G.Lassus", 1000)
            >>> compteGL.retrait(50)
            Vous avez retiré 50 euros
            Solde actuel du compte : 950 euros
            >>> compteGL.retrait(40000)
            Retrait impossible
            >>> compteGL.depot(10000000)
            Vous avez déposé 10000000 euros
            Solde actuel du compte : 10000950 euros
            ```
                
        {{
        correction(True,
        """
\"Correction\" 
            ```python linenums='1'
            class CompteBancaire:
                def __init__(self, titulaire, solde):
                    self.titulaire = titulaire
                    self.solde = solde
                    
                def retrait(self, somme):
                    if somme > self.solde:
                        print('Retrait impossible')
                    else :
                        self.solde -= somme
                        print('Vous avez retiré {} euros'.format(somme))
                        print('Solde actuel du compte : {} euros'.format(self.solde))

                def depot(self, somme):
                    self.solde += somme
                    print('Vous avez déposé {} euros'.format(somme))
                    print('Solde actuel du compte : {} euros'.format(self.solde))
            ```            
        """
        )
        }}

    Exercice 14.2 de la BNS 2024.

    Exercice 2 Partie A du sujet Métropole Septembre 2022

    Exercice 5 du sujet Métropole J1 2022

    Exercice 2 du sujet La Réunion J1 2022
ex3J1ME2024">"
    Exercice 3 (partie A et B) du sujet Métropole J1 2024   

    **Partie A**

    

    

      

    **Partie B**
ex1J2G12024">"
    Exercice 1 du sujet Centres Étrangers J2 2024   

    ```python linenums='1'
    class Chemin:

        def __init__(self, itineraire):
            self.itineraire = itineraire
            longueur, largeur = 0, 0
            for direction in self.itineraire:
                if direction == "D":
                    longueur = longueur + 1
                if direction == "B":
                    largeur = largeur +1
            self.longueur = longueur
            self.largeur = largeur
            self.grille = [['.' for i in range(longueur+1)] for j in range(largeur+1)]

        def remplir_grille(self):
            i, j = 0, 0 
            self.grille[0][0] = 'S' 
            for direction in ...:
                if direction == 'D':
                    ... = ... 
                elif direction == 'B':
                    ... = ... 
                self.grille[i][j] = '*' 
            self.grille[self.largeur][self.longueur] = 'E'

    ```

    Pour la question 6 :

    ```python linenums='1'
    from random import choice

    def itineraire_aleatoire(m, n):
        itineraire = ''
        i, j = 0, 0
        while i != m and j != n:
            ...
            ...
            ...
            ...
            ...
            ...
        if i == m:
            itineraire = itineraire + 'D'*(n-j)
        if j == n:
            itineraire = itineraire + 'B'*(m-i)
        return itineraire
    ```

    

    

    

    

    

    {{
    correction(True,
    """
\"Correction Q7 \" 
        Si la largeur de la grille est 1, il n'y a qu'un seul mouvement possible (```D```) donc il n'y a qu'un seul chemin. 
        
        Donc $\\forall n \\in \\mathbb{N}, N(1,n) = 1$
    """
    )
    }}
ex2J1AN2025">"
    Exercice 2 du sujet Amérique du Nord J1 2025   

    ```python
    class Colis:
        def __init__(self, id, poids, adresse):
            self.id = id
            self.poids = poids
            self.adresse = adresse
            self.etat = 'préparé'
    
    colisA = Colis('AC12', 5.0, '20 rue de la paix 57000 Metz')
    colisB = Colis('AF34', 10.25, '32 rue du centre 57000 Metz')
    ```

    

    ```python
    def ajouter_colis(liste, colis):
        # ajoute le colis à la fin de la liste
        liste.append(colis)
    ```

    

    

    ```python
    def poids_total(liste):
        total = ...
        for c in liste :
            total = ...
        return total
    ```

    

    

    ```python
    def tri_decroissant(liste):
        n = len(liste)
        for i in range(n - 1):
            min_pos = i
            for j in range(i + 1, n):
                if liste[j].poids > liste[min_pos].poids:
                    min_pos = j
            # Échanger les éléments
            temp = liste[i]
            liste[i] = liste[min_pos]
            liste[min_pos] = temp
        return liste
    ```

    

    

    ```python
    def chargement_glouton(liste, rang, capacite):
        if rang == len(liste):
            return ...
        elif liste[rang].poids "
    Exercice 3 du sujet Asie J1 2024   

    ```python
    class Personne():
        def __init__(self, num, n , p , a_naiss, a_entree):
            self.num_badge = num
            self.nom = n
            self.prenom = p
            self.annee_naissance = a_naiss
            self.annee_entree = a_entree
    ```

    

    

    

    ```python 
    class Personnel:
        def __init__(self):
            self.liste = []
    ```

    

    

    ```python
    def donne_nom(..., num):
        for elt in self.liste:
            if ... == num:
                return ...
        return ...
    ```
ex3J1ME2023">"
    Exercice 3 du sujet Métropole J1 2023

    ```python
    class Region:
        '''Modélise une région d'un pays sur une carte.'''
        def __init__(self, nom_region):
            '''
            initialise une région
            : param nom_region (str) le nom de la région
            '''
            self.nom = nom_region
            # tableau des régions voisines, vide au départ
            self.tab_voisines = []
            # tableau des couleurs disponibles pour colorier la région
            self.tab_couleurs_disponibles = ['rouge', 'vert', 'bleu', 'jaune', 'orange', 'marron']
            # couleur attribuée à la région et non encore choisie au départ
            self.couleur_attribuee = None

    ```
ex3J2AN2024">"
    Exercice 3 du sujet Amérique du Nord J2 2024 

        
        
    ```python
    class Transaction:
        def __init__(self, expediteur, destinataire, montant):
            self.expediteur = expediteur
            self.destinataire = destinataire
            self.montant = montant

    class Bloc:
        def __init__(self, liste_transactions, bloc_precedent):
            self.liste_transactions = liste_transactions
            self.bloc_precedent = bloc_precedent # de type Bloc

    class Blockchain:
        def __init__(self):
            self.tete = self.creer_bloc_0()

        def creer_bloc_0(self):
            '''
            Crée le premier bloc qui distribue 100 nsicoin à tous les
            utilisateurs (un pseudo-utilisateur Genesis est utilisé comme
            expéditeur)
            '''
            liste_transactions = [
            Transaction('Genesis', 'Alice', 100),
            Transaction('Genesis', 'Bob', 100),
            Transaction('Genesis', 'Charlie', 100)
            ]
            return Bloc(liste_transactions, None) 
    ```

    

    

    

    

    

    

    

    

    :warning: À la question 9, le code à utiliser est celui-ci (erreur d'énoncé à la ligne 6):
    ```python linenums='1'
    def calculer_solde(self, utilisateur):
        if self.bloc_precedent is None:
            solde = 0
        else:
            solde = ...
            for transaction in self.liste_transactions:
                if ... == utilisateur:
                    solde = solde - ...
                elif ...:
                    ...
            return solde    
    ```

    

    

    

    

    {{
    correction(True,
    """
\"Correction Q13 \" 
        Chaque bit peut prendre la valeur 0 ou 1, soit 2 possibilités. Le nombre de hashs possibles est donc $2^{256}$.
    """
    )
    }}
ex1J1G112025">"
    Exercice 1 du sujet Centre Étrangers J1 2025

    ```python linenums='1'
    class Balise:
        def __init__(self, numero, couleurs):
            self.num_balise = numero
            self.couleurs_balise = couleurs
            self.voisines = []
            self.visitee = False

        def methode1(self):
            return [b.num_balise for b in self.voisines]

        def methode2(self, couleur):
            self.couleurs_balise = [c for c in self.couleurs_balise if c != couleur]

        def methode3(self, couleur):
            self.couleurs_balise.append(couleur)

    balise1 = Balise(1, ['vert', 'rouge', 'noir'])
    balise2 = Balise(2, ['rouge'])
    balise3 = Balise(3, ['vert', 'noir'])
    balise4 = Balise(4, ['rouge', 'noir'])
    balise5 = Balise(5, ['noir'])
    balise6 = Balise(6, ['vert', 'rouge', 'noir'])
    balise7 = Balise(7, ['vert'])
    balise8 = Balise(8, ['rouge'])
    balise9 = Balise(9, ['rouge'])
    balise10 = Balise(10, ['vert', 'noir'])
    balise11 = Balise(11, ['rouge'])
    balise12 = ...

    balise1.voisines = [balise2, balise3]
    balise2.voisines = [balise1, balise4]
    balise3.voisines = [balise1, balise6]
    balise4.voisines = [balise2, balise5, balise6]
    balise5.voisines = [balise4, balise10]
    balise6.voisines = [balise3, balise4, balise7, balise11]
    balise7.voisines = [balise6, balise10]
    balise8.voisines = [balise9]
    ...
    balise10.voisines = [balise5, balise7, balise12]
    balise11.voisines = [balise6, balise9]
    balise12.voisines = [balise9, balise10]

    ```

    

    

    

    

    ```python
    def itineraire(balise_debut, balise_fin, couleur):
        assert couleur in balise_debut.couleurs_balise
        assert couleur in balise_fin.couleurs_balise
        balise = balise_debut
        chemin = [balise]
        while balise.num_balise != ...:
            for b in balise.voisines:
                if (couleur in ...) and (b not in ...):
                    balise = ...
                    chemin.append(balise)
        return [b.num_balise for b in chemin]
    ```

    

    

    

    ```python
    def mystere(balise):
        meilleure_balise = None
        mini = -1
        for b, t in balise.voisines:
            if (b.visitee == False) and (mini == -1 or t >> ma_bibli = Bibliotheque()
        >>> livre1 = Livre('Les Misérables', 'Victor Hugo', 3)
        >>> livre2 = Livre('Les fleurs du mal', 'Charles Baudelaire', 1)
        >>> ma_bibli.ajoute(livre1)
        >>> ma_bibli.ajoute(livre2)
        >>> livre1.description()
        Titre : Les Misérables
        Auteur : Victor Hugo
        Etat : 3
        >>> livre2.degrade()
        >>> livre2.description()
        Titre : Les fleurs du mal
        Auteur : Charles Baudelaire
        Etat : 0
        >>> ma_bibli.inventaire()
        -------------------------------
        contenu de ma bibliothèque :
        -------------------------------

        Titre : Les Misérables
        Auteur : Victor Hugo
        Etat : 3

        Titre : Les fleurs du mal
        Auteur : Charles Baudelaire
        Etat : 0

        >>> ma_bibli.supprime_livres_abimes()
        >>> ma_bibli.inventaire()
        -------------------------------
        contenu de ma bibliothèque :
        -------------------------------

        Titre : Les Misérables
        Auteur : Victor Hugo
        Etat : 3

        ```

        ### ▸ Question

        Proposer un code pour la classe `Livre` et la classe `Bibliotheque` répondant au cahier des charges.
'Correction'

        ```python linenums='1'
        class Livre():
            def __init__(self, titre, auteur, etat):
                self.titre = titre
                self.auteur = auteur
                self.etat = etat

            def degrade(self):
                if self.etat > 0:
                    self.etat -= 1

            def description(self):
                print('Titre :', self.titre)
                print('Auteur :',self.auteur)
                print('Etat :', self.etat)

        class Bibliotheque:
            def __init__(self):
                self.livres = []

            def ajoute(self, livre):
                self.livres.append(livre)

            def supprime_livres_abimes(self):
                for livre in self.livres:
                    if livre.etat == 0:
                        self.livres.remove(livre)

            def inventaire(self):
                print('---------------')
                print('contenu de ma bibliothèque :')
                print('---------------')
                for livre in self.livres:
                    livre.description()
                    print()

        ma_bibli = Bibliotheque()
        livre1 = Livre('Les Misérables', 'Victor Hugo', 3)
        livre2 = Livre('Les fleurs du mal', 'Charles Baudelaire', 1)
        livre1.description()
        ma_bibli.ajoute(livre1)
        ma_bibli.ajoute(livre2)
        ma_bibli.inventaire()

        ```
#}

## Recursivite

### 1.2 Un très mauvais exemple

C'est déjà une première chose à comprendre : un programme **peut** être appelé par lui-même, à l'intérieur de sa propre définition.

```python linenums='1'
def prems():
    print("un très mauvais exemple")
    prems()
```

Si on appelle cette fonction, par la commande :

```python
>>> prems()
```
La sortie en console sera celle-ci :

```
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
un très mauvais exemple
...
```

Évidemment, comme prévu, ce programme ne s'arrête pas. Nous sommes obligés de l'arrêter manuellement. Nous sommes (volontairement) tombés dans un piège qui sera systématiquement présent lors d'une programmation récursive : le piège de la boucle infinie{target=_blank}.

### 1.3 La mauvaise réputation{target=_blank}

Dans la culture informatique, la récursivité est (trop) souvent abordée par le biais de l'auto-référence, le puits sans fin de la boucle infinie.

On trouve d'ailleurs fréquemment cette définition de la récursivité :

> **Fonction récursive** : fonction qui fait appel à la récursivité. Voir *fonction récursive*.

Google fait aussi (dans toutes les langues) la même blague lors d'une recherche sur le terme «récursivité» :

Les acronymes récursifs{target=_blank} sont aussi très fréquents... et véhiculent avec eux le même piège : une fonction récursive ne serait *jamais vraiment définie* (c'est faux, nous le verrons)

Par exemple :

- GNU (dans GNU/Linux) signifie GNU is Not Unix. On ne sait jamais vraiment ce que signifie GNU...  
- PHP (le langage serveur) sigifie PHP: Hypertext Preprocessor
- VISA (les cartes bancaires) signifie VISA International Service Association.

### 2. La récursivité, ça marche !

Disons-le clairement : au-delà de la blague pour initiés (dont vous faites partie maintenant) la récursivité ne DOIT PAS être associée à une auto-référence vertigineuse : c'est en algorithmique une méthode (parfois) très efficace, à condition de respecter une règle cruciale :  :star: :star: :star: **l'existence d'un CAS DE BASE** :star: :star: :star: .  

Ce «cas de base» sera aussi appelé «condition d'arrêt», puisque la très grande majorité des algorithmes récursifs peuvent être perçus comme des escaliers qu'on descend marche par marche, jusqu'au sol qui assure notre arrêt.

### 2.1 La récursivité en BD

[](data/bd.png)

Observez bien la descente puis la remontée de notre vendeur de livre. 
Le cas de base est ici l'étage 0. Il empêche une descente infinie.

Nous coderons bientôt la fonction donnant le prix du livre en fonction de l'étage.

Pour l'instant, découvrons enfin à quoi ressemble une fonction récursive «bien écrite» :

### 2.2 Enfin un bon exemple

```python linenums='1'
    def mystere(n):
        if n == 0 :
            return 0
        else : 
            return n + mystere(n-1)
    ```

Trois choses sont essentielles et doivent se retrouver dans tout programme récursif :

- ```lignes 2 et 3``` :  le cas de base (si ```n``` vaut 0 on renvoie *vraiment* une valeur, en l'occurence 0)
- ```ligne 5``` : l'appel récursif
- ```ligne 5``` : la décrémentation du paramètre d'appel

**Utilisation de la fonction ```mystere```** 

```python
>>> mystere(0)
0
>>> mystere(4)
10
```

     

Que se passe-t-il lorsqu'on appelle ```mystere(4)``` ?

\begin{align}
  \rm{mystere(4)} &= 4+ \rm{mystere(3)}\\
   &= 4+ (3+\rm{mystere(2)}) \\
   &= 4+ (3+(2+\rm{mystere(1)} )) \\
   &= 4+ (3+(2+(1+\rm{mystere(0)} ))) \\   
   &= 4+ (3+(2+(1+0 ))) \\  
\end{align}

On voit que l'existence du cas de base pour $n=0$ est primordiale pour éviter la récursion infinie.

Cette fonction ```mystere(n)``` calcule donc la somme des entiers positifs inférieurs ou égaux à $n$.

    ```mystere(100)``` est égal à 5050. 
    Une anecdote raconte que Carl Friedrich Gauss trouva cette valeur de 5050 en quelques secondes, devant son instituteur ébahi.  
    Il venait pour cela d'inventer la formule : 
    $1+2+3+\dots+n=\frac{n(n+1)}{2}$

    Ici, $1+2+3+\dots+100=\frac{100\times 101}{2}=50 \times 101=5050$

    Coder la fonction ```prix``` de la BD présentée plus haut, qui prend en paramètre un entier positif ```etage``` et qui renvoie le prix de vente de la BD.

    On considère la fonction ```factorielle``` (notée $n!$ en mathématiques), qui prend en paramètre un entier positif ```n``` et qui calcule le produit de $n$ et de tous les entiers positifs qui lui sont inférieurs:

    $$ n! = n \times (n-1) \times (n-2) \times  \dots \times 3 \times 2 \times 1$$
    
    Exemple : $5!=5\times4\times3\times2\times1=120$

    Par convention, $1!=1$

    **Q1.** Programmer de manière impérative (dite aussi manière *itérative* ou manière *classique*) la fonction factorielle. On l'appelera ```fact_imp```. 
    

    **Q2.** Programmer de façon récursive la fonction factorielle. On l'appelera ```fact_rec```.

    

    Quel paradigme de programmation vous a semblé le plus naturel ?

### 3.1 Notion de pile

Lors d'un appel à une fonction récursive, le processeur utilise une structure de **pile** pour stocker les contextes d'exécution de chaque appel. Dans la notion de pile (voir ici), seule l'instruction «en haut de la pile» peut être traitée et enlevée (on dit «dépilée»).

La pile d'appels de notre fonction ```mystere(5)``` peut donc être schématisée comme ceci :

### 3.2 Limitation de la taille de la pile

Nous venons de voir que notre appel à ```mystere(5)``` générait une pile de hauteur 6 (on parlera plutôt de *profondeur* 6). Cette profondeur est-elle limitée ?

```python
mystere(2962)
```

    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

     in 
    ----> 1 mystere(2962)
    

     in mystere(n)
          3         return 0
          4     else :
    ----> 5         return n + mystere(n-1)
    

    ... last 1 frames repeated, from the frame below ...

     in mystere(n)
          3         return 0
          4     else :
    ----> 5         return n + mystere(n-1)
    

    RecursionError: maximum recursion depth exceeded in comparison

Vous venons de provoquer un «débordement de pile», le célèbre **stack overflow**. 

De manière générale, les programmes récursifs sont souvent susceptibles de générer un trop grand nombre d'appels à eux-mêmes. Il est parfois possible de les optimiser, comme nous le verrons dans le cours concernant la **programmation dynamique**.  

Nous reparlerons aussi de récursivité lorsque nous l'inscrirons dans un paradigme plus global de programmation, qui est **« diviser pour régner »** (en anglais *divide and conquer*).

### 4.1 La suite de Fibonacci

Considérons la suite numérique ainsi définie :

- $F_0 = 0$
- $F_1 = 1$
- $\forall n \in \mathbb{N}, F_{n+2} = F_{n+1}+F_n$

On a donc $F_2=0+1=1, F_3=F_2+F_1=1+1=2, F_4=F_3+F_2=2+1=3, F_5=F_4+F_3=3+2=5$ ...

    Implémenter de façon récursive la suite de Fibonacci.
    
        

        

**Observation de la pile d'exécution**

Appelons ```F(n)``` la fonction calculant de manière récursive le n-ième terme de la suite. Observons en détail la pile d'exécution lors du calcul de ```F(4)```.

     

On s'aperçoit notamment que :

- les appels récursifs ne sont PAS simultanés (rappelons que la simultanéité n'existe pas en informatique). On pourrait s'imaginer que la relation $F_4=F_3+F_2$ allait déclencher deux «fils» récursifs calculant respectivement $F_3$ et $F_2$. Il n'en est rien, on va jusqu'au bout du calcul de $F_3$ avant de s'intéresser à $F_2$.
- conséquence de la remarque précédente : le calcul de $F_2$ s'effectue 2 fois. Une amélioration future (appelée **mémoïsation**, voir le cours de programmation dynamique) sera de conserver cette valeur de $F_2$ afin d'améliorer les calculs.

Le module ```rcviz``` permet d'observer l'arbre des appels récursifs :
voir cette activité Capytale
  

On peut y construire par exemple l'arbre d'appel de ```fibo(6)``` :

On y remarque (par exemple) que ```fibo(2)``` est calculé 5 fois...

### 4.2 Comparaison des performances

Écrire une fonction ```fibo_imperatif(n)``` qui calcule de façon directe (*impérative*) le n-ième terme de la suite de Fibonacci. On pourra par exemple utiliser un dictionnaire.

    {{
    correction(True,
    """
\"Correction\" 
        ```python linenums='1'
        def fibo_imperatif(n):
            f = {}
            f[0] = 0
            f[1] = 1
            for k in range(2, n+1):
                f[k] = f[k-1] + f[k-2]
            return f[n]
        ```        
    """
    )
    }}

Construisons une fonction ```comparaison``` qui affichera le temps de calcul pour chacune des deux fonctions ```fibo_imperatif``` et ```fibo_recursif``` :

{#
```python linenums='1'
import time

def fibo_imperatif(n):
    ...

def fibo_recursif(n):
    if n == 0 :
        return 0   
    elif n == 1 :
        return 1
    else :
        return fibo_recursif(n-1) + fibo_recursif(n-2)

def comparaison(n):
    t0 = time.time()
    fibo_imperatif(n)
    print("algo impératif : ", time.time() - t0)
    t0 = time.time()
    fibo_recursif(n)
    print("algo récursif : ", time.time() - t0)

```
#}

```python linenums='1'
import time

def fibo_imperatif(n):
    f = {}
    f[0] = 0
    f[1] = 1
    for k in range(2, n+1):
        f[k] = f[k-1] + f[k-2]
    return f[n]

def fibo_recursif(n):
    if n == 0 :
        return 0   
    elif n == 1 :
        return 1
    else :
        return fibo_recursif(n-1) + fibo_recursif(n-2)

def comparaison(n):
    t0 = time.time()
    fibo_imperatif(n)
    print("algo impératif : ", time.time() - t0)
    t0 = time.time()
    fibo_recursif(n)
    print("algo récursif : ", time.time() - t0)

```

:arrow_right: **Résultats**

```python
>>> comparaison(10)
algo impératif :  6.9141387939453125e-06
algo récursif :  1.7642974853515625e-05
>>> comparaison(20)
algo impératif :  7.62939453125e-06
algo récursif :  0.0021445751190185547
>>> comparaison(30)
algo impératif :  1.8596649169921875e-05
algo récursif :  0.25478553771972656
>>> comparaison(40)
algo impératif :  1.1920928955078125e-05
algo récursif :  31.332343339920044
```

La fonction récursive apparait donc **beaucoup**, beaucoup plus lente que l'impérative (ici d'un facteur 100 pour toute augmentation de 10 du paramètre ```n```.)

:warning: **Attention :** cette comparaison des vitesses d'éxécution peut être critiquée car les deux programmes n'ont pas la même _complexité_. Nous étudierons la complexité au moment des algorithmes de tri. La complexité des fonctions récursives n'est pas au programme de NSI.

Peut-on résumer la récursivité à une méthode élégante mais inefficace ? Ce serait réducteur : l'efficacité c'est _aussi_ avoir un code lisible et intuitif. Nous en reparlerons lors du parcours des arbres et des graphes. (cf aussi l'exercice sur les Tours de Hanoï)

### 5. Annexe : dessins récursifs grâce au module ```turtle```

Le module ```turtle``` permet de faire des tracés basiques. Mais dès l'instant où on met de la récursivité dans le code, les résultats peuvent devenir très surprenants, et aboutir à des structures fractales.

```python linenums='1'
from turtle import *

ang = 40

def trace(n,l):
    if n == 0 :
        return None
    else :
        forward(l)
        left(ang)
        trace(n-1, 0.7*l)
        right(2*ang)
        trace(n-1, 0.7*l)
        left(ang)
        forward(-l)

        
penup()        
goto(0,-80)
pendown()
left(90)
speed(0)

trace(5,100)
```

{#
Astuce pour dessin instantanné dans Turtle
wn = Screen()
wn.tracer(0)

code

wn.update()

#}

### Introduction

#Exercices

    Écrire une fonction récursive ```puissance``` qui prend en paramètres deux nombres ```x``` et ```n``` qui renvoie le nombre $x^n$.

    On rappelle que le PGCD (plus grand diviseur commun de deux nombres) vérifie la propriété suivante : si la division euclidienne de $a$ par $b$ s'écrit $a = b \times q + r$, alors $pgcd(a,b)=pgcd(b,r)$. 

    Cette propriété est à la base de l'algorithme d'Euclide

    Exemple : $pgcd(24,18)=pgcd(18,6)=pgcd(6,0)$, donc $pgcd(24,18)=6$

    Écrire une fonction récursive ```pgcd``` qui prend en paramètres deux nombres ```a``` et ```b``` et qui renvoie leur PGCD.

    La conjecture de Syracuse  (ou de Collatz) postule ceci :  

    *Prenons un nombre $n$ : si $n$ est pair, on le divise par 2, sinon on le multiplie par 3 puis on ajoute 1. On recommence cette opération tant que possible. Au bout d'un certain temps, on finira toujours par tomber sur le nombre 1.*

    **Q1.** Écrire une fonction récursive ```syracuse``` qui prend en paramètres une entier ```n``` et qui écrivant tous les termes de la suite de Syracuse commençant à ```n``` , et s'arrêtant (on l'espère...) à la valeur 1.

    

    **Q2.** On appelle «temps de vol» le nombre d'étapes nécessaires avant de retomber sur 1. Modifier la fonction précédente afin qu'elle affiche le temps de vol pour tout nombre ```n```.

    Reproduire le dessin suivant, à l'aide du module ```turtle```.  

    ```turtle``` est un hommage au langage LOGO inventé par Seymour Papert au MIT à la fin des années 60.

    Proposer une nouvelle fonction récursive ```puissance_mod``` qui prend en paramètres deux nombres ```x``` et ```n``` et qui renvoie le nombre $x^n$. Pour optimiser la fonction déjà construite à l'exercice 1, utiliser le fait que :

    - si $n$ est pair, $a^n=(a \times a)^{n/2}$
    - sinon $a^n=a \times (a \times a)^{(n-1)/2}$

    Écrire un algorithme récursif ```dicho_recursive``` qui prend en paramètres une liste **triée** (par ordre croissant) ```lst``` et une valeur ```val```  et qui renvoie un booléen indiquant la présence ou non de la valeur ```val``` dans une liste ```lst```. 
    

    *Exemple d'utilisation :*

    ```python
    >>> lst = [2,4,5,5,7,9,11,15,16,18,19]
    >>> dicho_recursive(lst, 16)
    [2, 4, 5, 5, 7, 9, 11, 15, 16, 18, 19]
    [9, 11, 15, 16, 18, 19]
    [16, 18, 19]
    [16]
    True
    >>> dicho_recursive(lst, 6)
    [2, 4, 5, 5, 7, 9, 11, 15, 16, 18, 19]
    [2, 4, 5, 5, 7]
    [5, 5, 7]
    [5, 7]
    [5]
    False
    
    ```

    _Aide :_
    
    Les techniques de *slicing* (hors-programme) permettent de couper une liste en deux : 
    ```python
    >>> lst = [10, 12, 15, 17, 18, 20, 22]
    >>> lst[:3]
    [10, 12, 15]
    >>> lst[3:]
    [17, 18, 20, 22]
    ``` 

    On considère le jeu des **Tours de Hanoï**.
    Le but est de faire passer toutes les assiettes de A vers C, sachant qu'une assiette ne peut être déposée que sur une assiette de diamètre inférieur.
    

    Une version jouable en ligne peut être trouvée ici.

    1. S'entraîner et essayer d'établir une stratégie de victoire.
    2. Observer les images ci-dessous :
    
    
    
    

    Écrire une fonction récursive ```hanoi(n, depart, inter, arrivee)``` qui donnera la suite d'instructions (sous la forme " A vers C") pour faire passer une pile de taille n de ```depart```  vers ```arrivee```  en prenant ```inter```  comme intermédiaire.

    Cet exercice a pour objectif le tracé du flocon de Von Koch.

        Ce flocon est une structure fractale, au même titre que le superbe ensemble de Mandelbrot, dont vous pouvez trouver une implémentation en Pygame ici.

    L'idée est de répéter de manière récursive la transformation ci-dessous : chaque segment de longueur ```l``` donne naissance à 4 segments de longueur ```l/3```, en construisant une pointe de triangle équilatéral sur le deuxième tiers du segment.

    

    **Q1.** Créer une fonction récursive ```floc(n, l)``` qui trace à une «profondeur» ```n``` un segment de longueur ```l```.
    
    **Indications**

    - l'instruction de tracé n'a lieu que quand ```n``` vaut 0.
    - l'étape ```n``` fait 4 appels successifs à l'étape ```n-1```.

    

    **Q2.** Créer une fonction ```triangle(n, l)``` qui trace le flocon complet.

    1. Exercice 43.2 de la BNS 2025
    2. Application sur Capytale à retrouver ici 

    Exercice 4 du sujet Amérique du Nord J1 2022

    

    

    

    

    {{
    correction(False,
    """
\"Correction Q4.a.\" 
        ```python linenums='1'
        def complementaire(txt):
            comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
            sol = ''
            for c in txt:
                sol += comp[c]
            return sol
        ```         
    """
    )
    }}

    Exercice 1 du sujet Centres Étrangers J2 2022

    

    

    
    
    

    

    {#
    La question 3. est difficile, vous pouvez vous aider du code ci-dessous :

    ```python
    def ajouter(s, liste):
        res = []
        for m in liste:
            res.append(s + m)
        return res

    def produit(s, n):
        if n == 0:
            return [""]
        else:
            res = []
            for i in range(len(s)):
                res = res + ajouter(s[i], produit(s, n-1))
            return res

    ```
    #}
ex1J2AN2024">"

    Exercice 1 du sujet Amérique du Nord J2 2024    

    
    
    

    
    
    

    
    
    

    

    {{
    correction(False,
    """
\"Correction Q8\" 
        Nous connaissons (par exemple) le tri par sélection, dont l'ordre est en $n^2$. 

        Comme $2 < \\frac{8}{3}$, on en déduit que le tri par sélection a un coût meilleur que le tri de Stooge. 
    """
    )
    }}

{#

    - Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
    - Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.
#}

### Recursivite

Terminale - Spécialité NSI IFS Singapour
Chapitre 2 - Récursivité
Objectifs :
▷ Écrire un programme récursif
▷ Analyser le fonctionnement d'un programme récursif.
▷ Connaître des exemples relevant de domaines variés utilisant la récursivité
1 Introduction
La récursivité, à la fois en informatique et dans la vie courante, trouve son utilité dans la résolution
de problèmes de façon élégante de problèmes complexes en les décomposant en cas de base et en sous-
problèmes gérables.
La récursivité trouve son application dans une variété de domaines informatiques, tels que la program-
mation, la conception d'algorithmes, la modélisation de données et même dans la création de structures
récursives comme les arbres et les listes chaînées.
2 Définition
A retenir!
La récursivité est une méthode de résolution de problèmes qui consiste à décomposer le problème
en sous-problèmes identiques de plus en plus petits jusqu'à obtenir un problème suffisamment
petit pour qu'il puisse être résolu de manière triviale.
3 Exemples
Voici quelques exemples de problèmes que l'on résout facilement grâce à la récursivité :
▷ Calcul de factorielle
▷ Suite de Fibonacci
▷ Parcours d'arbres
▷ Calcul de puissance
▷ Tri de tableaux
▷ Recherche dans des structures de données
▷ Permutations et combinaisons
▷ Chemin le plus court dans un graphe
▷ Construction de fractales
▷ Évaluation d'expressions mathématiques
4 Application
4.1 Algorithme itératif
Étant donné une liste d'entiers L = [ 2, 12, 1, 8, 5, 10, 20 ] , on désire calculer la somme des
éléments de cette liste. Comme les listes sontitérables, nous pouvons simplement résoudre ce problème
avec un algorithme que l'on dititératif comme ci-dessous :
Algorithme 1 : Fonction somme des éléments d'une liste d'entiers
Données : Une liste d'entiersliste
Sorties : La somme des éléments de la liste
F onctionsomme_liste(liste) :
somme← 0
pour chaque chaque élément dans liste faire
somme← somme + élément
retourner somme
T. Rahobisoa 1/7 LP02 - Récursivité
Terminale - Spécialité NSI IFS Singapour
4.2 Algorithme récursif
Supposons maintenant que nous n'ayons pas la possibilité de faire deboucles. On peut alors aborder le
problème sous un autre angle. La somme des termes de cette liste est :
■ 2 + ( la somme des termes de[12,1,8,5,10,20])
■ soit : 2 + (12 + ( la somme des termes de[1,8,5,10,20])
■ et ainsi de suite...
■ jusqu'à : 2 + (12 + (1 + (8 + (5 + (10 + ( la somme des termes de[20]))))))
■ Et enfin, il est clair que la somme des termes de[20] est 20
Par conséquent, le calcul à faire est :2 + (12 + (1 + (8 + (5 + (10 + (20)))))) = 58 .
Considérons alors une fonctionsommeliste(liste) et qui renvoie le résultat de la somme des éléments
de la liste.
L'algorithme ci-dessous que l'on ditrécursif réalise cette seconde approche :
Algorithme 2 : Calcul récursif de la somme d'une liste d'entiers
Données : Une liste d'entiersliste
Sorties : La somme des éléments de la liste
F onctionsomme_liste(liste) :
si la longueur de la liste est égale à 1 alors
retourner liste[0]
sinon
retourner liste[0] + somme_liste(liste[1 :])
A faire 1 : Écrire en Python cette fonction, et la tester avec plusieurs exemples.
A faire 2 : Comparer les vitesses d'exécution des fonctions itérative et récursive de l'exemple précédent.
Pour tester la vitesse d'exécution d'une fonction on utilise le module timeit, comme le montre le code
ci-dessous pour une liste de 1000 entiers choisis aléatoirement entre 0 et 100 avec le module random.
1 from timeit import d e f a u l t _ t i m e r as timer
2 from random import randint
3
4 # ecrire les deux f on ct io ns ici
5
6 L = [ randint (0 ,100) for i in range (1000) ]
7
8 debut = timer ()
9 print ( s o m m e l i s t e ( L ) )
10 fin = timer ()
11 print ( fin - debut )
12
13 debut = timer ()
14 print ( somme ( L ) )
15 fin = timer ()
16 print ( fin - debut )
Question 1 Que pouvez-vous en conclure (pour cet exemple)?
T. Rahobisoa 2/7 LP02 - Récursivité
Terminale - Spécialité NSI IFS Singapour
5 Comment fonctionne un programme récursif?
Un programme est une suite d'instructions , son exécution peut être représentée par un parcours de
chemin ayant une origine et une extrémité.
Lorsde l'appel d'une fonction,cettesuiteestinterrompueletempsdecettefonction,avantdereprendre
à l'endroit où le programme s'est arrêté.
Figure 1 – Appel de fonction
Au moment où débute cette bifurcation, le processeur sauvegarde un certain nombre d'informations :
■ adresse de retour
■ état des variables, ..., etc.
Toutes ces données forment ce qu'on appelle lecontexte du programme , et elles sont stockées dans
ce qu'on appelle lapile d'exécution. À la fin de l'exécution de la fonction, le contexte est sorti pour
permettre la poursuite de l'exécution du programme.
Lors de l'exécution d'une fonction récursive, chaque appel récursif conduit au moment où il se produit à
un empilement du contexte dans la pile d'exécution.
Lorsqu'au bout den appels se produit la condition d'arrêt, les différents contextes sont progressivement
dépilés pour poursuivre l'exécution de la fonction.
Figure 2 – Contextes
Il est important de prendre conscience qu'une fonction récursive s'accompagne d'unecomplexité qui va
croître avec le nombre d'appels récursifs (en général linéairement, mais ce n'est pas une règle, cela dépend
du contenu du contexte).
T. Rahobisoa 3/7 LP02 - Récursivité
Terminale - Spécialité NSI IFS Singapour
6 Les trois règles
Tout comme les robots dans le roman de science-fiction de 1942 d'Isaac Asimov, les algorithmes récursifs
doivent obéir à trois règles :
A retenir!
■ Un algorithme récursif doit avoir un "état trivial" , cela permet d'avoir une condition
d'arrêt. Dans notre exemple :si la liste est de longueur 1 alors on renvoie le seul élément
de la liste .
■ Un algorithme récursif doit conduire vers cet "état d'arrêt" , cela permet de ne pas
faire une infinité d'appels récursifs. Dans notre exemple, à chaque appel récursif, la liste est
diminuée d'un élément donc nécessairement elle finira par n'en n'avoir plus qu'un.
■ Un algorithme récursif s'appelle lui même .
7 Itératif ou récursif?
Il n'existe pas de réponse définitive à la question de savoir si un algorithme récursif est préférable à un
algorithme itératif ou le contraire.
Il a été prouvé que ces deuxparadigmes de programmation sont équivalents.
On peut donc affirmer que tout algorithme itératif possède une version récursive, et réciproquement.
Le choix du langage peut aussi avoir son importance : un langage fonctionnel tel queCaml est conçu
pour exploiter la récursivité et le programmeur est naturellement amené à choisir la version récursive de
l'algorithme qu'il souhaite écrire.
À l'inverse, Python, même s'il l'autorise, ne favorise pas l'écriture récursive (limitation basse du nombre
d'appels récursifs; 1000 par défaut).
Enfin, le choix d'écrire une fonction récursive ou itérative peut dépendre du problème à résoudre. Certains
problèmes se résolvent particulièrement simplement sous forme récursive.
Figure 3 – Itératif vs récursif
T. Rahobisoa 4/7 LP02 - Récursivité
Terminale - Spécialité NSI IFS Singapour
8 Exercices
Exercice 1 : Mystère
On considère la fonctionmyst(L) qui prend une listeL en entrée et définie récursivement par :
1 def myst ( L ) :
2 if L == []:
3 return 0
4 else :
5 return 1 + myst ( L [1:])
Que fait cette fonction?
Exercice 2 : Maximum
Écrire les versionsitérative et récursive de fonctions renvoyant le maximum d'une liste d'entiers.
Exercice 3 : Puissance
Écrire les versionsitérative et récursive de fonctions calculantxnoù n est un entier etx est un réel.
Exercice 4 : Factorielle
Écrire les versionsitérative et récursivede fonctions calculantn! (appelée factorielle n) oùn est un entier
positif sachant que :n! = n· (n− 1)· (n− 2)··· 2· 1
Rappel : Par définition, 0 ! = 1 .
Exercice 5 : Décimal ↣ Binaire
Le but de cet exercice est de convertir un nombre décimal en binaire. Pour cela, on utilisera la succession
de divisions euclidiennes par 2.
Exemple :
Considérons le nombre 29 en base 10.
On effectue les divisions successives par 2 jusqu'à obtenir un quotient nul.
En lisant de droite à gauche les restes obtenus, on obtient l'écriture en base 2 de l'entier.
Ici, on obtient donc(292)10 = (11101) 2.
Écrire une fonction récursivedec_vers_bin(n) qui prend un entier naturel comme argument et renvoie
son écriture binaire sous la forme d'une chaîne de caractères.
Exemple :
>>> d e c _ v e r s _ b i n (38)
' 100110 '
T. Rahobisoa 5/7 LP02 - Récursivité
Terminale - Spécialité NSI IFS Singapour
Exercice 6 : Binaire ↣ Décimal
On souhaite cette fois convertir un binaire représenté par une chaîne de caractères en un décimal, codé
par un entier.
Si n est un entier naturel eta0, a1,...,ap sont les chiffres de son écriture en base 2, on a :
n = 2 pap + 2p−1ap−1a0
En remarquant quen = 2× (2p−1ap−1 + ... + a1) +a0 si n≤ 2, écrire une fonction récursivebin_vers_dec
qui répond au problème.
Exercice 7 : Recherche d'un mot dans un texte
On cherche à déterminer si un mot est présent dans un texte. Pour cela, on utilisera des chaînes de
caractères en Python. On considérera que la chaine vide"" est préfixe de toutes les autres chaînes.
1. Écrire une fonction prefixe(mot,texte) qui prend en argument deux chaînes de caractèresmot
et texte et détermine si le début de la chaînetexte est mot : on renverraTrue dans ce cas etFalse
sinon.
Exemple :
>> prefixe ( " inf " ," i n f o r m a t i q u e " )
True
>> prefix ( " nf " ," i n f o r m a t i q u e " )
False
2. En utilisant la fonction précédente, écrire une fonctionEst_dans_texte(mot,texte) qui renvoie
True si mot apparaît dans texte etFalse sinon.
Exercice 8 : Flocon de Von Koch
La courbe deVon Koch d'ordre n est défini de la manière suivante :
■ si n = 0 alors c'est un segment de longueur 1.
■ sinon :
▷ On divise le segment de droite en trois segments de longueurs égales.
▷ On construit un triangle équilatéral ayant pour base le segment médian de la première étape.
▷ On supprime le segment de droite qui était la base du triangle de la deuxième étape.
Figure 4 – Courbes de Von Koch d'ordren pour 0≤ n≤ 3
L'objectif du problème est de dessiner cette courbe à l'aide de la bibliothèqueTurtle grâce à une fonction
récursive. Pour cela, on remarquera que la courbe de Von Koch d'ordren + 1 est constituée de 4 parties
qui sont des courbes de Von Koch d'ordren dont la taille a été divisée par 3.
1. Écrire une fonction récursive courbeVK(n,l) qui dessine cette courbe en utilisantTurtle avec n
l'ordre de la courbe etl la longueur du segment à l'ordre 0.
2. En utilisant la fonction précédente, écrire une fonctionflocon(n,l) dessinant le flocon de Von
Koch d'ordre n.
T. Rahobisoa 6/7 LP02 - Récursivité
Terminale - Spécialité NSI IFS Singapour
Figure 5 – Flocons de l'ordre 0 à l'ordre 5
On rappelle quelques commandes :
reset() Efface tout
penup() Relève le stylo
goto(-200,125) Place au point de coordonnées(-200,125)
setup(600,600) Fenêtre de600 x 600
speed(0) Vitesse maximale
color("blue") Couleur bleue
pendown() Stylo en position d'écriture
right(d) Tourner à droite ded degrés
left(d) Tourner à gauche ded degrés
fd(p) Avancer dep pixels
T. Rahobisoa 7/7 LP02 - Récursivité

## Calculabilite Decidabilite

### 1. Un programme comme paramètre d'un programme

Les codes que nous manipulons ressemblent souvent à cela :
```python
def accueil(n):
    for k in range(n):
        print("bonjour")
```

Le programme s'appelle ```accueil```, et pour fonctionner il a besoin d'un paramètre, qui sera ici un nombre entier ```n```.

Voici comment nous pouvons représenter notre machine ```accueil```, son paramètre d'entrée (5) et sa sortie (les 5 «bonjour»)

Maintenant, enregistrons le code suivant dans un fichier ```test.py``` :
```python
def accueil(n):
    for k in range(n):
        print("bonjour")

accueil(5)
```

Pour exécuter ce code, nous devons taper dans un terminal l'instruction suivante :
```python3 test.py```, ce qui donnera 

Le programme utilisé est alors ```python3```, qui prend comme paramètre le programme ```test.py```. Ce paramètre ```test.py``` est un ensemble de caractères qui contient les instructions que le programme ```python3``` va interpréter. 

L'illustration correspondante sera donc :

 

Mais nous pouvons aller encore plus loin : l'instruction ```python3 test.py``` est tapée dans mon Terminal Linux, qui lui-même est un programme appelé ```Terminal```.

Et donc :

Conclusion :

**Il n'y a donc aucun obstacle à considérer un programme comme une simple donnée, pouvant être reçue en paramètre par un autre programme.** (voire par lui-même !)

    À titre anecdotique, on pourra exécuter en console cette instruction Python :
    ```python
    a='a=%r;print(a%%a)';print(a%a)
    ```
     Ce type de code (magique !) existe dans tous les langages et s'appelle un quine).

### 2.1 Un exemple

Considérons le programme suivant :

```python
def countdown(n):
    while n != 0:
        print(n)
        n = n - 1
    print("fini")
```

En l'observant attentivement, je peux prévoir que ```countdown(10)``` affichera les nombres de 10 à 1 avant d'écrire "fini". Puis le programme s'arrêtera.

Mais que va provoquer ```countdown(10.8)``` ?

Comme la variable ```n``` ne sera jamais égale à 0, le programme va rentrer dans une boucle infinie, il ne s'arrêtera jamais. Mauvaise nouvelle. 
J'ai pu prévoir ceci en regardant attentivement le code de mon programme. J'ai «remarqué» qu'une variable ```n``` non entière provoquerait une boucle infinie.

**Question :**
Est-ce qu'un programme d'_analyse de programmes_ aurait pu faire cela à ma place ?

### 2.2 Une machine pour prédire l'arrêt ou non d'un programme.

Après tout, un programme est une suite d'instructions (le code-source), et peut donc être, comme on l'a vu, le paramètre d'entrée d'un autre programme qui l'analyserait. 
Un tel programme (appelons-le ```halt```) prendrait en entrées :

- un paramètre ```prog``` (le code-source du programme)
- un paramètre  ```x```, qui serait le paramètre d'entrée de ```prog```.

 L'instruction ```halt(prog, x)``` renverrait ```True``` si ```prog(x)``` s'arrête, et ```False``` si ```prog(x)``` ne s'arrête pas.
 

**Exemple** : 

- ```halt(countdown, 10)``` renverrait ```True```.
- ```halt(countdown, 10.8)``` renverrait ```False```. 

**Tentative d'écriture de ```halt``` en Python :**

```python
def halt(prog, x):
    if "prog(x) s'arrête":   # mes excuses, je n'ai pas eu le temps de finir totalement ce code
        return True
    else :
        return False
```

Nous en resterons là pour l'instant dans l'écriture de ce programme. Nous allons nous en servir pour construire d'autres programmes.

### 2.3 Amusons-nous avec ce programme ```halt```.

Considérons le programme :

```python
def sym(prog):
    if halt(prog, prog) == True:
        while True:
            print("vers l'infini et au-delà !")
    else:
        return 1
```

On peut remarquer que le programme ```halt``` est appelé avec comme paramètres ```prog, prog```, ce qui signifie que ```prog``` se prend lui-même en paramètre. On rappelle que ce n'est pas choquant, un code-source étant une donnée comme une autre.

Ce programme ```sym``` reçoit donc en paramètre un programme ```prog```, et :

- va rentrer dans une boucle infinie si ```prog(prog)``` s'arrête.
- va renvoyer 1 si  ```prog(prog)``` ne s'arrête pas.

### 2.4 Un léger problème ...

Puisqu'un programme peut prendre en paramètre son propre code-source, que donnerait l'appel à ```sym(sym)``` ?

Deux cas peuvent se présenter, suivant si ```halt(sym, sym)``` renvoie ```True``` ou ```False```.

* **cas n°1** : ```halt(sym, sym)``` renvoie ```True```, ce qui signifie que ```sym(sym)```  devrait s'arrêter. Mais dans ce cas-là, l'exécution de ```sym(sym)``` rentre dans une boucle infinie. C'est une contradiction.

* **cas n°2** : ```halt(sym, sym)``` renvoie ```False```, ce qui signifie que ```sym(sym)```  rentre dans une boucle infinie. Mais dans ce cas-là, l'exécution de ```sym(sym)``` se termine correctement et renvoie la valeur 1. C'est une contradiction.

### 2.5 Conclusion

Nous venons de prouver que notre programme ```halt```, censé prédire si un programme ```prog``` peut s'arrêter sur une entrée ```x```, **NE PEUT PAS EXISTER**.

Ce résultat théorique, d'une importance cruciale, s'appelle **le problème de l'arrêt**.

    Il **ne peut pas exister** de programme universel qui prendrait en entrées :

     - un programme P 
     - une entrée E de ce programme P

    et qui déterminerait si ce programme P, lancé avec l'entrée E, va s'arrêter ou non. 

Ce résultat a été démontré par Alan Turing en 1936, dans un article intitulé *«On computable numbers, with an application to the Entscheidungsproblem»*.

Pour sa démonstration, il présente un modèle théorique de machine capable d'exécuter des instructions basiques sur un ruban infini, les machines de Turing.

À la même époque, le mathématicien Alonzo Church démontre lui aussi ce théorème de l'arrêt, mais par un moyen totalement différent, en inventant le lambda-calcul.

Tous deux mettent ainsi un terme au rêve du mathématicien allemand David Hilbert, qui avait en 1928 posé la question de l'existence d'un algorithme capable de répondre «oui» ou «non» à n'importe quel énoncé mathématique posé sous forme décisionnelle («un triangle rectangle peut-il être isocèle ?», «existe-t-il un nombre premier pair ?»)

Cette question, appelée «problème de la décision», ou *Entscheidungsproblem* en allemand, est définitivement tranchée par le problème de l'arrêt : un tel théorème ne peut pas exister, puisque par exemple, aucun algorithme ne peut répondre «oui» ou «non» à la question «ce programme va-t-il s'arrêter ?».

Le théorème de l'arrêt sera étendu plus tard par le théorème de Rice.

Ce résultat démontre que toutes les questions sémantiques (non évidentes) au sujet d'un programme sont indécidables :

- «ce programme va-t-il s'arrêter ?» (le théorème de l'arrêt)
- «ce programme va renvoyer la valeur 12 ?» 
- «ce programme va-t-il un jour renvoyer un message d'erreur ?» 
- ...

Rice démontre que toutes ces questions peuvent être ramenées (on dit *réduites*) au théorème de l'arrêt, qui est indécidable.

### 2. Calculabilité

Le problème de l'arrêt est dit **indécidable** car la fonction qui le résout (notre brave programme ```halt```) n'est pas **calculable**.

### 2.1 Notion de calculabilité

Qu'y a-t-il derrière cette notion de calculabilité ?
Cette notion, qui jette un pont entre les mathématiques (la vision de Church, pour schématiser) et l'informatique (la vision de Turing) n'est pas simple à définir !

Le *calcul* mathématique peut se réduire à une succession d'opérations élémentaires (songez à la multiplication entière comme une série d'additions). Les nombres calculables sont les nombres qui sont générables en un nombre fini d'opérations élémentaires. 
De la même manière, une fonction mathématique sera dite calculable s'il existe une suite finie d'opérations élémentaires permettant de passer d'un nombre x à son image f(x).

On retrouve cette notion d'opérations élémentaires dans les machines de Turing. 
Cette machine (théorique) permet de simuler tout ce qu'un programme informatique (une suite d'instructions) est capable d'exécuter. Un algorithme peut se réduire à une suite d'opérations élementaires, comme une fonction mathématique peut se réduire à une suite de calculs.
Dès lors, on pourra considérer un algorithme comme une fonction.

 
Turing a démontré que l'ensemble des fonctions calculables, au sens de Church, était équivalent à l'ensemble des fonctions programmables sur sa machine.
Certaines fonctions peuvent être calculables, *ou ne pas l'être* : c'est notamment le cas de notre fonction du problème de l'arrêt.

### 2.2 Langages Turing-complets

Ce résultat ne dépend pas du langage utilisé : le fait que nous ayons utilisé Python au paragraphe précédent n'a pas d'influence sur notre démonstration. Nous savons depuis les machines de Turing que tous nos langages de programmation sont **Turing-complets** : ils sont tous capables de faire la même chose (avec plus ou moins de facilité !). 
Scratch, C, Python, Java, Basic, Haskell, Brainfuck, Piet, Whitespace) ... tous ces langages sont théoriquement équivalents : **la calculabilité ne dépend pas du langage utilisé**.

### 2.3 (HP) Calculable, oui, mais facilement ? -> 1 million de $ à gagner ci-dessous.

L'étude de la calculabilité d'une fonction (à prendre au sens le plus large, c'est-à-dire un algorithme) ne se limite pas à un choix binaire : «calculable» vs «non calculable».  
Parmi les fonctions calculables, certaines peuvent l'être rapidement, et d'autre beaucoup moins.

On retrouve alors la notion bien connue de **complexité** algorithmique, qui permet de classifier les algorithmes suivant leur dépendance à la taille de leurs données d'entrée (voir le cours de Première).

On peut regrouper les problèmes suivant la complexité de l'algorithme qui permet de les résoudre.

#### 2.3.1 la classe P

    On dira que sont de **«classe P»** tous les problèmes dont l'algorithme de recherche de solution est de **complexité polynomiale**.

Que retrouve-t-on dans la classe P ? Tous les problèmes dont la solution est un algorithme de complexité linéraire, quadratique, logarithmique... Tout mais surtout pas un algorithme de complexité exponentielle.

Pour le résumer très grossièrement, un problème de classe P est un problème que l'on sait résoudre en temps raisonnable (même grand). 

- le problème du tri d'une liste est dans P.
- le problème de la factorisation d'un grand nombre (sur lequel repose la sécurité du RSA) n'est *a priori* **pas** dans P.
- le problème de la primalité («ce nombre est-il premier ?») a longtemps été considéré comme n'étant pas dans P... jusqu'en 2002, où a été découvert le test de primalité AKS, de complexité polynomiale (d'ordre 6). Ce test est donc maintenant dans P.

#### 2.3.2 la classe NP

    On dira que sont de **«classe NP»** tous les problèmes dont l'algorithme de recherche de solution est **Non-déterministe Polynomial**.
 

> Warning : :warning: NP ne signifie **pas** Non-Polynomial !!! :warning:

Que veut dire la formulation «non-déterministe polynomial» ? Cela fait référence à ce que serait capable de faire une machine de Turing (donc, n'importe quel ordinateur) travaillant de manière **non-déterministe**, donc capable d'explorer simultanément plusieurs solutions possibles. On peut imaginer un arbre dont le parcours se ferait simultanément dans toutes les branches, et non en largeur ou profondeur comme nous l'avons vu.

Sur une machine non-déterministe, si la solution à un problème se trouve en temps polynomial, alors ce problème appartient à la classe NP. 

Très bien, mais les machines non-déterministes... cela n'existe pas réellement. Comment caractériser concrètement cette classe de problème ?

Si la solution peut être trouvée de manière polynomiale par une machine non-déterministe, une machine déterministe *qui aurait de la chance* en partant directement vers la bonne solution la trouverait elle aussi de manière polynomiale. On simplifie souvent cela en disant «la vérification de la solution est polynomiale». Cela nous donnne cette définition plus accessible de la classe NP :

    On dira que sont de **«classe NP»** tous les problèmes dont l'algorithme de **vérification** de solution est **polynomial**.

Pour le résumer très grossièrement, un problème de classe NP est un problème dont on sait vérifier facilement si une solution proposée marche ou pas :

- la résolution d'un sudoku est dans NP : si quelqu'un vous montre un sudoku rempli, vous pouvez très rapidement lui dire si sa solution est valable ou pas.
- la factorisation d'un nombre est dans NP : si quelqu'un vous propose 4567*6037 comme décomposition de 27570979, vous pouvez très rapidement lui dire s'il a raison. (oui)
- le problème du sac à dos (en version décisionnelle) est dans NP. Une proposition de butin peut facilement être examinée pour savoir si elle est possible ou non.
- le problème du voyageur de commerce (ou TSP : Traveller Sales Problem), en version décisionnelle, est dans NP. Si on vous propose un trajet, vous pouvez facilement vérifier que sa longueur est (par exemple) inférieure à 150 km.

Malheureusement, aucun de ces problèmes cités n'a (à ce jour) d'algorithme de **résolution** meilleur qu'exponentiel...

#### 2.2.3 P = NP, ou pas ?

Tous les problèmes de P ont une solution qui peut être **trouvée** de manière polynomiale. Donc évidemment, la vérification de cette solution est aussi polynomiale. Donc tous les problèmes de P sont dans NP. On dit que P est inclus dans NP, que l'on écrit **P ⊂ NP**.

Voici une capture d'écran de l'excellente vidéo Nos algorithmes pourraient-ils être BEAUCOUP plus rapides ? (P=NP ?) de l'excellent David Louapre :

On y retrouve (en vert) la classe P, qui contient les algorithmes de tri.
En blanc, la classe NP, qui contient les problèmes de factorisation, du sudoku, du sac-à-dos...

Si quelqu'un trouve un jour un algorithme de polynomial de factorisation, alors le problème de factorisation viendra se ranger dans P. (accessoirement, le RSA sera sans doute détruit par cette découverte, sauf si l'ordre de complexité est très grand)

Mais certains de ces problèmes dans NP ont une propriété remarquable : la résolution polynomiale d'un seul d'entre eux ferait ramener la **totalité** des problèmes NP dans P. On dit que ces problèmes sont NP-complets (marqués en rouge ci-dessus)
Concrètement, si vous trouvez une solution polynomiale de résolution du sudoku, vous entrainez avec lui dans P tous les autres problèmes NP, et vous aurez ainsi prouvé que P = NP.
Accessoirement, vous gagnerez aussi le prix d'un million de dollars promis par la fondation Clay à qui tranchera cette question...
(prix que vous partagerez bien évidemment avec votre professeur de NSI)

Actuellement, à part le grand Donald Knuth, la plupart des chercheurs qui travaillent à ce problème sont plutôt pessimistes, et pensent que P ≠ NP. 
Cela signifie qu'ils pensent que certains problèmes ne pourront jamais avoir une solution polynomiale. 

Alors, P = NP ou P ≠ NP ? Réponse peut-être un jour...

---

    - Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
    - Prépabac NSI, Terminale, G. CONNAN, V. PETROV, G. ROZSAVOLGYI, L. SIGNAC, éditions HATIER.
    -  https://interstices.info/pnp-elementaire-ma-chere-watson/
    - https://interstices.info/alan-turing-du-calculable-a-lindecidable/ 
    - https://www.labri.fr/perso/betrema/MC/MC8.html 
    - https://scienceetonnante.com/2020/07/17/est-ce-que-p-np/

## Pratiques de programmation

### 1. Conventions syntaxiques

La programmation est un art délicat : un simple caractère en trop peut provoquer une erreur pour le code tout entier (penser à un innocent caractère d'espace en début de ligne dans un code Python).

Mais même lorsqu'un code s'exécute sans erreur, il ne faut pas négliger l'aspect purement «esthétique» de celui-ci : il est nécessaire de respecter autant que possible des conventions typographiques, qui vont standardiser le code et le rendre ainsi plus lisible.

Ainsi pour chaque langage, il existe une «bible» de bonnes pratiques de présentation du code, qui visent à l'uniformiser. Pour Python, cette référence s'appelle la Python Enhancement Proposal 8, plus connue sous le nom de PEP8. 

En voici quelques extraits :

### Les espaces

▶ Il faut mettre une espace (oui, en typographie, on dit «une» espace et non pas «un» espace) avant et après chaque opérateur de comparaison, d'affectation, ou mathématique  (```=, ==, >, +, *, ...``` )

```python

### BIEN

if x > 3:
    print("ok")
```

▶ Pour les opérateurs mathématiques, on essaie de reconstituer les groupes de priorité (lorsqu'il y en a) :

```python

### BIEN

for x in range(5):
    print('bonjour')
```

▶ Pour les virgules, et les deux points : 
pas d'espace avant mais une espace après.

```python

### BIEN

if color == (0, 255, 0):
    print('vert')
```

On peut contrôler si son code vérifie les standards de la PEP8 sur ce site http://pep8online.com/

### Les conventions de nommage

▶ Les variables à une lettre (comme ```i```, ```j```, ```k``` ) sont réservées aux indices (notamment dans les boucles).

▶ Les autres variables doivent avoir des noms explicites, éventuellement écrits en ```snake_case``` si plusieurs mots doivent être reliés.

```python

### BIEN

if date == 1:
    compte_epargne += versement_mensuel
```

Rappel des différents types de casse :

- ```snake_case``` : les mots sont séparés par des underscores. Conseillé en Python.
- ```camelCase``` : les mots sont séparés par des majuscules mais la 1ère lettre est minuscule. Conseillé en Javascript.
- ```PascalCase``` : les mots sont séparés par des majuscules et la 1ère lettre est majuscule. Conseillé en C.
- ```kebab-case``` : les mots sont séparés par des tirets courts. Conseillé en HTML - CSS.

▶ Cas particulier des classes en Programmation Orientée Objet : leur nom doit commencer par une majuscule.

```python

### 2.1 Commenter son code ? (ou pas)

La nécessité de commenter son code est assez controversée.  
Il est d'usage de dire qu'un code doit être assez **explicite** pour que le lecteur puisse le comprendre sans avoir à lire un commentaire. 

De fait, les commentaires sont parfois (souvent) superflus :

Et s'ils sont réellement nécessaires, il faut se poser la question : est-ce que ce code n'aurait pas pu être plus simple ? (attention, la réponse n'est pas toujours oui)

**Exemple :**

Considérons la fonction suivante.
```python
def f(c, t, n):
    # c est le capital de départ, t le taux annuel et n le nombre d'années
    return c * (1 + t)**n  #renvoie le capital après n années
```
Elle est bien commentée. Mais si on croise la fonction ```f()``` ailleurs dans le code, se souviendra-t-on de son rôle ?

Il aurait mieux valu écrire :
```python
def capital_apres_n_annees(capital, taux, nombre_annees) :
    return capital * (1 + taux)**nombre_annees
```
Ce code est plus long, mais assez explicite pour se passer de commentaires.

### 2.2 Le cas particulier des ```docstrings```

#### 2.2.1 Que sont les ```docstrings```?

Les ```docstrings``` sont des commentaires *normalisés* pour les fonctions, qui peuvent être consultés en console.

**Exemples :**

Nous connaissons la fonction ```len()``` qui permet par exemple de connaître la longueur d'une liste passée en paramètre.

Si nous tapons en console la commande ```print(len.__doc__)```, nous aurons la description de cette fonction. 

```python
>>> len.__doc__
'Return the number of items in a container.'
```
Il est aussi possible d'accéder à la docstring d'une fonction ```f```  par la commande ```help(f)``` :

```python
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

```

De même pour la fonction ```range``` :
```python
>>> print(range.__doc__)
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
```

Le résultat de la commande ```help(range)``` est trop long pour être repris ici, mais on y retrouve bien la docstring de la fonction ```range```.

#### 2.2.2 Créer ses propres docstrings

Il suffit pour cela de commencer la fonction à documenter par une ou plusieurs phrases entre triples quotes :

```python
def capital_apres_n_annees(capital, taux, nombre_annees) :
    """
    Renvoie le capital après n années.
    capital : valeur initiale
    taux : taux d'intérêt exprimé en nombre décimal (ex: 0.02 pour un taux de 2 %)
    nombre_annees : nombre d'années de placement du capital
    """
    return capital * (1 + taux)**nombre_annees
```
Ainsi, un utilisateur pourra trouver en console le mode d'emploi de notre fonction :

```python
>>> help(capital_apres_n_annees)
Help on function capital_apres_n_annees in module __main__:

capital_apres_n_annees(capital, taux, nombre_annees)
    Renvoie le capital après n années.
    capital : valeur initiale
    taux : taux d'intérêt exprimé en nombre décimal (ex: 0.02 pour un taux de 2 %)
    nombre_annees : nombre d'années de placement du capital
```

Comme on le voit, tout cela est très «verbeux». Cela peut nous paraître largement superflu puisque nos codes dépassent rarement quelques dizaines de lignes et sont lus par rarement plus de 2 personnes. Mais dans la vraie vie des développeurs, il est primordial qu'un code soit clair et documenté.

### 3. La programmation défensive : des ```assert``` pour sécuriser le code

La programmation défensive est l'art de prévoir le pire et d'essayer de le détecter avant qu'il ne soit trop tard.  
De manière bien plus concrète, il est d'usage d'essayer de répérer si des données (souvent des paramètres d'une fonction) sont susceptibles de créer des problèmes, ou sont hors spécification.

**Un exemple :**

La fonction :

```python
def racine_carree(x):
    assert x >= 0, 'un nombre positif ou nul est requis'
    return x ** 0.5
```
donnera, lors de l'appel à ```racine_carree(-2)```, le message suivant :

```python
>>> racine_carree(-2)
Traceback (most recent call last):
  File "", line 1, in 
  File "/home/gilles/Bureau/exemples_assert.py", line 2, in racine_carree
    assert x >= 0, 'un nombre positif ou nul est requis'
AssertionError: un nombre positif ou nul est requis
```

**Un autre exemple :**

```python
def moyenne_trimestrielle(liste_notes):
    """
    calcule la moyenne des nombres de la liste liste_notes
    """
    assert liste_notes != [] , 'liste vide'
    assert max(liste_notes) =0, 'au moins une note est en dessous de 0'
    
    return sum(liste_notes) / len(liste_notes)
```

À ce stade, les ```assert``` sont donc pour nous juste un moyen rapide de remplacer un test ```if ... then ... else``` pour détecter des erreurs potentielles.  
Ils sont en réalité plus utiles que cela : lors de la conception d'un programme, des ```assert``` sont posés pour vérifier l'intégrité du code, mais peuvent être désactivés à tout moment pour en faire un code optimisé (par la commande ```-O``` à l'exécution). Tout ceci dépasse largement le cadre de notre cours.

Il est à noter aussi que les erreurs peuvent être gérées par le mécanisme ```try ... except```, qui permet de «lever des exceptions». Pour les curieux, plus de renseignements ici.

### 4.1 Pourquoi des tests ?

Tester une fonction est la première chose que l'on fait (normalement...) lorsqu'on vient de finir de l'écrire. 

Par exemple, si on vient de construire la fonction ```valeur_absolue(n)```, il est fort probable qu'on aille taper ceci dans la console :

```python
>>> valeur_absolue(-3)
3
>>> valeur_absolue(0)
0
>>> valeur_absolue(7)
7
```

- On peut regrouper tous ces tests au sein d'une même fonction ```test_valeur_absolue()```.
- On peut écrire cette fonction ```test_valeur_absolue()``` avant même de commencer à écrire la fonction ```valeur_absolue(n)```.

> Remarque : 
> la méthode de développement logiciel TDD (Test Driven Developement) est basée en partie sur ce principe  : 

> 1. On commence par écrire le test de la fonction.
> 2. Le test échoue (forcément, la fonction n'est pas encore codée !)
 > 3. On écrit le code de la fonction pour que le test soit validé.
 > 4. On améliore (si possible) ce code tout en vérifiant que le test continue à être valide.

Revenons à nos tests sur la fonction ```valeur_absolue(n)```

```python
def test_valeur_absolue():
    if valeur_absolue(-3) == 3 :
        print("ok")
    else:
        print("erreur")
        
    if valeur_absolue(0) == 0 :
        print("ok")
    else:
        print("erreur")
        
    if valeur_absolue(7) == 7 :
        print("ok")
    else:
        print("erreur")
```

En console, il suffit maintenant d'appeler la fonction ```test_valeur_absolue()``` :

```python
>>> test_valeur_absolue()
ok
ok
ok
```

### 4.2 Revoilà les ```assert```

Utiliser des ```assert``` permet d'écrire très simplement les tests précédents.

Reprenons notre fonction ```valeur_absolue()```. Sa fonction test  ```test_valeur_absolue()``` peut s'écrire :

```python
def test_valeur_absolue():
    assert valeur_absolue(-3) == 3
    assert valeur_absolue(0) == 0
    assert valeur_absolue(7) == 7

```

**Exercice :**  
Écrire une fonction ```maxi(liste)``` qui renvoie le plus grand élément de la liste ```liste``` passée en paramètre (de préférence sans utiliser la fonction ```max()``` ...).  
Vous écrirez **d'abord** une fonction ```test_maxi()``` avant d'écrire la fonction ```maxi(liste)```

### 4.3 Le module ```doctest```

Le module ```doctest```  permet d'écrire les tests **à l'intérieur** de la docstring d'une fonction. 

Considérons une fonction dont le but est de compter les voyelles du mot passé en paramètre.

```python
def compte_voyelles(mot):
    """
    renvoie le nombre de voyelles du mot donné en paramètre.
    >>> compte_voyelles("python")
    2
    >>> compte_voyelles("HTTP")
    0
    >>> compte_voyelles("eau")
    3
    """
    voyelles = "aeiou"
    total = 0
    for lettre in mot:
        if lettre in voyelles:
            total += 1
    return total
```

Observez bien la docstring : elle contient explicitement ce qu'on veut que renvoie le terminal lorsqu'on appellera la fonction.
On écrit donc les trois chevrons ```>>>``` suivi de l'appel à la fonction, et à la ligne en dessous ce que nous espérons que la fonction nous renvoie.
On peut écrire autant de tests que l'on veut.

Ensuite, en console :
```python
>>> import doctest
>>> doctest.testmod()
```
Dans notre cas, le retour sera celui-ci :

```python
>>> import doctest
>>> doctest.testmod()
**********************************************************************
File "voyelles.py", line 4, in __main__.compte_voyelles
Failed example:
    compte_voyelles("python")
Expected:
    2
Got:
    1
**********************************************************************
1 items had failures:
   1 of   3 in __main__.compte_voyelles
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=3)
```

On voit que le test ```compte_voyelles("python")``` a renvoyé la valeur 1 alors qu'on attendait 2. En regardant notre fonction, on s'aperçoit donc qu'on avait oublié le ```y``` dans la liste des voyelles. 

En corrigeant ceci, le test devient :
```python
>>> import doctest
>>> doctest.testmod()
TestResults(failed=0, attempted=3)
```
Ce qui est beaucoup plus satisfaisant.

### 4.3 À propos des tests

Le comportement face aux tests en programmation doit être le même qu'en mathématiques : _un test qui ne marche pas est plus riche d'enseignements qu'un test qui marche_.

En mathématiques, seule la notion de contre-exemple est fertile : si quelqu'un vous affirme que _«tous les nombres impairs sont premiers»_, il vous suffit d'exhiber le nombre 9 pour lui prouver qu'il a tort et achever la discussion.

Par contre, il aurait pu essayer de vous convaincre avec les nombres 3, 5 et 13, qui sont bien impairs et premiers.

De la même manière, voir qu'une fonction passe les tests que vous avez écrits ne vous assurera pas que cette fonction aura _toujours_ le bon comportement souhaité. Elle l'aura pour les valeurs de test, mais pas forcément pour les autres.

En revanche, si une fonction ne passe pas un des tests, vous avez la certitude qu'il y a un problème à régler quelque part.

Tout ceci en admettant, bien sûr, que vos tests _eux-mêmes_ ne comportent pas d'erreurs...

---

### Bibliographie

- https://www.reddit.com/r/ProgrammerHumor/
- https://fr.wikipedia.org/wiki/Test_driven_development
- https://www.fil.univ-lille1.fr/~L1S2API/CoursTP/tp_doctest.html
---

## Pseudo-code

### Pseudo-code

Terminale - Spécialité NSI IFS Singapour
Chapitre 1 - Pseudo-code et révisions Python
Objectifs :
▷ Améliorer sa pensée logique
▷ Décomposer un problème complexe en étapes simples
▷ Décrire les étapes d'un programme en une structure simple et lisible
▷ Écrire un programme en langage naturel
1 Introduction
Le langage naturel, ou pseudo-code, agit comme un pont entre la langue humaine et les langages de
programmation. Il permet aux programmeurs de conceptualiser des algorithmes en utilisant une syntaxe
informelle, favorisant la planification efficace et la communication des idées complexes avant la mise en
œuvre concrète. En simplifiant les concepts de programmation, le pseudo code facilite le développement
d'algorithmes logiques et bien conçus.
2 Définition
A retenir!
Le pseudo-code permet de décrire facilement un algorithme avec un vocabulaire simple et sans
connaissance à priori du langage de programmation utilisé pour son implémentation machine.
3 Consignes
Pour chacun des exercices ci-dessous, il faudra :
▷ Ecrire l'algorithme correspondant en pseudo-code
▷ Implémenter la fonction demandée en Python
▷ Faire l'appel de la fonction ainsi créée dans votre programme principal
▷ Déposer chaque code source dansClassroom avec un fichier nomméTP00-ExN.py
4 Exercices
Exercice 1 : Somme d'une liste d'entiers
Écrire une fonctionsomme(L), qui prend en paramètre une liste d'entiers et qui retourne la somme de ses
éléments.
Algorithme en pseudo-code :
T. Rahobisoa 1/6 LP01 - Pseudo-code
Terminale - Spécialité NSI IFS Singapour
Rappel :
Pour implémenter l'algorithme écrit en pseudo-code, vous pourrez compléter le code Python ci-dessous :
1 from random import *
2 L = [ randint (0 ,100) for i in range (20) ]
3
4 def somme ( L ) :
5
6 # ecrire votre code ici
7
8 print ( somme ( L ) ) # appel de la fonction dans le PP
Exercice 2 : Maximum d'une liste
Écrire une fonctionmaxi(L), qui prend en paramètre une liste d'entiers et qui retourne le plus grand de
ses éléments.
Algorithme en pseudo-code :
Exercice 3 : Minimum d'une liste
Écrire une fonctionmini(L), qui prend en paramètre une liste d'entiers et qui retourne le plus petit de
ses éléments.
Algorithme en pseudo-code :
T. Rahobisoa 2/6 LP01 - Pseudo-code
Terminale - Spécialité NSI IFS Singapour
Exercice 4 : Puissance
Écrire une fonction puissance(x,n), qui prend en paramètre un réelx et un entier naturel n et qui
renvoie xn.
Algorithme en pseudo-code :
Exercice 5 : Mot inversé
Écrire une fonctioninverse(mot) qui prend en paramètre un mot et qui renvoie le mot écrit à l'envers.
Par exemple :
1 >>> mot = bonjour
2 >>> inverse ( mot )
3 >>> roujnob
Algorithme en pseudo-code :
Exercice 6 : Tri par insertion
Implémenter la fonction tri_insertion(L) correspondant à l'algorithme de tri ci-dessous vu en classe
de Première :
Algorithme 1 : Tri par insertion
Données : Une liste L de n éléments
Sorties : La liste L triée en ordre croissant
pour k allant de 1 à n− 1 faire
j← k;
tant que j > 0 et L[j− 1] > L[j] faire
On échange L[j-1] et L[j]
j← j− 1
retourner L
T. Rahobisoa 3/6 LP01 - Pseudo-code
Terminale - Spécialité NSI IFS Singapour
Exercice 7 : Conversion
Examiner le code Python ci-dessous :
1 def c o n v e r s i o n (n , b ) :
2 signes = " 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
3 mot = " "
4 while n ! = 0:
5 mot = signes [ n % b ] + mot
6 n = n // b
7 return mot
1. Que permet de faire la fonction ci-dessus?
2. Ecrire l'algorithme en pseudo-code.
Algorithme en pseudo-code :
Exercice 8 : Déconversion
Écrire une fonctiondeconvers(mot,b) qui fait le contraire de la fonction de l'exercice 7.
Aide :l'instruction print(signes.index("A")) affiche 10
Algorithme en pseudo-code :
T. Rahobisoa 4/6 LP01 - Pseudo-code
Terminale - Spécialité NSI IFS Singapour
Exercice 9 : Suite de Fibonacci
Ecrire une fonction fib(n) qui affiche lesn premiers termes de la suite de Fibonacci.
Rappel :
Les deux premiers termes de la suite de Fibonacci sont 0 et 1. Ensuite, chaque terme successif est la
somme des deux termes précédents. Ainsi 0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8,...,etc.
Algorithme en pseudo-code :
Exercice 10 : Plus Grand Commun Diviseur
Ecrire une fonctionpgcd(a,b) qui renvoie le PGCD de deux entiers naturels a et b.
Rappel :
PourrevoirlanotiondePGCD,utiliserlesitesuivant:https://www.jeuxmaths.fr/cours/calcul-PGCD.php
Algorithme en pseudo-code :
T. Rahobisoa 5/6 LP01 - Pseudo-code
Terminale - Spécialité NSI IFS Singapour
Exercice 11 : Tri à bulles
Ecrire une fonctiontri_bulles(L) qui effectue le tri à bulles d'une liste L passée en paramètres.
Rappel :
Pour découvrir et comprendre le principe du tri à bulles, utiliser l'article Wikipedia correspondant.
Algorithme en pseudo-code :
T. Rahobisoa 6/6 LP01 - Pseudo-code

## Programmation objet

### Programmation objet

Terminale - Spécialité NSI IFS Singapour
Chapitre 3 - Programmation orientée objet
Objectifs :
▷ Connaître le vocabulaire de la programmation objet : classes, attributs, méthodes, objets.
▷ Ecrire la définition d'une classe
▷ Accéder aux attributs et méthodes d'une classe.
1 Introduction
Jusqu'à présent nous avons utilisé des objets dont le type est prédéfini :int, float, bool, str, list,
tuple, dict. Sans le savoir, nous avons découvert les concepts de laprogrammation orientée objet
ou POO. Ainsi, en classe de Première, nous avions déjà appris à utiliser des méthodes associées à ces
types, comme :
ma_liste.append(valeur)
Comme de nombreux autres langages tels queJava ou C++, Python est un langage orienté objet .
On peut donc dire que tout y estobjet. Une variable de typeint est en fait un objet de typeint donc
construit à partir de la classeint. Idem pour lesfloat et str. Mais également pour leslist, tuple,
dict, ..., etc.
On peut donc créer ses propres objets qui auront leursméthodes, ce qui aura pour effet :
▷ de faciliter l'implémentation de données
▷ d'augmenter la lisibilité du programme.
2 Définition
A retenir!
Une classe définit des objets qui sont desinstances (des représentants) de cette classe.
On utilisera le motobjet ou instance pour désigner la même chose.
Les objets peuvent posséder desattributs (variables associées aux objets) et desméthodes (qui
sont des fonctions associées aux objets et qui peuvent agir sur ces derniers ou encore les utiliser).
3 Découverte par des exemples
Imaginons que nous ayons un objetEleve, qui permettrait pour un élève de stocker dans une variable
eleve1 des données comme son nom, son prénom, sa date de naissance et ses notes dans différentes
matières, ainsi qu'une méthode qui calculerait samoyenne.
3.1 Création de la classe
▷ Pour créer une classe, on utilise le mot-clé :class suivi par le nom de la classe et les ":"
▷ Par convention, le nom de la classe commence par unemajuscule et ne contient que des caractères
alphanumériques.
1 # creation de la classe Eleve
2 class Eleve :
Ajoutons l'instructionpasset créons une variableeleve1de typeEleve(une instance de la classeEleve).
T. Rahobisoa 1/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
1 class Eleve :
2 pass # signifie qu ' on ne fait rien ...
3
4 eleve1 = Eleve ()
5 print ( type ( eleve1 ) )
Le résultat signifie queeleve1 est une instance de la classeEleve (une variable de typeEleve).
3.2 Les attributs
Les attributs sont des variables associées à la classe.
Il y en a de deux types :
▷ Les attributs de classe : un attribut de classe (ou variable de classe) est un attribut qui sera
identique pour chaque instance et n'a pas vocation à être changé.
▷ Les attributs d'instance : une variable ou attribut d'instance est une variable accrochée à une
instance et qui est spécifique à cette instance. Et d'une instance à l'autre, il ne prendra pas forcément
la même valeur.
Pour notre exemple, nous choisirons les matières comme attributs de classe et lesnom, prénom, date de
naissance et les notes comme attributs d'instance.
Le constructeur
L'endroit le plus approprié pour déclarer un attribut est à l'intérieur d'une méthode appelée
le constructeur. S'il est défini, il est implicitement exécuté lors de la création de chaque instance.
Le constructeur d'une classe se présente comme une méthode et suit la même syntaxe sauf que
son nom est imposé :__init__ (Attention, il faut deux underscores de chaque côté ! ).
Hormis le premier paramètreself, il n'existe pas de contrainte concernant la liste des paramètres
excepté que le constructeur ne doit pas retourner de résultat.
Exemple :
1 class Eleve :
2 # a tt ri bu ts de classe
3 matiere1 = " P r o g r a m m a t i o n "
4 matiere2 = " A l g o r i t h m i q u e "
5 matiere3 = " Projet "
6
7 # c o n s t r u c t e u r
8 def __init__ ( self , Nom , Prenom , Date , Note1 , Note2 , Note3 ) :
9 # a tt ri bu ts d ' instance
10 self . nom = Nom
11 self . prenom = Prenom
12 self . date = Date
13 self . no te _m at 1 = Note1
14 self . no te _m at 2 = Note2
15 self . no te _m at 3 = Note3
16
17 # creation d ' un eleve
18 eleve1 = Eleve ( ' Terieur ' , ' Alain ' , ' 0 1 / 0 1 / 2 0 0 5 ' ,12 ,10 ,15)
Comment accéder aux valeurs des attributs d'instance créés ?
On utilise la syntaxe :instance.attribut (notez bien le point )
print ( eleve1 . prenom , eleve1 . nom )
print ( eleve1 . matiere1 , ': ' , eleve1 . n ot e_ ma t1 )
T. Rahobisoa 2/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
print ( eleve1 . matiere2 , ': ' , eleve1 . n ot e_ ma t2 )
print ( eleve1 . matiere3 , ': ' , eleve1 . n ot e_ ma t3 )
Noter ci-dessous l'affichage obtenu :
3.3 Les méthodes
Il serait intéressant de pouvoir obtenir la moyenne de l'élève avec l'instructioneleve1.moyenne(), c'est-
à-dire en appliquant la méthodemoyenne() à l'instance eleve1.
Pour cela on crée une fonction à l'intérieur de la classeEleve qui retourne la moyenne de l'élève :
1 def moyenne ( self ) :
2 return (( self . no te _m at 1 + self . no te _m at 2 + self . no te _m at 3 ) /3)
A faire :
▷ Ajouter cette méthode et faire afficher la moyenne de l'élève.
▷ Ajouter ces trois élèves et faire afficher leurs résultats et leurs moyennes.
Nom : Oma Nom : Neymar Nom: Duff
Prénom : Modeste Prénom : Jean Nom: John
Date : 01/03/2006 Date : 01/07/2006 Date : 01/11/2007
Programmation : 17 Programmation : 7 Programmation : 13
Algorithmique : 6 Algorithmique : 14 Algorithmique : 8
Projet : 16 Projet : 11 Projet : 17
▷ Ecrire une fonction (hors de la classe bien sûr!) qui prend en paramètres une liste constituée de
ces quatre élèves et qui retourne les moyennes par matière.
On attend le rendu suivant :
Programmation : 12.25
Algorithmique : 9.5
Projet : 14.75
3.4 La documentation
Notre classe Eleve est une structure de données qui peut être utilisée dans différents programmes par
différents programmeurs, il est donc important voire primordial de bien la documenter.
Cette documentation doit montrer à minima comment sont construites les instances, quels sont les attri-
buts et les méthodes disponibles.
Cette documentation est accessible via l'instruction :help(Eleve)
Par exemple, voici une documentation possible :
1 class Eleve :
2 '''
3 Creation d ' une instance eleve :
4 eleve = eleve ( nom ( str ) , prenom ( str ) , date ( str ) ,
note1 ( float ) , note2 ( float ) , note3 ( float ) )
5
T. Rahobisoa 3/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
6 at tr i bu ts d ' instance : nom , prenom , date , note_mat1 , note_mat2 , n ot e_ m at 3
7 at tr i bu ts de classe : matiere1 , matiere2 , matiere3
8 methode : moyenne () retourne la moyenne de l ' eleve
9 '''
C'est d'autant plus important lorsque si cette classe se trouve dans un autre fichier.
A faire :
▷ Copier-coller la classeEleve dans un fichier que vous enregistrerez sous le nomMaclasse.py
▷ Créer un autre fichiermon_programme.py, dans lequel vous écrirez :
from Maclasse import Eleve
eleve5 = Eleve ( ' Onette ' , ' Camille ' , ' 0 1 / 0 8 / 2 0 0 6 ' ,18 ,17 ,19)
print ( eleve5 . prenom , eleve5 . nom , ': ' , eleve5 . moyenne () )
Attention, les deux fichiers doivent être dans le même dossier!
La documentation est toujours très importante car si vous donnez cette classe à un autre programmeur,
il faut qu'il puisse savoir comment l'utiliser sans avoir à en décortiquer le code...
Remarques :
Nous avons construit une structure de données répondant à un cahier des charges qui n'est pas
trop ambitieux.
On pourrait se poser les questions suivantes :
▷ Que faire si un élève n'a pas de notes dans une des matières?
▷ Comment rendre impossible la saisie d'une note supérieure à 20?
▷ Comment rendre impossible la saisie d'une note inférieure à 0?
▷ Que faire lors de la saisie d'une note non numérique, ...,etc.
4 Exercices
Exercice 1 : Dominos
1. Écrire une classeDomino pour représenter une pièce de domino. Les objets sont initialisés avec les
valeurs des deux faces, A et B.
2. Ajouter une méthodeaffichePoints(self) qui affiche les valeurs des deux faces, et une méthode
total(self)qui retourne la somme des deux valeurs.
Exercice 2 : Compte bancaire
1. Écrire une classe CompteBancaire. Les objets sont initialisés avec le nom du titulaire et le solde.
L'argument solde doit être facultatif et avoir une valeur prédéfinie à zéro.
2. Ajouter deux méthodesdepot(self,somme) et retrait(self,somme) pour changer le solde.
3. Ajouter une méthodeaffiche(self) qui montre le solde courant.
Exercice 3 : Rectangle
1. Écrire une classe Rectangle, permettant de construire un rectangle doté d'attributs longueur et
largeur.
2. Ajouter deux méthodesperimetre(self) et surface(self).
T. Rahobisoa 4/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
Exercice 4 : Personnage
1. Écrire une classePersonnage, avec son nom et ses points de vie comme attribut.
2. Ajouter une méthodecombat(self,other) qui diminue de façon aléatoire les points de vie de l'un
des personnages.
Exercice 5 : Robot
1. Écrire une classeRobot, avec ses coordonnées comme attributs et une direction (None par défaut).
2. Ajouter la méthode avancer(self), qui permet au robot d'avancer d'une case dans la direction
choisie.
Exercice 6 : Personnage 2
On considère une classePersonnage représentant un personnage de jeu. Le plateau de jeu est représenté
par un repère orthonormé à trois axes. La position du joueur dans le plateau est repérée par ses attributs
x, y et z.
1. Ecrire un constructeur initialisant les mesures.
2. Ecrire les méthodes avance, droite et saute permettant respectivement de faire avancer, aller à
droite et sauter le personnage, c'est-à-dire d'augmenter de 1 respectivement x, y et z.
3. Implémenter une autre méthodecoord renvoyant les coordonnées sous forme d'un triplet.
4. Essayer avec :Laura = Personnage(0, 0, 0)
Exercice 7 : Mystère
Voici un programme en Python :
1 import random
2
3 class Piece :
4
5 def alea ( self ) :
6 return random . randint (0 ,1)
7
8 def moyenne ( self , n ) :
9 tirage = [ ]
10 for i in range ( n ) :
11 tirage . append ( self . alea () )
12 return sum ( tirage ) / n
13
14 p = Piece ()
15 print ( p . moyenne (100) )
Expliquer en détail ce que ce programme permet d'afficher.
T. Rahobisoa 5/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
Exercice 8 : Voitures
1. Créer une classeVoiture avec deux attributs d'instance :
- couleur, qui stocke la couleur de la voiture sous forme de chaîne de caractères
- kilometrage, qui stocke le nombre de kilomètres sur la voiture sous forme d'entier.
2. Instancier deux objetsVoiture :
- une voiture bleue de 20 000 kilomètres
- une voiture rouge de 30 000 kilomètres.
3. Afficher leurs couleurs et leur kilométrage.
Votre sortie devrait ressembler à ceci :
La voiture bleue a 20 000 k i l o m e t r e s .
La voiture rouge a 30 000 k i l o m e t r e s .
Exercice 9 : Cinéma
On considère les définitions de classe suivantes :
1 class Personne :
2 """ Objet r e p r e s e n t a n t une personne """
3
4 def __init__ ( self , nom : str , a n n e e _ n a i s s a n c e : int , l i e u _ n a i s s a n c e :
str ) :
5 self . nom = nom
6 self . a n n e e _ n a i s s a n c e = a n n e e _ n a i s s a n c e
7 self . l i e u _ n a i s s a n c e = l i e u _ n a i s s a n c e
8
9
10 class Film :
11 """ Objet r e p r e s e n t a n t un film """
12
13 def __init__ ( self , titre : str , r e a l i s a t e u r : Personne ) :
14 self . titre = titre
15 self . r e a l i s a t e u r = r e a l i s a t e u r
1. Comment créer une instance de la classePersonne appelée lautner pour le réalisateur Georges
Lautner né en 1926 à Nice?
2. Proposer la définition d'une méthode __str__ dans la classe Personne qui afficherait "Georges
Lautner est une personne née à Nice en 1926 " lors de l'appelprint(lautner).
3. On crée une instance de la classeFilm avec l'instruction suivante :
tonton = Film("Les tontons flingueurs", lautner) .
- Qu'affiche l'instruction :print(tonton.titre)?
- Qu'affiche l'instruction :print(tonton.réalisateur.nom)?
4. - Proposer la définition d'une méthode __str__ dans la classeFilm qui afficherait "Les tontons
flingeurs est un film réalisé par Georges Lautner originaire de Nice " lors de l'appel
print(tonton).
T. Rahobisoa 6/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
Exercice 10 : Jeu de dominos
Le domino est un jeu très ancien composé de 28 pièces toutes différentes. Sur chacune de ces pièces, il y
a deux côtés constitués de 0 (blanc) à 6 points. Lorsque deux côtés possèdent le même nombre de points,
on l'appelle domino double.
1. Proposer une classe Domino permettant de représenter une pièce. Les objets seront initialisés par
les valeurs portées par les des deux côtés (gauche et droite). On définit des méthodesest_double
et est_blanc pour tester si le domino est double ou blanc.
2. Ajouter une méthodeaffiche qui affiche les valeurs des deux faces de manière horizontale pour un
domino classique et de manière verticale pour un domino double.
3. Proposer une classe JeuDeDomino permettant de manipuler le jeu de domino complet. On créera
une méthode pour mélanger le jeu et pour une autre distribuer selon 2 joueurs.
On pourra utiliser la méthoderandom.shuffle(mylist).
Rappel :
>>> import random
mylist = [ ' apple ' , ' banana ' , ' cherry ']
random . shuffle ( mylist )
>>> mylist
[ ' banana ' , ' apple ' , ' cherry ']
En utilisant cette classe, on devrait obtenir le tirage au sort de 7 dominos pour chacun des 2 joueurs.
Par exemple :
>>> mon_jeu = J e u D e D o m i n o ()
>>> mon_jeu . montre ()
Joueur 1
- - - - - - - - -
| |
| 6 | 3 |
| |
- - - - - - - - -
- - - - - - - - -
| |
| 6 | 5 |
| |
- - - - - - - - -
- - - -
| |
| 0 |
| - - - |
| 0 |
| |
- - - -
- - - - - - - - -
| |
| 5 | 4 |
| |
- - - - - - - - -
- - - - - - - - -
| |
| 3 | 1 |
| |
- - - - - - - - -
T. Rahobisoa 7/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
- - - - - - - - -
| |
| 5 | 0 |
| |
- - - - - - - - -
- - - - - - - - -
| |
| 3 | 2 |
| |
- - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Joueur 2
- - - - - - - - -
| |
| 1 | 0 |
| |
- - - - - - - - -
- - - - - - - - -
| |
| 2 | 1 |
| |
- - - - - - - - -
- - - - - - - - -
| |
| 6 | 4 |
| |
- - - - - - - - -
- - - -
| |
| 2 |
| - - - |
| 2 |
| |
- - - -
- - - - - - - - -
| |
| 3 | 0 |
| |
- - - - - - - - -
- - - - - - - - -
| |
| 6 | 2 |
| |
- - - - - - - - -
- - - - - - - - -
| |
| 2 | 0 |
| |
- - - - - - - - -
T. Rahobisoa 8/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
Exercice 11 : Chiens
On souhaite dans cet exercice créer une classeChien ayant deux attributs :
— un nom nom de type str,
— un poids poids de type float.
Cette classe possède aussi différentes méthodes décrites ci-dessous (chien est un objet de typeChien) :
— chien.donne_nom() qui renvoie la valeur de l'attributnom;
— chien.donne_poids() qui renvoie la valeur de l'attributpoids;
— chien.machouille(jouet) qui renvoie son argument, la chaine de caractèresjouet, privé de son
dernier caractère;
— chien.aboie(nb_fois) qui renvoie la chaine'Ouaf' * nb_fois , où nb_fois est un entier passé
en argument;
— chien.mange(ration) qui modifie l'attributpoids en lui ajoutant la valeur de l'argumentration
(de type float).
On ajoute les contraintes suivantes concernant la méthodemange :
— on vérifiera que la valeur deration est comprise entre 0 (exclu) et un dixième du poids du chien
(inclus),
— la méthode renverraTrue si ration satisfait ces conditions et que l'attributpoids est bien modifié,
False dans le cas contraire.
Exemples :
1 >>> medor = Chien ( ' Medor ' , 12.0)
2 >>> medor . do nn e_ no m ()
3 ' Medor '
4 >>> medor . d o n n e _ p o i d s ()
5 12.0
6 >>> medor . m a c h o u i l l e ( ' baton ')
7 ' bato '
8 >>> medor . aboie (3)
9 ' O u a f O u a f O u a f '
10 >>> medor . mange (2.0)
11 False
12 >>> medor . mange (1.0)
13 True
14 >>> medor . d o n n e _ p o i d s ()
15 13.0
16 >>> medor . mange (1.3)
17 True
T. Rahobisoa 9/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
Compléter le code de la classeChien ci-dessous :
1 class Chien :
2 def __init__ ( self , nom , poids ) :
3 self .... = nom
4 self .... = poids
5
6 def do nn e_ no m ( self ) :
7 return self ....
8
9 def ...( self ) :
10 return self ....
11
12 def m a c h o u i l l e ( self , jouet ) :
13 resultat = " "
14 for i in range (...) :
15 resultat += jouet [...]
16 return ...
17
18 def ...( self , ...) :
19 ...
20
21 def ...( self , ration ) :
22 if ...:
23 ...
24 return True
25 else :
26 return ...
27
28
29 # Tests
30 medor = Chien ( ' Medor ' , 12.0)
31 assert medor . do nn e_ no m () == ' Medor '
32 assert medor . d o n n e _ p o i d s () == 12.0
33 assert medor . m a c h o u i l l e ( ' baton ') == ' bato '
34 assert medor . aboie (3) == ' O u a f O u a f O u a f '
35 assert not medor . mange (2.0)
36 assert medor . mange (1.0)
37 assert medor . d o n n e _ p o i d s () == 13.0
38 assert medor . mange (1.3)
T. Rahobisoa 10/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
Exercice 12 : Trains
On souhaite dans cet exercice créer une classeTrain permettant de relier des objets de typeWagon.
Un objet de typeWagon possède deux attributs :
- un contenu contenu de typestr,
- un lien vers le wagon suivant suivant de typeWagon.
On inclut aussi deux méthodes permettant d'afficher le wagon dans la console ou sous forme d'une chaine
de caractère.
Un objet de la classeTrain possède deux attributs :
- premier contient son premier wagon (de type Wagon) ou None si le train est vide (il n'y a que la
locomotive),
- nb_wagons (de type int) contient le nombre de wagons attachés à la locomotive.
Lors de sa création, un objet de typeTrain sera toujours vide.
Les méthodes de la classeTrain sont présentées ci-dessous (train est un objet de type Train) :
1. train.est_vide() renvoie True si train est vide (ne comporte aucun wagon),False sinon;
2. train.donne_nb_wagons() renvoie le nombre de wagons de train;
3. train.transporte_du(contenu) détermine si train transporte du contenu (une chaine de carac-
tères). Renvoie True si c'est le cas,False sinon;
4. train.ajoute_wagon(wagon) ajoute un wagon à la fin du train. On passe en argument le wagon à
ajouter;
5. train.supprime_wagon_de(contenu) prend en argument une chaine de caractères contenu et sup-
prime le premier wagon de contenu du train. Si le train est vide ou ne comporte aucun wagon de
contenu, la méthode renvoieFalse. S'il en contient un et que celui-ci est effectivement supprimé,
la méthode renvoieTrue.
On inclut là-aussi aussi deux méthodes permettant d'afficher le train dans la console ou sous forme d'une
chaine de caractères.
Exemples :
- Création d'un train vide :
>>> train = Train ()
- Ajout de wagons :
>>> w1 = Wagon ( ' ble ')
>>> train . a j o u t e _ w a g o n ( w1 )
>>> w2 = Wagon ( ' riz ')
>>> train . a j o u t e _ w a g o n ( w2 )
>>> train . a j o u t e _ w a g o n ( Wagon ( ' sable ') )
>>> train
' L o c o m o t i v e - Wagon de ble - Wagon de riz - Wagon de sable '
- Description du train :
>>> train . est_vide ()
False
>>> train . d o n n e _ n b _ w a g o n s ()
3
>>> train . t r a n s p o r t e _ d u ( ' ble ')
True
>>> train . t r a n s p o r t e _ d u ( ' materiel ')
False
T. Rahobisoa 11/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
- Suppression de wagon :
>>> train . s u p p r i m e _ w a g o n _ d e ( ' riz ')
True
>>> train
' L o c o m o t i v e - Wagon de ble - Wagon de sable '
>>> train . s u p p r i m e _ w a g o n _ d e ( ' riz ')
False
On pourra parcourir tous les wagons du train en utilisant les instructions ci-dessous :
wagon = self . premier
while wagon is not None :
wagon = wagon . suivant
En plusieurs occasions il faudra prendre soin de traiter séparément le cas du premier wagon et celui des
suivants.
Enfin, lors de la suppression d'un wagon, on se contentera de l'omettre en liant son wagon précédent à son
suivant. La figure ci-dessous illustre ainsi l'instruction train.supprime_wagon_de('riz') avant et après la
suppression.
Compléter le code ci-dessous :
1 class Train :
2 def __init__ ( self ) :
3 " C o n s t r u c t e u r "
4 self . premier = None
5 self . nb _w ag on s = ...
6
7 def est_vide ( self ) :
8 """ renvoie True si ce train est vide ( ne comporte aucun wagon ) ,
9 False sinon
10 """
11 return ...
12
13 def d o n n e _ n b _ w a g o n s ( self ) :
14 " Renvoie le nombre de wagons de ce train "
15 return ...
16
17 def t r a n s p o r t e _ d u ( self , contenu ) :
18 """ De te rm in e si ce train t r a n s p o r t e du { contenu } ( une chaine de
c a r a c t e r e s ) .
19 Renvoie True si c ' est le cas , False sinon
20 """
21 wagon = self . premier
T. Rahobisoa 12/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
22 while wagon is not None :
23 if wagon . contenu == ...:
24 return ...
25 ... = wagon ....
26 return ...
27
28 def a j o u t e _ w a g o n ( self , nouveau ) :
29 """ Ajoute un wagon a la fin de ce train .
30 L ' argument est le wagon a ajouter
31 """
32 if self . est_vide () :
33 self . premier = ...
34 else :
35 wagon = self . premier
36 while .... suivant is not None :
37 wagon = .... suivant
38 wagon . suivant = ...
39 self . nb _w ag on s = ...
40
41 def s u p p r i m e _ w a g o n _ d e ( self , contenu ) :
42 """ Supprime le premier wagon de { contenu }
43 Renvoie False si ce train ne contient pas de { contenu } ,
44 True si la s u p p r e s s i o n est ef fe ct ue e
45 """
46 # On parcourt le train afin de trouver le contenu
47 pr e ce de nt = None
48 wagon = self . premier
49 while wagon is not ... and wagon . contenu != ...:
50 p re ce de nt = wagon
51 wagon = wagon ....
52
53 if wagon is ...: # on a parcouru tout le train sans trouver le
contenu
54 return ...
55 if pr ec ed en t is ...: # le wagon supprime est le premier du
train
56 self . premier = wagon ....
57 else : # le wagon supprime n ' est pas le premier
58 p re ce de nt .... = wagon ....
59 self . nb _w ag on s -= ...
60 return ...
61
62 def __repr__ ( self ) :
63 " A ff ic ha ge dans la console "
64 c o n t e n u s _ w a g o n s = [ ' ']
65 wagon = self . premier
66 while wagon is not None :
67 c o n t e n u s _ w a g o n s . append ( str ( wagon ) )
68 wagon = wagon . suivant
69 return " L o c o m o t i v e " + " - " . join ( c o n t e n u s _ w a g o n s )
70
71 def __str__ ( self ) :
72 " C o n v e r s i o n en string "
73 return self . __repr__ ()
74
75
76 # Tests
77 train = Train ()
78 w1 = Wagon ( " ble " )
79 train . a j o u t e _ w a g o n ( w1 )
80 w2 = Wagon ( " riz " )
T. Rahobisoa 13/14 LP03 - Programmation objet
Terminale - Spécialité NSI IFS Singapour
81 train . a j o u t e _ w a g o n ( w2 )
82 train . a j o u t e _ w a g o n ( Wagon ( " sable " ) )
83 assert str ( train ) == ' L o c o m o t i v e - Wagon de ble - Wagon de riz - Wagon
de sable '
84 assert not train . est_vide ()
85 assert train . d o n n e _ n b _ w a g o n s () == 3
86 assert train . t r a n s p o r t e _ d u ( ' ble ')
87 assert not train . t r a n s p o r t e _ d u ( ' materiel ')
88 assert train . s u p p r i m e _ w a g o n _ d e ( ' riz ')
89 assert str ( train ) == ' L o c o m o t i v e - Wagon de ble - Wagon de sable '
90 assert not train . s u p p r i m e _ w a g o n _ d e ( ' riz ')
T. Rahobisoa 14/14 LP03 - Programmation objet

## Modularite

### Modularite

Terminale - Spécialité NSI IFS Singapour
Chapitre 10 - Modularité
Objectifs :
▷ Savoir utiliser des bibliothèques
▷ Exploiter leur documentation
▷ Créer des modules simples et les documenter.
1 Introduction
Laprogrammation modulaireconsiste à décomposer une grosse application en modules que l'on peut ensuite
améliorer et utiliser indépendamment dans d'autres applications.
Cette méthode réalise uneencapsulation comparable à celle de la programmation orientée objet.
Un module doit être conçu pour pouvoir être utilisé par d'autres utilisateurs comme une interface qui fournit
des données (math.pi, math.e...), des objets (structures de données comme les piles, les arbres, les graphes,
..., etc.) et des traitements (fonctions, méthodes), sans rentrer dans le code du module.
Il faut donc prévoir unedocumentation claire et complète.
2 Exemples
Nous avons déjà créé des modules en implémentant des listes, des piles, des files, des arbres et des graphes.
Python dispose d'une vaste bibliothèque de modules, certains sont fréquemennt utilisés commemath, random,
numpy, matplotlib, tkinter,..., etc..
2.1 Module simple
Un module simple est juste un fichier écrit en Python.
Exemple 1 :Turtle
▷ Importer le moduleturtle avec import turtle
▷ Repérer son emplacement sur le disque dur avecturtle.__file__
▷ Ouvrir le fichierturtle.py dans un éditeur et observer le texte en début de fichier
▷ Afficher la doc avecprint(turtle.__doc__)
Remarquez que turtle fait appel à d'autres modules. D'après vous, quel module gère l'interface graphique de
turtle?
T. Rahobisoa 1/4 LP04 - Modularité
Terminale - Spécialité NSI IFS Singapour
2.2 Module complexe
Les modules plus complexes sont des répertoires contenant de nombreux fichiers, parfois codés en C.
Exemple 2 :Numpy
▷ Importer le modulenumpy avec import numpy
▷ Repérer son emplacement sur le disque dur avecnumpy.__file__
▷ Ouvrir le fichiernumpy/__init__.py
▷ Regarder la documentation et l'afficher dans votre interpréteur Python
▷ Remarquez que le fichier__init__.py, qui est appelé lorsqu'on importe le modulenumpy n'est qu'un des
nombreux fichiers de ce module.
Certains modules sont incorporés (builtins) dans l'interpréteur Python.
Une fonction extraite d'un module connu sera en principe plus performante qu'une fonction programmée soi-
même. Elle a été optimisée et testée, et sera beaucoup plus rapide si elle est écrite en C (ce qui est le cas des
modules math et numpy par exemple).
3 Accès à la documentation d'un module
Testertouteslescommandessuivantesavecdesmodulesetfonctionsquevousutilisezrégulièrement.Parexemple
avec la fonctionrandint du module random.
▷ dir(nom_du_module) renvoie tous les attributs du module.
▷ nom_du_module.__doc__ renvoie la description du module (chaîne de caractères entrée en premières lignes
de code).
▷ nom_du_module.nom_de_la_fonction.__doc__ renvoie la description (ou la documentation ) d'une fonc-
tion (chaîne de caractères entrée en premières lignes).
▷ help(nom_du_module) génère et affiche une documentation constituée des descriptions du module et de
ses différentes classes et fonctions.
▷ Fonctionnement similaire avec les classes : la méthode__doc__ appliquée à une classe d'un module renvoie
la description de la classe et la fonctionhelp() affiche la description de la classe et de toutes ses méthodes.
▷ Après avoir faitimport sys , testersys.builtin_module_names qui permet d'obtenir la liste des modules
incorporés.
▷ Testeravecquelquesmodulesquevousavezimportés( random, turtle, tkinter,math,..., etc.): random.__doc__,
help(tkinter), turtle.goto.__doc__, help(math.tan), ...
T. Rahobisoa 2/4 LP04 - Modularité
Terminale - Spécialité NSI IFS Singapour
4 Documenter un module
La documentation d'un module est une chaîne de caractères située au début du module.
Toutes les fonctions du module sont également documentées par une chaîne de caractères située au début de la
fonction. Il n'y a pas de règle universelle pour écrire la documentation d'un code, mais on précise généralement
les préconditions et postconditions des fonctions.
Voici un exemple de fonction bien documentée :
1 def pgcd (a , b ) :
2 """ Calcule le pgcd de a et b
3 P a r a m e t r e s
4 - - - - - - - - - - - -
5 a : int ( entier q u e l c o n q u e )
6 b : int ( entier q u e l c o n q u e )
7 Renvoie
8 - - - - - - - - -
9 int : pgcd de a et de b """
10
11 while b != 0 :
12 a , b = b , a % b
13
14 return a
T. Rahobisoa 3/4 LP04 - Modularité
Terminale - Spécialité NSI IFS Singapour
5 A propos de l'importation
En Python, import module va charger et exécuter le fichier désigné, en généralmodule.py ou dans le cas d'un
module complexe, un fichier__init__.py.
5.1 Remarques
▷ module.__file__ renvoie l'emplacement de ce fichier
▷ import module définit alors un espace de noms, comme en POO
▷ Lesdonnées,classes,fonctionsdufichierimportésontaccessiblesavec module.donneesou module.fonction,...
▷ import module as md va importer le module en le renommantmd, afin de raccourcir les noms
5.2 Exemples
Quelques exemples de renommages bien connus :
▷ import numpy as np
▷ import matplotlib.pyplot as plt
▷ import tkinter as tk
5.3 import *
Attention, la ligne de code ci-dessous :
from module import *
va importer toutes les fonctions du module sans créer d'espace de noms.
Ce n'est généralement pas recommandé car si deux entités (classes, fonctions...) portent le même nom dans le
module et dans notre code, l'une des deux va être écrasée.
5.4 main
On peut aussi utiliser la ligne de code ci-dessous :
if __name__ == ' __main__ ' :
Lors d'un import, le fichier importé est exécuté, ce qui permet de charger ses variables, classes et fonctions en
mémoire. Dans le cas d'un module importé, la variable__name__ contient le nom du module.
Ce nom est égal à__main__ lorsque le module est le fichier principal, et pas lorsqu'il est importé.
Ainsi l'instruction conditionnelle précédente permet d'écrire des instructionsqui ne seront exécutées que
lorsqu'on lance le script en fichier principalet ne seront pas exécutées lors d'un import.
Vous allez maintenant appliquer tout cela dans leTP Immeubles .
T. Rahobisoa 4/4 LP04 - Modularité

## Notion de programme

### Notion de programme

Terminale - Spécialité NSI IFS Singapour
Chapitre 25 - Calculabilité, décidabilité
Objectifs :
▷ Comprendre que tout programme est aussi une donnée.
▷ Comprendre que la calculabilité ne dépend pas du langage de programmation utilisé.
▷ Montrer, sans formalisme théorique, que le problème de l'arrêt est indécidable.
1 Introduction
Comme nous l'avons vu en classe dePremière, un programme est la traduction électronique d'un algorithme
afin qu'il puisse être compris par une machine. Dans ce chapitre, nous allons montrer qu'un programme ne peut
pas toutcalculer ou décider.
L'indécidabilité est un concept fondamental en logique. Il a plusieurs sens. Au sens de la démonstration, il
signifie qu'on ne peut démontrer ni qu'une proposition est vraie ni qu'elle est fausse dans un système d'axiomes;
ici, le contenu sémantique ne permet d'affirmer ni que l'objet est une pipe ni qu'il n'en est pas une. Au sens de
la calculabilité, il signifie qu'il n'existe aucun algorithme capable de résoudre un problème (ici déterminer si
l'objet est une pipe ou non).
2 Notion de programme en tant que donnée
Les codes que nous manipulons ressemblent souvent à cela :
1 def accueil ( n ) :
2 for k in range ( n ) :
3 print ( " bonjour " )
Le programme s'appelleaccueil, et pour fonctionner il a besoin d'un paramètre, qui est un nombre entiern.
Voici comment nous pouvons représenter notre machineaccueil :
— son paramètre d'entrée :5
— sa sortie :bonjour affiché 5 fois
Maintenant, enregistrons le code suivant dans un fichiertest.py :
T. Rahobisoa 1/8 LP05 - Notion de programme
Terminale - Spécialité NSI IFS Singapour
1 def accueil ( n ) :
2 for k in range ( n ) :
3 print ( " bonjour " )
4
5 accueil (5)
Pour exécuter ce code, nous devons taper dans un terminal l'instruction suivante :python test.py
Ce qui donne :
Le programme utilisé est alors python, qui prend comme paramètre le programme test.py. Ce paramètre
test.py est un ensemble de caractères qui contient les instructions que le programmepython va interpréter.
L'illustration correspondante sera donc :
Mais nous pouvons aller encore plus loin. L'instructionpython test.py est saisie dans monTerminal Windows ,
qui lui-même est un programme appeléTerminal.
Et donc :
Conclusion :
Il n'y a donc aucun obstacle à considérerun programme comme une simple donnée, pouvant être reçue
en paramètre par un autre programme. (voire par lui-même!)
Ainsi, certains programmes utilisent comme données le code source d'autres programmes.
Exemples :
— unsystèmed'exploitation(comme Linux ouWindows)estunprogrammequiéxecuted'autresprogrammes
(traitement de texte, tableur, ...,etc.).
— l'interpréteur Python, est un programme qui traduit le code source de votre programme Python en ins-
tructions exécutables par la machine : du langage machine (cf. cours dePremière sur l'architecture de
Von Neumannet le langage assembleur).
T. Rahobisoa 2/8 LP05 - Notion de programme
Terminale - Spécialité NSI IFS Singapour
3 Décidabilité
3.1 Mon programme va-t-il s'arrêter ?
Considérons le programme suivant :
1 def co un td ow n ( n ) :
2 while n != 0:
3 print ( n )
4 n = n - 1
5 print ( " fini " )
En l'observant attentivement, on peut prévoir quecountdown(10) affichera les nombres de10 à 1 avant d'écrire
"fini". Puis le programme s'arrêtera.
Mais que va provoquercountdown(10.8)?
Comme la variablen ne sera jamais égale à0, le programme va rentrer dans uneboucle infinie, il ne s'arrêtera
jamais! On a pu prévoir ceci en analysant attentivement le code du programme. On a ainsi remarqué qu'une
variable n non entière provoquerait une boucle infinie.
Question :Est-ce qu'un programme d'analyse de programmes aurait pu faire cela à ma place?
3.2 Une machine pour prédire l'arrêt ou non d'un programme
Après tout, un programme est une suite d'instructions (le code source), et peut donc être le paramètre d'entrée
d'un autre programme qui l'analyserait. Un tel programme (appelons-lehalt) prendrait en entrées :
— un paramètre prog (le code-source du programme)
— un paramètre x, qui serait le paramètre d'entrée deprog.
L'instruction halt(prog,x) renverrait True si prog(x) s'arrête, et False si prog(x) ne s'arrête pas.
Exemples :
— halt(countdown,10) renverrait True.
— halt(countdown,10.8) renverrait False.
T. Rahobisoa 3/8 LP05 - Notion de programme
Terminale - Spécialité NSI IFS Singapour
Tentative d'écriture dehalt en Python :
1 def halt ( prog , x ) :
2 if " prog ( x ) s ' arrete " : # code a d e t e r m i n e r
3 return True
4 else :
5 return False
Nous en resterons là pour l'instant dans l'écriture de ce programme. Nous allons nous en servir pour construire
d'autres programmes.
3.3 Le problème de l'arrêt
Considérons le programme suivant :
1 def sym ( prog ) :
2
3 if halt ( prog , prog ) == True :
4 while True :
5 print ( " vers l ' infini et au - dela ! " )
6 else :
7 return 1
On peut remarquer que le programmehalt est appelé avec comme paramètres(prog,prog), ce qui signifie que
prog se prend lui-même en paramètre. On rappelle que ce n'est pas choquant, un code source étant une donnée
comme une autre.
Ce programme sym reçoit donc en paramètre un programmeprog, et :
— va rentrer dans une boucle infinie siprog(prog) s'arrête.
— va renvoyer1 si prog(prog) ne s'arrête pas.
Problème :
Puisqu'un programme peut prendre en paramètre son propre code-source, que donnerait l'appel àsym(sym)?
Deux cas peuvent se présenter, suivant sihalt(sym, sym) renvoie True ou False.
T. Rahobisoa 4/8 LP05 - Notion de programme
Terminale - Spécialité NSI IFS Singapour
— cas n°1 : halt(sym, sym) renvoie True, ce qui signifie que sym(sym) devrait s'arrêter. Mais dans ce
cas-là, l'exécution desym(sym) rentre dans une boucle infinie. C'est unecontradiction!
— cas n°2 : halt(sym, sym) renvoie False, ce qui signifie quesym(sym) rentre dans une boucle infinie.
Mais dans ce cas-là, l'exécution desym(sym) se termine correctement et renvoie la valeur1. C'est une
contradiction!
3.4 Conclusion
Nous venons de prouver que notre programmehalt, censé prédire si un programmeprog peut s'arrêter sur une
entrée x, ne peut pas exister!
Ce résultat théorique, d'une importance cruciale, s'appelle leproblème de l'arrêt.
Problème de l'arrêt
Il ne peut pas exister de programme universel qui prendrait en entrées :
— un programme P
— une entrée E de ce programmeP
et qui déterminerait si ce programmeP, lancé avec l'entréeE, va s'arrêter ou non.
Ce résultat a été démontré parAlan Turingen 1936, dans un article intitulé«On computable numbers, with an
application to the Entscheidungsproblem».
T. Rahobisoa 5/8 LP05 - Notion de programme
Terminale - Spécialité NSI IFS Singapour
Pour sa démonstration, il présente un modèle théorique de machine capable d'exécuter des instructions basiques
sur un ruban infini, lesmachines de Turing.
À la même époque, le mathématicienAlonzo Churchdémontre lui aussi cethéorème de l'arrêt, mais par un
moyen totalement différent, en inventant lelambda-calcul.
Tous deux mettent ainsi un terme au rêve du mathématicien allemandDavid Hilbert, qui avait en 1928 posé la
question de l'existence d'un algorithme capable de répondre «oui» ou «non» à n'importe quel énoncé mathéma-
tique posé sous forme décisionnelle («un triangle rectangle peut-il être isocèle?», «existe-t-il un nombre premier
pair?»).
Cette question, appeléeproblème de la décision, ouEntscheidungsproblem en allemand, est définitivement
tranchée par le problème de l'arrêt : un tel théorème ne peut pas exister, puisque par exemple, aucun
algorithme ne peut répondre «oui» ou «non» à la question«ce programme va-t-il s'arrêter?».
Définition
Un problème de décision est ditdécidable s'il existe un algorithme, une procédure mécanique qui se
termine en un nombre fini d'étapes, qui le décide, c'est-à-dire qui réponde par oui ou par non à la question
posée par le problème.
S'il n'existe pas de tels algorithmes, le problème est ditindécidable. Par exemple, le problème de l'arrêt
est indécidable.
4 Calculabilité
Le problème de l'arrêt est ditindécidable car la fonction qui le résout (notre programmehalt) n'est pas
calculable.
La notion decalculabilité date de 1936, il s'agit de savoir ce qui peut être calculé par un ordinateur, et donc
permet de voir les limites des problèmes que peuvent résoudre les ordinateurs.
Propriété
On dira qu'une fonction estcalculable si elle peut être programmée dans l'un ou l'autre des langages
de programmation usuels.
En Première et Terminale, nous utilisons le langage Python comme témoin : une fonction est calculable
si on peut la programmer en Python.
Il existe d'autres modèles de calcul, comme leλ-calcul, les fonctions récursives, les machines de Turing, que
nous ne développerons pas ici, et qui ne font pas partie des attendus du programme.
La thèse deChurch postule que tous ces modèles de calcul sont équivalents : une fonction calculable pour un
modèle l'est pour un autre. Cela nous permet d'utiliser le modèle des fonctions programmables en Python sans
perdre de généralité.
On peut calculer beaucoup de choses avec un ordinateur comme le nombreπ, les nombres rationnels,
√
2,
√
3,
..., etc.
Cependant, il a été prouvé que certains problèmes n'étaient pas calculables comme par exemple :
— Savoir si un énoncé mathématique est un théorème ou pas (s'il peut être démontré).
— Créer un programme qui prend un programme en entrée, et qui indiquera si le programme s'arrête ou
pas : le problème de l'arrêt.
Il s'agit de problèmes dedécidabilité.
En résumé, voir la vidéo suivante
T. Rahobisoa 6/8 LP05 - Notion de programme
Terminale - Spécialité NSI IFS Singapour
5 Exercices
Exercice 1 :Vocabulaire
1. Donner deux exemples qui montrent pourquoi un programme est aussi une donnée.
2. Quelle est la différence entre la calculabilité et la décidabilité d'un problème?
3. Faire des recherches et donner des exemples de problèmesdécidables.
4. Faire des recherches e dtonner des exemples de problèmesindécidables.
Exercice 2 :Racine carrée
On définit ci-dessous une fonctionracine_carree :
1
2 def r a c i n e _ c a r r e e (n , pr ec is io n =1 E -2) :
3 """ Re ch er ch e d ' une racine carree par une methode d i c h o t o m i q u e
4 P a r a m e t r e s :
5 - - - - - - - - - - - -
6 n : float
7 le nombre dont on re ch er ch e la racine
8 pr ec is i on : float 0.01 par defaut
9 pr ec is i on du calcul du carre
10
11 Retour :
12 - - - - - - - -
13 float : la racine carree de n
14 """
15 gauche , droite , milieu = 0 , n , n
16 while abs ( milieu ** 2 - n ) > p re ci si on :
17 milieu = ( gauche + droite ) / 2
18 if milieu ** 2 - n > 0:
19 droite = milieu - pr ec is io n
20 else :
21 gauche = milieu + pr ec is io n
22 return milieu
1. Expliquer pourquoi il est nécessaire d'utiliser une précision dans ce calcul?
2. Expliquer la ligne :while abs(milieu ** 2 - n) > precision :
3. Pourquoi peut-on qualifier cet algorithme de dichotomique?
Exercice 3 :Entiers
1. Implémenter en Python deux fonctions :
▷ est_pair(n) : renvoie True si le nombre entiern est pair, False sinon.
▷ est_premier(n) : renvoie True si le nombre entiern est premier, False sinon.
2. Tester ces fonctions avec un entier négatif et un nombre décimal. Que se passe-t-il?
3. Tester ces fonctions avec des petites entrées, puis avec des grandes pour voir si ces algorithmes seraient
utilisables en pratique.
Exercice 4 :Non-décidabilité de l'arrêt
1. Pourquoi dit-on que le problème de l'arrêt est indécidable?
Supposons qu'il existe une fonction calculabletermine(fonction, données) qui prend 2 arguments :
— une fonction,
— et des données d'entrée pour cette fonction
T. Rahobisoa 7/8 LP05 - Notion de programme
Terminale - Spécialité NSI IFS Singapour
et qui renverraTrue si le programme termine etFalse s'il entre dans une boucle infinie.
On définit les deux fonctions suivantes :
1 def fo nc ti on 1 ( n ) :
2 if n % 3 != 0:
3 return True
4 else :
5 return False
6
7 def fo nc ti on 2 ( n ) :
8 while n % 3 != 0:
9 print ( " True " )
10 print ( " False " )
2. Que renverront les appels ci-dessous?
1 termine ( fonction1 ,7)
2 termine ( fonction1 ,9)
3 termine ( fonction2 ,7)
4 termine ( fonction2 ,9)
Justifier vos réponses.
3. On définit une fonctiontest_sur_soi.
1 def t e s t _ s u r _ s o i ( pr og ra mm e ) :
2 if termine ( programme , pr og ra mm e ) :
3 while True :
4 pass # boucle infinie
Que se passe-t-il si on appelletest_sur_soi sur elle-même :test_sur_soi(test_sur_soi)?
Exercice 5 :Machines de Turing
1. Consulter le site suivant et noter les grands noms et repères historiques de la calculabilité.
2. Visionner la vidéo surAlan Turinget faire un résumé de sa vie en quelques lignes.
3. Si vous avez du temps, vous pouvez également visionner le filmImitation Gamequi dure 2 heures!
T. Rahobisoa 8/8 LP05 - Notion de programme
