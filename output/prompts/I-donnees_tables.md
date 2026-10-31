# Plan I-donnees_tables (inedit)

Notion : donnees_tables (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Dictionnaires > 2.1 Vérification de l'intégrité]
> Lorsque vous téléchargez un fichier important et que vous souhaitez vérifier qu'il n'a pas été corrompu lors du téléchargement (ou avant), vous avez parfois la possibilité de vérifier l'intégrité de votre fichier téléchargé, en calculant une «empreinte» de votre fichier et en la comparant avec celle que vous êtes censée obtenir :
> 
> Voilà par exemple ce qui apparaît sur la page de téléchargement d'une iso d'ubuntu 18.04 :
> 
> La clé MD5 proposée pour chaque fichier est le résultat ce que **doit** donner le fichier (ici une iso d'environ 1,9 Go) lorsqu'il est «haché» par la fonction MD5. Dans notre cas, si nous téléchargeons 
> ```ubuntu-18.04.3-desktop-amd64.iso```, nous devons calculer l'empreinte du fichier téléchargé et vérifier que nous obtenons bien ```72491db7ef6f3cd4b085b9fe1f232345``` :
> 
> Essayons :
> 
> La clé calculée sur l'ordinateur correspond bien à celle indiquée sur le site de télécha
> [Bases de données > Langage SQL > Exercices SQL débranchés]
> *(d'après Prépabac NSI, Terminale, G.CONNAN, V.PETROV, G.ROZSAVOLGYI, L.SIGNAC, éditions HATIER.)*
> 
>     On veut créer une base de données ```baseHopital.db```  qui contiendra les trois tables suivantes :
> 
>     |  | Patients |
>     |-----|----|
>     | id | ```Int```  |
>     | nom | ```Text```  |
>     | prenom | ```Text```  |
>     | genre | ```Text```  |
>     | annee_naissance | ```Int```  |
> 
>     |  | Ordonnances |
>     |-----|----|
>     | code | ```Int```  |
>     | id_patient | ```Int```  |
>     | matricule_medecin  | ```Int```  |
>     | date_ord | ```Text```  |
>     | medicaments | ```Text```  |
> 
>     |  | Medecins |
>     |-----|----|
>     | matricule | ```Int```  |
>     | nom_prenom | ```Text```  |
>     | specialite | ```Text```  |
>     | telephone | ```Text```  |
> 
>     On suppose que les dates sont données sous la forme ```jj-mm-aaaa```.
> 
>     On donne le diagramme relationnel de cette base :
>     
>     
>    

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C6 : Exécuter mentalement une requête ou instruction suivante — L'élève lit une requête SQL ou une commande donnée et indique ce qu'elle renvoie. On évalue la capacité à simuler l'exécution.
    gabarit : Donner les valeurs renvoyées par la requête suivante : [requête].
    exemple réel (autre notion) : « 3. Donner et expliquer la valeur de l'expression suivante : s2.successeurs[1][1] »
    exemple réel (autre notion) : « 3. En s'appuyant uniquement sur l 'extrait des tables fourni dans la figure 1 écrire ce que renvoie la requête :  SELECT nom FROM groupes WHERE style = 'Latin Jazz'; »
    support S7 : Chaînes et dictionnaires entre guillemets — Matériau contenant des chaînes entre guillemets : dictionnaires Python, propositions, noms. L'élève exploite ces littéraux pour dessiner, évaluer ou coder.
    exemple de support (autre notion) : « 2. Cet arbre binaire de recherche n'est pas " bien construit ". Proposer un arbre binaire de recherche contenant les mêmes clés et dont la hauteur est plus petite que celle de l'arbre initial. 15 20 12 5 4 8 10 »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : milieu d'exercice
    manière de demander C15 : Recopier et compléter un élément — L'élève recopie puis complète une fonction, un résultat ou une table partiellement donnés. On évalue la capacité à combler les trous correctement.
    gabarit : Recopier et compléter [la fonction|le tableau] [nom] [donné ci-dessous].
    exemple réel (autre notion) : « 1. Recopier et compléter le code de la ligne 28 afin d'instancier la balise portant le numéro 12. »
    exemple réel (autre notion) : « a. Recopier et compléter la définition de la classe Noeud pour ajouter un attribut generation qui indique la génération d'un individu.  class Noeud() : def init(prenom, nom) :  self.identite = (prenom, nom)  self.gauche = None  self.droite  »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 7. On considère la fonction Python mystere qui prend en paramètre une chaîne de 9 caractères et qui renvoie une chaîne de caractères.  1 def mystere(chaine): 2 resultat = '' EN_OOTgzNT7QzNjAc0ND4UzMsTYxMj8A2NTAAwMDbAxNEjkx 3 for c in chaine: 4 if c == '-': 5  »

- slot 3 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C1 : Écrire la fonction ou commande nommée — L'élève produit un code précis (fonction, méthode, commande shell) dont le nom est imposé. On évalue la justesse et la syntaxe du code écrit.
    gabarit : Écrire la [fonction|méthode|commande] [nom] qui [comportement attendu].
    exemple réel (autre notion) : « 11. Commenter cette approche. »
    exemple réel (autre notion) : « 6. Écrire la ou les instructions qui permettent de créer la course de la cliente Jeanne Doe. À l'aide de la bibliothèque Python datetime on peut calculer la différence de temps en secondes entre deux dates à l'aide de la fonction du même no »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 5. Recopier et modifier la ligne 6 de la fonction en_grille afin de corriger cette erreur. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C0 : Consignes génériques sans tournure dominante — Groupe fourre-tout : indiquer, dessiner, donner une requête… Aucun geste commun, les termes dominants sont des mots-outils.
    gabarit : [Verbe] [objet] en tenant compte de [contexte].
    exemple réel (autre notion) : « 4. La liaison Liaison2 a un débit très inférieur aux autres liaison s. Expliquer pourquoi le choix du protocole RIP n'est pas judicieux. »
    détail du cours à évaluer (OS) : « Dans le dossiertest2 créer un fichier videexemple.txt. 4. »

Le champ id vaut « I-donnees_tables ».