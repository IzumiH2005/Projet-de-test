# Plan I-matrice (inedit)

Notion : matrice (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Graphes > 2.1 Représentation par matrice d'adjacence]
> - On classe les sommets (en les numérotant, ou par ordre alphabétique).
>     - on représente les arêtes (ou les arcs) dans une matrice, c'est-à-dire un tableau à deux dimensions où on inscrit un 1 en ligne `i` et colonne `j` si les sommets de rang `i` et de rang `j` sont **voisins** (dits aussi *adjacents*).
> 
>     Ce tableau s'appelle une **matrice d'adjacence** (on aurait très bien pu l'appeler aussi *matrice de voisinage*).
> 
> #### 2.1.1 Graphe non orienté
> 
> Dans ce graphe non orienté, comme B est voisin de C, C est aussi voisin de B, ce qui signifie que l'arête qui relie B et C va donner lieu à deux "1" dans la matrice, situé de part et d'autre de la diagonale descendante (un mathématicien parlera de matrice *symétrique*).
> 
> #### 2.1.2 Graphe orienté
> 
> Comme le graphe est orienté, la matrice n'est pas forcément symétrique (il faudrait que tous les liens soient réciproques pour qu'elle le soi
> [Programmation > Programmation Orientee Objet > Exercices]
> **Q1.** Écrire une classe ```Eleve``` qui contiendra les attributs ```nom```, ```classe``` et ```note```.
>     
> 
>     **Q2.** Instancier trois élèves de cette classe.
>     
> 
>     **Q3.**  Écrire une fonction ```compare``` qui prend en paramètres deux élèves ```eleve1``` et ```eleve2``` qui renvoie le nom de l'élève ayant la meilleure note (on ne traitera pas à part le cas d'égalité).
> 
>         ```python
>         >>> riri = Eleve("Henri", "TG2", 12)
>         >>> fifi = Eleve("Philippe", "TG6", 15)
>         >>> loulou = Eleve("Louis", "TG1", 8)
>         >>> compare(riri, fifi)
>         'Philippe'
>         ```
> 
>     
>     Écrire une classe ```TriangleRect``` qui contiendra les attributs ```cote1```, ```cote2``` et ```hypotenuse```.
> 
>     La méthode constructeur ne prendra en paramètres que ```cote1``` et ```cote2```, l'attribut ```hypotenuse``` se calculera automatiquement.
> 
>         ```python
>         >>>

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 11. Compléter le script de cette fonction recherche_mot en recopiant les lignes 5, 6, 15, 16, 18 sur votre copie. 1 def recherche_mot(mdp): 2 mot = transforme(mdp) 3 trouve = [] 4 i = 0 5 while ... : 6 if ... : # si le caractère est un chif »
    exemple réel (autre notion) : « 9. La fonction fournit le coloriage : {1: 'Vert', 2: 'Bleu', 3: 'Rouge', 4: 'Vert', 5: 'Rouge', 6: 'Bleu', 7: 'Bleu', 8: 'Bleu', 9: 'Rouge'} »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 12. Recopier et compléter la fonction plus_court donnée ci-dessous. La fonction plus_court prend pour paramètres un graphe G, un sommet de départ depart et un sommet d'arrivée arrivee ; elle renvoie un des chemins les plus courts sous la forme d'une liste de s »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « 2. Proposer le schéma relationnel de la table Type en soulignant la clé primaire. »
    exemple réel (autre notion) : « 11. Écrire le schéma relationnel des deux nouvelles tables en indiquant clairement les clés primaires et les clés étrangères. »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 5. Expliquer succinctement le principe de l'algorithme de Boyer-Moore qui permet d'implémenter cette fonction recherche. Une idée est d'écrire une fonction qui décrète qu'un programme s'arrête s'il ne contient pas de while et ne s'arrête pas s'il en contient u »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C11 : Analyser une ligne de code précise — L'élève explique ou corrige le rôle d'une ligne désignée dans un programme fourni. On évalue la lecture fine du code.
    gabarit : Expliquer le rôle de la ligne [n] de la fonction [nom].
    exemple réel (autre notion) : « b. ligne 3 : compléter le masque de sous réseau en notation binaire ; »
    exemple réel (autre notion) : « 1. Cette partie comprend plusieurs questions générales : »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 3. Expliquer pourquoi l'exécution de la fonction lcs_force_brute risque de prendre beaucoup de temps selon la longueur des listes passées en paramètre. Justifier. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « b. Indiquer la route entre les routeurs G et E avec le protocole OSPF. »
    détail du cours à évaluer (Cryptographie) : « chiffrement par bloc de 128 bits, répartis dans une matrice de 16 octets (matrice carrée de taille 4). »

Le champ id vaut « I-matrice ».