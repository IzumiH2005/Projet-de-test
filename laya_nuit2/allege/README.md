# Laya nuit 2 allégé (français + anglais)

647 Mo -> 459 Mo (256 000 -> 142 776 tokens). Couches inchangées, seules les lignes
d'embedding des tokens inutiles sont retirées.

Tokens gardés (`keep_union.json.gz`) :
- la liste anglais/français de laya-multilingual-en-fr ;
- tous les tokens utilisés par les 230 000 exemples d'entraînement et d'évaluation ;
- leurs variantes en majuscules ;
- tous les tokens intermédiaires de leurs fusions BPE (découpage strictement identique).

Vérification : découpage identique sur 4 977 / 4 977 phrases (éval + pièges),
même score à l'éval complète (0,838) et aux 27 pièges (22/27).

Refaire : `python prune_vocab.py <laya_fr> <sortie> keep_union.json`
