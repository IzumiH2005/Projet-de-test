# Plan B-mise_au_point (banque)

Notion : mise_au_point (Programmation) — banque de questions isolées
Extraits du cours :
> [Programmation > Pratiques de programmation > 1. Conventions syntaxiques]
> La programmation est un art délicat : un simple caractère en trop peut provoquer une erreur pour le code tout entier (penser à un innocent caractère d'espace en début de ligne dans un code Python).
> 
> Mais même lorsqu'un code s'exécute sans erreur, il ne faut pas négliger l'aspect purement «esthétique» de celui-ci : il est nécessaire de respecter autant que possible des conventions typographiques, qui vont standardiser le code et le rendre ainsi plus lisible.
> 
> Ainsi pour chaque langage, il existe une «bible» de bonnes pratiques de présentation du code, qui visent à l'uniformiser. Pour Python, cette référence s'appelle la Python Enhancement Proposal 8, plus connue sous le nom de PEP8. 
> 
> En voici quelques extraits :
> [Programmation > Pratiques de programmation > 4.1 Pourquoi des tests ?]
> Tester une fonction est la première chose que l'on fait (normalement...) lorsqu'on vient de finir de l'écrire. 
> 
> Par exemple, si on vient de construire la fonction ```valeur_absolue(n)```, il est fort probable qu'on aille taper ceci dans la console :
> 
> ```python
> >>> valeur_absolue(-3)
> 3
> >>> valeur_absolue(0)
> 0
> >>> valeur_absolue(7)
> 7
> ```
> 
> - On peut regrouper tous ces tests au sein d'une même fonction ```test_valeur_absolue()```.
> - On peut écrire cette fonction ```test_valeur_absolue()``` avant même de commencer à écrire la fonction ```valeur_absolue(n)```.
> 
> > Remarque : 
> > la méthode de développement logiciel TDD (Test Driven Developement) est basée en partie sur ce principe  : 
> 
> > 1. On commence par écrire le test de la fonction.
> > 2. Le test échoue (forcément, la fonction n'est pas encore codée !)
>  > 3. On écrit le code de la fonction pour que le test soit validé.
>  > 4. On améliore (si 
Questions à rédiger (exercice numéro 0, points = 1 par défaut) :
- slot 1 | archétype=corriger_code / explication / analyser | Bloom=analyser | formulations typiques : erreur, corriger, expliquer, pourquoi
    style réel : « 3) On cherche à supprimer un acteur de la base. Une fois la requête correspondante
lancée, le message d'erreur suivant apparaît.
Indiquer ce qui a pu provoquer cette erreur.

ERREUR
Requête SQL :
DELETE FROM `Acteur` WHE »
- slot 2 | archétype=completer_code / code_python / appliquer | Bloom=appliquer | formulations typiques : completer, recopier, recopier completer, fonction
    style réel : « 4. Recopier et compléter les lignes 10 à 12 de la méthode soutenir, en
respectant sa documentation. »
- slot 3 | archétype=justifier_choix / explication / évaluer | Bloom=évaluer | formulations typiques : justifier, recursive, citer, fonction
    style réel : « 3. Justifier que la boucle de la fonction précédente se termine. »

Le champ id vaut « B-mise_au_point ».