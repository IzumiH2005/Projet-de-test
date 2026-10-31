# Plan I-modularite (inedit)

Notion : modularite (Programmation) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Programmation > Modularite > Modularite]
> Terminale - Spécialité NSI IFS Singapour
> Chapitre 10 - Modularité
> Objectifs :
> ▷ Savoir utiliser des bibliothèques
> ▷ Exploiter leur documentation
> ▷ Créer des modules simples et les documenter.
> 1 Introduction
> Laprogrammation modulaireconsiste à décomposer une grosse application en modules que l'on peut ensuite
> améliorer et utiliser indépendamment dans d'autres applications.
> Cette méthode réalise uneencapsulation comparable à celle de la programmation orientée objet.
> Un module doit être conçu pour pouvoir être utilisé par d'autres utilisateurs comme une interface qui fournit
> des données (math.pi, math.e...), des objets (structures de données comme les piles, les arbres, les graphes,
> ..., etc.) et des traitements (fonctions, méthodes), sans rentrer dans le code du module.
> Il faut donc prévoir unedocumentation claire et complète.
> 2 Exemples
> Nous avons déjà créé des modules en implémentant des
> [Programmation > Pratiques de programmation > 2.2 Le cas particulier des ```docstrings```]
> #### 2.2.1 Que sont les ```docstrings```?
> 
> Les ```docstrings``` sont des commentaires *normalisés* pour les fonctions, qui peuvent être consultés en console.
> 
> **Exemples :**
> 
> Nous connaissons la fonction ```len()``` qui permet par exemple de connaître la longueur d'une liste passée en paramètre.
> 
> Si nous tapons en console la commande ```print(len.__doc__)```, nous aurons la description de cette fonction. 
> 
> ```python
> >>> len.__doc__
> 'Return the number of items in a container.'
> ```
> Il est aussi possible d'accéder à la docstring d'une fonction ```f```  par la commande ```help(f)``` :
> 
> ```python
> >>> help(len)
> Help on built-in function len in module builtins:
> 
> len(obj, /)
>     Return the number of items in a container.
> 
> ```
> 
> De même pour la fonction ```range``` :
> ```python
> >>> print(range.__doc__)
> range(stop) -> range object
> range(start, stop[, step]) -> range object
> 
> Return an object that pro

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C4 : Donner la valeur ou l'élément demandé — L'élève fournit un résultat ponctuel (requête, codage, table) désigné par « donner la ». On évalue l'exactitude du résultat, sur des notions variées.
    gabarit : Donner la [requête|valeur|table] de [objet] [condition].
    exemple réel (autre notion) : « 1. (a) Donner la clé primaire et les éventuelles clés étrangères de la relationSport. (b) Citer une contrainte d'intégrité de domaine puis une contrainte d'intégrité de relation et enﬁn une contrainte d'intégrité de référence que doivent re »
    exemple réel (autre notion) : « 2. Donner la table de routage de F à l'initialisation du protocole RIP. »
    support S10 : Prose riche en virgules — Phrases longues avec énumérations par virgules ou listes de choix. Artefact de ponctuation, contenus variés.
    exemple de support (autre notion) : « 4. Ecrire une requête qui affiche le nom, le prénom et la note des élèves ayant fait le QCM Arbre Binaire . L'utilisation des trois tables dans la requête est attendue.  22-NSIJ1LR1 Page 10 sur 16 »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « 2. Finaliser le programme précédent en complétant les lignes 6, 7 et 8 sur votre copie. »
    exemple réel (autre notion) : « 10. Recopier et compléter les lignes 4 et 6 du code ci-après de la méthode m_a_j. EN_OOTgzNT7QzNjAc0ND4UzMsTYxMj4A2NTAAwMDcAxNRjIx 26-NSIJ1JA1 Page 15 sur 16  1 def m_a_j(self, passerelle, i_interf, vecteurs): 2 a_ete_modif = False 3 for ad »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 13. Expliquer le test de la ligne 6 du code de la fonction maj. »

- slot 3 | combinaison_inedite | support jamais utilisé pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 14. Recopier et compléter les lignes 8 à 11 du code de la méthode chiffrer ci- après.  1 def chiffrer(self, octet):  2 '''  3 renvoie le chiffrement de octet  4 : paramètre octet (list) un tableau de huit 0 ou 1  5 : return (int)  6 '''  7  »
    exemple réel (autre notion) : « 12. Compléter la méthode reduire qui permet d'appliquer cette règle récursivement pour réduire la taille d'un arbre de décision binaire. 1 def reduire(self): 2 """fonction récursive qui réduit la taille d'un arbre de 3 décision sans changer »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 5. g=hauteur(gauche(A)) »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C19 : Écrire une fonction avec paramètres spécifiés — L'élève écrit une fonction dont les paramètres et la valeur renvoyée sont décrits. On évalue le respect de la spécification et l'algorithme.
    gabarit : Écrire une fonction [nom] qui prend en paramètres [p1] et [p2] et qui renvoie [résultat].
    exemple réel (autre notion) : « b) Recopier et compléter le programme implémentant la fonction récursive hauteur qui prend en argument un arbre binaire A et qui renvoie la hauteur de cet arbre. »
    détail du cours à évaluer (Pratiques de programmation) : « Il est aussi possible d'accéder à la docstring d'une fonction »

Le champ id vaut « I-modularite ».