# Plan I-abr (inedit)

Notion : abr (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Arbres > 5. Arbres binaires de recherche (ABR)]
> Un **arbre binaire de recherche** est un arbre binaire dont les valeurs des nœuds (valeurs qu'on appelle étiquettes, ou clés) vérifient la propriété suivante :
> 
>     - l'étiquette d'un nœud est **supérieure ou égale** à celle de **chaque** nœud de son **sous-arbre gauche**.
>     - l'étiquette d'un nœud est **strictement inférieure** à celle du **chaque** nœud de son **sous-arbre droit**.
> 
> À noter que l'arbre 3 (qui est bien un ABR) est appelé **arbre filiforme**. 
> 
> L'arbre 5 n'est pas un ABR à cause de la feuille 9, qui fait partie du sous-arbre gauche de 3 sans lui être inférieure.
> 
> **Remarque :** on pourrait aussi définir un ABR comme un arbre dont le parcours infixe est une suite croissante.
> [Structures de données > Arbres > Introduction]
> Exercice 2 du sujet Nouvelle-Calédonie J2 2022  
> 
>     *2020, sujet 0*
> 
>     **Question  1**
> 
>     Déterminer la taille et la hauteur de l’arbre binaire suivant :
>     
> 
>     
> 
>     **Question 2**  
> 
>     On décide de numéroter en binaire les nœuds d’un arbre binaire de la façon suivante :  
> 
>     - la racine correspond à 1 ;
>     - la numérotation pour un fils gauche s’obtient en ajoutant le chiffre 0 à droite au numéro de son
>     père ;
>     - la numérotation pour un fils droit s’obtient en ajoutant le chiffre 1 à droite au numéro de son
>     père ;  
> 
>     Par exemple, dans l’arbre ci-dessous, on a utilisé ce procédé pour numéroter les nœuds A, B, C, E et
>     F .
> 
>     
> 
>     **a**. Dans l’exemple précédent, quel est le numéro en binaire associé au nœud G ?
>     
>     **b**. Quel est le nœud dont le numéro en binaire vaut 13 en décimal ?
>     
>     **c**. En notant $h$ la hauteur de l’arbre, sur combie

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Analyser un code fourni — Un extrait de code (def numéroté) est donné, à compléter ou à exécuter mentalement ; on évalue la lecture de code et la compréhension de ce qu'il fait.
    gabarit : On considère le code suivant : [code]. [Compléter la ligne n / Donner ce qu'affiche l'appel [appel]].
    exemple réel (autre notion) : « b. Dessiner sur la copie un arbre binaire de hauteur 4. La hauteur d'un arbre est calculée par l'algorithme récursif suivant : 1 Algorithme hauteur(A): 2 test d'assertion : A est supposé non vide 3 si sous_arbre_gauche(A) vide et sous_arbre »
    exemple réel (autre notion) : « 1. def dic_parent(mot_depart, mot_final): »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 4. Avant d'insérer une nouvelle tâche dans l'arbre binaire de recherche, il faut s'assurer que son indice de priorité n'est pas déjà présent. Écrire une méthode est_present de la classe ABR qui répond à la description :  41 42 43 44 def est_present(self, indic »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 4. Écrire une fonction supprime_toutes_occurences(pile, element) qui prend en arguments un objet Pile appelé pile et un élément element et supprime tous les éléments element de pile. »
    exemple réel (autre notion) : « 4. Écrire une fonction verifier_contenu qui prend en paramètres une ﬁle F et trois entiers : nb_rouge, nb_vert et nb_jaune. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « 7. Expliquer en quoi les informations m0, m0_s et cle1_a connues de Bob permettent de garantir à la fois que le message provient bien d'Alice et que Mallory n'a pas pu envoyer le message m3 à Bob en se faisant passer pour Alice. »

- slot 3 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 9. Écrire l'instruction permettant d'obtenir la valeur ‘F03071997DUPON01'. »
    détail du cours à évaluer (ABR) : « On les utilise par exemple pour : ▷ l'implémentation des bases de données indexées ▷ les systèmes de gestion de fichiers ▷ les algorithmes de recherche et de tri ▷ les structures de recherche dans les compilateurs et analyseurs syntaxiques 2 Principe de l'ABR Un arbre binaire de recherche (ABR)est une structure de donnée composée de noeuds (on parlera aussi de clés). »

Le champ id vaut « I-abr ».