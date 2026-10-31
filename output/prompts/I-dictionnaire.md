# Plan I-dictionnaire (inedit)

Notion : dictionnaire (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Structures donnees > Structures donnees]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 4 - Les structures de données
> Objectifs :
> ▷ Remettre en mémoire les structures de données vues enPremière
> ▷ Montrer qu'il existe plusieurs implémentations possibles
> 1 Introduction
> En informatique, on manipule essentiellement des données. Lorsqu'elles sont simples comme desnombres,
> des chaînes de caractères ou des booléens, on peut les stocker dans des variables qui seront typées en
> fonction de la nature de la donnée.
> 2 Définition
> A retenir!
> Une structure de données est une organisation logique des données permettant de simplifier ou
> d'accélérer leur traitement.
> 3 Exemple
> Par exemple, si on a écrit un code avec les affectations suivantes :
> 1 n = 4
> 2 p = -5
> 3 r = 0.7
> 4 phrase = 'hello'
> 5 test = True
> Python est un langage avec untypage dynamique, c'est-à-dire que le type de la variable est automa-
> tiquement déterminé la première fois qu'elle
> [Structures de données > Dictionnaires > 3. Retour aux dictionnaires]
> Quel est le lien entre les fonctions de hachage et les  dictionnaires ??? 
> 
> L'idée essentielle est que chaque clé est hachée pour donner une empreinte unique, qui est ensuite transformée en un indice de positionnement dans un tableau.
> 
> Le dictionnaire :
> 
> ```python
> d = {"pommes":3, "poires":0, "bananes":5}
> ```
> 
> serait donc par exemple implémenté dans un tableau comme celui-ci :
> 
> On peut remarquer que ce tableau laisse beaucoup de cases vides.
> 
> Si je souhaite ensuite accéder à l'élément ```d["kiwis"]``` :
> 
> - le hash de la chaîne ```"kiwis"``` est calculé. Par exemple, ```4512d2202```.
> - l'indice de la position (éventuelle) de la clé ```"kiwis"``` dans mon dictionnaire est calculé à partir de ce hash ```4512d2202```. Dans notre exemple, cela pourrait donner l'indice 3.
> - Python accède **directement** à cet indice du tableau :
>     - si la valeur de la clé sur cette ligne du tableau est None,

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C1 : Écrire la fonction ou commande nommée — L'élève produit un code précis (fonction, méthode, commande shell) dont le nom est imposé. On évalue la justesse et la syntaxe du code écrit.
    gabarit : Écrire la [fonction|méthode|commande] [nom] qui [comportement attendu].
    exemple réel (autre notion) : « 9. Écrire la fonction choose_interface(t_routage, destination_ip) qui prend en paramètres un tableau t_routage qui modélise une table de routage et un quadruplet destination_ip qui représente une a dresse IP, et qui renvoie l'interface de s »
    exemple réel (autre notion) : « 4. Écrire la méthode ajouter permettant d'ajouter un objet de type Personne à la liste du personnel de l'entreprise de la classe Personnel. »
    support S13 : Listes et tableaux de nombres — Littéraux Python de listes ou matrices d'entiers, doctests. L'élève s'en sert comme données d'entrée ou de vérification.
    exemple de support (autre notion) : « 6. Déterminer la liste auxiliaire aux_B associée à la carte représentée par carte_B.  carte_B = [  [1, 1, 1, 1],  [0, 1, 1, 1],  [0, 1, 1, 1],  [1, 0, 1, 1], ] On considère une carte carte_C de taille 6 ainsi que la liste auxiliaire aux_C associée. Seules cert »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 2) Après exécution du programme Programme 1, voici le début de l'affichage obtenu :   [{'dep': '56',  'nom': 'Lorient',  'nb_hab_1999': '59224',  'nb_hab_2012': '58100',  'densite': '3272',  'superficie': '17.48',  'alt_min': '0',  'alt_max »
    exemple réel (autre notion) : « 6. Expliquer pourquoi la fonction ci -dessous renvoie effectivement la distance entre les deux mots mot1 et mot2, deux chaines de quatre caractères.  1. def distance(mot1, mot2): 2. tab = chaine_vers_tab(mot1) 3. for lettre in mot2: 4. if l »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 1. L'attribut titre peut-il être une clé primaire pour la table Chanson ? Justifier. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C17 : Question directe « quelle est » — L'élève indique une valeur, une propriété ou un élément d'une structure. Réponse courte ; le groupe reste un peu hétérogène.
    gabarit : Quelle est la [valeur|propriété] de [objet] ?
    exemple réel (autre notion) : « 1. Parmi les propositions suivantes, quelle est la structure de données la plus appropriée pour mettre en œuvre le mode FIFO (First In First Out) ? a) liste b) dictionnaire c) pile d) file »
    exemple réel (autre notion) : « b) Écrire l'instruction permettant d'accéder à la valeur " 7 " stockée dans cette variable. »
    support S2 : Prose sur un modèle relationnel — Texte court sur une base de données (clés, relations, suppression). L'élève raisonne sur le schéma décrit.
    exemple de support (autre notion) : « d. SID »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 1. L'attribut masse de la relation Exoplanetes ne peut pas servir de clé primaire de cette relation car il n'est pas unique, plusieurs exoplanètes peuvent avoir la mê me masse, p.ex celles d' id_exoplanete 6 et 7. »
    détail du cours à évaluer (Dictionnaires) : « Lors du transit du mot de passe, le chiffrement effectué par le protocole »

Le champ id vaut « I-dictionnaire ».