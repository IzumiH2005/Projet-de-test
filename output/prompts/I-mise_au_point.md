# Plan I-mise_au_point (inedit)

Notion : mise_au_point (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Pratiques de programmation > 1. Conventions syntaxiques]
> La programmation est un art délicat : un simple caractère en trop peut provoquer une erreur pour le code tout entier (penser à un innocent caractère d'espace en début de ligne dans un code Python).
> 
> Mais même lorsqu'un code s'exécute sans erreur, il ne faut pas négliger l'aspect purement «esthétique» de celui-ci : il est nécessaire de respecter autant que possible des conventions typographiques, qui vont standardiser le code et le rendre ainsi plus lisible.
> 
> Ainsi pour chaque langage, il existe une «bible» de bonnes pratiques de présentation du code, qui visent à l'uniformiser. Pour Python, cette référence s'appelle la Python Enhancement Proposal 8, plus connue sous le nom de PEP8. 
> 
> En voici quelques extraits :
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

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C24 : Compléter une fonction à trous — L'élève recopie et complète une fonction ou une table entière (parfois à partir d'une ligne donnée) ; on évalue l'achèvement d'un code partiellement fourni.
    gabarit : Recopier et compléter la fonction [nom] (à partir de la ligne [n]) qui [comportement].
    exemple réel (autre notion) : « 4. La documentation de la fonction randint indique que randint(a, b) renvoie un entier aléatoire compris entre les entiers a et b incluant les deux extrémités a et b. Recopier et compléter la ligne 21 du code de la fonction gen_mdp. »
    exemple réel (autre notion) : « 8. Recopier et compléter la représentation graphique, ci -dessus, en y ajoutant successivement et dans cet ordre les nœuds suivants : o sonde portant le nom sonde900 et le numéro de série 900 ; o sonde portant le nom sonde650 et le numéro d »
    support S5 : Données numériques littérales — Le support fournit des listes, tableaux ou tuples de nombres (cas de test, matrices, appels) ; l'élève exécute ou programme sur ces valeurs concrètes.
    exemple de support (autre notion) : « 3. On considère dans cette question que la salle d'attente est triée par ordre croissant des priorités. a. Quand un patient est pris en charge, il faut l'enlever de la salle d'attente. La fonction quitte(attente) supprime le patient de priorité 1 de la liste a »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 9. Recopier et compléter les quatre lignes ci-dessous.  valmax(1) = prix[...] = ...  valmax(2) = ... = ...  valmax(3) = ... = ...  valmax(4) = max(prix[...], prix[...] + ... , prix[...] + ... , prix[...] + ...) = ... »
    exemple réel (autre notion) : « a. Écrire ce qui sera affiché dans la console après l'exécution de la ligne suivante : res = somme_entiers_rec(3) »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 3. Pour que le client puisse connaitre à tout moment le montant de son panier, on souhaite ajouter une méthode prix_total() à la classe Panier qui renvoie la somme des prix de tous les articles présents dans le panier. Ecrire le code de la méthode prix_total . »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « a. Quelle valeur contient la variable temp après cette exécution ? »
    exemple réel (autre notion) : « a. Que renvoie mystere( '01110111 ') ? »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 3. Donner une instruction permettant de créer une instance nommée ge de la classe Region correspondant à la région dont le nom est " Grand Est ". »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C6 : Établir ou lire une table de routage — Majoritairement réseau : dresser, compléter ou exploiter une table de routage selon un protocole (RIP/OSPF), ou identifier un chemin ; on évalue l'application d'un protocole à une topologie.
    gabarit : Donner la [table/chemin] [de l'élément] selon [protocole/règle], après [événement].
    exemple réel (autre notion) : « b. Donner la hauteur de cet arbre. »
    détail du cours à évaluer (Routage) : « Si le réseau global est complexe, la configuration peut être fastidieuse et source d'erreurs. »

Le champ id vaut « I-mise_au_point ».