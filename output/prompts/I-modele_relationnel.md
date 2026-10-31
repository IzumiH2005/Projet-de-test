# Plan I-modele_relationnel (inedit)

Notion : modele_relationnel (Bases de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Bases de données > Base de donnees relationnelles > Base de donnees relationnelles]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 8 - Les bases de données relationnelles
> Objectifs :
> ▷ Identifier les concepts définissant le modèle relationnel.
> ▷ Maîtriser les définitions de : relation, attribut, domaine, clé primaire, clé étrangère, schéma relationnel
> ▷ Exprimer les contraintes d'intégrité d'une base de données
> ▷ Savoir réaliser un schéma relationnel
> ▷ Savoir repérer les anomalies dans le schéma relationnel d'une base de données
> 1 Introduction
> Les bases de données sont aujourd'hui incontournables, car très peu d'informations restent encore stockées sur
> du papier. Nous avons vu en classe dePremière comment utiliser des données comme celle d'un tableur avec
> notamment l'utilisation du formatcsv.
> En effet, prenons l'exemple d'une table contenant quelques films :
> Titre Réalisateur Année Durée
> 2001 : A Space Odyssey Stanley Kubrick 1968 149
> Alien Ridley Scott 1979 117
> Blad
> [Bases de données > Modele relationnel > 3. Clé Primaire]
> Une clé primaire est un attribut (ou une réunion d'attributs) **dont la connaissance suffit à identifier avec certitude un unique enregistrement**.
> 
> Par exemple, la clé primaire de la relation des personnes nées en France pourrait être leur numéro de Sécurité Sociale.
> 
>  Observons, dans notre relation précédente, ce qui peut être une clé primaire et ce qui ne peut pas l'être.
> 
> - Titre : cet attribut pourrait jouer le rôle de clé primaire. En effet, notre table ne contient pas deux livres ayant le même titre.
> - Auteur : cet attribut pourrait jouer le rôle de clé primaire. En effet, notre table ne contient pas deux livres ayant le même auteur.
> - Éditeur : cet attribut ne peut **pas** jouer le rôle de clé primaire. En effet, la donnée de l'attribut «Actes Sud» renvoie vers 4 livres différents.
> - ISBN : (International Standard Book Number) cet attribut est un numéro unique spécifique à chaque

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C16 : Écrire une requête SQL — L'élève rédige une requête SQL répondant à un besoin formulé en langage naturel. On évalue sélection, jointures, filtres et tris.
    gabarit : Écrire une requête SQL permettant d'afficher [attributs] des [entités] [condition].
    exemple réel (autre notion) : « a. Écrire une requête qui corrige cette erreur dans la table espece. »
    exemple réel (autre notion) : « 10. Écrire une requête SQL permettant d'obtenir le nombre d'affirmations qui ont 50 likes ou plus. »
    support S8 : Phrases courtes isolées — Fragments brefs d'une phrase (hypothèse de scénario, consigne courte). Aucun matériau fourni ; groupe défini par la brièveté.
    exemple de support (autre notion) : « 4. Bob envoie un message à Alice. Énumérer dans l'ordre tous les routeurs par lesquels transitera ce message. »

- slot 2 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Donner le nom ou l'instruction — L'élève nomme un élément ou fournit une instruction ou un tuple précis. On évalue une réponse courte et exacte.
    gabarit : Donner le [nom|tuple|instruction] correspondant à [situation].
    exemple réel (autre notion) : « 9. Donner le coût en temps de la recherche dichotomique. EN_NOTM0NT7QzNjAc0ND4UzMsTYxMj4A2NTAAwMDxAxNAjQx »
    exemple réel (autre notion) : « 11. Donner le schéma relationnel de la table ville. »
    support S15 : Sous-questions lettrées a) b) — Énoncés découpés en items a), b), c) ou en options lettrées. L'élève traite chaque sous-question ou choisit une option.
    exemple de support (autre notion) : « b) Indiquer le plus court chemin au sens du protocole RIP, minimisant le nombre de routeurs traversés (sauts), en précisant son nombre de sauts. »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : début d'exercice (question d'entrée)
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 8. Donner la commande qu'Alan doit utiliser dans le terminal pour tester la connectivité entre son ordinateur et l'ordinateur de Grace. »
    exemple réel (autre notion) : « 2. Écrire les lignes de code permettant d'instancier un objet Bot1 de la classe Chatbot et d'ajouter à son dictionnaire l'interaction : Question : "Bonjour, comment vas-tu ?" Réponse : "Bonjour, je vais bien, merci." »
    support S6 : Prose technique avec valeurs numériques — Texte contenant des nombres (masques, suffixes, tables de vérité, scores). Mélange réseaux, booléens et données sans forme commune nette.
    exemple de support (autre notion) : « 1. Toutes les machines devront , pour se connecter à ce réseau, disposer d'une carte électronique dédiée. Donner son nom. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 6. Compléter ce jeu de tests pour s'assurer que l'on couvre les cas suivants : les piles sont différentes, mais de même taille ; les piles sont identiques. »
    détail du cours à évaluer (Modele relationnel) : « La cohérence entre les différentes tables d'une base de données est assurée par les clés étrangères : dans une table, la valeur d'un attribut qui est clé étrangère doit obligatoirement pouvoir être retrouvée dans la table dont cet attribut est clé primaire. »

Le champ id vaut « I-modele_relationnel ».