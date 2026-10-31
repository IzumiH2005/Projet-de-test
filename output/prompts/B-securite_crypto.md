# Plan B-securite_crypto (banque)

Notion : securite_crypto (Architecture, OS et réseaux) — banque de questions isolées
Extraits du cours :
> [Architecture, OS et réseaux > Cryptographie > 1.2 Principe du chiffrement symétrique]
> Dans un chiffrement symétrique, c'est **la même clé** qui va servir au chiffrement et au déchiffrement.
> 
> *Illustration :*
> 
> #### :arrow_right: Qu'appelle-t-on une clé ?
> La clé est un renseignement permettant de chiffrer ou déchiffrer un message. Cela peut être :
> 
> - un nombre (dans un simple décalage des lettres de l'alphabet, comme le chiffre de César)
> - une phrase (dans la méthode du masque jetable)
> - une image (imaginez un chiffrement où on effectue un XOR par les pixels d'une image, comme dans cette énigme)
> 
> Un chiffrement est dit symétrique lorsque la connaissance de la clé ayant servi au chiffrement permet de déchiffrer le message. Par exemple, Alice chiffre son message en décalant les lettres de 3 rangs vers la droite dans l'alphabet, Bob saura qu'il doit les décaler de 3 rangs vers la gauche pour retrouver le message initial.
> 
> #### :arrow_right: Quel est l'avantage d'un chiffrement
> [Architecture, OS et réseaux > Cryptographie > 2.2 Le rôle interchangeable des clés publiques et privées]
> L'illustration précédente associe :
> 
> - une image de cadenas à la clé publique (car on s'en sert pour chiffrer les messages)
> - une image de clé à la clé privée (car on s'en sert pour déchiffrer les messages)
> 
> Concrètement, (nous le verrons dans l'application par le chiffrement RSA), la clé privée et la clé publique sont **deux nombres** aux rôles identiques. Appelons-les A et B :
> 
> - il est impossible de trouver A en fonction de B. Réciproquement, si on connaît A, il est impossible d'en déduire B.
> - si on chiffre un message avec A, on peut le déchiffrer avec B. Réciproquement, si on chiffre avec B, on peut déchiffrer le message grâce à A.
> - on peut donc chiffrer avec une clé publique et déchiffrer avec la clé privée associée (ce qui est fait dans l'exemple précédent). Mais on peut aussi chiffrer avec la clé privée, et déchiffrer avec la clé publique associée.
> 
> A et B ont donc des rôles int
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, fonction
    style réel : « 14. Recopier et compléter les lignes 8 à 11 du code de la méthode chiffrer ci-
après.
 1 def chiffrer(self, octet):
 2 '''
 3 renvoie le chiffrement de octet
 4 : paramètre octet (list) un tableau de huit 0 ou 1
 5 : ret »
- slot 2 | archétype=expliquer / explication / évaluer | Bloom=évaluer | formulations typiques : justifiant, indiquer justifiant, indiquer, verifier
    style réel : « 10. Décrire ce que doit désormais réaliser Bob pour vérifier l'authenticité du
message, c'est-à-dire qu'il a bien été envoyé par Alice. »
- slot 3 | archétype=autre / explication / appliquer | Bloom=appliquer | formulations typiques : donner, determiner, arbre, liste
    style réel : « b. Chiffrer la chaîne de caractères "BAGAGE" avec le dictionnaire alpha . »
- slot 4 | archétype=expliquer / explication / comprendre | Bloom=comprendre | formulations typiques : indiquer, expliquer, preciser, quel
    style réel : « 9. Expliquer la différence de fonctionnement entre les chiffrements symétrique et
asymétrique. »

Le champ id vaut « B-securite_crypto ».