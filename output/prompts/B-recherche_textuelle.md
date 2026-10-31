# Plan B-recherche_textuelle (banque)

Notion : recherche_textuelle (Algorithmique) — banque de questions isolées
Extraits du cours :
> [Algorithmique > Recherche textuelle > 2.2 Implémentation]
> #### 2.2.1 Fonction préparatoire
> On va d'abord coder une fonction ```dico_lettres``` qui prend en paramètre un mot ```mot``` et qui renvoie un dictionnaire associant à chaque lettre de ```mot``` son dernier rang dans ```mot```. On exclut la dernière lettre, qui poserait un problème lors du décalage (on décalerait de 0...) 
> 
>     Écrire la fonction ```dico_lettres```.
> 
>     *Exemple d'utilisation :*
> 
>     ```python
>     >>> dico_lettres("MAURIAC")
>     {'M': 0, 'A': 5, 'U': 2, 'R': 3, 'I': 4}
>     ```
> 
>     {{
>     correction(True,
>     """
> \"Correction\" 
>         ```python linenums='1'
>         def dico_lettres(mot):
>             d = {}
>             for i in range(len(mot)-1):
>                 d[mot[i]] = i
>             return d
>         ``` 
>     """
>     )
>     }}
> 
> #### 2.2.2 Boyer-Moore-Horspool
>   
> codes à trous
> 
> {#
> 
>     
>     ```python linenums='1'
>     def dico_lettres(mot):
>         
> 
>     def BMH(texte
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
- slot 1 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, fonction
    style réel : « 5. Recopier et compléter le code de la fonction occurrence ci-dessous qui, pour
un texte passé en paramètre, renvoie le dictionnaire d'occurrences associé.

1 def occurrence(texte):
2 dico = {}
3 for lettre in ... :
4 if »
- slot 2 | archétype=autre / explication / créer | Bloom=créer | formulations typiques : ecrire, python, proposer, permettant
    style réel : « 3. Écrire le tableau d'occurrences associé à la chaîne de caractères txt. »
- slot 3 | archétype=trace_execution / valeur / appliquer | Bloom=appliquer | formulations typiques : apres, apres execution, execution, renvoie
    style réel : « 9. Donner le résultat de l'appel recherche('na', 'banana'). »

Le champ id vaut « B-recherche_textuelle ».