# Plan I-calculabilite (inedit)

Notion : calculabilite (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Notion de programme > Notion de programme]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 25 - Calculabilité, décidabilité
> Objectifs :
> ▷ Comprendre que tout programme est aussi une donnée.
> ▷ Comprendre que la calculabilité ne dépend pas du langage de programmation utilisé.
> ▷ Montrer, sans formalisme théorique, que le problème de l'arrêt est indécidable.
> 1 Introduction
> Comme nous l'avons vu en classe dePremière, un programme est la traduction électronique d'un algorithme
> afin qu'il puisse être compris par une machine. Dans ce chapitre, nous allons montrer qu'un programme ne peut
> pas toutcalculer ou décider.
> L'indécidabilité est un concept fondamental en logique. Il a plusieurs sens. Au sens de la démonstration, il
> signifie qu'on ne peut démontrer ni qu'une proposition est vraie ni qu'elle est fausse dans un système d'axiomes;
> ici, le contenu sémantique ne permet d'affirmer ni que l'objet est une pipe ni qu'il n'en est pas une. 
> [Programmation > Calculabilite Decidabilite > 2. Calculabilité]
> Le problème de l'arrêt est dit **indécidable** car la fonction qui le résout (notre brave programme ```halt```) n'est pas **calculable**.

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 1. Écrire en Python une fonction corrige qui prend en paramètre cop et corr, deux listes d'entiers entre 1 et 5 et qui renvoie la liste des booléens associée à la copie cop selon la correction corr. »
    exemple réel (autre notion) : « 3. Écrire en Python une fonction notes_paquet qui prend en paramètre un paquet de copies p et une correction corr et qui renvoie un dictionnaire dont les clés sont les noms des candidats du paquet p et les valeurs sont leurs notes selon la  »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 17. Recopier et compléter l e code de l a fonction welsh_powell donné ci-après. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « 5. Recopier et compléter les lignes 3 et 5 de la méthode indice. On admet que la classe Taquin dispose d'une méthode est_possible qui prend en paramètre un entier numero, compris entre 1 et 8 inclus, et qui renvoie True s'il est possible de »
    exemple réel (autre notion) : « 5. Recopier et compléter les lignes 4 à 8 de la fonction itineraire. »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 3. Connexion du PC8 au réseau Répondre au questionnaire sur le document réponse joint en cochant la ou les bonnes réponses. »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Donner le nom ou l'instruction — L'élève nomme un élément ou fournit une instruction ou un tuple précis. On évalue une réponse courte et exacte.
    gabarit : Donner le [nom|tuple|instruction] correspondant à [situation].
    exemple réel (autre notion) : « a. Indiquer un attribut de la table Album. »
    exemple réel (autre notion) : « 4. Donner le nom du parcours réalisé par le code précédent. »
    support S8 : Phrases courtes isolées — Fragments brefs d'une phrase (hypothèse de scénario, consigne courte). Aucun matériau fourni ; groupe défini par la brièveté.
    exemple de support (autre notion) : « 4. a. Vérifier ces inégalités sur l'arbre binaire de la question 1.a. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C12 : Consignes génériques sans tournure dominante (bis) — Second fourre-tout aux mêmes termes que le groupe 0 : droits Linux, dessin d'arbre, tables… Pas de geste partagé.
    gabarit : [Verbe] [objet] [contexte].
    exemple réel (autre notion) : « a. Recopier sur votre copie les demandes ci-dessous, dans leur intégralité, et les compléter correctement pour qu'elles ajoutent dans la relation emploi les rôles de Daniel Crog en tant que James Bond dans le film nommé ‘Casino Impérial' pu »
    détail du cours à évaluer (Calculabilite Decidabilite) : « Mais dans ce cas-là, l'exécution de (sym) se termine correctement et renvoie la valeur 1. »

Le champ id vaut « I-calculabilite ».