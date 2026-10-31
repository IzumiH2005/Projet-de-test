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
> [Architecture, OS et réseaux > Protocoles de routage > 1. Tables de routage]
> Les tables de routage sont des informations stockées dans le routeur permettant d'aiguiller intelligemment les données qui lui sont transmises.
> 
> Dans le réseau ci-dessus, si l'ordinateur d'adresse ```192.168.0.5``` veut interroger le serveur ```10.7.3.8``` :
> 
> - l'adresse ```10.7.3.8``` n'étant pas dans le sous-réseau F (d'adresse ```192.168.0.0 / 24```), la requête est confiée au routeur R1 via son adresse passerelle dans le réseau F (ici ```192.168.0.254```).
> - le routeur R1 observe si l'IP recherchée appartient à un autre des sous-réseaux auquel il est connecté. Ici, l'IP recherchée ```10.7.3.8``` n'appartient ni au sous-réseau A, ni au sous-réseau E. 
> - le routeur R1 va donc regarder dans sa table de routage l'adresse passerelle d'un autre routeur vers qui elle doit rediriger les données. Si le sous-réseau C fait partie de sa table de routage, le routeur R1 saura alors que le meilleur

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C23 : Donner une information précise — Restitution courte (nom d'un algorithme, coût, adresse, masque, type) ; on évalue une connaissance ou un calcul ponctuel.
    gabarit : Donner le [nom/coût/valeur] [de l'élément] [dans le contexte].
    exemple réel (autre notion) : « 2. (a) Recopier et compléter la fonction récursive Python present ayant pour paramètres un arbre de pédigréearb et le nom d'un chiennom et qui renvoieTrue si ce nom est présent dans l'arbre de pédigrée ouFalse sinon. 1 def present(arb, nom) »
    exemple réel (autre notion) : « 6. Écrire une requête SQL permettant d'obtenir le nom et le prénom du joueur j_1 de l'équipe "Les Kangourous". L'équipe "Volley Warriors" a terminé le tournoi avec un total de 5 points. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « 1. Indiquer ce que renvoie la requête suivante lorsqu'on l'applique aux extraits précédents.  SELECT nom FROM lac WHERE altitude <= 2000; »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C23 : Donner une information précise — Restitution courte (nom d'un algorithme, coût, adresse, masque, type) ; on évalue une connaissance ou un calcul ponctuel.
    gabarit : Donner le [nom/coût/valeur] [de l'élément] [dans le contexte].
    exemple réel (autre notion) : « 2. La requête SELECT nom FROM station ORDER BY nom ; permet d'obtenir le nom de toutes les stations météorologiques triées par ordre alphabétique. »
    exemple réel (autre notion) : « 7. Écrire une requête SQL permettant d'afficher le nom et le site web des AASQA. »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « a. On donne ci-dessous, le code Python d'une fonction mystere.  On rappelle que l'appel L.append(x) ajoute l'élément x à la fin de la liste L. Indiquer l'affichage produit par l'exécution de la ligne de code suivante : print(mystere(reservation, '2022-08-23')) »

- slot 3 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C6 : Établir ou lire une table de routage — Majoritairement réseau : dresser, compléter ou exploiter une table de routage selon un protocole (RIP/OSPF), ou identifier un chemin ; on évalue l'application d'un protocole à une topologie.
    gabarit : Donner la [table/chemin] [de l'élément] selon [protocole/règle], après [événement].
    exemple réel (autre notion) : « c. Donner la hauteur des ABR a1 et a2. »
    détail du cours à évaluer (Protocoles de routage) : « La figure 1 ci-dessus représente le schéma d’un réseau d’entreprise. »

Le champ id vaut « I-routage ».