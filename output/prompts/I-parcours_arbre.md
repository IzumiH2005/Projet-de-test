# Plan I-parcours_arbre (inedit)

Notion : parcours_arbre (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Arbres > 2.4 Parcours postfixe]
> Le parcours **postfixe** est aussi un parcours en profondeur d'abord.
> 
>     (parfois aussi appelé **post-ordre** ou encore **suffixe**)
> 
>     - Chaque nœud est visité **après** ses fils le soient.
>     - On part donc de la feuille la plus à gauche, et on ne remonte à un nœud père que si ses fils ont tous été visités. 
> 
> L'ordre des lettres parcourues est donc P-Y-H-N-O-T.
> [Structures de données > Arbres > 2.5 Comment ne pas se mélanger entre le pré / in / post fixe ?]
> - *pré* veut dire *avant*
> - *in* veut dire *au milieu*
> - *post* veut dire *après*
> 
> Ces trois mots-clés parlent de la place du **père** par rapport à ses fils. 
> Ensuite, il faut toujours se souvenir qu'on traite le fils gauche avant le fils droit.
> 
> - préfixe : le père doit être le premier par rapport à ses fils.
> - infixe : le père doit être entre son fils gauche (traité en premier) et son fils droit.
> - postfixe : le père ne doit être traité que quand ses deux fils (gauche d'abord, droite ensuite) l'ont été.
> 
> Un parcours préfixe commencera toujours par la racine, alors qu'un parcours postfixe finira toujours par la racine. Dans un parcours infixe, la racine sera «au milieu» (pas nécessairement parfaitement).
> 
>         Donner le rendu de chaque parcours :
> 
>         1. Parcours en largeur 
>         2. Parcours préfixe
>         3. Parcours infixe
>         4. Parcours postfixe
> 
>         largeur : 1 

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 1. Ecrire une fonction autre(x) qui renvoie 1 si x vaut 0 et 0 si x vaut 1. »
    exemple réel (autre notion) : « 2. On dispose d'une fonction distance_point_droite(p, a, b) qui prend en argument les tuples représentant les coordonnées respectives des points ܲ ,ܣet ܤ , et qui renvoie la distance du point ܲà la droite ሻ. L'exécution de cette fonction pr »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 12. Expliquer le rôle de l'attribut id_ville dans la table sport. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C4 : Expliquer ou justifier un fonctionnement — L'élève rédige une explication causale (pourquoi, comment, en quoi) sur un mécanisme ou un choix ; on évalue la compréhension conceptuelle et la capacité à argumenter, pas l'exécution.
    gabarit : Expliquer pourquoi [choix/propriété/phénomène] dans le cas de [situation].
    exemple réel (autre notion) : « 1. Expliquer pourquoi on ne peut pas prendre l'attribut nom comme clé primaire pour la relation adherent. »
    exemple réel (autre notion) : « 9. Expliquer la différence entre un algorithme de chiffrement symétrique et un algorithme de chiffrement asymétrique. »
    support S6 : Texte avec parenthèses explicatives — Support riche en parenthèses (signatures, précisions, sous-questions (a)(b)) ; l'élève doit tenir compte des précisions et des paramètres annoncés.
    exemple de support (autre notion) : « 2. Recopier et compléter le schéma ci-dessous avec les termes suivants :  élu, bloqué, prêt, élection, blocage, déblocage.   Figure 1. Schéma processus On considère qu'un monoprocesseur est utilisé. Le système d'exploitation tel un chef d'orchestre, gère l'acc »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « a. Qu'affiche le premier print ? »
    exemple réel (autre notion) : « 1. Quel nom générique donne-t-on aux logiciels qui assurent, entre autres, la persistance des données, l'efficacité de traitement des requêtes et la sécurisation des accès pour les bases de données ?  2. a. On considère les requêtes SQL sui »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 1. Écrire le résultat de l'exécution de la requête SQL suivante : SELECT nom_client, prenom_client FROM client ORDER BY nom_client; Pour écrire la relation medicament, il doit utiliser les informations fournies par la notice des médicaments. En voici une ci-de »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C20 : Énoncés de mise en situation — Mélange d'énoncés introductifs et de questions descriptives (arbres, parité, interfaces) ; groupe défini par des tournures génériques plutôt que par un geste.
    gabarit : On considère [situation]. Indiquer [éléments] qui [propriété].
    exemple réel (autre notion) : « 2. Préciser les valeurs contenues dans chacune des variables a et b. »
    détail du cours à évaluer (Arbres) : « Le parcours en largeur d'abord est un parcours étage par étage (de haut en bas) et de gauche à droite. »

Le champ id vaut « I-parcours_arbre ».