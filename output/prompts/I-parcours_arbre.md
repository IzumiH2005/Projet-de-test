# Plan I-parcours_arbre (inedit)

Notion : parcours_arbre (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Arbres > 2.4 Parcours postfixe]
> Le parcours **postfixe** est aussi un parcours en profondeur d'abord.
> 
>     (parfois aussi appelé **post-ordre** ou encore **suffixe**)
> 
>     - Chaque nœud est visité **après** ses fils le soient.
>     - On part donc de la feuille la plus à gauche, et on ne remonte à un nœud père que si ses fils ont tous été visités. 
> 
> L'ordre des lettres parcourues est donc P-Y-H-N-O-T.
> [Structures de données > Arbres > 2.1 Parcours en largeur d'abord (BFS)]
> *BFS : Breadth First Search*
>  
>     Le parcours en largeur d'abord est un parcours étage par étage (de haut en bas) et de gauche à droite.
> 
> L'ordre des lettres parcourues est donc T-Y-O-P-H-N.
> 
> Les trois parcours que nous allons voir maintenant sont des parcours en **profondeur d'abord**, ou **DFS** (*Depth First Search*). Ce qui signifie qu'un des deux sous-arbres sera totalement parcouru avant que l'exploration du deuxième ne commence.

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « 4. Recopier et compléter les lignes 8, 14 et 17 du code de la fonction ajout_espace. »
    exemple réel (autre notion) : « 3. Recopier sur la copie les lignes 9 et 11 en complétant les points de suspension. »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 4. Écrire l'instruction à exécuter pour créditer de 100 € le compte de Cara créé à la question 2. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 9. Écrire une fonction evaluation(expression) qui prend en paramètre une expression en notation polonaise inverse dont les termes et les opérateurs sont deux à deux séparés par des espaces et qui renvoie l'évaluation de cette expression sou »
    exemple réel (autre notion) : « b. De manière plus générale, que renvoie la fonction mystere pour une chaîne représentant un déplacement donné ? »
    support S14 : Prose avec parenthèses — Phrases contenant des parenthèses (couples, types, précisions). Artefact de ponctuation sans matériau commun.
    exemple de support (autre notion) : « 4. Écrire le code Python d'une fonction nb_maison(lst) qui prend en argument une liste Python de biens immobiliers de type Bim et qui renvoie le nombre d'objets de nature 'maison' contenus dans la liste lst. »

- slot 3 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 7. Écrire l'instruction permettant d'instancier navigateurs un objet de la classe Priority_Queue. EN_NOTM0NT7QzNjAc0ND4UzMsTYxMj4A2NTAAwMDxAxNAjQx On rappelle que la méthode pop(), appelée sans argument, supprime et renvoie le dernier éléme »
    détail du cours à évaluer (Arbres) : « Choisir le type de parcours d'arbres binaires de recherche réalisé parmi les propositions suivantes : Préfixe, Suffixe ou Infixe. »

Le champ id vaut « I-parcours_arbre ».