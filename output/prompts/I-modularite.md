# Plan I-modularite (inedit)

Notion : modularite (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Modularite > Modularite]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 10 - Modularité
> Objectifs :
> ▷ Savoir utiliser des bibliothèques
> ▷ Exploiter leur documentation
> ▷ Créer des modules simples et les documenter.
> 1 Introduction
> Laprogrammation modulaireconsiste à décomposer une grosse application en modules que l'on peut ensuite
> améliorer et utiliser indépendamment dans d'autres applications.
> Cette méthode réalise uneencapsulation comparable à celle de la programmation orientée objet.
> Un module doit être conçu pour pouvoir être utilisé par d'autres utilisateurs comme une interface qui fournit
> des données (math.pi, math.e...), des objets (structures de données comme les piles, les arbres, les graphes,
> ..., etc.) et des traitements (fonctions, méthodes), sans rentrer dans le code du module.
> Il faut donc prévoir unedocumentation claire et complète.
> 2 Exemples
> Nous avons déjà créé des modules en implémentant des
> [Programmation > Pratiques de programmation > 2.2 Le cas particulier des ```docstrings```]
> #### 2.2.1 Que sont les ```docstrings```?
> 
> Les ```docstrings``` sont des commentaires *normalisés* pour les fonctions, qui peuvent être consultés en console.
> 
> **Exemples :**
> 
> Nous connaissons la fonction ```len()``` qui permet par exemple de connaître la longueur d'une liste passée en paramètre.
> 
> Si nous tapons en console la commande ```print(len.__doc__)```, nous aurons la description de cette fonction. 
> 
> ```python
> >>> len.__doc__
> 'Return the number of items in a container.'
> ```
> Il est aussi possible d'accéder à la docstring d'une fonction ```f```  par la commande ```help(f)``` :
> 
> ```python
> >>> help(len)
> Help on built-in function len in module builtins:
> 
> len(obj, /)
>     Return the number of items in a container.
> 
> ```
> 
> De même pour la fonction ```range``` :
> ```python
> >>> print(range.__doc__)
> range(stop) -> range object
> range(start, stop[, step]) -> range object
> 
> Return an object that pro

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « 3. Parmi les adresses IP ci-dessous, quelle est la seule possible pour un autre appareil connecté au même réseau ? ◦ 192.168.0.14 ◦ 192.168.0.1 ◦ 192.168.1.1 ◦ 192.168.1.255 »
    exemple réel (autre notion) : « b. De quelle table l'attribut identifiant est-il une clé étrangère ? »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 4. Il existe des algorithmes pour modifier la structure d'un ABR , afin par exemple de diminuer la hauteur d'un ABR ; on s'intéresse aux algorithmes appelés rotation, consistant à faire "pivoter" une partie de l'arbre autour d'un de ses nœuds.  L'exemple ci-de »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C6 : Établir ou lire une table de routage — Majoritairement réseau : dresser, compléter ou exploiter une table de routage selon un protocole (RIP/OSPF), ou identifier un chemin ; on évalue l'application d'un protocole à une topologie.
    gabarit : Donner la [table/chemin] [de l'élément] selon [protocole/règle], après [événement].
    exemple réel (autre notion) : « 2) Indiquer la fonction principale du composant SSD (Solid State Drive). »
    exemple réel (autre notion) : « 6. Afin de ne pas parcourir tout l'arbre, il est plus efficace de rechercher la tâche du nœud situé le plus à gauche de l'arbre binaire de recherche : il correspond à la tâche prioritaire. Recopier et compléter la méthode récursive tache_pr »
    support S0 : Énoncé en prose avec numéros — Support textuel ordinaire mêlant prose et nombres (routeurs, adresses, tailles) ; l'élève travaille à partir d'une mise en situation décrite, sans matériau structuré dominant.
    exemple de support (autre notion) : « 13. Expliquer le test de la ligne 6 du code de la fonction maj. »

- slot 3 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C12 : Exploiter l'élément fourni ci-dessous — La consigne renvoie à un document joint (commandes, circuit, requêtes numérotées, classe, code) à sélectionner, compléter ou utiliser ; on évalue la lecture attentive du support plus qu'une notion précise.
    gabarit : Parmi les [éléments] ci-dessous, [sélectionner/compléter/utiliser] ceux qui permettent de [objectif].
    exemple réel (autre notion) : « 3. Parmi les propositions suivantes, donner la structure la plus adaptée pour stocker les processus d'une même priorité : - Proposition 1 : Liste - Proposition 2 : File - Proposition 3 : Pile Pour représenter le processus, on utilise une cl »
    exemple réel (autre notion) : « 1. Un processeur choisit à chaque cycle d'exécution le processus qui doit être exécuté. Le tableau ci-dessous donne pour trois processus P1, P2, P3 : - la durée d'exécution (en nombre de cycles), - l'instant d'arrivée sur le processeur (exp »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 14. Recopier et compléter les lignes 8 à 11 du code de la méthode chiffrer ci- après.  1 def chiffrer(self, octet):  2 '''  3 renvoie le chiffrement de octet  4 : paramètre octet (list) un tableau de huit 0 ou 1  5 : return (int)  6 '''  7 tab_produits = []  8 »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C19 : Déterminer un chemin ou élément — Questions de détermination (chemin d'un paquet, répertoire, sous-séquence, protocole) sans geste unique, souvent en réseau ; on évalue une déduction à partir du contexte.
    gabarit : Déterminer [le chemin/l'élément] [de A à B / vérifiant la condition] dans [situation].
    exemple réel (autre notion) : « a. Déterminer le parcours infixe de l'arbre de la Proposition B de la question 4. »
    détail du cours à évaluer (Cryptographie) : « import Crypto import libnum from Crypto.Util.number import bytes_to_long, long_to_bytes from Crypto.Random import get_random_bytes »

Le champ id vaut « I-modularite ».