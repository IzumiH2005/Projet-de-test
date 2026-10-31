# Plan B-routage (banque)

Notion : routage (Architecture, OS et réseaux) — banque de questions isolées
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
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=autre / explication / créer | Bloom=créer | formulations typiques : ecrire, python, proposer, permettant
    style réel : « 3. Identifier dans la configuration de cet hôte le paramètre mal configuré et
proposer une correction. »
- slot 2 | archétype=table_routage / explication / appliquer | Bloom=appliquer | formulations typiques : routeur, routage, table routage, routeurs
    style réel : « a. Indiquer deux routes qui permettent d'atteindre le routeur D et leur nombre de sauts. »
- slot 3 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « 12. Écrire le code de la méthode voisins qui renvoie la liste de tous les robots
avec lesquels il peut directement communiquer. »
- slot 4 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, lignes
    style réel : « b. Compléter sur le document réponse le tableau des routes et des nombres de sauts
respectifs établis par chacun des routeurs pour rejoindre le routeur D. »

Le champ id vaut « B-routage ».