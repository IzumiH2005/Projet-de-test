# Plan I-algo_simples (inedit)

Notion : algo_simples (Algorithmique) — questions JAMAIS POSÉES aux annales

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

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C11 : Analyser une ligne de code précise — L'élève explique ou corrige le rôle d'une ligne désignée dans un programme fourni. On évalue la lecture fine du code.
    gabarit : Expliquer le rôle de la ligne [n] de la fonction [nom].
    exemple réel (autre notion) : « 3. La ligne 18 permet de supprimer le mur Nord de cellule1. Un mur de cellule2 doit aussi être supprimé pour libérer un passage entre cellule1 et cellule2. Écrire l'instruction Python que l'on doit ajouter à la ligne 19. »
    exemple réel (autre notion) : « 5. Proposer un algorithme en langage naturel permettant de déterminer après quel mot d'un texte revenir à la ligne, étant donné une certaine justification. On attend uniquement une explication précise de l'algorithme, pas sa programmation e »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 10. Compléter le code de la fonction Python renote_express2 pour qu'elle calcule la même chose que renote_express. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 3. Recopier et compléter le code de la méthode est_terminee de la classe Tache qui renvoie True si la tâche est terminée, ou False sinon.  1 def est_terminee(self): 2 ... »
    exemple réel (autre notion) : « 2. On considère la classe Noeud définie de la façon suivante en Python : 1 class Noeud: 2 def init(self, g, v, d): 3 self.gauche = g 4 self.valeur = v 5 self.droit = d »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 6. On considére I'arbre binaire de recherche ci-dessous : »

- slot 3 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C1 : Écrire la fonction ou commande nommée — L'élève produit un code précis (fonction, méthode, commande shell) dont le nom est imposé. On évalue la justesse et la syntaxe du code écrit.
    gabarit : Écrire la [fonction|méthode|commande] [nom] qui [comportement attendu].
    exemple réel (autre notion) : « 7. Écrire la méthode get_note de la classe Livre. Cette méthode devra renvoyer la note d'un livre. »
    exemple réel (autre notion) : « 2. Écrire la méthode set_couleur de la classe Piste qui permet d'affecter à l'attribut couleur la chaîne de caractères correspondant à la couleur de la piste. »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 2. Expliquer quelles données n'auraient pas pu être stockées dans la table match si le champ id_match n'avait pas été introduit dans cette table. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « a. Indiquer le chemin emprunté par un message d'un ordinateur du réseau F à destination d'un ordinateur du réseau I. Justifier votre réponse. »
    détail du cours à évaluer (Pseudo-code) : « Ensuite, chaque terme successif est la somme des deux termes précédents. »

Le champ id vaut « I-algo_simples ».