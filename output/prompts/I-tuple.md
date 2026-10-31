# Plan I-tuple (inedit)

Notion : tuple (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Programmation objet > Programmation objet]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 3 - Programmation orientée objet
> Objectifs :
> ▷ Connaître le vocabulaire de la programmation objet : classes, attributs, méthodes, objets.
> ▷ Ecrire la définition d'une classe
> ▷ Accéder aux attributs et méthodes d'une classe.
> 1 Introduction
> Jusqu'à présent nous avons utilisé des objets dont le type est prédéfini :int, float, bool, str, list,
> tuple, dict. Sans le savoir, nous avons découvert les concepts de laprogrammation orientée objet
> ou POO. Ainsi, en classe de Première, nous avions déjà appris à utiliser des méthodes associées à ces
> types, comme :
> ma_liste.append(valeur)
> Comme de nombreux autres langages tels queJava ou C++, Python est un langage orienté objet .
> On peut donc dire que tout y estobjet. Une variable de typeint est en fait un objet de typeint donc
> construit à partir de la classeint. Idem pour lesfloat et str. Mais également
> [Structures de données > Les listes > Les listes]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 5 - Les listes
> Objectifs :
> ▷ Distinguer des structures par le jeu des méthodes qui les caractérisent.
> ▷ Choisir une structure de données adaptée à la situation à modéliser.
> ▷ Distinguer la recherche d'une valeur dans une liste et dans un dictionnaire.
> 1 Introduction
> Historique
> Le langage de programmationLisp (inventé parJohn McCarthy en 1958) a été un des premiers langages
> de programmation à introduire cette notion de liste (Lisp signifie list processing).
> Lisp qui fait partie de la plus ancienne famille de langages de programmation à la fois impératifs et
> fonctionnels, est devenu dans les années 1970-80 le langage de choix pour la recherche en intelligence
> artificielle. Ils sont aujourd'hui utilisés dans de nombreux domaines, de la programmation Web à la
> finance.
> Python abuse du terme liste qu'il utilise pour ce qui sont destableaux dyna

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C12 : Exploiter l'élément fourni ci-dessous — La consigne renvoie à un document joint (commandes, circuit, requêtes numérotées, classe, code) à sélectionner, compléter ou utiliser ; on évalue la lecture attentive du support plus qu'une notion précise.
    gabarit : Parmi les [éléments] ci-dessous, [sélectionner/compléter/utiliser] ceux qui permettent de [objectif].
    exemple réel (autre notion) : « 2. Ravel, un nouveau fabricant, a livré à l'entreprise 10 vélos du modèle 'Bovelo'. Parmi les cinq requêtes numérotées ci-dessous, en sélectionner deux qui permettent d'intégrer cette nouvelle information et indiquer l'ordre dans lequel ell »
    exemple réel (autre notion) : « a. Écrire ce que renvoie la requête ci-dessous :  SELECT nom, prenom, naissance FROM individu WHERE nom = 'Crog';  b. Fournir une requête SQL permettant de récupérer le titre et la clé primaire de chaque film dont la date de sortie est stri »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 6. Écrire le résultat obtenu suite à l'exécution de la requête suivante si on l'applique sur les extraits des tables donnés.  SELECT nomSc FROM plante JOIN zone_geographique ON plante.zone = zone_geographique.num WHERE zone_geographique.zone = 'Asie' »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C22 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes précisément numérotées d'une fonction à trous ; on évalue la compréhension de la logique locale du code et le respect de la spécification.
    gabarit : Recopier et compléter les lignes [n1] à [n2] de la fonction [nom] afin qu'elle [comportement].
    exemple réel (autre notion) : « 7. Recopier et compléter les lignes 4 et 10 pour compléter le code de la fonction regle1. Règle 2 : S'il n'y a qu'un seul nombre impair dans une ligne ou une colonne dont la cible est paire, on peut éliminer ce nombre impair. Par exemple, p »
    exemple réel (autre notion) : « 9. Recopier et compléter les lignes 10, 12, 14 et 15 de cette fonction. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 9. Recopier et compléter les lignes 5 et 6 de cette fonction afin qu'elle renvoie la distance attendue. »

- slot 3 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 8. Écrire une fonction voisins qui prend en paramètres un graphe G et un sommet s du graphe G et qui renvoie la liste des voisins du sommet s. »
    exemple réel (autre notion) : « c. Écrire en Python une fonction defiler(f) qui prend en argument un couple de piles f et qui renvoie l'élement en tête de la file représentée par f en le retirant.  ps5 ps4 ps1 ps3 ps2 p1 p2 Annexe A de l'exercice 3 Tables de routage du ré »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 5. À l'aide des classes Bloc et Blockchain, écrire le code Python permettant de créer un objet ma_blockchain de type Blockchain représenté par la figure 1. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C3 : Questions de raisonnement hétérogènes — Mélange de consignes (dessiner un graphe, comparer, justifier, lister des dépendances) liées par des tournures pluriel génériques ; le point commun est seulement un raisonnement contextualisé sur une situation.
    gabarit : En étudiant [situation/données], [donner/comparer/justifier] [élément demandé]. Justifier la réponse.
    exemple réel (autre notion) : « 12. Donner un avantage et un inconvénient des deux approches utilisées pour classer les athlètes :  Utiliser des dictionnaires et un tri  Utiliser un arbre binaire de recherche approche objet avec insertion dans un arbre binaire  EN_NOzUz »
    détail du cours à évaluer (Routage) : « Un vecteur de distance est un couple (adresse, distance). »

Le champ id vaut « I-tuple ».