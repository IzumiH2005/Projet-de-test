# Plan I-recherche_textuelle (inedit)

Notion : recherche_textuelle (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Recherche textuelle > Recherche textuelle]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 23 - Recherche textuelle
> Objectifs :
> ▷ Comprendre le principe de la recherche textuelle.
> ▷ Etudier l'algorithme deBoyer-Moore pour la recherche d'un motif dans un texte.
> 1 Introduction
> Tout logiciel de traitement de texte possède une fonction de recherche textuelle, permettant de trouver un mot
> ou une partie d'un mot (chaîne ou sous-chaîne). Il en est de même pour les navigateurs Internet.
> Ainsi, le raccourci clavierCTRL+F permet de rechercher dans la page la chaine"mot".
> Les algorithmes qui permettent de trouver unesous-chaîne de caractères dans une chaine de caractères plus
> grande sont des "grands classiques" de l'algorithmique. On parle aussi de recherche d'unmotif dans un texte.
> Voici un exemple. Soit le texte suivant :
> "Les sanglots longs des violons de l'automne blessent mon coeur d'une langueur monotone. Tout suffocant et
> blême, qu
> [Algorithmique > Recherche textuelle > Vers Boyer-Moore-Horspool]
> L'idée est d'améliorer le code précédent (celui on parcourt le motif à l'envers) en **sautant** directement au prochain endroit potentiellement valide. 
> 
> Pour cela on regarde le caractère ```X```  du texte sur lequel on s'est arrêté (car ```X``` n'était pas égal au caractère de rang équivalent dans le motif):
> 
> - si ```X``` n'est pas dans le motif, il est inutile de se déplacer "de 1" : on retomberait tout de suite sur ```X```, c'est du temps perdu. On se décale donc juste assez pour dépasser ```X```.
> - si ```X``` est dans le motif (sauf à la dernière place du motif !), on va regarder la place de la dernière occurence de ```X``` dans le motif et de déplacer de ce nombre, afin de faire coïncider le ```X``` du motif et le ```X``` du texte.
> 
>     
> 
>     _Vous pouvez contrôler le déroulement de l'animation en la survolant avec la souris._
> 
> On dispose de la fonction ```dico_lettres``` :
> ```pytho

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « 13. Le chemin emprunté par un paquet de données allant de l'or dinateur P1 à l'ordinateur P2 est P1-S1- R1-R2-R3-R8-R9-S2-P2. 1 »
    exemple réel (autre notion) : « 11. Dans cette question on considère que les tables de la base de données contiennent exactement ce qui est présenté dans les extraits en début d'exercice. On exécute la requête SQL : DELETE FROM produit WHERE ref_produit = 89363;. Celle -c »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « b. Le groupe est bien enregistré dans la base de données. Écrire une requête permettant d'afficher tous les albums du groupe Black Eyed Peas déjà présents dans la base de données.  La requête doit permettre d'obtenir un résultat semblable au tableau ci-dessous »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « 6. Recopier et compléter les lignes 3, 4, 5 et 7 de la fonction eff_dico suivante qui prend en paramètre une liste lst et qui renvoie un dictionnaire dont les clés sont les éléments de lst et les valeurs les effectifs de chacun de ces éléme »
    exemple réel (autre notion) : « 3. Recopier et compléter les lignes 3, 5 et 6 de la fonction score. »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 1. On insère la valeur 25 dans l'arbre, dans un nouveau nœud nommé nœud11. Recopier l'arbre binaire de recherche étudié et placer la valeur 25 sur cet arbre en coloriant en rouge le chemin parcouru. Préciser sous quel nœud la valeur 25 sera insérée et si elle  »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 8. Écrire une fonction meilleur_priorite qui renvoie None s'il n'y a plus de processus et la priorité de l'un des processus les plus prioritaires de la liste des files d'attente dans le cas contraire. 1 def meilleur_priorite(liste_files): 2 »
    exemple réel (autre notion) : « b. La fonction pgsp ci-dessous permet de déterminer la plus grande des sommes obtenues en additionnant les éléments de toutes les sous-séquences possibles du tableau lst. def pgsp(lst):  n = len(lst)  somme_max = lst[0]  for i in range(n):  »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 11. Recopier et compléter les lignes 6, 7, 13, 14 et 16 du code ci-dessous de la méthode mise_a_jour permettant de compléter automatiquement les matchs du tournoi en les mettant à jour à partir des résultats des matchs des tours précédents.  1 def mise_a_jour( »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « Question 4 Proposer la structure d'une table coordonnees dans laquelle on pourra indiquer, pour chaque élève, son adresse, son code postal, sa ville, son adresse mail. Préciser la clef primaire et/ou la clé étrangère en vue de la mise en re »
    détail du cours à évaluer (Recherche textuelle) : « Re-écrire l'algorithme précédent en s'arrêtant dès qu'une occurrence de »

Le champ id vaut « I-recherche_textuelle ».