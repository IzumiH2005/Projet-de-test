# Plan I-recursivite (inedit)

Notion : recursivite (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Recursivite > Introduction]
> #Exercices
> 
>     Écrire une fonction récursive ```puissance``` qui prend en paramètres deux nombres ```x``` et ```n``` qui renvoie le nombre $x^n$.
> 
>     On rappelle que le PGCD (plus grand diviseur commun de deux nombres) vérifie la propriété suivante : si la division euclidienne de $a$ par $b$ s'écrit $a = b \times q + r$, alors $pgcd(a,b)=pgcd(b,r)$. 
> 
>     Cette propriété est à la base de l'algorithme d'Euclide
> 
>     Exemple : $pgcd(24,18)=pgcd(18,6)=pgcd(6,0)$, donc $pgcd(24,18)=6$
> 
>     Écrire une fonction récursive ```pgcd``` qui prend en paramètres deux nombres ```a``` et ```b``` et qui renvoie leur PGCD.
> 
>     La conjecture de Syracuse  (ou de Collatz) postule ceci :  
> 
>     *Prenons un nombre $n$ : si $n$ est pair, on le divise par 2, sinon on le multiplie par 3 puis on ajoute 1. On recommence cette opération tant que possible. Au bout d'un certain temps, on finira toujours par tomber
> [Programmation > Recursivite > Recursivite]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 2 - Récursivité
> Objectifs :
> ▷ Écrire un programme récursif
> ▷ Analyser le fonctionnement d'un programme récursif.
> ▷ Connaître des exemples relevant de domaines variés utilisant la récursivité
> 1 Introduction
> La récursivité, à la fois en informatique et dans la vie courante, trouve son utilité dans la résolution
> de problèmes de façon élégante de problèmes complexes en les décomposant en cas de base et en sous-
> problèmes gérables.
> La récursivité trouve son application dans une variété de domaines informatiques, tels que la program-
> mation, la conception d'algorithmes, la modélisation de données et même dans la création de structures
> récursives comme les arbres et les listes chaînées.
> 2 Définition
> A retenir!
> La récursivité est une méthode de résolution de problèmes qui consiste à décomposer le problème
> en sous-problèmes identiques de plus en p

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 9. De manière générale, expliquer dans quel cas cette fonction mystere renvoie False. L'objectif est d'utiliser la fonction mystere pour écrire une fonction ordre_realisation qui, lorsque c'est possible, détermine l'ordre de réalisation des »
    exemple réel (autre notion) : « 2. Écrire une fonction nb_additions_suite prenant en paramètre un entier 𝑛 et renvoyant la valeur de 𝑝(𝑛) où 𝑝 est la fonction définie ci-dessus. »
    support S13 : Listes et tableaux de nombres — Littéraux Python de listes ou matrices d'entiers, doctests. L'élève s'en sert comme données d'entrée ou de vérification.
    exemple de support (autre notion) : « 4. Écrire une fonction supprime_toutes_occurences(pile, element) qui prend en arguments un objet Pile appelé pile et un élément element et supprime tous les éléments element de pile. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 9. Écrire le code d'une fonction somme qui prend en paramè tre un tableau (type list en Python) d'entiers et renvoie la somme des éléments de ce tableau. »
    exemple réel (autre notion) : « 12. Écrire le code Python de la méthode mkdir. »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 16. Écrire le code de la méthode dechiffrer de la classe Cle_symetrique qui prend en paramètre un entier à déchiffrer et renvoie un tableau représentant l'octet correspondant à cet entier. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C17 : Question directe « quelle est » — L'élève indique une valeur, une propriété ou un élément d'une structure. Réponse courte ; le groupe reste un peu hétérogène.
    gabarit : Quelle est la [valeur|propriété] de [objet] ?
    exemple réel (autre notion) : « 9. Donner la valeur de l'expression dict_perf_5km[2025][2] »
    exemple réel (autre notion) : « a. Quelle valeur renvoie l'appel de suite(6) ? »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « c. Recopier et compléter la ligne 4 de la méthode de la classe Region ci-dessous :Code 1 def renvoie_premiere_couleur_disponible(self): 2 """ Region -> str 3 Renvoie la première couleur du tableau des couleurs disponibles. """,→ 4 return ... »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 4. Expliquer si on peut utiliser des listes de noms plutôt qu'un couple comme clés du dictionnaire. »
    détail du cours à évaluer (Recursivite) : « S'entraîner et essayer d'établir une stratégie de victoire. 2. »

Le champ id vaut « I-recursivite ».