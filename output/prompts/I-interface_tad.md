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
    manière de demander C14 : Analyser un code fourni — Un extrait de code (def numéroté) est donné, à compléter ou à exécuter mentalement ; on évalue la lecture de code et la compréhension de ce qu'il fait.
    gabarit : On considère le code suivant : [code]. [Compléter la ligne n / Donner ce qu'affiche l'appel [appel]].
    exemple réel (autre notion) : « 4. On considère la méthode supplémentaire produire(self) de la classe Stock donnée par le code suivant : def produire(self):   res = 0  while self.stock_suffisant_brioche():  self.qt_beurre = self.qt_beurre - 175  self.qt_farine = self.qt_f »
    exemple réel (autre notion) : « 1. Compléter la fonction récursive suite qui prend en paramètre un entier n et renvoie la valeur de Un. 1 def suite(n): 2 if n < 2: 3 valeur = ... 4 else: 5 valeur = suite(n - 1) + suite(...) 6 return ... »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 4. Dans la console, on saisit la suite d'instructions suivante :  >>> balise4.methode2('rouge') >>> balise4.methode3('vert') >>> balise4.couleurs_balise  Indiquer le résultat renvoyé à l'écran. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « 13. Indiquer quel sera le message d'erreur renvoyé à la console parmi les choix suivants :  "expected an indented block" ;  "takes 2 positionnals arguments but 3 were given" ;  "local variable 'i_cat' referenced before assignement" ;  " »
    exemple réel (autre notion) : « b. Quelle commande permettrait de connaître son adresse IP ? »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 9. Décrire par une phrase en français le résultat de la requête SQL suivante : SELECT nom, prenom FROM Personnel WHERE num_centre = 2; »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C22 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes précisément numérotées d'une fonction à trous ; on évalue la compréhension de la logique locale du code et le respect de la spécification.
    gabarit : Recopier et compléter les lignes [n1] à [n2] de la fonction [nom] afin qu'elle [comportement].
    exemple réel (autre notion) : « 16. Recopier et compléter les lignes 4 et 6 du code de la fonction est_connexe. »
    exemple réel (autre notion) : « 2. Finaliser le programme précédent en complétant les lignes 6, 7 et 8 sur votre copie. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 12. Recopier et compléter les lignes 7 et 8 de la fonction llsc_dyn. On pourra utiliser la fonction native de Python max qui renvoie le maximum des valeurs données en paramètres.  1 def llsc_dyn(tab): 2 n = len(tab) 3 dyn = [1] * n 4 for i in range(1, n): 5 fo »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C8 : Manipuler une base de données — Requêtes et modélisation sur une base relationnelle (supprimer, ajouter, interroger, proposer un schéma) ; on évalue la correspondance entre un besoin métier et les opérations SQL ou la structure de tables.
    gabarit : Donner la (les) requête(s) SQL permettant de [opération] dans la base de données [nom], [contrainte].
    exemple réel (autre notion) : « c. Suite à un changement, l'horaire d'arrivée du train n°7869 est programmé à 08 h 11. Mettre à jour la base de données en conséquence. »
    détail du cours à évaluer (Langage SQL) : « Les SGBD jouent le rôle d'interface entre l'être humain et la base de données. »

Le champ id vaut « I-interface_tad ».