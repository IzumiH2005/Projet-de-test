# Bases de données

## Modele relationnel

### 0. De la nécessité d'organiser le stockage de ses données

Lorsqu'une grande quantité de données doit être gérée, il faut savoir distinguer deux choses :

- la structure qui va sous-tendre l'ensemble de ces données, notamment les liens entre elles, les hiérarchies éventuelles,...
- le type de logiciel qui va aider à gérer ces données.

Par exemple, si je souhaite stocker toutes les températures relevées dans mon jardin tous les matins à 07h00, je sais que mes données seront des couples ```(date, temperature)``` . Éventuellement ces dates seront regroupées par mois, ou par saison... mais la structure des données sera quand même simple et linéaire.  
Pour gérer ces données, je peux : les écrire à la main dans mon agenda, créer un feuille de tableur avec Excel ou LibreOffice, utiliser une liste dans un IDE Python,...
Chaque méthode aura ses avantages et ses inconvénients.  

- Si le nombre de données à stocker devient très grand, est-ce que ma solution choisie pourra les gérer ?  (on peut par exemple méditer sur le cas du Royaume-Uni dont le comptage des patients positifs au Covid est devenu faux car il a dépassé les limites de leur feuille Excel)

- Est-ce que d'autres personnes que moi sont susceptibles de consulter ou modifier ces données, éventuellement en même temps que moi ?

- Si une donnée se retrouve à plusieurs endroits dans mes données, devrais-je aller modifier cette donnée partout où elle se trouve ou bien une seule fois ?

L'étude des Bases de Données tente d'apporter des réponses à toutes ces questions.

### 1. Le modèle relationnel

Le programme de Terminale NSI prévoit uniquement l'étude du **modèle relationnel**.

Théorisé en 1970 par le Britannique Edgard J. Codd, 
le modèle relationnel est à ce jour le modèle de base de données le plus utilisé, même si l'ère actuelle du Big Data tend à mettre en avant d'autres modèles non relationnels (nous en reparlerons).

    - Les données sont regroupées dans différentes **tables** (qu'on appellera plutôt **relations** et qui donnent son nom au modèle). Chaque relation contient des éléments directement en lien avec le sujet général de la table.
    - Autant que possible, des données identiques ne doivent pas se trouver dans des tables différentes : on évite la **redondance** des données.
    - Les données ne doivent pas contenir elles-mêmes d'autres données : on parle d'**atomicité** des données.

Un modèle relationnel est donc basé sur des... **relations**.

### 2. Première relation

Prenons l'exemple d'une bibliothèque dont la base de données possède une relation «livres» :

    - **relation**, ou **table** : c'est l'endroit où sont rangées les données. L'ordre des lignes (que l'on appelera des enregistrements) n'a pas d'importance.
    - **enregistrement**, ou **tuple**, ou **n-uplet**, ou **t-uplet**, ou **vecteur** : cela correspond à une ligne du tableau, et donc un ensemble de valeurs liées entre elles : l'auteur «Eric VUILLARD» a bien écrit le livre «L'Ordre du jour». 
    Il est **interdit** que deux enregistrements soient totalement identiques. 
    Le nombre d'enregistrements d'une relation s'appelle son **cardinal**.
    - **attribut** : c'est l'équivalent d'une colonne. Il y a dans notre relation un attribut «code», un attribut «Titre», etc.
    - **domaine** : le domaine désigne «le type» (au sens type ```Int```, ```Float```, ```String```).      
    L'attribut «Éditeur» est une chaîne de caractères, son domaine est donc ```String```.  
    Par contre l'attribut «ISBN» est un nombre de 13 chiffres, commençant manifestement par 978. Son domaine est donc ```Int```.
    - **schéma** : le schéma d'une relation est le regroupement de tous les attributs et de leur domaine respectif. Ici notre schéma serait : 
    ```((Code, Entier), (Titre, Chaîne de caractères), (Auteur, Chaîne de caractères), (Éditeur, Chaîne de caractères), (ISBN, Entier))```

### 3. Clé Primaire

Une clé primaire est un attribut (ou une réunion d'attributs) **dont la connaissance suffit à identifier avec certitude un unique enregistrement**.

Par exemple, la clé primaire de la relation des personnes nées en France pourrait être leur numéro de Sécurité Sociale.

 Observons, dans notre relation précédente, ce qui peut être une clé primaire et ce qui ne peut pas l'être.

- Titre : cet attribut pourrait jouer le rôle de clé primaire. En effet, notre table ne contient pas deux livres ayant le même titre.
- Auteur : cet attribut pourrait jouer le rôle de clé primaire. En effet, notre table ne contient pas deux livres ayant le même auteur.
- Éditeur : cet attribut ne peut **pas** jouer le rôle de clé primaire. En effet, la donnée de l'attribut «Actes Sud» renvoie vers 4 livres différents.
- ISBN : (International Standard Book Number) cet attribut est un numéro unique spécifique à chaque livre : il peut jouer le rôle de clé primaire.
- Code : cet attribut pourrait jouer le rôle de clé primaire. En effet, notre table ne contient pas deux livres ayant le même code.

Alors, quelle clé primaire choisir ? Il faut pour cela réfléchir à ce que deviendrait notre relation si elle contenait 1000 livres au lieu de 10. Il est fort probable que deux livres aient alors le même auteur : l'attribut «Auteur» ne serait donc plus une clé primaire. 
Il peut arriver aussi que deux livres aient le même titre : l'attribut «Titre» n'est donc pas une bonne clé primaire.

Par définition, l'attribut «ISBN» pourrait jouer le rôle de clé primaire.

Quant à l'attribut «Code», il s'agit sans doute d'une nomenclature «maison» correspondant à une étiquette collée sur la tranche des livres : c'est donc une clé primaire qu'on qualifiera d'«artificielle».  

:warning: **Attention** :warning:  
Il ne peut pas y avoir deux clés primaires dans une table. La clé primaire choisie ici serait sans aucun doute l'attribut «Code».

### 4. D'autres relations

Ajoutons maintenant les relations ci-dessous :

 **Relation «Emprunts»** 

| id_emprunteur | date       | Nom    | Prénom | titre             | auteur          | code |
|---------------|------------|--------|--------|-------------------|-----------------|------|
| 845           | 12/10/2020 | DURAND | Michel | Au revoir là-haut | Pierre LEMAITRE | 942  |
| 125           | 13/10/2020 | MARTIN | Jean   | Pas pleurer       | Lydie SALVAYRE  | 1023 |
| 125           | 13/10/2020 | MARTIN | Jean   | Boussole          | Mathias ENARD   | 486  |

 **Relation «Emprunteurs»** 

| id_emprunteur | Nom    | Prénom | 
|---------------|--------|--------|
| 129           | DULAC | Marcel  | 
| 845           | DURAND | Michel |
| 125           | MARTIN | Jean   |

L'attribut «id_emprunteur» est une clé primaire de la relation «Emprunteurs».

**Notion de clé étrangère** 

Y-a-t-il une clé primaire dans la relation «Emprunts» ? 

«id_emprunteur» est bien une clé primaire (d'«Emprunteurs») mais ne peut pas être une clé primaire d'«Emprunts», car une personne peut prendre plusieurs livres à la fois : on dit que c'est une **clé étrangère**. 

    Une clé étrangère est une clé primaire d'une autre relation.

«code» est aussi une clé étrangère : c'est une clé primaire (de la relation «livres») mais elle ne peut pas jouer le rôle de clé primaire pour la relation emprunt, car un même livre pourra être pris à différentes dates.

Une clé primaire pourrait alors être la combinaison («date», «code»). En effet, aucun livre ne pouvant être emprunté deux fois le même jour, la connaissance de «date» et «code» suffit à identifier n'importe quel enregistrement.

### 5. Redondance des données

La relation «Emprunts» contient des informations qui sont déjà disponibles dans d'autres relations : on dit qu'elle est **redondante**, et c'est quelque chose qu'il faut éviter. À la fois pour des raisons d'espace de stockage mais aussi de cohérence : si une modification doit être faite (un emprunteur change de prénom), cette modification ne doit être faite qu'à un seul endroit de notre base de données.

Une version non-redondante de la relation «Emprunteurs» serait donc celle-ci :

**Relation «Emprunts»** 

| id_emprunteur | date       | code |
|---------------|------------|------|
| 845           | 12/10/2020 | 942  |
| 125           | 13/10/2020 | 1023 |
| 125           | 13/10/2020 | 486  |

### 6. Les 3 contraintes d'intégrité

Tout attribut d'un enregistrement doit respecter le domaine indiqué dans le schéma relationnel.

Attention, certains domaines sont subtils. Par exemple, si une relation possède un attribut "Code Postal", le domaine de cet attribut devra être ```String``` plutôt que ```Entier``` . Dans le cas contraire, un enregistrement possédant le code postal ```03150``` serait converti en ```3150``` (car pour les entiers, 03150 = 3150). Or le code postal ```3150``` n'existe pas.

    Tout enregistrement est unique.  
    Cette contrainte est assurée par l'existence obligatoire d'une clé primaire.

Cette clé primaire est souvent créée de manière artificielle (voir ```id_emprunteurs```  dans la table ci-dessus par exemple).

    La cohérence entre les différentes tables d'une base de données est assurée par les clés étrangères : dans une table, la valeur d'un attribut qui est clé étrangère doit obligatoirement pouvoir être retrouvée dans la table dont cet attribut est clé primaire.

Par exemple, la relation «Emprunts_v2» ci-dessous n'est pas valable :

**Relation «Emprunts_v2»** 

| id_emprunteur | date       | code |
|---------------|------------|------|
| 845           | 12/10/2020 | 942  |
| 125           | 13/10/2020 | 1023 |
| 125           | 13/10/2020 | **511**  |

En effet, le code 511 (clé étrangère de ma table «Emprunts_v2») ne correspond à aucun enregistrement dans la table dont il est clé primaire (la table «Livres») :

Il n'y a pas de code 511, donc ma relation «Emprunts_v2» ne respecte pas la contrainte de référence, et provoquerait une erreur du SGBD.

### 7. Représentation usuelles des bases de données en modèle relationnel

Considérons la base de données Tour de France 2020, contenant les relations suivantes :
(d'après une idée de Didier Boulle)

**relation Équipes**

| codeEquipe | nomEquipe                      |
|------|-----------------------------|
| ALM  |  AG2R La Mondiale           |
| AST  |  Astana Pro Team            |
| TBM  |  Bahrain - McLaren          |
| BOH  |  BORA - hansgrohe           |
| CCC  |  CCC Team                   |
| COF  |  Cofidis, Solutions Crédits |
| DQT  |  Deceuninck - Quick Step    |
| EF1  |  EF Pro Cycling             |
| GFC  |  Groupama - FDJ             |
| LTS  |  Lotto Soudal               |
| ...  | ...                         |

    Le schéma relationnel de cette table sera fréquemment donné sous cette forme :  
    Equipes ( codeEquipe  ```String```,  nomEquipe ```String``` ) 

    Notez le soulignement sous le mot «codeEquipe», qui signifie que cet attribut est une clé primaire. 
    Les clés étrangères, lorsqu'elles existent, peuvent être signalées par une astérisque * ou un dièse #.

**relation Coureurs**

| dossard | nomCoureur  | prénomCoureur | codeEquipe |
|---------------|-------------|---------------|------------|
| 141           | LÓPEZ       | Miguel Ángel  | AST        |
| 142           | FRAILE      | Omar          | AST        |
| 143           | HOULE       | Hugo          | AST        |
| 11            | ROGLIČ      | Primož        | TJV        |
| 12            | BENNETT     | George        | TJV        |
| 41            | ALAPHILIPPE | Julian        | DQT        |
| 44            | CAVAGNA     | Rémi          | DQT        |
| 45            | DECLERCQ    | Tim           | DQT        |
| 121           | MARTIN      | Guillaume     | COF        |
| 122           | CONSONNI    | Simone        | COF        |
| 123           | EDET        | Nicolas       | COF        |
| …             | …           | …             | …          |

Schéma : 
Equipes ( dossard  ```Int```,  nomCoureur ```String```,  prénomCoureur ```String```,   codeEquipe* ```String``` ) 

**relation Étapes**

| numéroEtape | villeDépart | villeArrivée      | km  |
|-------------|-------------|-------------------|-----|
| 1           | Nice        | Nice              | 156 |
| 2           | Nice        | Nice              | 185 |
| 3           | Nice        | Sisteron          | 198 |
| 4           | Sisteron    | Orcières-Merlette | 160 |
| 5           | Gap         | Privas            | 198 |
| ...         | ...         | ...               | ... |

Schéma : 
Étapes ( numéroEtape  ```Int```,  villeDépart ```String```,  villeArrivée ```String```,   km ```Int``` ) 

**relation Temps**

| dossard | numéroEtape | tempsRéalisé |
|:-------------:|:-----------:|:------------:|
| 41            | 2           | 04:55:27     |
| 121           | 4           | 04:07:47     |
| 11            | 5           | 04:21:22     |
| 122           | 5           | 04:21:22     |
| 41           | 4           | 04:08:24     |
| ...           | ...         | ...          |

Schéma : 
Temps ( dossard*  ```Int```,  numéroEtape *  ```Int```,  tempsRéalisé ```String```) 

Remarquez que la clé primaire de cette relation est le couple dossard-numéroEtape.

    Fréquemment, on présentera l'ensemble des renseignements d'un modèle relationnel sous forme d'un diagramme qui synthétise la composition des différentes tables et les relations entre elles.
    
    
    

---

### Bibliographie

- Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
- Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.
- Cours d'Olivier Lécluse, https://lecluseo.frama.io/leclusemaths/nsi/NSI_T/bdd/modrel/
- https://www.procyclingstats.com/

---

### Exercices sur le modèle relationnel

*(d'après Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.)*

    Deux relations modélisent la flotte de voitures d'un réseau de location de voitures.

    **Agences**

    | id_agence | ville     | département |
    |-----------|-----------|-------------|
    | 1         | Paris     | 75          |
    | 2         | Lyon      | 69          |
    | 3         | Marseille | 13          |
    | 4         | Aubagne   | 13          |

    **Voitures**

    | id_voiture | marque  | modèle | kilométrage | couleur | id_agence |
    |------------|---------|--------|-------------|---------|-----------|
    | 1          | Renault | Clio   | 12000       | Rouge   | 2         |
    | 2          | Peugeot | 205    | 22000       | Noir    | 3         |
    | 3          | Toyota  | Yaris  | 33000       | Noir    | 3         |

    

    1. Combien la relation ```Voitures``` comporte-t-elle d'attributs ?
    2. Que vaut son cardinal ?
    3. Quel est le domaine de l'attribut ```id_agence```  dans la relation ```Voitures``` ?
    4. Quel est le schéma relationnel de la relation ```Agences ``` ?
    5. Quelle est la clé primaire de la relation ```Agences ``` ?
    6. Quelle est la clé primaire de la relation ```Voitures ``` ?
    7. Quelle est la clé étrangère de la relation ```Voitures ``` ?

    

    Reprenons la base Tour de France 2020 vue en cours :

    **relation Équipes**

    | codeEquipe | nomEquipe                      |
    |------|-----------------------------|
    | ALM  |  AG2R La Mondiale           |
    | AST  |  Astana Pro Team            |
    | TBM  |  Bahrain - McLaren          |
    | BOH  |  BORA - hansgrohe           |
    | CCC  |  CCC Team                   |
    | COF  |  Cofidis, Solutions Crédits |
    | DQT  |  Deceuninck - Quick Step    |
    | EF1  |  EF Pro Cycling             |
    | GFC  |  Groupama - FDJ             |
    | LTS  |  Lotto Soudal               |
    | ...  | ...                         |

    **relation Coureurs**

    | dossard | nomCoureur  | prénomCoureur | codeEquipe |
    |---------------|-------------|---------------|------------|
    | 141           | LÓPEZ       | Miguel Ángel  | AST        |
    | 142           | FRAILE      | Omar          | AST        |
    | 143           | HOULE       | Hugo          | AST        |
    | 11            | ROGLIČ      | Primož        | TJV        |
    | 12            | BENNETT     | George        | TJV        |
    | 41            | ALAPHILIPPE | Julian        | DQT        |
    | 44            | CAVAGNA     | Rémi          | DQT        |
    | 45            | DECLERCQ    | Tim           | DQT        |
    | 121           | MARTIN      | Guillaume     | COF        |
    | 122           | CONSONNI    | Simone        | COF        |
    | 123           | EDET        | Nicolas       | COF        |
    | …             | …           | …             | …          |

    **relation Étapes**

    | numéroEtape | villeDépart | villeArrivée      | km  |
    |-------------|-------------|-------------------|-----|
    | 1           | Nice        | Nice              | 156 |
    | 2           | Nice        | Nice              | 185 |
    | 3           | Nice        | Sisteron          | 198 |
    | 4           | Sisteron    | Orcières-Merlette | 160 |
    | 5           | Gap         | Privas            | 198 |
    | ...         | ...         | ...               | ... |

    **relation Temps**

    | dossard | numéroEtape | tempsRéalisé |
    |:-------------:|:-----------:|:------------:|
    | 41            | 2           | 04:55:27     |
    | 121           | 4           | 04:07:47     |
    | 11            | 5           | 04:21:22     |
    | 122           | 5           | 04:21:22     |
    | ...           | ...         | ...          |

    

    1. Quel temps a réalisé Guillaume MARTIN sur l'étape Sisteron / Orcières-Merlette ?
    2. À l'arrivée à Privas, qui est arrivé en premier entre Primož ROGLIČ et Simone CONSONNI ?

## Langage SQL

### Exercices SQL débranchés

*(d'après Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.)*

    On veut créer une base de données ```baseHopital.db```  qui contiendra les trois tables suivantes :

    |  | Patients |
    |-----|----|
    | id | ```Int```  |
    | nom | ```Text```  |
    | prenom | ```Text```  |
    | genre | ```Text```  |
    | annee_naissance | ```Int```  |

    |  | Ordonnances |
    |-----|----|
    | code | ```Int```  |
    | id_patient | ```Int```  |
    | matricule_medecin  | ```Int```  |
    | date_ord | ```Text```  |
    | medicaments | ```Text```  |

    |  | Medecins |
    |-----|----|
    | matricule | ```Int```  |
    | nom_prenom | ```Text```  |
    | specialite | ```Text```  |
    | telephone | ```Text```  |

    On suppose que les dates sont données sous la forme ```jj-mm-aaaa```.

    On donne le diagramme relationnel de cette base :
    
    
    **Q0.** Écrire le schéma relationnel de la table Ordonnances. On soulignera les clés primaires et marquera d'un # les clés étrangères.

    
        

    **Q1.** (HP) Donner les commandes SQL permettant de créer ces tables.

    
           

    **Q2.** Mme Anne Wizeunid, née en 2000 et demeurant 3 rue des Pignons Verts 12345 Avonelit doit être enregistrée comme patiente numéro 1. Donner la commande SQLite correspondante.

    
           

    **Q3.** Le patient numéro 100 a changé de prénom et s'appelle maintenant "Alice". Donner la commande SQLite modifiant en conséquence ses données.

    
           

    **Q4.** Par souci d'économie, la direction décide de se passer des médecins spécialisés en épidémiologie. Donner la commande permettant de supprimer leurs fiches.
    
    
           

    **Q5.**  Donner la liste des patient(e)s ayant été examiné(e)s par un(e) psychiatre en avril 2020.

    _basé sur le travail de G.Viateau (Bayonne)_

    On considère ci-dessous le schéma de la base de données du stock d'un supermarché :

    

    **Q1**. Quelle requête SQL donne le prix d'achat du produit dont le ```nom_court``` est «Liq_Vaiss_1L» ?

    
            

    **Q2**. Quelle requête donne l'adresse, le code postal et la ville du fournisseur dont le nom est «Avenir_confiseur» ?

    
        
    

    **Q3**. Quelle requête donne les produits étant en rupture de stock ?

    
            

    **Q4**. Quelle requête donne la liste de toutes les ampoules vendues en magasin ? On pourra faire l'hypothèse que le nom du produit contient le mot «ampoule»

    
            

    **Q5**. Quelle requête permet d'avoir le prix moyen de ces ampoules ?

    
            

    **Q6**. Quelle requête permet d'identifier le produit le plus cher du magasin ?

    
            

    **Q7**. Quelle requête renvoie les noms des produits dont la date de péremption est dépassée ? _(on pourra utiliser la fonction SQL ```NOW()``` qui renvoie la date actuelle )_

    Exercice 1 du sujet Amérique du Nord J1 2022

    Exercice 4 du sujet Centres Étrangers J1 2022

    Exercice 4 du sujet Métropole J2 2022

    Exercice 2 du sujet La Réunion J2 2022
ex3J1AN2024">"

    Exercice 3 du sujet Amérique du Nord J1 2024    

    **Partie A**

    

    

    

    

    

      
    Si vous souhaitez jouer avec ces flashcards, téléchargez le fichier flashcards.csv et utilisez le code ci-dessous :

    ```python linenums='1'
    import csv
    import time

    def charger(nom_fichier):
        with open(nom_fichier, 'r') as fichier:
            donnees = list(csv.DictReader(fichier, delimiter=';'))
        return donnees

    def choix_discipline(donnees):
        disciplines = []
        for i in range(len(donnees)):
            disc = donnees[i]['discipline']
            if not disc in disciplines:
                disciplines.append(disc)
        for i in range(len(disciplines)):
            print(i + 1, disciplines[i])
        num_disc = int(input('numéro de la discipline ? '))
        return disciplines[num_disc - 1]

    def choix_chapitre(donnees, disc):
        chapitres = []
        for i in range(len(donnees)):
            if donnees[i]['discipline'] == disc:
                ch = donnees[i]['chapitre']
                if not ch in chapitres:
                    chapitres.append(ch)
        for i in range(len(chapitres)):
            print(i + 1, chapitres[i])
        num_ch = int(input('numéro du chapitre ? '))
        return chapitres[num_ch - 1]

    def entrainement(donnees, disc, ch):
        for i in range(len(donnees)):
            if donnees[i]['discipline'] == disc and donnees[i]['chapitre'] == ch:
                print('QUESTION : ', donnees[i]['question'])
                time.sleep(5)
                print(donnees[i]['réponse'])
                time.sleep(1)

    flashcard = ...
    d = ...
    c = ...
    entrainement(...)

    ```

    {{
    correction(True,
    """
\"Correction Q6\" 
        ```python linenums='1'
        flashcard = charger('flashcards.csv')
        d = choix_discipline(flashcard)
        c = choix_chapitre(flashcard, d)
        entrainement(flashcard, d, c)
        ```

        Si vous souhaitez jouer avec ces flashcards, téléchargez le fichier flashcards.csv et utilisez le code ci-dessous :

        ```python linenums='1'
        import csv
        import time

        def charger(nom_fichier):
            with open(nom_fichier, 'r') as fichier:
                donnees = list(csv.DictReader(fichier, delimiter=';'))
            return donnees

        def choix_discipline(donnees):
            disciplines = []
            for i in range(len(donnees)):
                disc = donnees[i]['discipline']
                if not disc in disciplines:
                    disciplines.append(disc)
            for i in range(len(disciplines)):
                print(i + 1, disciplines[i])
            num_disc = int(input('numéro de la discipline ? '))
            return disciplines[num_disc - 1]

        def choix_chapitre(donnees, disc):
            chapitres = []
            for i in range(len(donnees)):
                if donnees[i]['discipline'] == disc:
                    ch = donnees[i]['chapitre']
                    if not ch in chapitres:
                        chapitres.append(ch)
            for i in range(len(chapitres)):
                print(i + 1, chapitres[i])
            num_ch = int(input('numéro du chapitre ? '))
            return chapitres[num_ch - 1]

        def entrainement(donnees, disc, ch):
            for i in range(len(donnees)):
                if donnees[i]['discipline'] == disc and donnees[i]['chapitre'] == ch:
                    print('QUESTION : ', donnees[i]['question'])
                    time.sleep(5)
                    print(donnees[i]['réponse'])
                    time.sleep(1)

        flashcard = charger('flashcards.csv')
        d = choix_discipline(flashcard)
        c = choix_chapitre(flashcard, d)
        entrainement(flashcard, d, c)

        ```
    """
    )
    }}

    **Partie B**
ex2J2AN2024">"

    Exercice 2 du sujet Amérique du Nord J2 2024    
ex3J2G12024">"

    Exercice 3 Partie B du sujet Centres Étrangers J2 2024    
ex2J2PO2025">"

    Exercice 2 du sujet Polynésie J2 2025    

    
    

    

    

    

    
    
    $

        
        ```champignon(```$\\underline{\\texttt{id}}$```, nom, #id_ordre, lamelle, couleur, chapeau_min, chapeau_max, pied_min, pied_max, #id_toxicite)``` 

        ```ordre(```$\\underline{\\texttt{id}}$```, nom, classe)```

        ```toxicite(```$\\underline{\\texttt{id_tox}}$```, type, effet)```  
    """
    )
    }}
ex3J1AN2026">"

    Exercice 3 du sujet Amérique du Nord J1 2026

      

    

    

      

    

    

    

    

    

    

    ```python
    def llsc_fin(tab, i):
        if ...:
            return ...
        max_len = 1
        for j in range(i):
            if tab[j] < ...:
                max_len = max(max_len, llsc_fin(tab, j)+1)
        return max_len

    def llsc_rec(tab):
        n = len(tab)
        return max([llsc_fin(tab, i) for i in range(n)]) 
    ```

    
    
    ```python
    def llsc_dyn(tab):
        n = len(tab)
        dyn = [1] * n
        for i in range(1, n):
            for j in range(i):
                if tab[j] < tab[i]:
                    dyn[i] = max(..., ...)
        return ...
    ```

### Exercices SQL interactifs

*Vous pourrez trouver de très nombreux exercices interactifs d'entraînement sur le site de Nicolas Reveret, à l'adresse https://nreveret.forge.apps.education.fr/exercices_bdd/*

    *Questions interactives à réaliser sur le site sqlzoo.net.*

    **Q1.** Travail sur SELECT, (base de données Nobel) :arrow_right: ici.

    
        

    **Q2.** Travail sur SUM et COUNT, (base de données World) :arrow_right: ici. (jusqu'à la question 5.)

    

    **Q3.** Travail sur JOIN, (base de données Euro2012) :arrow_right: ici.

    Gestion d'un réseau d'agences de location de voitures.   
    *D'après le travail de J. Le Coupanec (Académie de Rennes)*

    La base de données locations.db contient les tables ```Agences```,```Locations```, ```Vehicules```.
    

    {!{ sqlide titre="**Requête :**"  base="T4_Bases_de_donnees/4.2_Langage_SQL/data/locations.db" }!}

        **Q1**. Visualisez toute la relation ```Agences```

        

        **Q2**. Listez uniquement les noms des agences et de leur ville.

        

        **Q3**. Listez les noms des agences de la ville de Lorient

        

        **Q4**. Listez les noms des agences du département du Morbihan (code postal 56***) ainsi que les codes postaux en utilisant par exemple un ```WHERE LIKE```.

        **Q5**. Déterminez le nombre de voitures que vous possédez. 

        

        **Q6**. Déterminez l'âge minimum et maximum de vos véhicules.
        

        **Q7**. Quels sont la marque et le modèle de votre dernière acquisition qui date de trois mois ?
        

        **Q8**.  Quel est le kilométrage maximum des véhicules ?
        

        **Q9**.  Quel est le kilométrage moyen des véhicules ?
        

        **Q10**. Afficher toute la flotte de véhicules par ordre décroissant de kilométrage.

        **Q11**. Visualisez toute la relation Locations. 
        

        **Q12**. Déterminez le nombre de locations effectuées avec changement d'agence
        

        **Q13**. Déterminez le nombre total de kilomètres effectués durant les locations
        

        **Q14**. Listez toutes les locations en y associant les caractéristiques du véhicule
        

        **Q15**. Affichez le nom et l'immatriculation du véhicule ainsi que la date de la location et le kilométrage réalisé pour chacune des locations
        

        **Q16**. Affichez une seule fois le nom et l'immatriculation des véhicules ayant déjà été loués.
        
 

        **Q17**. Affichez les locations du véhicule immatriculé AB-224-BA en précisant le nom de l'agence de départ ainsi que la ville de départ dans l'ordre chronologique des locations.

    Championnat de France de Football 2015-2016

    *D'après le travail de J. Le Coupanec (Académie de Rennes)*
   
    La base de données soccer.db contient les tables ```Team```,```Match```, ```Event```, ```Player```.  

    

    {!{ sqlide titre="**Requête :**"  base="T4_Bases_de_donnees/4.2_Langage_SQL/data/soccer.db" }!}

    **Q1**. Combien d'équipes ont participé à ce championnat ?

    

    **Q2**. Listez les noms des clubs ainsi que leur date de création dans l'ordre chronologique de leur création.

    

    **Q3**. Combien de pénaltys ont été marqués ?

    

    **Q4**. Combien de pénaltys ont été sifflés ?

    

    **Q5**. Combien de cartons ont été distribués ? 

    

    **Q6**. Combien de buts ont été marqués ?
    

    **Q7**. Affichez tous les renseignements sur les 10 cartons rouges obtenus le plus rapidement pendant un match.

    

    **Q8**.  Donnez le nom du joueur qui a obtenu le carton rouge le plus rapidement.

    Cet exercice en ligne est proposé le Knight Lab de l'université américaine Northwerstern University.

    

    **Le point de départ de l'histoire** : un meurtre a été commis **dans la ville de SQL City le 15 janvier 2018.**

    À partir de ce point de départ et d'une base de données dont le diagramme est donné ci-dessous, il s'agit de trouver le meurtrier.

        Il est conseillé de travailler avec un Bloc-Notes ouvert à côté afin d'y coller les renseignements obtenus. Vous pouvez utiliser le champ de requêtes ci-dessous mais il est possible que des colonnes n'apparaissent pas. Vous pouvez aussi utiliser n'importe quel champ sur la la page officielle.

        {!{ sqlide titre="Tapez votre requête ci-dessous"  base="T4_Bases_de_donnees/4.2_Langage_SQL/data/sql-murder-mystery.db" }!}

        Copiez la requête 
        ```sql
        INSERT INTO solution VALUES (1, 'nom du meurtrier');
        SELECT value FROM solution;
        ```
        

        {!{ sqlide titre="dans le champ ci-dessous :"  base="T4_Bases_de_donnees/4.2_Langage_SQL/data/sql-murder-mystery.db" }!}

    Sur la page officielle, vous pouvez être guidés étape par étape jusqu'à la recherche du meurtrier (qui n'est pas la fin de l'énigme !)

    - Vous pouvez si vous le souhaitez télécharger la base sql-murder-mystery.db. 

    {{
    correction(True,
    """
\"Correction\" 
        Vous pouvez trouver des éléments de correction ici.
    """
    )
    }}

### 1. Permiers exemples

#### 1.1 Création d'une table 

```python
import sqlite3

#Connexion
connexion = sqlite3.connect('mynewbase.db')

#Récupération d'un curseur
c = connexion.cursor()

### ---- début des instructions SQL

#Création de la table
c.execute("""
    CREATE TABLE IF NOT EXISTS bulletin(
    Nom TEXT,
    Prénom TEXT,
    Note INT);
    """)

### ---- fin des instructions SQL

#Validation
connexion.commit()

#Déconnexion
connexion.close()

``` 

- Le fichier ```mynewbase.db``` sera créé dans le même répertoire que le fichier source Python. Si fichier existe déjà, il est ouvert et peut être modifié.
- ```IF NOT EXISTS``` assure de ne pas écraser une table existante qui porterait le même nom. Si une telle table existe, elle n'est alors pas modifiée.
- La nouvelle table peut être ouverte avec ```DB Browser``` pour vérifier sa structure et ses données.

#### 1.2 Insertion d'enregistrements dans la table
Les morceaux de code ci-dessous sont à positionner entre les balises ```# ---- début des instructions SQL```  et ```# ---- fin des instructions SQL```, **après** la commande de création de la table.

##### 1.2.1 Insertion d'un enregistrement unique
```python
c.execute('INSERT INTO bulletin VALUES ('Simpson', 'Bart', 17)')
``` 

Pensez à vérifier avec  ```DB Browser``` si les modifications sont effectives.

##### 1.2.2 Insertion d'un enregistrement unique avec variable
```python
data = ('Simpson', 'Maggie', 2)
c.execute('INSERT INTO bulletin VALUES (?,?,?)', data)
``` 

##### 1.2.3 Insertion de multiples enregistrements
```python
lst_notes = [ ('Simpson', 'Lisa', 19), ('Muntz', 'Nelson', 4), ('Van Houten', 'Milhouse', 12) ]

c.executemany('INSERT INTO bulletin VALUES (?, ?, ?)', lst_notes)
``` 
Les différentes valeurs sont stockées au préalable dans une liste de tuples.

    
    Créer un programme qui demande à l'utilisateur un nom et une note, en boucle. Les résultats sont stockés au fur et à mesure dans une base de données. Si le nom est égal à «Q» ou «q», le programme s'arrête.

    
    

    

#### 1.4 :skull: Exemple d'injection SQL :skull:
L'injection SQL est une technique consistant à écrire du code SQL à un endroit qui n'est pas censé en recevoir.

[](https://xkcd.com/327/)

- Créez un fichier contenant le code suivant :
```python
import sqlite3

#Connexion
connexion = sqlite3.connect('mabasecobaye.db')

#Récupération d'un curseur
c = connexion.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS notes(
    Nom TEXT,
    Note INT);
    """)

while True :
    nom = input('Nom ? ')
    if nom in ['Q','q'] :
        break
    note = input('Note ? ')
    data = (nom, note)
    p = "INSERT INTO notes VALUES ('" + nom + "','" + note + "')"

    c.executescript(p)

#Validation
    connexion.commit()

#Déconnexion
connexion.close()

``` 

- Exécutez ce fichier, rentrez quelques valeurs, quittez, et ouvrez dans ```DB Browser``` la table ```notes``` pour bien vérifier que vos valeurs ont bien été stockées.
- Lancez à nouveau le fichier, en donnant ensuite comme nom la chaîne de caractères suivante : 

```sql
g','3'); DROP TABLE notes;--
```

- Donnez une note quelconque (par exemple 12), quittez le programme... et allez observer l'état de la base de données.

:skull: :skull: :skull:

 La table  ```notes``` n'existe plus !

**Explication** :  
La requête qui a été formulée est ```INSERT INTO notes VALUES ('g','3'); DROP TABLE notes;--','12')``` 

Dans un premier temps, le couple ```('g','3')``` a été inséré.  
Puis l'ordre a été donné de détruire la table ```notes```.  
Le reste du code (qui n'est pas correct) est ignoré car ```--``` est le symbole du commentaire en SQL (l'équivalent du # de Python).  

**Remarques** : 
 
- Évidemment, ce code a été fait spécifiquement pour être vulnérable à l'injection SQL. Il suffit d'ailleurs de remplacer le ```c.executescript(p)``` par ```c.execute(p)``` pour que le code reste fonctionnel mais refuse l'injection SQL. 
Ceci dit, de nombreux serveurs sont encore attaqués par cette technique, au prix de manipulations bien sûr plus complexes que celles que nous venons de voir (vous pouvez par exemple regarder ici. 

- Rappelons enfin que ce genre de pratiques est interdit sur un serveur qui ne vous appartient pas.

- Si cela vous a plu, vous pouvez aller visiter l'excellent site https://www.hacksplaining.com/lessons/sql-injection.

### 2. Lecture des enregistrements

La récupération des résultats des requêtes peut se faire avec la méthode ```fetchall()```, qui renvoie une liste de tuples. 

```python
import sqlite3

#Connexion
connexion = sqlite3.connect('mynewbase.db')

#Récupération d'un curseur
c = connexion.cursor()

data = ('Simpson', )

c.execute('SELECT Prénom FROM Bulletin WHERE Nom = ?', data)
print(c.fetchall())  

#Déconnexion
connexion.close()
``` 

Ce code renvoie ```[('Homer',), ('Lisa',), ('Maggie',)]```, ou une liste vide s'il n'y a pas de résultat à la requête.

#### 2.1 Mini-projet 2
Reprendre le mini-projet précédent, en rendant possible à l'utilisateur de rentrer des notes ou bien de les consulter.

*Exemple :*

    ```python linenums='1'
    import sqlite3

    #Connexion
    connexion = sqlite3.connect('mabase.db')

    #Récupération d'un curseur
    c = connexion.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS notes(
        Nom TEXT,
        Note INT);
        ''')

    def menu():
        print('Menu')
        print('1. Rentrer des notes')
        print('2. Consulter des notes')
        print('3. Quitter')
        rep = input('choix ? ')
        if rep == '1':
            saisie()
        if rep == '2':
            consultation()
        if rep == '3':
            pass

    def saisie():
        while True :
            ...

            #Validation
            connexion.commit()
        menu()

    def consultation():
        print('Consultation des notes (taper Q pour sortir)')
        while True :
            ...

        menu()

    menu()

    connexion.close()    
    ```

#### 2.3 Mini-projet 3
Créer un système d'authenfication par login / mot de passe, dans le but de conserver une phrase secrète.  

Idéalement le mot de passe ne sera pas conservé en clair mais haché.

*Exemple :*

{#
lien vers une correction
#}

### 0. Du modèle relationnel au SGBD

Les considérations sur le modèle relationnel du cours précédent traitaient plutôt de la structure mathématique des données. 

Il s'agissait de déterminer la meilleure structure pour représenter les données et les relations qui les lient. 

Il convient maintenant d'aborder la partie logicielle : les SGBD (Systèmes de Gestion de Bases de Données).

Les SGBD jouent le rôle d'interface entre l'être humain et la base de données.
Par l'intermédiaire de **requêtes**, l'utilisateur va consulter ou modifier la base de données. Le SGBD est garant de l'intégrité de cette base, et prévient notamment que les modifications (souvent appelées **transactions**) ne soient pas préjudiciables à la base de données.

Le langage utilisé pour communiquer avec le SGBD est le langage **SQL**, pour Structured  Query Langage (pour *langage de requêtes structurées*).

Les SGBD les plus utilisés sont basés sur le modèle relationnel. Parmi eux, citons Oracle, MySQL, Microsoft SQL Server, PostgreSQL, Microsoft Access, SQLite, MariaDB...

Mais de plus en plus de SGBD **non-relationnels** sont utilisés, spécialement adaptés à des données plus diverses et moins structurées. On les retrouve sous l'appelation **NoSQL**  (pour *Not only SQL*). Citons parmi eux MongoDB, Cassandra (Facebook), BigTable (Google)...

La quasi-totalité de ces SGBD fonctionnent avec un modèle client-serveur. 

Nous allons travailler principalement avec le langage SQLite peut lui s'utiliser directement sans démarrer un serveur : la base de données est entièrement représentée dans le logiciel utilisant SQLite (dans notre cas, DB Browser for SQLite).  
Sa simplicité d'utilisation en fera notre choix pour illustrer cette présentation du langage SQL.

### 1. Introduction au langage SQL

Dans toute la suite, nous allons travailler avec la base de données ```livres.db``` qui provient de l'ouvrage paru chez Ellipses, cité en bibliographie.

### 1.0 Différents moyens d'interroger la base de données

**Pré-requis :** téléchargez la base de données livres.db.

    - Rendez vous sur https://sqliteonline.com/
    - Par File / OpenDB, ouvrez le fichier  ```livres.db``` précédemment téléchargé.
    - Écrivez votre requête plus cliquez sur Run.  

    - Installez ```DB Browser for SQLite```, téléchargeable à l'adresse https://sqlitebrowser.org/
    - Ouvrez le fichier ```livres.db```.  
    

--------

Dans toute la suite, les manipulations sont à faire en interrogeant la base de données ```livres.db```, avec l'une des méthodes indiquées ci-dessus.

Voici le diagramme relationnel de cette base :

- les clés primaires sont en bleu (suivi d'une icone de clé)
- les clés étrangères sont en noir et reliées à leur clé primaire.

 .sql fait avec DBbrowser -->

### 1.1. Sélection de données

#### 1.1.0 Exemple 0 

    - **Commande :** 
    ```sql
    SELECT titre
    FROM livre ;
    ``` 
    - **Traduction :** 

    On veut tous les titres de la table «livre».

    - **Résultat :**   

    

**Remarques**  

- Les mots-clés SQL sont traditionnellement écrits en MAJUSCULES. 

- Le ```;``` signale la fin de l'instruction. Il peut donc être omis s'il n'y a pas d'instructions enchaînées (ce qui sera toujours notre cas).  

- L'indentation n'est pas syntaxique (pas comme en Python). On peut faire des retours à la ligne et des indentations pour rendre le code plus lisible.

#### 1.1.1 Exemple 1 

    - **Commande :** 
    ```sql
    SELECT titre 
    FROM livre 
    WHERE annee >= 1990;
    ``` 
    - **Traduction :** 

    On veut les titres de la table «livre» qui sont parus après (ou en ) 1990;

    - **Résultat :**   

    

Le mot-clé WHERE doit être suivi d'un booléen. Les opérateurs classiques ```=``` , ```!=```, ```>```, ```>=```, ```= 1970
    AND annee = 1990;
    ``` 
    - **Traduction :** 

    On veut les titres et les ISBN de la table «livre» qui sont parus après 1990.

    - **Résultat :**   

    

#### 1.1.5 Exemple 5 

    - **Commande :** 
    ```sql
    SELECT * 
    FROM livre 
    WHERE annee >= 1990;
    ``` 
    - **Traduction :** 

    On veut toutes les colonnes disponibles de la table «livre» pour les livres qui sont parus après 1990.  
    L'astérisque ```*``` est un joker (*wildcard* en anglais).

    - **Résultat :**   

    

#### 1.1.6 Exemple 6 

    - **Commande :** 
    ```sql
    SELECT titre AS titre_du_livre 
    FROM livre 
    WHERE annee >= 1990;
    ``` 
    - **Traduction :** 

    Lors de l'affichage du résulats et dans la suite de la requête (important), la colonne "titre" est renommée "titre_du_livre".

    - **Résultat :**   

    

**Remarque**  
L'alias ```AS``` sera souvent utilisé pour raccourcir un nom, notamment lors des jointures de plusieurs tables (voir plus loin).

### 1.2. Opérations sur les données : sélection avec agrégation

Les requêtes effectuées jusqu'ici ont juste sélectionné des données grâce à différents filtres : aucune action à partir de ces données n'a été effectuée.  
Nous allons maintenant effectuer des opérations à partir des données sélectionnées. On appelle ces opérations des **opérations d'agrégation**.

#### 1.2.1 Exemple 7 

    - **Commande :** 
    ```sql
    SELECT COUNT(*) AS total 
    FROM livre
    WHERE titre LIKE "%Astérix%";
    ``` 
    - **Traduction :** 

    On veut compter le nombre d'enregistrements de la tables livres comportant le mot "Astérix". Le résultat sera le seul élément d'une colonne nommée «total».

    - **Résultat :**   

    

#### 1.2.2 Exemple 8 

    - **Commande :** 
    ```sql
    SELECT SUM(annee) AS somme
    FROM livre
    WHERE titre LIKE "%Astérix%";
    ``` 
    - **Traduction :** 

    On veut additionner les années des livres de la tables livres comportant le mot "Astérix". Le résultat sera le seul élément d'une colonne nommée «somme».
    *Attention : dans notre cas précis, ce calcul n'a aucun sens...*

    - **Résultat :**   

    

#### 1.2.3 Exemple 9 

    - **Commande :** 
    ```sql
    SELECT AVG(annee) AS moyenne
    FROM livre
    WHERE titre LIKE "%Astérix%";
    ``` 
    - **Traduction :** 

    On veut calculer la moyenne des années de parution des livres de la table livres comportant le mot "Astérix". Le résultat sera le seul élément d'une colonne nommée «moyenne».  
    *Attention : là encore, ce calcul n'a aucun sens...*

    - **Résultat :**   

    

#### 1.2.4 Exemple 10 

    - **Commande :** 
    ```sql
    SELECT MIN(annee) AS minimum
    FROM livre
    WHERE titre LIKE "%Astérix%";
    ``` 
    - **Traduction :** 

    On veut trouver la plus petite valeur de la colonne «annee» parmi les livres de la tables livre comportant le mot "Astérix". Le résultat sera le seul élément d'une colonne nommée minimum. Le fonctionnement est identique avec **MAX** pour la recherche du maximum.

    - **Résultat :**   

    

#### 1.2.5 Exemple 11 

    - **Commande :** 
    ```sql
    SELECT titre, annee 
    FROM livre
    WHERE titre LIKE "%Astérix%"
    ORDER BY annee DESC;
    ``` 

    - **Traduction :** 

    On veut afficher tous les albums d'Astérix, et leur année de parution, classés par année décroissante.
    
    - **Résultat :**   

    

    - **Comportement par défaut :** Si le paramètre ASC ou DESC est omis, le classement se fait par ordre **croissant** (donc ASC est le paramètre par défaut).

    - **Utilisation de LIMIT :** Le mot-clé LIMIT (suivi d'un nombre) permet de limiter le nombre de résultats affichés.  
    Ainsi la requête  
    ```sql
    SELECT titre, annee 
    FROM livre
    WHERE titre LIKE "%Astérix%"
    ORDER BY annee DESC
    LIMIT 1;
    ``` 
    permet d'obtenir les renseignements sur l'Astérix le plus récent.                    
       

#### 1.2.5 Exemple 12 

    - **Commande :** 
    ```sql
    SELECT DISTINCT editeur 
    FROM livre;
    ``` 
    - **Traduction :** 

    On veut la liste de tous les éditeurs. Sans le mot-clé ```DISTINCT```, beaucoup de doublons apparaîtraient.

    - **Résultat :**

### 1.3 Des recherches croisées sur les tables : les jointures

Observons le contenu de la table «emprunt» :

```sql
SELECT * 
FROM emprunt;
``` 

Le contenu est peu lisible : qui a emprunté quel livre ?  
Souvenons-nous du diagramme de la base de données.

 

 Pour que la table «emprunt» soit lisible, il faudrait (dans un premier temps) que l'on affiche à la place de l'ISBN le titre de l'ouvrage. Or ce titre est disponible dans la table «livres».  On va donc procéder à une **jointure** de ces deux tables.

#### 1.3.1 Exemple 13 

    - **Commande :** 
    ```sql
    SELECT livre.titre, emprunt.code_barre, emprunt.retour 
    FROM emprunt
    JOIN livre ON emprunt.isbn = livre.isbn;
    ``` 
    - **Traduction :** 
    Comme plusieurs tables sont appelées, nous préfixons chaque colonne avec le nom de la table. Nous demandons ici l'affichage de la table «emprunt», mais où on aura remplacé l'ISBN (peu lisible) par le titre du livre.

L'expression 
```sql
JOIN livre ON emprunt.isbn = livre.isbn
``` 
doit se comprendre comme ceci : on «invite» la table «livres» (dont on va afficher la colonne «titre»). La correspondance entre la table «livres» et la table «emprunt» doit se faire sur l'attribut ISBN, qui est la clé primaire de «livres» et une clé étrangère d'«emprunts».  
Il est donc très important de spécifier ce sur quoi les deux tables vont se retrouver (ici, l'ISBN) 

- **Résultat :**  

#### 1.3.2 Exemple 14 

Le résultat précédent a permis d'améliorer la visibilité de la table «emprunt», mais il reste la colonne «code_barre» qui est peu lisible. Nous pouvons la remplacer par le titre du livre, en faisant une nouvelle jointure, en invitant maintenant les deux tables «livre» et «usager».

    - **Commande :** 
    ```sql
    SELECT u.nom, u.prenom, l.titre, e.retour 
    FROM emprunt AS e
    JOIN livre AS l ON e.isbn = l.isbn
    JOIN usager AS u ON e.code_barre = u.code_barre;
    ``` 
    - **Traduction :** 
    Il faut bien comprendre que la table principale qui nous intéresse ici est «emprunts», mais qu'on modifie les valeurs affichées en allant chercher des correspondances dans deux autres tables. 
    Notez ici que des alias sont donnés aux tables (par **AS**) afin de faciliter l'écriture. 

    - **Résultat :**  

    

{#

### 1.4 Exercice d'application : The SQL Murder Mystery

Cet exercice en ligne est proposé le Knight Lab de l'université américaine Northwerstern University.

**Le point de départ de l'histoire** : un meurtre a été commis dans la ville de SQL City le 15 janvier 2018.

À partir de ce point de départ et d'une base de données dont le diagramme est donné ci-dessous, il s'agit de trouver le meurtrier.

Rendez-vous sur cette page, et bonne enquête à coups de requêtes !

- Vous pouvez travailler en ligne ou bien dans votre SGBD préféré, avec la base sql-murder-mystery.db. Attention pour valider votre réponse, il faudra vous rendre en bas de la page officielle.

- Vous pouvez trouver des éléments de correction ici...
#}

### 2. Création et modification d'une base de données

_rappel_ : 

L'objectif est de créer la table suivante :

| id | Nom | Maths | Anglais | NSI |
|:-----:|:-----:|:-------:|:----:|:----:|
| 1 | Alice | 16 | 11 | 17 |
| 2 | Bob  | 12 | 15 | 10 |
| 3 | Charles | 9 | 11 | 18 |

#### 2.1 Exemple 15 

*La création d'une table n'est pas explicitement au programme de NSI. Personne ne sait vraiment pourquoi*

    - **Commande :** 
    ```sql
    CREATE TABLE Table_notes (
            Id INTEGER PRIMARY KEY,
            Nom TEXT,
            Maths INTEGER,
            Anglais INTEGER,
            NSI INTEGER
            );
    ``` 
    - **Remarque :**  
    C'est l'utilisateur qui spécifie, éventuellement, quel attribut sera une clé primaire.

    - **Résultat :**  
    Dans DB Browser, il faut avoir au préalable créé une nouvelle base de données.

#### 2.2 Exemple 16 

    - **Commande :** 
    ```sql
    INSERT INTO Table_notes 
    VALUES (1, 'Alice', 16, 11, 17),
           (2, 'Bob', 12, 15, 10),
           (3, 'Charles', 9, 11, 18);
    ``` 

    - **Résultat :**  

    

#### 2.3 Exemple 17 : Intérêt de la clé primaire
Essayons d'insérer un 4ème enregistrement ayant le même ```id``` qu'un autre élève. 

- **Commande :** 
```sql
INSERT INTO Table_notes 
VALUES  (3, 'Denis', 18, 10, 12);
``` 

- **Résultat :**  
La contrainte de relation est violée : le SGBD «protège» la base de données en n'acceptant pas la proposition d'insertion. La base de données n'est pas modifiée.

- **Remarque :**
Il est possible de «déléguer» la gestion des valeurs de la clé primaire avec l'instruction ```AUTOINCREMENT```. 
La déclaration de la table et l'insertion des valeurs serait :
```sql
CREATE TABLE Table_notes (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nom TEXT,
        Maths INTEGER,
        Anglais INTEGER,
        NSI INTEGER
        );

INSERT INTO Table_notes 
VALUES
	('Alice', 16, 11, 17),
	('Bob', 12, 15, 10),
	('Charles', 9, 11, 18);
``` 
et le résultat serait : 

L'attribut ```id``` est donc géré automatiquement par le SGBD.

#### 2.4 Exemple 18 

    Pour modifier la note de Maths d'Alice :

    - **Commande :** 
    ```sql
    UPDATE Table_notes 
    SET Maths = 18 
    WHERE Nom = 'Alice';
    ``` 

#### 2.5 Exemple 19 

    Pour supprimer totalement la ligne concernant Charles :

    - **Commande :** 
    ```sql
    DELETE FROM Table_notes 
    WHERE Nom = 'Charles';
    ``` 

Si une autre table contient par exemple l'attribut ```id```  comme clé étrangère, et si l'```id```  de Charles fait partie de cette table, le SGBD refusera de supprimer cette ligne, afin de ne pas violer la contrainte de référence.

#### 2.6 Exemple 20 

    Pour supprimer totalement et défitivement la table :

    - **Commande :** 
    ```sql
    DROP TABLE Table_notes;
    ``` 

Là encore, si une autre table est reliée à ```Table_notes``` par une clé étrangère, la suppression sera bloquée par le SGBD.

## Base de donnees relationnelles

### Base de donnees relationnelles

Terminale - Spécialité NSI IFS Singapour
Chapitre 8 - Les bases de données relationnelles
Objectifs :
▷ Identifier les concepts définissant le modèle relationnel.
▷ Maîtriser les définitions de : relation, attribut, domaine, clé primaire, clé étrangère, schéma relationnel
▷ Exprimer les contraintes d'intégrité d'une base de données
▷ Savoir réaliser un schéma relationnel
▷ Savoir repérer les anomalies dans le schéma relationnel d'une base de données
1 Introduction
Les bases de données sont aujourd'hui incontournables, car très peu d'informations restent encore stockées sur
du papier. Nous avons vu en classe dePremière comment utiliser des données comme celle d'un tableur avec
notamment l'utilisation du formatcsv.
En effet, prenons l'exemple d'une table contenant quelques films :
Titre Réalisateur Année Durée
2001 : A Space Odyssey Stanley Kubrick 1968 149
Alien Ridley Scott 1979 117
Blade Runner Ridley Scott 1982 117
Akira Katsuhiro Ôtomo 1988 124
— Comment peut-on faire si on veut rajouter des informations sur le réalisateur, comme sa nationalité, sa
date de naissance ou un deuxième prénom pour le distinguer d'un homonyme?
— Faut-il le rajouter sur chacun de ses films?
— Faut-il ajouter de nouvelles entrées?
— Comment s'y prendre pour trouver facilement tous les films d'un même réalisateur?
Tous ces problèmes sont démultipliés si on veut rajouter par exemple les scénaristes, les acteurs ou le genre du
film. L'utilisation de simples tableaux a donc ses limites.
Pour apporter une solution, on sépare les données en plusieurs tables qui ont un lien (une relation) les unes
avec les autres. C'est ce que l'on appelle unebase de données relationnelle. Cela a été théorisé en 1970 par
le Britannique Edgar F. Codd . Il recevra leprix Turing en 1981 pour son travail.
2 Définition
A retenir!
Une base de donnéesest un moyen destocker des données de manière structurée, accessibles
en lecture et en écriture à l'aide d'un langage.
Les bases de données peuvent être divisées en deux catégories :
▷ Les bases données relationnelles utilisent des tableaux de données organisés en lignes et colonnes
auxquelles on accède grâce au langageSQL (pour Structured Query Language.).
▷ Les bases de données non relationnellesdites noSQL qui peuvent stocker des données de formes
diverses : graphes, documents, ..., etc. (hors programme de Terminale)
T. Rahobisoa 1/9 BDD01 - Les bases de données
Terminale - Spécialité NSI IFS Singapour
3 Le modèle relationnel
Dans une base de données, plutôt que de stocker toutes les données dans une table, on les stocke dans plusieurs
tables reliées entre elles par des clés.
Le modèle relationnel créé par E. F. Codd en 1970, consiste à voir chaquetable comme unerelation sur
les données qui la constituent.
Ainsi, dans notre exemple, on va définir une relation (table) pour les films et une autre pour les réalisateurs.
Relation Films
Film Titre Réal Année Durée
1 2001 : A Space Odyssey 1 1968 149
2 Alien 2 1979 117
3 Blade Runner 2 1982 117
4 Akira 3 1988 124
Relation Réalisateurs
Réal Nom
1 Stanley Kubrick
2 Ridley Scott
3 Katsuhiro Ôtomo
Les principes de base du modèle relationnel
▷ Les données sont regroupées dans différentes tables (qu'on appellera plutôt relations et qui
donnent son nom au modèle). Chaque relation contient des éléments directement en lien avec
le sujet général de la table.
▷ Autant que possible, des données identiques ne doivent pas se trouver dans des tables différentes :
on évite laredondance des données.
▷ Les données ne doivent pas contenir elles-mêmes d'autres données : on parle d'atomicité des
données.
4 Vocabulaire
La plupart des termes que nous allons voir forment le vocabulaire minimal qu'il faut savoir pour aborder ce
domaine.
A retenir!
▷ Relation, ou table :Tableau à 2 dimensions contenant les données de type texte ou numérique.
C'est l'endroit où sont rangées les données. L'ordre des lignes (que l'on appelera desenregistre-
ments) n'a pas d'importance.
▷ Enregistrement, ou tuple, ou t-uplet :cela correspond à une ligne du tableau, et donc un
ensemble de valeurs liées entre elles.
▷ En-tête :c'est l'ensemble des titres des attributs (première ligne de la table).
▷ Attribut : la table est composée de colonnes qui ont des titres que l'on appelle des attributs.
Dans une même table, chaque colonne devra avoir un nom différent.
▷ Domaine : le domaine d'un attribut donné correspond à un ensemble fini ou infini de valeurs
admissibles. Le domaine désigne «le type» (au sens typeInt, Float, String).
T. Rahobisoa 2/9 BDD01 - Les bases de données
Terminale - Spécialité NSI IFS Singapour
5 Exemple
Prenons l'exemple d'une bibliothèque dont la base de données possède une relationLivres suivante :
Dans notre exemple, nous avons l'entête (en bleu), l'enregistrement (en rouge) et l'attribut (en vert).
Ainsi :
▷ Il y a dans notre relation un attribut «Titre», un attribut «Auteur», ..., etc.
▷ L'auteur «Eric VUILLARD» a bien écrit le livre «L'Ordre du jour». Il est interdit que deux enregistre-
ments soient totalement identiques.
▷ L'attribut «Éditeur» est une chaîne de caractères, son domaine est doncString.
▷ Par contre l'attribut «ISBN» est un nombre de 13 chiffres, commençant manifestement toujours par978.
Son domaine est doncInt.
▷ Ici notre schéma serait :
((Code, Entier),(Titre, Chaîne de caractères),(Auteur, Chaîne de caractères),(Éditeur,
Chaîne de caractères),(ISBN, Entier))
Consulter un résumé en vidéo ici.
6 Notions de clé
Afin de comprendre le concept de clé dans une base de donnée relationnelle, consulter cette vidéo.
6.1 Clé primaire
A retenir!
Une clé primaire est un attribut (ou une réunion d'attributs) dont la connaissance suffit à identifier
avec certitude un unique enregistrement.
Dans l'exemple de la relation «Livre» traité précédemment, l'attribut «ISBN» pourrait jouer le rôle de clé
primaire car ilidentifie de manière uniquen'importe quel ouvrage.
Dans le cas d'une relation contenant des enregistrements de personnes nées en France, la clé primaire pourrait
être le numéro de Sécurité Sociale.
T. Rahobisoa 3/9 BDD01 - Les bases de données
Terminale - Spécialité NSI IFS Singapour
6.2 Clé étrangère
Dans notre exemple, ajoutons maintenant les relations ci-dessous :
▷ Relation «Emprunts»
id_emprunteur Date Nom Prénom Titre Auteur Code
845 12/10/2020 DURAND Michel Au revoir là-haut Pierre LEMAITRE 942
125 13/10/2020 MARTIN Jean Pas pleurer Lydie SALVAYRE 1023
125 13/10/2020 MARTIN Jean Boussole Mathias ENARD 486
▷ Relation «Emprunteurs»
id_emprunteur Nom Prénom Adresse Téléphone
1 Dupont Jean 123 Rue de la Libération 01-234-5678
2 Martin Marie 456 Avenue des Roses 02-345-6789
3 Dubois Pierre 789 Boulevard de l'Étoile 03-456-7890
L'attribut «id_emprunteur» est une clé primaire de la relation«Emprunteurs».
«id_emprunteur» est bien une clé primaire (de la relation «Emprunteurs») mais ne peut pas être une clé
primaire de la relation«Emprunts», car une personne peut prendre plusieurs livres à la fois.
On dit alors que c'est uneclé étrangère.
A retenir!
Une clé étrangère est une clé primaire d'une autre relation.
Consulter un résumé en vidéo ici.
7 Schéma et diagramme relationnel
7.1 Schéma relationnel
A retenir!
Le schéma d'une relation est le regroupement de tous les attributs et de leur domaine respectif.
On appelleschéma relationnell'ensemble des relations présentes dans une base de données.
Un schéma relationnel d'une base de données doit contenir les informations suivantes :
▷ Les noms des différentes relations
▷ Pour chaque relation, laliste des attributsavec leurdomaine respectif
▷ Pour chaque relation, laclé primaireet éventuellement la ou lesclés étrangères
On schématise une base de donnée par les structures des tables où sont reliées les clés primaires et
étrangères en relation.
Voici un exemple de schéma relationnel pour les relationsLIVRES etAUTEURS :
AUTEURS(id:INT, nom:TEXT, prenom:TEXT, ann_naissance:INT, langue_ecriture:TEXT)
LIVRES(id:INT, titre:TEXT, #id_auteur:INT, ann_publi:INT, note:INT)
Par convention :
— on souligne lesclés primaires
— on fait précéder lesclés étrangèresd'un dièse #.
T. Rahobisoa 4/9 BDD01 - Les bases de données
Terminale - Spécialité NSI IFS Singapour
7.2 Diagramme relationnel
Souvent, on présentera l'ensemble des renseignements d'un modèle relationnel sous forme d'undiagramme qui
synthétise la composition des différentes tables et les relations entre elles.
On pourra utiliser l'outil en ligne QuickDBD pour créer facilement des schémas relationnels.
Pour cela, on utilise une syntaxe simple pour saisir les attributs, leurs domaines, les clés primaires et étrangères
et les relations.
8 Les trois contraintes d'intégrité
Dans une base de données, il faut garantir que les données stockées soient :
— précises,
— cohérentes
— et conformes aux exigences du système,
C'est pour cela que l'on a défini des règles que l'on appelle lescontraintes d'intégrité, à savoir :
Contrainte n°1
Lacontrainte de domaine: chaque attribut doit prendre une valeur dans le domaine de valeurs (entier,
flottant etc...).
Attention, certains domaines sont subtils. Par exemple, si une relation possède un attribut"Code Postal",
le domaine de cet attribut devra êtreString plutôt que Entier . Dans le cas contraire, un enregistrement
possédant le code postal03150 serait converti en3150 (car pour les entiers,03150 = 3150). Or le code postal
3150 n'existe pas.
Contrainte n°2
La contrainte d'unicité: La valeur d'une clé primaire ne doit apparaître qu'une fois dans une table.
Elle doit être unique et non nulle.
Contrainte n°3
La contrainte d'intégrité référentielle: toutes les valeurs d'une clé étrangère d'une table doivent
correspondre à une valeur existante de la table à laquelle elle fait référence.
T. Rahobisoa 5/9 BDD01 - Les bases de données
Terminale - Spécialité NSI IFS Singapour
9 Les SGBD
Dans une base de données, l'information est stockée dans des fichiers, mais ceux-ci ne sont en général pas lisibles
par un humain. A la différence des fichiers au format.csv, il n'est pas possible de travailler sur ces données
avec un simple éditeur de texte.
Dans la pratique, les bases de données sont souvent stockées sur des serveurs. On y accède via unsystème de
gestion de base de donnéesnoté souvent par l'acronymeSGBD.
A retenir!
Le but de ce système est de définir les droits des différents utilisateurs (lecture, modification de certaines
tables), de gérer les accès en parallèle, de sécuriser les données et d'assurer leur sauvegardes.
Les SGBD permettent :
— la sauvegarde des données,
— l'interrogation des données,
— la recherche des données,
— la mise en forme des données.
On peut différencier 5 modèles de SGDB :
— le modèle hiérarchique: Les données sont classées hiérarchiquement. On les représente sous la forme
d'un arbre avec une arborescence descendante.
— le modèle réseauest une extension du modèle hiérarchique dans lequel l'on rajoute des relations entre
les enregistrements.
— le modèle relationnel: les données sont enregistrées dans des tableaux à deux entrées.
— le modèle objet: les données sont stockées sous forme de classe.
— le modèle déductif : qui ressemble au modèle relationnel avec une manipulation différente.
La plupart desSGBD-R (R de relationnelle) utilisent le langageSQL, Structured Query Language.
Figure 1 – SGBD les plus connus
T. Rahobisoa 6/9 BDD01 - Les bases de données
Terminale - Spécialité NSI IFS Singapour
10 Exercices
Exercice 1 : Résumé du cours
1. Visionner cette vidéo qui résume l'ensemble du cours.
2. Répondre au QCM suivant.
Exercice 2 :Deux relations modélisent la flotte de voitures d'un réseau de location de voitures.
Table 1 – RelationAgences
id_agence ville département
1 Paris 75
2 Lyon 69
3 Marseille 13
4 Aubagne 13
Table 2 – RelationVoitures
id_voiture marque modèle kilométrage couleur id_agence
1 Renault Clio 12000 Rouge 2
2 Peugeot 205 22000 Noir 3
3 Toyota Yaris 33000 Noir 3
1. Combien la relationVoitures comporte-t-elle d'attributs?
2. Que vaut son cardinal?
3. Quel est le domaine de l'attributid_agence dans la relationVoitures?
4. Quel est le schéma relationnel de la relationAgences?
5. Quelle est la clé primaire de la relationAgences?
6. Quelle est la clé primaire de la relationVoitures?
7. Quelle est la clé étrangère de la relationVoitures?
Exercice 3 :Un commerçant utilise plusieurs fichiers pour gérer ses produits. On considère un fichier destiné
à gérer des produits frais. Le tableau présenté est un extrait du contenu de ce fichier. Les quatre colonnes
contiennent respectivement un identifiant numérique, le nom du produit, son prix et la marque qui le commer-
cialise. Les mêmes noms de marques peuvent apparaître de nombreuses fois dans la colonne marque mais aussi
dans les fichiers correspondant à d'autres types de produits.
Table 3 – RelationMarques
id nom prix marque
17 Yaourt6 2,52 Yopnone
21 Yaourt12 4,93 Dalait
25 Beurre250 2,27 Croisement
28 Crème50 2,74 Dalait
31 Crème70 3,79 Yopnone
1. A partir de ce fichier, construire une relation Frais (pour les produits frais) et une relationMarques suivant
le modèle relationnel permettant d'éviter la redondance d'informations.
2. Indiquer une clé primaire pour chacune des deux tables et préciser la clé étrangère.
T. Rahobisoa 7/9 BDD01 - Les bases de données
Terminale - Spécialité NSI IFS Singapour
Exercice 4 :Concernant les vols qui sont prévus dans un aéroport pendant une journée, on dispose de données,
écrites dans un tableur. Nous avons le numéro du vol, les heures de départ et d'arrivée, la provenance pour les
vols à l'arrivée, la destination pour les vols au départ, le type d'avion et sa capacité totale de passagers. Chaque
vol a un numéro unique.
Extrait du tableau :
Table 4 – RelationVols
vol hd ha provenance destination avion capacité
AF373 8h45 10h05 Toulouse, France Paris, France Airbus A320 150
LX529 11h45 12h50 Nice, France Genève, Suisse Boeing 747 424
Décrire les 6 relations (Départs, Arrivées, Villes, Pays, Avions, Constructeurs) construites à partir de ce
fichier permettant de satisfaire au modèle relationnel.
Exercice 5 :Un particulier a un grand nombre de chansons stockées sur son ordinateur.
Il tient à jour un fichier qui contient toutes les chansons enregistrées par des groupes.
Cefichiercontientquatrecolonnesoùsontnotésrespectivementletitredelachanson,legroupequil'aenregistré,
les membres du groupe et la date d'enregistrement.
Voici une ligne de ce fichier :
titre groupe membres année
Roxane The Police Sting, Summers, Copeland 1978
Constituer un modèle relationnel normalisé à l'aide de trois tables nommées :Chansons, Groupes et Artistes.
Exercice 6 :On souhaite modéliser un annuaire téléphonique simple dans lequel chaque personne (identifiée
par son nom et son prénom) est associée à son numéro de téléphone. Proposer une modélisation relationnelle
de cet annuaire.
Vérifier si chacun des ensembles ci-dessous est une relation valide pour la relationAnnuaire :
1. {}
2. {(‘Titi','Toto','12345678')}
3. {(‘Titi','Toto','12345678'),(‘Dodo','Didi','12345678')}
4. {(‘Titi','Toto','12345678'),(‘Titi','Toto','+332345678674')}
5. {(‘Titi','Toto','12345678'),(‘Dodo','Didi')}
6. {(‘Titi','Toto',5678)}
T. Rahobisoa 8/9 BDD01 - Les bases de données
Terminale - Spécialité NSI IFS Singapour
Exercice 7 :Prenons la base de donnéesTour de France 2023 suivante :
Table 5 – RelationÉquipes
codeEquipe nomEquipe
ALM AG2R La Mondiale
AST Astana Pro Team
TBM Bahrain - McLaren
BOH BORA - hansgrohe
CCC CCC Team
COF Cofidis, Solutions Crédits
DQT Deceuninck - Quick Step
EF1 EF Pro Cycling
GFC Groupama - FDJ
LTS Lotto Soudal
Table 6 – RelationCoureurs
dossard nomCoureur prénomCoureur codeEquipe
141 LÓPEZ Miguel Ángel AST
142 FRAILE Omar AST
143 HOULE Hugo AST
11 ROGLIČ Primož TJV
12 BENNETT George TJV
41 ALAPHILIPPE Julian DQT
44 CAVAGNA Rémi DQT
45 DECLERCQ Tim DQT
121 MARTIN Guillaume COF
122 CONSONNI Simone COF
123 EDET Nicolas COF
Table 7 – Relation «Étapes»
numéroEtape villeDépart villeArrivée km
1 Nice Nice 156
2 Nice Nice 185
3 Nice Sisteron 198
4 Sisteron Orcières-Merlette 160
5 Gap Privas 198
Table 8 – Relation «Temps»
dossard numéroEtape tempsRéalisé
41 2 04 :55 :27
121 4 04 :07 :47
11 5 04 :21 :22
122 5 04 :21 :22
1. Quel temps a réalisé Guillaume MARTIN sur l'étape Sisteron / Orcières-Merlette?
2. À l'arrivée à Privas, qui est arrivé en premier entre Primož ROGLIČ et Simone CONSONNI?
T. Rahobisoa 9/9 BDD01 - Les bases de données

## SQL

### SQL

Terminale - Spécialité NSI IFS Singapour
Chapitre 9 - Le langage SQL
Objectifs :
▷ Identifier les composants d'une requête.
▷ Savoir utiliser des requêtes d'interrogation et de mise à jour d'une base de données.
▷ Construire des requêtes d'interrogation à l'aide des clauses du langage SQL :SELECT, FROM, WHERE, JOIN.
▷ Construire des requêtes d'insertion et de mise à jour à l'aide de :UPDATE, INSERT, DELETE.
1 Introduction
Dans le chapitre précédent sur le modèle relationnel, nous avons découvert la structure mathématique des bases
de données. Maintenant que nous avons vu comment celles-ci sont organisées, nous allons interagir avec elles.
Les SGBD jouent le rôle d'interface entre l'être humain et la base de données. Par l'intermédiaire de requêtes,
l'utilisateur vaconsulter ou mettre à jourla base de données.
Le langage utilisé pour communiquer avec le SGBD est lelangage SQL, (pour Structured Query Langage ou
langage de requêtes structurées).
Les SGBD les plus utilisés sont basés sur lemodèle relationnel. Parmi eux, on peut trouver :
La quasi-totalité de ces SGBD fonctionnent avec un modèleclient-serveur.
Cette année, nous allons travailler principalement avec le langageSQLite qui peut lui s'utiliser directement
sans démarrer un serveur : la base de données est entièrement représentée dans le logiciel utilisantSQLite. Sa
simplicité d'utilisation en fera notre choix pour illustrer cette présentation du langage SQL.
Il existe de nombreuses façons d'écrire des requêtes SQL avec une base de donnéesSqlite :
▷ Avec un logiciel muni d'une interface graphique commeDB Browser for SQLite .
▷ Via un langage de programmation comme Python grâce au modulesqlite3
▷ En console, en lançant :sqlite3 nom_de_ma_bdd.db .
▷ En ligne avec des sites commeSQLite online ou SQLite Viewer,
T. Rahobisoa 1/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
2 Le langage SQL
Les instructions SQL s'écrivent d'une manière qui ressemble à celle de phrases ordinaires en anglais. C'est
un langage déclaratif, c'est-à-dire qu'il permet de décrire le résultat escompté, sans décrire la manière de
l'obtenir.
Le langage SQL n'estpas sensible à la casse, mais a l'habitude d'écrire les instructions en majuscules, on
peut écrire les instructions sur plusieurs lignes avec ou sans indentation et chaque instruction doit être terminée
par unpoint-virgule.
Nous verrons cette année les instructions de manipulation du contenu de la base de données qui commencent
par les mots clés :
▷ SELECT : recherche de contenu;
▷ UPDATE : modification,
▷ INSERT : ajout,
▷ DELETE : suppression.
Pour illustrer ce cours, nous étudierons les données situées dans la base de donnéeslivres.db.
Voici le diagramme relationnel de cette base :
— Les clés primaires sont en bleu (suivi d'une icone de clé)
— Les clés étrangères sont en noir et reliées à leur clé primaire.
T. Rahobisoa 2/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
3 Sélection de données
3.1 Comment interroger une base de données?
3.1.1 Requête basique : SELECT ... FROM ...
Exemple 0
SELECT titre FROM livre ;
Traduction :
On veut tous les titres de la tablelivre.
Remarques :
▷ Les mots-clés SQL sont traditionnellement écrits en MAJUSCULES.
▷ Le ; signale la fin de l'instruction. Il peut donc être omis s'il n'y a pas d'instructions enchaînées
(ce qui sera toujours notre cas).
▷ L'indentation n'est pas syntaxique (pas comme en Python). On peut donc faire des retours à la
ligne et des indentations pour rendre le code plus lisible.
3.1.2 Requête filtrée : SELECT ... FROM ... WHERE ...
Exemple 1
SELECT titre FROM livre WHERE annee >= 1990;
Traduction :
On veut les titres de la tablelivre qui sont parus après (ou en ) 1990;
Remarques :
▷ Le mot-cléWHERE doit être suivi d'un booléen. Les opérateurs classiques= , !=, >, >=, <, <= peuvent
être utilisés, mais aussi le mot-cléIN.
3.1.3 Requête avec plusieurs possibilités : WHERE ... IN ...
Exemple 1bis
SELECT titre FROM livre WHERE annee IN (1990 , 1991 , 1992) ;
Traduction :
On veut les titres de la tablelivre qui sont parus en 1990, 1991 ou 1992.
3.1.4 Requête avec booléens : AND - OR
Exemple 2
SELECT titre FROM livre WHERE annee >= 1970 AND
annee <= 1980 AND
editeur = ' Dargaud ';
Traduction :
On veut les titres de la tablelivre qui sont parus entre 1970 et 1980 chez l'éditeur Dargaud;
T. Rahobisoa 3/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
3.1.5 Requête approchée : LIKE
Exemple 3
SELECT titre FROM livre WHERE titre LIKE '% Asterix % ';
Traduction :
On veut les titres de la tablelivre dont le titre contient la chaîne de caractèresAstérix.
Remarque :
▷ Le symbole % est un joker qui peut symboliser n'importe quelle chaîne de caractères.
3.1.6 Plusieurs colonnes
Exemple 4
SELECT titre , isbn FROM livre WHERE annee >= 1990;
Traduction :
On veut les titres et les ISBN de la tablelivre qui sont parus après 1990.
Remarque :
▷ Le symbole % est un joker qui peut symboliser n'importe quelle chaîne de caractères.
3.1.7 Toutes les colonnes : *
Exemple 5
SELECT * FROM livre WHERE annee >= 1990;
Traduction :
On veut les titres et les ISBN de la tablelivre qui sont parus après 1990.
Remarque :
▷ L'astérisque * est un joker (wildcard en anglais).
3.1.8 Renommer les colonnes : AS
Exemple 6
SELECT titre AS t i t r e _ d u _ l i v r e FROM livre WHERE annee >= 1990;
Traduction :
Lors de l'affichage du résulats et dans la suite de la requête (important), la colonnetitre est renommée
titre_du_livre.
Remarque :
▷ L'alias AS sera souvent utilisé pour raccourcir un nom, notamment lors des jointures de plusieurs
tables.
T. Rahobisoa 4/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
4 Opérations sur les données
4.1 Sélection avec agrégation
Les requêtes effectuées jusqu'ici ont juste sélectionné des données grâce à différents filtres : aucune action à
partir de ces données n'a été effectuée.
Nous allons maintenant effectuer desopérations à partir des données sélectionnées.
4.1.1 Compter : COUNT
Exemple 7
SELECT COUNT (*) AS total FROM livre
WHERE titre LIKE " % Asterix % " ;
Traduction :
On veut compter le nombre d'enregistrements de la tables livre comportant le mot "Astérix". Le
résultat sera le seul élément d'une colonne nomméetotal.
4.1.2 Additionner : SUM
Exemple 8
SELECT SUM ( annee ) AS somme FROM livre
WHERE titre LIKE " % Asterix % " ;
Traduction :
On veut additionner les années des livres de la tableslivre comportant le mot Astérix. Le résultat
sera le seul élément d'une colonne nomméesomme.
Remarque :
▷ Attention : dans notre cas précis, ce calcul n'a aucun sens car on additionne des années...
4.1.3 Faire une moyenne : AVG
Exemple 9
SELECT AVG ( annee ) AS moyenne FROM livre
WHERE titre LIKE " % Asterix % " ;
Traduction :
On veut calculer la moyenne des années de parution des livres de la tablelivre comportant le mot
Astérix. Le résultat sera le seul élément d'une colonne nomméemoyenne.
Remarque :
▷ Attention : là encore, ce calcul n'a aucun sens...
4.1.4 Trouver les extremums : MIN, MAX
Exemple 10
SELECT MIN ( annee ) AS minimum FROM livre
WHERE titre LIKE " % Asterix % " ;
Traduction :
On veut trouver la plus petite valeur de la colonneannee parmi les livres de la tablelivre comportant
le mot Astérix. Le résultat sera le seul élément d'une colonne nomméeminimum. Le fonctionnement est
identique avecMAX pour la recherche du maximum.
T. Rahobisoa 5/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
4.1.5 Classer des valeurs : ORDER BY, ASC, DESC, LIMIT
Exemple 11
SELECT titre , annee FROM livre
WHERE titre LIKE " % Asterix % "
ORDER BY annee DESC ;
Traduction :
On veut afficher tous les albums d'Astérix, et leur année de parution, classés par année décroissante.
Remarques :
▷ Comportement par défaut: Si le paramètre ASC ou DESC est omis, le classement se fait par
ordre croissant (doncASC est le paramètre par défaut).
▷ Utilisation de LIMIT : Le mot-clé LIMIT (suivi d'un nombre) permet de limiter le nombre de
résultats affichés. Ainsi la requête
4.1.6 Suppression des doublons : DISTINCT
Exemple 12
SELECT DISTINCT editeur FROM livre ;
Traduction :
On veut la liste de tous les éditeurs. Sans le mot-cléDISTINCT, beaucoup de doublons apparaîtraient.
5 Les jointures
Parfois, on a besoin aussi d'effectuer des requête complexes, comme par exemple desrecherches croiséessur
les tables. Pour cela, on va devoir faire desjointures.
Définition
En SQL, unejointure est une opération qui permet de combiner des données de deux tables (ou plus)
en fonction d'une ou plusieurscolonnes communes.
Cela permet de relier des informations provenant de différentes tables pour effectuer des requêtes
complexes et obtenir des résultats plus riches en informations.
Les jointures sont couramment utilisées pourrécupérer des données à partir de plusieurs sources
de données liées entre elles, en utilisant des critères de correspondance spécifiques.
5.1 Exemple
Par exemple, si on exécute la requête suivante sur le contenu de la tableemprunt :
SELECT * FROM emprunt ;
On obtient ceci :
T. Rahobisoa 6/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
Le contenu est peu lisible... Qui a emprunté quel livre? Qui est l'auteur ou le titre du livre emprunté?
En effet, le schéma relationnel est le suivant :
Pour que la tableemprunt soit lisible, il faudrait (dans un premier temps) que l'on affiche à la place de l'ISBN
le titre de l'ouvrage. Or ce titre est disponible dans la tablelivres
On va donc procéder à unejointure de ces deux tables.
5.1.1 Jointure de 2 tables : JOIN
Exemple 13
SELECT livre . titre , emprunt . code_barre , emprunt . retour FROM emprunt
JOIN livre ON emprunt . isbn = livre . isbn ;
Traduction :
Comme plusieurs tables sont appelées, nous préfixons chaque colonne avec le nom de la table. Nous
demandons ici l'affichage de la tableemprunt, mais où on aura remplacé l'ISBN (peu lisible) par le titre
du livre.
Résultat :
T. Rahobisoa 7/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
Remarques :
L'expression
JOIN livre ON emprunt . isbn = livre . isbn
doit se comprendre comme ceci :
▷ on «invite» la tablelivres (dont on va afficher la colonnetitre)
▷ la correspondance entre la tablelivres et la table emprunt doit se faire sur l'attribut ISBN, qui est la
clé primaire delivres et une clé étrangère d'emprunts.
Il est donc très important de spécifier ce sur quoi les deux tables vont se retrouver (ici, l'ISBN)
5.1.2 Jointure de 3 tables : JOIN
Le résultat précédent a permis d'améliorer la visibilité de la tableemprunt, mais il reste la colonnecode_barre
qui est peu lisible. Nous pouvons la remplacer par le titre du livre, en faisant une nouvelle jointure, en invitant
maintenant les deux tableslivre et usager.
Exemple 14
SELECT u . nom , u . prenom , l . titre , e . retour FROM emprunt AS e
JOIN livre AS l ON e . isbn = l . isbn
JOIN usager AS u ON e . c o d e _ b a r r e = u . c o d e _ b a r r e ;
Traduction :
Il faut bien comprendre que la table principale qui nous intéresse ici est «emprunts», mais qu'on modifie
les valeurs affichées en allant chercher des correspondances dans deux autres tables.
Notez ici que des alias sont donnés aux tables (parAS) afin de faciliter l'écriture.
Résultat :
T. Rahobisoa 8/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
6 Création et modification d'une base de données
L'objectif est maintenant de créer la table suivante :
id Nom Maths Anglais NSI
1 Alice 16 11 17
2 Bob 12 15 10
3 Charles 9 11 18
6.1 Création d'une table : CREATE TABLE
Exemple 15
CREATE TABLE T a b l e _ n o t e s (
Id INTEGER PRIMARY KEY ,
Nom TEXT ,
Maths INTEGER ,
Anglais INTEGER ,
NSI INTEGER
) ;
Remarques :
▷ C'est l'utilisateur qui spécifie, éventuellement, quel attribut sera uneclé primaire.
▷ Dans DB Browser, il faut avoir au préalable créé une nouvelle base de données.
6.2 Insertion de valeurs : INSERT INTO, VALUES
Exemple 16
INSERT INTO T a b l e _ n o t e s VALUES (1 , ' Alice ' , 16 , 11 , 17) ,
(2 , ' Bob ' , 12 , 15 , 10) ,
(3 , ' Charles ' , 9 , 11 , 18) ;
Traduction :On ajoute 3 élèves dans la tableTables_notes avec leurs notes respectives.
Remarques :
Si on essayer d'insérer un quatrième enregistrement ayant le mêmeId qu'un autre élève.
Par exemple :
INSERT INTO T a b l e _ n o t e s VALUES (3 , ' Denis ' , 18 , 10 , 12) ;
Alors, la contrainte de relation est violée : le SGBD «protège» la base de données en n'acceptant pas la propo-
sition d'insertion.
La base de donnéesn'est pas modifiée.
T. Rahobisoa 9/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
6.3 Modification d'une valeur UPDATE, SET
Exemple 17
Pour modifier la note de Maths d'Alice :
UPDATE T a b l e _ n o t e s SET Maths = 18 WHERE Nom = ' Alice ';
6.4 Suppression d'un enregistrement : DELETE
Exemple 18
Pour supprimer totalement la ligne concernantCharles :
DELETE FROM T a b l e _ n o t e s WHERE Nom = ' Charles ';
Remarque :
Si une autre table contient par exemple l'attributId comme clé étrangère, et si l'Id de Charles fait partie
de cette table, le SGBD refusera de supprimer cette ligne, afin de ne pas violer la contrainte de référence.
6.5 Suppression totale d'une table : DROP TABLE
Exemple 19
Pour supprimer totalement et défitivement la table :
DROP TABLE T a b l e _ n o t e s ;
Remarque : Si une autre table est reliée à Table_notes par une clé étrangère, la suppression sera
bloquée par le SGBD.
T. Rahobisoa 10/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
7 Exercices
Exercice 1 :Base de donnéesPrix Nobel
▷ Aller sur le site de la base de données des prix Nobel
▷ Répondre aux questions interactives pour réaliser les 15 requêtes demandées (en anglais).
Exercice 2 :Base de donnéesWorld
▷ Aller sur le site de la base de données de la population mondiale
▷ Répondre aux 8 questions interactives (en anglais).
Exercice 3 : Gestion d'un réseau d'agences de location de voitures
La base de donnéeslocations.db contient les tablesAgences, Locations, Vehicules.
Ecrire les requêtes SQL permettant de répondre aux questions ci-dessous :
1. Visualiser toute la relationAgences.
2. Lister uniquement les noms des agences et de leur ville.
3. Lister les noms des agences de la ville de Lorient.
4. Lister les noms des agences du département du Morbihan (code postal56***) ainsi que les codes postaux
en utilisant par exemple unWHERE LIKE .
5. Déterminer le nombre de voitures que vous possédez.
6. Déterminer l'âge minimum et maximum de vos véhicules.
7. Quels sont la marque et le modèle de votre dernière acquisition qui date de trois mois?
8. Quel est le kilométrage maximum des véhicules?
9. Quel est le kilométrage moyen des véhicules?
10. Afficher toute la flotte de véhicules par ordre décroissant de kilométrage.
11. Visualiser toute la relationLocations.
12. Déterminer le nombre de locations effectuées avec changement d'agence.
13. Déterminer le nombre total de kilomètres effectués durant les locations.
14. Lister toutes les locations en y associant les caractéristiques du véhicule.
15. Afficher le nom et l'immatriculation du véhicule ainsi que la date de la location et le kilométrage réalisé
pour chacune des locations.
16. Afficher une seule fois le nom et l'immatriculation des véhicules ayant déjà été loués.
17. Afficher les locations du véhicule immatriculé AB-224-BA en précisant le nom de l'agence de départ ainsi
que la ville de départ dans l'ordre chronologique des locations.
T. Rahobisoa 11/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
Exercice 4 : Championnat de France de football
La base de donnéessoccer.db contient les tablesTeam, Match, Event, Player.
Ecrire les requêtes SQL permettant de répondre aux questions ci-dessous :
1. Combien d'équipes ont participé à ce championnat?
2. Lister les noms des clubs ainsi que leur date de création dans l'ordre chronologique de leur création.
3. Combien de pénaltys ont été marqués?
4. Combien de pénaltys ont été sifflés?
5. Combien de cartons ont été distribués?
6. Combien de buts ont été marqués?
7. Afficher tous les renseignements sur les 10 cartons rouges obtenus le plus rapidement pendant un match.
8. Donner le nom du joueur qui a obtenu le carton rouge le plus rapidement.
Exercice 5 : Films
On dispose de la base de donnéesfilms.db suivante :
T. Rahobisoa 12/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
Elle donne naissance aux tables du modèle relationnel suivant :
Ecrire les requêtes qui permettent d'afficher :
1. Dix noms de personnes (réalisateurs ou acteurs)
2. La liste des titres des films commençant par la lettreM et se terminant par la lettrer ou s
3. La liste des titres des films sortis entre 2002 et 2004 (sur les 3 années)
4. La liste des noms et dates de naissance des personnes connues de la base dont le prénom commence par
'Ro' et de nationalité française (le pays vaut 'France'), par ordre alphabétique
5. Les pays (une fois chacun) dont ont connaît au moins une personne de sexe féminin (donc une réalisatrice
ou une actrice)
6. La liste des films sortis en 2006 en indiquant le titre, et le genre (en texte), par ordre alphabétique des
titres
7. La liste des drames sortis strictement avant 1970 en donnant le titre et l'année de sortie
8. La liste alphabétique des acteurs du film "Le convoyeur "
9. La table contenant seulement l'année de sortie du plus ancien film, et l'année de sortie du film le plus
récent
10. La moyenne du nombre de spectateurs par film
11. La liste des 10 films comptant le plus de spectateurs
12. La liste des films (avec leur année de sortie) sortis au moins 50 ans après le film le plus ancien de la base.
Exercice 6 :Base de donnéesEuro 2012
▷ Aller sur le site de la base de données de l'Euro 2012
▷ Répondre aux questions interactives pour réaliser les 9 premières requêtes demandées (en anglais).
Exercice 7 : Livres
Afin de créer une nouvelle base de données de livres, suivre les instructions pas à pas du site suivant (activités
3.1 à 3.16).
Exercice 8 : QCM de révisions
Répondre au QCM suivant sur les principales commandes SQL à connaître. (en anglais)
T. Rahobisoa 13/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
Exercice 9 : SQL Murder Mystery
Cet exercice en ligne est proposé leKnight Labde l'université américaineNorthwerstern University.
Le point de départ de l'histoire : un meurtre a été commis dans la ville deSQL City le 15 janvier 2018.
À partir de ce point de départ et d'une base de données dont le diagramme est donné ci-dessous, il s'agit de
trouver le meurtrier.
Rendez-vous sur cette page, et bonne enquête à coups de requêtes!
Exercice 10 : Sujet BAC (épreuve écrite)
Sur feuille, faire l'exercice 1du sujet BAC 2023 suivant : 23NSIJ1_G11_sujet.pdf
T. Rahobisoa 14/15 BDD02 - SQL
Terminale - Spécialité NSI IFS Singapour
8 Validation de compétences PIX
▷ Se connecter d'abord à son comptePix avec le compte IFS. Cliquer sur"Mot de passe oublié" si nécessaire.
▷ Suivre le lienPix suivant :https://app.pix.fr/campagnes/VSUPXU1661
▷ Répondre aux différentes questions afin de valider vos compétencesPix sur le thèmeGérer les données.
T. Rahobisoa 15/15 BDD02 - SQL
