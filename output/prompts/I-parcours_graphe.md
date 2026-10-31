# Plan I-parcours_graphe (inedit)

Notion : parcours_graphe (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Graphes > 6. Annexe : et pourquoi pas en DFS ?]
> Les parcours BFS et DFS ont tous deux la propriété de parcourir **la totalité** du graphe (ils sont même conçus pour cela). Cela a permis au parcours BFS de nous fournir une solution au labyrinthe (dont on a démontré qu'elle était la plus courte).
> 
> Que penser de la solution qui sera donnée par le DFS ?
> 
> #### 6.1 Dans un labyrinthe parfait
> 
> Voici un code où la solution est d'abord recherchée par BFS (cases explorées en bleu clair, chemin trouvé marqué en bleu), puis en DFS (cases explorées en rose, chemin trouvé marqué en rouge).
> 
> anim_laby_DFSvsBFS_laby_parfait.py :arrow_down:
> 
> Que remarquez-vous ???
> 
> #### 6.2 Dans un labyrinthe non parfait
> 
> Changeons de code pour un labyrinthe *dégénéré* :
> 
> anim_laby_DFSvsBFS_laby_degenere.py :arrow_down:
> 
> Que remarquez-vous ???
> 
>     Notre labyrinthe conçu de manière aléatoire possède une propriété remarquable (due à son algorithme de construction) : ch
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

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C15 : Recopier et compléter un élément — L'élève recopie puis complète une fonction, un résultat ou une table partiellement donnés. On évalue la capacité à combler les trous correctement.
    gabarit : Recopier et compléter [la fonction|le tableau] [nom] [donné ci-dessous].
    exemple réel (autre notion) : « 5. Recopier et compléter la fonction chaine_vers_tab(mot) ci-dessous. Cette fonction prend en paramètre une chaine de quatre caractères et renvoie un tableau (ty pe list en Python) dont les éléments sont les caractères de cette chaine. »
    exemple réel (autre notion) : « 4. Le magasin vient de recevoir des meubles dont l'intitulé est 'hylla' et dont l'attribut id dans la relation Meubles vaut 98. Le stock de ces meubles est alors de 50. Recopier et compléter la requête SQL ci-dessous qui permet de mettre à  »
    support S13 : Listes et tableaux de nombres — Littéraux Python de listes ou matrices d'entiers, doctests. L'élève s'en sert comme données d'entrée ou de vérification.
    exemple de support (autre notion) : « 9. Recopier et compléter la ligne 4 de la fonction get_nb_rando qui prend en paramètres un identifiant de parking et une liste de randonnées, et qui renvoie le nombre de randonnées qui partent de ce parking.  1 def get_nb_rando(parking, randos): 2 nb = 0 3 for »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 7. Recopier et compléter le code de la fonction ajouter_file_prio.  1 def ajouter_file_prio(f, t, p):  2 f_aux = File()  3 while ...:  4 ...  5 ...enfiler(...)  6 while not ...:  7 ...  8 while not ...:  9 ... »
    exemple réel (autre notion) : « 3. Un extrait des informations stockées dans le fichier collection_timbres.csv au format CSV est donné ci-dessous : nom_timbre;annee_fabrication;nom_collectionneur Gustave Eiffel;1950;Dupont Marianne;1989;Durand Alan Turing;2012;Dupont Donn »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 10. Écrire une fonction modification qui prend en paramètres une file f et une chaine de caractères nv_mdp. Si le mot de passe nv_mdp répond bien aux deux exigences des questions 7 et 9, alors elle modifie la file des mots de passe stockés et renvoie True. Dan »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C1 : Écrire la fonction ou commande nommée — L'élève produit un code précis (fonction, méthode, commande shell) dont le nom est imposé. On évalue la justesse et la syntaxe du code écrit.
    gabarit : Écrire la [fonction|méthode|commande] [nom] qui [comportement attendu].
    exemple réel (autre notion) : « a. Ecrire la commande qui permet de lister le contenu du répertoire projet . »
    exemple réel (autre notion) : « a. Écrire une instruction qui permet d'importer la fonction sqrt du module math. »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 7. Recopier et compléter le code de la fonction meme_reseau. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « 2. Indiquer quels sont les nœuds de la branche qui se termine par la feuille qui a pour valeur 3. »
    détail du cours à évaluer (Protocoles de routage) : « Quel est le chemin reliant R1 et R6 qui a le plus petit coût ? »

Le champ id vaut « I-parcours_graphe ».