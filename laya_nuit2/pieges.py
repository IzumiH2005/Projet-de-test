import sys, json, laya

V = "L'affirmation est-elle appuyée, contredite, ou le texte ne permet-il pas de trancher ?"
VC = {"appuyée": "le texte confirme l'affirmation", "indéterminée": "le texte ne permet pas de savoir",
      "contredite": "le texte dit le contraire"}
NOTE = ["très négatif (1 étoile)", "négatif (2 étoiles)", "mitigé (3 étoiles)", "positif (4 étoiles)", "très positif (5 étoiles)"]
SENT = {"positif": "avis positif", "négatif": "avis négatif"}

def ch(instr, crit): return {"type": "choice", "instructions": instr, "criteria": crit}
def nl(instr): return {"type": "noul", "instructions": instr}
def sc(instr, crit): return {"type": "score", "instructions": instr, "criteria": crit}

T = [
 # catégorie, piège, texte, question, attendu
 ("Sarcasme", "ironie : mots positifs, sens négatif",
  "Génial, encore un colis livré avec trois semaines de retard et la boîte écrasée. Vraiment, bravo.",
  ch("Le client est-il satisfait ?", SENT), "négatif"),
 ("Sarcasme", "ironie subtile",
  "Merveilleux ce téléphone, la batterie tient presque jusqu'au petit-déjeuner.",
  ch("Le client est-il satisfait ?", SENT), "négatif"),
 ("Négation", "double négation",
  "Je ne peux pas dire que je n'ai pas aimé ce film, bien au contraire.",
  ch("Le client est-il satisfait ?", SENT), "positif"),
 ("Négation", "mots négatifs, avis positif",
  "Aucun défaut, rien à redire, pas une seule déception.",
  ch("Le client est-il satisfait ?", SENT), "positif"),
 ("Note", "mitigé : un plus, un moins",
  "La qualité est correcte mais le prix est vraiment excessif pour ce que c'est. Bof.",
  sc("Quelle note le client donne-t-il ?", NOTE), 2),
 ("Note", "enthousiasme total",
  "Un chef-d'œuvre absolu, je l'ai déjà offert à toute ma famille !",
  sc("Quelle note le client donne-t-il ?", NOTE), 4),
 ("Logique", "chiffre modifié",
  "Texte : Marie est arrivée à Lyon en 2015 après dix ans passés à Marseille.\nAffirmation : Marie a vécu cinq ans à Marseille.",
  ch(V, VC), "contredite"),
 ("Logique", "déduction temporelle",
  "Texte : Marie est arrivée à Lyon en 2015 après dix ans passés à Marseille.\nAffirmation : En 2010, Marie vivait à Marseille.",
  ch(V, VC), "appuyée"),
 ("Logique", "info absente (ne pas inventer)",
  "Texte : Marie est arrivée à Lyon en 2015 après dix ans passés à Marseille.\nAffirmation : Marie travaille dans un hôpital.",
  ch(V, VC), "indéterminée"),
 ("Logique", "quantificateur « tous / certains »",
  "Texte : Certains élèves de la classe ont réussi l'examen.\nAffirmation : Tous les élèves ont réussi l'examen.",
  ch(V, VC), "indéterminée"),
 ("Logique", "inversion des rôles",
  "Texte : Le chat a été poursuivi par le chien dans le jardin.\nAffirmation : Le chat poursuivait le chien.",
  ch(V, VC), "contredite"),
 ("Logique", "négation cachée",
  "Texte : Le ministre a refusé de confirmer sa démission.\nAffirmation : Le ministre a confirmé sa démission.",
  ch(V, VC), "contredite"),
 ("Paraphrase", "mêmes mots, sens inversé",
  "Phrase 1 : Paul a prêté de l'argent à Julie.\nPhrase 2 : Julie a prêté de l'argent à Paul.",
  nl("Les deux phrases ont-elles exactement le même sens ?"), False),
 ("Paraphrase", "mots différents, même sens",
  "Phrase 1 : Le magasin ouvre à neuf heures.\nPhrase 2 : L'ouverture de la boutique a lieu à 9h.",
  nl("Les deux phrases ont-elles exactement le même sens ?"), True),
 ("Toxicité", "insulte polie / déguisée",
  "Avec tout le respect que je vous dois, vous êtes d'une stupidité rare.",
  nl("Ce message est-il toxique ou insultant ?"), True),
 ("Toxicité", "gros mot mais bienveillant",
  "Putain, t'es trop fort, bravo pour ton concours !",
  nl("Ce message est-il toxique ou insultant ?"), False),
 ("Toxicité", "critique ferme mais respectueuse",
  "Je ne suis pas du tout d'accord avec votre analyse, les chiffres disent l'inverse.",
  nl("Ce message est-il toxique ou insultant ?"), False),
 ("Intention", "demande indirecte",
  "Je vais finir par être en retard demain si personne ne me réveille à 6h30...",
  ch("Que demande l'utilisateur ?", {"régler une alarme": "alarm set", "météo": "weather query",
     "jouer de la musique": "play music", "envoyer un message": "email send"}), "régler une alarme"),
 ("Intention", "mot-piège « musique »",
  "Est-ce qu'il va pleuvoir pendant le festival de musique samedi ?",
  ch("Que demande l'utilisateur ?", {"régler une alarme": "alarm set", "météo": "weather query",
     "jouer de la musique": "play music", "envoyer un message": "email send"}), "météo"),
 ("Question", "bon thème mais pas de réponse",
  "Question : En quelle année la tour Eiffel a-t-elle été construite ?\nPassage : La tour Eiffel est le monument le plus visité de Paris, avec ses 330 mètres de hauteur.",
  nl("Le passage répond-il à la question ?"), False),
 ("Question", "réponse formulée autrement",
  "Question : Qui a écrit Les Misérables ?\nPassage : Publié en 1862, ce roman fleuve est l'œuvre de Victor Hugo, alors en exil à Guernesey.",
  nl("Le passage répond-il à la question ?"), True),
 ("Matière", "sujet scolaire",
  "On calcule la dérivée de f(x)=x² pour trouver la pente de la tangente en x=3.",
  ch("De quelle matière scolaire parle ce texte ?", {"mathématiques": "maths", "histoire": "histoire",
     "français": "français", "physique": "physique", "biologie": "SVT"}), "mathématiques"),
 ("Matière", "piège : vocabulaire mixte",
  "Newton publie ses Principia en 1687, un tournant qui change la vision de la gravitation.",
  ch("De quelle matière scolaire parle ce texte ?", {"mathématiques": "maths", "histoire": "histoire",
     "français": "français", "physique": "physique", "biologie": "SVT"}), "physique"),
 # Questions jamais vues à l'entraînement (généralisation)
 ("Inédit", "urgence d'un message",
  "Bonjour, la canalisation vient d'exploser, l'eau coule partout dans l'appartement !",
  ch("Quel est le niveau d'urgence ?", {"urgent": "doit être traité tout de suite", "normal": "peut attendre quelques jours"}), "urgent"),
 ("Inédit", "demande de remboursement",
  "Le produit est arrivé cassé, je souhaite récupérer mon argent.",
  nl("Le client veut-il être remboursé ?"), True),
 ("Inédit", "spam",
  "FÉLICITATIONS !!! Vous avez gagné un iPhone, cliquez vite ici pour réclamer votre cadeau",
  nl("Ce message est-il une arnaque ou un spam ?"), True),
 ("Inédit", "dialogue de dresseur Pokémon",
  "Hé toi ! Nos regards se sont croisés, tu sais ce que ça veut dire : combat !",
  ch("Qui parle probablement ?", {"dresseur": "un dresseur qui veut se battre", "vendeur": "un vendeur de boutique",
     "infirmière": "l'infirmière du centre de soins"}), "dresseur"),
]

def run(path):
    a = laya.load(path) if hasattr(laya, "load") else laya.Agent(path)
    out = []
    for cat, piege, s, q, exp in T:
        ans = a.predict(s, {"q": q})["answers"]["q"]
        if ans["type"] == "noul":
            got = ans["noul"] >= .5; c = max(ans["noul"], 1 - ans["noul"])
        elif ans["type"] == "score":
            pr = ans["probabilities"]; got = int(max(pr, key=pr.get)); c = max(pr.values())
        else:
            got = ans["choice"]; c = ans["probabilities"][got]
        out.append((got == exp, got, round(c, 2)))
    return out

base = run(sys.argv[1]); new = run(sys.argv[2])
res = []
for (cat, piege, s, q, exp), b, n in zip(T, base, new):
    res.append({"cat": cat, "piege": piege, "texte": s, "attendu": exp,
                "base": {"ok": b[0], "rep": b[1], "conf": b[2]}, "nuit2": {"ok": n[0], "rep": n[1], "conf": n[2]}})
    print(f"{cat:10} {piege[:34]:34} attendu={str(exp)[:12]:12} base={'OK ' if b[0] else 'X  '}{str(b[1])[:12]:12} nuit2={'OK ' if n[0] else 'X  '}{str(n[1])[:12]} ({n[2]})")
print("SCORE base", sum(r["base"]["ok"] for r in res), "/", len(res), "| nuit2", sum(r["nuit2"]["ok"] for r in res), "/", len(res))
json.dump(res, open(sys.argv[3], "w"), ensure_ascii=False, indent=1, default=str)
