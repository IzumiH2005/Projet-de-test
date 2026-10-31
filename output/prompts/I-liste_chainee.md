# Plan I-liste_chainee (inedit)

Notion : liste_chainee (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Listes Piles Files > 3.2 Implémentation(s) d'une pile]
> L'objectif est de créer une classe ```Pile```. L'instruction  ```Pile()```  créera une pile vide. Chaque objet ```Pile``` disposera des méthodes suivantes :
> 
> - ```est_vide``` : indique si la pile est vide (renvoie un booléen)
> - ```empile``` : insère un élément (passé en paramètre) en haut de la pile. Ne renvoie rien.
> - ```depile``` : renvoie la valeur de l'élément en haut de la pile ET le supprime de la pile.
> 
> Ces 3 méthodes sont essentielles et se retrouveront systématiquement dans chaque interface. Nous y ajouterons, uniquement par commodité, la méthode suivante :
> 
> - ```__repr__``` : permet d'afficher la pile sous forme agréable (par ex : ```|3|6|2|5|```)
> 
> #### 3.2.1 À l'aide du type ```list``` de Python 
> {#
> 
>     Créer la classe ```Pile```   ci-dessus. 
>     
>     Le type ```list``` de Python est parfaitement adapté. Des renseignements intéressants à son sujet peuvent être trouvés ici.
> 
> 
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

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « 7. Recopier et compléter les lignes 3, 5 et 6 de le fonction degre qui prend en paramètre la matrice d'adjacence d'un graphe donné sous forme d'une liste de listes et qui renvoie la liste des degrés de tous les sommets du graphe rangés dans »
    exemple réel (autre notion) : « 6. Compléter les lignes 9 et 14 du code précédent pour que la méthode empiler permette d'empiler un élément elt dans une pile et que la méthode depiler permette de dépiler une pile en renvoyant l'élément dépilé. Vous n'écrirez que le code d »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 2. Codage des entiers relatifs : Pour effectuer la soustraction sur 8 bits : 65 – 58, un processeur effectue l'addition : 65 + (-58) où -58 est obtenu par la méthode du complément à deux. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 8. Rappeler brièvement ce qu'est un algorithme de chiffrement asymétrique. On suppose à présent que Bob possède une clé publique et une clé privée. La clé publique de Bob est supposée connue par le serveur. »
    exemple réel (autre notion) : « 9. Proposer alors une solution pour que le serveur puisse envoyer la clé C à l'ordinateur de Bob de façon sécurisée, c'est-à-dire pour que seul Bob puisse déchiffrer la clé envoyée. »
    support S10 : Prose riche en virgules — Phrases longues avec énumérations par virgules ou listes de choix. Artefact de ponctuation, contenus variés.
    exemple de support (autre notion) : « 2. Dans un premier temps, les tables de routage des routeurs sont configurées manuellement (voir figure 2).  Routeur R1 Destination Suivant SiteA Local SiteB R2 SiteC R3 SiteD R3  Routeur R2 Destination Suivant SiteA R1 SiteB Local SiteC R3 SiteD R3  Routeur R »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C11 : Analyser une ligne de code précise — L'élève explique ou corrige le rôle d'une ligne désignée dans un programme fourni. On évalue la lecture fine du code.
    gabarit : Expliquer le rôle de la ligne [n] de la fonction [nom].
    exemple réel (autre notion) : « 6. Recopier et compléter la ligne 3 du code ci-dessous afin que n soit égal au nombre total d'éléments nécessaires dans le dictionnaire dmateriel. »
    exemple réel (autre notion) : « 11. Compléter la ligne 5 de la fonction montant_a_regler. 1 def montant_a_regler(triplet): 2 """ renvoie le montant en euros 3 à régler pour cette réservation """ 4 client, reservation, emplacement = triplet 5 return ....................... »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 9. Recopier et compléter les lignes 5 et 6 de cette fonction afin qu'elle renvoie la distance attendue. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 4) Écrire un programme en langage Python permettant :  a) la création d'une instance lancelot de cette classe ayant pour attributs 5,5,5 en coordonnées, 15 en point_de_vie et 3 en point_degats.  b) la création d'une instance sorcier de cett »
    détail du cours à évaluer (Les listes) : « On a donc affaire à une chaîne de cellules qu'on appelle plus couramment uneliste chaînée. »

Le champ id vaut « I-liste_chainee ».