# Plan I-interface_tad (inedit)

Notion : interface_tad (Structures de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Architecture, OS et réseaux > Protocoles de routage > 1. Tables de routage]
> Les tables de routage sont des informations stockées dans le routeur permettant d'aiguiller intelligemment les données qui lui sont transmises.
> 
> Dans le réseau ci-dessus, si l'ordinateur d'adresse ```192.168.0.5``` veut interroger le serveur ```10.7.3.8``` :
> 
> - l'adresse ```10.7.3.8``` n'étant pas dans le sous-réseau F (d'adresse ```192.168.0.0 / 24```), la requête est confiée au routeur R1 via son adresse passerelle dans le réseau F (ici ```192.168.0.254```).
> - le routeur R1 observe si l'IP recherchée appartient à un autre des sous-réseaux auquel il est connecté. Ici, l'IP recherchée ```10.7.3.8``` n'appartient ni au sous-réseau A, ni au sous-réseau E. 
> - le routeur R1 va donc regarder dans sa table de routage l'adresse passerelle d'un autre routeur vers qui elle doit rediriger les données. Si le sous-réseau C fait partie de sa table de routage, le routeur R1 saura alors que le meilleur
> [Structures de données > Listes Piles Files > 4.2 Implémentation d'une file]
> L'objectif est de créer une classe ```File```, disposant des méthodes suivantes :
> 
> - ```est_vide``` : indique si la file est vide. (renvoie un booléen)
> - ```enfile``` : insère un élément (passé en paramètre) en queue de file. (ne renvoie rien)
> - ```defile``` : renvoie la valeur de l'élément en tête de la file ET le supprime de la file.
> 
> Nous y ajouterons comme précédemment la méthode facultative suivante :
> 
> - ```__repr__``` : permet d'afficher la file sous forme agréable (par ex : ```|3|6|2|5|```)
> 
>     Créer la classe ci-dessus. Là encore, le type ```list```  de Python est peut être utilisé.
>     
>     Penser à aller voir ici les méthodes des objets de types ```list```, notamment la méthode ```insert```.
> 
>     
> 
> **Remarque :**  
> Notre implémentation répond parfaitement à l'interface qui était demandée. Mais si le «cahier des charges» obligeait à ce que les opérations ```enfile()``` et ```de

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 10. Recopier et compléter le code de la fonction execute_tous_processus ci- dessous.  1 def execute_tous_processus (file_d_attente): 2 t = 0 3 while ... 4 t = ... 5 return t  EN_NOzgzNT7QzNjAc0ND8UzMsTYxMj2A2NTAAwMDcAxNLjIx »
    exemple réel (autre notion) : « 10. Parmi les durées suivantes, indiquer celle qui permet d'estimer le temps d'exécution de l'appel plus_grande_base(carte_3000) : – 0,4 seconde ; – 1,2 seconde ; – 3,6 secondes.  Justifier. »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « b) Recopier la fonction sans les commentaires et compléter le code manquant. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « f. La fonction récursive maximum ci-dessous prend en paramètre un arbre binaire de recherche abr et renvoie la valeur maximale de ses nœuds. Recopier et compléter les lignes 5 et 7 de cette fonction. »
    exemple réel (autre notion) : « 12. Recopier et compléter les lignes 3, 8, 9, 10 et 12 du code de la fonction contient.  1 def contient(arbre, position):  2 if arbre is None:  3 return ...  4  5 sag, valeur, sad = arbre  6  7 if position < valeur:  8 return contient(...,  »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 7. Recopier et compléter les lignes 12, 16 et 20 du code de la fonction lire_parcours. »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « 7. On souhaite doter la classe Blockchain d'une méthode ajouter_bloc qui prend en paramètre la liste des transactions des dix dernières minutes et l'ajoute dans un nouveau bloc. Écrire le code P ython de cette méthode ci - dessous. 1 def aj »
    exemple réel (autre notion) : « 3. On souhaite créer une fonctionmeilleur_concurrent qui prend en paramètre une listeL de concurrents et qui renvoie l'objetConcurrent correspondant au concurrent le plus rapide. On suppose que la liste est non vide. Recopier et compléter l »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 2. Donner l'instruction permettant de créer compte_cara un compte bancaire de numéro 15083 et de montant initial de 670 € au nom de Cara. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « 5. Écrire la requête permettant d'enregistre r cette modification dans la base de données précédente. »
    détail du cours à évaluer (Langage SQL) : « Les SGBD jouent le rôle d'interface entre l'être humain et la base de données. »

Le champ id vaut « I-interface_tad ».