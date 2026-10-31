# Plan I-tableau_liste (inedit)

Notion : tableau_liste (Programmation) — questions JAMAIS POSÉES aux annales

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
> [Algorithmique > Programmation dynamique > Introduction]
> Exercice 1 du sujet 0 - version B 2024
> 
>     
> 
>     
> 
>     
> 
>     {{
>     correction(False,
>     """
> \"Correction Q4.\" 
>         Pour une pyramide de $n$ niveaux, il va y avoir $n-1$ choix de direction (droite ou gauche). Cela revient donc à écrire un mot binaire composé de $n-1$ chiffres (0 ou 1).
> 
>         Or le nombre de mots binaires de longueur $n-1$ est égal à $2^{n-1}$ donc une pyramide de n niveaux comportera $2^{n-1}$ conduits.
>     """
>     )
>     }}
> 
>     
> 
>     
> 
>     
> 
>     
> 
>     
> 
>     {{
>     correction(False,
>     """
> \"Correction Q10.\" 
>         On pourrait utiliser la mémoïsation pour éviter la redondance des calculs, par exemple en utilisant un dictionnaire de clés ```(i,j)``` pour stocker les ```score_max(i,j,p)```.
>        
>         Exemple de code (non demandé) :
>         ```python linenums='1'
>         memo = {}
>         def score_max(i, j, p):
>             if i == len(p) - 1:
>           

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « a. Recopier et compléter les ………… des lignes 10, 11 et 14 de la fonction code_morse. »
    exemple réel (autre notion) : « b. Recopier les lignes issues de la requête : SELECT Nom_evaluation, Date FROM Evaluations WHERE auteur= "Peltier" »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 8. Adapter les lignes 6 à 13 de la fonction chiffrement pour obtenir la nouvelle fonction dechiffrement. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « 2. Écrire la requête SQL permettant de mettre à jour la base de données. »
    exemple réel (autre notion) : « 2. Indiquer les noms des lacs qu'on peut atteindre depuis le parking de Chamonix d'après la base de données de Susie. À partir de maintenant, on travaille sur la totalité des enregistrements et non plus seulement sur les extraits précédents »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 11. Écrire en Python cette fonction adherent_plus_age. »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C18 : Tracer une boucle Python donnée — L'élève suit l'exécution d'un code avec boucles for/range pour en déduire une valeur ou un affichage. On évalue la trace d'exécution.
    gabarit : Déterminer la valeur de [variable] à l'issue des instructions suivantes : [code].
    exemple réel (autre notion) : « 12. L.append(L1[i1]) »
    exemple réel (autre notion) : « 4. Edgar réalise maintenant l'appel tri_dictatorial([]) et obtient l'erreur suivante :  Traceback (most recent call last):  File "tri_edgar.py", line 8, in <module>  tri_dictatorial([])  File "tri_edgar.py", line 2, in tri_dictatorial  resu »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 1. Recopier et compléter la ligne 4 de la fonction est_operateur. On souhaite maintenant écrire une fonction est_nombre qui prend en paramètre une chaîne de caractères s et qui renvoie si s correspond à un nombre (positif ou négatif). Par exemple les appels à  »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 3. Que renvoie l'appel mystere(A2,‘SIMENON') ? Justifier la réponse.  L'éditeur souhaite utiliser une fonction récursive hauteur(ABR) qui prend en paramètre un arbre binaire ABR et renvoie la hauteur de cet arbre. »
    détail du cours à évaluer (Listes Piles Files) : « _vide : indique si la liste est vide. (renvoie un booléen) »

Le champ id vaut « I-tableau_liste ».