# Plan B-chaines (banque)

Notion : chaines (Programmation) — banque de questions isolées
Extraits du cours :
> [Structures de données > Dictionnaires > 2.2 Mécanisme de la fonction de hachage]
> Quelle que soit la taille du fichier donné en entrée, la fonction MD5 va le réduire à un mot de 128 bits.
> Ce mot binaire de 128 bits est représenté par une chaîne de 32 caractères (en hexadécimal, de 0 à f). Il y a donc $2^{128}$ (de l'ordre de $10^{39}$) empreintes MD5 différentes, ce qui rend quasiment impossible le fait d'avoir un mauvais fichier qui donnerait (par un très très mauvais hasard) la bonne empreinte.
> 
> Le mécanisme effectif de calcul de la fonction MD5 est très complexe : une explication en est donnée ici.
> 
> Il est évidemment **impossible** de revenir en arrière et de recréer le fichier original à partir de l'empreinte MD5. Dans le cas contraire, cela voudrait dire qu'on est capable de compresser *sans perte* un fichier de 1,9 Go en une chaîne de 128 bits. Cette impossibilité de trouver une fonction réciproque à la fonction de hachage est très importante en cryptographie.
> 
> 
> [Structures de données > Dictionnaires > Exercices sur les dictionnaires]
> On considère la liste suivante :
> 
>     ```lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']``` 
> 
>     Quel est le **chiffre** qui revient le plus fréquemment dans cette liste ?
> 
>      
>     {{
>     correction(True,
>     """
> \"Correction\" 
>         ```python linenums='1'
>         lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053',
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=expliquer / explication / comprendre | Bloom=comprendre | formulations typiques : indiquer, expliquer, preciser, quel
    style réel : « 9. Étudier si le programme paradoxal termine ou non, c'est -à-dire si
exec(programme_paradoxal) termine ou non. »
- slot 2 | archétype=ecrire_fonction / code_python / créer | Bloom=créer | formulations typiques : ecrire, ecrire fonction, fonction, prend
    style réel : « 8. Écrire le code de la fonction premiere_diff qui prend en paramètres deux
chaînes de caractères mot1 et mot2 représentant deux mots distincts et qui
renvoie le premier indice où les deux lettres sont différentes. Si l' »
- slot 3 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « 6. Déterminer un numéro de licence possible pour Eddie Nirrer né le 12/10/2021. »
- slot 4 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier completer, fonction, recopier
    style réel : « 3. On modélise les choix du joueur par une chaî ne de caractères qui contient les
caractères "D" (le joueur se déplace sur la case juste à droite) ou "XS" (le joueur
saute une case toujours sur la droite).
Écrire une fo »

Le champ id vaut « B-chaines ».