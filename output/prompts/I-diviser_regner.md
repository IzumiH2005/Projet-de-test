# Plan I-diviser_regner (inedit)

Notion : diviser_regner (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Diviser pour regner > Vers l'algorithme d'interclassement]
> Pour interclasser deux listes triées ```lst1``` et ```lst2```.
> 
>     - on part d'une liste vide ```lst_totale```
>     - on y ajoute alternativement les éléments de ```lst1``` et ```lst2```, en veillant à maintenir un ordre croissant. Il faut pour cela gérer séparément un indice ```i1``` pour la liste ```lst1```  et un indice ```i2```  pour la liste ```lst2```.
>     - quand une liste est épuisée, on y ajoute la totalité restante de l'autre liste.
> 
> Exemple d'utilisation :
> 
> ```python
> >>> interclassement([2, 4, 5, 13, 15, 19], [3, 7, 8, 10, 16])
> [2, 3, 4, 5, 7, 8, 10, 13, 15, 16, 19]
> ```
> 
>     ```python linenums='1'
>     def interclassement(lst1, lst2):
>         ...
>                            
>     ``` 
>  
>     ```python linenums='1'
>     def interclassement(lst1, lst2):
>         i1 = ...
>         i2 = ...
>         lst_totale = ...
>         while ...:
>             if ...:
>                 lst_totale.append(
> [Algorithmique > Diviser pour regner > Diviser pour regner]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 24 - Diviser pour régner
> Objectifs :
> ▷ Ecrire un algorithme en utilisant la méthode"diviser pour régner".
> 1 Introduction
> Nous avons vu en première deux algorithmes de tris assez naturels, mais peu efficaces : letri par insertionet
> le tri par sélectionen classe de Première.
> Cette année, nous allons étudier un algorithme beaucoup plus efficace et très utilisé, inventé parJohn Von
> Neumann en 1945 : letri par fusion.
> Cet algorithme nous permettra d'illustrer la méthodediviser pour régnerque nous avions également déjà
> vue lors de larecherche dichotomiqueen classe de Première.
> 2 La dichotomie (rappels)
> Nous avons vu en classe dePremièrel'algorithme dedichotomie. Ce mot, qui vient du grecdikhotomia, signifie
> « division en deux parties ».
> Notre but ici est la recherche de la présence (ou non) d'un élément dans une liste triée. Notre fonction renv

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « 9. Indiquer en justifiant quel autre attribut de la table utilisateur aurait aussi pu servir de clé primaire. On rappelle que la fonction d'agrégation COUNT permet de compter les éléments du résultat d'une requête en plaçant COUNT(*) dans l »
    exemple réel (autre notion) : « c. Déterminer quel type de parcours utilise la fonction est_present. »
    support S12 : Requêtes et syntaxe SQL — Code SQL fourni (SELECT, FROM, WHERE, UPDATE) ou rappel de syntaxe. L'élève lit, exécute mentalement ou s'en inspire.
    exemple de support (autre notion) : « 6. La requête SELECT rayon FROM Exoplanetes NATURAL JOIN Etoiles WHERE no m = 'Kepler-11' ; permet d'obtenir les rayons des exoplanètes orbitant autou r de l'étoile nommée Kepler-11. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C11 : Analyser une ligne de code précise — L'élève explique ou corrige le rôle d'une ligne désignée dans un programme fourni. On évalue la lecture fine du code.
    gabarit : Expliquer le rôle de la ligne [n] de la fonction [nom].
    exemple réel (autre notion) : « b. Donner une commande qui permet d'accéder au répertoire timbres à partir de la racine. »
    exemple réel (autre notion) : « 17. Recopier et compléter la ligne 35 du code de la fonction rechercher. »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 2. Recopier et compléter le code de la fonction suivante qui transforme une liste en pile.  def liste_vers_pile(L):  '''prend en paramètre une liste et renvoie une pile'''  N = len(L)  p_temp = Pile()  for i in range(N):  …………………….  return ………. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 5. Écrire une fonction mise_a_jour qui prend en paramètre l'effectif du stock déjà présent dans la scierie nommé effectif et l'effectif du stock contenu dans le camion nommé autre_effectif et qui met à jo ur le dictionnaire effectif.  Par  »
    exemple réel (autre notion) : « 10. Utiliser les fonctions précédentes et la classe Noeud afin d'écrire une fonction choisit_coup(grille, joueur) prenant en arguments une grille de jeu et le numéro d'un joueur et renvoyant le numéro de la colonne où devrait jouer le joueu »
    support S14 : Prose avec parenthèses — Phrases contenant des parenthèses (couples, types, précisions). Artefact de ponctuation sans matériau commun.
    exemple de support (autre notion) : « 2. Etude du PC7 dont l'adresse IP est : 192.168.20.10 / 24. 2.a. Combien d'octets sont nécessaires pour composer une adresse IP(V4) ? 2.b. Compléter la ligne 2 du tableau du document ré ponse en convertissant la notation décimale de l'adresse IP en notation bi »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 3. Citer un des avantages d'un ci rcuit imprimé de petite taille. »
    détail du cours à évaluer (Diviser pour regner) : « Pour finir, une jolie animation permettant de comparer les tris : »

Le champ id vaut « I-diviser_regner ».