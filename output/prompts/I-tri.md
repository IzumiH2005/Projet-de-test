# Plan I-tri (inedit)

Notion : tri (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Diviser pour regner > Diviser pour regner]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 24 - Diviser pour régner
> Objectifs :
> ▷ Ecrire un algorithme en utilisant la méthode"diviser pour régner".
> 1 Introduction
> Nous avons vu en première deux algorithmes de tris assez naturels, mais peu efficaces : letri par insertionet
> le tri par sélectionen classe de Première.
> Cette année, nous allons étudier un algorithme beaucoup plus efficace et très utilisé, inventé parJohn Von
> Neumann en 1945 : letri par fusion.
> Cet algorithme nous permettra d'illustrer la méthodediviser pour régnerque nous avions également déjà
> vue lors de larecherche dichotomiqueen classe de Première.
> 2 La dichotomie (rappels)
> Nous avons vu en classe dePremièrel'algorithme dedichotomie. Ce mot, qui vient du grecdikhotomia, signifie
> « division en deux parties ».
> Notre but ici est la recherche de la présence (ou non) d'un élément dans une liste triée. Notre fonction renv
> [Algorithmique > Diviser pour regner > 4.1 Preambule : l'interclassement]
> Le mécanisme principal du tri fusion est la **fusion** de deux listes triées en une nouvelle liste elle aussi triée.
> 
> On appelera ce mécanisme l'**interclassement**.
> 
>     Pour interclasser deux listes triées ```lst1``` et ```lst2```.
> 
>     - on part d'une liste vide ```lst_totale```
>     - on y ajoute alternativement les éléments de ```lst1``` et ```lst2```, en veillant à maintenir un ordre croissant. Il faut pour cela gérer séparément un indice ```i1``` pour la liste ```lst1```  et un indice ```i2```  pour la liste ```i2```.
>     - quand une liste est épuisée, on y ajoute la totalité restante de l'autre liste.
> 
>     
>     Coder la fonction ```interclassement```. 
> 
>     :arrow_right: Aide avec des codes à trous
> 
>     
> 
> **Remarque :** cette fonction fait l'objet d'un exercice de la BNS, qui n'utilise pas le slicing (ce qui rend le code plus efficace).

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C18 : Tracer une boucle Python donnée — L'élève suit l'exécution d'un code avec boucles for/range pour en déduire une valeur ou un affichage. On évalue la trace d'exécution.
    gabarit : Déterminer la valeur de [variable] à l'issue des instructions suivantes : [code].
    exemple réel (autre notion) : « 1. Ceconstructeurautomobileintègreàsesvéhiculesdessystèmesembarqués,commeparexemple un système de guidage par satellites (GPS), un système de freinage antiblocage (ABS) ... Ces dispositifs utilisent des systèmes sur puces (SoC : Système on  »
    exemple réel (autre notion) : « 3. Compléter le code de la fonction est_constructible.  1 def est_constructible(carte, i_coin, j_coin, taille): 2 s = 0 3 for i in range(i_coin, i_coin + taille): 4 for j in range(..., ...): 5 s = ... 6 ... # Plusieurs lignes possibles »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « a. Recopier et compléter la ligne 4 de la fonction ci-dessous :  1 def chercher_mots(liste_mots,longueur,lettre,position): 2 res = [] 3 for i in range(len(liste_mots)): 4 if …………… and …………… : 5 res.append(liste_mots[i]) 6 return res »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « Question 3 1. Vériﬁer que le coût de la liaison entre les routeurs A et B est 0,01. 2. La liaison entre le routeur B et D a un coût de 5. Quel est le débit de cette liaison? »
    exemple réel (autre notion) : « b. renommer le dossier "bizarre" en dossier "videos" ?  22-NSIJ2LR1 Page 8 sur 13 »
    support S10 : Prose riche en virgules — Phrases longues avec énumérations par virgules ou listes de choix. Artefact de ponctuation, contenus variés.
    exemple de support (autre notion) : « 16. Déterminer la route qui sera empruntée par le paquet de données envoyé de l'ordinateur P1 à l'ordinateur P2, en respectant le protocole OSPF. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C5 : Donner le nom ou l'instruction — L'élève nomme un élément ou fournit une instruction ou un tuple précis. On évalue une réponse courte et exacte.
    gabarit : Donner le [nom|tuple|instruction] correspondant à [situation].
    exemple réel (autre notion) : « a. Ecrire une requête SQL permettant d'afficher le nom des plats, leur type et leur prix. »
    exemple réel (autre notion) : « 12. Donner le nom du type de parcours de graphe, utilisé dans la fonction dico_distance. »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 13. Dessiner le nouvel arbre de recherche a_final obtenu après suppression des équipes eq2 et eq5 dans l'ABR correspondant au classement général. L'organisateur souhaite disposer d'une fonction rechercher permettant de savoir si une équipe a été disqualifiée o »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « 4. Classer les types de mémoire suivants selon leur rapidité d'accès aux données, de la plus rapide à la plus lente. – Mémoire cache – Disque dur – Mémoire vive – Registre Les instructions d'un programme Python ne peuvent pas être exécutées »
    détail du cours à évaluer (Langage SQL) : « À partir de ce point de départ et d'une base de données dont le diagramme est donné ci-dessous, il s'agit de trouver le meurtrier. »

Le champ id vaut « I-tri ».