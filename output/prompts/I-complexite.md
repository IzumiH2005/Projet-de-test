# Plan I-complexite (inedit)

Notion : complexite (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Diviser pour regner > 4.3 Complexité]
> La division par 2 de la taille de la liste pourrait nous amener à penser que le tri fusion est de complexité logarithmique, comme l'algorithme de dichotomie. Il n'en est rien.
> 
> En effet, l'instruction finale ```interclassement(tri_fusion(lst[:m]), tri_fusion(lst[m:]))``` lance **deux** appels à la fonction ```tri_fusion``` (avec certes des données d'entrée deux fois plus petites).
> 
> On peut montrer que :
> 
>     L'algorithme de tri fusion est en $O(n \log n)$.
> 
>     On dit qu'il est **quasi-linéaire**. (ou *linéarithmique*)
> 
> Une complexité quasi-linéaire (en $O(n \log n)$) se situe «entre» une complexité linéaire (en $O(n)$) et une complexité quadratique (en $O(n^2)$). Mais elle est plus proche de la complexité linéaire.
> 
> Pour finir, une jolie animation permettant de comparer les tris :
> 
> Issue de ce site
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
    manière de demander C0 : Écrire une méthode ou requête ciblée — L'élève produit une méthode de classe, une instruction ou une requête SQL qui réalise une opération précisément décrite ; on évalue la traduction exacte d'un besoin en code (conditions, attributs, tables).
    gabarit : Écrire la [méthode/requête/fonction] [nom] permettant de [effet attendu sur les données].
    exemple réel (autre notion) : « 6. Écrire la fonction récursive score_max qui implémente les règles précédentes. »
    exemple réel (autre notion) : « 7. Écrire la méthode get_note de la classe Livre. Cette méthode devra renvoyer la note d'un livre. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 9. Expliquer brièvement pourquoi, lors d'un appel à la fonction chargement_glouton, on peut obtenir l'erreur suivante. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C23 : Donner une information précise — Restitution courte (nom d'un algorithme, coût, adresse, masque, type) ; on évalue une connaissance ou un calcul ponctuel.
    gabarit : Donner le [nom/coût/valeur] [de l'élément] [dans le contexte].
    exemple réel (autre notion) : « 4. Préciser, sans justifier, le coût temporel du tri par insertion d'une liste de 𝑛 éléments dans le pire des cas. »
    exemple réel (autre notion) : « c. Donner le type pour chacun des deux premiers attri buts de la relation clients. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « b. Citer un cas pour lequel l'insertion d'un enregistrement dans la table Reservation n'est pas possible. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « 3. Expliquer pourquoi dans la situation décrite, un pompier ne peut pas avoir de qualification dont le codage décimale est 4. »
    exemple réel (autre notion) : « 4. Expliquer pourquoi il est nécessaire d'avoir "au minimum deux" interfaces réseau dans un routeur. »
    support S6 : Texte avec parenthèses explicatives — Support riche en parenthèses (signatures, précisions, sous-questions (a)(b)) ; l'élève doit tenir compte des précisions et des paramètres annoncés.
    exemple de support (autre notion) : « 1. (a) Recopier et compléter le code du constructeur de la classeConcurrent. On exécute l'instruction suivante :c1 = Concurrent("Mosquito", 87.67, 12) (b) Donner la valeur de l'attributtemps_tot de c1. (c) Donner l'instruction permettant d'accéder à la valeurt »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C19 : Déterminer un chemin ou élément — Questions de détermination (chemin d'un paquet, répertoire, sous-séquence, protocole) sans geste unique, souvent en réseau ; on évalue une déduction à partir du contexte.
    gabarit : Déterminer [le chemin/l'élément] [de A à B / vérifiant la condition] dans [situation].
    exemple réel (autre notion) : « b. Donner le parcours emprunté par celui -ci en respectant le protocole RIP et en utilisant les tables de routage. »
    détail du cours à évaluer (Diviser pour regner) : « Une complexité quasi-linéaire (en O(n \log n)) se situe "entre" une complexité linéaire (en O(n)) et une complexité quadratique (en O(n^2)). »

Le champ id vaut « I-complexite ».