# Plan I-calculabilite (inedit)

Notion : calculabilite (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Notion de programme > Notion de programme]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 25 - Calculabilité, décidabilité
> Objectifs :
> ▷ Comprendre que tout programme est aussi une donnée.
> ▷ Comprendre que la calculabilité ne dépend pas du langage de programmation utilisé.
> ▷ Montrer, sans formalisme théorique, que le problème de l'arrêt est indécidable.
> 1 Introduction
> Comme nous l'avons vu en classe dePremière, un programme est la traduction électronique d'un algorithme
> afin qu'il puisse être compris par une machine. Dans ce chapitre, nous allons montrer qu'un programme ne peut
> pas toutcalculer ou décider.
> L'indécidabilité est un concept fondamental en logique. Il a plusieurs sens. Au sens de la démonstration, il
> signifie qu'on ne peut démontrer ni qu'une proposition est vraie ni qu'elle est fausse dans un système d'axiomes;
> ici, le contenu sémantique ne permet d'affirmer ni que l'objet est une pipe ni qu'il n'en est pas une. 
> [Programmation > Calculabilite Decidabilite > 2.5 Conclusion]
> Nous venons de prouver que notre programme ```halt```, censé prédire si un programme ```prog``` peut s'arrêter sur une entrée ```x```, **NE PEUT PAS EXISTER**.
> 
> Ce résultat théorique, d'une importance cruciale, s'appelle **le problème de l'arrêt**.
> 
>     Il **ne peut pas exister** de programme universel qui prendrait en entrées :
> 
>      - un programme P 
>      - une entrée E de ce programme P
> 
>     et qui déterminerait si ce programme P, lancé avec l'entrée E, va s'arrêter ou non. 
> 
> Ce résultat a été démontré par Alan Turing en 1936, dans un article intitulé *«On computable numbers, with an application to the Entscheidungsproblem»*.
> 
> Pour sa démonstration, il présente un modèle théorique de machine capable d'exécuter des instructions basiques sur un ruban infini, les machines de Turing.
> 
> À la même époque, le mathématicien Alonzo Church démontre lui aussi ce théorème de l'arrêt, mais par un m

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C12 : Exploiter l'élément fourni ci-dessous — La consigne renvoie à un document joint (commandes, circuit, requêtes numérotées, classe, code) à sélectionner, compléter ou utiliser ; on évalue la lecture attentive du support plus qu'une notion précise.
    gabarit : Parmi les [éléments] ci-dessous, [sélectionner/compléter/utiliser] ceux qui permettent de [objectif].
    exemple réel (autre notion) : « 1. Le labyrinthe ci-dessous est censé être représenté par le tableau de tableaux lab2. Cependant, dans ce tableau, un mur se trouve à la place du départ du labyrinthe. Donner une instruction permettant de placer le départ au bon endroit dan »
    exemple réel (autre notion) : « a. Recopier et compléter le tableau ci-dessous qui dét aille le fonctionnement de cet algorithme étape par étape pour la file 2,1,3 . Une étape correspond à une modification de la pile ou de la file. Le nombre de colonnes peut bien sûr être »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 1. Donner les clés primaires des relations Films et Abonnes. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C23 : Donner une information précise — Restitution courte (nom d'un algorithme, coût, adresse, masque, type) ; on évalue une connaissance ou un calcul ponctuel.
    gabarit : Donner le [nom/coût/valeur] [de l'élément] [dans le contexte].
    exemple réel (autre notion) : « 3. Écrire en SQL les requêtes permettant d'eﬀectuer les tâches suivantes : (a) Aﬃcher le nom et le prénom de tous les abonnés. (b) Aﬃcher le titre et la durée des ﬁlms projetés le 12 octobre 2021 à21:00. On remarquera que les heures apparai »
    exemple réel (autre notion) : « 14. Donner le nom du protocole de routage qui semble être utilisé. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « 4. Écrire une requête SQL permettant d'ajouter la chanson dont le titre est Megalomania de l'album Hullabaloo du groupe Muse. »

- slot 3 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 3. Dessiner l'arbre obtenu après l'ajout de la valeur 6. »
    exemple réel (autre notion) : « 1. Si on se donne l'état e2 = [1, 1, 0, 1, 0, 0] indiquer quels sont les lancers possibles. »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 4. Recopier et compléter la méthode grille_demineur_vide de la classe Demineur qui permet d'initialiser une grille vide du jeu. EN_NOzUzMD2M0ODAczOT1UzMmTYxMj5A2MDEO2OTdQ5MLTcx  def grille_demineur_vide(self):  return [[0 for _ in range(...)] for _ in range(. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C3 : Questions de raisonnement hétérogènes — Mélange de consignes (dessiner un graphe, comparer, justifier, lister des dépendances) liées par des tournures pluriel génériques ; le point commun est seulement un raisonnement contextualisé sur une situation.
    gabarit : En étudiant [situation/données], [donner/comparer/justifier] [élément demandé]. Justifier la réponse.
    exemple réel (autre notion) : « 9. Entre le chiffrement symétrique ou asymétrique, donner en justifiant lequel des deux Alice et Bob doivent préférer utiliser pour éviter que le pirate ne puisse connaître le contenu de leurs échanges. »
    détail du cours à évaluer (Notion de programme) : « L'indécidabilité est un concept fondamental en logique. »

Le champ id vaut « I-calculabilite ».