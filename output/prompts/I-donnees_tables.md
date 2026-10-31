# Plan I-donnees_tables (inedit)

Notion : donnees_tables (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Bases de données > Langage SQL > Exercices SQL débranchés]
> *(d'après Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.)*
> 
>     On veut créer une base de données ```baseHopital.db```  qui contiendra les trois tables suivantes :
> 
>     |  | Patients |
>     |-----|----|
>     | id | ```Int```  |
>     | nom | ```Text```  |
>     | prenom | ```Text```  |
>     | genre | ```Text```  |
>     | annee_naissance | ```Int```  |
> 
>     |  | Ordonnances |
>     |-----|----|
>     | code | ```Int```  |
>     | id_patient | ```Int```  |
>     | matricule_medecin  | ```Int```  |
>     | date_ord | ```Text```  |
>     | medicaments | ```Text```  |
> 
>     |  | Medecins |
>     |-----|----|
>     | matricule | ```Int```  |
>     | nom_prenom | ```Text```  |
>     | specialite | ```Text```  |
>     | telephone | ```Text```  |
> 
>     On suppose que les dates sont données sous la forme ```jj-mm-aaaa```.
> 
>     On donne le diagramme relationnel de cette base :
>     
>     
>    
> [Structures de données > Dictionnaires > 2.1 Vérification de l'intégrité]
> Lorsque vous téléchargez un fichier important et que vous souhaitez vérifier qu'il n'a pas été corrompu lors du téléchargement (ou avant), vous avez parfois la possibilité de vérifier l'intégrité de votre fichier téléchargé, en calculant une «empreinte» de votre fichier et en la comparant avec celle que vous êtes censée obtenir :
> 
> Voilà par exemple ce qui apparaît sur la page de téléchargement d'une iso d'ubuntu 18.04 :
> 
> La clé MD5 proposée pour chaque fichier est le résultat ce que **doit** donner le fichier (ici une iso d'environ 1,9 Go) lorsqu'il est «haché» par la fonction MD5. Dans notre cas, si nous téléchargeons 
> ```ubuntu-18.04.3-desktop-amd64.iso```, nous devons calculer l'empreinte du fichier téléchargé et vérifier que nous obtenons bien ```72491db7ef6f3cd4b085b9fe1f232345``` :
> 
> Essayons :
> 
> La clé calculée sur l'ordinateur correspond bien à celle indiquée sur le site de télécha

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C22 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes précisément numérotées d'une fonction à trous ; on évalue la compréhension de la logique locale du code et le respect de la spécification.
    gabarit : Recopier et compléter les lignes [n1] à [n2] de la fonction [nom] afin qu'elle [comportement].
    exemple réel (autre notion) : « 10. Recopier et compléter les huit lignes 24, 29, 30, 31, 32, 33, 36, et 37 du code de la méthode index_insertion_element qui prend en paramètre un élément element et qui renvoie la position d'insertion de l'élément element en utilisant une »
    exemple réel (autre notion) : « 10. Recopier et compléter les lignes 9 et 11 du code de la fonction récursive shannon qui prend en paramètres un caractère symbole et un tableau trié tab et qui renvoie l'écriture binaire associée à symbole dans le tableau tab.  1 def shann »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 10. On complète la méthode index_insertion_element. 17 def index_insertion_element(self, element): 18 """Renvoie la position/index d'insertion 19 d'element dans liste_priorite triée 20 par ordre décroissant 21 de numéro de priorité 22 """ 23 if self .est_vide( »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 7. Écrire une fonction temps_course qui prend pour paramètre equipe de type Equipe et qui renvoie un nombre flottant correspondant au cumul des temps de l'équipe equipe à l'issue des 9 étapes de la course. On rappelle que la classe Equipe d »
    exemple réel (autre notion) : « 10. Écrire une fonction gagne qui prend comme argument un état et qui renvoie True si la partie est terminée et False sinon. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 3. On se propose maintenant d'écrire une fonction parcourir_pile_en_reduisant qui parcourt la pile du haut vers le bas en procédant aux réductions pour chaque triplet rencontré quand cela est possible. »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : milieu d'exercice
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « a. Appliquer sur votre copie, de la même façon que dans l'exemple précédent, le déroulement de l'algorithme pour la liste suivante : [46, 108, 55, 53]  On rappelle que l'appel L.append(x) ajoute l'élément x à la fin de la liste L et que len »
    exemple réel (autre notion) : « 2. Réécrire cette instruction en la corrigeant pour que la liste valeurs contienne bien les entiers de 1 à 16. »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 7. Écrire la fonction decompChiffre qui prend en paramètre un entier n compris entre 0 et 19 et renvoie la liste [c, p, t] où c vaut 0 ou 1 et indique la présence ou non d'une coquille, p est le nombre de points et t le nombre de traits composant le "chiffre"  »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « b. Indiquer quelle condition simple (sur le contenu de la pile) permet alors de dire que le balisage est correct lorsque toute l'expression HTML simplifiée a été entièrement parcourue, sans que l'analyse ne s'arrête. »
    détail du cours à évaluer (Dictionnaires) : « La clé MD5 proposée pour chaque fichier est le résultat ce que doit donner le fichier (ici une iso d'environ 1,9 Go) lorsqu'il est "haché" par la fonction MD5. »

Le champ id vaut « I-donnees_tables ».