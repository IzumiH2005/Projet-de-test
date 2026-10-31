# Plan I-mise_au_point (inedit)

Notion : mise_au_point (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Pratiques de programmation > 4.1 Pourquoi des tests ?]
> Tester une fonction est la première chose que l'on fait (normalement...) lorsqu'on vient de finir de l'écrire. 
> 
> Par exemple, si on vient de construire la fonction ```valeur_absolue(n)```, il est fort probable qu'on aille taper ceci dans la console :
> 
> ```python
> >>> valeur_absolue(-3)
> 3
> >>> valeur_absolue(0)
> 0
> >>> valeur_absolue(7)
> 7
> ```
> 
> - On peut regrouper tous ces tests au sein d'une même fonction ```test_valeur_absolue()```.
> - On peut écrire cette fonction ```test_valeur_absolue()``` avant même de commencer à écrire la fonction ```valeur_absolue(n)```.
> 
> > Remarque : 
> > la méthode de développement logiciel TDD (Test Driven Developement) est basée en partie sur ce principe  : 
> 
> > 1. On commence par écrire le test de la fonction.
> > 2. Le test échoue (forcément, la fonction n'est pas encore codée !)
>  > 3. On écrit le code de la fonction pour que le test soit validé.
>  > 4. On améliore (si 
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

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C11 : Analyser une ligne de code précise — L'élève explique ou corrige le rôle d'une ligne désignée dans un programme fourni. On évalue la lecture fine du code.
    gabarit : Expliquer le rôle de la ligne [n] de la fonction [nom].
    exemple réel (autre notion) : « a. Parmi les deux scripts proposés, indiquer celui q ui vous semble le plus adapté pour initialiser un tableau de 0. Justifier votre choix Choix 1 Choix 2 1 | ligne = [0,0,0,0,0,0,0,0] 2 | jeu = [] 3 | for i in range(8) : 4 | jeu.append(lig »
    exemple réel (autre notion) : « 2. Donner la plus petite valeur de cible que la ligne [6,4,5,8,2] peut atteindre. Donner aussi la plus grande valeur de cible que la ligne peut atteindre. »
    support S2 : Prose sur un modèle relationnel — Texte court sur une base de données (clés, relations, suppression). L'élève raisonne sur le schéma décrit.
    exemple de support (autre notion) : « d. Déterminer le nouveau parcours emprunté par le paquet IP pour aller du routeur R1 au routeur R6. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C5 : Donner le nom ou l'instruction — L'élève nomme un élément ou fournit une instruction ou un tuple précis. On évalue une réponse courte et exacte.
    gabarit : Donner le [nom|tuple|instruction] correspondant à [situation].
    exemple réel (autre notion) : « 3. Écrire une requête SQL permettant d'établir le nom et prénom de toutes les femmes inscrites à la compétition. »
    exemple réel (autre notion) : « 11. Expliquer la différence de comportement entre un appel à la méthode parcours de la classe Dossier et une exécution de la commande UNIX ls. »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 4. On complète la section de code que Bachir doit modiﬁer pour r épondre à l'annonce. <h2>En échange de</ h2> <table> <tr><td>Nom :</ td><td>Bachir</td></tr> <tr><td>Plante :</ td><td>Orchidée noire Cymbidium</ td></tr> <tr><td>Lien : </ td><td><a href="monsit »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C18 : Tracer une boucle Python donnée — L'élève suit l'exécution d'un code avec boucles for/range pour en déduire une valeur ou un affichage. On évalue la trace d'exécution.
    gabarit : Déterminer la valeur de [variable] à l'issue des instructions suivantes : [code].
    exemple réel (autre notion) : « 1. On donne la fonction suivante.  def fonction1(tab, i):  nb_elem = len(tab)  cpt = 0  for j in range(i+1, nb_elem):  if tab[j] < tab[i]:  cpt += 1  return cpt »
    exemple réel (autre notion) : « 2. On propose la fonction ci-dessous, qui prend en argument une pile P et renvoie un couple de piles : def transforme(P) :  Q = creer_pile()  while not est_vide(P) :  v = depile(P)  empile(Q,v)  return (P,Q) Recopier et compléter sur votre  »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 1. Compléter la fonction récursive suite qui prend en paramètre un entier n et renvoie la valeur de Un. 1 def suite(n): 2 if n < 2: 3 valeur = ... 4 else: 5 valeur = suite(n - 1) + suite(...) 6 return ... »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 12. Indiquer, parmi les deux propositions suivantes, celle qui est correcte : − Proposition A : le graphe de la compagnie AirInfo est connexe ; − Proposition B : le graphe de la compagnie Droidevant est connexe. »
    détail du cours à évaluer (Routage) : « Si le réseau global est complexe, la configuration peut être fastidieuse et source d'erreurs. »

Le champ id vaut « I-mise_au_point ».