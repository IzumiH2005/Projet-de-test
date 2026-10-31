# Plan I-diviser_regner (inedit)

Notion : diviser_regner (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Diviser pour regner > Vers l'algorithme d'interclassement]
> Pour interclasser deux listes triées ```lst1``` et ```lst2```.
> 
>     - on part d'une liste vide ```lst_totale```
>     - on y ajoute alternativement les éléments de ```lst1``` et ```lst2```, en veillant à maintenir un ordre croissant. Il faut pour cela gérer séparément un indice ```i1``` pour la liste ```lst1```  et un indice ```i2```  pour la liste ```lst2```.
>     - quand une liste est épuisée, on y ajoute la totalité restante de l'autre liste.
> 
> Exemple d'utilisation :
> 
> ```python
> >>> interclassement([2, 4, 5, 13, 15, 19], [3, 7, 8, 10, 16])
> [2, 3, 4, 5, 7, 8, 10, 13, 15, 16, 19]
> ```
> 
>     ```python linenums='1'
>     def interclassement(lst1, lst2):
>         ...
>                            
>     ``` 
>  
>     ```python linenums='1'
>     def interclassement(lst1, lst2):
>         i1 = ...
>         i2 = ...
>         lst_totale = ...
>         while ...:
>             if ...:
>                 lst_totale.append(
> [Algorithmique > Diviser pour regner > 4.2 La fusion]
> #### 4.2.1 Principe
> 
> L'idée du tri fusion est le découpage de la liste originale en une multitude de listes ne contenant qu'un seul élément. Ces listes élémentaires seront ensuite interclassées avec la fonction précédente.
> 
> **Principe de l'algorithme du tri fusion :**
> 
> - pour trier une liste, on interclasse les deux moitiés de cette liste, précédémment elles-mêmes triées par le tri fusion.
> - si une liste à trier est réduite à un élément, elle est déjà triée. 
> 
> #### 4.2.2 Implémentation
> 
> La grande force de ce tri va être qu'il se programme simplement de manière **récursive**, en appelant à chaque étape la même fonction mais avec une taille de liste divisée par deux, ce qui justifie son classement parmi les algorithmes utilisants «diviser pour régner».
> 
> {#
> 
>   
>     ```python
>     def interclassement(lst1, lst2):
>         ...
> 
>     def tri_fusion(lst):
>         ...
>     ```
> #}
> 
>     
>     ```python

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | combinaison inédite d'éléments connus | position visée : milieu d'exercice
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 14. Donner en justifiant le nombre d'appels récursifs effectués par l'appel de valmax_dynamique(6), après l'exécution de valmax_dynamique(5). »
    exemple réel (autre notion) : « Question 1 On considère tous les chemins allant de la case (0, 0) à la case (2, 3) du tableau T donné en exemple. 1. Un tel chemin comprend nécessairement 3 déplacements vers la droite. Combien de déplacements vers le bas comprend-il? »
    support S6 : Texte avec parenthèses explicatives — Support riche en parenthèses (signatures, précisions, sous-questions (a)(b)) ; l'élève doit tenir compte des précisions et des paramètres annoncés.
    exemple de support (autre notion) : « 7. Lors de la célèbre cérémonie des vœux, l'entreprise souhaite mettre à l'honneur les personnes ayant exactement 10 ans d'ancienneté dans l'entreprise. Écrire une méthode de la classe Personnel nb_personne_honneur qui prend en paramètre l'année de la cérémoni »

- slot 2 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C9 : Prédire le résultat d'un appel — À partir d'un appel ou d'une instruction avec arguments explicites, l'élève donne la valeur renvoyée ou l'état obtenu ; on évalue la trace d'exécution précise, cas limites compris.
    gabarit : Donner la valeur renvoyée par [appel([arguments])] / l'état de [structure] après [instruction].
    exemple réel (autre notion) : « 10. Écrire un programme permettant de créer et d'entrainer le détecteur sur les listes emails = [[0, 0], [0, 1], [1, 0], [1, 1]] et spams = [0, 0, 0, 1]. pendant au maximum 1000 époques, puis d'afficher dans la console le nombre d'époques n »
    exemple réel (autre notion) : « 3. Edgar réalise l'appel tri_dictatorial([8, 2, 9, 6, 12]).  Expliquer pas à pas comment la liste serie_triee se construit après cet appel. »
    support S0 : Énoncé en prose avec numéros — Support textuel ordinaire mêlant prose et nombres (routeurs, adresses, tailles) ; l'élève travaille à partir d'une mise en situation décrite, sans matériau structuré dominant.
    exemple de support (autre notion) : « 7. Recopier et compléter les lignes 12, 16 et 20 du code de la fonction lire_parcours. »

- slot 3 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C19 : Déterminer un chemin ou élément — Questions de détermination (chemin d'un paquet, répertoire, sous-séquence, protocole) sans geste unique, souvent en réseau ; on évalue une déduction à partir du contexte.
    gabarit : Déterminer [le chemin/l'élément] [de A à B / vérifiant la condition] dans [situation].
    exemple réel (autre notion) : « 3. Déterminer le chemin parcouru par un paquet partant du serveur patients (SP) vers le service de radiologie (RL R) en utilisant le protocole OSPF. On précisera également le coût de ce chemin. »
    détail du cours à évaluer (Diviser pour regner) : « Pour finir, une jolie animation permettant de comparer les tris : »

Le champ id vaut « I-diviser_regner ».