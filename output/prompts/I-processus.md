# Plan I-processus (inedit)

Notion : processus (Architecture, OS et réseaux) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

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
> [Architecture, OS et réseaux > Gestion des processus > 3.1 Définition et exemple]
> Comme nous venons de le voir, un processus peut être dans l'état bloqué dans l'attente de la libération d'une ressource. 
> 
> Ces ressources (l'accès en écriture à un fichier, à un registre de la mémoire...) ne peuvent être données à deux processus à la fois. Des processus souhaitant accéder à cette ressource sont donc en concurrence sur cette ressource. Un processus peut donc devoir attendre qu'une ressource se libère avant de pouvoir y accéder (et ainsi passer de l'état Bloqué à l'état Prêt).
> 
> **Problème :** Et si deux processus se bloquent mutuellement la ressource dont ils ont besoin ?
> 
> **Exemple :** Considérons 2 processus A et B, et deux ressources R et S. L'action des processus A et B est décrite ci-dessous :
> 
> **Déroulement des processus A et B :**
> 
> - A et B sont créés et passent à l'état **Prêt**.
> - L'ordonnanceur déclare **Élu** le processus A (ou bien B, cela ne change rien).
> - L'

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C13 : Raisonner sur une figure — La question s'appuie sur une figure numérotée (arbre, réseau, arborescence, configuration) que l'élève lit, mesure ou complète ; on évalue la lecture d'une représentation graphique.
    gabarit : En vous appuyant sur la figure [n], [donner/justifier/compléter] [propriété de l'objet représenté].
    exemple réel (autre notion) : « a. On exécute l'instruction nb_sup(16, abr) dans laquelle abr est l'arbre initial de la figure 1. Déterminer le nombre d'appels à la fonction nb_sup. »
    exemple réel (autre notion) : « b. Ecrire les deux instructions permettant de construire l'arbre de la figure 1. On rappelle que le nombre val est égal à 16. »
    support S0 : Énoncé en prose avec numéros — Support textuel ordinaire mêlant prose et nombres (routeurs, adresses, tailles) ; l'élève travaille à partir d'une mise en situation décrite, sans matériau structuré dominant.
    exemple de support (autre notion) : « 3. Écrire une requête permettant d'obtenir la liste sans doublon des id_salle des salles réservées depuis janvier 2024. On pourra utiliser le com parateur > pour les dates. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C6 : Établir ou lire une table de routage — Majoritairement réseau : dresser, compléter ou exploiter une table de routage selon un protocole (RIP/OSPF), ou identifier un chemin ; on évalue l'application d'un protocole à une topologie.
    gabarit : Donner la [table/chemin] [de l'élément] selon [protocole/règle], après [événement].
    exemple réel (autre notion) : « 3. Donner la table de routage du routeur R2 pour le réseau représenté sur la figure 1, selon le protocole RIP. »
    exemple réel (autre notion) : « a. Donner la taille de cet arbre. »
    support S0 : Énoncé en prose avec numéros — Support textuel ordinaire mêlant prose et nombres (routeurs, adresses, tailles) ; l'élève travaille à partir d'une mise en situation décrite, sans matériau structuré dominant.
    exemple de support (autre notion) : « d. Donner, en la justifiant, la route qui sera empruntée par un paquet IPv4 pour aller d'une machine ayant pour adresse IPv4 192.168.2.1 à une machine ayant pour adresse IPv4 192.168.4.1 »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C23 : Donner une information précise — Restitution courte (nom d'un algorithme, coût, adresse, masque, type) ; on évalue une connaissance ou un calcul ponctuel.
    gabarit : Donner le [nom/coût/valeur] [de l'élément] [dans le contexte].
    exemple réel (autre notion) : « 5. Donner une requête SQL permettant de récupérer le nom de tous les groupes qui jouent sur la scène 1. »
    exemple réel (autre notion) : « 4. Écrire une requête SQL permettant d'obtenir l'identifiant et le nom des étoiles dont l'ascension droite est supérieure ou égale à 100 degrés. »
    support S3 : Contexte rédigé en plusieurs phrases — Questions précédées ou suivies d'un paragraphe de contexte (données, schéma relationnel, situation) ; l'élève doit extraire l'information utile du texte.
    exemple de support (autre notion) : « 7. Écrire une requête permettant d'obtenir la liste sans doublon des noms de société ayant réservé une salle de réunion. EN_NOzUzMD2M0ODAczOT0UzMmTYxMj5A2MDEO2OTjQ3OVTYx »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C20 : Énoncés de mise en situation — Mélange d'énoncés introductifs et de questions descriptives (arbres, parité, interfaces) ; groupe défini par des tournures génériques plutôt que par un geste.
    gabarit : On considère [situation]. Indiquer [éléments] qui [propriété].
    exemple réel (autre notion) : « a. Donner les valeurs d'affichage des nœuds dans le cas du parcours infixe de l'arbre. »
    détail du cours à évaluer (Gestion des processus) : « On suppose que les quatre processus arrivent dans la file et y sont placés dans l’ordre C₁, C₂, C₃ et C₄. »

Le champ id vaut « I-processus ».