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
> [Architecture, OS et réseaux > Securisation > Securisation]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 19 - Sécurisation des communications
> Objectifs :
> ▷ Décrire les principes de chiffrement symétrique et asymétrique (avec clef privée/clef publique).
> ▷ Décrire l'échange d'une clef symétrique en utilisant un protocole asymétrique pour sécuriser une commu-
> nication HTTPS.
> 1 Introduction
> Pour qu'un message entre deux machines dans un réseau informatique ne puisse pas être compréhensible s'il est
> intercepté, il faut qu'il soitchiffré.
> A retenir!
> Il y a deux manières principales pourchiffrer un message:
> ▷ par unchiffrement symétriquequi utilise une clé unique, connue seulement de l'émetteur et du
> récepteur. L'émetteur chiffre le message avec la clé et le récepteur le déchiffre avec la même clé.
> ▷ par unchiffrement asymétriquequi utilise un couple de clés, l'une publique connue de tout le
> monde, l'autre privée connue uniquement par le récepteur.

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Donner le nom ou l'instruction — L'élève nomme un élément ou fournit une instruction ou un tuple précis. On évalue une réponse courte et exacte.
    gabarit : Donner le [nom|tuple|instruction] correspondant à [situation].
    exemple réel (autre notion) : « 1. Représenter le parcours effectué par le robot s'il reçoit la chaîne ‘4(AG)'. »
    exemple réel (autre notion) : « 8. Écrire une requête SQL renvoyant le numéro de dossard, le nom, le prénom et le temps de course de ces participantes classées par temps de course croissant. »
    support S4 : Prose multi-lignes sans forme distinctive — Texte d'énoncé courant sur plusieurs lignes, sujets divers (algorithmes, graphes, Huffman). Forme générique, pas de matériau spécifique.
    exemple de support (autre notion) : « 8. Préciser à quel type d'algorithme vu en cours cette stratégie fait référence. Pour le moment, on suppose que la fonction clefs_triees_selon_volume prend en paramètre un dictionnaire dmatos contenant le matériel et renvoie la liste des clefs de dmatos triée  »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C1 : Écrire la fonction ou commande nommée — L'élève produit un code précis (fonction, méthode, commande shell) dont le nom est imposé. On évalue la justesse et la syntaxe du code écrit.
    gabarit : Écrire la [fonction|méthode|commande] [nom] qui [comportement attendu].
    exemple réel (autre notion) : « 9. Écrire la méthode multiplie de la classe Maya qui renvoie le résultat de la multiplication par 20 d'un nombre en modélisation Maya. »
    exemple réel (autre notion) : « b. Ecrire la fonction récursive numerotation qui parcourt l'arbre et modifie l'attribut generation de tous les ancêtres d'Albert Normand, de sorte que les parents d'Albert Normand soient la génération 1 etc… Cette fonction prend en paramètr »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 3. Écrire une fonction compte_fermante qui prend en paramètre une chaine de caractères txt et qui renvoie le nombre de parenthèses fermantes qu'il contient. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C17 : Question directe « quelle est » — L'élève indique une valeur, une propriété ou un élément d'une structure. Réponse courte ; le groupe reste un peu hétérogène.
    gabarit : Quelle est la [valeur|propriété] de [objet] ?
    exemple réel (autre notion) : « 1. Trouver la valeur exprimée en hexadécimal de la clé qui sera associée au mot 'EW'. »
    exemple réel (autre notion) : « d. ls »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 2. Donner et expliquer la valeur de l'expression a2.voisines[2][1]. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 3. La différence de hauteur entre l'ABR a1 et l'ABR a2 aura des conséquences lors de la recherche d'une valeur dans l'ABR. »
    détail du cours à évaluer (Cryptographie) : « Un chiffrement est dit symétrique lorsque la connaissance de la clé ayant servi au chiffrement permet de déchiffrer le message. »

Le champ id vaut « I-securite_crypto ».