# Architecture, OS et réseaux

## Systemes sur puce

### 1.1 La Loi de Moore

En 1965, Gordon Moore postule que le nombre de transistors présents sur une puce de microprocesseur doublera tous les deux ans.

Cette prédiction s'est révélée étonnamment juste (à quelques approximations près) et les équipements électroniques n'ont depuis jamais cessé de devenir toujours plus performants / miniatures / économes en énergie.

### 1.2  Évolution de la taille des ordinateurs

#### 1.2.1 IBM 650, le premier ordinateur fabriqué en série (1955)

Cet ordinateur n'a pas encore de transistors mais des tubes à vide.

#### 1.2.2 IBM 7090, le premier ordinateur à transistors (1959)
inline end "Le transistor"
    Le transistor est un composant électronique essentiel : il permet de laisser (ou non) passer un courant électrique.
    
    

#### 1.2.3 Le rôle crucial de la taille des transistors
Ainsi que l'avait prédit Moore, c'est la progression du nombre de transistors gravables sur le processeur qui guidera pendant des années l'évolution de l'informatique :

### 2. Composition d'un pc actuel

Chaque composant a un rôle spécifique. Ils communiquent entre eux par des **bus** de différentes vitesses. Chaque composant est remplaçable, et il est possible d'ajouter de nouveaux composants sur la carte mère qui possède des slots d'extension.

### 3.1 L'intégration de composants différents au sein d'une même puce

Le principe d'un **système sur puce** ou **System On a Chip** (SoC) est d'intégrer au sein d'une puce unique un ensemble de composants habituellement physiquement dissociés dans un ordinateur classique (ordinateur de bureau ou ordinateur portable).

On peut retrouver ainsi au sein d'une **même puce** :

- le microprocesseur (CPU)
- la carte graphique (GPU)
- la mémoire RAM

\+ éventuellement des composants de communication (WiFi, Bluetooth...)

    :white_check_mark: **Avantages**

    - moindre consommation électrique
    - moindre encombrement
    - pas besoin de refroidissement
    - meilleure sécurité (vue globale sur la sécurité qui n'est plus dépendante d'une multitude de composants)
    - moindre coût (forte automisation du processus, gros volumes de production)

    :name_badge: **Inconvénients**

    - Impossibilité de choisir indépendamment ses composants
    - Pas de mise à jour possible / remplacement / ajout d'un composant
    - La panne d'un seul composant entraîne la panne totale du SoC

### 3.2 Exemple : A15 Bionic

Observons par exemple la puce Apple A15 Bionic, qui équipe les iPhone 13. Cette puce est fabriquée par TSMC{https://fr.wikipedia.org/wiki/Taiwan_Semiconductor_Manufacturing_Companyrget="_blank"}.

Cette puce contient :

- 15 milliards de transistors (gravés à 5 nm)
- un processeur central à 6 cœurs (2 cœurs hautes performances + 4 cœurs plus économes en énergie)
- un GPU (processeur dédié uniquement au calcul du rendu graphique) de 5 cœurs.
- une puce dédiée au Machine Learning (*Neural Engine*)

### 4. Des puces dédiées à des tâches spécifiques

L'intégration dans un SoC n'est pas totale : il reste des puces dédiées à des tâches très spécifiques qui ne sont pas forcément intégrées dans le SoC.

### 4.1 Au sein d'un téléphone

Ainsi, d'après le site iFixit, on peut retrouver ceci dans l'iPhone Pro 13, au côté de la puce A15 évoquée plus haut :

 

On voit que (par exemple) qu'il existe une puce spécifique pour gérer l'audio, une puce spécifique pour le module WiFi, une puce spécifique pour le module Modem 5G...

### 4.2 En électronique «grand public»

Ce composant (pouvant être utilisé dans un montage personnel, sur un Arduino par exemple) ne sert qu'à faire des calculs cryptographiques.

### 4.3 Un principe général

Il est important de comprendre que certains processeurs sont optimisés pour un certains types de calcul. C'est le cas par exemple d'une carte graphique, qui excelle dans le calcul de rendus de polygones.

On s'est aperçu que cette aptitude à faire des calculs «bêtes et répétitifs» était parfaite pour faire les calculs mathématiques (inutiles) nécessaires
au minage des cryptomonnaies. Les cartes graphiques ont donc été détournées de leur usage originel, à cause de la spécificité de l'implémentation de leur puce.

De même, les calculs sur les réseaux de neurones (essentiels en IA) nécessitent une grande rapidité dans les multiplications de matrices. Pour cette raison, Apple a intégré directement dans son SoC A15 une puce spécalisée dans ces calculs (voir plus haut).

### 4.4 Conclusion

L'orientation actuelle de l'électronique est donc à la fois :

- une intégration toujours plus grande dans des SoC multi-tâches.
- des puces toujours plus spécifiques qui excellent dans un domaine particulier.

### 5. Exercice

Un constructeur automobile intègre à ses véhicules des systèmes embarqués, comme par exemple un système de guidage par satellites (GPS), un système de freinage antiblocage (ABS)... 

    Ces dispositifs utilisent des systèmes sur puces (SoC : System on a Chip).

    Citer deux avantages à utiliser ces systèmes sur puces plutôt qu'une architecture classique d'ordinateur.

    - Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
    - Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.
    - https://fr.wikipedia.org/wiki/Loi_de_Moore
    - https://blog.iakaa.com/lordinateur-fete-ses-60-ans/
    - https://www.thewindowsclub.com/history-of-computers
    - https://perso-etis.ensea.fr//lorandel/M2_SoC/s1.pdf
    - https://www.hawkpointtechnologies.com/about/blog/computer-components
    - https://www.tremplin-numerique.org/apple-a15-vs-a14-quoi-de-neuf-dans-la-puce-de-liphone-13
    - https://www.distrelec.be/fr/cryptoprocesseur-breakout-atecc608a-sparkfun-electronics-dev-18077/p/30241877

## Gestion des processus

### 1.1 Définition d'un processus

Lorsqu'un programme est exécuté sur un ordinateur, celui-ci va créer un (ou plusieurs) **processus**.

On dit que ce processus est une **instance d'exécution** de ce programme.

Un processus est caractérisé par :

- l'ensemble des instructions qu'il va devoir accomplir (écrites dans le fichier exécutable obtenu par la compilation du code-source du programme)
- les ressources que le programme va mobiliser (fichier en ouverture, carte son...)
- l'état des registres du processeur (voir le cours de Première sur l'architecture Von Neumann)

### 1.2.1 La commande ```ps```

Dans un terminal, la commande ```ps``` va permettre d'afficher la liste des processus actifs. 

> Plus précisément, nous allons utiliser la commande ```ps -lu nom_user```. L'option ```l``` permet d'afficher un grand nombre de renseignements et l'option ```u``` permet de spécifier l'utilisateur propriétaire des processus.

On retrouve notamment dans ce tableau les colonnes :

- ```CMD```  (Command) : le nom de la commande qui a créé le processus. Vous pouvez y retrouver par ordre chronologique le nom de tous les programmes actifs. Certains sont ceux que vous avez ouverts volontairement (navigateur...) mais on y trouve surtout tous les programmes nécessaires au bon fonctionnement du système d'exploitation. Le dernier processus en bas de la liste est forcément ```ps```, puisque vous venez de l'appeler.

- ```PID``` (Process Identifier) : le numéro unique d'identification, affecté chronologiquement par le système d'exploitation. Le processus de PID égal à 1 est ```systemd```, qui est le tout premier programme lancé par le noyau Linux au démarrage. 

- ```PPID``` (Parent PID) : certains processus vont *eux-mêmes* lancer plusieurs processus-fils, qui porteront le même nom. C'est ainsi qu'on peut retrouver de multiples processus s'appelant ```chrome``` :

Ici, l'instance «principale» de Chrome (```PID``` 1453) a généré 6 autres instances de ```PID``` différents, dont le ```PPID``` vaut 1453.

> Dans Chrome/Chromium, vous pouvez comprendre le rôle de chaque processus en le retrouvant dans le gestionnaire des tâches (clic-droit sur une zone vide de la barre d'onglets)

### 1.2.3 La commande ```top```

La commande ```top``` permet de connaître en temps réel la liste des processus, classés par ordre décroissant de consommation de CPU. 

On ferme ```top``` par la combinaison de touches ```Ctrl-C```.

    En face de chaque processus est affichée sa consommation de CPU. Elle est calculée en prenant, sur un intervalle de temps donné, le temps qu'a passé le CPU à traiter le processus en question, et en divisant ce temps par le temps total de la mesure. 

    $$\text{Pourcentage d'utilisation CPU} = \frac{\text{Temps d'utilisation CPU}}{\text{Temps total écoulé}} \times 100$$

Si on repère alors un processus qui consomme beaucoup trop de ressources, on peut utiliser...

### 1.2.4 La commande ```kill```

La commande ```kill``` permet de fermer un processus, en donnant son ```PID```  en argument.

Exemple : ```kill 1453``` tuera Chrome (voir la capture du 1.2.1)

### 2.1 Expérience : les processus fonctionnent ~~simultanément~~ à tour de rôle.

Un ordinateur donne l'illusion de réaliser plusieurs tâches simultanément. Hormis pour les processeurs fonctionnant avec plusieurs cœurs, il n'en est rien.

Comme nous l'avons vu, ces processus sont lancés séquentiellement par le système d'exploitation, et sont ensuite en apparence tous «actifs en même temps» (les guillemets sont importants) : on parle de **programmation concurrente**.

Revenons sur l'expression «actifs en même temps», car elle véhicule une fausse idée : ces processus sont bien vivants dans un même laps de temps, mais ils s'exécutent **LES UNS APRÈS LES AUTRES**, le processeur ne pouvant en traiter qu'**un seul à la fois**.

Un cadencement extrêmement rapide et efficace donne l'*apparence* d'une (fausse) simultanéité. Nous allons la mettre en évidence :

Considérons les fichiers ```progA.py``` et ```progB.py``` ci-dessous :

```python title="progA.py"
import time

for i in range(10):
    print("programme A en cours, itération", i)
    time.sleep(0.02)  
```

```python title="progB.py"
import time
time.sleep(0.01)
for i in range(10):
    print("programme B en cours, itération", i)
    time.sleep(0.02)  
```

Le programme ```progB.py``` est légèrement retardé au démarrage par le ```time.sleep(0.01)```.
Il devrait donc en résulter un entrelacement entre les phrases ```programme A en cours``` et ```programme B en cours```.  

L'exécution «d'apparence simultanée» de ces deux programmes peut se faire dans un Terminal via la commande ```python3 progA.py & python3 progB.py```.

Il en résulte ceci :

Nous retrouvons bien l'alternance prévue à la lecture du code.  
Tout se passe donc comme si les deux processus avaient été lancés et traités simultanément.

Réduisons maintenant les temporisations (en passant du centième de seconde à la milliseconde): 

```python title="progA.py"
import time

for i in range(10):
    print("programme A en cours, itération", i)
    time.sleep(0.002)  
```

```python title="progB.py"
import time
time.sleep(0.001)
for i in range(10):
    print("programme B en cours, itération", i)
    time.sleep(0.002)  
```

Il en résulte maintenant ceci :

L'alternance prévue n'est plus respectée (et les résultats deviennent non-reproductibles).

Si la gestion des processus était réellement simultanée, même en considérant des ralentissements du processeur par des sollicitations extérieures, chaque processus serait ralenti de la même manière : l'entrelacement des phrases serait toujours le même. 

En réalité, le processeur passe son temps à alterner entre les divers processus qu'il a à gérer, et les met en attente quand il ne peut pas s'occuper d'eux. Il obéit pour cela aux instructions de son **ordonnanceur**.

### 2.2.1 Différents types d'ordonnancement

Si on vous donne 4 tâches A, B, C et D à accomplir, vous pouvez décider :

- de faire la tâche prioritaire d'abord ;
- de faire la tâche la plus rapide d'abord ;
- de faire la tâche la plus longue d'abord ;
- de les faire dans l'ordre où elles vous ont été données ;
- de faire à tour de rôle chaque tâche pendant un temps fixe jusqu'à ce qu'elles soient toutes terminées;
- ...

Un processeur est confronté aux mêmes choix : comment déterminer quel processus doit être traité à quel moment ?

Le schéma ci-dessous (issu de ce site) présente quelques politiques d'ordonnancement :

Sous Linux, l'ordonnancement est effectué par un système hybride où les processus sont exécutés à tour de rôle (on parle de *tourniquet* ou de *Round Robin*) suivant un ordre de priorité dynamique.

> Dans le cas (très fréquent maintenant) d'un processeur *multi-cœurs*, le problème reste identique. Certes, sur 4 cœurs, 4 processus pourront être traités simultanément (une **réelle** simultanéité) mais il reste toujours beaucoup plus de processus à traiter que de cœurs dans le processeur... et un ordonnancement est donc toujours nécessaire.

### 2.2.2 Les différents états d'un processus

Selon que l'ordonnanceur aura décidé de le confier ou non au processeur pour son exécution, un processus peut donc se trouver dans 3 états :

- **Prêt** : il attend qu'arrive le moment de son exécution.
- **Élu** : il est en cours d'exécution par le processeur.
- **Bloqué** : pendant son exécution (état **Élu**), le processus réclame une ressource qui n'est pas immédiatement disponible. Son exécution s'interrompt. Lorsque la ressource sera disponible, le processus repassera par l'état **Prêt** et attendra à nouveau son tour. 

Voici les transitions possibles entre ces états (diagramme issu de https://info.blaisepascal.fr/nsi-processus-et-ressources) : 

Ou de manière simplifiée :

On peut utiliser la métaphore suivante :

Sur le bureau d'un professeur, il y a 3 paquets de copies, correspondant aux classes A, B, et C. Ces paquets sont **Prêts** à être corrigés.

- Si le professeur ramène devant lui le paquet A, celui-ci devient **Élu**, et le professeur peut commencer à le corriger.
- Pour se changer les idées, il peut interrompre la correction du paquet A (qui repassera à l'état **Prêt** en attendant son tour) et ramener vers lui le paquet C. Il pourra ensuite prendre le paquet B, puis à nouveau le C, puis le A, ainsi de suite jusqu'à ce que tous les paquets soient totalement corrigés. Ces paquets seront alors **Terminés**. 
- Si, pendant la correction du paquet, le professeur donne celui-ci à sa fille pour qu'elle classe les copies par ordre alphabétique, ce paquet sera **Bloqué**. Il ne reviendra à l'état **Prêt** que quand la fille du professeur aura rendu le paquet.

Au cours de cette procédure, le professeur n'a toujours eu devant lui qu'**un seul paquet de copies** (soit A, soit B, soit C).

**Pourquoi l'accès à une ressource peut bloquer un processus ?**

Pendant son exécution, un processus peut avoir besoin d'accéder à une ressource déjà occupée (un fichier déjà ouvert, par exemple) ou être en attente d'une entrée-utilisateur (un ```input()``` dans un code ```Python``` par exemple). Dans ce cas-là, le processeur va passer ce processus à l'état **Bloqué**, pour pouvoir ainsi se consacrer à un autre processus.

Une fois débloqué, le processus va repasser à l'état **Prêt** et rejoindre (par exemple) la file d'attente des processus avant d'être à nouveau **Élu** et donc exécuté.

### 3.1 Définition et exemple

Comme nous venons de le voir, un processus peut être dans l'état bloqué dans l'attente de la libération d'une ressource. 

Ces ressources (l'accès en écriture à un fichier, à un registre de la mémoire...) ne peuvent être données à deux processus à la fois. Des processus souhaitant accéder à cette ressource sont donc en concurrence sur cette ressource. Un processus peut donc devoir attendre qu'une ressource se libère avant de pouvoir y accéder (et ainsi passer de l'état Bloqué à l'état Prêt).

**Problème :** Et si deux processus se bloquent mutuellement la ressource dont ils ont besoin ?

**Exemple :** Considérons 2 processus A et B, et deux ressources R et S. L'action des processus A et B est décrite ci-dessous :

**Déroulement des processus A et B :**

- A et B sont créés et passent à l'état **Prêt**.
- L'ordonnanceur déclare **Élu** le processus A (ou bien B, cela ne change rien).
- L'étape A1 de A est réalisée : la ressource R est donc affectée à A.
- L'ordonnanceur déclare maintenant **Élu** le processus B. A est donc passé à **Prêt** en attendant que son tour revienne.
- L'étape B1 de B est réalisée : la ressource S est donc affectée à B.
- L'ordonnanceur déclare à nouveau **Élu** le processus A. B est donc passé à **Prêt** en attendant que son tour revienne.
- L'étape A2 de A est donc enclenchée : problème, il faut pour cela pouvoir accèder à la ressource S, qui n'est pas disponible. L'ordonnanceur va donc passer A à **Bloqué** et va revenir au processus B qui redevient **Élu**.
- L'étape B2 de B est donc enclenchée : problème, il faut pour cela pouvoir accèder à la ressource R, qui n'est pas disponible. L'ordonnanceur va donc passer B à **Bloqué**.

Les deux processus A et B sont donc dans l'état **Bloqué**, chacun en attente de la libération d'une ressource bloquée par l'autre : ils se bloquent mutuellement.

Cette situation (critique) est appelée **interblocage** ou **deadlock**.

### 3.3 Représentation schématique

- les processus seront représentés par des **cercles**, les ressources par des **carrés**.
- Si à l'étape A1 le processus A a demandé et **reçu** la ressource R, la représentation sera :

- Si à l'étape A2 le processus A est **en attente** de la ressource S, la représentation sera :

Avec ces conventions, la situation précédente peut donc se schématiser par :

Ce type de schéma fait apparaître un **cycle d'interdépendance**, qui caractérise ici la situation de deadlock.

### 3.4 Comment s'en prémunir ? *(HP)*

Il existe trois stratégies pour éviter les interblocages :

- **la prévention** : on oblige le processus à déclarer à l'avance la liste de toutes les ressources auxquelles il va accéder.
- **l'évitement** : on fait en sorte qu'à chaque étape il reste une possibilité d'attribution de ressources qui évite le deadlock.
- **la détection/résolution** : on laisse la situation arriver jusqu'au deadlock, puis un algorithme de résolution détermine quelle ressource libérer pour mettre fin à l'interblocage.

### 3.5 Le deadlock dans la vie courante

#### 3.5.1 L'emballage diabolique

#### 3.5.2 Le carrefour maudit

#### 3.5.3 Le rond-point fatal

#### 3.5.4 Le chômage éternel

    - http://info-mounier.fr/terminale_nsi/archi_se_reseaux/processus.php
    - http://lycee.educinfo.org/index.php?page=creation_thread&activite=processus
    - https://www.lecluse.fr/nsi/NSI_T/archi/process/
    - http://www.uqac.ca/pguerin/8INF341/Cours9_Interblocage.html}
    - http://www-inf.it-sudparis.eu/cours/AlgoRep/Web/8.25.html

### Introduction

**Partie A**

    Cette partie est un questionnaire à choix multiples (QCM).
    Pour chacune des questions, une seule des quatre réponses est exacte.

    1. Parmi les commandes ci-dessous, laquelle permet d’afficher les processus en cours
    d’exécution ?
        - a. ```dir```
        - b. ```ps``` 
        - c. ```man``` 
        - d.   ```ls```
    2. Quelle abréviation désigne l’identifiant d’un processus dans un système d’exploitation de type UNIX ?
        - a. PIX
        - b. SIG 
        - c. PID 
        - d. SID
    3. Comment s'appelle la gestion du partage de processeur entre les différents processus ?
        - a. L'interblocage
        - b. L'ordonnancement
        - c. La planification
        - d. La priorisation
    4. Quelle commande permet d’interrompre un processus dans un système d’exploitation de type
    UNIX ?
        - a. ```stop```
        - b. ```interrupt``` 
        - c. ```end``` 
        - d.   ```kill```

    

    **Partie B**

    **Q1.** Un processeur choisit à chaque cycle d’exécution le processus qui doit être exécuté. Le
    tableau ci-dessous donne pour trois processus P1, P2, P3 :

    - la durée d’exécution (en nombre de cycles),
    - l’instant d’arrivée sur le processeur (exprimé en nombre de cycles à partir de 0),
    - le numéro de priorité.

    Le numéro de priorité est d’autant plus petit que la priorité est grande. On suppose qu’à chaque instant, c’est le processus qui a le plus petit numéro de priorité qui est exécuté, ce qui peut provoquer la suspension d’un autre processus, lequel reprendra lorsqu’il sera le plus prioritaire.

    
    Reproduire le tableau ci-dessous sur la copie et indiquer dans chacune des cases le processus
    exécuté à chaque cycle.
    

    

        

    **Q2.** On suppose maintenant que les trois processus précédents s’exécutent et utilisent une ou plusieurs ressources parmi R1, R2 et R3.
    Parmi les scénarios suivants, lequel provoque un interblocage ? Justifier.
 

    _2021, Métropole Candidats Libres sujet 2_

    **Q1.** Les états possibles d’un processus sont : *prêt*, *élu*, *terminé* et *bloqué*.

    **Q1.a.** Expliquer à quoi correspond l’état *élu*.  
    **Q1.b.** Proposer un schéma illustrant les passages entre les différents états.

    

       

    **Q2.** On suppose que quatre processus C₁, C₂, C₃ et C₄ sont créés sur un ordinateur,
    et qu’aucun autre processus n’est lancé sur celui-ci, ni préalablement ni pendant
    l’exécution des quatre processus.
    L’ordonnanceur, pour exécuter les différents processus prêts, les place dans une
    structure de données de type file. Un processus prêt est enfilé et un processus
    élu est défilé.
    

    **Q2.a.** Parmi les propositions suivantes, recopier celle qui décrit le fonctionnement
    des entrées/sorties dans une file :  

    - i.Premier entré, dernier sorti
    - ii. Premier entré, premier sorti
    - iii. Dernier entré, premier sorti

    

    **Q2.b.** On suppose que les quatre processus arrivent dans la file et y sont placés
    dans l’ordre C₁, C₂, C₃ et C₄.

    - Les temps d’exécution totaux de C₁, C₂, C₃ et C₄ sont respectivement
    100 ms, 150 ms, 80 ms et 60 ms.
    - Après 40 ms d’exécution, le processus C₁ demande une opération d’écriture
    disque, opération qui dure 200 ms. Pendant cette opération d’écriture, le
    processus C₁ passe à l’état bloqué.
    - Après 20 ms d’exécution, le processus C₃ demande une opération d’écriture
    disque, opération qui dure 10 ms. Pendant cette opération d’écriture, le
    processus C₃ passe à l’état bloqué.

    Sur la frise chronologique ci-dessous, les
    états du processus C₂ sont donnés. Compléter la frise avec les états des
    processus C₁, C₃ et C₄.

    _2021, sujet Amérique du Nord_

    Un constructeur automobile utilise des ordinateurs pour la conception de ses véhicules.
    Ceux-ci sont munis d'un système d'exploitation ainsi que de nombreuses applications parmi lesquelles on peut citer :

    - un logiciel de traitement de texte ;
    - un tableur ;
    - un logiciel de Conception Assistée par Ordinateur (CAO) ;
    - un système de gestion de base de données (SGBD)

    Chaque ordinateur est équipé des périphériques classiques : clavier, souris, écran et est relié à une imprimante réseau.

    1. *(question System On Chip)*
    2. Un ingénieur travaille sur son ordinateur et utilise les quatre applications citées au début de l'énoncé.  
    Pendant l'exécution de ces applications, des processus mobilisent des données et sont en attente d'autres données mobilisées par d'autres processus.  
    On donne ci-dessous un tableau indiquant à un instant précis l'état des processus en cours d'exécution et dans lequel D1, D2, D3, D4 et D5 sont des données.

    La lettre M signifie que la donnée est mobilisée par l'application ; la lettre A signifie que l'application est en attente de cette donnée.

    Lecture du tableau : le logiciel de traitement de texte mobilise (M) la donnée D1 et est en attente (A) de la donnée D2.

    | | D1 | D2 | D3 | D4 | D5|
    |:---:|:---:|:---:|:---:|:---:|:---:|
    | Traitement de texte | M | A |-|-|-|
    | Tableur | A | - |-|-|M|
    | SGBD | - | M |A|A|-|
    | CAO | - | - |A|M|A|

    Montrer que les applications s'attendent mutuellement. Comment s'appelle cette situation ?
   

    _2021, Métropole sujet 2_

    **Partie A**

    Dans un bureau d’architectes, on dispose de certaines ressources qui ne peuvent être utilisées
    simultanément par plus d’un processus, comme l’imprimante, la table traçante, le modem.
    Chaque programme, lorsqu’il s’exécute, demande l’allocation des ressources qui lui sont
    nécessaires. Lorsqu’il a fini de s’exécuter, il libère ses ressources.

    

    On appelle p1, p2 et p3 les processus associés respectivement aux programmes 1, 2 et 3

    **Q1.** Les processus s'exécutent de manière concurrente.
    Justifier qu'une situation d'interblocage peut se produire.

    

        

    **Q2**. Modifier l'ordre des instructions du programme 3 pour qu'une telle situation ne puisse pas se produire. Aucune justification n'est attendue.

    
 
        

    **Q3**. Supposons que le processus p1 demande la table traçante alors qu'elle est en cours
    d'utilisation par le processus p3. Parmi les états suivants, quel sera l'état du processus p1
    tant que la table traçante n'est pas disponible :
    
        - a. élu
        - b. bloqué
        - c. prêt
        - d. terminé

    
        

    **Partie B**

    Avec une ligne de commande dans un terminal sous Linux, on obtient l'affichage suivant :

    

    La documentation Linux donne la signification des différents champs :

    - `UID` : identifiant utilisateur effectif ;
    - `PID` : identifiant de processus ;
    - `PPID` : `PID` du processus parent ;
    - `C` : partie entière du pourcentage d'utilisation du processeur par rapport au temps de vie
    des processus ;
    - `STIME` : l'heure de lancement du processus ;
    - `TTY` : terminal de contrôle
    - `TIME` : temps d'exécution
    - `CMD` : nom de la commande du processus

    **Q1.** Parmi les quatre commandes suivantes, laquelle a permis cet affichage ?

    - a. ```ls -l``` 
    - b. ```ps -ef``` 
    - c. ```cd ..``` 
    - d. ```chmod 741 processus.txt``` 

    **Q2.** Quel est l'identifiant du processus parent à l'origine de tous les processus concernant le
    navigateur Web (chromium-browser) ?

    **Q3.** Quel est l'identifiant du processus dont le temps d'exécution est le plus long ?
        

    Exercice 2 du sujet Amérique du Nord J2 2022

    

    

    

    

    

    

    

    

    

    

    

    {{
    correction(False,
    """
\"Correction Q4.b.\" 
        En inversant la demande de R3 et R1 pour le processus P3, le risque d'interblocage disparaît.
        Fichier svg d'explication
    """
    )
    }}
        

    Exercice 2 du sujet Polynésie J1 2023

    

    

    **Q2.a.**
    ```python
    class Processus:
        def __init__(self, pid, duree):
            self.pid = pid
            self.duree = duree
            # Le nombre de cycle qui restent à faire :
            self.reste_a_faire = duree
            self.etat = "Prêt"
    ```

    

    **Q2.b.**
    ```python
    def execute_un_cycle(self):
        ...
    
    def change_etat(self, nouvel_etat):
        ...
    
    def est_termine(self):
        ...
    ```

    

    **Q2.c.**
    ```python
    def tourniquet(liste_attente, quantum):
        ordre_execution = []
        while liste_attente != []:
            processus = liste_attente.pop(0)
            processus.change_etat('En cours d exécution')
            compteur_tourniquet = 0
            while ... and ...:
                ordre_execution.append(...)
                processus.execute_un_cycle()
                compteur_tourniquet = compteur_tourniquet + 1
            if ...:
                processus.change_etat('Suspendu')
                liste_attente.append(processus)
            else:
                processus.change_etat(...)
        return ordre_execution
    ```
        

    Exercice 2 du sujet 0 version B 2024

    {{
    correction(True,
    """
\"Correction Q1\" 
        Dans un logiciel libre, le code-source est disponible, peut être amélioré et redistribué par les utilisateurs (voir ici).

        Dans un logiciel propriétaire le code-source n'est pas disponible.

    """
    )
    }}
        

    Exercice 1 du sujet Amérique du Nord J1 2024

    

 

    

    
    ```python linenums='1'
        class File:
            def __init__ (self):
                """ Crée une file vide """
                self.contenu = []
            
            def enfile(self, element):
                """ Enfile element dans la file """
                self.contenu.append(element)
            
            def defile (self):
                """ Renvoie le premier élément de la file et l'enlève de la file """
                return self.contenu.pop(0)

            def est_vide(self):
                """ Renvoie True si la file est vide, False sinon """
                return self.contenu == []
    ```

    

    

    

    Pour tester votre code de la question Q6, vous pouvez utiliser le code suivant (qui propose une implémentation de la classe ```Processus```, qui n'est pas donnée dans l'énoncé)

    ```python linenums='1'

    class Ordonnanceur:	
        def __init__(self):
            self.temps = 0
            self.file = File()
            
        def ajoute_nouveau_processus(self, proc):
            """Ajoute un nouveau processus dans la file de l'ordonnanceur. """
            ...
            
        def tourniquet (self) :
            """Effectue une étape d'ordonnancement et renvoie le nom du processus élu."""
            self.temps += 1
            if not self.file.est_vide():
                proc = ...
                ...
                if not proc.est_fini ():
                    ...
                return proc.nom
            else:
                return None

    class Processus:
        def __init__(self, nom, duree):
            self.nom = nom
            self.duree = duree
            self.exectime = 0
        
        def execute_un_cycle(self):
            self.exectime += 1
        
        def est_fini(self):
            return self.exectime == self.duree

    p1 = Processus("p1", 4)
    p2 = Processus("p2", 3)
    p3 = Processus("p3", 5)
    p4 = Processus("p4", 3)
    depart_proc = {0: p1, 1: p3, 2: p2, 3: p4}
    ```

## Protocoles de routage

### 0. Résumé des épisodes précédents

- cours de 1ère sur l'architecture d'un réseau
- cours de 1ère sur les différents protocoles de communication dans un réseau.

    
    
    Lorsqu'une machine A, d'adresse IP_A veut discuter avec une machine B, d'adresse IP_B :

    - La machine A calcule (grâce au masque de sous-réseau) si B est dans le même sous-réseau qu'elle, ou pas.
    - Si oui, elle peut donc connaître l'adresse MAC de la carte réseau de la machine B (soit elle la possède déjà dans sa table ARP, soit elle la demande en envoyant un message de broadcast à tout le sous-réseau : «qui possède cette adresse IP_B ?»).
    Elle envoie donc dans le sous-réseau une trame ayant pour entête l'adresse MAC de B : le switch lit cette trame, sait sur quel port est branché la machine B et lui envoie spécifiquement donc le message.
    - Si B n'est pas dans le même sous-réseau que A, A mettra en entête de sa trame l'adresse MAC de la carte réseau du routeur, qui joue le rôle de passerelle. Le routeur va ouvrir la trame et va observer l'IP_B, à qui il doit remettre ce message. C'est maintenant que vont intervenir les protocoles de routage :
        - est-ce que B est dans le même sous-réseau que le routeur ?
        - est-ce que B est dans un autre sous-réseau connu du routeur ?
        - est-ce que B est totalement inconnu du routeur ?

    Ces questions trouveront des réponses grâce à **table de routage** du routeur.

### 1. Tables de routage

Les tables de routage sont des informations stockées dans le routeur permettant d'aiguiller intelligemment les données qui lui sont transmises.

Dans le réseau ci-dessus, si l'ordinateur d'adresse ```192.168.0.5``` veut interroger le serveur ```10.7.3.8``` :

- l'adresse ```10.7.3.8``` n'étant pas dans le sous-réseau F (d'adresse ```192.168.0.0 / 24```), la requête est confiée au routeur R1 via son adresse passerelle dans le réseau F (ici ```192.168.0.254```).
- le routeur R1 observe si l'IP recherchée appartient à un autre des sous-réseaux auquel il est connecté. Ici, l'IP recherchée ```10.7.3.8``` n'appartient ni au sous-réseau A, ni au sous-réseau E. 
- le routeur R1 va donc regarder dans sa table de routage l'adresse passerelle d'un autre routeur vers qui elle doit rediriger les données. Si le sous-réseau C fait partie de sa table de routage, le routeur R1 saura alors que le meilleur chemin est (par exemple) de confier les données au routeur R3.
- si le sous-réseau C ne fait pas partie de la table de routage, le routeur R1 va alors le rediriger vers une route «par défaut» (que l'on peut assimiler au panneau «toutes directions» sur les panneaux de signalisation).

    Les tables de routage des routeurs font très souvent apparaître deux colonnes, _interface_ et _passerelle_, dont il ne faut pas confondre l'utilité :

    - **interface** : c'est l'adresse IP de la carte réseau du routeur par où va **sortir** le paquet à envoyer. Il y a donc **toujours** une adresse d'interface à renseigner (car un paquet sort bien de quelque part !). Parfois cette interface sera juste nommée _interface1_ ou _interface2_.

    - **passerelle** : c'est l'adresse IP de la carte réseau du routeur **à qui on va confier le paquet**, si on n'est pas capable de le délivrer directement (donc si l'adresse IP de destination n'est pas dans notre propre sous-réseau). Cette adresse de passerelle n'est donc pas _systématiquement_ mentionnée. Quand elle l'est, elle donne le renseignement sur le prochain routeur à qui le paquet est confié.

**Exemple: table de routage du routeur R1**

**Table de routage du routeur R1 :**

| Destination | Interface | Passerelle |
|:-:|-|-|
| F | 192.168.0.254 | | 
| A | 10.0.5.152 | |
| E | 172.17.1.254 | |  
| B | 172.17.1.254 |172.17.1.123| 
| C | 10.0.5.152 |10.0.5.135| 

Les trois réseaux F, A et E sont directement accessibles au routeur R1, puisqu'il en fait partie : il n'a donc pas besoin d'adresse passerelle pour communiquer avec ces réseaux.

Par contre, la communication avec le réseau B nécessite de confier le paquet au routeur R2 (c'est le choix de cette table de routage). Il faut donc mentionner l'adresse IP de ce routeur R2 (172.17.1.123), qu'on appelle adresse de passerelle.

De la même manière, la communication avec le réseau C nécessite de confier le paquet au routeur R3 (c'est le choix de cette table de routage). Il faut donc mentionner l'adresse IP de ce routeur R3 (10.0.5.135).

#### Comment sont construites les tables de routage ?
- Soit à la main par l'administrateur réseau, quand le réseau est petit : on parle alors de table **statique**.
- Soit de manière **dynamique** : les réseaux s'envoient eux-mêmes des informations permettant de mettre à jour leurs tables de routages respectives. Des algorithmes de détermination de meilleur chemin sont alors utilisés : nous allons en découvrir deux, le protocole RIP et le protocole OSPF.

### 2. Le protocole RIP

_voir le TP débranché_ : le jeu dont vous êtes le routeur

    Le Routing Information Protocol (RIP) est basé sur l'échange (toutes les 30 secondes) des tables de routage de chaque routeur.  
    Au début, chaque routeur ne connaît que les réseaux auquel il est directement connecté, associé à la distance 1.  
    Ensuite, chaque routeur va recevoir périodiquement (toutes les 30 secondes) la table des réseaux auquel il est connecté, et mettre à jour sa propre table suivant les règles ci-dessous :

    - s'il découvre une route vers un nouveau réseau inconnu, il l'ajoute à sa table en augmentant de 1 la distance annoncée par le routeur qui lui a transmis sa table.

    - s'il découvre une route vers un réseau connu mais plus courte (en rajoutant 1) que celle qu'il possède dans sa table,  il actualise sa table.

    - s'il découvre une route vers un réseau connu mais plus longue que celle qu'il possède dans sa table, il ignore cette route.

    - s'il reçoit une route vers un réseau connu en provenance d'un routeur déjà existant dans sa table, s'il met à jour sa table car la topologie du réseau a été modifiée.

    - si le réseau n'évolue pas (panne ou ajout de nouveau matériel), les tables de routage _convergent_ vers une valeur stable. Elles n'évoluent plus.

    - si un routeur ne reçoit pas pendant 3 minutes d'information de la part d'un routeur qui lui avait auparavant communiqué sa table de routage, ce routeur est considéré comme en panne, et toutes les routes passant par lui sont affectées de la distance infinie : 16.

    Le protocole RIP cherche à minimiser **le nombre de sauts**, donc le nombre de routeurs traversés. 

    En extrapolant un peu, on peut dire que RIP minimise **la distance parcourue**.

**Remarques et inconvénients:** 

- Le protocole RIP n'admet qu'une distance maximale égale à 15 (ceci explique que 16 soit considéré comme la distance infinie), ce qui le limite aux réseaux de petite taille.

- Chaque routeur n'a jamais connaissance de la topologie du réseau tout entier : il ne le connaît que par ce que les autres routeurs lui ont raconté. On dit que ce protocole de routage est du _routing by rumor_.

- La _métrique_ utilisée (le nombre de sauts) ne tient pas compte de la qualité de la liaison, contrairement au protocole OSPF.

### 3. Le protocole OSPF

OSPF : *Open Shortest Path First*

Un inconvénient majeur du protocole précédent est la non-prise en compte de la bande passante reliant les routeurs.

    Le chemin le plus rapide n'est pas forcément le plus court.

En gris, le chemin RIP. En bleu, l'OSPF.

Dans le protocole OSPF, les tables de routage vont prendre en considération la vitesse de communication entre les routeurs.

Dans une première phase d'initialisation, chaque routeur va acquérir (par succession de messages envoyés et reçus) la connaissance **totale** du réseau (différence fondamentale avec RIP) et de la qualité technique de la liaison entre chaque routeur.

#### 3.1 Les différents types de liaison et leur coût
On peut, approximativement, classer les types de liaison suivant ce tableau de débits **théoriques** :

| Technologie | BP descendante | BP montante |
|-|-|-|
| Modem | 56 kbit/s | 48 kbit/s |
| Bluetooth | 3 Mbit/s | 3 Mbit/s |
| Ethernet | 10 Mbit/s | 10 Mbit/s |
| Wi-Fi |  10 Mbit/s ~ 10 Gbits/s | 10 Mbit/s ~ 10 Gbits/s |
| ADSL | 13 Mbit/s | 1 Mbit/s |
| 4G | 100 Mbit/s | 50 Mbit/s |
| Satellite | 50 Mbit/s | 1 Mbit/s |
| Fast Ethernet | 100 Mbit/s | 100 Mbit/s |
| FFTH (fibre) | 10 Gbit/s | 10 Gbit/s |
| 5G | 20 Gbit/s | 10 Gbit/s |

L'idée du protocole OSPF est de pondérer chaque trajet entre routeurs (comptant simplement pour «1» dans le protocole RIP) par une valeur de **coût** inversement proportionnelle au débit de transfert.

Par exemple, si le débit $d$ est exprimé en bits/s, on peut calculer le coût de chaque liaison par la formule :

$$ \text{coût} = \frac{10^8}{d} $$

Cette formule de calcul peut être différente suivant les exercices, et sera systématiquement redonnée. Néanmoins la valeur $d$ sera toujours au dénominateur, pour assurer la proportionnalité inverse du débit.

Avec cette convention, un route entre deux routeurs reliés en Fast Ethernet (100 Mbits/s) aura a un poids de 1, une liaison satellite de 20 Mbits/s aura un poids de 5, etc.

### 3.2 Exemple

Reprenons le réseau suivant :

et simplifions-le en ne gardant que les liens entre routeurs, en indiquant leur débit :

Notre réseau est devenu un **graphe**. 

Nous allons pondérer ses arêtes avec la fonction coût introduite précédemment. L'unité étant le Mbit/s, l'arête entre R1 et R3 aura un poids de $\frac{100}{20}=5$.

Le graphe pondéré est donc :

Le chemin le plus rapide pour aller de l'ordinateur au serveur est donc R1-R2-R4, et non plus R1-R3 comme l'aurait indiqué le protocole RIP.

    Le protocole OSPF cherche à minimiser **le temps de parcours**, en choisissant les lignes les plus rapides.

On peut donc retenir la différence fondamentale :
 
- RIP cherche le chemin le plus court.
- OSPF cherche le chemin le plus rapide.

### 3.3 Trouver le plus court chemin dans un graphe pondéré

L'exemple précédent était très simple et de solution intuitive. Dans le cas d'un graphe pondéré complexe, existe-t-il un algorithme de détermination du plus court chemin d'un point à un autre ?

La réponse est **oui**, depuis la découverte en 1959 par Edsger Dijkstra de l'algorithme qui porte son nom, **l'algorithme de Dijkstra**.

Pour le comprendre, vous pouvez regarder la vidéo d'un célèbre YouTuber :

Cet algorithme, ici exécuté de manière manuelle, est bien sûr programmable. Et c'est donc grâce à lui que chaque routeur calcule la route la plus rapide pour acheminer les données qu'il reçoit.

      
    Donner le plus court chemin pour aller de E à F dans le graphe ci-dessous :

    
    On considère le réseau suivant :

    

    On rappelle que le coût d’une liaison est donné par la formule suivante :

    $$ \text{coût} = \frac{10^8}{d} $$

    **Question 1**

    a. Vérifier que le coût de la liaison entre les routeurs A et B est 0,01.

    b. La liaison entre le routeur B et D a un coût de 5. Quel est le débit de cette liaison ?

    {{
    correction(True,
    """
\"Correction\" 
        **Q1**  
            a. $\\text{coût} = \\dfrac{10^8}{10 \\times 10^9}= \\dfrac{10^8}{10^{10}}= 10^{-2}=0,01$  
            b. $5=\\dfrac{10^8}{d}$ donc $d=\\dfrac{10^8}{5}=20 \\times 10^6$ = 20 Mb/s        
    """
    )
    }}

    **Question 2**

    Le routeur A doit transmettre un message au routeur G, en empruntant le chemin dont la somme des coûts sera la plus petite possible. Déterminer le chemin parcouru. On indiquera le raisonnement utilisé.

    

    

---

    - Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
    - Prépabac NSI, Terminale, G. CONNAN, V. PETROV, G. ROZSAVOLGYI, L. SIGNAC, éditions HATIER.
    - Site d'Olivier Lécluse https://lecluseo.frama.io/leclusemaths/nsi/NSI_T/archi/

---

### Introduction

Dans un réseau quelconque, le coût de chaque liaison se calcule par la formule :

    $$ \text{coût} = \frac{10^8}{d} $$

    où le débit $d$ est exprimé en bits/s.

    Calculer le coût si la liaison a un débit de :

    **A.** 10 Mb/s

    **B.** 1 Gb/s

    **C.** 1 Mb/s

    **D.** 50 Mb/s

    {{
    correction(True,
    """
\"Correction \" 
        - **A.** $c = \\dfrac{10^8}{10 \\times 10^6} = \\dfrac{10^8}{10^7}= 10$
        - **B.** $c = \\dfrac{10^8}{10^9} = 10^{-1}= 0,1$
        - **C.** $c = \\dfrac{10^8}{10^6} = 10^2= 100$
        - **D.** $c = \\dfrac{10^8}{50 \\times 10^6} = \\dfrac{10^2}{50}=2$
    """
    )
    }}

    Exercice 5 du sujet La Réunion J1 2022

    _2020, sujet 0_

    On considère un réseau composé de plusieurs routeurs reliés de la façon suivante :

    

    Le protocole RIP permet de construire les tables de routage des différents routeurs, en indiquant pour chaque routeur la distance, en nombre de sauts, qui le sépare d’un autre routeur. Pour le réseau ci-dessus, on dispose des tables de routage suivantes :

    

    **Question 1**

    1.1 Le routeur A doit transmettre un message au routeur G, en effectuant un nombre minimal de
    sauts. Déterminer le trajet parcouru.
    
    1.2. Déterminer une table de routage possible pour le routeur G obtenue à l’aide du protocole RIP.
    

    **Question 2**

    Le routeur C tombe en panne. Reconstruire la table de routage du routeur A en suivant le
    protocole RIP.

    _2021, sujet Métropole 1_

    On représente ci-dessous un réseau dans lequel R1, R2, R3, R4, R5 et R6 sont des
    routeurs. Le réseau local L1 est relié au routeur R1 et le réseau local L2 au routeur R6.

    

    Dans cet exercice, les adresses IP sont composées de 4 octets, soit 32 bits. Elles sont notées X1.X2.X3.X4, où X1, X2, X3 et X4 sont les valeurs des 4 octets, convertis en notation décimale.
    La notation X1.X2.X3.X4/n signifie que les n premiers bits de poids forts de l’adresse IP représentent la partie « réseau », les bits suivants représentent la partie « hôte ».
    Toutes les adresses des hôtes connectés à un réseau local ont la même partie réseau et peuvent donc communiquer directement. L’adresse IP dont tous les bits de la partie « hôte » sont à 0 est appelée « adresse du réseau ».

    On donne également des extraits de la table de routage des routeurs R1 à R5 dans le
    tableau suivant :

    

    1/ Un paquet part du réseau local L1 à destination du réseau local L2.

    1.a. En utilisant l’extrait de la table de routage de R1, vers quel routeur R1 envoie-t-il ce paquet : R2 ou R3 ? Justifier.
    

    1.b. A l’aide des extraits de tables de routage ci-dessus, nommer les routeurs traversés par ce paquet, lorsqu’il va du réseau L1 au réseau L2.
    
    2/ La liaison entre R1 et R2 est rompue.

    2.a. Sachant que ce réseau utilise le protocole RIP (distance en nombre de sauts), donner l’un des deux chemins possibles que pourra suivre un paquet allant de L1 vers L2.
    
    2.b. Dans les extraits de tables de routage ci-dessus, pour le chemin de la question 2.a, quelle(s) ligne(s) sera (seront) modifiée(s) ?
    
    3/ On a rétabli la liaison entre R1 et R2.
    Par ailleurs, pour tenir compte du débit des liaisons, on décide d’utiliser le
    protocole OSPF (distance liée au coût minimal des liaisons) pour effectuer le
    routage. Le coût des liaisons entre les routeurs est donné par le tableau suivant :

    

    a. Le coût _C_ d’une liaison est donné ici par la formule
    $C = \dfrac{10^9}{BP}$

    où $BP$ est la bande passante de la connexion en bps (bits par seconde).
    Sachant que la bande passante de la liaison R2-R3 est de 10 Mbps, calculer le coût correspondant.
    {{
    correction(True,
    """
\"Correction\" 
        3.a $\\dfrac{10^9}{10 \\times 10^6}=100$ donc le coût R2-R3 est 100.  
    """
    )
    }}

    b. Déterminer le chemin parcouru par un paquet partant du réseau L1 et arrivant au réseau L2, en utilisant le protocole OSPF.
    
    c. Indiquer pour quel(s) routeur(s) l’extrait de la table de routage sera modifié pour un paquet à destination de L2, avec la métrique OSPF.

    _2021, sujet Métropole 2_ (sujet modifié, correction d'erreurs sur les adresses passerelles)

    |  | 
    |:--:| 
    | *Figure 1* |

    La figure 1 ci-dessus représente le schéma d’un réseau d’entreprise. Il y figure deux réseaux locaux L1 et L2. Ces deux réseaux locaux sont interconnectés par les routeurs R2, R3, R4 et R5. Le réseau local L1 est constitué des PC portables P1 et P2 connectés à la passerelle R1 par le switch Sw1. Les serveurs S1 et S2 sont connectés à la passerelle R6 par le switch Sw2.

    Le tableau 1 suivant indique les adresses IPv4 des machines constituants le réseau de l’entreprise.

    |   | 
    |:--:| 
    | *Tableau 1 : adresses IPv4 des machines* |

    **Rappels et notations**

    Rappelons qu’une adresse IP est composée de 4 octets, soit 32 bits. Elle est notée
    X1.X2.X3.X4, où X1, X2, X3 et X4 sont les valeurs des 4 octets. Dans le tableau 1, les valeurs des 4 octets ont été converties en notation décimale.

    La notation X1.X2.X3.X4/n signifie que les n premiers bits de poids forts de l’adresse IP représentent la partie « réseau », les bits suivants de poids faibles représentent la partie « machine ».

    Toutes les adresses des machines connectées à un réseau local ont la même partie réseau.
    L’adresse IP dont tous les bits de la partie « machine » sont à 0 est appelée « adresse du réseau ».
    L’adresse IP dont tous les bits de la partie « machine » sont à 1 est appelée « adresse de diffusion ».

    1/ 
    1.a. Quelles sont les adresses des réseaux locaux L1 et L2 ?
    
    1.b. Donner la plus petite et la plus grande adresse IP valides pouvant être attribuées à un ordinateur portable ou un serveur sur chacun des réseaux L1 et L2 sachant que l’adresse du réseau et l’adresse de diffusion ne peuvent pas être attribuées à une machine.
    
    1.c. Combien de machines peut-on connecter au maximum à chacun des réseaux locaux L1
    et L2 ? 
    
    2/ 
    2.a. Expliquer l’utilité d’avoir plusieurs chemins possibles reliant les réseaux L1 et L2.
    
    2.b. Quel est le chemin le plus court en nombre de sauts pour relier R1 et R6 ? Donner le nombre de sauts de ce chemin et préciser les routeurs utilisés.
    
    2.c. La bande passante d’une liaison Ether (quantité d’information qui peut être transmise en bits/s) est de $10^7$ bits/s et celle d’une liaison FastEther est de $10^8$ bits/s. Le coût d’une liaison est défini par $\frac{10^8}{d}$ , où $d$ est sa bande passante en bits/s.

    |   | 
    |:--:| 
    | *Tableau 2 : type des liaisons entre les routeurs* |

    Quel est le chemin reliant R1 et R6 qui a le plus petit coût ? Donner le coût de ce chemin et préciser les routeurs utilisés.
    
    3/ Dans l’annexe A figurent les tables de routages des routeurs R1, R2, R5 et R6 au
    démarrage du réseau. Indiquer sur votre copie ce qui doit figurer dans les lignes laissées vides des tables de routage des routeurs R5 et R6 pour que les échanges entre les ordinateurs des réseaux L1 et L2 se fassent en empruntant le chemin le plus court en nombre de sauts.

    _2021, sujet Amérique du Nord_

    Un constructeur automobile possède six sites de production qui échangent des documents entre eux. Les sites de production sont reliés entre eux par six routeurs A, B, C, D, E et F.  
    On donne ci-dessous les tables de routage des routeurs A à F obtenues avec le protocole RIP.

    

    1. Déterminer à l'aide de ces tables le chemin emprunté par un paquet de données envoyé du routeur A vers le routeur F.
        
    2. On veut représenter schématiquement le réseau de routeur à partir des tables de routage. 
    Recopier sur la copie le schéma ci-dessous : 

    

    En s'appuyant sur les tables de routage, tracer les liaisons entre les routeurs.

    Exercice 4 du sujet Nouvelle-Calédonie J2 2022.

    

    
    

    

    

    
    

    

    {{
    correction(True,
    """
\"Correction Q5.a.\" 
        $10=\\dfrac{10^9}{d}$ donc $d=\\dfrac{10^9}{10}=10^8$.

        Le débit de cette liaison est donc de $10^8$ bits par seconde, soit 100 Mbps.
    """
    )
    }}

    Parties 2, 3 et 4 de l'exercice 2 du sujet Nouvelle-Calédonie J1 2022.

    **Correction Partie 2**

    

    

    

    **Correction Partie 3**

    

    

    

    **Correction Partie 4**

    Créer une fonction ```meme_sous_reseau(ip_a, ip_b, masque)``` qui renvoie un booléen indiquant si A et B sont partie du même sous-réseau.

    Exercice (difficile) à réaliser en Test Driven Developpement à partir du squelette de code ci-dessous, en testant chaque fonction après sa réalisation, jusqu'à la fonction finale.

    ```python
    def convert_ip_to_list(ip):
        """
        entrée : ip (string) 
        sortie : liste d'entiers
        """
        # à vous

    def test_convert_ip_to_list():
        assert convert_ip_to_list('192.168.0.1') == [192, 168, 0, 1]
        

    def nb_to_binary_word(masque):
        """
        entrée : masque (int)
        sortie : string
        """
        # à vous
        
    def test_nb_convert_to_binary_word():
        assert nb_to_binary_word(24) == '11111111111111111111111100000000'

    def binary_word_to_list(word):
        """
        entrée : word (string de 32 caractères)
        sortie : liste de 4 entiers
        """
        # à vous

    def test_binary_word_to_list():
        assert binary_word_to_list('11111111111111111111111100000000') == [255, 255, 255, 0]

    def meme_sous_reseau(ip_a, ip_b, masque):
        """
        ip_a:  string contenant une IP (ex "192.168.0.1")
        ip_b : string contenant une IP
        masque : entier du masque en notation CIDR (ex : 24)
        renvoie un booléen indiquant si ip_a et ip_b sont dans
        le même sous-réseau
        """
        # à vous
        

    def test_meme_sous_reseau():
        assert meme_sous_reseau("192.168.0.1", "192.168.1.3", 24) == False
        assert meme_sous_reseau("192.168.0.1", "192.168.1.3", 20) == True
        assert meme_sous_reseau("192.168.0.1", "192.168.0.3", 30) == True
    ```

## Cryptographie

### 1.1 Activité du masque jetable

On considère la variable suivante :

        ```python
        masque = "CETTEPHRASEESTVRAIMENTTRESTRESLONGUEMAISCESTFAITEXPRES"
        ```

        - Créer une fonction ```chiffre(message, masque)``` qui chiffre ```message ``` en le XORant avec ```masque```.
        - Cette fonction doit pouvoir **aussi** servir à déchiffrer le message chiffré.

        - Le ```XOR``` (voir ici{target = "_blank"}) est une opération symétrique :
        ```python
        >>> 34 ^ 23
        53
        >>> 53 ^ 23
        34
        ```
        - La fonction ```ord``` permet de renvoyer le code ASCII d'un caractère. La fonction ```chr``` fait l'opération inverse.
        ```python
        >>> ord('A')
        65
        >>> chr(65)
        'A'
        ```

### 1.2 Principe du chiffrement symétrique

Dans un chiffrement symétrique, c'est **la même clé** qui va servir au chiffrement et au déchiffrement.

*Illustration :*

#### :arrow_right: Qu'appelle-t-on une clé ?
La clé est un renseignement permettant de chiffrer ou déchiffrer un message. Cela peut être :

- un nombre (dans un simple décalage des lettres de l'alphabet, comme le chiffre de César)
- une phrase (dans la méthode du masque jetable)
- une image (imaginez un chiffrement où on effectue un XOR par les pixels d'une image, comme dans cette énigme)

Un chiffrement est dit symétrique lorsque la connaissance de la clé ayant servi au chiffrement permet de déchiffrer le message. Par exemple, Alice chiffre son message en décalant les lettres de 3 rangs vers la droite dans l'alphabet, Bob saura qu'il doit les décaler de 3 rangs vers la gauche pour retrouver le message initial.

#### :arrow_right: Quel est l'avantage d'un chiffrement symétrique ?
Les chiffrements symétriques sont souvent rapides, consommant peu de ressources et donc adaptés au chiffrement de flux important d'informations.

Comme nous le verrons, la sécurisation des données transitant par le protocole ```https``` est basée sur un chiffrement symétrique.

#### :arrow_right: Quel est l'inconvénient d'un chiffrement symétrique ?
La clé ! Si Alice et Bob ont besoin d'utiliser un chiffrement pour se parler, comment peuvent-ils échanger leurs clés  puisque leur canal de transmission n'est pas sûr ?

Le chiffrement symétrique impose qu'Alice et Bob aient pu se rencontrer physiquement au préalable pour convenir d'une clé secrète, ou bien qu'ils aient réussi à établir une connexion sécurisée pour s'échanger cette clé.

#### :arrow_right: Un chiffrement symétrique est-il un chiffrement de mauvaise qualité ?
Pas du tout ! S'il est associé naturellement à des chiffrements simples et faibles (comme le décalage de César), un chiffrement symétrique peut être très robuste... voire inviolable.

C'est le cas du masque jetable. Si le masque avec lequel on effectue le XOR sur le message est aussi long que le message, alors il est **impossible** de retrouver le message initial. Pourquoi ?

Imaginons qu'Alice veuille transmettre le message clair "LUNDI".
Elle le chiffre avec un masque jetable (que connait aussi Bob), et Bob reçoit donc "KHZOK". 
Si Marc a intercepté le message "KHZOK", *même s'il sait que la méthode de chiffrement utilisée est celle du masque jetable* (*principe de Kerckhoffs*), il n'a pas d'autre choix que de tester tous les masques de 5 lettres possibles.
inline end "Principe de Kerckhoffs" 
     La sécurité d'un système de chiffrement ne doit reposer que sur le secret de la clé, et non pas sur la connaissance de l'algorithme de chiffrement. Cet algorithme peut même être public (ce qui est pratiquement toujours le cas).

Ce qui lui donne $26^5$ possibilités (plus de 11 millions) pour le masque, et par conséquent (propriété de bijectivité du XOR) $26^5$ possibilités pour le message «déchiffré»...

Cela signifie que Marc verra apparaître, dans sa tentative de déchiffrage, les mots "MARDI", "JEUDI", "JOUDI", "STYLO", "FSDJK", "LUNDI", "LUNDA"... 
Il n'a aucune possibilité de savoir où est le bon message original parmi toutes les propositions (on parle de *sécurité sémantique*).

#### :arrow_right: Quels sont les chiffrements symétriques modernes ?
L'algorithme de chiffrement symétrique le plus utilisé actuellement est le chiffrement AES, pour Advanced Encryption Standard.

- chiffrement par bloc de 128 bits, répartis dans une matrice de 16 octets (matrice carrée de taille 4).
- ces 128 bits sont transformés par des rotations, multiplications, transpositions, [...] de la matrice initiale, en faisant intervenir dans ces transformations une clé de 128, 192 ou 256 bits.
- pour l'AES-256 (avec une clé de 256 bits), l'attaque par force brute nécessiterait $2^{256}$ opérations, soit un nombre à 78 chiffres...
- il n'existe pas d'attaque connue efficace à ce jour. Les seules attaques sont des attaques sur des faiblesses d'implémentation, ou par canal auxiliaire.

### 2. Chiffrement asymétrique

Inventé par Whitfield Diffie et Martin Hellman en 1976, le chiffrement asymétrique vient résoudre l'inconvénient essentiel du chiffrement symétrique : le nécessaire partage d'un secret (la clé) avant l'établissement de la communication sécurisée.

### 2.1 Principe du chiffrement asymétrique

Le principe de base est l'existence d'une **clé publique**, appelée à être distribuée largement, et d'une **clé privée**, qui ne quitte jamais son propriétaire.

### 2.2 Le rôle interchangeable des clés publiques et privées

L'illustration précédente associe :

- une image de cadenas à la clé publique (car on s'en sert pour chiffrer les messages)
- une image de clé à la clé privée (car on s'en sert pour déchiffrer les messages)

Concrètement, (nous le verrons dans l'application par le chiffrement RSA), la clé privée et la clé publique sont **deux nombres** aux rôles identiques. Appelons-les A et B :

- il est impossible de trouver A en fonction de B. Réciproquement, si on connaît A, il est impossible d'en déduire B.
- si on chiffre un message avec A, on peut le déchiffrer avec B. Réciproquement, si on chiffre avec B, on peut déchiffrer le message grâce à A.
- on peut donc chiffrer avec une clé publique et déchiffrer avec la clé privée associée (ce qui est fait dans l'exemple précédent). Mais on peut aussi chiffrer avec la clé privée, et déchiffrer avec la clé publique associée.

A et B ont donc des rôles interchangeables (chacun peut être un cadenas, chacun peut être une clé), et ce n'est qu'en connaissant A **et** B qu'on peut déchiffrer le message.

Nous allons donc maintenant adopter une nouvelle convention infographique :

- Considérons ce message :

- Si ce message est chiffré avec la clé publique d'Alice, le message sera :

- Si on déchiffre ce message avec la clé privée d'Alice, il deviendra

et donc

puisque l'application de la clé privée sur la clé publique, ou bien de la clé publique sur la clé privée, permet de retrouver le message en clair.

De manière graphique, la connaissance des deux moitiés du disque qui s'assemblent permet de les faire disparaitre, peu importe qu'on ait commencé par chiffrer avec la clé publique ou avec la clé privée.

### 2.3 Communication authentifiée.

Dans la situation du 2.1, Alice (qui a distribué largement sa clé publique) ne peut pas s'assurer que le message vient bien de Bob. Il peut avoir été créé par Marc, qui signe «Bob» et usurpe ainsi son identité. 

Le protocole que nous allons décrire ci-dessous permet :

- d'empêcher qu'un message intercepté soit déchiffré (ce qui était déjà le cas dans le 2.1)
- mais aussi de s'assurer que chaque personne est bien celle qu'elle prétend être : on résout le **problème d'authentification**.

    - Alice est sûre que seul Bob pourra déchiffrer le message qu'elle envoie.
    - Bob est sûr que le message qu'il reçoit vient bien d'Alice.

### 2.3 Un exemple de chiffrement asymétrique : le chiffrement RSA

#### 2.3.1 Histoire
Lorsqu'en 1976 Diffie et Hellman (chercheurs à Stanford) présentent le concept de chiffrement asymétrique (souvent appelé _cryptographie à clés publiques_), ils en proposent uniquement un modèle théorique, n'ayant pas trouvé une réelle implémentation de leur protocole.

Trois chercheurs du MIT (Boston), Ron Rivest, Adi Shamir et Len Adleman se penchent alors sur ce protocole, convaincus qu'il est en effet impossible d'en trouver une implémentation pratique. En 1977, au cours de leurs recherches, ils démontrent en fait l'inverse de ce qu'ils cherchaient : ils créent le premier protocole concret de chiffrement asymétrique : le chiffrement **RSA**.

Au même moment à Londres, Clifford Cocks, (chercheur au très secret GCHQ) apprend que Rivest Shamir et Adleman viennent de découvrir ce que lui-même a découvert **3 ans auparavant** mais qui est resté classé Secret Défense.

Il est le véritable inventeur du RSA... mais le reste du monde ne l'apprendra qu'en 1997 au moment de la déclassification de cette information. 

#### 2.3.1 Description

Le chiffrement RSA est basé sur *l'arithmétique modulaire*. Faire des calculs *modulo* un entier $n$, c'est ne garder que le reste de la division euclidienne par $n$.

Le fait que 15 soit égal à 1 modulo 7 (car $15=2 \times 7+1$) s'écrira $15 \equiv 1 [7]$.

De même, $10 \equiv  3 [7]$, $25 \equiv 4 [7]$, $32 \equiv 2 [10]$, etc.

#### :arrow_right: Étape 1
Alice choisit 2 grands nombres premiers $p$ et $q$. Dans la réalité ces nombres seront vraiment très grands (plus de 100 chiffres). Dans notre exemple, nous prendrons $p = 3$ et $q = 11$.

#### :arrow_right: Étape 2
Alice multiplie ces deux nombres $p$ et $q$ et obtient ainsi un nombre $n$.
>Il est très facile pour Alice de calculer $n$ en connaissant $p$ et $q$, mais il  extrêmement difficile pour Marc de faire le travail inverse : trouver $p$ et $q$ en connaissant $n$ prend un temps exponentiel avec la taille de $n$.  
C'est sur cette difficulté (appelée difficulté de *factorisation*) que repose la robustesse du système RSA.
Le «dernier» (en 2020) grand nombre $n$ factorisé en $p \times q$ avait 250 chiffres, soit une clé de 829 bits. (voir https://en.wikipedia.org/wiki/RSA_Factoring_Challenge)

#### :arrow_right: Étape 3
Alice choisit un nombre $e$ qui doit être premier avec $(p-1)(q-1)$.  On note $\phi(n)$ le nombre $(p-1)(q-1)$.

Dans notre exemple, $(p-1)(q-1) = 20$, Alice choisit donc $e = 3$. (mais elle aurait pu aussi choisir 7, 9, 13...).

Le couple $(e, n)$ sera **la clé publique** d'Alice. Elle la diffuse à qui veut lui écrire.

Dans notre exemple, la clé publique d'Alice est $(3, 33)$.

#### :arrow_right: Étape 4
Alice calcule maintenant sa clé privée : elle doit trouver un nombre *d* qui vérifie l'égalité $e d \equiv 1 [\phi(n)]$.

Dans notre exemple, comme $7 \times 3  \equiv 1 [20]$, ce nombre $d$ est égal à 7.

En pratique, il existe un algorithme simple (algorithme d'Euclide étendu) pour trouver cette valeur $d$, appelée *inverse modulaire de e*. En Python, on utilisera ```pow(3, -1, 20)```. 

Le couple $(d, n)$ sera **la clé privée** d'Alice. Elle ne la diffuse à personne.

Dans notre exemple, la clé privée d'Alice est $(7, 33)$.

#### :arrow_right: Étape 5
Supposons que Bob veuille écrire à Alice pour lui envoyer le nombre 4. 
Il possède la clé publique d'Alice, qui est $(3, 33)$.

Il calcule donc $4^3$ modulo 33, qui vaut 31. C'est cette valeur 31 qu'il transmet à Alice.

$$4^3 \equiv 31 [33]$$

> Si Marc intercepte cette valeur 31, même en connaissant la clé publique d'Alice (3,33), il ne peut pas résoudre l'équation $x^3 \equiv 31 [33]$ de manière efficace.

#### :arrow_right: Étape 6
Alice reçoit la valeur 31.  
Il lui suffit alors d'élever 31 à la puissance 7 (sa clé privée), et de calculer le reste modulo 33 :

$31^7 = 27512614111$

$27512614111 \equiv 4 [33]$

Elle récupère la valeur 4, qui est bien le message original de Bob.

> **Comment ça marche ?**
Grâce au Petit Théorème de Fermat, on démontre (voir ici) assez facilement que $M^{ed} \equiv M [n]$.

Il faut remarquer que $M^{ed} = M^{de}$. On voit que les rôles de la clé publique et de la clé privée sont **symétriques** : un message chiffré avec la clé publique se déchiffrera en le chiffrant avec la clé privée, tout comme un message chiffré avec la clé privée se déchiffrera en le chiffrant avec la clé publique.

    voir https://animations.interstices.info/interstices-rsa/rsa.html

    Le chiffrement RSA a des défauts (notamment une grande consommation des ressources, due à la manipulation de très grands nombres).
    Mais le choix d'une clé publique de grande taille (actuellement 1024 ou 2048 bits) le rend pour l'instant inviolable. 

    Actuellement, il n'existe pas d'algorithme efficace pour factoriser un nombre ayant plusieurs centaines de chiffres.

    Deux évènements pourraient faire s'écrouler la sécurité du RSA :

    - la découverte d'un algorithme efficace de factorisation, capable de tourner sur les ordinateurs actuels. Cette annonce est régulièrement faite, et tout aussi régulièrement contredite par la communauté scientifique. (voir, le 05/03/2021,  https://www.schneier.com/blog/archives/2021/03/no-rsa-is-not-broken.html)
    - l'avènement d'ordinateurs quantiques, dont la vitesse d'exécution permettrait une factorisation rapide. Il est à noter que l'algorithme de factorisation destiné à tourner sur un ordinateur quantique existe déjà : l'algorithme de Schor.

### 3.1 Principe général

Aujourd'hui, plus de 90 % du trafic sur internet est chiffré : les données ne transitent plus en clair (protocole ```http```) mais de manière chiffrée (protocole ```https```), ce qui empêche la lecture de paquets éventuellements interceptés.

Le protocole ```https``` est la réunion de deux protocoles :

-  le protocole ```TLS``` (Transport Layer Security, qui a succédé au SSL) : ce protocole, basé sur du **chiffrement asymétrique**, va conduire à la génération d'une clé identique chez le client et chez le serveur.
- le (bon vieux) protocole  ```http```, mais qui convoiera maintenant des données chiffrées avec la clé générée à l'étape précédente. Les données peuvent toujours être interceptées, mais sont illisibles. Le **chiffrement symétrique** utilisé est actuellement le chiffrement AES.

**Pourquoi ne pas utiliser que le chiffrement asymétrique, RSA par exemple ?**
Car il est très gourmand en ressources ! Le chiffrement/déchiffrement doit être rapide pour ne pas ralentir les communications ou l'exploitation des données.
Le chiffrement asymétrique est donc réservé à l'échange de clés (au début de la communication).
Le chiffrement symétrique, bien plus rapide, prend ensuite le relais pour l'ensemble de la communication.

### 3.2 (HP) Fonctionnement du TLS : explication du *handshake*

Observons en détail le fonctionnement du protocole ```TLS```, dont le rôle est de générer de manière sécurisée une clé dont disposeront à la fois le client et le serveur, leur permettant ainsi d'appliquer un chiffrement symétrique à leurs échanges.

- **étape 1** : le «client Hello». Le client envoie sa version de TLS utilisée. 

- **étape 2** : le «server Hello». Le serveur répond en renvoyant son certificat prouvant son identité, ainsi que sa clé publique.

- **étape 3** : le client interroge l'autorité de certification pour valider le fait que le certificat est bien valide et que le serveur est bien celui qu'il prétend être. Cette vérification est faite grâce à un mécanisme de chiffrement asymétrique.

> La présentation du certificat à l'autorité de certification peut se représenter comme le scan d'une pièce d'identité dans un aéroport. L'autorité de certification est alors l'État (dont la base de données est interrogée par un logiciel) qui valide que la pièce d'identité est bien un document officiel.

- **étape 4** : une fois vérifiée l'authenticité du serveur et que son certificat est valide, le client calcule ce qui sera la future clé de chiffrement symétrique (appelée «clé AES» dans l'infographie). Cette clé est chiffrée avec la clé publique du server (transmise à l'étape 1), ce qui assure la sécurité de son transfert. Le serveur déchiffre cette clé grâce à sa clé privée, et dispose ainsi lui aussi de la clé. 

Le transmission par protocole ```http``` de données chiffrées au préalable avec la clé AES peut commencer. 

>Remarque : en réalité, ce n'est pas la clé AES qui est transmise à l'étape 4, mais un nombre choisi par le client, qui permettra, avec deux autres nombres choisis par le client (étape 1) et le serveur (étape 2) de reconstituer la clé AES, qui sera donc identique côté client et côté serveur.

---

    - Numérique et Sciences Informatiques, Terminale, T. BALABONSKI, S. CONCHON, J.-C. FILLIATRE, K. NGUYEN, éditions ELLIPSES.
    - Prépabac NSI, Terminale, G. CONNAN, V. PETROV, G. ROZSAVOLGYI, L. SIGNAC, éditions HATIER.
    - https://www.cloudflare.com/fr-fr/learning/ssl/what-happens-in-a-tls-handshake/
 

---

### Introduction

**Utilisation des bibliothèques cryptographiques du module ```sympy```.**

    Documentation : https://docs.sympy.org/latest/modules/crypto.html{target="_blank"}

    Décoder la phrase ```RYTVJKGCLJWRTZCVRMVTLEDFULCVHLZWRZKKFLKRMFKIVGCRTV```, sachant qu'elle a été chiffrée par décalage (*shift* en anglais...)

    **Chiffrage affine**

    Principe du chiffrage affine :

    - Chaque lettre est codée par son rang, en commençant à 0 (A->0, B->1, ..., Z->25)
    - On applique à chaque rang la transformation affine 
    $f(x) = (ax+b)\, \%26$

    où $a$ et $b$ sont deux nombres entiers. Attention, $a$ doit être premier avec 26.

        Deux nombres sont dits *premiers entre eux* si leur PGCD vaut 1. 

        Exemples :
        
        - 8 et 15 sont premiers entre eux (ils n'ont aucun diviseur commun autre que 1)
        - 8 et 12 ne sont pas premiers entre eux (leur PGCD vaut 4).

    **Q1.** Codez votre fonction ```affine(msg, a, b)```.

    Pour tester votre fonction :
    ```python
    >>> affine("BONJOUR", 3, 5)
    'IVSGVNE'
    ```

    

    **Q2.** Comparez vos résultats avec ceux obtenus par la fonction ```encipher_affine()``` de ```sympy```.

    **Q3.** Décodez la phrase ```UCGXLODCMOXPMFMSRJCFQOGTCRSUSXC```, sachant qu'elle contient le mot ```TRAVAIL``` et que $a$ et $b$ sont inférieurs à 20.

        L'instruction ```gcd``` du module ```math``` permet de calculer le PGCD de deux nombres.

    Exercice 3 (Parties A et B) du sujet Métropole J2 2025

    **Partie A**

    ```python
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z']
    ```

    

    

    

    ```python
    def indices_vers_lettres(lst):
        s = ''
        for c in lst:
            s += alphabet[c]
        return s
    ```

    ```python
    def chiffrement(msg, cle):
        assert len(cle) >= len(msg), 'impossible'
        indices_msg = lettres_vers_indices(msg)
        indices_cle = lettres_vers_indices(cle)
        n = len(msg)
        indices_msg_chiffre = []
        for k in range(n):
            ind = ...
            if ind >= 26:
                ind = ...
            indices_msg_chiffre.append(ind)
        msg_chiffre = indices_vers_lettres(...)
        return msg_chiffre    
    ```

    

    

    

    

    

    **Partie B**

    **Cryptographie RSA** presque à la main

    ```python linenums='1'
    import Crypto
    import libnum
    from Crypto.Util.number import bytes_to_long, long_to_bytes
    from Crypto.Random import get_random_bytes 

    bits = 256

    p = ...
    q = ...

    n = ...
    phi = ...

    e = 65537  # très souvent choisi comme exposant de chiffrement
    d = ...  # on calcule l'inverse de e modulo phi

    def encipher(msg):
        M = bytes_to_long(msg.encode('utf-8')) # on convertit le message msg en un nombre M
        c = ... # M puissance e modulo n
        return c

    def decipher(c):
        res = ...
        return long_to_bytes(res) # on convertit le nombre res en une chaine de caractères

    ```

    - Pour générer un grand nombre premier de taille ```bits``` , on utilise la fonction ```Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)```.
    - Pour inverser un nombre $x$ modulo $n$, on utilise la fonction    ```pow(x, -1, n)```.
    - Pour calculer ```a``` à la puissance ```b``` modulo ```n```, on utilise ```pow(a, b, n)```.

    En vous servant du code précédent, déchiffrez le message ```58152918114477529438769495136495430966050302170947748011925859233600631318929939319619808279389222131229963717435870597641010567365311762267359794338657867540621133550787677728203831932548041236152866441194127191404729294628415184239755221703677388875259927092794165578604353985011899152968982365630138088486380827379488939561996226754182```  sachant que :

    - $e$ vaut 65537.
    - $p$ et $q$ sont respectivement les 13èmes et 14èmes nombres de Mersenne.

    **module RSA** dans les règles de l'art

    ```python
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    import binascii

    keyPair = RSA.generate(1024)

    pubKey = keyPair.publickey()

    pubKeyPEM = pubKey.exportKey()

    privKeyPEM = keyPair.exportKey()

    msg = b'vive la crypto en NSI !'
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    print("Encrypted:", binascii.hexlify(encrypted))

    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('Decrypted:', decrypted)
    ```
ex3J1PO2025">"
    Exercice 3 du sujet Polynésie J1 2025

    ```python linenums='1'
    from random import randint

    def gen_mdp(longueur, cont_min, cont_maj, cont_spe):
        # Pour qu'un mot de passe soit non vide, il doit
        # pouvoir contenir des minuscules ou des majuscules
        # ou des caractères spéciaux.
        assert (cont_min or cont_maj or cont_spe)
        minuscules = [chr(i) for i in ...]
        majuscules = [...]
        caracteres_speciaux = ... + ...
        jeu_caracteres = []
        if cont_min:
            ...
        ...
            ...
        ...
            ...
        mot_de_passe = ''
        n = len(jeu_caracteres)
        for i in range(longueur):
            mot_de_passe = ...
        return mot_de_passe
    ```
ex3J2ME2025">"
    Exercice 3 du sujet Métropole J2 2025

    

    
    
    

    ```python
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def indices_vers_lettres(lst):
        s = ''
        for k in lst:
            s += alphabet[k]
        return s

    def chiffrement(msg, cle):
        assert len(cle) >= len(msg), 'impossible'
        indices_msg = lettres_vers_indices(msg)
        indices_cle = lettres_vers_indices(cle)
        n = len(msg)
        indices_msg_chiffre = []
        for k in range(n):
            ind = ...
            if ind >= 26:
                ind = ...
            indices_msg_chiffre.append(ind)
        msg_chiffre = indices_vers_lettres(...)
        return msg_chiffre
    ```

## Rappels reseaux

### Rappels reseaux

Terminale - Spécialité NSI IFS Singapour
Chapitre 14 - Les réseaux (rappels)
Objectifs :
▷ Rappels de la classe de Première sur les réseaux
▷ Rappels de la classe de Première sur fonctionnement du protocole TCP/IP
1 Introduction
Onappelle réseauinformatique ,unensembled'équipementsinformatiquesconnectésentreeuxpardesliaisons
physiques.
Ces machines distantes échangent des informations sous forme de données binaires.
Pourquoi utilise-t-on des réseaux?
▷ pour partager des données et des applications;
▷ pour partager l'utilisation des périphériques;
▷ pour travailler sur une même base de données, un même document ...,etc.
2 Les composants d'un réseau
Les différents ordinateurs et serveurs sont reliés entre eux comme sur le dessin ci-dessous :
Un réseau localpeut être constitué des éléments suivants :
▷ le câble réseau: il peut être en cuivre (appeléRJ45) ou enfibre optique.
▷ lacarte réseau: elle est l'interface entre l'ordinateur et le câble du réseau. Elle prépare, envoie et contrôle
les données sur le réseau. Ces données sont découpées en blocs appelés trames.
▷ le répéteur :c'est un équipement qui sert à régénérer le signal afin d'étendre la distance du réseau.
▷ le concentrateur (ou hub en anglais) : c'est un boîtier constitué de plusieurs ports Ethernet qui permet
la connexion de plusieurs appareils en régénérant le signal, et ne faisant que répercuter les données émises
par l'un vers tous les autres équipements qui lui sont reliés.
T. Rahobisoa 1/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
▷ le commutateur (ou switch en anglais) : c'est un boîtier muni de plusieurs ports Ethernet. Il distribue
les trames directement aux machines destinataires, contrairement auhub.
▷ le routeur : c'est un équipement qui permet de relier plusieurs réseaux. Par exemple, tous les ordinateurs
du réseau de votre domicile connectés par câble (LAN) ou sans-fil sont connectés au réseau Internet par
l'intermédiaire de votre routeur.
▷ l'armoire de brassage: dans laquelle on trouve tous les composants actifs (hub, switch, routeur, etc...)
d'un réseau et toutes les arrivées des câbles d'un secteur.
Figure 1 – Câble réseau
Figure 2 – Carte réseau
Figure 3 – Répéteur
Figure 4 – Hub
Figure 5 – Switch
 Figure 6 – Routeur
Figure 7 – Armoire de
brassage
3 D'autres technologies
3.1 Le Wi-Fi
Apparu à la fin des années 1990, leWi-Fi (Wireless Fidelity) permet un câblage
virtuel entre deux machines en utilisant la modulation des ondes radio.
Les différentes normes 802.11 représentent les variations de débit.
T. Rahobisoa 2/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
3.2 La fibre optique
Elle transporte l'information avec la lumière et non plus des 0 et 1. C'est une
technologie coûteuse mais beaucoup plus efficace.
Elle est utilisée au coeur du réseau.
Record : 8000 km avec une seule fibre.
En pratique, on relie les continents entre eux (comme par exemple l'Europe et le
continent américain) grâce à des câbles sous-marins en fibre optique monomode avec
des répétiteurs tous les 60 km.
Figure 8 – Câblage sous-marin par fibre optique
Figure 9 – Les câbles sous-marins dans le monde
T. Rahobisoa 3/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
4 Caractéristiques d'un réseau
4.1 Taille
On distingue généralement trois catégories de réseaux :
4.1.1 LAN : Local Area Network
C'est un ensemble d'équipements appartenant à une
même société.
Les machines sont situées sur un périmètre géographi-
quement restreint.
4.1.2 MAN : Metropolitan Area Network
Ce type de réseau interconnecte plusieurs LAN.
Dispersion géographique : plusieurs réseaux
LAN géographiquement proches.
4.1.3 WAN : Wide Area Network
Un WAN interconnecte plusieurs LAN ou MAN.
Dispersion géographique : très grandes distances.
Internet est un WAN.
T. Rahobisoa 4/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
4.2 Topologie
A retenir!
La topologie d'un réseau (ou architecture physique) décrit la manière dont sont reliées entre elles les
machines.
On en rencontre souvent deux :
4.2.1 Réseau en étoile
Le routeur ouswitch est au centre.
Exemple : un réseau local (LAN) domestique ou d'entreprise
4.2.2 Réseau maillé
Tous les hôtes sont connectés en pair à pair ( Peer to Peer en anglais) sans
hiérarchie centrale.
Exemple : Internet
5 Les protocoles de communication
5.1 Définition
A retenir!
Un protocole de communication est un ensemble de règles et de procédures à respecter pour émettre et
recevoir des données sur un réseau.
Faisons un parallèle avec l'expédition/la réception de courrier par La
Poste.
Quand vous voulez envoyer une lettre parLa Poste :
— vous placez votre lettre dans une enveloppe
— sur le recto vous inscrivez l'adresse du destinataire
— au dos, vous écrivez l'adresse de l'expéditeur (la votre).
Ce sont des règles utilisées par tout le monde.
C'est ce que l'on appelle unprotocole.
T. Rahobisoa 5/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
5.2 Modèle OSI ou modèle TCP/IP
Ainsi, les règles utilisées afin de faciliter le transfert de données sur Internet font partie d'un ensemble de
protocoles hiérarchisés selon deux modèles :
1. le modèle OSI conçu dans les années 1970 par l'ISO
2. le modèle TCP/IP créé en 1983 par Arpanet
Selon les échanges d'informations à effectuer entre ordinateurs, il existe de nombreux protocoles de communi-
cation ou d'encodage. Par exemple, avec le modèle OSI en 7 couches, on a :
— HTTP
— FTP
— VoIP
— ASCII
— Ethernet, Wifi,..., etc.
Et les correspondances avec le modèle TCP/IP :
Nous n'étudierons ici que le modèleTCP/IP (Transmission Control Protocol/Internet Protocol).
C'est un protocole, c'est-à-dire unensemble de règles de communicationqui réunit :
— TCP : Transmission Control Protocol
— IP : Internet Protocol
Ils interviennent à des niveaux différents que l'on appellecouches afin de réaliser :
▷ le fractionnement des messages en paquets;
▷ l'utilisation d'un système d'adresses;
▷ l'acheminement des données sur le réseau (routage);
▷ le contrôle des erreurs de transmission de données.
T. Rahobisoa 6/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
6 Le protocole TCP/IP
6.1 Le protocole IP
Pour pouvoir transmettre un message il faut connaître l'émetteur et le récepteur du message. Faisons un parallèle
avec une lettre envoyée par la poste :
— On met la lettre dans une enveloppe,
— On inscrit l'adresse du destinataire,
— On inscrit l'adresse de l'expéditeur.
Sur Internet, c'est à peu près la même chose. Chaque
message (chaque petit paquet de données) est enveloppé
parleprotocoleIPquiyajoutedifférentesinformations:
— l'adresse IP de l'expéditeur,
— l'adresse IP du destinataire,
— des données supplémentaires (qui permettent de
bien contrôler l'acheminement du message).
6.2 Le routage IP
Pour envoyer votre lettre, vous la postez dans la boîte aux lettres la plus proche. Ce courrier est relevé, envoyé
au centre de tri de votre ville, puis transmis à d'autres centres de tri jusqu'à atteindre le destinataire.
C'est la même chose sur Internet.
Vous déposez le paquet IP sur l'ordinateur le plus proche (celui de votre fournisseur d'accès en général). Le
paquet IP va transiter d'ordinateur en ordinateur jusqu'à atteindre le destinataire.
T. Rahobisoa 7/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
6.3 Le protocole UDP
IP nous permet d'envoyer et de recevoir des paquets de données d'un ordinateur à un autre.
Mais si nous avons plusieurs applications qui fonctionnent sur l'ordinateur (un navigateur, un logiciel d'e-mail,
un logiciel de visioconférence, ...,etc.), comment faire pour savoir à quel logiciel délivrer les paquets?
On attribue alors un numéro unique à chaque logiciel dans l'ordinateur (comme pour les portes d'un immeuble).
C'est ce qu'on appelle lesports. Ces ports sont des informations présentes dans les datagrammes duprotoco-
cole UDP(ports).
6.4 Le protocole TCP
On peut envoyer des paquets de données d'un ordinateur à un autre (protocole IP) et s'adresser au bon logiciel
(protocole UDP), cependant il y a encore des problèmes :
— Des paquets peuvent se perdre.
— Rien ne permet de savoir s'ils sont bien arrivés.
— La taille des paquets est limitée (1500 octets environ). Et si je veux envoyer une photo de 100 000 octets?
C'est le rôle deu protocoleTCP (Transmission Control Protocol) de régler tous ces éventuels problèmes.
TCP sait faire :
▷ Tout ce que UDP sait faire (ports).
▷ Vérifier que le destinataire est prêt à recevoir les données.
▷ Découper les gros paquets en paquets plus petits.
▷ Numéroter les segments, vérifier qu'ils arrivent à destination (les redemander sinon), les réordonner.
▷ Émettre des accusés de réception.
Par exemple, pour envoyer le message"Salut, comment ça va ?" , voilà ce que fait TCP (chaque flèche repré-
sente un paquet IP) :
T. Rahobisoa 8/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
À l'arrivée, sur l'ordinateur204.66.224.82, la couche TCP reconstitue le message"Salut, comment ça va
?" à partir des trois paquets IP reçus et le donne au logiciel qui est sur le port 80.
6.5 Perte de paquets
Il se peut, et cela est courant que des paquets se perdent...
Les causes possibles sont nombreuses :
— Engorgement d'un serveur
— Délai d'attente trop long
Le protocole TCP contrôle l'envoi et la bonne réception des paquets avec des accusés de réception.
(ACK : acknowledgement ou acquittement en français ).
Ce processus d'acquittement permet de détecter les pertes de paquets.
6.6 En résumé
A retenir!
▷ Afin de faciliter la communication et d'éviter les erreurs pendant la transmission, les informations
sont divisées enpaquets (ou trames)au lieu d'être envoyées en un seul bloc.
▷ Chaque paquet transmis via le protocole IP contient dans son en-tête l'adresse IPde l'émetteur
ainsi que l'adresse IP du destinataire.
▷ Cela permet aux machines du réseau de router les paquets jusqu'à destination grâce à l'adresse IP.
▷ Le destinataire saura ainsi à qui renvoyer les données grâce à l'adresse IP de l'émetteur contenu
dans les en-têtes des paquets envoyés.
T. Rahobisoa 9/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
7 Adresse IP et adresse MAC
7.1 Adresse MAC
A retenir!
En réseau informatique uneadresse MAC(Media Access Control address) est un identifiant physique
stocké dans une carte réseau ou une interface réseau similaire et utilisé pour attribuermondialement
une adresse unique.
Elle est appelée égalementadresse physique.
Une adresse MAC est constituée de6 octetset est généralement représentée sous la formehexadécimale, en
séparant les octets par undouble point ou un tiret.
Exemple : 00:0C:6E:A2:AF:15
L'adresse est divisée en deux parties égales : (soit 2× 3 octets) :
▷ les 3 premiers octets désignent leconstructeur
▷ les 3 derniers octets désignent lenuméro d'identifiant de la carte(unique)
7.2 Adresse IP
TCP/IP se base sur la notion d'adressage IP. Ainsi, chaque machine connectée au réseau reçoit une adresse IP
dans le but d'acheminer des paquets de données.
A retenir!
Une adresse IPest une suite de chiffres qui joue une rôle d'identification et qui permet l'acheminement
(ou routage) des paquets de données d'un ordinateur connecté à un réseau local ou à Internet.
Les adresses IP permettent d'identifier les cartes réseau ou tout matériel se connectant à un réseau (modem,
routeur, switch, imprimante réseau...)
Actuellement la norme utilisée est l'IP version 4 :IPv4.
Ainsi, une adresse IP est codée sur 32 bits soit4 octets.
Elle est composée de 4 nombres entiers (en base 10) compris entre 0 et 255séparés par un point.
Exemple : 192.168.0.1 est certainement l'adresse IP privée du routeur de votre domicile.
T. Rahobisoa 10/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
8 Encapsulation des données
A chaque fois qu'un protocole reçoit une donnée d'une couche supérieure, celui-ci ajoute des informations
qu'il place au début de la donnée (ou entête), créant ainsi une nouvelle donnée. C'est ce que l'on appelle
l'encapsulation.
La nouvelle donnée créée est envoyée à la couche directement inférieure (si elle existe) selon le schéma suivant :
Inversement, à chaque fois qu'un protocole reçoit une donnée d'une couche inférieure, il enlève les données
d'entête correspondant à son protocole (on appelle cette opération ladécapsulation) puis envoie la donnée
décapsulée à la couche directement supérieure (si elle existe).
9 Quelques commandes à connaître
Avec un système d'exploitationWindows, après avoir lancé un terminal sousWindows (Command Prompt), il
est possible d'exécuter quelques commandes réseau basiques telle ques :
9.1 ipconfig
A retenir!
ipconfig est une commande qui permet d'afficher la configuration réseau d'un PC.
Avec un système d'exploitation de typeLinux ou MacOs, la commande similaire se nommeifconfig.
T. Rahobisoa 11/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
9.2 tracert
A retenir!
tracert est une commande qui permet de suivre les chemins qu'un paquet de données va prendre pour
aller de la machine locale à une autre machine connectée au réseau IP.
Avec un système d'exploitation de typeLinux ou MacOs, la commande similaire se nommetraceroute.
9.3 ping
A retenir!
ping est une commande permettant de tester l'accessibilité d'une autre machine à travers un réseau IP.
La commande mesure également le temps mis pour recevoir une réponse, appeléround-trip time.
T. Rahobisoa 12/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
10 Exercices
Exercice 1 : Classes d'adresses
Rappel : Une adresse IP est composée d'une partie d'adresse du réseauet une deuxième partie qui corres-
pondant à l'adresse de la machineou adresse hôte.
On dénombre 3 classes d'adresses IP :
1. Trouver les adresses IP minimales et maximales des classes A, B et C.
2. Combien de machines peut-on connecter dans un réseau de classe A, B et C?
3. Quels sont les masques de sous-réseau dans un réseau de classe A, B et C?
Exercice 2 : Notation IP/n
On peut voir dans la classe A que l'on peut avoir beaucoup d'adresse machines (224) mais seulement 255 réseaux.
A la différence de la classe C, on peut avoir beaucoup de réseaux (224) mais peu de machines dans le réseau
(255).
Attention, on ajoute souvent à l'adresse IP un "/" suivi d'un nombre qui correspond au nombre de bits de
l'adresse réseau. Si ce nombre est 8 (exemple :192.168.2.1/8), le premier octet est consacré à l'adresse réseau,
le reste est consacré à la partie machine de l'adresse IP. On aura donc une adresse réseau de la forme192.0.0.0
Déterminer les adresses réseaux à partir des adresses IP suivantes :
— 147.12.1.24/16
— 192.168.2.45/24
— 50.230.65.87/10
T. Rahobisoa 13/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
Exercice 3 :Soient 2 machines A et B connectées à un switch, déterminer l'adresse de réseau de chaque
machine et vérifier qu'elles peuvent communiquer ensemble, justifier :
1. adresse IP de A :172.23.4.7/16; adresse IP de B :172.23.5.8/16
2. adresse IP de A :24.2.8.127/11; adresse IP de B :24.23.5.52/11
3. adresse IP de A :193.28.7.2/22; adresse IP de B :193.28.8.3/22
Exercice 4 : Adresses réservées
Il est à noter que certaines adresses IP ne sont pas disponibles :
▷ une adresse réseau ne peut pas être attribuée à une machine, par exemple aucune machine ne pourra avoir
l'adresse IP 192.168.1.0/24 ou encore l'adresse IP255.0.0.0/8
▷ les adresses IP qui ont tous les octets de la partie "machines" de l'adresse IP à 255 ne sont pas utilisables
(ce sont des adresses debroadcast qui permettent d'envoyer des données vers toutes les machines d'un
réseau).
Exemples : 192.167.24.255/24, 172.28.255.255/16 ou encore 4.255.255.255/8 sont des adresses de
broadcast.
Combien de machines peut-on trouver au maximum :
1. dans un réseau d'adresse réseau192.168.2.0/24?
2. dans un réseau d'adresse réseau176.24.0.0/16?
3. dans un réseau d'adresse réseau50.192.0.0/10?
Exercice 5 : IPv4 ou IPv6
1. Combien y a-t-il d'adresses IP disponibles avec le protocoleIPv4 ?
2. Combien y a-t-il de personnes connectées à Internet en 2024?
3. Comment est codé une adresse IP selon le nouveau protocoleIPv6 ?
4. Combien y a-t-il d'adresses IP disponibles avec le protocoleIPv6 ?
5. Depuis quand fonctionne le protocoleIPv6 ?
Exercice 6 : Adresse MAC
1. Ouvrir un terminal (Tapercmd ou powershell dans la barre de rechercheWindows).
2. Trouver l'adresse MAC de votre carte réseau (avec la commandeipconfig /all ).
3. A l'aide de la commandeping suivie de l'adresse Internet du site, trouver l'adresse IP des siteswww.x.com
et www.google.fr. Y a-t-il une différence?
4. A l'aide de la commandetracert , suivie de l'adresse IP du site, trouver les routeurs rencontrés pour
accéder au sitewww.nba.com.
Exercice 7 : Masque de sous-réseau
Le masque est un séparateur entre la partie réseau et la partie machine d'une adresse IP. Le masque est une
suite de 4 octets, comme l'adresse IP.
Pour définir le masque, il nous suffit de dire que les bits à 1 représenteront la partie réseau (Net-ID) de l'adresse,
et les bits à 0 la partie machine (Host-ID).
Ainsi, on fera une association entre une adresse IP et un masque pour savoir dans cette adresse IP quelle est la
partie réseau et quelle est la partie machine de l'adresse.
Ainsi, dans l'exemple ci-dessus, il nous reste 8 bits à 0, on aura donc la possibilité d'avoir28 machines disponibles
dans ce sous-réseau qui pourront dialoguer entre-elles.
L'adresse réseau permet de savoir si 2 machines peuvent communiquer entre elle. Si ces 2 machines ont une
adresse réseau identique, alors, elles appartiennent au même réseau et elles peuvent communiquer.
T. Rahobisoa 14/15 AMSER01 - Réseau (rappels)
Terminale - Spécialité NSI IFS Singapour
Calculer l'adresse réseau de la machine suivante :
— Adresse IP :24.2.179.127
— Masque : 255.255.224.0
Exercice 8 : Réseau d'une petite entreprise
Vous travaillez dans le cabinet comptableS.A Compta . Tous les ordinateurs du cabinet sont en réseau comme
sur le schéma. Nous sommes en présence d'un réseau utilisant le protocole TCP/IP.
Les adresses IP de chaque nœud du réseau sont listées dans le tableau suivant :
1. Quel est le masque de sous-réseau utilisé?
2. Indiquer quelle est l'adresse IP du réseau?
3. Déterminer le nombre de machines que l'on peut brancher dans ce réseau.
4. Quels sont les différents sous-réseaux obtenus si le 4ème octet du nouveau masque est :11000000. Dans
ce cas les machines pourront-elles encore communiquer? Expliquer. Comment peut-on y remédier?
Exercice 9 : TP Filius
Suivre les instructions du document suivant pour simuler plusieurs réseaux avec le logicielFilius.
Exercice 10 : QCM de révision
Répondre aux questions du QCM sur le site suivant.
Exercice 11 : Exercices d'entraînement
Faire les exercices en ligne suivants.
T. Rahobisoa 15/15 AMSER01 - Réseau (rappels)

## Routage

### Routage

Terminale - Spécialité NSI IFS Singapour
Chapitre 15 - Le routage
Objectifs :
▷ Connaître les principaux protocoles de routage
▷ Identifier, suivant le protocole de routage utilisé (RIP ou OSPF), la route empruntée par un paquet.
1 Introduction
Exemple
Thomas veut envoyer une lettre de remerciement à son amiPacôme Toullemonde, habitant à Toulouse
(en France), qui lui a prété un manuel de NSI.
1. Il rédige donc un courrier, le place dans une enveloppe sur laquelle il inscrit le nom, le prénom, le
numéro, la rue, le code postal, la ville et enfin le pays.
2. Puis il dépose le tout à la poste deSerangoon à Singapour.
3. L'agent de la poste ne connaît pasPacôme, mais il sait que la lettre doit aller en France.
4. Une fois arrivée en France, l'agent de poste Français ne connaît toujours pasPacôme, mais il sait
qu'il doit envoyer la lettre vers un nouveau centre de tri, celui de Toulouse.
5. Arrivée au centre de Toulouse, la lettre va au bureau de poste correspondant au quartier dePacôme.
Et enfin elle sera remise au facteur qui distribue le courrier dans la rue de Pacôme, afin qu'il la
dépose dans sa boite aux lettres.
Nous pouvons ici faire une analogie entre lesréseaux postauxet lesréseaux informatiques:
— Thomas et son ami sont desmachines.
— Les centres de tris par desrouteurs.
— Le facteur est unswitch.
2 Le principe
De la même façon, le rôle d'un réseau informatique consiste essentiellement à trouver les bons chemins pour
amener chaque paquet à sa destination. Un paquet de données qui doit traverser un réseau n'aa prioriaucune
idée du chemin qu'il va devoir suivre. Il fait entièrement confiance aux indications fournies par les routeurs.
Chaque routeur va donc devoir orienter le paquet sur la base d'une et une seule information :
l'adresse de la destination du paquet. On parle ici de relayage.
Au sein d'un réseau, le relayage consiste essentiellement à trouver la bonne sortie, celle qui mènera un paquet
au plus proche possible de sa destination, et à trouver au sein du réseau le chemin qui mènera le paquet à cette
sortie.
T. Rahobisoa 1/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
3 Définition
A retenir!
Le routage est le processus qui permet de sélectionner un chemin dans un ou plusieurs réseaux pour
transmettre des données depuis un expéditeur jusqu'à un ou plusieurs destinataires.
Le routage n'est pas exclusivement destiné aux réseaux informatiques tel qu'Internet, il existe aussi dans d'autres
domaines comme les réseaux de transports, les réseaux téléphoniques, ...,etc.
Par la suite nous nous intéresserons uniquement au routage au sein des réseaux informatiques.
4 Le routeur
La box que vous avez chez vous est également un routeur qui possède plusieurs interfaces réseau :
▷ une interface connectée au réseau de votre fournisseur d'accès à Internet, par exemple via la fibre.
▷ une interface filaire (Ethernet) connectée à votre réseau local
▷ une interface Wifi
Un routeur sur Internet possède souvent plus de ports et ressemble d'extérieur à un switch. Il dispose d'un
logiciel interne lui permettant de communiquer avec ses routeurs voisins pour l'aider à déterminer les meilleures
routes à emprunter pour acheminer ses paquets.
Le routeur reçoit un paquet sur l'un de ses ports et sa mission consiste essentiellement à déterminer sur lequel
de ses autres ports il doit ré-acheminer le paquet. Il doit le faire très vite et s'adapter à un environnement qui
change (routes qui apparaissent et disparaissent).
5 La table de routage
Pour choisir le bon chemin, le routeur s'appuie sur unetable de routage: c'est une table donnant pour chaque
destination connue par le routeur la porte de sortie à emprunter ainsi que l'efficacité de cette route.
Cette efficacité sera exploitée dans les protocoles que nous détaillerons par la suite.
Voici un exemple :
Ici, on voit que pour joindre le réseau137.194.2.0, il faut passer par le portv10, c'est-à-dire sur le lien de
communication qui le relie au routeur dont l'adresse IP est137.194.4.254.
T. Rahobisoa 2/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
Pour éviter que la table ne grossisse trop, on ne stocke pas l'adresse de chaque machine, mais des adresses de
réseaux. Ici la dernière ligne de la table est valable pour toutes les machines dont les 24 premiers bits forment
le préfixe 137.194.17.XXX, car le masque de sous-réseau est :255.255.255.0.
A retenir!
Lorsqu'un routeur reçoit un paquet celui-ci comporte une adresse IP de destination. Pour savoir dans
quelle direction envoyer le paquet, chaque routeur possède une table de routage.
Une table de routage est un tableau indiquant pour chaque réseau de destination (connu à partir de
l'IP de la destination), quelle interface réseau on peut utiliser en lui associant également une métrique
qui mesure la «distance» séparant le routeur du réseau de destination.
Pour afficher une table de routage :
— Sous Windows : route print ou netsh int ipv4/ipv6 sh route
— Sous Unix/Mac Os: netstat -rn
— Sous Linux : ip -4/-6 route
6 Types de routage
Il existe deux types de routage :
▷ Le routage statique qui consiste à indiquer l'adresse IP des réseaux que l'on cherche à atteindre. Les
administrateurs vont configurer les routeurs un à un au sein du réseau afin d'y saisir les routes à emprunter
pour aller sur tel ou tel réseau.
Les administrateurs vont renseignermanuellementpour chaque adresse le nom de l'interface du routeur
ou l'adresse IP du routeur voisin.
Chaque routeur ainsi paramétré permettra de faire le lien entre deux réseaux.
Si le réseau global est complexe, la configuration peut être fastidieuse et source d'erreurs.
Deplussilereseauévolue,ilfaudralemettreàjourmanuellement.Cetypederoutagepeut-êtreintéressant
pour des raisons de sécurité si on veut maîtriser la route des paquets.
Ce type de routage reste très localisé.
▷ Le routage dynamiquepermet quant à lui de se mettre à jour de façon automatique.
Un protocole de routage va permettre aux différents routeurs de se comprendre et d'échanger des infor-
mations de façonpériodique ou événementielleafin que chaque routeur soit au courant des évolutions
du réseau sans aucune intervention de l'administrateur du réseau.
T. Rahobisoa 3/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
7 Cas concret
Nous avons sur le schéma ci-dessous les éléments suivants :
— 15 ordinateurs :M1 à M15
— 6 switchs :R1 à R6
— 8 routeurs :A, B, C, D, E, F, G et H.
Nous avons 6 réseaux locaux, chaque réseau local possède son propre switch.
Les ordinateurs M1, M2 et M3 appartiennent au réseau local 1.
Les ordinateurs M4, M5 et M6 appartiennent au réseau local 2.
Nous pouvons synthétiser tout cela comme suit :
Réseau local 1 :M1, M2 et M3 Réseau local 4 :M9 et M10
Réseau local 2 : Réseau local 5 :
Réseau local 3 : Réseau local 6 :
1. Compléter le tableau ci-dessus avec les réseaux locaux 2, 3, 5 et 6.
2. Observer les exemples de communications suivants :
— M1 veut communiquer avecM3
— M1 veut communiquer avecM6
— M1 veut communiquer avecM9
— M13 veut communiquer avecM9
3. Déterminer deux chemins possibles reliantM4 et M14.
T. Rahobisoa 4/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
7.1 Comment les routeurs procèdent-ils pour amener les paquets à bon port?
Soit le schéma suivant :
Dans le schéma ci-dessusM1 et M4 n'ont pas la même adresse réseau (car elles n'appartiennent pas au même
réseau local).
Si M1 cherche à entrer en communication avecM4, le switchR1 va constater queM4 n'appartient pas au réseau
local (grâce à son adresse IP),R1 va donc envoyer le paquet de données vers le routeurA.
Cela sera donc au routeurA de gérer le "problème".
Comment atteindre M4?
Chaque routeur possède unetable de routage.
7.2 Comment fonctionne une table de routage?
Étudiez attentivement le schéma ci-dessus. Le choix des adresses IP des machines a été fait au hasard. En
revanche,vérifiezquetoutestcohérent:adressesmachinesavecadressesréseaux(lesadressesréseauxsontnotées
à côté des différents switchs, par exemple le switchR1 est utilisé dans le réseau d'adresse172.168.0.0/16).
Voici les informations présentes dans la table de routage du routeurA :
— le routeur A est directement relié au réseau172.168.0.0/16 par l'intermédiaire de son interfaceeth0
— le routeur A est directement relié au réseau172.169.0.0/16 par l'intermédiaire de son interfaceeth2
— le routeur A est directement relié au réseau192.168.7.0/24 par l'intermédiaire de son interfaceeth1 (le
réseau 192.168.7.0/24 est un peu particulier car il est uniquement composé desrouteurs A et G)
— le routeur A n'est pas directement relié au réseau10.0.0.0/8 mais par contre il "sait" que les paquets à
destination de ce réseau doivent être envoyés à la machine d'adresse IP192.168.7.2/24 (c'est-à-dire le
routeur G qui lui est directement relié au réseau10.0.0.0/8)
On peut résumer tout cela avec le tableau suivant (table de routage simplifiée de A)
Réseau Passerelle Interface Nombre de sauts *
172.168.0.0/16 eth0 0
192.168.7.0/24 eth1 0
172.169.0.0/16 eth2 0
10.0.0.0/8 192.168.7.2/24 eth1 1
* nombre de sauts permet de trouver le chemin le plus court : plus la valeur est petite, plus le chemin est
court. Un réseau directement lié à un routeur aura un nombre de saut de0.
T. Rahobisoa 5/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
7.3 Exercice d'application
Déterminer la table de routage de G.
Réseau Passerelle Interface Nombre de sauts
7.4 En résumé
Plusieurs algorithmes sont possibles pour compléter les tables de routage.
Pour le routage réseau, des contraintes particulières liées au fonctionnement des réseaux sont à prendre en
compte :
▷ Les routeurs n'ont pas connaissance de la topologie globale du réseau,ils ne communiquent qu'avec
leurs voisins immédiats.
▷ L'algorithme est distribué : il n'y a pas de centre de gestion central. Chaque routeur se constitue sa
propre table à partir des informations communiquées par ses voisins, puis il transmet à ses voisins les
informations en sa possession.
▷ L'algorithme estitératif : il est exécuté en permanence et ne s'arrête jamais.
Lorsqu'une modification est faite sur le réseau, celle-ci se propage de proche en proche à chaque routeur qui
adapte alors sa table de routage.
A retenir!
A partir de là, deux grandes familles de protocole de routage se dégagent :
▷ le routageà vecteur de distance: il consiste à compter lenombre d'étapes nécessairespour
atteindre l'objectif.
▷ le routageà état de lien: il consiste à prendre en comptela qualité des liaisonspour optimiser
le débit ou la latence de la liaison.
8 Le protocole RIP
8.1 Principe général de l'algorithme
A retenir!
Le protocole RIP (Routing Information Protocol) rentre dans la catégorie des protocoles à vecteur de
distance. Un vecteur de distance est un couple (adresse, distance).
Le principe simplifié de ce protocole est de chercher à minimiser le nombre de routeurs à
traverser pour atteindre la destination(on minimise le nombre de sauts).
Il est utilisé pour des réseaux de petite taille (jusqu'à 15 machines au maximum).
Chaque routeur reçoit en permanence de ses voisins les informations de routage qu'ils possèdent. Il va alors
exploiter ces informations pour se construire lui-même sa table de routage en ne retenant que les informations les
plus pertinentes : une simple comparaison permet de ne garder que le chemin le plus avantageux. Il transmettra
à son tour ces informations à ses voisins et ainsi de suite.
L'algorithme deBellman-Ford est un algorithme de recherche de plus court chemin dans un graphe.
Al'issuedequelquesétapes,lestablessestabilisentetleroutageestpleinementopérationnel.Letempsnécessaire
à la stabilisation des tables est proportionnel au diamètre du graphe modélisant le réseau (c'est-à-dire au nombre
maximal d'étapes nécessaires pour relier deux points quelconques du réseau).
T. Rahobisoa 6/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
8.2 Exemple
Considérons le réseau suivant qui relie deux réseaux d'une entreprise :
Le “réseau local 1” contient des postes de travail
dans un bureau.
Le “serveur réseau 2” contient un serveur dans un
centre de données.
Les routeurs R1 et R6 permettent d'accéder au ré-
seau de l'entreprise.
R2, R3, R4 et R5 sont des routeurs internes au ré-
seau.
Nous allons nous intéresser à l'évolution des tables
de routage des routeursR1 et R3 sur lesquelles on
a activé le protocole RIP.
8.2.1 Etape 0
— Au démarrage, les routeursR1 et R3 ne connaissent que leurs voisins proches.
— Au départ, R1 ne peut atteindre que ses voisins immédiats (nb sauts vaut 1).
— Aucune passerelle n'est nécessaire puisque la communication est directe.
— Chaque sous-réseau utilise une interface spécifique. Leréseau local 1contenant les postes de travail est
accessible en wifi.
Voici à quoi peut ressembler la table de routage deR1 au démarrage :
Destination Passerelle Interface Nb sauts Remarques
192.168.1.0 wifi 1 ⇒ vers les postes de travail
172.16.0.0 eth0-1 1 ⇒ vers R3
Pour ce qui concerneR3, celui-ci possède 4 interfaces réseau filaires, que nous nommeronseth0-3 qui permettent
d'atteindre les routeurs immédiats (R1, R2, R4 et R5).
Voici à quoi peut ressembler la table de routage deR3 au démarrage :
Destination Passerelle Interface Nb sauts Remarques
172.16.0.0 eth0-3 1
172.16.1.0 eth1-3 1
172.16.6.0 eth2-3 1
172.16.3.0 eth3-3 1
T. Rahobisoa 7/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
8.2.2 Etape 1
Au bout de 30 secondes, un premier échange intervient avec les voisins immédiats des routeurs.
Le principe de l'algorithme
Lorsqu'un routeur reçoit une nouvelle route de la part d'un voisin, 4 cas sont envisageables :
1. Il découvre une route vers un nouveau réseau inconnu.
⇒ Il l'ajoute à sa table.
2. Il découvre une route vers un réseau connu, plus courte que celle qu'il possède dans sa table.
⇒ Il actualise sa table.
3. Il découvre une route vers un réseau connu, plus longue que celle qu'il possède dans sa table.
⇒ Il ignore cette route.
4. Il reçoit une route vers un réseau connu en provenance d'un routeur déjà existant dans sa table.
⇒ Il met à jour sa table car la topologie du réseau a été modifiée.
En appliquant ces règles, voici la table de routage deR1 après une étape :
Destination Passerelle Interface Nb sauts Remarques
192.168.1.0 wifi0 1 ⇒ vers les postes de travail
172.16.0.0 eth0-1 1 ⇒ vers R3
172.16.1.0 172.16.0.3 eth0-1 2 Ces 3 routes proviennent deR3
172.16.6.0 172.16.0.3 eth0-1 2 Ces 3 routes proviennent deR3
172.16.3.0 172.16.0.3 eth0-1 2 Ces 3 routes proviennent deR3
172.16.0.3 est l'adresse IP du routeurR3.
— On ajoute à la table précédente les réseaux atteignables parR3.
— On pense cependant à ajouter1 au nombre de sauts!
— Si R1 veut atteindre le réseau172.16.3.0, il s'adressera àR3 et atteindra le réseau cible en 2 sauts.
Voici la table deR3 qui s'enrichit des informations envoyées parR1 afin d'atteindre le réseau local, mais aussi
des informations en provenance deR2, R4 et R5.
Il découvre ainsi 4 nouveaux réseaux.
Destination Passerelle Interface Nb sauts Remarques
172.16.0.0 eth0-3 1
172.16.1.0 eth1-3 1
172.16.6.0 eth2-3 1
172.16.3.0 eth3-3 1
192.168.1.0 172.16.0.1 eth0-3 2 Reçu de R1
172.16.2.0 172.16.1.2 eth1-3 2 Reçu de R2
172.16.5.0 172.16.6.5 eth2-3 2 Reçu de R5
172.16.4.0 172.16.3.4 eth3-3 2 Reçu de R4
8.2.3 Etape 3
Comme vous le voyez, les tables deviennent vite longues et énumérer dans le détail chacune d'elle est trop long.
On va donc passer directement à l'étape finale : l'étape 3.
Voici ce que contient la table de routage deR1 :
Destination Passerelle Interface Nb sauts Remarques
192.168.1.0 wifi0 1 ⇒ vers les postes de travail
172.16.0.0 eth0-1 1 ⇒ vers R3
172.16.1.0 172.16.0.3 eth0-1 2
172.16.6.0 172.16.0.3 eth0-1 2
172.16.3.0 172.16.0.3 eth0-1 2
172.16.5.0 172.16.0.3 eth0-1 3 Obtenu à l'étape 2
192.168.2.0 172.16.0.3 eth0-1 4 Obtenu à l'étape 3
Comme vous le voyez, le routeurR1 est à présent en capacité d'acheminer un paquet du poste de travail du
réseau 1 vers le serveur se trouvant dans le réseau 2.
T. Rahobisoa 8/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
8.3 Détection des pannes
Le protocole RIP est en mesure de détecter des pannes :
Si un routeur ne reçoit pas d'information de la part d'un de ses voisins au bout d'un temps de l'ordre de 3
minutes (configurable), il va considérer que ce lien est mort et en informer ses voisins en indiquant un nombre
de sauts égal à 16.
Puisque RIP ne gère que 15 sauts au maximum, 16 peut être considéré comme une distance infinie. De cette
manière, les voisins vont pouvoir recalculer leurs routes en conséquence en évitant le lien qui est tombé.
8.4 Détection des boucles
RIP implémente d'autres mécanismes pour empêcher que se forment des boucles de routage.
Une boucle est par exemple une route du typeR2⇒ R3⇒ R5⇒ R2.
Des exemples de tels mécanismes sont :
▷ une durée de vie limitée sur les paquets (TTL) afin qu'un paquet qui tourne en rond soit détruit
▷ ne pas renvoyer une information vers un routeur si celle-ci est déjà passée par ce routeur
Exercice 1 :A vous de jouer!
Élaborer au fil du temps la table de routage du routeurR4 de manière similaire à ce que l'on vient de faire.
Destination Passerelle Interface Nb sauts Remarques
8.5 Conclusion
Le protocole RIP est en général utilisé sur depetits réseaux: il est en effet limité à15 sautset de plus, il
génère un trafic important.
Pour des structures plus importantes, on va lui préférer leprotocole OSPF.
En conclusion, regarder la vidéo suivante sur le principe du routage à vecteur de distance.
T. Rahobisoa 9/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
9 Le protocole OSPF
Le protocole OSPF(Open Shortest Path First) est dans la catégorie des protocolesà état de lien.
Dans le protocole à vecteur de distance que nous venons de voir, on cherche à minimiser le nombre de sauts,
mais sans aucune garantie que le chemin emprunté soit en réalité le plus performant (en termes de débit par
exemple).
9.1 Principe général de l'algorithme
A retenir!
Le protocole OSPF propose une approche tout à fait différente : au lieu de s'intéresser au nombre de
sauts, on va chercher àoptimiser le débit des liaisons empruntées.
Pour cela, chaque routeur va devoirconnaître l'intégralité du réseau avec le débit associé à
chaque lienafin d'appliquer un algorithme de recherche de chemin optimal.
On peut faire un parallèle entre le fonctionnement d'OSPF et celui de nos logiciels de guidage par GPS.
En effet, dans ce type de logiciels :
▷ l'ensemble de la carte de France et de ses routes est connue du logiciel
▷ le type de chaque route est renseigné ainsi que la vitesse autorisée sur la route
▷ le calcul d'itinéraire va permettre le calcul d'un chemin permettant par exemple d'emprunter les routes
sur lesquelles la vitesse est la plus importante (temps le plus court).
9.2 Découverte de la topologie du réseau
Le protocole OSPF a besoin de connaître la topologie du réseau ainsi que la qualité de chaque lien en terme de
bande passante.
Pour cela, chaque routeur va fabriquer unetable de voisinage: il s'agit d'un tableau permettant d'identifier
tous les routeurs qui lui sont connectés ainsi que le débit associé à chaque lien.
Pour obtenir ces informations, le routeur échange périodiquement des messages (appelés messagesHello) avec
ses voisins.
Voisin Qualité du lien
B 1 Gb/s
C 10 Gb/s
T. Rahobisoa 10/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
Une fois tous ses voisins directs identifiés, le routeur va envoyer sa table de voisinage à tous les autres routeurs du
réseau. Il va recevoir des autres routeurs leurs tables de voisinages et ainsi pouvoir constituer une cartographie
complète du réseau.
Nous allons utiliser l'algorithme de Djikstradatant de 1959 qui permet de trouverle chemin le plus court
sur un graphe.
Visionner cette vidéo pour comprendre le fonctionnement de l'algorithme de Dijkstra.
9.3 Exemple d'application
Considérons le réseau suivant. Après échanges de messagesHello, la cartographie suivante du réseau a été
constituée :
Nous cherchons à déterminer le chemin le plus rapide entreR1 et R7.
L'outil Graph Online vous permet de le faire visuellement via le menuAlgorithmes / plus court chemin avec
l'algorithme de Djisktra.
Contrairement à RIP, le chemin qu'OSPF nous indiquera seraR1⇒ R2⇒ R3⇒ R5⇒ R4⇒ R6⇒ R7.
Ce chemin n'est clairement pas le plus efficace en termes de sauts mais c'est le plus rapide en terme de débit
car il n'exploite pratiquement que des liaisons à 10 Gb/s.
9.4 Notion de coût
L'algorithme de Dijkstra permet de minimiser la longueur d'un chemin, or nous souhaitons maximiser le débit
sur nos liaisons. Nous allons donc considérer l'inverse de la bande passante de nos liens pour appliquer Dijkstra :
maximiser les débit revient à minimiser l'inverse des débits.
La métrique utilisée n'est donc plus le nombre de sauts, mais lecoût de la liaison.
Celui-ci tient compte dudébit binaire de chaque liaison en bits par seconde.
On définit le coût par l'expression suivante :
coût = 108
débit
où le débit est exprimé en bit/s.
▷ 10 Gb/s sera affecté au poids 0.01
▷ 1 Gb/s au poids 0.1
▷ 100 Mb/s = 0,1 Gb/s au poids 1
T. Rahobisoa 11/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
9.5 Application de l'algorithme
Nous allons ensuite constituer notre tableau. A chaque nouvelle ligne :
▷ on calcule les distances totales vers les destinations possibles
▷ on ne retient que la plus petite (en gras) que l'on marque sur une nouvelle ligne
▷ pour empêcher les retours, une fois une destination choisie (en gras), on désactive tout le reste de la
colonne (avec des×).
Tableau pour la liaison deR1 à R7 :
R1 R2 R3 R4 R5 R6 R7
Dans le tableau, on indique descouples distance - origine:
Ainsi 0.05 - R4 dans la colonneR6 signifie queR6 est à une distance minimum de0.05 du départ en provenance
de R4.
On peut ainsi reconstituer l'itinéraire optimal en partant deR7 et en remontant à l'envers en utilisant le champ
origine :
R1⇒ R2⇒ R3⇒ R5⇒ R4⇒ R6⇒ R7 avec un poids total minimum de0.15.
Exercice 2 :A vous de jouer!
On supprime la liaisonR4-R5.
Appliquer l'algorithme de Dijkstra pour déterminer un chemin optimal entreR1 et R7.
R1 R2 R3 R4 R5 R6 R7
9.6 Conclusion
OSPF peut s'adapter à la qualité des liens mais dans une certaine mesure uniquement : si un lien à 10Gb/s est
saturé, il vaut mieux emprunter un lien à 1Gb/s sous utilisé, mais OSPF n'en a pas connaissance.
Il n'y a pas dans l'absolu de meilleur algorithme de routage, tout dépend du réseau auquel on a affaire. Un
protocole sera plus réactif face aux changements de topologie mais au prix d'un plus gros volume échangé. Un
autre sera plus efficace si les liaisons au sein du réseau sont très hétérogènes.
Pour conclure, visionner la vidéo suivante sur le principe du routage à état de lien.
T. Rahobisoa 12/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
10 Exercices
Exercice 3 :Comparatif
1. Pour récapituler ce qui a été vu en cours, regarder la vidéo bilan suivante sur les protocoles RIP et OSPF.
2. Faire les recherches nécessaires pour établir un tableau comparatif entre les protocoles RIP et OSPF.
RIP OSPF
Fonctionnement
Métrique
Limite taille du réseau
Messages émis
Avantages
Inconvénients
Exercice 4 :Voisinage
On considère le réseau suivant dont le noeud A reçoit les tables de routage suivantes de ses voisins :
Table de B
Destination Lien
A A
C A
D D
E D
F D
G D
H D
Table de C
Destination Lien
A A
B A
D E
E E
F E
G E
H H
Table de E
Destination Lien
A A
B D
C C
D D
F F
G C
H C
1. Les sommets B et D sont-ils voisins?
2. Les sommets E et G sont-ils voisins?
3. Tracer les liens directs connus à partir de ces 3 tables de routage.
4. Compléter le schéma avec les coûts puis déterminer les tables de routage de A et E.
Les coûts des liens sont : AB=3; AC=2; AE=2; CE=5; BD=2; DE=2; EF=6; CH=2; GH=3
Dest. Lien Coût Dest. Lien Coût
T. Rahobisoa 13/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
Exercice 5 :RIP/OSPF
1. En vous basant sur le protocole RIP, déterminer la table de routage du routeur A.
Destination Passerelle Interface Nombre de sauts
2. D'après la table de routage construite ci-dessus, quel est le chemin qui sera emprunté par un paquet
pour aller d'une machine ayant pour adresse IP172.18.1.1/16 à une machine ayant pour adresse IP
172.16.5.3/16?
3. En vous basant sur le protocole OSPF, déterminer la table de routage du routeur A.
On donne les débits suivants :
— liaison routeur A - routeur B : 1 Mbps
— liaison routeur A - routeur C : 10 Mbps
— liaison routeur C - routeur B : 10 Mbps
Destination Passerelle Interface Coût
4. Quel est, d'après la table de routage construite ci-dessus, le chemin qui sera emprunté par un paquet
pour aller d'une machine ayant pour adresseIP 172.18.1.1/16 à une machine ayant pour adresse IP
172.16.5.3/16?
T. Rahobisoa 14/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
Exercice 6 :Considérons le réseau suivant. Dans ce réseau, les noeuds A à F sont des routeurs dont on veut
calculer les tables de routage. On suppose que l'on a exécuté le protocole RIP sur ce réseau.
1. Compléter la table suivante, qui indique pour chaque machine la portion de la table de routage pour la
destination G.
Machine Destination Passerelle Interface Vecteur de distance
A G
B G
C G
D G
E G
F G
On suppose maintenant que le lien B-F tombe en panne.
2. Quel est le vecteur de distance envoyé par B à ses voisins pour atteindre G, une fois qu'il détecte la panne?
(on suppose que les autres noeuds n'ont pas modifié leurs tables de routage)
3. Pour chacun des évènements suivants, dire lequel des quatre cas du protocole RIP est appliqué (cf. cours
“Principe de l'algorithme”). On supposera, pour simplifier, qu'aucun autre événement ne se produit entre-
temps et qu'ils sont tous exécutés “en séquence”.
(a) Les routeurs A et C reçoivent de B le vecteur trouvé à la question 2.
(b) Le routeur C retransmet ce même vecteur D.
(c) Le routeur D transmet le vecteur (G,3) à C.
Exercice 7 :Considérons le réseau ci-dessous. Ce réseau consiste en multiple routeurs interconnectés par des
liaisons. Chaque lien a un coût associé représentant le coût de l'envoi de données sur ce lien.
1. En utilisant l'algorithme de Dijkstra, déterminer le chemin le plus court entre A et tous les autres noeuds
du réseau.
2. Etablir sa table de routage.
T. Rahobisoa 15/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
Exercice 8 :D'après le sujet Bac 2022, Métropole, J2, Ex. 3
On considère le réseau représenté sur la ci-dessous :
On considère la machine d'adresse IPv4192.168.1.1.
1. Donner l'adresse du réseau sur lequel se trouve cette machine.
2. Donner l'adresse de diffusion (broadcast) de ce réseau.
3. Donner le nombre maximal de machines que l'on peut connecter sur ce réseau.
4. On souhaite ajouter une machine sur ce réseau, proposer une adresse IPv4 possible pour cette machine.
La machine d'adresse192.168.1.1 transmet un paquet à la machine d'adresse192.168.4.2.
5. Donner toutes les routes pouvant être empruntées par ce paquet IPv4, chaque routeur ne pouvant être
traversé qu'une seule fois.
6. Expliquerl'utilitéd'avoirplusieursroutespossiblesreliantlesréseaux 192.168.1.0/24et 192.168.4.0/24.
Dans cette question, on suppose que le protocole de routage mis en place dans le réseau est RIP. Ce
protocole consiste à minimiser le nombre de sauts. Le schéma du réseau est celui de la figure ci-dessus.
Les tables de routage utilisées sont données ci-dessous :
7. Recopier et compléter sur la copie la table de routage du routeur A.
8. Un paquet IP doit aller du routeur B au routeur D. En utilisant les tables de routage, donner le parcours
emprunté par celui-ci.
9. Les connexions entre les routeurs B-C et A-E étant coupées, sur la copie, réécrire les tables de routage
des routeurs A, B et C.
10. Déterminer le nouveau parcours emprunté par le paquet IP pour aller du routeur B au routeur D.
Dans cette question, on suppose que le protocole de routage mis en place dans le réseau est OSPF. Ce
protocole consiste à minimiser la somme des coûts des liaisons empruntées.
Le coût d'une liaison est défini par la relation où d représente le débit en bit/s et coût est sans unité.
Le schéma du réseau reste celui du début de l'exercice.
T. Rahobisoa 16/17 AMSER02 - Le routage
Terminale - Spécialité NSI IFS Singapour
11. Déterminer le coût des liaisonsEthernet , Fast-Ethernet et Fibre.
On veut représenter schématiquement le réseau de routeurs à partir du schéma du réseau.
12. Recopier le schéma ci-dessous et tracer les liaisons entre les routeurs en y indiquant leur coût.
Un paquet IPv4 doit être acheminé d'une machine ayant pour adresse192.168.2.1 à une machine ayant
pour adresse 192.168.4.1.
13. Écrire les routes possibles, c'est-à-dire la liste des routeurs traversés, et le coût de chacune de ces routes,
chaque routeur ne pouvant être traversé qu'une seule fois.
14. Donner, en la justifiant, la route qui sera empruntée par un paquet IPv4 pour aller d'une machine ayant
pour adresse 192.168.2.1 à une machine ayant pour adresse192.168.4.1.
Exercice 9 :Sujets supplémentaires de type Bac
Faire un ou plusieurs exercices au choix parmi la liste ci-dessous :
▷ Sujet 1 - Bac 2021 - Exercice 5
▷ Sujet 2 - Bac 2021 - Exercice 5
▷ Sujet 3 - Bac 2021 - Exercice 3
▷ Sujet 6 - Bac 2021 - Exercice 4
▷ Sujet 10 - Bac 2021 - Exercice 1
▷ Sujet 2 - Bac 2022 - Exercice 3
▷ Sujet 3 - Bac 2022 - Exercice 3
▷ Sujet 4 - Bac 2022 - Exercice 2
▷ Sujet 6 - Bac 2022 - Exercice 5
▷ Sujet 7 - Bac 2022 - Exercice 5
▷ Sujet 10 - Bac 2022 - Exercice 5
▷ Sujet 1 - Bac 2022 - Exercice 2
▷ Sujet 13 - Bac 2022 - Exercice 5
Les corrigés sont disponibles ici.
T. Rahobisoa 17/17 AMSER02 - Le routage

## OS

### OS

Terminale - Spécialité NSI IFS Singapour
Chapitre 16 - Systèmes d'exploitation
Objectifs :
▷ Utiliser les commandes de base en ligne de commande.
▷ Gérer les droits et permissions d'accès aux fichiers.
1 Introduction
Dans ce chapitre, nous allons revoir les commandes de base en ligne de commande, vues en classe de1ère,
notamment celles qui sont les plus utilisées dans les deuxsystèmes d'exploitation ou OS (Operating System)
les plus courants :Windows et Linux.
Pour cela, au fur et à mesure que l'on présente les commandes systèmes, vous devez les tester sur chacun des
systèmes d'exploitation.
2 Environnement de travail
2.1 Interpréteur de commandes
Windows Linux
Interpréteur : Interpréteur :
Les commandes sont tapées dans un terminal en
mode texte.
Les commandes sont tapées dans un terminal en
mode texte.
Pour démarrer l'interpréteur de commandes sous
Windows,ilvoussuffitd'allerdanslemenu Démarrer
puis cmd.
Nous allons utiliser le site JsLinux qui simule une
interface Linux.
2.2 Aide sur les commandes
2.2.1 Liste des commandes
Un premier niveau d'aide vous permet d'avoir accès à la liste des commandes de base disponibles depuis votre
interpréteur de commandes. Il vous suffit d'utiliser la commandehelp.
$ help
2.2.2 Aide sur une commande particulière
Il est aussi possible d'obtenir de l'aide sur une commande particulière afin de connaître les options et les
arguments pour l'utiliser.
$ help commande
Par exemple :
$ help cd
Retourne :
cd [-L|[-P [-e]] [-@]] [dir]
Change the shell working directory.
Change the current directory to DIR. The default DIR is the value of the
HOME shell variable [...]
T. Rahobisoa 1/10 AMSER03 - Systèmes d'exploitation
Terminale - Spécialité NSI IFS Singapour
3 Répertoires
Rappel :
Imaginez une grande commode qui contient des tiroirs dans lesquels pourraient se trouver des fichiers et d'autres
tiroirs,...,etc.
Un répertoire peut donc contenir :
— des fichiers,
— d'autres répertoires.
Sous Windows Sous Linux
C: est la racine de votre disque dur / est la racine unique sousLinux.
D: est la racine de votre lecteur optique (BluRay)
E: est la racine d'un lecteur réseau partagé, ...,etc. Il n'y a pas de lettre de lecteur carLinux ne donne
pas de nom aux lecteurs comme le faitWindows. Il
dit juste : « La base, c'est/ ».
3.1 Visualisation des répertoires
Sous Windows Sous Linux
La commande dir (directory) permet de lister le
contenu d'un répertoire.
La commande ls (list subdirectory) permet de
lister le contenu d'un répertoire.
Les options de ce tableau peuvent être utilisées sépa-
rément ou conjointement.
Vous pouvez trouver les différentes options surhttp:
//www.commandeslinux.fr/commande-ls/.
Par exemple :
> dir /S /P
Par exemple :
$ ls -l affiche toutes les informations sur les fichiers
et répertoires, du répertoire courant.
/ A Affiche tous les fichiers y compris
les fichiers caches
/ N Affich le contenu du r e p e r t o i r e au
format long
/ P Affiche le contenu du r e p e r t o i r e en
d e f i l e m e n t par page
/ S Af fi c ha ge recursif du r e p e r t o i r e
courant
La commandetree permet l'affichage récursif du ré-
pertoire courant sous la forme d'un arbre.
> tree
Une des options importante estF pour aussi lister les
fichiers.
La commandetree permet l'affichage récursif du ré-
pertoire courant sous la forme d'un arbre.
$ tree
3.2 Comment se déplacer dans les répertoires?
La commandecd (change directory) permet de se déplacer dans l'arborescence des fichiers. Elle s'utilise en lui
donnant comme argument un répertoire.
$ cd repertoire
Il est possible d'utiliser des chemins relatifs et absolus. Ainsi, pour donner un chemin relatif on peut utiliser le
. qui veut dire le répertoire courant ou.. qui veut dire le répertoire parent.
Exemple pour remonter dans un répertoire parent :
$ cd ..
T. Rahobisoa 2/10 AMSER03 - Systèmes d'exploitation
Terminale - Spécialité NSI IFS Singapour
Sous Windows Sous Linux
La commande cd, utilisée sans argument, vous in-
forme sur le chemin du répertoire courant.
La commande cd, utilisée sans argument, vous in-
forme sur le chemin du répertoire courant.
La commandecd utilisée avec pour argument\ vous
ramène à la racine de l'unité (partition) en cours.
> cd \
La commandecd, utilisée avec pour argument/, vous
ramène à la racine.
$ cd /
Pour changer d'unité, il vous suffit de désigner par
sa lettre la nouvelle unité sur laquelle vous souhaitez
aller.
La commandepwd (print working directory) vous in-
forme sur le chemin du répertoire courant.
Imaginons que vous possédez deux unités appeléesC:
et D:. Vous pouvez taper la lettre en majuscule ou en
minuscule.
> d:
3.3 Créer un répertoire
Sous Windows Sous Linux
La commande mkdir ou md (make directory) permet
de créer un nouveau répertoire (dossier).
La commandemkdir permet de créer un nouveau ré-
pertoire (dossier).
$ mkdir NouveauDossier ou $ md NouveauDossier $ mkdir NouveauDossier
Elle prend en argument le nom du répertoire que vous souhaitez créer.
Par exemple, la commande suivante :
$ mkdir dossier\dossier2
permet de créer un sous-répertoiredossier2 à l'intérieur du répertoiredossier.
3.4 Copier un répertoire
Sous Windows Sous Linux
Pour copier un répertoire et ce qu'il contient, il faut
utiliser la commandexcopy qui permet de copier des
fichiers ou répertoires et ce qu'ils contiennent.
La commande cp -r permet de copier un répertoire
et ses sous-répertoires.
$ xcopy source destination /options $ cp -r source destination
Options spécifiques àxcopy :
/S : Copie les répertoires vides.
/E : Copie les répertoires, y compris ceux vides.
/Y: Confirme la suppression des fichiers existants sans
demande de confirmation.
/H : Copie également les fichiers cachés et systèmes.
Options spécifiques àcp -r :
-i : Demande confirmation avant d'écraser les fichiers
existants.
-u : Ne copie que les fichiers plus récents que ceux
déjà existants dans la destination.
-r : Copie les répertoires de manière récursive.
Plus d'options disponibles. Plus d'options disponibles.
T. Rahobisoa 3/10 AMSER03 - Systèmes d'exploitation
Terminale - Spécialité NSI IFS Singapour
3.5 Supprimer un répertoire
Sous Windows Sous Linux
La commandermdir ou rd (remove directory) permet
de supprimer un répertoire vide.
La commandermdir permet de supprimer un réper-
toire vide.
Deux conditions permettent de supprimer un réper-
toire avec cette commande :
1. On doit être à l'extérieur du répertoire.
2. Il doit être vide.
Répertoire vide :
rmdir test
Par exemple, la commande suivante supprime le ré-
pertoire videtest qui a été créé dansdossier.
$ rd dossier\test
4 Fichiers
4.1 Renommer un fichier
Sous Windows Sous Linux
La commande rename ou ren en abrégé, change le
nom d'un fichier.
La commande mv (move) permet de déplacer ou de
renommer des fichiers sousLinux.
Sa syntaxe générale est la suivante :
$ rename ancien_nom nouveau_nom $ mv ancien_nom nouveau_nom
4.2 Supprimer un fichier
Sous Windows Sous Linux
La commandedel ou erase supprime un ou plusieurs
fichiers.
La commande rm (remove) permet de supprimer un
fichier ou un dossier sousLinux.
Sa syntaxe générale est la suivante :
$ del fichier1.txt fichier2.txt
$ rm fichier1.txt fichier2.txt
Plusieurs options peuvent être utilisées avec cette
commande. Par exemple :
$ del /s monDossier\*.txt
va supprimer tous les fichiers textes dansmonDossier
ainsi que dans tous les sous-dossiers demonDossier.
Plusieurs options peuvent être utilisées avec la com-
mande rm.
Remarquez le joker * qui permet des suppressions
multiples en une seule opération.
Vous pouvez consulter ce site http://www.
commandeslinux.fr/commande-rm/ pour plus
d'informations.
T. Rahobisoa 4/10 AMSER03 - Systèmes d'exploitation
Terminale - Spécialité NSI IFS Singapour
4.3 Copier un fichier
Sous Windows Sous Linux
La commandecopy permet de copier un ou plusieurs
fichiers d'une source à une destination.
Si on met le nom de répertoire comme destination, le
fichier copié a le même nom que le fichier source.
$ copy test.txt dossier
La commandecp permet de copier un fichier ou plu-
sieurs fichiers sous Linux.
Si on met le nom de répertoire comme destination, le
fichier copié a le même nom que le fichier source.
$ cp test.txt dossier
Si on met un fichier en destination, alors le fichier
copié aura le nom donné en destination.
$ copy test.txt test2.txt
En utilisant le caractère +, il est possible de copier
le contenu de plusieurs fichiers dans un unique fichier.
Par exemple, dans la commande suivante, les contenus
de test et test2 sont copiés dans le fichiertest3.
$ cp test.txt+test2.txt test3.txt
Afin de pouvoir copier plusieurs fichiers, il faut utili-
ser le caractère générique*. Il est possible d'utiliser
deux caractères génériques :*signifie n'importe quelle
combinaison de caractères et? signifie n'importe quel
caractère.
La commande suivante copie tous les fichiers ayant
pour extension.txt à la racine de l'unitéd:.
$ copy *.txt d:
Vous pouvez consulter ce site http://www.
commandeslinux.fr/commande-cp/ pour plus
d'informations sur la commandecp.
4.4 Créer un fichier vide
Sous Windows Sous Linux
La commande copy nul permet de créer un fichier
vide.
La commandetouch permet de créer un fichier vide.
$ copy nul test.txt $ touch test.txt
5 Exercices
Exercice 1 : Linux cheatsheet
A partir du site suivant, faire un mémento des commandes fondamenalesLinux que vous devez connaître pour
le Bac. Faire un tableau avec les commandes suivantes :
— ls
— cd
— pwd
— cp
— mv
— rm
— mkdir
— chmod
— chown
— ainsi que les commandes de gestion de processus (top, free, ps, kill)
T. Rahobisoa 5/10 AMSER03 - Systèmes d'exploitation
Terminale - Spécialité NSI IFS Singapour
Exercice 2 : Application directe
Réaliser les actions suivantes surWindows (cmd) et surLinux :
1. Créer un dossiertest et un sous-dossier à l'intérieur de ce dossiertest2.
2. Afficher l'arborescence de vos dossiers pour vérifier qu'ils ont bien été créés.
3. Dans le dossiertest2 créer un fichier videexemple.txt.
4. Afficher l'arborescence de vos dossiers pour vérifier qu'ils ont bien été créés.
5. Créer une copie deexemple.txt et le nommer parexemple2.txt
6. Afficher l'arborescence de vos dossiers pour vérifier qu'il a bien été créé.
7. Créer une copie du dossiertest2 et le nommertest3.
8. Supprimer le dossiertest2.
9. Est-ce que cela fonctionne?
Pour les exercices 2 et 3, vous prendrez soin de compter le nombre d'opérations ou de commandes nécessaires
pour réaliser chaque exercice.
Exercice 3 : Mode graphique
Admettons que vous soyez historien et que vous souhaitiez rédiger un texte concernant l'histoire, le présent et
le futur de plusieurs pays. Vous devez donc constituer pour chaque pays un dossier qui doit contenir trois sous-
dossiers qui contiendront les documents sur chacun des trois sujets principaux de l'histoire :passe, present et
futur.
Un extrait de cette hiérarchie de dossiers se présentera de la façon suivante (ceci devrait vous servir de référence
lors des exercices suivants) :
Partie Afrique :
1. Créer le répertoireTerre et à l'intérieur de celui-ci le répertoireAfrique et à l'intérieur de ce dernier le
répertoire Kenya.
2. Sélectionner le répertoireKenya et créez trois dossierspasse, present et futur.
La structure d'un pays est maintenant complète.
3. Dupliquer cette structure pour les autres pays en ajoutant les pays suivants :Madagascar, leCameroun et
l'Afrique du sud pour l'Afrique ainsi queSingapour, leVietnam et leCambodge pour l'Asie.
T. Rahobisoa 6/10 AMSER03 - Systèmes d'exploitation
Terminale - Spécialité NSI IFS Singapour
Exercice 4 : Lignes de commandes sous Windows
Faire les mêmes exercices mais avec l'interpréteur de commandes pour les continentsAsie, Europe, Amérique
et Océanie. N'oubliez pas d'aller chercher l'aide sur les commandes pour trouver les bonnes options qui peuvent
diminuer le nombre de commande à réaliser pour faire une opération.
Vous devez utiliser les commandesmd et xcopy!
Exercice 5 : Lignes de commandes sous Linux
Pour les TP nécessitant un terminal Linux, vous pouvez également utiliser ce site :
http://s-macke.github.io/jor1k/demos/main.html
À partir du répertoire courant et en utilisant les commandesmkdir et touch, créer l'arborescence suivante :
1. Placez-vous dans le répertoiredir1. Lister les fichiers. Que constatez-vous? Chercher l'option de la com-
mande ls qui permet d'obtenir ce qui est attendu à l'aide de la commandeman ls.
2. Donner le chemin relatif defichier3.
3. Taper la commandecd .. Donner à nouveau le chemin relatif defichier3.
4. Taperlacommandecd dir2/puislacommande cp fichier3 ../dir2/fichier4 .Vérifierquele fichier4
a bien été créé.
5. Taper la commandecd .. puis la commandermdir dir1. Que se passe-t-il? Expliquer pourquoi à l'aide
de la commandeman rmdir.
6. Déplacer l'ensemble des fichiers contenus dans le répertoire dir1 dans le répertoiredir2en saisissant depuis
le répertoire courant; mv dir1/* dir2/
* est un métacaractère (wildcard en anglais), il remplace tout les nom de fichiers.
*.jpg signifierait tous les fichiers dont l'extension est jpg.
7. Effacer le répertoiredir1/
Exercice 6 : Redirection dans un fichier
1. Dans le répertoire courant, taper :echo ‘Longtemps, je me suis couché de bonne heure.‘
2. Danslerépertoirecourant,taper: echo ‘Longtemps, je me suis couché de bonne heure.‘ > debut.txt
3. Lire le fichierdebut.txt à l'aide de la commandecat debut.txt
4. Taperensuite: echo 'Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que
je n'avais pas le temps de me dire : « Je m'endors. » ' » debut.txt
5. Lire le fichierdebut.txt.
T. Rahobisoa 7/10 AMSER03 - Systèmes d'exploitation
Terminale - Spécialité NSI IFS Singapour
Pour mieux comprendre :
▷ commande > fichier envoie le contenu de la sortie standard ( par défaut le terminal) de la com-
mande dans le fichier fichier en écriture avec écrasement du contenu précédent.
▷ commande » fichier envoie le contenu de la sortie standard de la commande dans le fichier fichier
en écriture avec ajout à la fin du fichier.
▷ echo texte envoie texte dans la sortie standard
▷ cat NomFichier affiche le contenu deNomFichier
Exercice 7 : D'autres possibilités du shell
Taper chacune des lignes de commandes. Observer les résultats obtenus et faire des recherches sur Internet pour
comprendre ce que font chacune des commandes.
1. curl wttr.in/singapore (Fonctionne également dans le terminalWindows si ne marche pas surCocalc)
2. cal
3. date
4. echo "4+6" | bc -l
5. echo "scale=10; 4*a(1)" | bc -l
6. ls | sort –r ( à comparer avecls seul)
7. echo ‘Un palindrome' | rev
8. echo $(($RANDOM %6 +1)) (la répéter plusieurs fois)
9. yes (saisir Ctrl + Cpour arrêter)
10. factor 12 puis factor 13 puis factor 64
11. while true; do echo "$(date '+%D %T')" ; sleep 1; done (Ctrl + Cpour arrêter)
Exercice 8 : Script Shell sous Linux
Dans cet exercice nous allons créer un scriptShell. Pour cela :
1. Aller surCocalc.
2. Aller dans l'ongletNew à côté deFiles en haut de la page.
3. Entrer le nom du fichier, par exemplescript.
4. Dans la liste déroulanteMore file types, choisissezShell(.bash).
5. Cela crée et ouvre le nouveau fichier dans un éditeur texte.
6. Ne pas oublier d'utiliser le bouton de sauvegarde avant de tester votre script.
7. Recopier le programme ci-dessous dans le fichierscript.sh
1 #!/bin/bash
2 for i in $(seq 1 10)
3 do
4 if test -d TP$i
5 then
6 echo "TP$i existe deja"
7 else
8 echo "creation de TP$i"
9 mkdir "TP$i"
10 fi
11 done
8. Dans le terminal, rendre votre script exécutable avec la commandechmod.
9. Exécuter le programme en tapant la commande :./script.sh
T. Rahobisoa 8/10 AMSER03 - Systèmes d'exploitation
Terminale - Spécialité NSI IFS Singapour
10. Que se passe-t-il?
11. Pour régler le problème, faire des recherches sur la commandechmod.
12. Commenter ce script en décrivant précisément ce qui se passe à chaque ligne. Comme en Python, les
commentaires en shell commencent par un# et finissent à la fin de la ligne.
13. Améliorer le programme pour qu'il puisse créer dans chaque dossier seulement s'il existe déjà, 5 fichiers
denommés new_file_1.txt, new_file_2.txt, ...,new_file_5.txt. Vous pouvez utiliser la commande
touch "TP$i/new_file_$j.txt"
14. Pouvons-nous trouver une commande pour supprimer en une seule fois tous les dossiers et fichiers que
nous venons de créer?
Exercice 9 : Terminus
Dans cet exercice vous allez découvrir un certain nombres de commandesLinux/UNIX, utilisable dans leshell
à travers un escape game en ligne :Terminus.
Vous trouverez ce jeu à l'url suivante :http://luffah.xyz/bidules/Terminus/
Jouer àTerminus et compléter au fil du jeuune représentation du monde de Terminus sous la forme d'une
arborescence, comme celle d'un système de fichiers.
On donne ci-dessous un tableau des commandes disponibles au début du jeu :
Commande Description Syntaxe
cat Afficher dans la console Saisir cat Objet ou cat Personne
ls Lister les éléments Saisir ls
cd Changer de destination cd .. pour revenir à l'emplacement précédent
cd Changer de destination cd Salle pour entrer dans Salle
cd Changer de destination cd ~ pour revenir au point de départ
Exercice 10 : Find your path
1. Aller sur le sitehttps://demo710.univ-lyon1.fr/FYP/
2. Appuyer sur F1 pour basculer en français.
3. Indiquer les chemins relatifs ou absolus pour aller vers le dossier indiqué en vert à partir du dossier courant
(en rose).
T. Rahobisoa 9/10 AMSER03 - Systèmes d'exploitation
Terminale - Spécialité NSI IFS Singapour
Cela peut paraître étonnant pour des personnes n'ayant rien connu d'autre que l'interface graphique utilisateur,
mais leTerminal (aussi appeléconsole) est un outil de travail indispensable pour de nombreux développeurs et
Ops. Il y a plusieurs raisons à cela :
T. Rahobisoa 10/10 AMSER03 - Systèmes d'exploitation

## Processus

### Processus

Terminale - Spécialité NSI IFS Singapour
Chapitre 17 - Les processus
Objectifs :
▷ Décrire la création d'un processus, l'ordonnancement de plusieurs processus par le système.
▷ Mettre en évidence le risque de l'interblocage (deadlock).
1 Introduction
Dans les années 1970, les ordinateurs personnels n'étaient pas capables d'exécuter plusieurs tâches à la fois. On
lançait un programme et on y restait jusqu'à ce que celui-ci "plante" ou se termine.
Les systèmes d'exploitation récents (Windows, Linux ou MacOS par exemple) permettent d'exécuter plusieurs
tâches simultanément - ou en tous cas, donner l'impression que celles-ci s'exécutent en même temps. C'est ce
que l'on appelle lepseudo-parallélisme.
A un instant donné, il n'y a donc pas un mais plusieurs programmes qui sont en cours d'exécution sur un
ordinateur : on les nommeprocessus.
Une des tâches du système d'exploitation est d'allouer à chacun des processus les ressourcesdont il
a besoin en termes de mémoire, entrées-sorties ou temps processeur, et des'assurer que les processus
ne se gênent pas les uns les autres.
Nous avons tous été confrontés à la problématique de la gestion des processus dans un système d'exploitation,
en tant qu'utilisateur :
— quand nous cliquons sur l'icône d'un programme, nous provoquons la naissance d'un ou plusieurs processus
liés au programme que nous lançons
— quand un programme ne répond plus, il nous arrive de lancer le gestionnaire de tâches pour tuer le
processus en défaut
Nous allons voir en détails dans ce cours comment les processus sont gérés dans les systèmes d'exploitation.
Un processus peut déclencher d'autres processus. On dira que ce sont des processusparent et fils.
Certains fonctionnent en permanence enarrière-plan (comme un antivirus) et ceux qui s'exécutent dès le
démarrage de la machine (lesservices sous Windows ou lesdaemons sous Linux).
T. Rahobisoa 1/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
2 Programme ̸= Processus
On peut comparer un programme à une recette de cuisine listant les ingrédients et décrivant la méthode à
utiliser pour la réaliser.
Le processus serait alors quelqu'un qui a récupéré la recette, acheté les ingrédients et qui serait en train de
réaliser la recette.
De plus à un instant donné, on peut avoir plusieurs personnes dans la même cuisine. Chacun s'occupe d'une
recette (la même ou pas...), chacun est sur son propre exemplaire de recette et dans un état d'avancement
différent.
A retenir!
Un programme est une suite figée d'instructions, un ensemble statique.
Un processus est une exécution (ou une ‘instance') d'un programme sur un ordinateur.
Il est caractérisé par :
▷ Un ensemble d'instructions à exécuter- souvent stockées dans un fichier exécutable sur lequel
on clique pour lancer un programme. (ex. firefox.exe)
▷ Un espace mémoire dédié à ce processuspour lui permettre de travailler sur des données qui
lui sont propres : si vous lancez deux instances Firefox, chacune travaillera indépendamment de
l'autre avec ses propres données. C'est ce qu'on appelle le contexte d'un processus.
▷ Des ressources matérielles: processeur, entrées-sorties ...
La gestion des processus offerte par le système d'exploitation permet d'agir de façon individuelle sur les diffé-
rentes tâches sans impacter les autres.
On peut par exemple :
— en mettre certaine en pause.
— en terminer d'autres.
— gérer les tâches en fonction de priorités.
T. Rahobisoa 2/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
3 Création d'un processus
A retenir!
La création d'un processus peut intervenir :
▷ au démarrage du système
▷ par unappel d'un autre processus
▷ par uneaction d'un utilisateur(lancement d'application)
L'illustration ci-contre montre le graphe d'appels des processus
sous Linux.
On comprend que tous les processus et applications sont en fait
démarrés par le Processus 0 , qui est lancé au démarrage de la
machine; celui-ci lance ensuite le processus filsinit qui va lancer
les processus systèmes ( daemons) qui vont eux-mêmes lancer
d'autres processus,...,etc.
Lors de sa création, un processus sera identifié par :
— Un numéro PID (Process Identification)
— Un PPID (le numéro du processus parent)
— Un UID, l'identifiant de l'utilisateur qui l'a lancé
4 Etat du processus
Dans un système multitâches, plusieurs processus peuvent se trouver simultanément en cours d'exécution : ils
se partagent l'accès aux ressources de la machine (Entrée-sortie, CPU, mémoire...).
A retenir!
Un processus peut prendre 3 états :
▷ État actif ou élu (running) : le processus utilise le processeur.
▷ État prêt ou éligible (ready) : le processus pourrait utiliser le processeur s'il était libre (et si
c'était son tour).
▷ État en attenteou bloqué : le processus attend une ressource (ex : fin d'une entrée-sortie, par
exemple il est en pause car il attend que l'utilisateur fasse une entrée clavier...).
T. Rahobisoa 3/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
Tout processus qui se bloque en attente d'un événement, passe dans l'état bloqué tant que l'événement attendu
n'est pas arrivé.
Lors de l'occurrence de cet événement, le processus passe dans l'état prêt. Il sera alors susceptible de se voir
attribuer le processeur pour continuer ses activités.
A retenir!
Le changement d'état d'un processus peut être provoqué par :
— un autre processus(qui lui a envoyé un signal, par exemple)
— le processus lui-même(appel à une fonction d'entrée-sortie bloquante),
— une interruption (fin de quantum, terminaison d'entrée-sortie, ...,etc.)
La sortie de l'état actif pour passer à l'état prêt se produit dans le cas des ordonnancements lorsqu'un processus
plus prioritaire que le processus actif courant devient prêt.
5 Ordonnancement
Si le processus est en cours d'exécution, le contexte est mis en mémoire dans les registres du processeur.
Si le processus est mis en pause pour qu'un autre s'exécute, le contexte est mis en mémoire quelque part et sera
rappelé dans les registres du processeur lorsque le processus aura de nouveau la main.
Voici un schéma qui illustre l'ordonnancement de 3 processus (P1, P2, et P3) avec un seul processeur.
Chacun des processus occupe le processeur pendant un certain temps.
La mise en mémoireet le rappel des contextesest très important pour que l'exécution d'un processus
n'interfère pas avec les autres.
Il existe plusieurs types d'ordonnancement :
1. FIFO(First In, First Out):,parexemplelafiled'impressiondansuneimprimante.Icilepremierprocessus
à arriver va utiliser la ressource jusqu'à ce qu'il ait terminé.
2. Round Robin : la ressource est affectée à chaque processus à tour de rôle. On définit une durée fixe
pendant laquelle un processus est exécuté sur le processeur
3. Avec priorité: l'ordre est déterminé par la priorité du processus; si un processus plus prioritaire arrive,
c'est lui qui prend la main.
4. Le plus court d'abord: ici on s'intéresse à la durée d'exécution de chaque processus. Cet ordonnance-
ment est très efficace pour satisfaire au mieux les utilisateurs; mais il n'est pas toujours facile d'évaluer
la durée d'une tâche avant son début.
T. Rahobisoa 4/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
6 Interblocage ( deadlock)
Les interblocages sont des situations de la vie quotidienne. Un exemple est celui du carrefour avec priorité à
droite où chaque véhicule est bloqué car il doit laisser le passage au véhicule à sa droite.
En informatique également, l'interblocage peut se produire lorsque des processus concurrents s'attendent mu-
tuellement. Les processus bloqués dans cet état le sont définitivement. Ce scénario catastrophique peut se
produire dans un environnement où des ressources nécessaires sont partagées entre plusieurs processus et l'un
d'entre eux détient indéfiniment une ressource nécessaire à l'autre.
6.1 Les 4 conditions de l'interblocage
Cette situation d'interblocage a été théorisée par l'informaticienEdward Coffmanqui a énoncé quatre conditions
(appelées conditions de Coffman) menant à l'interblocage :
A retenir!
1. Exclusion mutuelle: au moins une des ressources du système doit être en accès exclusif, seule
un processus peut l'utiliser à la fois
2. Rétention des ressources (Hold and wait) : un processus détient au moins une ressource et
requiert une autre ressource détenue par un autre processus
3. Non préemption: seul le détenteur d'une ressource peut la libérer.
4. Attente circulaire: chaque processus attend une ressource détenue par un autre processus.
P1 attend une ressource détenue parP2 qui à son tour attend une ressource détenue parP3, ...,etc., qui attend
une ressource détenue parP1 ce qui clos la boucle.
6.2 Comment s'en prémunir ?
Il existe trois stratégies pour éviter les interblocages :
▷ la prévention: on oblige le processus à déclarer à l'avance la liste de toutes les ressources auxquelles il
va accéder.
▷ l'évitement : on fait en sorte qu'à chaque étape il reste une possibilité d'attribution de ressources qui
évite le deadlock.
▷ la détection/résolution: on laisse la situation arriver jusqu'au deadlock, puis un algorithme de résolu-
tion détermine quelle ressource libérer pour mettre fin à l'interblocage.
T. Rahobisoa 5/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
6.3 Le deadlock dans la vie courante
▷ L'emballage diabolique
▷ Le carrefour maudit
▷ L'entretien d'embauche
T. Rahobisoa 6/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
7 Exercices
Exercice 1 :Task manager
Ouvrir le gestionnaire de tâches de Windows en faisantCTRL+ALT+Suppr ou en tapant la commandetaskmgr
dans la console, puis en choisissantTask Manager. Aller dans l'ongletDétails
1. Quel processus utilise le plus de mémoire?
2. Combien de pourcentage du temps le processeur est-il en attente (System Idle Process)?
3. Quel processus utilise le plus le CPU?
4. Combien y a-t-il d'utilisateurs?
Faire un clic droit sur un des processus. Les actions disponibles sont :
— End task pour interrompre immédiatement le processus
— End processtree pour interrompre immédiatement le processus et son arborescence (les processus fils
qu'il a démarré)
— Set Prioritypour changer la priorité de ce processus par rapport aux autres
5. Ouvrir l'ongletServices. Il permet de voir les processus systèmes qui sont exécutés en arrière plan.
Vous pouvez observer l'utilisation des ressources (mémoire, disque, réseau) dans l'ongletPerformances.
L'utilisation du CPU est donnée soit de manière globale soit séparément par coeur. Pour voir l'un ou
l'autre des affichages, faire un clic droit et choisirChange graph to.
6. Aller maintenant surCocalc et saisir la commandetop. Il s'agit du gestionnaire de processus deLinux.
7. Quelles sont les colonnes communes avec l'ongletDétails du Gestionnaire de tâches Windows?
Exercice 2 :Console Windows
1. Faire une recherche pour savoir comment démarrer depuis la consoleWindows le programme msedge
(Microsoft Edge) en fournissant l'adresse du site du lycée.
2. Combien de processus ont été démarrés? Quels sont leurs PID? Quelle est leur relation?
3. Identifier le PID du processus qui consomme le plus de mémoire.
4. Que permet de faire la commandetasklist dans une consoleWindows?
5. Chercher de l'aide sur la commande taskkill et utilisez-la pour terminer le processus msedge qui
consomme le plus de mémoire. Que se passe-t-il?
6. Utiliser l'option /F pour forcer à terminer ce processus.
7. Terminer le processusmsedge qui consomme le moins de mémoire.
8. Expliquer ce que vous observez.
T. Rahobisoa 7/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
Exercice 3 :Ordonnancement et chronogramme
On considère un systèmemonoprocesseur et les4 processus P1, P2, P3 et P4 qui effectuent du calcul et
des entrées/sorties avec un disque selon les temps donnés ci-dessous :
On considère que l'ordonnancement sur le processeur se fait selon une politique FIFO : le processus élu à un
instant t est celui qui est le plus anciennement dans l'état prêt. Initialement, l'ordre de soumission des processus
est P1, puis P2, puis P3, puis P4.
De même, on considère que l'ordre de services des requêtes d'E/S pour le disque se fait selon une politique
FIFO.
Sur graphe suivant, donnez le chronogramme d'exécution des 4 processus P1, P2, P3 et P4 :
Vous distinguerez les états des processus :Prêt, Actif et Bloqué et vous indiquerez le contenu des files d'attente
des processus (attente processeur et attente du disque, rappelons que le disque ne peut exécuter qu'une seule
opération à la fois).
Pour vous guider, la première unité de temps est déjà portée sur le chronogramme.
Justifier votre raisonnement, en expliquant la gestion des files d'attentes et les transitions des processus. Donnez
le temps de réponse moyen obtenu.
T. Rahobisoa 8/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
Exercice 4 :Ordonnancement de 3 processus
Les trois processus suivants doivent être exécutés simultanément sur un ordinateur à un processeur :
Instruction 1
Instruction 2
Instruction 3
Instruction 4
Instruction 5
Instruction 6
Instruction 7
Processus 1
Instruction 1
Instruction 2
Instruction 3
Processus 2
Instruction 1
Instruction 2
Processus 3
1. L'ordonnanceur du système d'exploitation utilise l'ordonnancement duplus court d'abord. Schématiser
l'ordre de traitement des instructions des trois processus.
2. Schématiser l'ordre de traitement des instructions des trois processus pour un ordonnancementRound
Robin.
3. Ecrire en Python le programme correspondant. Utiliser par exemple la liste suivante :
1 l i s t e _ p r o c e s s u s = [
2 # pr o ce ss us 1
3 [ " p1_i1 " ," p1_i2 " ," p1_i3 " ," p1_i4 " ," p1_i5 " ," p1_i6 " ," p1_i7 " ] ,
4 # pr o ce ss us 2
5 [ " p2_i1 " ," p2_i2 " ," p2_i3 " ] ,
6 # pr o ce ss us 3
7 [ " p3_i1 " ," p3_i2 " ]
8 ]
Exercice 5 :Excercice type BAC
Cet exercice est l'exercice n°2 du sujet n°2 du BAC 2021 métropole en candidat libre.
Les états possibles d'un processus sont : prêt, élu, terminé et bloqué.
1. Expliquer à quoi correspond l'état élu.
2. Proposer un schéma illustrant les passages entre les différents états.
Onsupposequequatreprocessus C1, C2, C3 et C4 sontcrééssurunordinateur,etqu'aucunautreprocessus
n'est lancé sur celui-ci, ni préalablement ni pendant l'exécution des quatre processus.
L'ordonnanceur, pour exécuter les différents processus prêts, les place dans une structure de données de
type file. Un processus prêt est enfilé et un processus élu est défilé.
T. Rahobisoa 9/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
Parmi les propositions suivantes, recopier celle qui décrit le fonctionnement des entrées/sorties dans une
file :
— Premier entré, dernier sorti
— Premier entré, premier sorti
— Dernier entré, premier sorti
3. On suppose que les quatre processus arrivent dans la file et y sont placés dans l'ordreC1, C2, C3 et C4 .
▷ Les temps d'exécution totaux deC1, C2, C3 et C4 sont respectivement 100 ms, 150 ms, 80 ms et 60
ms.
▷ Après 40 ms d'exécution, le processusC1 demande une opération d'écriture disque, opération qui
dure 200 ms. Pendant cette opération d'écriture, le processusC1 passe à l'état bloqué.
▷ Après 20 ms d'exécution, le processusC3 demande une opération d'écriture disque, opération qui
dure 10 ms. Pendant cette opération d'écriture, le processusC3 passe à l'état bloqué.
Sur la frise chronologique ci-dessous donnée en annexe, les états du processusC2 sont donnés.
Compléter la frise avec les états des processusC1, C3 et C4.
On trouvera ci-dessous deux programmes rédigés en pseudo-code.
Verrouiller un fichier signifie que le programme demande un accès exclusif au fichier et l'obtient si le fichier
est disponible.
Programme 1 Programme 2
Verrouiller fichier_1 Verrouiller fichier_2
Calculs sur fichier_1 Verrouiller fichier_1
Verrouiller fichier_2 Calculs sur fichier_1
Calculs sur fichier_1 Calculs sur fichier_2
Calculs sur fichier_2 Déverrouiller fichier_1
Calculs sur fichier_1 Déverrouiller fichier_2
Déverrouiller fichier_2
Déverrouiller fichier_1
4. En supposant que les processus correspondant à ces programmes s'exécutent simultanément (exécution
concurrente), expliquer le problème qui peut être rencontré.
5. Proposer une modification du programme 2 permettant d'éviter ce problème.
Exercice 6 :Faire l'exercice 3 du sujet BAC 2023 - Polynésie suivant.
T. Rahobisoa 10/11 AMSER05 - Processus
Terminale - Spécialité NSI IFS Singapour
Exercice 7 :Excercice type BAC
Cet exercice est la première partie de l'exercice 3 du sujet 1 candidat libre Métropole 2021.
La commande UNIXps présente un cliché instantané des processus en cours d'exécution.
Avec l'option-eo pid , ppid, stat, command, cette commande affiche dans l'ordre l'identifiant du processusPID
(process identifier), le PPID (parent process identifier ), l'état STAT et le nom de la commande à l'origine
du processus.
Les valeurs du champSTAT indique l'état des processus :
▷ R : processus en cours d'exécution
▷ S : processus endormi
Sur un ordinateur, on exécute la commandeps -eo pid , ppid,stat, command et on obtient un affichage dont
on donne ci-dessous un extrait.
À l'aide de cet affichage, répondre aux questions ci-dessous.
1. Quel est le nom de la première commande exécutée par le système d'exploitation lors du démarrage?
2. Quels sont les identifiants des processus actifs sur cet ordinateur au moment de l'appel de la commande
ps? Justifier la réponse.
3. Depuis quelle application a-t-on exécuté la commande ps? Donner les autres commandes qui ont été
exécutées à partir de cette application.
4. Expliquer l'ordre dans lequel les deux commandespython programme1.py et python programme2.py ont
été exécutées.
5. Peut-on prédire que l'une des deux commandespython programme1.py et python programme2.py finira
avant l'autre?
Exercice 8 :Illustration de l'interblocage en Python
Sur Colab, suivre les consignes du document suivant.
Exercice 9 :Sujets BAC supplémentaires
— Exercice 2 du sujet de BAC 2023 - Polynésie.
— Exercice 2 du sujet de BAC 2022 - Amérique du Nord.
— Exercice 2 du sujet de BAC 2022 - Polynésie.
— Exercice 2 du sujet de BAC 2021 - Amérique du Nord.
— Exercice 2 du sujet de BAC 2021 - Candidats libres.
— Exercice 4 du sujet de BAC 2021 - Métropole.
T. Rahobisoa 11/11 AMSER05 - Processus

## SoC

### SoC

Terminale - Spécialité NSI IFS Singapour
Chapitre 18 - Les systèmes sur puce
Objectifs :
▷ Connaître quelques composants intégrés d'un système sur puce
▷ Identifier les principaux composants sur un schéma de circuit
▷ Comprendre les avantages de leur intégration en terme de vitesse et de consommation
1 Introduction
La réduction de taille des éléments des circuits électroniques a conduit à l'avènement de systèmes sur puce.
Ce SoC (pour System on a Chipen anglais) qui regroupe dans un seul circuit nombre de fonctions autrefois
effectuées par des circuits séparés assemblés sur une carte électronique.
Un tel système sur puce est conçu et mis au point de façon logicielle, ses briques électroniques sont accessibles
par des API, comme pour les bibliothèques logicielles.
2 De l'ordinateur au smartphone/tablette
Dans un ordinateur “classique” tel qu'un PC de bureau, le "hardware" est organisé autour de 4 éléments
principaux :
▷ le processeur(CPU – Central Processing Unit) se charge de réaliser les calculs les plus courants, ceux
qui permettent par exemple de faire tourner le système d'exploitation ou un navigateur web.
▷ la mémoire vive(RAM – Random Access Memory) permet d'enregistrer temporairement les données
traitées par le processeur.
▷ la carte graphique(ou GPU – Graphics Processing Unit) se charge d'afficher une image, qu'elle soit
en 2D ou bien en 3D comme dans les jeux.
▷ la carte-mère (Motherboard) permet l'acheminement des données entre les composants (CPU, RAM,
GPU,disque dur, SSD, cartes réseau,..., etc.) via des "bus".
Principaux éléments d'un PC :
1. CPU surmonté d'un dissipateur thermique (ventirad)
2. Barrettes de RAM
3. GPU
4. Carte mère
Mais depuis le début de l'ère des smartphones et des tablettes, on assiste à l'émergence de systèmes tout-en-un
appelé SoC (System on a Chip) afin d'optimiser la miniaturisation et l'intégration des différents composants.
Ces derniers sont alors bien mieux interconnectés les uns aux autres, avec par exemple une fréquence processeur
qui varie en fonction de la fréquence de la carte graphique du fait de contraintes thermiques et de consommation.
Un Soc présente donc une structure complètement inédite par rapport à un ordinateur classique où chaque
composant est plus ou moins indépendant.
T. Rahobisoa 1/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
A retenir!
Un « système sur une puce», souvent désigné dans la littéra-
ture scientifique par le terme anglaissystem on a chip (d'où son
abréviation SoC), est un système complet embarqué sur une seule
puce ("circuit intégré"), pouvant comprendre de la mémoire, un ou
plusieurs microprocesseurs, des périphériques d'interface, ou tout
autre composant nécessaire à la réalisation de la fonction attendue.
On peut intégrer de la logique, de la mémoire (statique, dynamique,
flash,ROM,PROM,EPROM,EEPROM), des dispositifs (capteurs)
mécaniques, opto-électroniques, chimiques ou biologiques ou des cir-
cuits radio,...,etc.
Puce ARM Exynos
Smartphone Nexus S de Samsung
3 Composition d'un SoC
Un System on Chip(SoC) est un circuit intégré qui regroupe sur une seule puce plusieurs composants essentiels
commeleprocesseur,leGPU,lamémoireetlescontrôleurs.Cetteintégrationpermetderéduirelaconsommation
d'énergie, d'améliorer les performances et d'optimiser l'espace dans les appareils électroniques.
Très utilisé dans les smartphones, tablettes et objets connectés, le SoC offre une solution compacte et efficace
pour l'informatique embarquée.
Figure 1 – Architecture simplifiée du SoCSamsung Exynos 990 - Galaxy S20
3.1 Le processeur (CPU)
Le processeur ou « Central Processing Unit »(CPU) est le cœur duSoC. Son fonctionnement est identique
à celui d'un ordinateur.
On y retrouve donc plusieurscœurs cadencés à différentesfréquences effectuant desthreads et stockant des
informations encache.
▷ Les cœurs :
Un processeur compte généralement plusieurs cœurs, on parle couramment dans la littérature technique
de dual-core, quad-core ou d'octo-core parfois. Ainsi, ces processeurs se composent respectivement de
T. Rahobisoa 2/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
deux, quatre ou huit cœurs. Ceux-ci permettent de lancer en parallèle plusieurs applications de manière
simultanée (multitâche) et permettent l'utilisation d'application lourde comme des jeux.
▷ La fréquence :
La fréquence d'un processeur est le nombre de cycles de calculs qu'il peut effectuer chaque seconde.
Elle va donc naturellement déterminer la durée d'exécution d'une tâche : plus la fréquence du processeur
est élevée, plus l'exécution d'une tâche est rapide.
Mesurée en gigahertz (GHz), celle-ci est souvent différente entre chaque cœur.
▷ Les threads :
Les cœurs réalisent ce qu'on appelle un thread, littéralement unfil d'exécution, une tâche qui doit être
réalisée par le processeur.
▷ Le cache :
C'est une petite mémoire rapide intégrée au processeur. En effet, celle-ci va permettre destocker les
informations récurrentes au plus près du processeur pour éviter d'avoir à aller les chercher sans arrêt
dans la RAM.
3.2 La puce graphique (GPU)
La puce graphiqueou « Graphics Processing Unit »(GPU) est un élément crucial pour les gamers, car c'est
lui qui est en charge de calculer les images afin de pouvoir les afficher à l'écran.
Celle-ci prend ainsi en charge les images en 2D et en 3D que ce soit une page web, une vidéo ou encore une
partie endiablée de votre jeu favori.
Une carte graphique doit donc réaliser un nombre élevé de tâches, puisque qu'elle doit par exemple calculer la
couleur à affichersur chaque pixel de l'écran de votre smartphone.
Par exemple dans le cas d'une image Full HD (1920×1080), le GPU affiche 2 073 600 pixels différents ou 8 294
400 pixels pour de l'Ultra HD (3840×2160).
Rappelons également que ce calcul est fait selon lafréquence de rafraichissementde l'écran. Celle-ci peut
par exemple varier entre 60 et 120 fois par secondes c'est-à-dire entre 60 Hz et 120 Hz.
3.3 La puce neuronale (NPU)
Lapuce neuronaleou « Neuronal Processing Unit »(NPU) est une puce en charge de l'intelligence artificielle
des smartphones.
Les calculs de l'intelligence artificielle ont longtemps été faits par le biais de serveurs dans le cloud (distant).
Néanmoins, depuis quelques années pour des raisons derapidité et de respect de la vie privée, les calculs
se font désormais directement sur les smartphones.
T. Rahobisoa 3/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
C'est utile par exemple dansGoogle Translatepour reconnaître des caractères, pour optimiser les photos ou
encore l'autonomie.
3.4 Le modem (Interface)
Les smartphones embarquent également dans le SoC une unité réseau assurant la prise en charge des différents
protocoles de communication.
Cette unité est la partie la plus compliquée à développer et à implémenter sur un SoC. Néanmoins, il s'agit d'un
élément crucial afin d'assurer le nomadisme d'un smartphone en itinérance.
Le modem intégré au SoC gère non seulement leWifi, leBluetooth, leNFC ou bien encore lestechnologies
mobiles. C'est-à-dire la4G, ou plus récemment la5G mais également de plus vieux réseaux tels que la3G.
3.5 Le processeur de signal numérique (DSP)
Le processeur de signal numérique ou« Digital Signal Processor »(DSP) est en charge detraiter les signaux
numériques.
Ainsi, il va permettre le filtrage, la compression ou encore l'extraction de différents signaux tels que la musique
ou encore une vidéo.
3.6 Le processeur de signal d'images (ISP)
Le processeur d'image ou « Image Signal Processor » (ISP) est une puce prenant en charge la création
d'images numériques.
En effet, à cause de leurs tailles minuscules, lescapteurs photodes smartphones ne sont pas de très bonne
qualitéd'unpointdevuedel'optiquepure.Laqualitéqu'ilestactuellementpossibled'obtenirvaêtreintimement
liée à cette puce qui va compenser logiquement certaines limitations optiques (zoom numérique).
3.7 Le processeur de sécurité (SPU)
Le processeur de sécurité ou« Secure Processing Unit »(SPU) est le« bouclier » du smartphone.
Son alimentation électrique est indépendante afin de ne pas pouvoir être éteint en cas d'attaque sur celui-ci. Le
SPU est d'une importance capitale.
En effet, celui-ci va stocker les donnéesbiométriques, bancaires, la carte SIM ou encore les titres de
transport. C'est lui qui contient les clés de chiffrement des données de l'utilisateur.
T. Rahobisoa 4/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
4 Les avantages d'un SoC par rapport à un système classique
Outre leur taille miniaturisée bien adaptée aux terminaux nomades (smartphones et tablettes), les SoC offrent
d'autres avantages par rapport aux systèmes "classiques" rencontrés dans les ordinateurs :
▷ les SoC sont conçus pour consommer beaucoup moins d'énergie qu'un système classique à puissance
équivalente de calculs;
▷ cette consommation réduite d'énergie permet dans la plupart des cas de s'affranchir de la présence d'un
système de refroidissement actif comme les ventilateurs ou de type « watercooling »; un système équipé
de SoC est donc silencieux car il chauffe relativement peu;
▷ étant donné les distances très faibles entre, par exemple, le CPU et la mémoire, les données circulent
beaucoup plus vites, ce qui permet d'améliorer grandement les performances; en effet, dans les systèmes
"classiques" les BUS chargés d'acheminer les données sont souvent des "goulots d'étranglement" en termes
de performances à cause de la vitesse limitée de circulation des données. En revanche, le principal inconvé-
nient d'un SoC est que là ou un ordinateur équipé d'une carte mère permet de faire évoluer les composants
individuellement, l'extrême intégration du SoC présente en revanche l'inconvénient de n'autoriser aucune
mise à jour possible du matériel.
5 Quelques familles de SoC utilisées dans les smartphones
Les nouveaux procédés de gravure des semi-conducteurs CMOS telle que lalithographie extrême ul-
traviolette, ont permis de réduire significativement la taille des composants électroniques constituants
les SoC.
Ainsi, on dispose aujourd'hui de la même puissance dans un smartphone que celle embarquée dans un
ordinateur il y a quelques années de cela. Ceci s'est cependant fait au prix d'une complexité technologique
croissante. Par exemple, la génération deSoC des téléphonesiPhone 11est gravée en7 nmdepuis juillet
2019. On rappelle que1nm = 10 −9m!
Le SoC A13 Bionic d'Apple est par exemple composé de 8,5 milliards de transistors répartis sur une
surface de 98, 48mm2. On pense que les futures générations seront gravée en 1 nm aux alentours de 2030!
On trouve une grande variété deSoC en fonction des différents constructeurs. Par exemple, voici les
caractéristiques d'une ancienne génération de smartphones :
SoC Gravure Instructions CPU GPU Smartphone
Exynos 990 7 nm ARM v8.4 8 cœurs 64 bits Mali-G77 MP11 Samsung Galaxy S20
A13-Bionic 7 nm ARM v8.3-A 6 cœurs 64 bits Apple 4 cores Apple iPhone 11
Snapdragon 865 7 nm ARM v8.2-A 8 cœurs 64 bits Qualcomm Adreno 65 0 Xiaomi Mi 10
Kirin 990 7 nm ARM v8.2-A 8 cœurs 64 bits Mali-G76 MP16 Huawei P40
T. Rahobisoa 5/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
Pour les modèles de smartphones du début des années 2020, la principale difficulté technologique a été
d'intégrer auxSoCs les modems 5G qui sont complexes à fabriquer.
Ils étaient gravés en 10 nm sur une puce indépendante duSoC. Le prochain défi technologique a été
d'intégrer les modems 5G directement dans leSoC gravé en 7 nm puis 5 nm.
Figure 2 – Block diagram – Snapdragon 865
6 L'architecture ARM
Dotés d'une architecture relativement plus simple que d'autres familles de processeurs, et bénéficiant d'une
faible consommation électrique, les processeursARM (Advanced Risc Machine) sont devenus dominants dans
le domaine de l'informatique embarquée, en particulier dans la téléphonie mobile et les tablettes.
Les architectures ARM reposent sur des processeurs à jeu d'instructions réduitRISC (Reduced Instruction Set
Computer) 32 bits (ARMv1 à ARMv7) ou 64 bits (ARMv8).
Aujourd'hui, ARM est surtout connu pour ses systèmes sur puce (SoC), inté-
grant sur une seule puce :
▷ microprocesseur
▷ processeur graphique (GPU)
▷ DSP
▷ FPU
▷ SIMD
▷ contrôleur de périphériques
Ceux-ci sont présents dans la majorité des smartphones et tablettes.
ARM propose des architectures qui sont vendues sous licence de propriété intellectuelle aux concepteurs. Ils
proposentdifférentesoptionsdanslesquelleslesconstructeurspeuventprendrecequilesintéressepourcompléter
avec leurs options propres ou de concepteurs tiers.
ARM propose ainsi pour lesSoC les plus récents les microprocesseursCortex (Cortex-A pour les dispositifs
portables de type smartphones et tablettes,Cortex-M pour le couplage à un microcontrôleur,Cortex-R pour
les microprocesseurs temps réel), des processeurs graphiques (Mali), des busAMBA sous licence libre, ainsi que
les divers autres composants nécessaires à la composition duSoC complet.
Certains constructeurs, tels queNvidia, préfèrent produire leur propre processeur graphique, d'autres, comme
Samsung, préfèrent prendre dans certains cas un processeur graphique de prestataire tiers ou d'ARM selon les
modèles, et d'autres, commeApple, modifient certains composants du microprocesseur en mélangeant plusieurs
architectures processeur ARM.
T. Rahobisoa 6/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
7 Conclusion
Les SoCs sont utilisés dans tous les téléphones, tablettes, système embarqués et consoles :
▷ iPhone 15 : SoCA16 Bionic
▷ Samsung Galaxy S11: SoCExynos 2400
▷ Nintendo Switch: Nvidia Tegra X1
▷ Sony PS5 : SoC d'AMD
Les fabricants de SoCs sont très nombreux :
▷ AMD
▷ Apple
▷ Broadcom
▷ Intel
▷ Nvidia
▷ Qualcomm
▷ Samsung
▷ Texas Instrument
Même s'il n'y a que deux architectures différentes : x86 et ARM.
T. Rahobisoa 7/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
8 Exercices
Exercice 1 :En résumé
Résumer en quelques phrases le contenu de cette vidéoSystems on a Chip as Fast As Possible(jusqu'à 5'40”).
Mettre les sous-titres automatiques en français si besoin.
Exercice 2 :
1. Qu'est-ce qu'unSoC ?
2. Quels sont les appareils à base deSoC ?
3. Au niveau matériel (hardware), qu'est-ce qui différencie fondamentalement unSoC des composants d'un
ordinateur?
Exercice 3 :
1. Pourquoi les CPU d'unSoC embarquent-ils plusieurs cœurs?
2. Donner un ordre de grandeur de la fréquence du CPU d'unSoC.
3. Sur quel paramètre influe la fréquence du CPU d'unSoC ?
4. Qu'est-ce qu'un thread?
5. Qu'est-ce que la mémoire cache d'un CPU?
6. Dans unSoC, à quoi sert le GPU?
7. Dans unSoC, quel élément est chargé du traitement des photos prises par la (les) caméra(s) intégrée(s)
au smartphone?
8. Dans unSoC, quel élément permet de lire de l'audio ou de la vidéo?
9. Dans unSoC, à quoi sert le SPU?
10. Quel élément d'unSoC permet à un smartphone de communiquer avec d'autres machines?
Exercice 4 :
1. Quels sont les principaux avantages d'un SoC?
2. Citer le principal inconvénient d'un SoC.
Exercice 5 :Recherches Internet
1. En vous inspirant du tableau de la page 5, créer un tableau similaire avec 5 smartphones actuels (le vôtre
et ceux de quelques camarades).
2. Pour les modèles les plus récents (2025) de téléphones portables, quelle est la finesse de gravures desSoC ?
3. En 2025, quel est l'ordre de grandeur de la surface d'unSoC ?
4. En 2025, , quel est l'ordre de grandeur du nombre de transistors présents sur unSoC ?
5. En 2025, quel est l'ordre de grandeur de la densité moyenne de transistors par mm2 dans unSoC ?
6. Quelle sera la finesse de gravure desSoC pour la prochaine génération de smartphones?
7. Quelle est la principale difficulté technologique rencontrée à l'heure actuelle par les concepteurs deSoC ?
T. Rahobisoa 8/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
Exercice 6 :Compléter le schéma duSoC ci-dessous :
Exercice 7 :A partir de l'article du site elektormagazine.fr :
1. Relever les differentes caractéristiques duSoC du Raspberry Pi 3modèle B+.
2. Les comparer auSoC du Raspberry Pi 4.
3. Quelles sont les principales évolutions qui contribuent à ce gain? Une copie de l'article est disponible ici.
Exercice 8 :La photo ci-dessous montre le détail d'unSoC Kirin 990.
Identifier les différentes parties de ceSoC.
T. Rahobisoa 9/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
Exercice 9 :Parmi les images ci-dessus, la(les)quelle(s) représente(nt) unSoC.
Exercice 10 :Sujet de Bac
Répondre aux 3 questions de la partie 1 de l'exercice 2 du sujet de Bac 2022, Nouvelle-Calédonie, J1.
T. Rahobisoa 10/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
Exercice 11 :Exposés
Parmi la liste, ci-dessous choisir un thème :
1. Les SoC et l'intelligence artificielle embarquée :Michel
— Comment les SoC modernes intègrent des unités de traitement dédiées à l'IA (NPU ou TPU).
— Applications récentes : reconnaissance faciale, traitement du langage naturel, voitures autonomes,
etc.
2. Les SoC dans la 5G et l'Internet des Objets (IoT) : l'ère des connexions intelligentes: Ange
— Impact des SoC dans le déploiement de la 5G : gestion des réseaux, smartphones 5G, IoT connecté.
— Rôle des SoC dans l'optimisation des performances des appareils IoT intelligents.
3. Les SoC et la gestion de la confidentialité avec l'IA: Léane
— Rôle des SoC dans la sécurisation des données personnelles (exemple : cryptage des informations dans
des SoC pour smartphones).
— Comment les SoC sont utilisés pour répondre aux défis de confidentialité dans les systèmes d'IA (par
exemple : confidentialité des données traitées par IA sur les appareils).
4. Les SoC dédiés à la vision par ordinateur et l'IA : applications en temps réel: Matteo
— Les SoC intégrant des capacités de vision par ordinateur et leur utilisation dans des technologies
récentes (comme les caméras intelligentes, la réalité augmentée, etc.).
— L'impact sur des secteurs comme la santé, l'automobile ou la sécurité (exemple : Tesla et la vision
par ordinateur pour les véhicules autonomes).
5. Les SoC et l'optimisation de l'IA dans les smartphones :Ian
— Étude des SoC récents intégrant des capacités d'IA dans les smartphones (par exemple, les séries
Apple A14/A15, Qualcomm Snapdragon).
— Comment ces SoC optimisent l'IA pour des applications pratiques (reconnaissance vocale, photogra-
phie intelligente, etc.).
6. Le rôle des SoC dans les assistants vocaux intelligents
— Analyse des SoC intégrés dans des dispositifs comme Amazon Echo, Google Home, et autres assistants
vocaux.
— L'IA embarquée et son rôle dans l'amélioration des interactions vocales et des commandes contex-
tuelles.
7. L'impact des SoC dans le développement de l'IA générative (ex. ChatGPT)Lino
— Comment les SoC peuvent être utilisés pour accélérer les calculs nécessaires aux modèles d'IA géné-
rative tels que ChatGPT, DALL·E, etc.
— Défis techniques et innovations récentes pour les calculs massifs (exemple : SoC spécialisés pour
l'entraînement des modèles d'IA).
8. L'évolution des SoC pour les applications de réalité augmentée (AR) et réalité virtuelle
(VR) : Guillaume
— Le rôle crucial des SoC dans les technologies AR/VR récentes : latence, puissance de traitement,
gestion graphique.
— Applications pratiques dans les jeux vidéo, les industries créatives, la formation, etc.
T. Rahobisoa 11/12 AMSER05 - SoC
Terminale - Spécialité NSI IFS Singapour
9. Les SoC dans les véhicules autonomes : intégration de l'IA et des capteurs
— Comment les SoC sont utilisés pour traiter les données en temps réel provenant des capteurs dans
les véhicules autonomes.
— Impact de l'IA dans le traitement des données pour prendre des décisions en temps réel.
10. Les SoC et la transition énergétique : vers des systèmes plus efficaces
— Rôle des SoC dans l'optimisation de la consommation d'énergie dans les dispositifs IoT et les smart-
phones.
— Comment les SoC peuvent contribuer à des solutions plus écologiques dans l'IA embarquée.
Vous devrez réaliser une présentation que vous déposerez surClassroom pour la semaine prochaine.
Ce travail de recherche sera présenté à l'oral (10 minutes à l'oralpar personne).
T. Rahobisoa 12/12 AMSER05 - SoC

## Securisation

### Securisation

Terminale - Spécialité NSI IFS Singapour
Chapitre 19 - Sécurisation des communications
Objectifs :
▷ Décrire les principes de chiffrement symétrique et asymétrique (avec clef privée/clef publique).
▷ Décrire l'échange d'une clef symétrique en utilisant un protocole asymétrique pour sécuriser une commu-
nication HTTPS.
1 Introduction
Pour qu'un message entre deux machines dans un réseau informatique ne puisse pas être compréhensible s'il est
intercepté, il faut qu'il soitchiffré.
A retenir!
Il y a deux manières principales pourchiffrer un message:
▷ par unchiffrement symétriquequi utilise une clé unique, connue seulement de l'émetteur et du
récepteur. L'émetteur chiffre le message avec la clé et le récepteur le déchiffre avec la même clé.
▷ par unchiffrement asymétriquequi utilise un couple de clés, l'une publique connue de tout le
monde, l'autre privée connue uniquement par le récepteur. L'émetteur chiffre le message avec la
clé publique. Le récepteur le déchiffre avec la clé privée.
Ces deux méthodes de chiffrement sont utilisées lorsqu'un navigateur demande une page web avec leprotocole
HTTPS.
Les caractéristiques que l'on cherche à protéger :
— La confidentialité : les données échangées ne peuvent être connues que de l'expéditeur (Anne) et du
destinataire (Bob). Pour ce faire, Alice va chiffrer le message et Bob devra le déchiffrer avant de le lire.
Toute personne qui ne possède pas le moyen de déchiffrer ce message chiffré se verra dans l'impossibilité
de comprendre le contenu du message.
— L'authentification : les interlocuteurs sont réellement qui ils prétendent être. Uncertificat numérique
est alors nécessaire, car il permet d'utiliser une signature numérique comme moyen d'authentifier des
informations numériques.
— L'intégrité : toute modification (involontaire ou malveillante) est détectée. Dans ce cas, il faut calculer
la somme de contrôle (checksum, en anglais) ou « empreinte » du message et la comparer avec celle du
message original.
T. Rahobisoa 1/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
2 Le chiffrement symétrique
L'idée de chiffrer des messages (de les rendre illisibles pour des personnes non autorisées) ne date pas du début
de l'ère de l'informatique. En effet, dès l'Antiquité, on cherchait déjà à sécuriser les communications en chiffrant
les messages sensibles. On a des traces de son utilisation par les Égyptiens vers2000 av. J.-C.
Nous nous intéresserons ici uniquement aux communications ayant lieu par l'intermédiaire d'un réseau informa-
tique.
Dans un chiffrement symétrique, la clé utilisée par l'expéditeur pour chiffrer le message est la même que celle
utilisée par le récepteur pour déchiffrer le message.
2.1 Le chiffrement de César
Principe :on décale les lettres den rangs. La clé est tout simplement ledécalage.
En ne considérant que les lettres en majuscule et non accentuées, notre alphabet se réduit à 26 lettres :
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
Par exemple, avec un décalage de 13 : (A → N) et (N → A).
On utilise bien la même clé pour chiffrer et déchiffrer, il s'agit donc d'unchiffrement symétrique.
Par exemple, le message'BONJOUR, COMMENT ALLEZ-VOUS' se code par :'OBAWBHE, PBZZRAG NYYRM-IBHF'
Le déchiffrement nous redonne bien le message d'origine.
T. Rahobisoa 2/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
Inconvénient :
Cetteméthodeestintéressantepourvérifierl' intégritéetpourlesperformancesmaiscelapermetàunattaquant
de deviner plus facilement la clé.
L'attaque la plus évidente de ce code est d'utiliser laméthode des fréquencesdes caractères.
Par exemple, sur un texte en français suffisamment long, la lettre la plus fréquente (qui revient le plus souvent)
du chiffrement correspondra à la lettreE. On peut donc retrouver facilement le décalage (la clé).
2.2 Le chiffrement par substitution
Principe :On remplace une lettre par une autre de l'alphabet.
On a donc26! ≈ 4 × 1026 clés possibles.
Exemple
Avec la clé suivante :
ABCDEFGHIJKLMNOPQRSTUVWXYZ
AZERTYUIOPQSDFGHJKLMWXCVBN
le messageSUBSTITUTION devient LWZLMOMWMOGF
2.3 Le chiffrement de Vigenère (XVIème siècle)
Cette méthode a été mise au point durant laRenaissance pour contrer la cryptanalyse par la méthode des
fréquences de lettres qui permettait de “casser” les clés de cryptage assez facilement.
On choisit une clé sous la forme d'un mot ou d'une phrase qui donne le décalage à appliquer qui devient alors
variable.
Supposons que la clé soitABC, les décalages successifs seront0, 1, 2, 0, 1, 2, 0, ..., etc.
Exemple
Avec la cléABC :
Le messageSUBSTITUTION devient SVDSUKTVVIPP car :
SUBSTITUTION
ABCABCABCABC
–––––––––––-
SVDSUKTVVIPP
T. Rahobisoa 3/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
2.4 Le code ASCII
Nous pouvons utiliser le code ASCII de chaque caractère et coder notre message en binaire (par exemple, on
peut vérifier que leH correspond bien à l'octet01001000).
Pour effectuer la "conversion" texte vers un code binaire ASCII ou vice-versa, on peut utiliser le site :
https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html
Par exemple le messageHello World! se code par :
010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001
2.5 Le chiffrement de Vernam
Il s'agit d'un système parfaitement sûr, le mathématicienC.Shannon a montré que si on respecte bien les trois
règles deVernam, ce système est inviolable.
▷ La clé doit être une suite de caractères au moins aussi longue que le message à chiffrer.
▷ Les caractères composant la clé doivent être choisis de façon totalement aléatoire.
▷ Chaque clé, ou masque, ne doit être utilisée qu'une seule fois (d'où le nom demasque jetable).
Une méthode particulièrement efficace pour traiter le chiffrement et le déchiffrement de messages à partir de la
clé est d'utiliser la fonction logiqueXOR, c'est-à-dire l'opération logiqueOU EXCLUSIFvue en classe de 1ère.
T. Rahobisoa 4/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
Pour rappel, vous trouverez la table de vérité duXOR ci-dessous :
A B S
0 0 0
0 1 1
1 0 1
1 1 0
L'une des propriétés les plus intéressantes de cette opération est qu'elle estsymétrique et réversible :
(A ⊕B) ⊕B =A
XOR se note ⊕.
Exemple
On noteM le message etS la clé secrète.
On obtient le message chiffréC en faisant :C =M ⊕S
Le déchiffrement se fait tout simplement en appliquant la même opérationC ⊕S =M
Malgré sa simplicité, ce système de chiffrement (inventé en 1917 parGilbert Vernam) est très sûr. Il a été utilisé
pour le téléphone rouge reliant directement le Kremlin à la Maison-Blanche, les clés transitant alors par
valises diplomatiques.
Le système de masque jetable était également employé par les espions soviétiques. Certains masques furent
utilisés plus d'une fois (parfois avec des années d'intervalle) ce qui permit aux services de renseignements
anglais de déchiffrer certains messages.
2.6 En résumé
Le gros problème avec le chiffrement symétrique, c'est qu'il est indispensable pour A et B de se mettre d'accord
à l'avance sur la clé qui sera utilisée lors des échanges et que cette clé reste secrète. Le chiffrement asymétrique
permet d'éviter ce problème.
Vidéo présentant un résumé de quelques une des méthodes de chiffrements symétriques.
Faire les exercices 1 à 7.
T. Rahobisoa 5/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
3 Le chiffrement asymétrique
3.1 Principe du chiffrement asymétrique
L'inconvénient essentiel du chiffrement symétrique est le nécessairepartage d'un secret (la clé) avant
l'établissement de la communication sécurisée.
La cryptographie asymétrique permet de résoudre le problème de l'échange de laclé secrète. Elle fut inventée
par des chercheurs de l'université deStanford, Whitfield Diffieet Martin Hellman en 1976, qui reçurent leprix
Turing 2015 pour cette découverte.
Le principe de base est l'existence d'uneclé publique, appelée à être distribuée largement, et d'uneclé privée,
qui ne quitte jamais son propriétaire.
L'illustration précédente associe :
— une image decadenas à laclé publique(car on s'en sert pour chiffrer les messages)
— une image declé à laclé privée(car on s'en sert pour déchiffrer les messages)
T. Rahobisoa 6/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
3.2 Le rôle interchangeable des clés publiques et privées
Concrètement, la clé privée et la clé publique sont deux nombres aux rôles identiques.
Appelons-les A et B :
— il est impossible de trouver A en fonction de B. Réciproquement, si on connaît A, il est impossible d'en
déduire B.
— si on chiffre un message avec A, on peut le déchiffrer avec B. Réciproquement, si on chiffre avec B, on
peut déchiffrer le message grâce à A.
— on peut donc chiffrer avec une clé publique et déchiffrer avec la clé privée associée (ce qui est fait dans
l'exemple précédent). Mais on peut aussi chiffrer avec la clé privée, et déchiffrer avec la clé publique
associée.
A et B ont donc des rôles interchangeables (chacun peut être un cadenas, chacun peut être une clé), et ce n'est
qu'en connaissant A et B qu'on peut déchiffrer le message.
Pour que cela fonctionne, il faut que la paire clé publique/clé privée ait une propriété particulière.
Soit FP la fonction de chiffrement utilisée avec la clé publique, etFS la fonction relative à la clé privée. Une
relation particulière relie ces deux fonctions :
m =FS(FP (m))
Enfin pour que ce système fonctionne, il faut que :
— la fonctionFP soit facile à calculer pour tout le monde,
— la fonctionFS soit facile à calculer uniquement pour le détenteur de la clé privée.
Les algorithmes de chiffrement asymétriques reposent sur des problèmes faciles à résoudre dans un sens et très
difficiles à résoudre dans l'autre sens.
Un système qui satisfait ces deux critères est le système dechiffrement RSAutilisé pour échanger des données
confidentielles sur Internet.
3.3 Le système RSA
Cet algorithme fut inventé en 1977 parRonald Rivest, Adi Shamir et Leonard Adleman breveté par le MIT en
1983. Le brevet a expiré le 21 septembre 2000 ce qui permet de l'utiliser librement depuis.
Le système de chiffrement asymétrique RSA est le plus couramment utilisé aujourd'hui, notamment pour tout
ce qui concerne lecommerce électronique.
Il consiste en la création, pour chacun des deux participants, de deux clés (publique et privée), liées entre elles de
telle sorte que le chiffrement d'un message par la clé publique, puis par la clé privé redonne le message original,
et que l'opération inverse est vraie aussi.
RSA se base sur la factorisation des très grands nombres premiers.
Vidéo sur le principe de l'arithmétique modulaire dans le protocole RSA.
T. Rahobisoa 7/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
3.3.1 Les étapes de l'algorithme RSA
1. Génération des clés :
— Choisissez deux nombres premiers distincts très grands,p et q.
— Calculez leur produit,n =p ×q. Ceci est appelé lemodule de chiffrement.
— Calculez la fonction d'Euler de n :ϕ(n) = (p − 1) × (q − 1).
— Choisissez un exposant de chiffremente tel que 1<e<ϕ (n) et que e soit premier avecϕ(n)(c'est-à-dire
qu'ils n'ont pas de facteur premier commun autre que 1).
— Calculez l'exposant de déchiffrement, d, tel que(d×e) %ϕ(n) == 1. C'est-à-dire,d est l'inverse modulaire
de e modulo ϕ(n).
2. Chiffrement :
— Convertissez le message en un entier représentatif.
— Chiffrez le message en utilisant la formule :c = (message)e % n.
3. Déchiffrement :
Utilisez la clé privée(d, n)pour déchiffrer le message chiffré en utilisant la formule :message = (cd) % n.
Ces étapes vous permettent de chiffrer un message avec la clé publique et de le déchiffrer avec la clé privée
correspondante. C'est le principe fondamental de l'algorithme RSA.
3.3.2 Exemple de chiffrement avec RSA
Supposons que vous souhaitez utiliser l'algorithme RSA pour chiffrer un message "HELLO".
Génération des clés :
— Choisissez deux nombres premiers :p = 7 et q = 11.
— Calculez le module de chiffrement :n =p ×q = 7 × 11 = 77.
— Calculez la fonctionϕ(n) : ϕ(77) = (p − 1) × (q − 1) = (7 − 1) × (11 − 1) = 6 × 10 = 60.
— Choisissez un exposant de chiffrement :e = 13.
— Trouvez l'exposant de déchiffrementd tel que (d ∗e) % ϕ(n) == 1.
En utilisant l'algorithme d'Euclide étendu, trouvez qued = 37.
Chiffrement :
— Convertissez le message "HELLO" en nombres, par exemple, en utilisant la tableASCII : H = 72, E =
69, L = 76, L = 76, O = 79.
— Chiffrez chaque nombre en utilisant la formulec = (messagee) % n :
— Pour H : c = (72 13) % 77 = 344373768865426431 % 77 = 48.
— Pour E : c = (69 13) % 77 = 680369848560 % 77 = 47.
— Pour L : c = (76 13) % 77 = 2131167792897337916176 % 77 = 59.
— Pour L :c = (76 13) % 77 = 2131167792897337916176 % 77 = 59.
— Pour O :c = (79 13) % 77 = 575398451422268922025 % 77 = 47.
— Le message chiffré est donc :48 47 59 59 47.
Déchiffrement :
Pour déchiffrer chaque nombre chiffré, utilisez la formule :message = (cd) % n.
— Pour 48 :message = (48 37) % 77 = 72 (H).
— Pour 47 :message = (47 37) % 77 = 69 (E).
— Pour 59 :message = (59 37) % 77 = 76 (L).
— Pour 59 :message = (59 37) % 77 = 76 (L).
— Pour 47 :message = (47 37) % 77 = 79 (O).
Le message original "HELLO" a été chiffré en "48 47 59 59 47" et déchiffré avec succès en "HELLO" en utilisant
l'alogorithme de chiffrement RSA.
T. Rahobisoa 8/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
3.3.3 RSA, un système inviolable?
Le problème du chiffrement asymétrique est que sesperformances (mémoire, vitesse) sont nettement
inférieuresauchiffrementsymétrique.LechiffrementRSAadesdéfauts(notammentunegrandeconsommation
des ressources, due à la manipulation de très grands nombres).
Mais le choix d'une clé publique de grande taille (actuellement 1024 ou 2048 bits) le rend pour l'instantinvio-
lable.
Actuellement, il n'existe pas d'algorithme efficace pour factoriser un nombre ayant plusieurs centaines de chiffres.
Deux évènements pourraient faire s'écrouler la sécurité du RSA :
— la découverte d'unalgorithme efficace de factorisation, capable de tourner sur les ordinateurs ac-
tuels. Cette annonce est régulièrement faite, et tout aussi régulièrement contredite par la communauté
scientifique. (cf.https://www.schneier.com/blog/archives/2021/03/no-rsa-is-not-broken.html)
— l'avènement d'ordinateurs quantiques, dont la vitesse d'exécution permettrait une factorisation ra-
pide. Il est à noter que l'algorithme de factorisation destiné à tourner sur un ordinateur quantique existe
déjà : l'algorithme de Schor.
4 Le protocole HTTPS
Nous allons maintenant voir une utilisation concrète de ces chiffrements symétriques et asymétriques : le pro-
tocole HTTPS.
Avant de parler du protocole HTTPS, petit retour sur le protocole HTTP : un client effectue une requête HTTP
vers un serveur, le serveur va alors répondre à cette requête (par exemple en envoyant une page HTML au
client).
Le protocole HTTPpose 2 problèmes en termes de sécurité informatique :
1. Un individu qui intercepterait les données transitant entre le client et le serveur pourrait les lire sans
aucun problème (ce qui serait problématique notamment avec un site de e-commerce au moment où le
client envoie des données bancaires)
2. Grâce à une technique qui ne sera pas détaillée ici (leDNS spoofing), un serveur "pirate" peut se faire
passer pour un site sur lequel vous avez l'habitude de vous rendre en toute confiance. Comme illustré sur le
schéma ci-dessous, un pirate pourrait récupérer vos identifiants bancaires en créant un faux site identique
au site de votre banque.
HTTPS est donc la version sécurisée de HTTP, il s'appuie sur le protocole TLS (Transport Layer
Security) anciennement connu sous le nom de SSL (Secure Sockets Layer).
Il permet d'éviter les 2 problèmes évoqués en garantissant laconfidentialité et l'authentification.
T. Rahobisoa 9/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
4.1 La confidentialité dans HTTPS
HTTPS fournit une couche de chiffrement des données circulant entre le
client et le serveur.
Les communications vont être chiffrées grâce à une clé symétrique (pour
des raisons de débit).
Problème :comment échanger cette clé entre le client et le serveur?
En utilisant une paire clé publique / clé privée!
Voici le déroulement des opérations :
1 et 2.Le client effectue une requête HTTPS vers le serveur, en retour
le serveur envoie sa clé publique (KpuS) au client.
3. Le client "fabrique" une clé K (qui sera utilisé pour chiffrer les futurs
échanges), chiffre cette clé K avec KpuS et envoie la version chiffrée de
la clé K au serveur.
4 et 5.Le serveur reçoit la version chiffrée de la clé K et la déchiffre en
utilisant sa clé privée (KprS). À partir de ce moment-là, le client et le
serveur sont en possession de la clé K.
6. Le client et le serveur commencent à échanger des données en les
chiffrant et en les déchiffrant à l'aide de la clé K (chiffrement symétrique).
Ce processus se répète à chaque fois qu'un nouveau client effectue une
requête HTTPS vers le serveur.
4.2 L'authentification dans HTTPS
L'autre aspect de la sécurité du protocole HTTPS est de s'assurer que le serveur justifie de son "identité".
Le problème vient de la transmission de la clé publique : si celle-ci n'est pas sécurisée, un attaquant peut se
positionner entre l'entreprise et son audience en diffusant de fausses clés publiques (par le biais d'un faux site
web par exemple) puis intercepter toutes les communications, lui permettant de se faire passer pour l'entreprise.
Les certificats résolvent ce problème grâce à la signature
d'une autorité de confiance.
Un certificat électronique est un fichier contenant :
— la clé publique de l'entreprise;
— des informations d'identification, par exemple : nom, lo-
calisation, adresse électronique de l'entreprise;
— une signature sécurisée d'une autorité de confiance
garantissant l'exactitude des informations du certificat.
Le serveur enverra donc lecertificat authentifiépar l'auto-
rité.
En cas d'absence de certificat (ou d'envoi de certificat non conforme), le client stoppe immédiatement les
échanges avec le serveur. Ce mécanisme rend toute attaque du typeDNS Spoofingimpossible sur HTTPS.
Vidéo sur le chiffrement SSL/TLS :https://youtu.be/7W7WPMX7arI?si=zvsZdg0D7_P5N-Ji
T. Rahobisoa 10/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
5 Exercices
Exercice 1 :Chiffrement de Vernam
On souhaite transmettre le message NSI de façon privée. Le code ASCII correspondant au message M est
01001110 01010011 01001001. On crée une clés secrèteS aléatoirement que l'on transmet au destinataire :
11001001 11001101 01100011.
1. Ecrire le message chiffréC en faisant :C =M ⊕S
2. Vérifier qu'on déchiffre par la même opération :C ⊕S =M
Exercice 2 :Module string
Pour réaliser les exercices ci-dessous, on aura besoin d'utiliser le modulestring de Python.
1. Dans un fichier Python, copier le code ci-dessous :
1 from string import ascii_uppercase as alphabet
2
3 print(alphabet)
4 alphabet[0], alphabet[25]
5
6 alphabet.index("A")
7 alphabet.index("Z")
8
9 "Message".upper()
2. Que produisent les lignes 3 et 4?
3. Que produisent les lignes 6 et 7?
4. Que permet de faire la ligne 9?
5. Trouver la commande qui permet de mettre n'importe quel texte en minuscules.
Exercice 3 :Chiffrement de César
Créer deux fonctionschiff_cesar et dechiff_cesar pour réaliser respectivement le chiffrement et déchiffre-
ment avec en argument le message et la clé.
Ces deux fonctions ont deux paramètres :
— message : une chaîne de caractères à (dé)coder.
— n : un entier qui donne le décalage.
Par exemple, la fonctionchiff_cesar doit convertir le message en majuscule, et décaler toutes les lettres den
grâce au codage César, et laisser tous les autres caractères inchangés (ponctuation).
Voici une série de tests à passer.
1 assert cesar('message', 0) == "MESSAGE"
2 assert cesar('message', 1) == 'NFTTBHF'
3 assert cesar('message', -1) == 'LDRRZFD'
4 assert cesar('message', 26) == 'MESSAGE'
5 assert cesar('message', 53) == 'NFTTBHF'
6 assert cesar('message', -27) == 'LDRRZFD'
7
8 eluard = "Sur mes cahiers d ecolier, sur mon pupitre et les arbres, sur le
sable, sur la neige, j ecris ton nom"
9
10 assert cesar(eluard, 13) == 'FHE ZRF PNUVREF Q EPBYVRE, FHE ZBA CHCVGER RG
YRF NEOERF, FHE YR FNOYR, FHE YN ARVTR, WEPEVF GBA ABZ'
11
T. Rahobisoa 11/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
12 # verification du decodage
13 assert cesar(cesar(eluard,13),-13) == eluard.upper()
Exercice 4 :Chiffrement par substitution
Implémenter le chiffrement par substitution avec une fonctionsubstitution qui prend deux paramètres :
— message : une chaîne de caractères à coder ou décoder.
— clé : une chaîne de caractères qui donne les correspondances des caractères.
On pourra vérifier son fonctionnement sur l'exemple du cours :
1 assert substitution("SUBSTITUTION", "AZERTYUIOPQSDFGHJKLMWXCVBN") ==
"LWZLMOMWMOGF"
Comment devra être effectué le décodage à partir du message codé et de la clé?
Exercice 5 :OU Exclusif
XOR est une opération de logique bit à bit qui renvoie 0 si les deux bits sont égaux et 1 sinon.
Une particularité de cette opération est :
Si (b1 xor b2 == b3) alors (b1 xor b3 == b2) et (b2 xor b3 == b1)
Ce qui permet un chiffrement symétrique.
Par exemple, le motbonjour dont le codeASCII est donné par ce programme :
m = "bonjour"
for c in m:
print(ord(c),end=' ')
On obtient :98 111 110 106 111 117 114
Le mot 'nsi' va nous servir de clé : ('nsi' → 110 115 105)
La méthode consiste alors à aligner le mot et la clé en la répétant autant de fois que nécessaire et d'effectuer
un XOR entre les codesASCII :
b o n j o u r
98 111 110 106 111 117 114
n s i n s i n
110 115 105 110 115 105 110
En pratiquant unXOR lettre par lettre entre les nombres obtenus (après une écriture en binaire...), on obtient
les codesASCII suivant :12 28 7 4 28 28 28 (que l'on pourrait transformer en caractères mais ce n'est pas
très utile...)
Pour décoder le message, il suffit alors de recommencer l'opération avec les codesASCII du message chiffré en
utilisant la même clé : (12 xor 110 = 98 donc 'b') etc.
En Python, l'opérateurˆ permet d'effectuer unXOR directement sur deux entiers.
T. Rahobisoa 12/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
Le programme suivant chiffre un message en utilisant cette méthode :
message = "Bonjour, vive la NSI!"
cle = "mystere"
def chiffre(message,key):
c = []
n = len(message)
lk = len(key)
j = 0
for i in range(n):
c.append(ord(message[i]) ^ ord(key[j]))
j = (j+1)%lk
return c
print(chiffre(message,cle))
Ce qui donne en console :
>>>
[47,22,29,30,135,7,23,65,89,16,27,133,31,0,3,13,83,21,132,30,0,23,84,5,27,
157,1,69,82]
Chaque nombre peut être converti en caractère (le contenu complet du message est chiffré, y compris les
caractères de ponctuation et d'espace).
Chaque nombre peut être converti en caractère (le contenu complet du message est chiffré, y compris les
caractères de ponctuation et d'espace).
1. Modifier la fonctionchiffre pour qu'elle renvoie le message chiffré (avec les caractères).
2. Écrire une fonctiondechiffre qui prend en paramètres le message chiffré et la clé et qui renvoie le
message déchiffré.
3. Valider les tests unitaires suivants :
assert dechiffre(chiffre("Hello World!","key1"),"key1") == "Hello World!"
assert dechiffre(chiffre("Hello World!","key1"),"key2") != "Hello World!"
4. Vérifier que les méthodes soient documentées (docstring).
Exercice 6 :Module sympy
1. Consulter la documentation de librairiesympy.
2. Décoder la phraseRYTVJKGCLJWRTZCVRMVTLEDFULCVHLZWRZKKFLKRMFKIVGCRTV, sachant qu'elle a été chif-
frée par décalage (shift en anglais...)
Exercice 7 :Chiffrage affine
Principe du chiffrage affine :
— Chaque lettre est codée par son rang, en commençant à 0 (A : 0, B : 1, ...,Z : 25)
— On applique à chaque rang la transformation affine :f (x) = (ax +b) % 26
où a et b sont deux nombres entiers. Attention,a doit être premier avec 26!
1. Implémenter la fonctionaffine(msg,a,b)
2. Comparer vos résultats avec ceux obtenus par la fonctionencipher_affine() de sympy.
3. Décodez la phraseUCGXLODCMOXPMFMSRJCFQOGTCRSUSXC, sachant qu'elle contient le motTRAVAIL et que
et a et b sont inférieurs à 20.
Aide : L'instructiongcd du modulemath permet de calculer le PGCD de deux nombres.
T. Rahobisoa 13/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
Exercice 8 :Chiffrement RSA
Alice veut écrire à Bob.
Soit le couple de nombre premiers(p,q ) avecp = 15 et q = 13.
1. Calculer n et ϕ(n).
2. Justifier que (9, 65) ne peut pas être une clé publique.
3. Vérifier que (11, 65) est une clé publique. C'est la clé publique de Bob.
4. Vérifier que 35 est un inverse de 11 modulo 48.
5. En déduire la clé privée de Bob.
6. Chiffrer le nombre secret d'Alice 17 avec la clé publique de Bob. C'est ce nombre qu'Alice envoie à Bob.
7. Déchiffrer le nombre reçu par Bob.
Exercice 9 :Le chiffrement asymétrique
Le schéma ci-dessous rappelle le principe du chiffrement asymétrique :
Nous allons illustrer ce principe en utilisant le modulersa.py fourni.
Ce module contient la classersa dont nous utiliserons 3 méthodes :
— rsa_get_public_key()
— rsa_encode_text()
— rsa_decode_text()
1. Ouvrir le fichierrsa.py et lire la description (Docstring) de ces méthodes.
2. Écrire un programme qui réalise les opérations suivantes :
— Anne partage sa clef publique.
— Anne reçoit le message “test” de Bob
— Anne envoie le message en clair "Hello World!".
— Bob et Dylan lisent le message d'Anne.
— Bob envoie le message "OK" chiffréuniquement pour Anneet l'envoie à Anne et Dylan.
— Anne et Dylan lisent le message de Bob.
Résultat attendu :
— Anne reçoit :test
— Bob reçoit :Hello World!
— Dylan reçoit :Hello World!
— Dylan reçoit : ... (ce message sera différent à chaque test)
— Anne reçoit :OK
3. Tester l'échange de messages chiffrés entre Dylan et Bob.
T. Rahobisoa 14/15 AMSER06 - Sécurisation
Terminale - Spécialité NSI IFS Singapour
Exercice 10 :Certificats
1. À l'aide deChrome, accéder au site de l'IFS :https://www.ifs.edu.sg
2. Afficher son certificat en cliquant sur ... puis surConnection is secureet enfin surCertificate is valid.
3. Dans Details, rechercher et noter les informations suivantes :
— la date de validité
— l'autorité de certification
— les informations sur le site
— l'algorithme de chiffrement de la communication
— la clé publique
Exercice 11 :Chiffrons une image
Le code suivant permet de créer et afficher une image de dimension 240 x 180 en niveaux de gris (valeurs entre
0 et 255); cette image est composée de bandes blanches (valeur 255) et noires (valeur 0) verticales.
from PIL import Image
import numpy as np
def matrice(n,p):
#Initialise m comme une matrice de 0 de taille n x p
m=[[0 for j in range(p)] for i in range(n)]
for i in range(n):
#n est la hauteur de l'image
for j in range(p):
#p est la largeur de l'image
#valeurs differentes dans chaque bande de 20 pixels
if (j // 20) % 2 == 0:
m[i][j]=255
else:
m[i][j]=0
return np.array(m)
img=matrice(240,180)
print("Image originale")
Image.fromarray(img).show()
1. Créer une fonction generer_cle(n,p) qui génère une matrice de taille 240 x 180 remplie de valeurs
aléatoires (vous pouvez utiliser la fonctionrandint(0,255)). Afficher cette clé.
2. Créer une fonctionchiffre qui prend en argument l'image originale et la clé, et fait unOU EXCLUSIF
entre chaque élément (pixel) de l'image et de la clé. Afficher l'image chiffrée.
3. On souhaite maintenant déchiffrer l'image, que suggérez-vous?
4. Réaliser le déchiffrement et afficher l'image finale pour vérifier qu'elle est identique à l'image originale.
Exercice 12 :Compétences PIX
Connectez-vous à votre compte Pix et complétez la campagne ci-dessous traitant de cybersécurité :
https://app.pix.fr/campagnes/PHPGME255
T. Rahobisoa 15/15 AMSER06 - Sécurisation
