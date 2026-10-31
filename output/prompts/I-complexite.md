# Plan I-complexite (inedit)

Notion : complexite (Algorithmique) — questions JAMAIS POSÉES aux annales

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

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 2. On considère la fonction maxi(L) qui prend comme paramètre une liste L de nombres et renvoie le plus grand nombre de cette liste : 1| def maxi(L) : 2| indice = 0 3| maximum = 0 4| while indice <= len(L) : 5| if L[indice] > maximum : 6| m »
    exemple réel (autre notion) : « 7. Recopier et compléter le code de la méthode est_presente ci-dessous qui renvoie True si la clé cle_a_rechercher est présente dans l'instance d'ABR et False sinon :  1 def est_present(self, cle_a_rechercher): 2 if self.est_vide() : 3 retu »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 9. Recopier et compléter le programme ci -dessous permettant d'afficher le(s) nom(s) des champignons que l'on trouve lors de la saison été. for e in liste_champi:  if ...... == 'été':  print(...)  La plaque de cuisson de Quentin est défectueuse. Il ne peut cui »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 3. Écrire une fonction nb_colis qui prend en paramètre une liste d'objets de la classe Colis et qui renvoie le nombre de colis présents dans cette liste. »
    exemple réel (autre notion) : « 7. Écrire une fonction comptes_dans_le_rouge qui prend en paramètre comptes une liste de comptes et qui renvoie la liste des comptes de cette liste dont le montant est strictement négatif. »
    support S5 : Besoin formulé pour requête SQL — Phrase décrivant en langage naturel l'information à extraire d'une base. L'élève la convertit en requête SQL.
    exemple de support (autre notion) : « 1. Expliquer succinctement les différences entre les logiciels libres et les logiciels propriétaires. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C5 : Donner le nom ou l'instruction — L'élève nomme un élément ou fournit une instruction ou un tuple précis. On évalue une réponse courte et exacte.
    gabarit : Donner le [nom|tuple|instruction] correspondant à [situation].
    exemple réel (autre notion) : « 3. Citer le type de parcours de l'arbre qui permettrait d'obtenir les symboles classés par taille d'encodage croissante. »
    exemple réel (autre notion) : « 3. Ce code comporte des erreurs. Indiquer les numéros de lignes à rectifier ainsi que les rectifications à apporter. »
    support S10 : Prose riche en virgules — Phrases longues avec énumérations par virgules ou listes de choix. Artefact de ponctuation, contenus variés.
    exemple de support (autre notion) : « 2. D'après la première règle, si une ligne contient 5 zéros, les cases blanches de cette ligne sont forcément des uns. De même si une ligne contient 5 uns, les cases blanches sont forcément des zéros. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 5. a. Recopier sur la copie et indiquer dans le circuit ci-dessous les entrées e0 et e1 de façon à ce que ce circuit sélectionne le périphérique 1. »
    détail du cours à évaluer (Diviser pour regner) : « Une complexité quasi-linéaire (en O(n \log n)) se situe "entre" une complexité linéaire (en O(n)) et une complexité quadratique (en O(n^2)). »

Le champ id vaut « I-complexite ».