# Plan I-recherche_dichotomique (inedit)

Notion : recherche_dichotomique (Algorithmique) — questions JAMAIS POSÉES aux annales

Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une vraie question. Ou bien le slot vise un détail du cours jamais interrogé.

Règles propres à ce mode :
- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.
- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.
- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.

Extraits du cours :
> [Algorithmique > Diviser pour regner > 1.2 Version récursive]
> #### 1.2.1 Préambule : le slicing
> Pour écrire simplement la version récursive de cet algorithme, nous allons avoir besoin de faire du *slicing* (découpage) de listes. Cette manipulation n'est pas au programme de NSI (même si elle est très simple). Attention, elle a un coût algorithmique important, qui peut fausser notre analyse de complexité.
> 
> Exemples de slicing :
> 
> ```python
> >>> lst = ['a', 'b', 'c', 'd', 'e']
> >>> lst[:2]
> ['a', 'b']
> >>> lst[2:]
> ['c', 'd', 'e']
> ```
> 
> On comprend que  :
> 
> - ```lst[:k]``` va renvoyer la sous-liste composée du premier élément jusqu'à celui d'indice ```k``` **non inclus**.
> - ```lst[k:]``` va renvoyer la sous-liste composée du ```k```-ième élément (**inclus**) jusqu'au dernier.
> - plus généralement, ```lst[k:p]``` va renvoyer la sous-liste composée du ```k```-ième élément (**inclus**) jusqu'au ```p```-ième (**non inclus**).
> 
> #### 1.2.2 Dichotomie récursive avec 
> [Algorithmique > Diviser pour regner > 1.1 Version impérative]
> {#
> 
>     ```python linenums='1'
>     def recherche_dichotomique(tab, val) :
>         '''
>         renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
>         '''
>         ...
>     ```
> #}
> 
>     ```python linenums='1'
>     def recherche_dichotomique(tab, val) :
>         '''
>         renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
>         '''
>         i_debut = 0
>         i_fin = len(tab) - 1
>         while i_debut >> tab = [1, 5, 7, 9, 12, 13]
> >>> recherche_dichotomique(tab, 12)
> True
> >>> recherche_dichotomique(tab, 17)
> False
> ```
> 
> À chaque tour de la boucle ```while```, la taille de la liste est divisée par 2. Ceci confère à cet algorithme une **complexité logarithmique** (bien meilleure qu'une complexité linéaire).

Questions à rédiger (points = 1 par défaut) :

- slot 1 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : début d'exercice (question d'entrée)
    manière de demander C2 : Compléter des lignes de code numérotées — L'élève recopie et complète des lignes désignées par leur numéro dans un code fourni. On évalue la compréhension locale de l'algorithme.
    gabarit : Recopier et compléter les lignes [n1], [n2] et [n3] de la fonction [nom].
    exemple réel (autre notion) : « 13. return annexe(h) 6. Recopier sur la copie les lignes 7 et 11 en complétant les points de suspension.  Annexe 1 de l'exercice 2, à rendre avec la copie. »
    exemple réel (autre notion) : « 5. Recopier et compléter les lignes 14, 15, 16 et 17 de la méthode placer_mines de la classe demineur. »
    support S9 : Prose ponctuée de nombres isolés — Texte ordinaire contenant quelques nombres (numéros, hauteurs, identifiants). Formes et notions disparates.
    exemple de support (autre notion) : « 5. Écrire une requête SQL permettant d'insérer cette nouvelle exoplanète dans la base de données. »

- slot 2 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C3 : Lire ou compléter une classe Python fournie — L'élève s'appuie sur un code Python donné (classe, def) pour le compléter ou l'utiliser. On évalue la lecture de code orienté objet.
    gabarit : On donne la classe [Classe] ci-dessous : [code]. Recopier et compléter la méthode [nom].
    exemple réel (autre notion) : « 1. Dessiner l'arbre donné par le dictionnaire suivant, qui correspond au dossier Documents . Documents = { "Administratif":{ "certificat JDC.pdf ": 1500, "attestation recensement.pdf ": 850 },  "Cours": {  "NSI": { "TP.html ": 60, "dm.odt": »
    exemple réel (autre notion) : « 5. La fonction code_morse(n, car) permet de traduire un caractère car présent dans l'arbre n et renvoie son code morse sous forme d'une chaîne de caractères. 8. 9. 10. def code_morse(n, car):  if n.valeur == car :  return ………… G : - - o M : »
    support S3 : Code Python à lignes numérotées — Programme Python fourni avec numéros de ligne, souvent incomplet. L'élève le lit, le complète ou en cite une ligne.
    exemple de support (autre notion) : « 12. Indiquer la valeur affectée à la variable i_cat au cours de l'appel mystere(dict_perf_5km, 'SH'). »

- slot 3 | combinaison_inedite | manière de demander jamais utilisée pour cette notion | position visée : fin d'exercice (question qui conclut)
    manière de demander C9 : Question directe « quel est » — L'élève répond à une question ouverte ou un QCM introduit par « quel ». On évalue l'identification d'un élément ou d'une propriété.
    gabarit : Quel est [élément] de [objet] ? [Justifier.]
    exemple réel (autre notion) : « 3. Combien de machines pourront avoir une adresse IPv4 sur ce réseau ? »
    exemple réel (autre notion) : « 11. Expliquer, en justifiant, le rôle de la fonction mystere. »
    support S11 : Texte contenant des tirets — Matériau marqué par des tirets (mots composés, puces, listes chaînées). Artefact typographique mêlant fonctions récursives et énigmes.
    exemple de support (autre notion) : « 2. Pour la validation du paiement, est-il préférable d'utiliser le protocole HTTP ou HTTPS ? Pourquoi ? »

- slot 4 | savoir_jamais_evalue | détail du cours évaluable jamais interrogé aux annales | position visée : milieu d'exercice
    manière de demander C7 : Questions autour d'une base de données — L'élève raisonne sur une base de données (erreur de suppression, contraintes, données), avec quelques intrus hors BDD. On évalue la compréhension du modèle relationnel.
    gabarit : On cherche à [action] dans la base [nom]. Expliquer [phénomène].
    exemple réel (autre notion) : « 12. Déterminer le chemin suivi par un paquet de données pour aller du routeur R8 au routeur R3 et donner son coût en respectant le protocole OSPF. EN_OODgzNT7QzNjAc0ND8UzMsTYxMj5A2NTAAwMDfAxNCjIx »
    détail du cours à évaluer (Diviser pour regner) : « Les algorithmes de dichotomie présentés ci-dessous ont tous en commun de diviser par deux la taille des données de travail à chaque étape. »

Le champ id vaut « I-recherche_dichotomique ».