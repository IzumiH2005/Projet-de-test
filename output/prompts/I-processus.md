# Plan I-processus (inedit)

Notion : processus (Architecture, OS et réseaux) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
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
> [Architecture, OS et réseaux > Gestion des processus > 2.2.2 Les différents états d'un processus]
> Selon que l'ordonnanceur aura décidé de le confier ou non au processeur pour son exécution, un processus peut donc se trouver dans 3 états :
> 
> - **Prêt** : il attend qu'arrive le moment de son exécution.
> - **Élu** : il est en cours d'exécution par le processeur.
> - **Bloqué** : pendant son exécution (état **Élu**), le processus réclame une ressource qui n'est pas immédiatement disponible. Son exécution s'interrompt. Lorsque la ressource sera disponible, le processus repassera par l'état **Prêt** et attendra à nouveau son tour. 
> 
> Voici les transitions possibles entre ces états (diagramme issu de https://info.blaisepascal.fr/nsi-processus-et-ressources) : 
> 
> Ou de manière simplifiée :
> 
> On peut utiliser la métaphore suivante :
> 
> Sur le bureau d'un professeur, il y a 3 paquets de copies, correspondant aux classes A, B, et C. Ces paquets sont **Prêts** à être corrigés.
> 
> - Si le professeur ramène 

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C15 : Recopier et compléter un élément — L'élève recopie puis complète une fonction, un résultat ou une table partiellement donnés. On évalue la capacité à combler les trous correctement.
    gabarit : Recopier et compléter [la fonction|le tableau] [nom] [donné ci-dessous].
    exemple réel (autre notion) : « 4. Recopier et compléter le programme pour qu'il en soit ainsi :  5 tableau_final = []  6 difference_temps = 0  7 premier = True  8 for ligne in tableau_temps:  9 coureur = [ligne[0]]  10 coureur.append(ligne[1])  11 if premier:  12 temps_p »
    exemple réel (autre notion) : « 7. Recopier et compléter la ligne à ajouter à la table de routage du routeur 2. »
    support S11 : Texte contenant des tirets — Matériau marqué par des tirets (mots composés, puces, listes chaînées). Artefact typographique mêlant fonctions récursives et énigmes.
    exemple de support (autre notion) : « 1. a. Cette fonction est-elle récursive ? Justifier. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 1. L'altitude du premier point est '1457'. Cette chaîne peut être affichée ainsi : print(tab_trace[0][2]). Donner l'instruction permettant d'afficher la longitude du dernier point uniquement. »
    exemple réel (autre notion) : « a. Des deux acronymes LIFO et FIFO, indiquer lequel permet de décrire, de manière gé- nérale, la structure de pile. Donner la signification des quatre lettres qui composent cet acronyme.  b. On applique l'algorithme précédent sur la liste [ »
    support S10 : Prose riche en virgules — Phrases longues avec énumérations par virgules ou listes de choix. Artefact de ponctuation, contenus variés.
    exemple de support (autre notion) : « 16. Écrire la requête SQL qui pour chaque sonde affiche le numéro de série, le nom de l'abonné, et la date de récupération. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « 1. Expliquer le rôle de la fonction init. »
    exemple réel (autre notion) : « 15. Expliquer le rôle de l'attribut id_auteur de la table livres. »
    support S15 : Sous-questions lettrées a) b) — Énoncés découpés en items a), b), c) ou en options lettrées. L'élève traite chaque sous-question ou choisit une option.
    exemple de support (autre notion) : « 2) En utilisant les détails de la trame N°4 (figure 5) ci-dessous, indiquer le protocole utilisé pour cette trame au niveau de la couche transport.  Figure 5 »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 3. La commande cp rosier_abi.html ../adherents/abi/ crée un nouveau ﬁchier /association/adherents/abi/rosier_abi.html sans détruire /association/annonces/rosier_abi.html tandis que mv rosier_abi.html ../adherents/abi/ déplace le ﬁchier ; da »
    détail du cours à évaluer (Gestion des processus) : « On suppose que les quatre processus arrivent dans la file et y sont placés dans l’ordre C₁, C₂, C₃ et C₄. »

Le champ id vaut « I-processus ».