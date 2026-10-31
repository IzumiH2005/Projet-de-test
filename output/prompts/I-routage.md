# Plan I-routage (inedit)

Notion : routage (Architecture, OS et réseaux) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Architecture, OS et réseaux > Protocoles de routage > Introduction]
> Dans un réseau quelconque, le coût de chaque liaison se calcule par la formule :
> 
>     $$ \text{coût} = \frac{10^8}{d} $$
> 
>     où le débit $d$ est exprimé en bits/s.
> 
>     Calculer le coût si la liaison a un débit de :
> 
>     **A.** 10 Mb/s
> 
>     **B.** 1 Gb/s
> 
>     **C.** 1 Mb/s
> 
>     **D.** 50 Mb/s
> 
>     {{
>     correction(True,
>     """
> \"Correction \" 
>         - **A.** $c = \\dfrac{10^8}{10 \\times 10^6} = \\dfrac{10^8}{10^7}= 10$
>         - **B.** $c = \\dfrac{10^8}{10^9} = 10^{-1}= 0,1$
>         - **C.** $c = \\dfrac{10^8}{10^6} = 10^2= 100$
>         - **D.** $c = \\dfrac{10^8}{50 \\times 10^6} = \\dfrac{10^2}{50}=2$
>     """
>     )
>     }}
> 
>     Exercice 5 du sujet La Réunion J1 2022
> 
>     _2020, sujet 0_
> 
>     On considère un réseau composé de plusieurs routeurs reliés de la façon suivante :
> 
>     
> 
>     Le protocole RIP permet de construire les tables de routage des différents routeurs, en indiquant
> [Architecture, OS et réseaux > Routage > Routage]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 15 - Le routage
> Objectifs :
> ▷ Connaître les principaux protocoles de routage
> ▷ Identifier, suivant le protocole de routage utilisé (RIP ou OSPF), la route empruntée par un paquet.
> 1 Introduction
> Exemple
> Thomas veut envoyer une lettre de remerciement à son amiPacôme Toullemonde, habitant à Toulouse
> (en France), qui lui a prété un manuel de NSI.
> 1. Il rédige donc un courrier, le place dans une enveloppe sur laquelle il inscrit le nom, le prénom, le
> numéro, la rue, le code postal, la ville et enfin le pays.
> 2. Puis il dépose le tout à la poste deSerangoon à Singapour.
> 3. L'agent de la poste ne connaît pasPacôme, mais il sait que la lettre doit aller en France.
> 4. Une fois arrivée en France, l'agent de poste Français ne connaît toujours pasPacôme, mais il sait
> qu'il doit envoyer la lettre vers un nouveau centre de tri, celui de Toulouse.
> 5. A

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 3. Donner la nouvelle définition de la variable voisins. »
    exemple réel (autre notion) : « 2. Coder en binaire le mot Bonjour en utilisant la méthode de l'étape 4 avec l'arbre de codage de la figure 1. »
    support S15 : Sous-questions lettrées a) b) — Énoncés découpés en items a), b), c) ou en options lettrées. L'élève traite chaque sous-question ou choisit une option.
    exemple de support (autre notion) : « f) retrait d'un élément ; »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C11 : Analyser une ligne de code précise — L'élève explique ou corrige le rôle d'une ligne désignée dans un programme fourni. On évalue la lecture fine du code.
    gabarit : Expliquer le rôle de la ligne [n] de la fonction [nom].
    exemple réel (autre notion) : « 2. Écrire l'instruction de la ligne 38 permettant de compléter l'implémentation du graphe de la Figure 1. »
    exemple réel (autre notion) : « 1. Recopier et compléter la ligne 7 de l'assertion pour que le pourcentage de mines respecte la précondition recommandée. »
    support S6 : Prose technique avec valeurs numériques — Texte contenant des nombres (masques, suffixes, tables de vérité, scores). Mélange réseaux, booléens et données sans forme commune nette.
    exemple de support (autre notion) : « 5. On reçoit le tableau suivant. 1 1 1 1 1 0 0 1 1  Sachant qu'une unique erreur de transmission s'est produite, recopier le tableau et entourer le bit qui a subi cette erreur (transformation d'un 0 en 1 ou d'un 1 en 0). »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 11. Écrire le code de la fonction en_arbre qui prend en paramètre une liste etoiles de couples de coordonnées non triés et renvoie l'arbre construit selon la démarche décrite plus haut. On pourra utiliser la fonction construction de la ques »
    exemple réel (autre notion) : « c. Indiquer, pour la relation reservation, la ou les clés étrangères (ou secondaires) et en indiquer l'utilité. »
    support S14 : Prose avec parenthèses — Phrases contenant des parenthèses (couples, types, précisions). Artefact de ponctuation sans matériau commun.
    exemple de support (autre notion) : « 6. La passagère d'identifiant 5 a déjà parcouru 10 milliers de kilomètres. Elle réserve un vol de Washington (IAD) à Paris (CDG), d'une distance de 6 milliers de kilomètres.  Écrire la requête permettant de mettre à jour la table passager. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 1. Cet algorithme est-il itératif ou récursif ? Justifier en un e phrase. »
    détail du cours à évaluer (Routage) : « Compléter le schéma avec les coûts puis déterminer les tables de routage de A et E. »

Le champ id vaut « I-routage ».