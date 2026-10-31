# Plan I-representation_nombres (inedit)

Notion : representation_nombres (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Architecture, OS et réseaux > Routage > Routage]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 15 - Le routage
> Objectifs :
> ▷ Connaître les principaux protocoles de routage
> ▷ Identifier, suivant le protocole de routage utilisé (RIP ou OSPF), la route empruntée par un paquet.
> 1 Introduction
> Exemple
> Thomas veut envoyer une lettre de remerciement à son amiPacôme Toullemonde, habitant à Toulouse
> (en France), qui lui a prété un manuel de NSI.
> 1. Il rédige donc un courrier, le place dans une enveloppe sur laquelle il inscrit le nom, le prénom, le
> numéro, la rue, le code postal, la ville et enfin le pays.
> 2. Puis il dépose le tout à la poste deSerangoon à Singapour.
> 3. L'agent de la poste ne connaît pasPacôme, mais il sait que la lettre doit aller en France.
> 4. Une fois arrivée en France, l'agent de poste Français ne connaît toujours pasPacôme, mais il sait
> qu'il doit envoyer la lettre vers un nouveau centre de tri, celui de Toulouse.
> 5. A
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
    manière de demander C22 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes précisément numérotées d'une fonction à trous ; on évalue la compréhension de la logique locale du code et le respect de la spécification.
    gabarit : Recopier et compléter les lignes [n1] à [n2] de la fonction [nom] afin qu'elle [comportement].
    exemple réel (autre notion) : « 3. Recopier et compléter les lignes 4, 7 et 8 du code de la fonction lancer_possible ci-dessous. Elle prend en argument un tableau etat représentant un état et un entier lancer , et renvoie True si le lancer est possible, et False sinon.  1 »
    exemple réel (autre notion) : « 9. Copier et compléter les lignes 6 et 7 de cette fonction. »
    support S0 : Énoncé en prose avec numéros — Support textuel ordinaire mêlant prose et nombres (routeurs, adresses, tailles) ; l'élève travaille à partir d'une mise en situation décrite, sans matériau structuré dominant.
    exemple de support (autre notion) : « 17. Recopier et compléter la ligne 35 du code de la fonction rechercher. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « 10. Expliquer en quoi la fonction inserer est une fonction récursive. »
    exemple réel (autre notion) : « 3. Expliquer ce que fait la requête SQL suivante.   UPDATE Piece  SET langue = "Anglais"  WHERE langue = "Américain" OR langue = "Britannique"; »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 3. Déterminer le nombre de comparaisons effectuées par l'appel effectif(1, [1, 4, 1, 6, 1, 7, 2, 1, 1]). »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C15 : Proposer une solution ou modification — L'élève propose une solution ouverte (parcours, fonction, modification de schéma, adresses, tests) ; on évalue la capacité à concevoir une réponse valide parmi plusieurs possibles.
    gabarit : Proposer [un/une] [solution/modification/test] permettant de [objectif] en respectant [contrainte].
    exemple réel (autre notion) : « 11. Proposer une modification de la méthode jouer à partir de la ligne 8 afin de prendre en compte cette optimisation.  EN_NOzUzMD2M0ODAczOT5UzMmTYxMj2A2MDEO2OTiQyNQTgx »
    exemple réel (autre notion) : « 6. On peut proposer ce nouvel algorithme : − Etape 1 : la personne déplace l'annonce vers son répertoire p ersonnel ; − Etape 2 : la personne ouvre, modiﬁe et enregistre le ﬁchier da ns son répertoire personnel ; − Etape 3 : le ﬁchier modiﬁ »
    support S0 : Énoncé en prose avec numéros — Support textuel ordinaire mêlant prose et nombres (routeurs, adresses, tailles) ; l'élève travaille à partir d'une mise en situation décrite, sans matériau structuré dominant.
    exemple de support (autre notion) : « 5. Écrire une requête permettant d'ajouter ce champignon avec l'id 56 dans la table champignon. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C19 : Déterminer un chemin ou élément — Questions de détermination (chemin d'un paquet, répertoire, sous-séquence, protocole) sans geste unique, souvent en réseau ; on évalue une déduction à partir du contexte.
    gabarit : Déterminer [le chemin/l'élément] [de A à B / vérifiant la condition] dans [situation].
    exemple réel (autre notion) : « 4. La liaison entre R4 et R6 est rétablie. Par ailleur s, on décide d'utiliser le protocole OSPF (distance liée au coût  minimal des liaisons) pour effectuer le routage. L e coût  des liaisons entre les routeurs est conditionné par la ban »
    détail du cours à évaluer (Protocoles de routage) : « Par exemple, si le débit d est exprimé en bits/s, on peut calculer le coût de chaque liaison par la formule : »

Le champ id vaut « I-representation_nombres ».