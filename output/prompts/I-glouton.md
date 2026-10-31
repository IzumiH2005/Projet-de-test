# Plan I-glouton (inedit)

Notion : glouton (Algorithmique) — questions JAMAIS POSÉES aux annales

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
> [Algorithmique > Programmation dynamique > 1. Retour sur l'algorithme glouton]
> Nous avons vu en Première un algorithme capable de donner une combinaison de pièces pour rendre la somme ```somme```.
> 
> Cet algorithme fonctionnait de manière gloutonne : on cherche à rendre à chaque fois la plus grosse pièce possible.
> 
>     Compléter la fonction ```rendu_glouton``` qui prend en paramètres une liste de pièces ```pieces``` (classées dans l'ordre **croissant**) et la somme à rendre ```somme``` et qui renvoie **le nombre minimal** de pièces qu'il faut rendre.
> 
>     ```python linenums='1'
>     def rendu_glouton(pieces, somme):
>         i =  ... # (1)
>         nb_pieces = ...
>         while ... > ...:
>             if ... >> rendu_glouton([1, 2, 5], 12)
>     3
>     ``` 
> 
>     
> 
> Nous savons que cet algorithme est optimal sous certaines conditions sur la composition des pièces. Par exemple le système des euros (1, 2, 5, 10, 20, 50, 100, 200) rend l'algorithme glouton optimal (on dit que le

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C18 : Tracer une boucle Python donnée — L'élève suit l'exécution d'un code avec boucles for/range pour en déduire une valeur ou un affichage. On évalue la trace d'exécution.
    gabarit : Déterminer la valeur de [variable] à l'issue des instructions suivantes : [code].
    exemple réel (autre notion) : « 7. renvoyer mystereABR(filsgauche(a)) »
    exemple réel (autre notion) : « 9. L.append(L2[i2]) »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 8. Recopier et compléter le code Python pour la méthode tarif de la classe Course suivant.  1 def tarif(self):  2 type_vehicule = ...  3 donnees_tarifaire = vehicules[type_vehicule]  4 prise_en_charge = ...  5 tarif_h = ...  6 prix_km = ...  7 tarif = ...  8 t »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 4. a. Recopier sur la copie et compléter les points de suspension ... du code de la fonction regleA ci-dessous pour qu'elle renvoie True si la chaîne passée en paramètre est construite suivant la règle A, et False sinon. def regleA(chaine): »
    exemple réel (autre notion) : « 4. Écrire le code de la méthode est_resultat pour la classe Noeud. »
    support S1 : Spécification de fonction en prose — Une phrase décrit une fonction à écrire ou compléter (nom, paramètre, valeur renvoyée). L'élève traduit cette description en code.
    exemple de support (autre notion) : « 7. En utilisant la fonction eff_dico précédente, écrire une fonction majo_abs2 qui prend en paramètre une liste lst, et qui renvoie son élément absolument majoritaire s'il existe et renvoie None sinon. »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « c. Écrire une fonction insertion(kppv, idx, d)qui insère le tuple (idx, d) dans la liste kppv préalablement triée en préservant l'ordre décroissant selon l'élément d. »
    exemple réel (autre notion) : « 1. Compléter le constructeur qui renvoie un objet Marchandise. Utiliser le mot-clé assert afin qu'une exception soit levée si le paramètre v n'est pas strictement positif. On rappelle que si condition est une expression Python booléenne s'é »
    support S14 : Prose avec parenthèses — Phrases contenant des parenthèses (couples, types, précisions). Artefact de ponctuation sans matériau commun.
    exemple de support (autre notion) : « 9. Dans le cas où arret(code_paradoxe, code_paradoxe) renvoie True, préciser la prochaine instruction à être exécutée. Dans ce cas, expliquer si l'appel paradoxe(code_paradoxe) termine. »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C14 : Écrire le code d'une méthode — L'élève rédige intégralement le code d'une fonction ou méthode décrite. On évalue la programmation, souvent en POO.
    gabarit : Écrire le code de la méthode [nom] de la classe [Classe] qui [comportement].
    exemple réel (autre notion) : « 1. Donner pour la table Agences un type possible pour l 'attribut CP qui indique le code postal. »
    détail du cours à évaluer (Programmation dynamique) : « Compléter la fonction _glouton ci-dessous qui calcule de manière gloutonne le "meilleur" trajet d'une pyramide »

Le champ id vaut « I-glouton ».