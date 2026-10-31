# Plan I-securite_crypto (inedit)

Notion : securite_crypto (Architecture, OS et réseaux) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Architecture, OS et réseaux > Cryptographie > 2.3 Un exemple de chiffrement asymétrique : le chiffrement RSA]
> #### 2.3.1 Histoire
> Lorsqu'en 1976 Diffie et Hellman (chercheurs à Stanford) présentent le concept de chiffrement asymétrique (souvent appelé _cryptographie à clés publiques_), ils en proposent uniquement un modèle théorique, n'ayant pas trouvé une réelle implémentation de leur protocole.
> 
> Trois chercheurs du MIT (Boston), Ron Rivest, Adi Shamir et Len Adleman se penchent alors sur ce protocole, convaincus qu'il est en effet impossible d'en trouver une implémentation pratique. En 1977, au cours de leurs recherches, ils démontrent en fait l'inverse de ce qu'ils cherchaient : ils créent le premier protocole concret de chiffrement asymétrique : le chiffrement **RSA**.
> 
> Au même moment à Londres, Clifford Cocks, (chercheur au très secret GCHQ) apprend que Rivest Shamir et Adleman viennent de découvrir ce que lui-même a découvert **3 ans auparavant** mais qui est resté classé Secret Défense.
> 
> 
> [Architecture, OS et réseaux > Cryptographie > 2.2 Le rôle interchangeable des clés publiques et privées]
> L'illustration précédente associe :
> 
> - une image de cadenas à la clé publique (car on s'en sert pour chiffrer les messages)
> - une image de clé à la clé privée (car on s'en sert pour déchiffrer les messages)
> 
> Concrètement, (nous le verrons dans l'application par le chiffrement RSA), la clé privée et la clé publique sont **deux nombres** aux rôles identiques. Appelons-les A et B :
> 
> - il est impossible de trouver A en fonction de B. Réciproquement, si on connaît A, il est impossible d'en déduire B.
> - si on chiffre un message avec A, on peut le déchiffrer avec B. Réciproquement, si on chiffre avec B, on peut déchiffrer le message grâce à A.
> - on peut donc chiffrer avec une clé publique et déchiffrer avec la clé privée associée (ce qui est fait dans l'exemple précédent). Mais on peut aussi chiffrer avec la clé privée, et déchiffrer avec la clé publique associée.
> 
> A et B ont donc des rôles int

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C11 : Traiter des chaînes de caractères — Questions de programmation ou d'analyse portant sur des chaînes (parcours, inversion, validation, exemple qui fait échouer un test) ; on évalue la manipulation de caractères et d'indices.
    gabarit : Écrire une fonction [nom] qui prend en paramètre une chaîne de caractères [s] et renvoie [résultat]. Exemple : [nom]([entrée]) renvoie [sortie].
    exemple réel (autre notion) : « 6. La classe Date dispose d'une méthode est_bissextile, q ui utilise uniquement l'attribut annee, et qui renvoie True si l'année de l'instance courante est bissextile et False sinon. On veut compléter la méthode init pour ajuster le nombre  »
    exemple réel (autre notion) : « 9. Donner la table de codage pour la chaîne de caractères txt. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 9. L'arbre peut être parcouru selon l'ordre de parcours préfixe, infixe, suffixe ou en largeur d'abord. Indiquer celui qui permet de lire les numéros des sondes dans l'ordre croissant des numéros de série. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C23 : Donner une information précise — Restitution courte (nom d'un algorithme, coût, adresse, masque, type) ; on évalue une connaissance ou un calcul ponctuel.
    gabarit : Donner le [nom/coût/valeur] [de l'élément] [dans le contexte].
    exemple réel (autre notion) : « 7. Donner le coût d'exécution temporel de la méthode prediction en fonction de la taille 𝑛 des entrées. »
    exemple réel (autre notion) : « a. Ecrire une requête SQL permettant d'afficher le nom des plats, leur type et leur prix. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « a. Donner l'ordre d es indices de priorité obtenus à l'aide d'un parcours infixe de l'arbre binaire de recherche de la figure 1. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « 2. On considère que le coût en temps du bloc manquant est constant. Quelle est la complexité de la fonction plus_proche_voisin quand ݇1 ? Dans la suite, on suppose que ≥ 1. »
    exemple réel (autre notion) : « 1. a. Quelles sont les adresses des réseaux locaux L1 et L2 ? »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 15. Donner la représentation décimale de ce masque de sous-réseau. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « 7. Montrer qu'il est possible que : • arret_essai2(programme) renvoie True alors que le programme ne s'arrête pas; • arret_essai2(programme) renvoie False alors que le programme s'arrête. Indication : il n'y a pas que les boucles while qui  »
    détail du cours à évaluer (Cryptographie) : « Un chiffrement est dit symétrique lorsque la connaissance de la clé ayant servi au chiffrement permet de déchiffrer le message. »

Le champ id vaut « I-securite_crypto ».