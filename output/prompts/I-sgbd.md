# Plan I-sgbd (inedit)

Notion : sgbd (Bases de données) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Programmation Orientee Objet > Exercices]
> **Q1.** Écrire une classe ```Eleve``` qui contiendra les attributs ```nom```, ```classe``` et ```note```.
>     
> 
>     **Q2.** Instancier trois élèves de cette classe.
>     
> 
>     **Q3.**  Écrire une fonction ```compare``` qui prend en paramètres deux élèves ```eleve1``` et ```eleve2``` qui renvoie le nom de l'élève ayant la meilleure note (on ne traitera pas à part le cas d'égalité).
> 
>         ```python
>         >>> riri = Eleve("Henri", "TG2", 12)
>         >>> fifi = Eleve("Philippe", "TG6", 15)
>         >>> loulou = Eleve("Louis", "TG1", 8)
>         >>> compare(riri, fifi)
>         'Philippe'
>         ```
> 
>     
>     Écrire une classe ```TriangleRect``` qui contiendra les attributs ```cote1```, ```cote2``` et ```hypotenuse```.
> 
>     La méthode constructeur ne prendra en paramètres que ```cote1``` et ```cote2```, l'attribut ```hypotenuse``` se calculera automatiquement.
> 
>         ```python
>         >>>
> [Bases de données > Langage SQL > 2. Création et modification d'une base de données]
> _rappel_ : 
> 
> L'objectif est de créer la table suivante :
> 
> | id | Nom | Maths | Anglais | NSI |
> |:-----:|:-----:|:-------:|:----:|:----:|
> | 1 | Alice | 16 | 11 | 17 |
> | 2 | Bob  | 12 | 15 | 10 |
> | 3 | Charles | 9 | 11 | 18 |
> 
> #### 2.1 Exemple 15 
> 
> *La création d'une table n'est pas explicitement au programme de NSI. Personne ne sait vraiment pourquoi*
> 
>     - **Commande :** 
>     ```sql
>     CREATE TABLE Table_notes (
>             Id INTEGER PRIMARY KEY,
>             Nom TEXT,
>             Maths INTEGER,
>             Anglais INTEGER,
>             NSI INTEGER
>             );
>     ``` 
>     - **Remarque :**  
>     C'est l'utilisateur qui spécifie, éventuellement, quel attribut sera une clé primaire.
> 
>     - **Résultat :**  
>     Dans DB Browser, il faut avoir au préalable créé une nouvelle base de données.
> 
> #### 2.2 Exemple 16 
> 
>     - **Commande :** 
>     ```sql
>     INSERT INTO Table_notes 
>     VALUES (1,

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 2. Indiquer si l'appel f1(-2) se termine. Si oui, indiquer la valeur renvoyée. »
    exemple réel (autre notion) : « 8. Dessiner l'arbre binaire représenté par le tuple (((None, (1, 34), None), (2, 35), None), (11, 36), (None, (17, 30), None)). L'arbre construit à partir de la liste etoiles a donc pour représentation Python : (((None, (10, 30), None), (15 »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 7. Recopier et compléter les lignes 3, 5 et 6 de le fonction degre qui prend en paramètre la matrice d'adjacence d'un graphe donné sous forme d'une liste de listes et qui renvoie la liste des degrés de tous les sommets du graphe rangés dans le même ordre que l »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C5 : Question directe à réponse courte — Question interrogative (quel, que renvoie, est-il…) appelant une identification ou un choix, souvent suivi de « Justifier » ; on évalue une lecture précise et une décision argumentée.
    gabarit : Quel(le) [élément] [condition] ? Justifier.
    exemple réel (autre notion) : « c. En quoi la solution obtenue par cette approche est-elle plus avantageuse que celle de la question 2.b. ?  Annexe de l'exercice 2 à rendre avec la copie. »
    exemple réel (autre notion) : « b. Quelle valeur sera alors affectée à la variable res ? »
    support S4 : Liste à tirets ou intitulés — Support comportant des listes à tirets, intitulés courts ou termes composés ; l'élève s'appuie sur une énumération d'éléments ou de propositions.
    exemple de support (autre notion) : « 2. Le répertoire courant dans le terminal est /association. Parmi les commandes systèmes suivantes, identifier celle qui permet de définir annonces comme répertoire courant. – cd /annonces – cd ../annonces – cd annonces – cd association/annonces Les quatre pre »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Analyser un code fourni — Un extrait de code (def numéroté) est donné, à compléter ou à exécuter mentalement ; on évalue la lecture de code et la compréhension de ce qu'il fait.
    gabarit : On considère le code suivant : [code]. [Compléter la ligne n / Donner ce qu'affiche l'appel [appel]].
    exemple réel (autre notion) : « 1. On donne la fonction suivante.  def fonction1(tab, i):  nb_elem = len(tab)  cpt = 0  for j in range(i+1, nb_elem):  if tab[j] < tab[i]:  cpt += 1  return cpt »
    exemple réel (autre notion) : « 4. else : »
    support S2 : Code source fourni — Le support contient du code avec identifiants et affectations (scripts, fonctions à trous, classes) ; l'élève doit lire, compléter ou exécuter mentalement ce code.
    exemple de support (autre notion) : « 8. Expliquer le cas d'arrêt de cette formule récursive. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C20 : Énoncés de mise en situation — Mélange d'énoncés introductifs et de questions descriptives (arbres, parité, interfaces) ; groupe défini par des tournures génériques plutôt que par un geste.
    gabarit : On considère [situation]. Indiquer [éléments] qui [propriété].
    exemple réel (autre notion) : « 3. On considère un arbre binaire R dont on note G le sous-arbre gauche et D le sous-arbre droit. On suppose que R est de hauteur 4 et G de hauteur 2. »
    détail du cours à évaluer (Base de donnees relationnelles) : « La plupart desSGBD-R (R de relationnelle) utilisent le langageSQL, Structured Query Language. »

Le champ id vaut « I-sgbd ».