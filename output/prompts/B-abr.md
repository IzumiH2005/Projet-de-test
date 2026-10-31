# Plan B-abr (banque)

Notion : abr (Structures de données) — banque de questions isolées
Extraits du cours :
> [Structures de données > Arbres > 5.3  Coût de la recherche dans un ABR équilibré]
> Imaginons un arbre équilibré de taille $n$. Combien d'étapes faudra-t-il, dans le pire des cas, pour trouver (ou pas) une clé particulière dans cet arbre ?
> 
> Après chaque nœud, le nombre de nœuds restant à explorer est divisé par 2. On retrouve là le principe de recherche dichotomique, vu en classe de Première (voir ici).
> 
> S'il faut parcourir tous les étages de l'arbre avant de trouver (ou pas) la clé recherchée, le nombre de nœuds parcourus est donc égal à la hauteur $h$ de l'arbre.
> 
> Pour un arbre complet, cette hauteur vérifie la relation $2^h -1= n$. et donc $2^h = n+1$.
> 
> $h$ est donc le «nombre de puissance de 2» que l'on peut mettre dans $n+1$. Cette notion s'appelle le logarithme de base 2 et se note $\log_2$.
> 
> Par exemple, $\log_2(64)=6$ car $2^6=64$.
> 
> Le nombre maximal de nœuds à parcourir pour rechercher une clé dans un ABR équilibré de taille $n$ est donc de l'ordre de $\log_2(n
> [Structures de données > Arbres > 5. Arbres binaires de recherche (ABR)]
> Un **arbre binaire de recherche** est un arbre binaire dont les valeurs des nœuds (valeurs qu'on appelle étiquettes, ou clés) vérifient la propriété suivante :
> 
>     - l'étiquette d'un nœud est **supérieure ou égale** à celle de **chaque** nœud de son **sous-arbre gauche**.
>     - l'étiquette d'un nœud est **strictement inférieure** à celle du **chaque** nœud de son **sous-arbre droit**.
> 
> À noter que l'arbre 3 (qui est bien un ABR) est appelé **arbre filiforme**. 
> 
> L'arbre 5 n'est pas un ABR à cause de la feuille 9, qui fait partie du sous-arbre gauche de 3 sans lui être inférieure.
> 
> **Remarque :** on pourrait aussi définir un ABR comme un arbre dont le parcours infixe est une suite croissante.
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=justifier_choix / explication / analyser | Bloom=analyser | formulations typiques : expliquer, pourquoi, expliquer pourquoi, quoi
    style réel : « 10. Expliquer en quoi la fonction inserer est une fonction récursive. »
- slot 2 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, fonction
    style réel : « b. Recopier et compléter la ligne 7 du code de la fonction ins ci-dessous qui
prend en paramètres une valeur v et un arbre binaire de recherche abr et qui
renvoie l'arbre obtenu suite à l'insertion de la valeur v dans l' »
- slot 3 | archétype=calcul_numerique / valeur / appliquer | Bloom=appliquer | formulations typiques : binaire, arbre, arbre binaire, calculer
    style réel : « 3. On donne l'arbre binaire de recherche abr_7_noeuds suivant :
6
4
3
 5
8
7
 9
On donne également ci-dessous la fonction mystere qui prend en paramètres un arbre binaire
de recherche abr, un entier x et une liste liste. »

Le champ id vaut « B-abr ».