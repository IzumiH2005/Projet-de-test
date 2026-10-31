# Plan B-modele_relationnel (banque)

Notion : modele_relationnel (Bases de données) — banque de questions isolées
Extraits du cours :
> [Bases de données > Modele relationnel > 6. Les 3 contraintes d'intégrité]
> Tout attribut d'un enregistrement doit respecter le domaine indiqué dans le schéma relationnel.
> 
> Attention, certains domaines sont subtils. Par exemple, si une relation possède un attribut "Code Postal", le domaine de cet attribut devra être ```String``` plutôt que ```Entier``` . Dans le cas contraire, un enregistrement possédant le code postal ```03150``` serait converti en ```3150``` (car pour les entiers, 03150 = 3150). Or le code postal ```3150``` n'existe pas.
> 
>     Tout enregistrement est unique.  
>     Cette contrainte est assurée par l'existence obligatoire d'une clé primaire.
> 
> Cette clé primaire est souvent créée de manière artificielle (voir ```id_emprunteurs```  dans la table ci-dessus par exemple).
> 
>     La cohérence entre les différentes tables d'une base de données est assurée par les clés étrangères : dans une table, la valeur d'un attribut qui est clé étrangère doit obligato
> [Bases de données > Modele relationnel > 3. Clé Primaire]
> Une clé primaire est un attribut (ou une réunion d'attributs) **dont la connaissance suffit à identifier avec certitude un unique enregistrement**.
> 
> Par exemple, la clé primaire de la relation des personnes nées en France pourrait être leur numéro de Sécurité Sociale.
> 
>  Observons, dans notre relation précédente, ce qui peut être une clé primaire et ce qui ne peut pas l'être.
> 
> - Titre : cet attribut pourrait jouer le rôle de clé primaire. En effet, notre table ne contient pas deux livres ayant le même titre.
> - Auteur : cet attribut pourrait jouer le rôle de clé primaire. En effet, notre table ne contient pas deux livres ayant le même auteur.
> - Éditeur : cet attribut ne peut **pas** jouer le rôle de clé primaire. En effet, la donnée de l'attribut «Actes Sud» renvoie vers 4 livres différents.
> - ISBN : (International Standard Book Number) cet attribut est un numéro unique spécifique à chaque
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=lire_sql / sql / appliquer | Bloom=appliquer | formulations typiques : requete, resultat, resultat requete, select
    style réel : « 3. Donner le résultat de la requête suivante en l'appliquant à l'extrait de la table
joueur donné dans l'énoncé.
 SELECT prenom FROM joueur WHERE ann_naiss < 1985 »
- slot 2 | archétype=expliquer / explication / comprendre | Bloom=comprendre | formulations typiques : indiquer, expliquer, preciser, quel
    style réel : « 2) Indiquer la fonction principale du composant SSD (Solid State Drive). »
- slot 3 | archétype=modele_donnees / explication / analyser | Bloom=analyser | formulations typiques : cle, cle primaire, primaire, attribut
    style réel : « 1) Indiquer ce qui différencie les concepts de clé primaire et de clé étrangère. »
- slot 4 | archétype=modele_donnees / explication / analyser | Bloom=analyser | formulations typiques : cle, cle primaire, primaire, attribut
    style réel : « 1. Lister les attributs de la classe Piste en précisant leur type. »

Le champ id vaut « B-modele_relationnel ».