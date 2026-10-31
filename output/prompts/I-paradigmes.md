# Plan I-paradigmes (inedit)

Notion : paradigmes (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Diviser pour regner > 1. Retour sur l'algorithme de dichotomie]
> Nous avons vu en classe de Première l'algorithme de **dichotomie** (du grec *dikhotomia*, « division en deux parties »).
> 
> Notre but ici est la recherche de la présence (ou non) d'un élément dans une liste **triée**.  
> Notre fonction renverra donc un booléen.
> 
> La recherche *naïve* (élément par élément) est naturellement de complexité linéaire. Nous allons voir que la méthode dichotomique est plus efficace.
> 
> :arrow_right: Activité d'introduction
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

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Analyser un code fourni — Un extrait de code (def numéroté) est donné, à compléter ou à exécuter mentalement ; on évalue la lecture de code et la compréhension de ce qu'il fait.
    gabarit : On considère le code suivant : [code]. [Compléter la ligne n / Donner ce qu'affiche l'appel [appel]].
    exemple réel (autre notion) : « 8. Écrire une fonction meilleur_priorite qui renvoie None s'il n'y a plus de processus et la priorité de l'un des processus les plus prioritaires de la liste des files d'attente dans le cas contraire. 1 def meilleur_priorite(liste_files): 2 »
    exemple réel (autre notion) : « 7. while i1 < n1 or i2 < n2 : »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 3. Expliquer pourquoi l'exécution de la fonction lcs_force_brute risque de prendre beaucoup de temps selon la longueur des listes passées en paramètre. Justifier. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 3. Écrire en Python une fonction notes_paquet qui prend en paramètre un paquet de copies p et une correction corr et qui renvoie un dictionnaire dont les clés sont les noms des candidats du paquet p et les valeurs sont leurs notes selon la  »
    exemple réel (autre notion) : « 3. On souhaite créer une fonctionmeilleur_concurrent qui prend en paramètre une listeL de concurrents et qui renvoie l'objetConcurrent correspondant au concurrent le plus rapide. On suppose que la liste est non vide. Recopier et compléter l »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 8. Proposer une requête qui renvoie l es prénoms, par ordre alphabétique, des enfants inscrits pour le parent dont le numéro de téléphone est 3619861122. »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « a. En utilisant l'extrait de la table de routage de R1, vers quel routeur R1 envoie- t-il ce paquet : R2 ou R3 ? Justifier. »
    exemple réel (autre notion) : « 10. Indiquer de quel type de parcours il s'agit. EN_NOzUzMD2M0ODAczOT5UzMmTYxMj2A2MDEO2OTiQyNQTgx »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 10. Indiquer quel type de parcours donnerait, dans cet ordre : IA, bot, programmation, algo, chatbot, informatique, python. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C6 : Établir ou lire une table de routage — Majoritairement réseau : dresser, compléter ou exploiter une table de routage selon un protocole (RIP/OSPF), ou identifier un chemin ; on évalue l'application d'un protocole à une topologie.
    gabarit : Donner la [table/chemin] [de l'élément] selon [protocole/règle], après [événement].
    exemple réel (autre notion) : « 2. Donner la liste des six chemins possibles que peut emprunter ce paquet. »
    détail du cours à évaluer (Recursivite) : « Écrire une fonction _imperatif(n) qui calcule de façon directe (*impérative*) le n-ième terme de la suite de Fibonacci. »

Le champ id vaut « I-paradigmes ».