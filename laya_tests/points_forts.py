import sys; sys.path.insert(0, "/home/user/laya/int8"); import laya_int8
a = laya_int8.charger("/home/user/laya/int8/laya_fr_en_int8", cache=sys.argv[1] + "/i8cache")
def ch(i, *c): return {"type": "choice", "instructions": i, "criteria": {k: k for k in c}}
def nl(i): return {"type": "noul", "instructions": i}
AB = {"type": "choice", "instructions": "Quel avis est le plus satisfait ?", "criteria": {"A": "l'avis A", "B": "l'avis B"}}
QAB = {"type": "choice", "instructions": "Quel passage répond le mieux à la question ?", "criteria": {"A": "le passage A", "B": "le passage B"}}
SUJ = ch("De quel sujet parle ce texte ?", "sport", "économie", "culture", "sciences", "faits divers")
SAV = ch("À quel service faut-il transmettre ce message ?", "livraison", "remboursement", "problème technique", "facturation", "compte client")
INT = ch("Que veut faire l'utilisateur ?", "créer un rappel", "écouter de la musique", "connaître la météo", "appeler quelqu'un", "trouver un itinéraire")
REP = nl("Le passage répond-il à la question ?")
E = [
 ("1. Ranger par sujet", "Le CAC 40 a clôturé en hausse de 1,2 % après l'annonce d'une baisse des taux par la BCE.", SUJ, "économie"),
 ("1. Ranger par sujet", "Le dernier film de Jacques Audiard a reçu une ovation de dix minutes au Festival de Cannes.", SUJ, "culture"),
 ("1. Ranger par sujet", "Des astronomes ont détecté de la vapeur d'eau dans l'atmosphère d'une exoplanète.", SUJ, "sciences"),
 ("1. Ranger par sujet", "Un camion s'est renversé sur l'A7 cette nuit, aucun blessé n'est à déplorer.", SUJ, "faits divers"),
 ("1. Ranger par sujet", "Le Stade Toulousain remporte son 23e titre de champion de France de rugby.", SUJ, "sport"),
 ("2. Support client", "Je n'arrive plus à me connecter, on me dit que mon mot de passe est incorrect alors que je ne l'ai pas changé.", SAV, "compte client"),
 ("2. Support client", "Ma commande devait arriver mardi, on est vendredi et le suivi n'a pas bougé.", SAV, "livraison"),
 ("2. Support client", "J'ai retourné l'article il y a 15 jours et je n'ai toujours pas été remboursé.", SAV, "remboursement"),
 ("2. Support client", "Votre facture indique une TVA à 20 % alors que je suis une association exonérée.", SAV, "facturation"),
 ("2. Support client", "Depuis la mise à jour, l'écran reste noir au démarrage.", SAV, "problème technique"),
 ("3. Assistant vocal", "Réveille-moi à 7h demain et préviens-moi de prendre mes médicaments.", INT, "créer un rappel"),
 ("3. Assistant vocal", "Lance ma playlist de rock des années 80.", INT, "écouter de la musique"),
 ("3. Assistant vocal", "Est-ce que je dois prendre un parapluie cet après-midi ?", INT, "connaître la météo"),
 ("3. Assistant vocal", "Passe un coup de fil à Julien.", INT, "appeler quelqu'un"),
 ("3. Assistant vocal", "Comment je vais à la tour Eiffel à pied depuis ici ?", INT, "trouver un itinéraire"),
 ("4. Avis clients", "Hôtel impeccable, personnel aux petits soins, petit-déjeuner copieux. On reviendra !", ch("Le client est-il satisfait ?", "positif", "négatif"), "positif"),
 ("4. Avis clients", "Chambre sale, bruit toute la nuit, et on nous a facturé un parking qui devait être gratuit.", ch("Le client est-il satisfait ?", "positif", "négatif"), "négatif"),
 ("4. Avis clients", "Battery life is great and the screen is gorgeous. Best purchase this year.", ch("Le client est-il satisfait ?", "positif", "négatif"), "positif"),
 ("5. Modération", "Espèce de sale con, t'as rien dans le crâne.", nl("Ce message est-il toxique ou insultant ?"), True),
 ("5. Modération", "Merci pour cette vidéo très claire, ça m'a beaucoup aidé pour mon examen.", nl("Ce message est-il toxique ou insultant ?"), False),
 ("5. Anti-arnaque", "Colissimo : votre colis est en attente, payez 1,99 € de frais de douane ici : colis-suivi-fr.info", nl("Ce message est-il une tentative d'arnaque ?"), True),
 ("5. Anti-arnaque", "Votre commande n°48213 a été expédiée. Elle arrivera entre le 12 et le 14 novembre.", nl("Ce message est-il une tentative d'arnaque ?"), False),
 ("6. FAQ / recherche", "Question : Peut-on payer en plusieurs fois ?\nPassage : Le paiement en 3 ou 4 fois sans frais est disponible dès 100 € d'achat.", REP, True),
 ("6. FAQ / recherche", "Question : Peut-on payer en plusieurs fois ?\nPassage : Nous acceptons les cartes Visa, Mastercard et PayPal.", REP, False),
 ("6. FAQ / recherche", "Question : Quel est l'âge minimum pour s'inscrire ?\nPassage : L'inscription est ouverte à toute personne âgée d'au moins 16 ans, avec accord parental jusqu'à 18 ans.", REP, True),
 ("7. Comparer", "Avis A : Produit correct, sans plus, la livraison était un peu lente.\nAvis B : Absolument parfait, je le recommande à tout le monde !", AB, "B"),
 ("7. Comparer", "Avis A : Très bon restaurant, accueil chaleureux et plats savoureux.\nAvis B : Service lent et plats tièdes, décevant.", AB, "A"),
 ("7. Comparer", "Question : Quand a eu lieu la prise de la Bastille ?\nPassage A : La Bastille était une forteresse servant de prison à Paris.\nPassage B : Le 14 juillet 1789, les Parisiens prennent d'assaut la Bastille.", QAB, "B"),
]
ok = 0; cur = None
for cat, s, q, exp in E:
    x = a.predict(s, {"q": q})["answers"]["q"]
    if x["type"] == "noul": g, c = x["noul"] >= .5, max(x["noul"], 1 - x["noul"]); g2 = "oui" if g else "non"; e2 = "oui" if exp else "non"
    else: g, c = x["choice"], x["probabilities"][x["choice"]]; g2, e2 = g, exp
    ok += g == exp
    if cat != cur: print(f"\n## {cat} — « {q['instructions']} »"); cur = cat
    print(f"{'✅' if g == exp else '❌'} {s}\n   → {g2} ({round(100*c)} %)" + ("" if g == exp else f"  [attendu : {e2}]"))
print("\nSCORE", ok, "/", len(E))
