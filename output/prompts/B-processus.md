# Plan B-processus (banque)

Notion : processus (Architecture, OS et réseaux) — banque de questions isolées
Extraits du cours :
> [Architecture, OS et réseaux > Gestion des processus > Introduction]
> **Partie A**
> 
>     Cette partie est un questionnaire à choix multiples (QCM).
>     Pour chacune des questions, une seule des quatre réponses est exacte.
> 
>     1. Parmi les commandes ci-dessous, laquelle permet d’afficher les processus en cours
>     d’exécution ?
>         - a. ```dir```
>         - b. ```ps``` 
>         - c. ```man``` 
>         - d.   ```ls```
>     2. Quelle abréviation désigne l’identifiant d’un processus dans un système d’exploitation de type UNIX ?
>         - a. PIX
>         - b. SIG 
>         - c. PID 
>         - d. SID
>     3. Comment s'appelle la gestion du partage de processeur entre les différents processus ?
>         - a. L'interblocage
>         - b. L'ordonnancement
>         - c. La planification
>         - d. La priorisation
>     4. Quelle commande permet d’interrompre un processus dans un système d’exploitation de type
>     UNIX ?
>         - a. ```stop```
>         - b. ```interrupt`
> [Architecture, OS et réseaux > Processus > Processus]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 17 - Les processus
> Objectifs :
> ▷ Décrire la création d'un processus, l'ordonnancement de plusieurs processus par le système.
> ▷ Mettre en évidence le risque de l'interblocage (deadlock).
> 1 Introduction
> Dans les années 1970, les ordinateurs personnels n'étaient pas capables d'exécuter plusieurs tâches à la fois. On
> lançait un programme et on y restait jusqu'à ce que celui-ci "plante" ou se termine.
> Les systèmes d'exploitation récents (Windows, Linux ou MacOS par exemple) permettent d'exécuter plusieurs
> tâches simultanément - ou en tous cas, donner l'impression que celles-ci s'exécutent en même temps. C'est ce
> que l'on appelle lepseudo-parallélisme.
> A un instant donné, il n'y a donc pas un mais plusieurs programmes qui sont en cours d'exécution sur un
> ordinateur : on les nommeprocessus.
> Une des tâches du système d'exploitation est d'allouer 
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=ordonnancement / explication / comprendre | Bloom=comprendre | formulations typiques : processus, interblocage, situation, elu
    style réel : « 1. Parmi les commandes ci-dessous, laquelle permet d'afficher les processus en cours
d'exécution ?

a. dir
b. ps
c. man »
- slot 2 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier completer, fonction, recopier
    style réel : « a) Recopier et compléter l'instruction Python suivante permettant de créer la liste d'attente
initiale des processus donnés dans le tableau précédent (le processus PID 11 est à l'indice
0 de la liste d'attente) :
liste_a »
- slot 3 | archétype=justifier_choix / explication / analyser | Bloom=analyser | formulations typiques : expliquer, pourquoi, expliquer pourquoi, quoi
    style réel : « 4. On considère trois ressourcesR1, R2 et R3 et trois processusP1, P2 et P3 dont les ﬁles d'exé-
cution des instructions élémentaires sont indiquées ci-dessous :
Processus P1
Demande R1
Demande R2
Libère R1
Libère R2
Pro »

Le champ id vaut « B-processus ».