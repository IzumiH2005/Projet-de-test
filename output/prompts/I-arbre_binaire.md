# Plan I-arbre_binaire (inedit)

Notion : arbre_binaire (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Arbres > 1.3 Caractéristiques d'un arbre]
> #### 1.3.1 Outils numériques de description
> 
>     - la **taille** d'un arbre est son nombre total de nœuds. Ici, elle vaut 8.
> 
>     - l'**arité** d'un nœud est son nombre de fils. Ici, l'arité de B vaut 2, celle de F vaut 1, celle de Z vaut 0.
> 
>     - la **profondeur** d'un nœud est le nombre de nœuds de son chemin le plus court vers la racine. 
>     Ici, la profondeur de G est 3 (G-K-C), la profondeur de B est 2 (B-C), la profondeur de Z est 4 (Z-F-B-C), la profondeur de C est 1.
> 
>     - la **hauteur** d'un arbre est la profondeur de son nœud le plus profond. 
>     Ici, la hauteur de l'arbre est 4.  
>         Nous prendrons comme **convention** que :  
>         - si un arbre est réduit à **un seul nœud-racine**, sa hauteur sera **1**.
>         - si un arbre est **vide**, sa hauteur est **0**.
> 
> *Cette convention est celle adoptée dans le sujet 0 publié le 15/12/2020. Attention, dans certains ouvr
> [Structures de données > Arbres > Introduction]
> Exercice 2 du sujet Nouvelle-Calédonie J2 2022  
> 
>     *2020, sujet 0*
> 
>     **Question  1**
> 
>     Déterminer la taille et la hauteur de l’arbre binaire suivant :
>     
> 
>     
> 
>     **Question 2**  
> 
>     On décide de numéroter en binaire les nœuds d’un arbre binaire de la façon suivante :  
> 
>     - la racine correspond à 1 ;
>     - la numérotation pour un fils gauche s’obtient en ajoutant le chiffre 0 à droite au numéro de son
>     père ;
>     - la numérotation pour un fils droit s’obtient en ajoutant le chiffre 1 à droite au numéro de son
>     père ;  
> 
>     Par exemple, dans l’arbre ci-dessous, on a utilisé ce procédé pour numéroter les nœuds A, B, C, E et
>     F .
> 
>     
> 
>     **a**. Dans l’exemple précédent, quel est le numéro en binaire associé au nœud G ?
>     
>     **b**. Quel est le nœud dont le numéro en binaire vaut 13 en décimal ?
>     
>     **c**. En notant $h$ la hauteur de l’arbre, sur combie

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « b. Que renvoie la commande ajouter("b", ["a","b","c"]) ? »
    exemple réel (autre notion) : « 1. Quel est le nom de la première commande exécutée par le système d'exploitation lors du démarrage ? »
    support S11 : Texte contenant des tirets — Matériau marqué par des tirets (mots composés, puces, listes chaînées). Artefact typographique mêlant fonctions récursives et énigmes.
    exemple de support (autre notion) : « 11. On envisage d'utiliser l'ensemble des fonctions proposées ci -dessus pour rechercher le site le plus populaire parmi un très grand nombre de sites (quelques milliers de sites). Expliquer si ce code est adapté à une telle quantité de sites à traiter. Justif »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C17 : Question directe « quelle est » — L'élève indique une valeur, une propriété ou un élément d'une structure. Réponse courte ; le groupe reste un peu hétérogène.
    gabarit : Quelle est la [valeur|propriété] de [objet] ?
    exemple réel (autre notion) : « 6. Rappeler avec quelle expression Python on peut tester si une clé c est déjà présente dans un dictionnaire dico. »
    exemple réel (autre notion) : « 3. Une fois ce code exécuté, donner la valeur de jeu_9[0].valeur. »
    support S14 : Prose avec parenthèses — Phrases contenant des parenthèses (couples, types, précisions). Artefact de ponctuation sans matériau commun.
    exemple de support (autre notion) : « 5. Indiquer l'acronyme utilisé pour désigner la structure de file.  Voici, en langage Python, les opérations pouvant être effectuées sur une telle file : • creerFile() : renvoie une file vide ; • estVide(F) : renvoie True si la file F est vide et False sinon ; »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 7. Compléter la méthode de la classe Region ci-dessous à partir de la ligne 8 :  1 2 3  4 5 6  7 8 def retire_couleur(self, couleur):  '''  Retire couleur du tableau de couleurs disponibles de la région si elle est dans ce tableau. Ne fait  »
    exemple réel (autre notion) : « 4. On considère la fonction suite(n) qui reçoit un entier positif et renvoie un entier. 1| def suite(n) : 2| if n == 0 : 3| return 0 4| else : 5| return 3+2*suite(n-2) »
    support S4 : Prose multi-lignes sans forme distinctive — Texte d'énoncé courant sur plusieurs lignes, sujets divers (algorithmes, graphes, Huffman). Forme générique, pas de matériau spécifique.
    exemple de support (autre notion) : « 13. Écrire les requêtes qui permettent de corriger la base de données. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 1. Donner la valeur de melangee[2][1]. »
    détail du cours à évaluer (Arbres) : « La taille d’un arbre est le nombre de nœuds qu’il contient ; sa hauteur est le nombre de nœuds du plus long chemin qui joint le nœud racine à l’une des feuilles. »

Le champ id vaut « I-arbre_binaire ».