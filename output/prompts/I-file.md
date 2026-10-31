# Plan I-file (inedit)

Notion : file (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Les files > Les files]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 7 - Les files
> Objectifs :
> ▷ Connaître et comprendre le type abstrait file.
> ▷ Modéliser puis simuler le comportement d'une file.
> ▷ Distinguer les modes FIFO et LIFO des piles et des files.
> 1 Introduction
> Dans ce chapitre nous allons décrire desstructures de données linéairesappelées files. On rappelle qu'une
> structure de données est une organisation logique des données permettant de simplifier ou d'accélérer leur
> traitement.
> Il faut bien comprendre que lorsqu'on parle de structure de données, on parle d'une représentationabstraite
> qui n'est pas en lien direct avec son implémentation qui peut être réalisée de diverses manières suivant le langage
> de programmation, voire au sein d'un même langage de programmation.
> 2 Définition
> A retenir!
> En informatique, unefile (appelée queue en anglais) est une structure de données basée sur le principe
> « P
> [Structures de données > Listes Piles Files > 1.2 Comment seront traitées ces données linéaires ? Introduction des listes, des piles et des files]
> La nature des données ne fait pas tout. Il faut aussi s'intéresser à la manière dont on voudra les traiter :
> 
> - À quelle position les faire entrer dans notre structure ?
> - À quel moment devront-elles en éventuellement en sortir ?
> - Veut-on pouvoir accéder rapidement à n'importe quel élément de la structure, ou simplement au premier ? ou au dernier ?
> 
> Lorsque ces problématiques d'entrée/sortie n'interviennent pas, la structure «classique» de liste est adaptée. Mais lorsque celle-ci est importante, il convient de différencier la structure de **pile** de celle de **file**.
> 
> #### 1.2.1 Les piles (*stack*)
> 
> Une structure de **pile** (penser à une pile d'assiette) est associée à la méthode **LIFO** (Last In, First Out) :
> les éléments sont empilés les uns au-dessus des autres, et on ne peut toujours dépiler que l'élément du haut de la pile. Le dernier élément à être arrivé est donc le premier à

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C18 : Tracer une boucle Python donnée — L'élève suit l'exécution d'un code avec boucles for/range pour en déduire une valeur ou un affichage. On évalue la trace d'exécution.
    gabarit : Déterminer la valeur de [variable] à l'issue des instructions suivantes : [code].
    exemple réel (autre notion) : « 11. elif i2 >= n2: »
    exemple réel (autre notion) : « 17. Déterminer les affichages produits lors de l'exécution de l'appel suivant :  mystere(graphe_airinfo, 'W', [], 0, 'B') »
    support S0 : Code indenté et tableaux mêlés — Matériau contenant du code indenté ou des tableaux à identifiants (conversions, codes de lettres, grilles). L'élève lit le code ou la table pour répondre.
    exemple de support (autre notion) : « 1. Écrire une requête SQL permettant d'afficher tous les modèles des ordinateurs en réparation présents dans la collection. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « 13. Citer les attributs qui sont des clés étrangères dans la relation infos_recuperation. »
    exemple réel (autre notion) : « 5. Citer l'avantage d'utiliser un arbre de recherche par rapport au type de données de la variable contacts_fictifs. »
    support S14 : Prose avec parenthèses — Phrases contenant des parenthèses (couples, types, précisions). Artefact de ponctuation sans matériau commun.
    exemple de support (autre notion) : « b. Ecrire les sept premières personnes (nom et prénom) rencontrées si on utilise le parcours en profondeur infixe.  On donne ci-dessous le code incomplet de la fonctio n d'un parcours en profondeur de l'arbre, dans lequel il manque la ligne correspo ndant à l' »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 2. Donner l'assertion à insérer en début de la fonction creer_liste_clef afin de s'assurer que l'hypothèse sur la clef soit respectée. »
    exemple réel (autre notion) : « 16. Réécrire le code de la fonction modifie en évitant cette répétition.  La classe Abr est complétée afin de permettre l'ajout de nouvelles lignes à la table de routage, tout en conservant les propriétés que doit posséder un arbre binaire  »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 3. Écrire la fonction moitie_droite. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 2. À partir d'un entiern, on construit une liste dek entiers en utilisant l'image étudiée dans la »
    détail du cours à évaluer (Listes Piles Files) : « Pour être utilisée, une interface de file doit proposer a minima : »

Le champ id vaut « I-file ».