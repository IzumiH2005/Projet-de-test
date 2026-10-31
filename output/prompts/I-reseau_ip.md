# Plan I-reseau_ip (inedit)

Notion : reseau_ip (Architecture, OS et réseaux) — questions JAMAIS POSÉES aux annales

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
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « 3. Écrire les lignes de code permettant d'obtenir la réponse à la question "Bonjour, comment vas-tu ?" EN_NOjczNT7QzNjAc0ND7UzMsTYxMj0A2NTAAwMDdAxNMjcx »
    exemple réel (autre notion) : « 1. Parmi les schémas suivants, lequel représente le mieux une architecture de Von Neumann ? a)   b) »
    support S8 : Phrases courtes isolées — Fragments brefs d'une phrase (hypothèse de scénario, consigne courte). Aucun matériau fourni ; groupe défini par la brièveté.
    exemple de support (autre notion) : « 2. On appelle longueur d'une ﬁle le nombre d'éléments qu'elle contient. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C11 : Analyser une ligne de code précise — L'élève explique ou corrige le rôle d'une ligne désignée dans un programme fourni. On évalue la lecture fine du code.
    gabarit : Expliquer le rôle de la ligne [n] de la fonction [nom].
    exemple réel (autre notion) : « 11. Recopier et compléter la ligne 3 du code ci-après de la fonction inverser qui modifie le tableau passé en paramètre en inversant l'ordre de ses éléments.  1 def inverser(tab): 2 for i in range(len(tab) // 2): 3 permuter(...) »
    exemple réel (autre notion) : « 13. Proposer une correction du code pour que cette erreur ne se produise plus. »
    support S6 : Prose technique avec valeurs numériques — Texte contenant des nombres (masques, suffixes, tables de vérité, scores). Mélange réseaux, booléens et données sans forme commune nette.
    exemple de support (autre notion) : « 6. Expliquer l'intérêt d'utiliser trois tables Chanson, Album et Groupe au lieu de regrouper toutes les informations dans une seule table. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C15 : Recopier et compléter un élément — L'élève recopie puis complète une fonction, un résultat ou une table partiellement donnés. On évalue la capacité à combler les trous correctement.
    gabarit : Recopier et compléter [la fonction|le tableau] [nom] [donné ci-dessous].
    exemple réel (autre notion) : « 9. Recopier et compléter le retour de la fonction coloration appliquée au graphe G donné plus haut.  {1: 'Vert', 2: ..., ...} »
    exemple réel (autre notion) : « a. Recopier et compléter l'arbre ci-dessous pour qu'il soit magique. »
    support S11 : Texte contenant des tirets — Matériau marqué par des tirets (mots composés, puces, listes chaînées). Artefact typographique mêlant fonctions récursives et énigmes.
    exemple de support (autre notion) : « c. Recopier et compléter l'algorithme ci-dessus en y i nsérant au bon endroit la ligne contenant l'instruction d'affichage pour que cet algorithme corresponde à un parcours en profondeur préfixe. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 2. Donner la taille maximale d'un arbre binaire de hauteur 10 dont tous les nœuds ont une valeur. »
    détail du cours à évaluer (Protocoles de routage) : « Toutes les adresses des machines connectées à un réseau local ont la même partie réseau. »

Le champ id vaut « I-reseau_ip ».