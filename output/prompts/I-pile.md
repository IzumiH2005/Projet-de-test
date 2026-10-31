# Plan I-pile (inedit)

Notion : pile (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Les piles > Les piles]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 6 - Les piles
> Objectifs :
> ▷ Connaître et comprendre le type abstrait pile.
> ▷ Modéliser puis simuler le comportement d'une pile.
> ▷ Distinguer les modes FIFO et LIFO des piles et des files.
> 1 Introduction
> Dans ce chapitre nous allons décrire desstructures de données linéairesappelées piles. Il faut bien com-
> prendrequelorsqu'onparledestructurededonnées,onparled'unereprésentation abstraitequin'estpasenlien
> direct avec son implémentation qui peut être réalisée de diverses manières suivant le langage de programmation,
> voire au sein d'un même langage de programmation.
> 2 Définition
> A retenir!
> En informatique, une pile (stack en anglais) est une structure de données fondée sur le principe du
> dernier arrivé, premier sorti(ou LIFO pour Last In, First Out).
> Cela signifie que les derniers éléments ajoutés à la pile seront les premiers à être récupéré
> [Structures de données > Listes Piles Files > 1.2 Comment seront traitées ces données linéaires ? Introduction des listes, des piles et des files]
> La nature des données ne fait pas tout. Il faut aussi s'intéresser à la manière dont on voudra les traiter :
> 
> - À quelle position les faire entrer dans notre structure ?
> - À quel moment devront-elles en éventuellement en sortir ?
> - Veut-on pouvoir accéder rapidement à n'importe quel élément de la structure, ou simplement au premier ? ou au dernier ?
> 
> Lorsque ces problématiques d'entrée/sortie n'interviennent pas, la structure «classique» de liste est adaptée. Mais lorsque celle-ci est importante, il convient de différencier la structure de **pile** de celle de **file**.
> 
> #### 1.2.1 Les piles (*stack*)
> 
> Une structure de **pile** (penser à une pile d'assiette) est associée à la méthode **LIFO** (Last In, First Out) :
> les éléments sont empilés les uns au-dessus des autres, et on ne peut toujours dépiler que l'élément du haut de la pile. Le dernier élément à être arrivé est donc le premier à

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C17 : Question directe « quelle est » — L'élève indique une valeur, une propriété ou un élément d'une structure. Réponse courte ; le groupe reste un peu hétérogène.
    gabarit : Quelle est la [valeur|propriété] de [objet] ?
    exemple réel (autre notion) : « 8. Déterminer la valeur de l'expression graphe_airinfo['T']['P']. »
    exemple réel (autre notion) : « 11. Donner une valeur possible de graphe_4_4[9] en supposant que graphe_4_4 est la liste d'adjacence représentant le graphe associé à une grille à 4 lignes et 4 colonnes. »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 4. La requête SELECT COUNT(idObs) FROM observation ; permet d'obtenir le nombre total de relevés en Nouvelle Calédonie. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 4. Écrire le code de la fonction indice_premiere_case_occupee. »
    exemple réel (autre notion) : « 2. Proposer une clé primaire pour la table reservation. »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 7. Expliquer en quoi les informations m0, m0_s et cle1_a connues de Bob permettent de garantir à la fois que le message provient bien d'Alice et que Mallory n'a pas pu envoyer le message m3 à Bob en se faisant passer pour Alice. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C18 : Tracer une boucle Python donnée — L'élève suit l'exécution d'un code avec boucles for/range pour en déduire une valeur ou un affichage. On évalue la trace d'exécution.
    gabarit : Déterminer la valeur de [variable] à l'issue des instructions suivantes : [code].
    exemple réel (autre notion) : « 8. Le tableau suivant montre, sur deux exemples, l'évolution d'une file f3 après l'exécution de l'instruction ajouter_mot(f3, 'super') :  état initial de f3 état de f3 après l'instruction ajouter_mot(f3, 'super') Exemple 1   'bac' 'nsi' '20 »
    exemple réel (autre notion) : « 7. return ... »
    support S13 : Listes et tableaux de nombres — Littéraux Python de listes ou matrices d'entiers, doctests. L'élève s'en sert comme données d'entrée ou de vérification.
    exemple de support (autre notion) : « 9. Recopier et compléter le code de la fonction construit_arbre, qui renvoie le nœud correspondant à la racine de l 'arbre. On considère que l'on dispose d'une fonction codage_arbre, qui à partir d'un arbre donné en paramètre renvoie une structure telle que da »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « b. A l'aide des extraits de tables de routage ci-dessus, nommer les routeurs traversés par ce paquet, lorsqu'il va du réseau L1 au réseau L2. »
    détail du cours à évaluer (Listes Piles Files) : « Comme expliqué précédemment, une pile travaille en mode LIFO (Last In First Out). »

Le champ id vaut « I-pile ».