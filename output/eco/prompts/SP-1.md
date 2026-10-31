# Consignes du rédacteur (eco)

Tu écris comme le professeur qui a conçu les anciens sujets. Le PROFIL ci-dessous est ce qu'un modèle
scikit-learn a appris de lui. Pour chaque plan, tu rends un JSON au format donné à la fin.

## Penser comme le professeur
- Étudie `anciens_sujets_proches` : comment il pose une situation, annonce les documents, tourne chaque
  question et ce que son corrigé attend. Ne recopie jamais une situation ancienne.
- Pour chaque `questions[slot]`, reprends la manière de demander de la facette : imite la tournure de
  ses `exemples_reels` (même verbe de consigne, même construction), sans les copier.
- Le contenu vient de `cours` (et `cours_partenaire`) : la question fait travailler les notions de la
  section visée. Si `inedit` est vrai, la section n'est jamais ou presque tombée : écris la question
  qu'il pourrait poser, avec sa façon de faire.
- Si le plan a une `intention_cachee` : la question la plus lourde porte sur `passage_vise` ;
  l'énoncé ne nomme PAS les notions de `evaluer_sans_le_dire`, le corrigé les exige.

## Documents
- Types qu'il fabrique pour le cas (des pib commerciale brut; les des menages investissements; publiques des recettes publique; chomage taux selon diplome; des entreprises pour les; inegalites les revenus sociales; des dans les chaines; emploi politiques des politique; economique des politiques economiques) : invente-les, cohérents avec la situation.
- Indique pour chaque document `source` : `cours`, `documents_reels` ou `invente`.

## Corrigé
- Écris le corrigé comme les siens, longueur `longueur_cible_car` (dans `longueur_reponse_car`).

## Format (JSON valide, rien d'autre)
```json
{
  "id": "<id du plan>",
  "type": "<type du plan>",
  "titre": "titre court",
  "situation": "texte de la situation (cas et sujet complet)",
  "annexes": [{"titre": "Annexe 1 – …", "texte": "…", "source": "cours|documents_reels|invente"}],
  "questions": [
    {"slot": 1, "situation": "(exercices seulement : mini-cas de 3 à 6 lignes)",
     "enonce": "…", "points": 2, "reponse_attendue": "…", "articles_cites": []}
  ]
}
```
Pour le type `exercices`, chaque question a sa courte `situation`. Garde les `slot` et `points` du plan.

PROFIL DU PROFESSEUR (appris par scikit-learn sur 38 anciens sujets et 14 corrigés)

Squelette d'une partie : {4: 23, 5: 19} questions par partie (le plus souvent 4).
Ordre typique des manières de demander : les / les x / presentez / expliquez → les / les x / presentez / expliquez → les / les x / presentez / expliquez → les / les x / presentez / expliquez.
Verdict : rituel (le rang explique la consigne) — la forme de la question dépend surtout de sa place dans le sujet.

Manières de demander découvertes :
  - F0 « une / suivante / suivante colon / une argumentation » (35 questions, place moyenne 1.0) ; ex. : Rédigez une argumentation qui vous permette de répondre à la question suivante :
  - F1 « les / les x / presentez / expliquez » (119 questions, place moyenne 0.45) ; ex. : Repérez les grandes évolutions des prix causées par la politique de concurrence sur le marché des services mobiles en France.
  - F2 « x evolution x / evolution / x evolution / evolution x » (33 questions, place moyenne 0.15) ; ex. : Commentez l’évolution du taux de chômage en France entre 2003 et 2023.

Types de documents en annexe :
  - des pib commerciale brut (65) ; titres réels : Annexe 1 : Croissance du PIB en France. | Annexe 2 : Les obstacles au commerce. | Annexe 1 : La décomposition du revenu disponible brut.
  - les des menages investissements (41) ; titres réels : Annexe 2 : Les investissements directs à l’étranger (IDE) de la France | Annexe 4 : La France continue d’attirer les investisseurs étrangers. | Annexe 2 : Les FMN et les Investissements Directs à l’Étranger.
  - publiques des recettes publique (41) ; titres réels : Annexe 3 : Dépenses et recettes des administrations publiques. | Annexe 6 : Charge d’intérêt de la dette publique depuis 2011. | Annexe 4 : Niveau de vie annuel avant et après redistribution en 2018.
  - chomage taux selon diplome (30) ; titres réels : Annexe 1 : Évolution du taux de chômage en France depuis 2006. | Annexe 2 : Taux de chômage selon le niveau de diplôme. | Annexe 4 : La réforme de l'assurance chômage.
  - des entreprises pour les (59) ; titres réels : Annexe 4 : La prime d’activité. | Annexe 5 : Aménagement numérique du territoire Français. | Annexe 7 : Une potion budgétaire 2021 dédiée à la relance, les déficit
  - inegalites les revenus sociales (22) ; titres réels : Annexe 2 : L’essentiel sur les inégalités de revenus. | Annexe 3 : Les inégalités en France. | Annexe 4 : La Covid-19, un accélérateur des inégalités sociales.
  - des dans les chaines (123) ; titres réels : Annexe 3 : Un retour du protectionnisme ? | Annexe 5 : L’intérêt d’avoir recours au libre-échange. | Annexe 7 : Part de chaque zone géographique dans le commerce mondial.
  - emploi politiques des politique (32) ; titres réels : Annexe 3 : Quel est le champ de la politique de l’emploi ? | Annexe 1 : Les taux d’emploi par âge en France (hors Mayotte). | Annexe 4 : Les effets des politiques de l’emploi.
  - economique des politiques economiques (27) ; titres réels : Annexe 2 : Qu’est-ce que le cycle économique ? | Annexe 4 : La mise en place de l’accord de partenariat économique Unio | Annexe 3 : L’internationalisation de l’économie mondiale.
Annexes par sujet : {5: 1, 6: 1, 8: 3, 9: 3, 10: 10, 11: 6, 12: 11, 13: 2, 14: 4, 15: 1}.

Opérations mentales (ce que la question fait faire) :
  - O0 : fort en appui_sur_le_cours ; faible en largeur_du_cours, rang_dans_le_sujet
  - O1 : fort en largeur_du_cours ; faible en forme_interrogative, appui_sur_le_cours
  - O2 : fort en largeur_du_cours, forme_interrogative, longueur_enonce ; faible en appui_sur_le_cours, appui_sur_les_documents
  - O3 : fort en appui_sur_le_cas ; faible en longueur_enonce, largeur_du_cours
  - O4 : fort en forme_interrogative, longueur_enonce, rang_dans_le_sujet ; faible en appui_sur_les_documents, appui_sur_le_cours

Niveau de détail attendu dans le corrigé : [368, 825, 1186] caractères par point (bas / médian / haut),
0.0 référence(s) citée(s) par réponse en moyenne.
Expressions typiques des corrigés : arguments, nombre, developper, candidat peut, baisse.
Ce que disent les corrigés au correcteur :
  - « Il n’est pas attendu de phrase introductive ou conclusive. »
  - « La position doit être exprimée tout au long de la réponse rédigée. »
  - « Dans le cas où un candidat développerait deux axes, un nombre égal d’arguments n’est pas attendu dans chacun des deux axes. »
  - « Elle doit être comprise à la lecture des arguments. »
  - « Il convient d’accepter tous les autres arguments pertinents qui seraient proposés par le candidat. »
  - « Le syllogisme juridique n’est pas la seule forme attendue. »
  - « Toute réponse argumentée doit être acceptée dès l’instant où elle répond à la question. »
  - « (Connaissances) Il convient d’accepter tous les autres arguments pertinents qui seraient proposés par le candidat. »
  - « Il appartient aux correcteurs de ne pas se laisser « enfermer » par la proposition de corrigé et d’analyser les productions des candidats avec intelligence en n’hésitant pas à valoriser ceux qui font preuve de capacités d’analyse et de réflexion. »
  - « Au moins deux idées sont attendues, dont l’une peut exploiter des transversalités avec d’autres enseignements de spécialité. »


PLAN
```json
{
 "id": "SP-1",
 "type": "sujet_le_plus_probable",
 "section": 20,
 "section_titre": "8.1 Les transformations du commerce mondial",
 "partenaire": 1,
 "partenaire_titre": "1.2 Les décisions du consommateur et du producteur",
 "frequence_passee": 0.28,
 "inedit": false,
 "proba_annee_suivante": 0.167,
 "questions": [
  {
   "slot": 1,
   "facette": 1,
   "nom": "les / les x / presentez / expliquez",
   "exemples_reels": [
    "Appréciez la situation des investissements directs à l’étranger (IDE) de la France.",
    "Repérez les grandes évolutions des prix causées par la politique de concurrence sur le marché des services mobiles en France.",
    "Identifiez à quels types de politiques de l’emploi appartiennent les mesures prises par l’État en matière de lutte contre le chômage."
   ],
   "operation_mentale": {
    "operation": 1,
    "fort": [
     "largeur_du_cours"
    ],
    "faible": [
     "forme_interrogative",
     "appui_sur_le_cours"
    ]
   },
   "points": 2,
   "longueur_reponse_car": [
    736,
    2372
   ],
   "longueur_cible_car": 1650
  },
  {
   "slot": 2,
   "facette": 1,
   "nom": "les / les x / presentez / expliquez",
   "exemples_reels": [
    "Appréciez la situation des investissements directs à l’étranger (IDE) de la France.",
    "Repérez les grandes évolutions des prix causées par la politique de concurrence sur le marché des services mobiles en France.",
    "Identifiez à quels types de politiques de l’emploi appartiennent les mesures prises par l’État en matière de lutte contre le chômage."
   ],
   "operation_mentale": {
    "operation": 1,
    "fort": [
     "largeur_du_cours"
    ],
    "faible": [
     "forme_interrogative",
     "appui_sur_le_cours"
    ]
   },
   "points": 2,
   "longueur_reponse_car": [
    736,
    2372
   ],
   "longueur_cible_car": 1650
  },
  {
   "slot": 3,
   "facette": 1,
   "nom": "les / les x / presentez / expliquez",
   "exemples_reels": [
    "Appréciez la situation des investissements directs à l’étranger (IDE) de la France.",
    "Repérez les grandes évolutions des prix causées par la politique de concurrence sur le marché des services mobiles en France.",
    "Identifiez à quels types de politiques de l’emploi appartiennent les mesures prises par l’État en matière de lutte contre le chômage."
   ],
   "operation_mentale": {
    "operation": 1,
    "fort": [
     "largeur_du_cours"
    ],
    "faible": [
     "forme_interrogative",
     "appui_sur_le_cours"
    ]
   },
   "points": 2,
   "longueur_reponse_car": [
    736,
    2372
   ],
   "longueur_cible_car": 1650
  },
  {
   "slot": 4,
   "facette": 1,
   "nom": "les / les x / presentez / expliquez",
   "exemples_reels": [
    "Appréciez la situation des investissements directs à l’étranger (IDE) de la France.",
    "Repérez les grandes évolutions des prix causées par la politique de concurrence sur le marché des services mobiles en France.",
    "Identifiez à quels types de politiques de l’emploi appartiennent les mesures prises par l’État en matière de lutte contre le chômage."
   ],
   "operation_mentale": {
    "operation": 1,
    "fort": [
     "largeur_du_cours"
    ],
    "faible": [
     "forme_interrogative",
     "appui_sur_le_cours"
    ]
   },
   "points": 3,
   "longueur_reponse_car": [
    1104,
    3558
   ],
   "longueur_cible_car": 2475
  }
 ],
 "nb_annexes": 11,
 "cours": {
  "section": "8.1 Les transformations du commerce mondial",
  "theme": "Thème 8 : Comment organiser le commerce international dans un",
  "texte": "L’ouverture des frontières, la baisse des coûts de transport et de communication, le développement des économies d’échelle ont transformé le commerce mondial. L’internationalisation de la chaîne de valeur des produits se concrétise par une segmentation croissante des processus de production : les entreprises sont aujourd’hui moins spécialisées dans la production d’un bien que dans une étape de sa fabrication.\nIl est important d’estimer la valeur ajoutée dégagée sur chacun des segments. Certains pays n’ont qu’un rôle d’assembleur de ce fait qu’une et ne dégagent d’autres se faible valeur ajoutée du produit final ; positionnent sur des segments à plus forte valeur ajoutée, par exemple dans les secteurs de l’innovation et de la recherche. à l’échelle internationale Cette segmentation se traduit par des importations de biens intermédiaires, qui représentent désormais plus de la moitié des échanges internationaux.\nCes flux au niveau d’un pays sont mesurés par la balance des biens et services. L’un des principaux indicateurs de l’attractivité économique d’un pays est constitué par le niveau des investissements directs à l’étranger (IDE).\nLes IDE sont un élément moteur de la multinationalisation des entreprises. Les principales motivations à l’origine des IDE sont la réduction des coûts et la conquête de nouveaux marchés, difficiles à pénétrer par les seules exportations.\nL’IDE est à l’origine de la création des firmes multinationales (FMN). Si l’effet des IDE est généralement considéré comme positif sur la croissance des pays d’accueil, notamment grâce aux transferts de technologie induits, il est plus discuté sur le commerce international, sur l’emploi dans les pays investisseurs, sur les conditions de travail dans les pays d’accueil et sur l’environnement.\nNotions : Les importations et les exportations de biens et services. La segmentation. Les produits intermédiaires, les produits finis. La balance des biens et des services Les investissements directs à l’étranger (IDE) Les firmes multinationales (FMN)\nCapacité attendue : l'élève est capable d’expliquer.\nCapacité attendue : l'élève est capable de décrire et le développement des échanges de biens et services entre pays.\nCapacité attendue : l'élève est capable l’évolution du solde d’une balance des biens et services.\nCapacité attendue : l'élève est capable d’interpréter.\nCapacité attendue : l'élève est capable de décrire les processus de mondialisation de la chaîne de valeur ajoutée pour un produit, en distinguant les phases d’élaboration des segments de produits et les phases d’assemblage.\nCapacité attendue : l'élève est capable de montrer comment la segmentation des processus de production engendre des flux d’importations et d’exportations des pays participant aux échanges.\nCapacité attendue : l'élève est capable les flux d’investissements directs à l’étranger (IDE).\nCapacité attendue : l'élève est capable la place des firmes multinationales dans les échanges internationaux.\nCapacité attendue : l'élève est capable d’apprécier.\nCapacité attendue : l'élève est capable d’expliquer.",
  "articles": []
 },
 "cours_partenaire": {
  "section": "1.2 Les décisions du consommateur et du producteur",
  "theme": "Thème 1 : Quelles sont les grandes questions économiques et leurs",
  "texte": "La science économique étudie les mécanismes des choix individuels et collectifs, et leurs effets. L’analyse des choix alternatifs des individus se fonde sur l’idée que les agents sont rationnels dans leurs décisions, c’est-à-dire qu’ils s’efforcent d’atteindre les objectifs qu’ils se sont fixés en fonction de leurs préférences individuelles et des contraintes économiques, sociales et environnementales.\nDécider et arbitrer requiert ainsi de comparer les coûts et bénéfices des choix alternatifs. La notion centrale de coût d’opportunité, liée aux utilités que l’on marginales estimées des biens et services consomme ou pas, peut ainsi être expliquée et démontrée.\nConsommer des biens et des services nécessite de les produire. Ces biens (ou services) peuvent être produits par des agents privés ou publics.\nLa valeur de ces biens (ou services) pour les agents économiques est liée à leur rareté et à leur utilité marginale. La question de la production (que produire et en quelle quantité ?) dépend à la fois des quantités et du coût des ressources disponibles (facteurs de production : travail, capital, terre) et de la valeur du bien fabriqué, exprimée par son prix.\nAinsi, un consommateur rationnel cherche à maximiser sa satisfaction (consommation, bien être) en prenant en compte sa contrainte budgétaire et l’utilité marginale estimée pour chacun des biens qu’il souhaite consommer. Le producteur, quant à lui, optimise sa production en comparant le bénéfice récupéré par la vente d’une unité supplémentaire du bien produit et le coût marginal de cette même unité supplémentaire de bien produit (raisonnement marginal).\nIl poursuit sa production jusqu’à ce que la fabrication d’une unité supplémentaire engendre un coût marginal égal à sa recette marginale obtenue par celle-ci.\nNotions : Les préférences et choix économiques. Les coûts d’opportunité. Préférences individuelles. La rationalité et l’utilité individuelles. La maximisation et le raisonnement « à la marge ». La rareté, la valeur, l’utilité marginale. La production, les ressources et les facteurs de production. Égalisation entre coût marginal et recette marginale.\nCapacité attendue : l'élève est capable de décrire concepts et principes fondamentaux du raisonnement économique (coût d’opportunité, utilité, rationalité, préférences, maximisation) pour décrire des choix économiques.\nCapacité attendue : l'élève est capable d’analyser ce que l’on entend par rationalité individuelle.\nCapacité attendue : l'élève est capable d’expliciter d’utilité marginale la notion.",
  "articles": []
 },
 "documents_reels": [
  {
   "source": "stmg-spe-droit-economie-2021-metro-cand-libre",
   "titre": "Annexe 2 : Les investissements directs à l’étranger (IDE) de la France.",
   "texte": "Flux entrants et flux sortants (en millions de $US)\n120000\n100000\n80000\n60000\n40000\n20000\n2012\n2013\n2014\n2015\nFlux entrants\n2016\n2017\n2018\n2019\n2020\nFlux sortants\nSource : OCDE (Organisation de coopération et de développement économiques),\n2020"
  },
  {
   "source": "stmg-spe-droit-economie-2021-metropole",
   "titre": "Annexe 2 : Les FMN et les Investissements Directs à l’Étranger.",
   "texte": "Dans un monde de plus en plus globalisé, où les barrières politiques, économiques et\ntechnologiques disparaissent rapidement, la capacité d’un pays à participer à une\nactivité mondiale constitue un indicateur important de sa performance et de sa\ncompétitivité. […], les relations commerciales vont de nos jours bien au-delà des\néchanges internationaux traditionnels de biens et services, […]. Les Investissements\nDirects à l’Étranger (1) peuvent être considérés comme une stratégie, adoptée par les\nentreprises souhaitant établir une nouvelle usine, de nouveaux bureaux ou acheter les\nactifs existants d’une entreprise étrangère. Ces entreprises cherchent à compléter ou\nà remplacer les échanges extérieurs en produisant (et souvent en vendant) des biens\net services dans des pays autres que celui où elles étaient initialement établies.\n(1) IDE : Investissement d’une entreprise résidente dans un pays étranger afin d’acquérir une\nentreprise existante ou de créer une nouvelle entreprise\nSource : europa.eu/ eurostat – 2017"
  },
  {
   "source": "stmg-spe-droit-economie-2021-metro-cand-libre",
   "titre": "Annexe 6 : Les firmes françaises dans les chaînes de valeurs mondiales.",
   "texte": "La mondialisation a provoqué une fragmentation des chaînes de valeur. Cela signifie\nque les diverses opérations de conception, de logistique, de production et de services\nnécessaires à la fabrication d'un produit final peuvent être réparties à travers un grand\nnombre de pays. Approximativement 70 % des échanges internationaux actuels\nreposent en fait sur les chaînes de valeur mondiales (CVM), et correspondent à des\nflux de services, de matières premières, de pièces détachées et de composants qui\ntraversent les frontières – souvent à de nombreuses reprises. Ils sont intégrés en bout\nde chaîne dans des produits finaux, qui sont ensuite expédiés aux consommateurs du\nmonde entier.\nXerfi canal : Quelles conséquences ont eu pour les entreprises françaises,\nl’allongement et la complexification des chaînes de valeurs mondiales ?\nSylvie Montout : […] Pour la France, la part des biens intermédiaires dans les\nexportations est de l’ordre de 48%. C’est le même taux en Allemagne. […]. Cela s’est\ntraduit par un flux croisé de commerce (importations et exportations) et\nd’investissement. […] On a une augmentation des exportations et aussi des\nimportations dans certains secteurs. Cela peut se refléter également dans les déficits\net les excédents dans certains secteurs. […]\nXerfi Canal : Est-il positif pour les entreprises d’être fortement engagées dans ces\nchaînes de valeur mondiales ?\nSylvie Montout : […] les entreprises des secteurs qui sont les plus engagés dans les\nchaînes de valeurs, sont également celles qui exportent le plus. […] Le secteur le plus\nengagé en France dans la chaîne de valeurs mondiales, dans la division internationale\ndu travail connaît un taux moyen à l’exportation 6 fois supérieur au secteur le moins\nengagé.\nXerfi Canal : L’OCDE* dit que [l’intégration aux chaînes de valeurs mondiales] est\nparticulièrement importante pour les PME.\nSylvie Montout : Oui, l’OCDE insiste beaucoup sur l’opportunité que représente\nl’intégration dans les chaînes de valeur mondiales pour les TPE et les PME. […] La\npremière raison est que l’intégration dans la chaîne de valeurs mondiales permet à\nces entreprises d’accroître ces opportunités, de stabiliser les […]"
  },
  {
   "source": "stmg-spe-droit-economie-2022-mayotte-liban",
   "titre": "Annexe 4 : Les bénéfices pour un pays de participer aux chaînes de valeur.",
   "texte": "Lorsque des pays en développement s'efforcent d'entrer dans les CVM ou d'y\nparticiper, des pressions peuvent s'exercer en faveur d'une progression le long de la\nchaîne de valeur, vers des activités à plus forte valeur ajoutée. Or, les fruits d'une\nparticipation aux CVM peuvent être récoltés à n'importe quel maillon de la chaîne de\nvaleur : ce qui compte pour une économie, c'est de renforcer les activités qui\nconstituent ses points forts. Autrement dit, les pays qui deviennent efficients au stade\nde l'assemblage ou de la production peuvent, en devenant des fournisseurs compétitifs\nau niveau mondial pour ces activités, créer une valeur totale plus importante qu'ils ne\nle pourront en réalisant des activités à plus haute valeur ajoutée pour lesquelles ils\nsont moins compétitifs. En dernière analyse, ce qui importe véritablement, c'est la\nvaleur totale que peuvent créer les activités économiques considérées au sein de la\nchaîne de valeur.\nPar conséquent, les pouvoirs publics devraient se focaliser sur la valeur totale que\ncréent les entreprises, et non sur la part de la valeur ajoutée qui est créée localement.\nAu Viêt Nam, par exemple, la part de la valeur ajoutée locale dans les exportations a\nreculé de 64 % à 53 % entre 2005 et 2016, mais dans le même temps, le total des\nexportations de valeur ajoutée locale a été multiplié par 4. Le pays a donc globalement\naccru ses gains et ses exportations.\nSource : OCDE, Documents de travail de l'OCDE sur la politique commerciale, 2019"
  },
  {
   "source": "stmg-spe-droit-economie-2022-mayotte-liban",
   "titre": "Annexe 5 : L’ouverture commerciale.",
   "texte": "Les échanges permettent aux entreprises de s’approvisionner en biens et services\nauprès des sources les plus compétitives en termes de coût et de qualité – quelle que\nsoit leur localisation géographique – et de vendre leurs biens et leurs services aux\nconsommateurs d’un plus grand nombre de marchés, réduisant de ce fait les coûts et\nprix moyens. Pour les consommateurs, les échanges sont synonymes d’un plus large\nchoix et de prix plus bas, en permettant l’accès à des biens et des services non\ndisponibles sur leurs marchés nationaux, ou à des biens à des prix plus compétitifs.\nUne analyse de l’OCDE sur l’impact des chaînes de valeur mondiales sur l’emploi\nconfirme qu’une fraction importante de l’emploi dans les pays de l’OCDE et dans les\ngrandes économies émergentes dépend des échanges. Dans un pays vaste comme\nles États-Unis, environ 10 % de la main-d’œuvre participe à la production de biens et\nde services qui sont consommés à l’étranger ; ce chiffre grimpe à 20 % en France, à\nprès de 30 % en Allemagne et jusqu’à 47 % pour une petite économie comme l’Irlande.\nDe nombreuses études de l’OCDE montrent également que les échanges ont un rôle\nséparé et positif dans l’augmentation du niveau de revenu moyen. Comparées aux\nentreprises qui ne participent pas au commerce international, les sociétés\nexportatrices ont généralement un meilleur niveau de productivité et versent des\nsalaires plus élevés que la moyenne à leurs salariés.\nSource : OCDE, Mettre en place des politiques publiques, 2019"
  },
  {
   "source": "stmg-spe-droit-economie-2023-la-reunion",
   "titre": "ANNEXE 4 - Le renchérissement des prix de l’énergie entraîne des",
   "texte": "comportements d’ajustement\nLa transmission de la hausse des prix de l’énergie […], se matérialise\nprogressivement, au fur et à mesure que le renchérissement de l’énergie se propage\nau sein du réseau de production. Elle peut être décomposée en plusieurs étapes. Dans\nun premier temps, les entreprises qui utilisent ces produits énergétiques augmentent\nleurs prix de vente aux ménages et aux autres entreprises de façon à compenser la\nhausse des prix de l’énergie […]. Dans un deuxième temps, les entreprises qui utilisent\nces produits dont le prix augmente répercutent elles aussi ces hausses de coûts sur\nleurs prix de vente. […]\nPar ailleurs, les ménages et les entreprises ont pu reporter une partie de leurs achats\nvers des produits dont le prix augmente moins, ou réduire le volume de leurs dépenses\n(en particulier sur les produits énergétiques), ce qui réduirait [la hausse des prix] totale\ninduite par le renchérissement de l’énergie.\nLes salariés notamment, s’efforcent [aussi] de maintenir la valeur réelle de leurs\nrevenus. Ainsi, la rémunération des facteurs de production, travail et capital, devrait\nréagir à terme à la hausse des prix de façon à préserver, pour chaque acteur, la part\nde la valeur ajoutée lui revenant. En particulier, les hausses de prix sont de nature à\nstimuler les revalorisations salariales, […].\nSource : INSEE, 1er septembre 2022"
  }
 ],
 "anciens_sujets_proches": [
  {
   "sujet": "stmg-spe-droit-economie-2022-mayotte-liban",
   "situation": "À partir de vos connaissances et/ou de la documentation fournie en annexes :",
   "annexes": [
    "Annexe 1 : Qu’est-ce qu’une chaîne de valeur mondiale (CVM) ?",
    "Annexe 2 : Les échanges liés aux CVM.",
    "Annexe 3 : La facilitation des échanges au service des consommateurs.",
    "Annexe 4 : Les bénéfices pour un pays de participer aux chaînes de valeur.",
    "Annexe 5 : L’ouverture commerciale.",
    "Annexe 6 : Comprendre les chaînes de valeur mondiales.",
    "Annexe 1 : Qu’est-ce qu’une chaîne de valeur mondiale (CVM) ?",
    "Annexe 2 : Les échanges liés aux CVM. (Chaînes de valeur mondiale)",
    "Annexe 3 : La facilitation des échanges au service des consommateurs.",
    "Annexe 4 : Les bénéfices pour un pays de participer aux chaînes de valeur.",
    "Annexe 5 : L’ouverture commerciale.",
    "Annexe 6 : Comprendre les chaînes de valeur mondiales"
   ],
   "questions": [
    {
     "enonce": "Décrivez le processus de mondialisation de la chaîne de valeur ajoutée d’un produit.",
     "points": null,
     "corrige": null
    },
    {
     "enonce": "Commentez l’évolution des échanges liés aux chaînes de valeur mondiales (CVM).",
     "points": null,
     "corrige": null
    },
    {
     "enonce": "Expliquez pour quelles raisons les firmes multinationales organisent leur production au niveau mondial.",
     "points": null,
     "corrige": null
    },
    {
     "enonce": "Montrez l’effet de la mondialisation des chaînes de valeur pour les consommateurs et pour le marché de l’emploi.",
     "points": null,
     "corrige": null
    }
   ]
  },
  {
   "sujet": "stmg-spe-droit-economie-2021-polynesie",
   "situation": "À partir de vos connaissances et de la documentation fournie en annexe :",
   "annexes": [
    "Annexe 1 : Solde de la balance commerciale française en biens de 1971 à 2018.",
    "Annexe 2 : Le protectionnisme dans le contexte de mondialisation des chaînes de",
    "Annexe 3 : Bilan record des investissements étrangers en France en 2019.",
    "Annexe 4 : Effet d’une hausse généralisée des droits de douane sur le PIB mondial.",
    "Annexe 5 : Qu’est-ce que le protectionnisme ?",
    "Annexe 1 : Solde de la balance commerciale française en biens de 1971 à 2018.",
    "Annexe 2 : Le protectionnisme dans le contexte de mondialisation des chaînes",
    "Annexe 3 : Bilan record des investissements étrangers en France en 2019.",
    "Annexe 4 : Effets d’une hausse généralisée des droits de douane sur le PIB",
    "Annexe 5 : Qu’est-ce que le protectionnisme ?"
   ],
   "questions": [
    {
     "enonce": "Commentez l’évolution du solde de la balance commerciale en biens de 1971 à 2018.",
     "points": null,
     "corrige": "1971 à 2018.\nOn attend du candidat qu’il identifie plusieurs périodes dans l’évolution de la balance\ncommerciale en biens (annexe1) en donnant les valeurs du solde de la balance\ncommerciale, et qu’il interprète ces données économiques. Le verbe directeur\n« commenter » indique que la réponse doit saisir les périodes d’évolution de la\nbalance commerciale en France pour mettre en évidence les changements les plus\nsignificatifs.\nLe solde de la balance commerciale en biens connaît quatre grandes périodes entre\n1971 et 2018 :\n\n\n\nLe solde oscille autour de 0 entre 1971 et 1979.\nLe solde est négatif entre 1979 et 1991, atteignant jusqu’à -14 milliards d’euros\ncourants de déficit, il y a donc un déficit de la balance commerciale en biens,\nles exportations de biens hors de France sont moins élevées que les\nimportations de biens en France sur cette période.\nLe solde est globalement positif de 1992 […]"
    },
    {
     "enonce": "Expliquez le rôle des firmes multinationales dans le processus de mondialisation de la chaîne de valeur.",
     "points": null,
     "corrige": "mondialisation de la chaîne de valeur.\nOn attend du candidat qu’il explique le processus de segmentation de la chaine de\nvaleur au niveau international, puis qu’il précise la place des firmes internationales\ndans ce processus. Le candidat doit exploiter les informations de l’annexe 2 ainsi\nque ses connaissances personnelles.\nLes différentes étapes de production d’un bien sont aujourd’hui segmentées au niveau\ninternational. Chaque pays est spécialisé dans un processus de production : la\nconception, l’assemblage ou la recherche et développement, etc.\nLes firmes multinationales sont des entreprises présentes dans plusieurs pays. Ces\nfirmes décomposent la fabrication du produit final en pratiquant l’externalisation ou à\ntravers des investissements directs à l’étranger (IDE), qui sont des prises de\nparticipation dans des entreprises étrangères. Les différents composants d’un produit\nsont […]"
    },
    {
     "enonce": "Décrivez l’évolution des investissements étrangers en France.",
     "points": null,
     "corrige": "Le candidat doit être capable de relever les données de l’annexe 5 et d’en\norganiser l’exposé.\n\nHausse de 11% des décisions d’investissements étrangers en France en 2019.\nOn dénombre 40 000 emplois créés ou sauvegardés en France grâce à ces\ninvestissements.\nL’ouverture internationale ainsi que les IDE permettent une diversification\nsectorielle."
    },
    {
     "enonce": "Présentez les risques de la mise en place par les États de mesures protectionnistes.",
     "points": null,
     "corrige": "protectionnistes.\n\nOn attend du candidat qu’il repère et expose les informations données dans les\nannexes 2 et 3. L’annexe 4 rappelle au candidat ce que sont les mesures\nprotectionnistes.\nLes mesures protectionnistes peuvent avoir plusieurs effets négatifs :\n\nLes États risquent de mettre en place des mesures de rétorsion (Annexe 2),\nc’est-à-dire qu’ils augmenteront à leur tour les droits de douane. Le commerce\nmondial se contractera. La Banque de France estime qu’une hausse de 10%\ndes droits de douane entraînerait une baisse du PIB mondial comprise entre\n1,5 et 2%. (Annexe 3)\n\n\nL’instauration de droits de douane sur les importations rend les produits\nimportés plus chers. Les producteurs qui utilisent dans leur processus de\nproduction des produits intermédiaires importés (ce qui est le cas des firmes\nmultinationales) subiront donc une augmentation de leurs coûts de production.\nDe plus, […]"
    },
    {
     "enonce": "Rédigez une argumentation qui vous permette de répondre à la question suivante : Le libre-échange est-il favorable à la croissance économique d’un pays ?",
     "points": null,
     "corrige": "suivante :\nLe libre-échange est-il favorable à la croissance économique d’un pays ?\nLa question 5 est le lieu de la réponse argumentée. Les questions préalables (1 à 4)\nont permis de construire des éléments de réponse pour cette question 5. Le corpus\ndocumentaire, apporte également des éléments de réponse au candidat. Ces\néléments ne sont toutefois pas suffisants ; le candidat doit également faire appel à ses\nconnaissances personnelles pour développer son argumentaire.\nPréconisations concernant l’utilisation du corrigé :\nLe nombre d’arguments est indicatif. Certains candidats ont pu retenir un nombre\nd’arguments moins important, mais les développer de façon plus approfondie\nGrille d’évaluation :\nConstruction de l’argumentation\n- Cohérence des arguments avec la question posée\n\nLogique globale de l’argumentation\n\n\nPrésentation d’un point de vue argumenté\n\nArguments et concepts\n- […]"
    }
   ]
  }
 ],
 "passage_vise": "Capacité attendue : l'élève est capable de décrire et le développement des échanges de biens et services entre pays.",
 "probabilite_de_tomber": 0.845,
 "deja_tombe": 3,
 "intention_cachee": {
  "evaluer_sans_le_dire": [],
  "deja_nomme_d_habitude": [],
  "type": null
 },
 "manieres_probables": [
  {
   "facette": 1,
   "nom": "les / les x / presentez / expliquez",
   "part": 0.59
  },
  {
   "facette": 2,
   "nom": "x evolution x / evolution / x evolution / evolution x",
   "part": 0.24
  },
  {
   "facette": 0,
   "nom": "une / suivante / suivante colon / une argumentation",
   "part": 0.17
  }
 ],
 "questions_passees_proches": [
  {
   "sujet": "stmg-spe-droit-economie-2022-mayotte-liban",
   "enonce": "Commentez l’évolution des échanges liés aux chaînes de valeur mondiales (CVM)."
  },
  {
   "sujet": "stmg-spe-droit-economie-2023-metropole",
   "enonce": "Décrivez l’évolution des échanges de biens de la France avec l’extérieur."
  }
 ],
 "regle": "La question la plus lourde porte sur le passage visé. L'énoncé ne nomme pas les notions de « evaluer_sans_le_dire » ; le corrigé les exige."
}
```

Écris le résultat dans `/home/user/Projet-de-test/output/eco/generated_probables/SP-1.json`.
