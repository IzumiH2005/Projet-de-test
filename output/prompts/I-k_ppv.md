# Plan I-k_ppv (inedit)

Notion : k_ppv (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Structures de données > Listes Piles Files > 0. Préambule : interface ≠ implémentation :star: :star: :star:]
> Les structures que nous allons voir peuvent s'envisager sous deux aspects :
> 
> - le côté utilisateur, qui utilisera une interface pour manipuler les données.
> - le côté concepteur, qui aura choisi une implémentation pour construire la structure de données.
> 
>     - Le volant et les pédales d'une voiture constituent une partie de son **interface**.
>     - L'**implémentation** va désigner tous les mécanismes techniques qui sont mis en œuvre pour que (par exemple) le mouvement de rotation du volant aboutisse à un changement de direction des roues.
>     - La standardisation des interfaces fait qu'un utilisateur peut passer sans problème d'une voiture à une autre, même si l'implémentation est complètement différente.
> 
>     
> 
> Nous avons déjà abordé ces deux aspects lors de la découverte de la Programmation Orientée Objet. Le principe d'encapsulation fait que l'utilisateur n'a qu'à connaître l'existenc
> [Structures de données > Listes Piles Files > 1.1 À chaque donnée sa structure]
> En informatique comme dans la vie courante, il est conseillé d'adapter sa manière de stocker et de traiter des données en fonction de la nature de celles-ci :
> 
> - Le serveur d'un café, chargé de transporter les boissons du comptoir aux tables des clients, n'utilisera pas un sac en plastique pour faire le transport : il préfèrera un plateau. 
> - Le chercheur de champignons, lui, n'utilisera pas un plateau pour stocker ses trouvailles : il préfèrera un panier.
> - Pour stocker des chaussettes, on préfèrera les entasser dans un tiroir (après les avoir appairées), plutôt que de les suspendre à des cintres. 
> 
> De même en informatique, pour chaque type de données, pour chaque utilisation prévue, une structure particulière de données se revèlera (peut-être) plus adaptée qu'une autre.
> 
> #### 1.1.1 Données linéaires
> Intéressons nous par exemple aux **données linéaires**. Ce sont des données qui ne comp

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Analyser un code fourni — Un extrait de code (def numéroté) est donné, à compléter ou à exécuter mentalement ; on évalue la lecture de code et la compréhension de ce qu'il fait.
    gabarit : On considère le code suivant : [code]. [Compléter la ligne n / Donner ce qu'affiche l'appel [appel]].
    exemple réel (autre notion) : « 4. On considère la fonction suite(n) qui reçoit un entier positif et renvoie un entier. 1| def suite(n) : 2| if n == 0 : 3| return 0 4| else : 5| return 3+2*suite(n-2) »
    exemple réel (autre notion) : « 3. Recopier et compléter le code suivant de la méthode annee_anciennete : 1 def annee_anciennete(self): 2 return ...  On considère la classe Personnel qui modélise la liste du personnel d'une entreprise et dont le début de l'implémentation  »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 4. Compléter le constructeur de la classe Processus :  1 class Processus: 4 ...(self, ..., priorite, temps_CPU): 5 ... priorite = priorite 7 ... PID = ... 8 self.temps_utilisation = 0 9 self.temps_CPU = temps_CPU »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C22 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes précisément numérotées d'une fonction à trous ; on évalue la compréhension de la logique locale du code et le respect de la spécification.
    gabarit : Recopier et compléter les lignes [n1] à [n2] de la fonction [nom] afin qu'elle [comportement].
    exemple réel (autre notion) : « 13. Recopier et compléter les lignes 7 à 10 de la fonction sommets_tries, qui prend en paramètre un dictionnaire g représentant un graphe, et qui renvoie la liste des sommets du graphe triés dans l'ordre décroissant de leur degré.   1 def s »
    exemple réel (autre notion) : « 10. Recopier et compléter les lignes 3, 7, 8 et 10 du code ci-dessus pour respecter les contraintes de la classe. »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 2. En vous basant uniquement sur les données du tableau de la figure 1, donner le résultat de la requête suivante :  SELECT id, stock, description FROM Meubles WHERE intitule = 'skap'; »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C2 : Écrire une fonction selon sa signature — L'élève implémente une fonction dont le nom, les paramètres et la valeur de retour sont spécifiés ; on évalue le respect de la spécification et la gestion des cas (vide, absence, modification en place).
    gabarit : Écrire une fonction [nom]([paramètres]) qui prend en paramètre [description des entrées] et qui renvoie [résultat attendu].
    exemple réel (autre notion) : « 11. Écrire une fonction trier qui prend en paramètre une liste mots représentant la liste des couples de mots et qui renvoie un ordre des 6 voyelles compatible avec le classement des mots donnés dans la liste. »
    exemple réel (autre notion) : « 4. Implémenter une fonction representant prenant en paramètre une liste de 0 et de 1 et renvoyant l'entier correspondant. »
    support S1 : Spécification en prose énumérée — Texte décrivant paramètres et comportement par énumérations séparées par des virgules ; l'élève s'appuie sur une spécification rédigée pour coder ou raisonner.
    exemple de support (autre notion) : « a. Parmi les propositions suivantes, recopier celle qui décrit le fonctionnement des entrées/sorties dans une file :  i. Premier entré, dernier sorti  ii. Premier entré, premier sorti  iii. Dernier entré, premier sorti »

Le champ id vaut « I-k_ppv ».