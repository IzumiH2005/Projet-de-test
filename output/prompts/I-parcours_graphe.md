# Plan I-parcours_graphe (inedit)

Notion : parcours_graphe (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Graphes > 4. Recherche du plus court chemin]
> En utilisant la fonction ```recherche_chemin``` du cours, établir le plus court chemin pour aller de A vers P dans ce labyrinthe.
> 
>     {{
>     correction(False,
>     """
> \"Correction\" 
>         ```python linenums='1'
>         def recherche_chemin(g, depart, arrivee):
>             '''
>             Parcours en largeur du graphe g en partant du sommet depart,
>             qui s'arrête dès que le sommet arrivee est atteint.
>             Renvoie alors le chemin du depart vers arrivee.
>             '''
>             traites = []
>             decouverts = [depart]
>             en_attente = [depart]
>             parent = {}
>             while en_attente != [] :
>                 sommet = en_attente.pop(0)
>                 voisins = g.voisins(sommet)
>                 for voisin in voisins:
>                     if voisin not in decouverts:
>                         decouverts.append(voisin)
>                         en_
> [Structures de données > Graphes > 4.1.3 Application du BFS : recherche du plus court chemin]
> L'algorithme BFS découvre les sommets «par cercles concentriques» autour du point de départ (ainsi que le montre la structure de la file d'attente). On découvre d'abord tous les sommets à la distance 1 du point de départ, puis à la distance 2, puis 3, etc.
> 
> Un sommet situé à la distance 5 sera découvert en tant que voisin d'un sommet à la distance 4, qui lui-même aura été découvert grâce à un sommet à la distance 3, qui lui-même...
> 
> On comprend donc que si on arrive à se souvenir du sommet «parent» de chaque sommet (celui qui lui a permis d'être découvert), on pourra alors reconstituer un chemin permettant de remonter au point de départ.
> 
> Nous allons pour cela nous servir d'une structure de dictionnaire pour associer à chaque sommet son sommet-parent.
> 
> Il faudra ensuite une fonction pour recréer le chemin.
> 
>     - Comment est-on sûr qu'un chemin va être trouvé entre deux sommets A et B ?
> 

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Analyser un code fourni — Un extrait de code (def numéroté) est donné, à compléter ou à exécuter mentalement ; on évalue la lecture de code et la compréhension de ce qu'il fait.
    gabarit : On considère le code suivant : [code]. [Compléter la ligne n / Donner ce qu'affiche l'appel [appel]].
    exemple réel (autre notion) : « 14. else: »
    exemple réel (autre notion) : « 2. Recopier et compléter le code de la méthode avancer de la classe Tache qui permet d'avancer la tâche self de n minutes.  1 def avancer(self, n): 2 ... »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 1. Déterminer si l'expression '[2*(i+1)-3) for i in range(3, 10)]' est bien parenthésée. Justifier votre réponse »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C18 : Programmer sur un tableau d'entiers — Exercices pratiques où l'élève programme une fonction parcourant un tableau de nombres (recherche, tri, vérification) avec exemples ; on évalue l'algorithmique de base et le passage des tests.
    gabarit : Écrire une fonction [nom] qui prend en paramètre un tableau [tab] de [type] et qui renvoie [résultat]. Exemples : [assertions].
    exemple réel (autre notion) : « 10. Utiliser les fonctions précédentes et la classe Noeud afin d'écrire une fonction choisit_coup(grille, joueur) prenant en arguments une grille de jeu et le numéro d'un joueur et renvoyant le numéro de la colonne où devrait jouer le joueu »
    exemple réel (autre notion) : « b. Donner le contenu de la pile A après l'exécution de cette instruction. On souhaite maintenant écrire le code d'une méthode depileMax d'une pile non vide ne contenant que des nombres entiers et renvoyant le plus grand élément de cette pil »
    support S6 : Texte avec parenthèses explicatives — Support riche en parenthèses (signatures, précisions, sous-questions (a)(b)) ; l'élève doit tenir compte des précisions et des paramètres annoncés.
    exemple de support (autre notion) : « 2. Donner la route suivie par une requête issue du bureau numéro 1 jusqu'au prestataire si on utilise le protocole RIP. »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « c. Ecrire une fonction dechiffre(mot, dico) qui reçoit un mot chiffré et un dictionnaire de chiffrement et renvoie le mot décodé. On utilisera les fonctions écrites dans les questions précédentes. »
    exemple réel (autre notion) : « 3. Écrire une fonction etendre(pile1, pile2) qui prend en arguments deux objets Pile appelés pile1 et pile2 et qui modifie pile1 en lui ajoutant les éléments de pile2 rangés dans l'ordre inverse. Cette fonction ne renvoie rien. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 6. Proposer une version itérative, non récursive, suite3 du calcul des termes de la suite Un. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C12 : Exploiter l'élément fourni ci-dessous — La consigne renvoie à un document joint (commandes, circuit, requêtes numérotées, classe, code) à sélectionner, compléter ou utiliser ; on évalue la lecture attentive du support plus qu'une notion précise.
    gabarit : Parmi les [éléments] ci-dessous, [sélectionner/compléter/utiliser] ceux qui permettent de [objectif].
    exemple réel (autre notion) : « 4. Recopier et compléter sur votre copie le chronogramme ci -dessous pour les processus p1, p2, p3 et p4.  Figure 2. Chronogramme pour les processus p1, p2, p3 et p4 Pour mettre en place l'ordonnancement suivant cette méthode, on écrit la c »
    détail du cours à évaluer (Gestion des processus) : « la durée d’exécution (en nombre de cycles), - l’instant d’arrivée sur le processeur (exprimé en nombre de cycles à partir de 0), - le numéro de priorité. »

Le champ id vaut « I-parcours_graphe ».