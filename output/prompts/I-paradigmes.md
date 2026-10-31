# Plan I-paradigmes (inedit)

Notion : paradigmes (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Diviser pour regner > 1.1 Version impérative]
> {#
> 
>     ```python linenums='1'
>     def recherche_dichotomique(tab, val) :
>         '''
>         renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
>         '''
>         ...
>     ```
> #}
> 
>     ```python linenums='1'
>     def recherche_dichotomique(tab, val) :
>         '''
>         renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
>         '''
>         i_debut = 0
>         i_fin = len(tab) - 1
>         while i_debut >> tab = [1, 5, 7, 9, 12, 13]
> >>> recherche_dichotomique(tab, 12)
> True
> >>> recherche_dichotomique(tab, 17)
> False
> ```
> 
> À chaque tour de la boucle ```while```, la taille de la liste est divisée par 2. Ceci confère à cet algorithme une **complexité logarithmique** (bien meilleure qu'une complexité linéaire).
> [Programmation > Recursivite > 4.2 Comparaison des performances]
> Écrire une fonction ```fibo_imperatif(n)``` qui calcule de façon directe (*impérative*) le n-ième terme de la suite de Fibonacci. On pourra par exemple utiliser un dictionnaire.
> 
>     {{
>     correction(True,
>     """
> \"Correction\" 
>         ```python linenums='1'
>         def fibo_imperatif(n):
>             f = {}
>             f[0] = 0
>             f[1] = 1
>             for k in range(2, n+1):
>                 f[k] = f[k-1] + f[k-2]
>             return f[n]
>         ```        
>     """
>     )
>     }}
> 
> Construisons une fonction ```comparaison``` qui affichera le temps de calcul pour chacune des deux fonctions ```fibo_imperatif``` et ```fibo_recursif``` :
> 
> {#
> ```python linenums='1'
> import time
> 
> def fibo_imperatif(n):
>     ...
> 
> def fibo_recursif(n):
>     if n == 0 :
>         return 0   
>     elif n == 1 :
>         return 1
>     else :
>         return fibo_recursif(n-1) + fibo_recursif(n-2)
> 
> def comparaison(n)

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « f ) La fonction récursive maximum ci-dessous prend en paramètre un arbre binaire de recherche abr et renvoie la valeur maximale de ses nœuds. Recopier et compléter les lignes 5 et 7 de cette fonction. 1 def maximum(abr): 2 if abr is None: 3 »
    exemple réel (autre notion) : « 2. Recopier et compléter les lignes 8 à 10 du code de la fonction gen_mdp permettant d'initialiser les trois variables minuscules, majuscules et caracteres_speciaux. On utilisera obligatoirement la syntaxe de tableaux donnés en compréhensio »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 5. Écrire une requête permettant d'ajouter ce champignon avec l'id 56 dans la table champignon. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 1. Expliquer le choix de num_dossard comme clé primaire pour la relation coureur. »
    exemple réel (autre notion) : « 8. Écrire le code de la fonction nb_amis(d, s) qui prend en paramètres un dictionnaire d'adjacence d et un nom de sommet s et qui renvoie le nombre d'amis du nom de sommet s. On suppose que s est bien dans d.  Par exemple : >>> nb_amis(grap »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 7. Écrire une fonction ordre_faro qui prend en paramètres un entier n pair et qui renvoie le plus petit nombre de répétitions du mélange faro pour qu'un jeu de n cartes soit remis dans son ordre initial. »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C18 : Tracer une boucle Python donnée — L'élève suit l'exécution d'un code avec boucles for/range pour en déduire une valeur ou un affichage. On évalue la trace d'exécution.
    gabarit : Déterminer la valeur de [variable] à l'issue des instructions suivantes : [code].
    exemple réel (autre notion) : « b. Représenter la pile p après l'exécution du code suivant. empiler(p, depiler(p)) »
    exemple réel (autre notion) : « 8. else: »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 16. Proposer une version corrigée de la fonction nettoie qui évite le déclenchement de l'erreur décrite. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 1. Alice s'inscrit sur un nouveau site lui demandant de créer un mot de passe de 8 caractères minimum, composé uniquement de majuscules et de minuscules. Écrire un appel à la fonction gen_mdp qui permette de répondre aux exigences de ce sit »
    détail du cours à évaluer (Recursivite) : « Écrire une fonction _imperatif(n) qui calcule de façon directe (*impérative*) le n-ième terme de la suite de Fibonacci. »

Le champ id vaut « I-paradigmes ».