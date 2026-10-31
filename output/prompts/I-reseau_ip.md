# Plan I-reseau_ip (inedit)

Notion : reseau_ip (Architecture, OS et réseaux) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Architecture, OS et réseaux > Rappels reseaux > Rappels reseaux]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 14 - Les réseaux (rappels)
> Objectifs :
> ▷ Rappels de la classe de Première sur les réseaux
> ▷ Rappels de la classe de Première sur fonctionnement du protocole TCP/IP
> 1 Introduction
> Onappelle réseauinformatique ,unensembled'équipementsinformatiquesconnectésentreeuxpardesliaisons
> physiques.
> Ces machines distantes échangent des informations sous forme de données binaires.
> Pourquoi utilise-t-on des réseaux?
> ▷ pour partager des données et des applications;
> ▷ pour partager l'utilisation des périphériques;
> ▷ pour travailler sur une même base de données, un même document ...,etc.
> 2 Les composants d'un réseau
> Les différents ordinateurs et serveurs sont reliés entre eux comme sur le dessin ci-dessous :
> Un réseau localpeut être constitué des éléments suivants :
> ▷ le câble réseau: il peut être en cuivre (appeléRJ45) ou enfibre optique.
> ▷ lacarte réseau
> [Architecture, OS et réseaux > Protocoles de routage > Introduction]
> Dans un réseau quelconque, le coût de chaque liaison se calcule par la formule :
> 
>     $$ \text{coût} = \frac{10^8}{d} $$
> 
>     où le débit $d$ est exprimé en bits/s.
> 
>     Calculer le coût si la liaison a un débit de :
> 
>     **A.** 10 Mb/s
> 
>     **B.** 1 Gb/s
> 
>     **C.** 1 Mb/s
> 
>     **D.** 50 Mb/s
> 
>     {{
>     correction(True,
>     """
> \"Correction \" 
>         - **A.** $c = \\dfrac{10^8}{10 \\times 10^6} = \\dfrac{10^8}{10^7}= 10$
>         - **B.** $c = \\dfrac{10^8}{10^9} = 10^{-1}= 0,1$
>         - **C.** $c = \\dfrac{10^8}{10^6} = 10^2= 100$
>         - **D.** $c = \\dfrac{10^8}{50 \\times 10^6} = \\dfrac{10^2}{50}=2$
>     """
>     )
>     }}
> 
>     Exercice 5 du sujet La Réunion J1 2022
> 
>     _2020, sujet 0_
> 
>     On considère un réseau composé de plusieurs routeurs reliés de la façon suivante :
> 
>     
> 
>     Le protocole RIP permet de construire les tables de routage des différents routeurs, en indiquant

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C15 : Proposer une solution ou modification — L'élève propose une solution ouverte (parcours, fonction, modification de schéma, adresses, tests) ; on évalue la capacité à concevoir une réponse valide parmi plusieurs possibles.
    gabarit : Proposer [un/une] [solution/modification/test] permettant de [objectif] en respectant [contrainte].
    exemple réel (autre notion) : « 7. Proposer un test faisant intervenir une liste aplatie de quatre éléments et comptant deux inversions permettant de vérifier que la fonction compte_inversions renvoie le résultat attendu. EN_NOzUzMD2M0ODAczOT4UzMmTYxMj1A2MDEO2OTtQ0MDTcx »
    exemple réel (autre notion) : « c. Indiquer, pour la relation reservation, la ou les clés étrangères (ou secondaires) et en indiquer l'utilité. »
    support S7 : Consigne brève sans support — Question courte et autonome, sans matériau joint notable ; l'élève répond à partir de ses connaissances ou du contexte de l'exercice.
    exemple de support (autre notion) : « 2. Proposer une clé primaire pour la table reservation. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C18 : Programmer sur un tableau d'entiers — Exercices pratiques où l'élève programme une fonction parcourant un tableau de nombres (recherche, tri, vérification) avec exemples ; on évalue l'algorithmique de base et le passage des tests.
    gabarit : Écrire une fonction [nom] qui prend en paramètre un tableau [tab] de [type] et qui renvoie [résultat]. Exemples : [assertions].
    exemple réel (autre notion) : « 9. Compléter l'instruction suivante afin de mettre à jour dans tournoi la première joueuse de la première demi-finale comme étant gauff.  tournoi. ... = gauff »
    exemple réel (autre notion) : « 2) Écrire en langage Python une fonction calcul_parite prenant en paramètre une liste Liste_bits constituée d'entiers valant 0 ou 1 et retournant l'entier 1 ou 0 correspondant à son bit de parité.  Exemple : >>> Liste_bits = [0, 1, 0, 0, 1, »
    support S0 : Énoncé en prose avec numéros — Support textuel ordinaire mêlant prose et nombres (routeurs, adresses, tailles) ; l'élève travaille à partir d'une mise en situation décrite, sans matériau structuré dominant.
    exemple de support (autre notion) : « 1) a. Indiquer les bits de parité associés aux représentations binaires des deux entiers naturels 9 et 16 écrits en base 10. »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C12 : Exploiter l'élément fourni ci-dessous — La consigne renvoie à un document joint (commandes, circuit, requêtes numérotées, classe, code) à sélectionner, compléter ou utiliser ; on évalue la lecture attentive du support plus qu'une notion précise.
    gabarit : Parmi les [éléments] ci-dessous, [sélectionner/compléter/utiliser] ceux qui permettent de [objectif].
    exemple réel (autre notion) : « 2. On considère la fonction voisine ci-dessous, écrite en langage Python, qui prend en paramètres deux cases données sous forme de couple. def voisine(case1, case2) :  l1, c1 = case1  l2, c2 = case2  # on vous rappelle que 2 signifie puissa »
    exemple réel (autre notion) : « 2. On dispose de la pile suivante nommée p1 :  On rappelle ci-dessous les primitives de la structure de pile (LIFO : Last In First out) : Fonction Description pile_vide() Créé et renvoie une nouvelle pile vide empiler(p, e) Place l'élément  »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 4. Onveutreprésenterschématiquementleréseauderouteursàpartirdestablesderoutage. Recopiersurlacopieleschémaci-dessous: A B C D E F Ens'appuyantsurlestablesderoutage,tracerlesliaisonsentrelesrouteurs. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C3 : Questions de raisonnement hétérogènes — Mélange de consignes (dessiner un graphe, comparer, justifier, lister des dépendances) liées par des tournures pluriel génériques ; le point commun est seulement un raisonnement contextualisé sur une situation.
    gabarit : En étudiant [situation/données], [donner/comparer/justifier] [élément demandé]. Justifier la réponse.
    exemple réel (autre notion) : « 2. À l'aide des extraits de tables, détailler un achat d'Emile Pasteur en précisant : – la date de son achat ; – le ou les article(s) acheté(s) ; – si c'est le cas, le taux de remise dont il a bénéficié. Un nouveau client doit être entré da »
    détail du cours à évaluer (Rappels reseaux) : « Ainsi, on fera une association entre une adresse IP et un masque pour savoir dans cette adresse IP quelle est la partie réseau et quelle est la partie machine de l'adresse. »

Le champ id vaut « I-reseau_ip ».