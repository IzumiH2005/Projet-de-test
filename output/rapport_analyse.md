# Analyse des annales NSI (Terminale)

Corpus : 96 sujets écrits uniques (341 exercices, 3052 questions), 181 sujets pratiques (362 exercices), 281 sections de cours.
Années : {'2021': 12, '2022': 17, '2023': 17, '2024': 17, '2025': 20, '2026': 13}

## 1. Archétypes de questions (26 formes, KMeans + silhouette)

| # | archétype (tâche / format / Bloom) | n | position moy. | code | dépend d'avant | formulations |
|---|---|---|---|---|---|---|
| 6 | completer_code / code_python / appliquer | 325 | 0.56 | 0.68 | 0.12 | completer, recopier, recopier completer, lignes |
| 2 | autre / explication / appliquer | 282 | 0.46 | 0.09 | 0.05 | determiner, donner, arbre, return |
| 10 | ecrire_fonction / code_python / créer | 235 | 0.59 | 0.06 | 0.05 | ecrire, ecrire fonction, fonction, prend |
| 8 | ecrire_sql / sql / créer | 231 | 0.55 | 0.04 | 0.02 | ecrire requete, requete, ecrire, requete sql |
| 1 | expliquer / explication / comprendre | 193 | 0.47 | 0.15 | 0.05 | indiquer, expliquer, preciser, quel |
| 19 | calcul_numerique / explication / appliquer | 168 | 0.44 | 0.12 | 0.03 | binaire, arbre, arbre binaire, adresse |
| 17 | modele_donnees / explication / analyser | 141 | 0.29 | 0.2 | 0.02 | cle, cle primaire, primaire, attribut |
| 0 | autre / explication / appliquer | 136 | 0.68 | 0.27 | 0.99 | fonction, deduire, completer, precedent |
| 23 | autre / explication / se souvenir | 129 | 0.37 | 0.09 | 0.04 | donner, adresse, donner adresse, reseau |
| 3 | completer_code / tableau / appliquer | 127 | 0.5 | 0.31 | 0.07 | completer, recopier, recopier completer, tableau |
| 20 | autre / explication / créer | 125 | 0.51 | 0.11 | 0.01 | ecrire, proposer, python, permettant |
| 9 | trace_execution / valeur / appliquer | 112 | 0.48 | 0.31 | 0.25 | apres, apres execution, execution, renvoie |
| 12 | dessiner_structure / schema / appliquer | 108 | 0.47 | 0.16 | 0.11 | schema, dessiner, schema relationnel, relationnel |
| 22 | table_routage / explication / appliquer | 103 | 0.52 | 0.03 | 0.1 | routeur, routage, table routage, routeurs |
| 11 | corriger_code / explication / analyser | 84 | 0.52 | 0.32 | 0.11 | erreur, corriger, expliquer, pourquoi |
| 4 | ecrire_sql / sql / appliquer | 79 | 0.49 | 0.7 | 0.03 | requete, select, sql, from |
| 15 | justifier_choix / explication / évaluer | 75 | 0.48 | 0.13 | 0.07 | justifier, recursive, fonction, citer |
| 25 | justifier_choix / explication / analyser | 70 | 0.55 | 0.16 | 0.07 | expliquer, pourquoi, expliquer pourquoi, quoi |
| 24 | autre / explication / comprendre | 69 | 0.4 | 0.12 | 0.14 | quelle, combien, quel, arbre |
| 5 | ecrire_fonction / code_python / créer | 68 | 0.59 | 0.91 | 0.22 | ecrire, fonction, ecrire fonction, ecrire code |
| 7 | ordonnancement / explication / appliquer | 63 | 0.43 | 0.05 | 0.05 | processus, processeur, interblocage, elu |
| 16 | autre / valeur / se souvenir | 36 | 0.39 | 0.08 | 0.0 | donner, valeur, obtenir, valeurs |
| 18 | lire_sql / sql / appliquer | 36 | 0.46 | 0.53 | 0.14 | resultat, resultat requete, requete, select |
| 21 | complexite / explication / évaluer | 22 | 0.62 | 0.14 | 0.32 | cout, nombre comparaisons, tri, comparaisons |
| 13 | definir_notion / explication / se souvenir | 20 | 0.39 | 0.05 | 0.0 | citer, signifie, definir, processus |
| 14 | complexite / complexite / analyser | 15 | 0.7 | 0.2 | 0.0 | complexite, temps, complexite temps, cout temps |

## 2. Enchaînement des questions (chaîne de Markov)

- Ouvertures typiques : autre / explication / appliquer (0.13), modele_donnees / explication / analyser (0.121), calcul_numerique / explication / appliquer (0.09), completer_code / code_python / appliquer (0.066)
- Fermetures typiques : autre / explication / appliquer (0.249), autre / explication / créer (0.186), ecrire_fonction / code_python / créer (0.184), complexite / complexite / analyser (0.157)
- Entropie moyenne des transitions : 3.87 bits
- Transitions les plus fortes :
  - lire_sql / sql / appliquer → ecrire_sql / sql / créer (0.56)
  - ecrire_sql / sql / appliquer → ecrire_sql / sql / créer (0.45)
  - ecrire_sql / sql / créer → ecrire_sql / sql / créer (0.43)
  - table_routage / explication / appliquer → table_routage / explication / appliquer (0.3)
  - modele_donnees / explication / analyser → modele_donnees / explication / analyser (0.27)
  - ordonnancement / explication / appliquer → ordonnancement / explication / appliquer (0.25)
  - autre / explication / appliquer → autre / explication / appliquer (0.24)
  - trace_execution / valeur / appliquer → trace_execution / valeur / appliquer (0.21)
  - ecrire_fonction / code_python / créer → ecrire_fonction / code_python / créer (0.21)
  - complexite / complexite / analyser → completer_code / code_python / appliquer (0.21)

## 3. Relations entre notions (graphe PMI)

- 3.29 notions par exercice en moyenne
- Notions pivots (PageRank) : sql (0.088), modele_relationnel (0.083), poo (0.064), arbre_binaire (0.063), graphe (0.056), reseau_ip (0.054), routage (0.052), recursivite (0.046)
- Notions ponts (betweenness) : poo (0.177), recursivite (0.173), arbre_binaire (0.128), parcours_graphe (0.093), modele_relationnel (0.076), sql (0.075)
- Associations fortes (PMI, nb d'exercices) :
  - abr + parcours_arbre : PMI 1.916, 5 exercices
  - glouton + recursivite : PMI 1.912, 3 exercices
  - diviser_regner + tri : PMI 1.83, 3 exercices
  - complexite + tri : PMI 1.83, 4 exercices
  - abr + arbre_binaire : PMI 1.716, 17 exercices
  - processus + soc_architecture : PMI 1.627, 8 exercices
  - arbre_binaire + parcours_arbre : PMI 1.606, 11 exercices
  - reseau_ip + routage : PMI 1.519, 50 exercices
  - complexite + processus : PMI 1.445, 4 exercices
  - file + processus : PMI 1.398, 7 exercices
  - glouton + graphe : PMI 1.355, 3 exercices
  - parcours_arbre + parcours_graphe : PMI 1.341, 5 exercices
- Blocs thématiques cachés (communautés) :
  - complexite, diviser_regner, glouton, graphe, matrice, modularite, pile, poo, prog_dynamique, recursivite, tri
  - algo_simples, dictionnaire, donnees_tables, mise_au_point, modele_relationnel, os_commandes, sgbd, sql, tuple, web_http
  - parcours_graphe, representation_nombres, reseau_ip, routage, securite_crypto
  - abr, arbre_binaire, parcours_arbre, recherche_textuelle
  - file, processus, soc_architecture
  - paradigmes
  - liste_chainee
  - calculabilite

## 4. Logique de construction d'un sujet

- Recouvrement des domaines entre exercices d'un même sujet : 0.269 (hasard : 0.363) → plus bas que le hasard = les concepteurs répartissent les domaines entre exercices
- Domaines couverts par sujet : 4.36 sur 5
- Barèmes d'exercices : {'4.0': 124, '6.0': 101, '8.0': 48, '3.0': 13, '5.0': 6, '9.0': 1}
- Courbe à l'intérieur d'un exercice :

| position | Bloom moyen | part code | part dépendante | mots |
|---|---|---|---|---|
| 0-20% | 3.38 | 0.16 | 0.03 | 34.5 |
| 20-40% | 3.73 | 0.24 | 0.09 | 35.4 |
| 40-60% | 3.78 | 0.27 | 0.11 | 39.6 |
| 60-80% | 3.81 | 0.28 | 0.16 | 40.4 |
| 80-100% | 4.1 | 0.32 | 0.17 | 42.7 |

## 5. Difficulté (Gradient Boosting, cible = position relative)

- R² en validation croisée par sujet : 0.144
- Placé en début d'exercice : task=modele_donnees (-0.212), bloom=1 (-0.131), concept=boucles (-0.089), concept=sgbd (-0.08), concept=recherche_textuelle (-0.072), format=schema (-0.069)
- Placé en fin d'exercice : task=complexite (0.159), task=ecrire_fonction (0.109), bloom=6 (0.092), format=code_python (0.085), task=completer_code (0.069), concept=fonctions (0.065)

## 6. Facteurs latents (SVD sur ~90 variables)

- F1 (0.051) : + format=code_python, code_lines, task=completer_code, has_code  /  − concept=sql, format=sql, concept=modele_relationnel, task=ecrire_sql
- F2 (0.044) : + format=sql, concept=sql, task=ecrire_sql, concept=modele_relationnel  /  − concept=reseau_ip, concept=routage, format=explication, concept=representation_nombres
- F3 (0.033) : + concept=routage, concept=reseau_ip, has_table, format=tableau  /  − concept=recursivite, concept=poo, task=autre, format=explication
- F4 (0.029) : + bloom=6, task=ecrire_fonction, format=code_python, task=ecrire_sql  /  − code_lines, has_code, format=explication, has_sql
- F5 (0.029) : + dep_depth, n_deps, explicit_dep, is_sub  /  − ctx_words, format=code_python, concept=poo, code_lines
- F6 (0.026) : + format=schema, concept=arbre_binaire, task=dessiner_structure, concept=abr  /  − format=complexite, task=complexite, bloom=4, concept=complexite

## 7. Règles d'association (lift)

- format=schema ⇒ task=dessiner_structure : lift 11.83, P(B|A)=0.43
- bloom=5 ⇒ task=justifier_choix : lift 8.06, P(B|A)=0.39
- format=sql ⇒ task=ecrire_sql : lift 6.84, P(B|A)=0.62
- task=table_routage ⇒ concept=routage : lift 5.99, P(B|A)=0.97
- has_table ⇒ format=tableau : lift 5.77, P(B|A)=0.44
- has_sql ⇒ format=sql : lift 5.74, P(B|A)=0.84
- bloom=2 ⇒ task=expliquer : lift 5.74, P(B|A)=0.39
- task=table_routage ⇒ concept=reseau_ip : lift 5.55, P(B|A)=0.85
- task=modele_donnees ⇒ concept=modele_relationnel : lift 4.52, P(B|A)=0.91
- question_mark ⇒ bloom=2 : lift 4.09, P(B|A)=0.52
- format=code_python ⇒ task=ecrire_fonction : lift 3.81, P(B|A)=0.36
- task=calcul_numerique ⇒ concept=representation_nombres : lift 3.76, P(B|A)=0.42
- has_figure ⇒ format=schema : lift 3.65, P(B|A)=0.31
- has_sql ⇒ concept=sql : lift 3.62, P(B|A)=1.0
- task=ecrire_sql ⇒ concept=sql : lift 3.61, P(B|A)=1.0

## 8. Tendances et prévision

- En hausse : graphe (0.084), poo (0.054), sql (0.028), dictionnaire (0.027), routage (0.026), recursivite (0.021)
- En baisse : os_commandes (-0.024), parcours_graphe (-0.023), processus (-0.019), parcours_arbre (-0.016), diviser_regner (-0.016), modularite (-0.011)
- Probabilité attendue par exercice (pondérée par récence) : poo (0.452), graphe (0.378), sql (0.323), routage (0.227), modele_relationnel (0.219), reseau_ip (0.198), recursivite (0.175), arbre_binaire (0.168), representation_nombres (0.136), dictionnaire (0.13), securite_crypto (0.09), file (0.08)
- Enseigné mais peu évalué : fonctions (0.0677), tableau_liste (0.0558), booleens (0.0434), boucles (0.0388), interface_tad (0.0259), chaines (0.0254), os_commandes (0.0209), complexite (0.0197)
- Très évalué par rapport au cours : sql (-0.0982), poo (-0.0777), routage (-0.0457), modele_relationnel (-0.0414), reseau_ip (-0.0412), arbre_binaire (-0.0393)

## 9. Changement de format 2022 → 2023

- χ² = 352.4 (p = 3.4e-50), Jensen-Shannon = 0.273
- 2021-2022 (5 ex. dont 3 au choix) : {'questions': 866, 'questions_par_exercice': 7.2, 'bloom_moyen': 3.7, 'part_ecrire_code': 0.193, 'part_sql': 0.121, 'part_dependances': 0.112, 'mots_par_question': 44.1}
- 2023+ (3 ex. obligatoires) : {'questions': 2186, 'questions_par_exercice': 11.1, 'bloom_moyen': 3.79, 'part_ecrire_code': 0.277, 'part_sql': 0.168, 'part_dependances': 0.114, 'mots_par_question': 36.4}

## 10. Scénarios d'exercices (NMF)

- cle, reference, indique, agit, att, eleves → sql, modele_relationnel, poo
- machine, ipv4, notation, ip, appelee, representent → reseau_ip, routage, representation_nombres
- case, cases, jeu, bas, taquin, droite → recursivite, graphe, poo
- parties, independantes, relationnelles, compose, requetes, recursivite → sql, poo, modele_relationnel
- exploitation, systemes, lineaires, structures, particulier, environnement → poo, processus, os_commandes
- structure, est_vide, abstraite, premier, vide, ajoute → pile, file, poo
- requetes, aide, construire, jour, recherches, affiner → sql, modele_relationnel, poo
- def, __init__, class, caracteristiques, rue, prix → poo, graphe, recursivite
- r4, routeurs, reseaux, r1, r5, r3 → reseau_ip, routage, representation_nombres
- droit, strictement, superieures, egales, inferieures, fils → arbre_binaire, parcours_arbre, abr
- points, tri, theme, principalement, traite, algorithmique → poo, graphe, arbre_binaire
- tab, indices, len, regions, expression, bien → poo, graphe, pile
- extrait, mots, into, set, insert, update → modele_relationnel, sql, web_http
- jeu, cartes, joueur, carte, couleur, plateau → poo, graphe, recursivite
- mot, palindrome, droite, vers, longueur, instruction → poo, recursivite, sql
- compression, mis, texte, information, recursivite, transmettre → arbre_binaire, representation_nombres, recursivite
- vide, non, mere, droit, chien, vaut → arbre_binaire, poo, graphe
- alice, chiffrement, bob, communications, message, securisation → securite_crypto, poo, reseau_ip

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

- Top-3 correct en validation croisée : 0.956 ; micro-F1 : 0.726

## 13. Questions atypiques (Isolation Forest)

- 2021 Centres étrangers [ecrire_fonction] 3. On donne, ci-dessous, un extrait de la table ASCII qui permet d'encoder les
caractères de A à Z.
On peut alors considérer l'opération X OR entre de
- 2023 Nouvelle-Calédonie [completer_code] d. Compléter, sur le document réponse , la table de routage complète av ec le protocole
OSPF du routeur B.

DOCUMENT RÉPONSE À RENDRE OBLIGATOIREMENT 
- 2022 Amérique du Nord [ecrire_fonction] 4. Écrire une fonction nombre_baisses qui prend en paramètre un tableautab, non vide, des
variations des températures et qui renvoie un p-uplet conten
- 2021 Sujet zéro [corriger_code] 3. Lors de l'insertion de l'élèveALTMEYER Yohan (ligne 2 du ﬁchierseconde_lyc.csv), une erreur de
saisie a été commise sur la première langue, qui dev
- 2022 Nouvelle-Calédonie [ecrire_fonction] c) Écrire la fonction profil prenant en argument un arbre binaire non vide A et qui
renvoie le profil du membre dont le pseudo nyme est l'étiquette de
- 2022 Nouvelle-Calédonie [dessiner_structure] a) Pour chaque écriture de masque de réseau, ci -dessous, indiquer et justifier si
elle correspond à un masque de réseau valide :

• 255.255.225.0
• 2
- 2026 Antilles-Guyane [table_routage] 9. Écrire la liste des sommets, dans l'ordre de leur visite, lors du parcours en
largeur du graphe du réseau routier de la figure 2 depuis le sommet '
- 2025 Métropole [ecrire_fonction] 9. Écrire une fonction somme_occ qui prend en paramètres un tableau tab de
tuples (symbole, nb_occ) et qui renvoie la somme des nombres
d'occurrences 
