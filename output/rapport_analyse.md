# Analyse des annales NSI (Terminale)

Corpus : 83 sujets écrits uniques (299 exercices, 2668 questions), 181 sujets pratiques (362 exercices), 281 sections de cours.
Années : {'2021': 11, '2022': 16, '2023': 14, '2024': 11, '2025': 18, '2026': 13}

## 1. Archétypes de questions (26 formes, KMeans + silhouette)

| # | archétype (tâche / format / Bloom) | n | position moy. | code | dépend d'avant | formulations |
|---|---|---|---|---|---|---|
| 11 | autre / explication / appliquer | 318 | 0.43 | 0.07 | 0.03 | donner, determiner, arbre, liste |
| 5 | ecrire_fonction / code_python / créer | 228 | 0.58 | 0.16 | 0.01 | ecrire, ecrire fonction, fonction, prend |
| 6 | completer_code / code_python / appliquer | 213 | 0.58 | 1.0 | 0.11 | completer, recopier, recopier completer, fonction |
| 8 | ecrire_sql / sql / créer | 200 | 0.55 | 0.04 | 0.01 | ecrire requete, requete, requete sql, ecrire |
| 19 | expliquer / explication / comprendre | 160 | 0.47 | 0.14 | 0.05 | indiquer, expliquer, preciser, quel |
| 25 | completer_code / code_python / appliquer | 160 | 0.5 | 0.03 | 0.0 | completer, recopier, recopier completer, lignes |
| 13 | modele_donnees / explication / analyser | 129 | 0.27 | 0.21 | 0.01 | cle, cle primaire, primaire, attribut |
| 1 | autre / explication / créer | 118 | 0.51 | 0.14 | 0.01 | ecrire, python, proposer, permettant |
| 22 | trace_execution / valeur / appliquer | 104 | 0.49 | 0.3 | 0.22 | apres, apres execution, execution, renvoie |
| 9 | calcul_numerique / explication / se souvenir | 94 | 0.39 | 0.02 | 0.05 | adresse, donner, binaire, reseau |
| 7 | dessiner_structure / schema / appliquer | 93 | 0.47 | 0.15 | 0.09 | schema, dessiner, schema relationnel, relationnel |
| 23 | calcul_numerique / valeur / appliquer | 91 | 0.5 | 0.23 | 0.0 | binaire, arbre, arbre binaire, calculer |
| 16 | table_routage / explication / appliquer | 88 | 0.51 | 0.03 | 0.08 | routeur, routage, table routage, routeurs |
| 14 | autre / explication / créer | 87 | 0.67 | 0.02 | 1.0 | fonction, deduire, ecrire, precedente |
| 3 | completer_code / code_python / appliquer | 80 | 0.63 | 0.8 | 0.96 | completer, recopier completer, fonction, recopier |
| 2 | corriger_code / explication / analyser | 76 | 0.51 | 0.28 | 0.11 | erreur, corriger, expliquer, pourquoi |
| 0 | ecrire_sql / sql / appliquer | 74 | 0.49 | 0.69 | 0.03 | requete, select, sql, from |
| 15 | justifier_choix / explication / analyser | 65 | 0.56 | 0.14 | 0.06 | expliquer, pourquoi, expliquer pourquoi, quoi |
| 24 | autre / explication / comprendre | 64 | 0.4 | 0.11 | 0.16 | quelle, combien, quelle valeur, quel |
| 10 | justifier_choix / explication / évaluer | 63 | 0.49 | 0.14 | 0.06 | justifier, recursive, citer, fonction |
| 12 | ordonnancement / explication / comprendre | 51 | 0.41 | 0.06 | 0.04 | processus, interblocage, situation, elu |
| 17 | lire_sql / sql / appliquer | 31 | 0.48 | 0.58 | 0.13 | requete, resultat, resultat requete, select |
| 4 | expliquer / explication / évaluer | 26 | 0.54 | 0.19 | 0.08 | justifiant, indiquer justifiant, indiquer, verifier |
| 21 | complexite / explication / évaluer | 21 | 0.6 | 0.14 | 0.33 | cout, nombre comparaisons, comparaisons, tri |
| 20 | definir_notion / explication / se souvenir | 19 | 0.35 | 0.05 | 0.0 | citer, signifie, definir, processus |
| 18 | complexite / complexite / analyser | 15 | 0.7 | 0.2 | 0.0 | complexite, temps, complexite temps, cout temps |

## 2. Enchaînement des questions (chaîne de Markov)

- Ouvertures typiques : autre / explication / appliquer (0.19), modele_donnees / explication / analyser (0.134), dessiner_structure / schema / appliquer (0.064), completer_code / code_python / appliquer (0.057)
- Fermetures typiques : autre / explication / créer (0.273), ecrire_fonction / code_python / créer (0.185), autre / explication / créer (0.172), expliquer / explication / évaluer (0.166)
- Entropie moyenne des transitions : 3.88 bits
- Transitions les plus fortes :
  - lire_sql / sql / appliquer → ecrire_sql / sql / créer (0.55)
  - ecrire_sql / sql / appliquer → ecrire_sql / sql / créer (0.43)
  - ecrire_sql / sql / créer → ecrire_sql / sql / créer (0.43)
  - modele_donnees / explication / analyser → modele_donnees / explication / analyser (0.28)
  - table_routage / explication / appliquer → table_routage / explication / appliquer (0.26)
  - ecrire_fonction / code_python / créer → ecrire_fonction / code_python / créer (0.25)
  - calcul_numerique / explication / se souvenir → calcul_numerique / explication / se souvenir (0.23)
  - autre / explication / appliquer → autre / explication / appliquer (0.22)
  - trace_execution / valeur / appliquer → trace_execution / valeur / appliquer (0.21)
  - ordonnancement / explication / comprendre → ordonnancement / explication / comprendre (0.2)

## 3. Relations entre notions (graphe PMI)

- 3.31 notions par exercice en moyenne
- Notions pivots (PageRank) : modele_relationnel (0.081), sql (0.081), poo (0.067), graphe (0.059), reseau_ip (0.056), arbre_binaire (0.055), routage (0.053), recursivite (0.051)
- Notions ponts (betweenness) : poo (0.18), recursivite (0.168), parcours_graphe (0.101), graphe (0.078), arbre_binaire (0.071), modele_relationnel (0.066)
- Associations fortes (PMI, nb d'exercices) :
  - glouton + recursivite : PMI 1.897, 3 exercices
  - diviser_regner + tri : PMI 1.828, 3 exercices
  - complexite + tri : PMI 1.828, 4 exercices
  - abr + arbre_binaire : PMI 1.716, 14 exercices
  - abr + parcours_arbre : PMI 1.627, 3 exercices
  - processus + soc_architecture : PMI 1.627, 8 exercices
  - prog_dynamique + recursivite : PMI 1.609, 3 exercices
  - arbre_binaire + parcours_arbre : PMI 1.584, 9 exercices
  - reseau_ip + routage : PMI 1.494, 43 exercices
  - file + processus : PMI 1.494, 7 exercices
  - complexite + processus : PMI 1.445, 4 exercices
  - glouton + graphe : PMI 1.372, 3 exercices
- Blocs thématiques cachés (communautés) :
  - complexite, diviser_regner, glouton, graphe, matrice, modularite, pile, poo, prog_dynamique, recursivite, tri
  - dictionnaire, donnees_tables, mise_au_point, modele_relationnel, os_commandes, sgbd, sql, tuple, web_http
  - parcours_graphe, representation_nombres, reseau_ip, routage, securite_crypto
  - abr, arbre_binaire, parcours_arbre
  - file, processus, soc_architecture
  - algo_simples
  - recherche_textuelle
  - paradigmes
  - liste_chainee
  - calculabilite

## 4. Logique de construction d'un sujet

- Recouvrement des domaines entre exercices d'un même sujet : 0.275 (hasard : 0.315) → plus bas que le hasard = les concepteurs répartissent les domaines entre exercices
- Domaines couverts par sujet : 4.36 sur 5
- Barèmes d'exercices : {'4.0': 112, '6.0': 88, '8.0': 42, '3.0': 12, '5.0': 4}
- Courbe à l'intérieur d'un exercice :

| position | Bloom moyen | part code | part dépendante | mots |
|---|---|---|---|---|
| 0-20% | 3.42 | 0.16 | 0.03 | 34.8 |
| 20-40% | 3.77 | 0.25 | 0.1 | 35.8 |
| 40-60% | 3.81 | 0.26 | 0.11 | 39.4 |
| 60-80% | 3.76 | 0.28 | 0.15 | 39.8 |
| 80-100% | 4.13 | 0.34 | 0.17 | 43.4 |

## 5. Difficulté (Gradient Boosting, cible = position relative)

- R² en validation croisée par sujet : 0.121
- Placé en début d'exercice : task=modele_donnees (-0.226), bloom=1 (-0.126), task=ordonnancement (-0.087), concept=sgbd (-0.08), format=schema (-0.072), concept=boucles (-0.069)
- Placé en fin d'exercice : task=complexite (0.149), task=ecrire_fonction (0.106), bloom=6 (0.091), format=code_python (0.088), task=completer_code (0.075), is_sub (0.066)

## 6. Facteurs latents (SVD sur ~90 variables)

- F1 (0.051) : + format=code_python, task=completer_code, code_lines, has_code  /  − concept=sql, format=sql, concept=modele_relationnel, task=ecrire_sql
- F2 (0.043) : + format=sql, concept=sql, task=ecrire_sql, bloom=6  /  − format=explication, concept=reseau_ip, concept=routage, concept=representation_nombres
- F3 (0.033) : + concept=routage, concept=reseau_ip, has_table, format=tableau  /  − concept=recursivite, task=autre, task=ecrire_fonction, format=explication
- F4 (0.029) : + dep_depth, n_deps, bloom=6, explicit_dep  /  − code_lines, has_code, ctx_words, format=explication
- F5 (0.029) : + dep_depth, n_deps, explicit_dep, question_mark  /  − task=ecrire_fonction, bloom=6, format=code_python, concept=poo
- F6 (0.026) : + format=schema, concept=arbre_binaire, task=dessiner_structure, concept=abr  /  − format=complexite, task=complexite, bloom=4, has_table

## 7. Règles d'association (lift)

- task=corriger_code ⇒ concept=mise_au_point : lift 13.26, P(B|A)=0.71
- format=schema ⇒ task=dessiner_structure : lift 11.91, P(B|A)=0.42
- bloom=5 ⇒ task=justifier_choix : lift 7.89, P(B|A)=0.39
- format=sql ⇒ task=ecrire_sql : lift 6.81, P(B|A)=0.61
- task=table_routage ⇒ concept=routage : lift 6.1, P(B|A)=0.98
- has_sql ⇒ format=sql : lift 5.76, P(B|A)=0.85
- has_table ⇒ format=tableau : lift 5.75, P(B|A)=0.42
- task=table_routage ⇒ concept=reseau_ip : lift 5.61, P(B|A)=0.83
- bloom=2 ⇒ task=expliquer : lift 5.6, P(B|A)=0.39
- task=modele_donnees ⇒ concept=modele_relationnel : lift 4.38, P(B|A)=0.91
- question_mark ⇒ bloom=2 : lift 3.93, P(B|A)=0.51
- task=calcul_numerique ⇒ concept=representation_nombres : lift 3.87, P(B|A)=0.44
- format=code_python ⇒ task=ecrire_fonction : lift 3.76, P(B|A)=0.36
- has_figure ⇒ format=schema : lift 3.7, P(B|A)=0.31
- has_sql ⇒ concept=sql : lift 3.57, P(B|A)=1.0

## 8. Tendances et prévision

- En hausse : graphe (0.084), poo (0.053), dictionnaire (0.029), sql (0.028), routage (0.027), recursivite (0.024)
- En baisse : os_commandes (-0.026), parcours_graphe (-0.024), processus (-0.017), parcours_arbre (-0.016), diviser_regner (-0.016), modularite (-0.012)
- Probabilité attendue par exercice (pondérée par récence) : poo (0.454), graphe (0.379), sql (0.326), modele_relationnel (0.233), routage (0.226), reseau_ip (0.203), recursivite (0.182), arbre_binaire (0.163), dictionnaire (0.131), representation_nombres (0.13), securite_crypto (0.088), file (0.083)
- Enseigné mais peu évalué : fonctions (0.0682), tableau_liste (0.0563), booleens (0.0436), boucles (0.0386), chaines (0.0267), interface_tad (0.0258), os_commandes (0.0205), complexite (0.0189)
- Très évalué par rapport au cours : sql (-0.1002), poo (-0.0792), routage (-0.0442), modele_relationnel (-0.0427), reseau_ip (-0.038), arbre_binaire (-0.0351)

## 9. Changement de format 2022 → 2023

- χ² = 343.7 (p = 1.6e-48), Jensen-Shannon = 0.28
- 2021-2022 (5 ex. dont 3 au choix) : {'questions': 840, 'questions_par_exercice': 7.2, 'bloom_moyen': 3.72, 'part_ecrire_code': 0.194, 'part_sql': 0.119, 'part_dependances': 0.113, 'mots_par_question': 44.0}
- 2023+ (3 ex. obligatoires) : {'questions': 1828, 'questions_par_exercice': 11.1, 'bloom_moyen': 3.82, 'part_ecrire_code': 0.284, 'part_sql': 0.172, 'part_dependances': 0.112, 'mots_par_question': 36.4}

## 10. Scénarios d'exercices (NMF)

- extrait, mots, into, set, insert, update → modele_relationnel, sql, web_http
- machine, ip, ipv4, notation, appelee, cidr → reseau_ip, routage, representation_nombres
- jeu, cartes, joueur, couleur, carte, plateau → graphe, poo, recursivite
- exploitation, systemes, lineaires, structures, particulier, environnement → poo, processus, soc_architecture
- parties, independantes, compose, relationnelles, requetes, constitue → poo, sql, graphe
- est_vide, vide, structure, abstraite, ajoute, premier → pile, poo, graphe
- aide, requetes, construire, jour, logiques, affiner → sql, modele_relationnel, poo
- droit, gauche, fils, strictement, superieures, inferieures → arbre_binaire, parcours_arbre, parcours_graphe
- r4, r1, r5, r3, r2, routeurs → routage, reseau_ip, representation_nombres
- points, tri, theme, principalement, traite, algorithmes → poo, tri, graphe
- def, __init__, class, rue, prix, position → poo, graphe, recursivite
- case, cases, bas, droite, jeu, taquin → recursivite, graphe, poo
- cle, indique, reference, att, agit, eleves → sql, modele_relationnel, poo
- mot, palindrome, vers, longueur, len, droite → poo, recursivite, sql
- alice, bob, site, communications, web, securisation → poo, securite_crypto, modele_relationnel
- tab, expression, nombres, indices, operateur, notation → graphe, poo, recursivite
- recursivite, course, vaut, compression, etudier, melange → recursivite, arbre_binaire, poo
- ordinateur, ordinateurs, logiciel, ecran, bit, peripheriques → reseau_ip, routage, representation_nombres

## 11. Épreuve pratique (267 exercices uniques)

- 35 ex. : false, true, ordre, false sinon, renvoie true (ex1/ex2 : {'1': 21, '2': 14})
- 30 ex. : binaire, entier, ecriture, bin_a, positif (ex1/ex2 : {'1': 15, '2': 15})
- 28 ex. : ligne, image, in range, range, for (ex1/ex2 : {'2': 28})
- 27 ex. : tab, element, tri, elements, etape (ex1/ex2 : {'2': 24, '1': 3})
- 26 ex. : caracteres, nom, lettre, chaine, resultat (ex1/ex2 : {'2': 14, '1': 12})
- 21 ex. : recherche, recherche recherche, tab, fonction recherche, python recherche (ex1/ex2 : {'1': 14, '2': 7})
- 20 ex. : liste, tab, indices, liste tab, cles (ex1/ex2 : {'1': 13, '2': 7})
- 16 ex. : arbre, none, none none, arbre binaire, self (ex1/ex2 : {'2': 9, '1': 7})
- 16 ex. : self, pile, sommet pile, sommet, classe (ex1/ex2 : {'2': 16})
- 14 ex. : moyenne, coefficient, fonction moyenne, renvoie moyenne, moyenne moyenne (ex1/ex2 : {'1': 11, '2': 3})
- 13 ex. : chaine, caractere, caracteres, chaine caracteres, occurrences (ex1/ex2 : {'1': 10, '2': 3})
- 10 ex. : tab, parametre tableau, element tableau, tab type, type list (ex1/ex2 : {'1': 10})
- 6 ex. : pieces, rendre, rendu, a_rendre, monnaie (ex1/ex2 : {'2': 5, '1': 1})
- 5 ex. : multiplication, multiplication multiplication, deux nombres, soustraction, produit deux (ex1/ex2 : {'1': 5})

## 12. Classifieur texte → notions (validateur)

- Top-3 correct en validation croisée : 0.893 ; micro-F1 : 0.585

## 13. Questions atypiques (Isolation Forest)

- 2021 Sujet zéro [corriger_code] 3. Lors de l'insertion de l'élèveALTMEYER Yohan (ligne 2 du ﬁchierseconde_lyc.csv), une erreur de
saisie a été commise sur la première langue, qui dev
- 2021 Centres étrangers [ecrire_fonction] 3. On donne, ci-dessous, un extrait de la table ASCII qui permet d'encoder les
caractères de A à Z.
On peut alors considérer l'opération X OR entre de
- 2023 Métropole [lire_sql] 2. En vous basant uniquement sur les données du tableau de la figure 1, donner le
résultat de la requête suivante :

SELECT id, stock, description
FRO
- 2023 Nouvelle-Calédonie [completer_code] d. Compléter, sur le document réponse , la table de routage complète av ec le protocole
OSPF du routeur B.

DOCUMENT RÉPONSE À RENDRE OBLIGATOIREMENT 
- 2026 Antilles-Guyane [table_routage] 9. Écrire la liste des sommets, dans l'ordre de leur visite, lors du parcours en
largeur du graphe du réseau routier de la figure 2 depuis le sommet '
- 2026 Centres étrangers [completer_code] 1. Déchiffrer le message (6,2) (3,6) (3,5) (2,2) en utilisant la grille ci-dessus.
Une façon simple de construire un tableau consiste à choisir un mot
- 2025 Métropole [lire_sql] 2. Donner, sous forme de tableau, le résultat de la requête suivante appliquée à
l'extrait de table précédent.
 SELECT marque, modele
FROM inventaire

- 2024 Sujet zéro [completer_code] 9. Recopier et compléter le schéma ci-dessous avec les processus P1 à P5 en
utilisant les informations présentes dans le tableau ci-dessus et l'algori
