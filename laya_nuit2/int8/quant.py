
import subprocess, sys, os, json, glob, time, collections
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "laya==0.4.30"], check=True)
import torch, laya
M = os.path.dirname(glob.glob("/kaggle/input/**/model.safetensors", recursive=True)[0])
E = glob.glob("/kaggle/input/**/eval.jsonl", recursive=True)[0]
print("GPU", torch.cuda.get_device_name(0), M, E, flush=True)
rows = [json.loads(l) for l in open(E)]
T = json.loads('[["Sarcasme", "ironie : mots positifs, sens négatif", "Génial, encore un colis livré avec trois semaines de retard et la boîte écrasée. Vraiment, bravo.", {"type": "choice", "instructions": "Le client est-il satisfait ?", "criteria": {"positif": "avis positif", "négatif": "avis négatif"}}, "négatif"], ["Sarcasme", "ironie subtile", "Merveilleux ce téléphone, la batterie tient presque jusqu\'au petit-déjeuner.", {"type": "choice", "instructions": "Le client est-il satisfait ?", "criteria": {"positif": "avis positif", "négatif": "avis négatif"}}, "négatif"], ["Négation", "double négation", "Je ne peux pas dire que je n\'ai pas aimé ce film, bien au contraire.", {"type": "choice", "instructions": "Le client est-il satisfait ?", "criteria": {"positif": "avis positif", "négatif": "avis négatif"}}, "positif"], ["Négation", "mots négatifs, avis positif", "Aucun défaut, rien à redire, pas une seule déception.", {"type": "choice", "instructions": "Le client est-il satisfait ?", "criteria": {"positif": "avis positif", "négatif": "avis négatif"}}, "positif"], ["Note", "mitigé : un plus, un moins", "La qualité est correcte mais le prix est vraiment excessif pour ce que c\'est. Bof.", {"type": "score", "instructions": "Quelle note le client donne-t-il ?", "criteria": ["très négatif (1 étoile)", "négatif (2 étoiles)", "mitigé (3 étoiles)", "positif (4 étoiles)", "très positif (5 étoiles)"]}, 2], ["Note", "enthousiasme total", "Un chef-d\'œuvre absolu, je l\'ai déjà offert à toute ma famille !", {"type": "score", "instructions": "Quelle note le client donne-t-il ?", "criteria": ["très négatif (1 étoile)", "négatif (2 étoiles)", "mitigé (3 étoiles)", "positif (4 étoiles)", "très positif (5 étoiles)"]}, 4], ["Logique", "chiffre modifié", "Texte : Marie est arrivée à Lyon en 2015 après dix ans passés à Marseille.\\nAffirmation : Marie a vécu cinq ans à Marseille.", {"type": "choice", "instructions": "L\'affirmation est-elle appuyée, contredite, ou le texte ne permet-il pas de trancher ?", "criteria": {"appuyée": "le texte confirme l\'affirmation", "indéterminée": "le texte ne permet pas de savoir", "contredite": "le texte dit le contraire"}}, "contredite"], ["Logique", "déduction temporelle", "Texte : Marie est arrivée à Lyon en 2015 après dix ans passés à Marseille.\\nAffirmation : En 2010, Marie vivait à Marseille.", {"type": "choice", "instructions": "L\'affirmation est-elle appuyée, contredite, ou le texte ne permet-il pas de trancher ?", "criteria": {"appuyée": "le texte confirme l\'affirmation", "indéterminée": "le texte ne permet pas de savoir", "contredite": "le texte dit le contraire"}}, "appuyée"], ["Logique", "info absente (ne pas inventer)", "Texte : Marie est arrivée à Lyon en 2015 après dix ans passés à Marseille.\\nAffirmation : Marie travaille dans un hôpital.", {"type": "choice", "instructions": "L\'affirmation est-elle appuyée, contredite, ou le texte ne permet-il pas de trancher ?", "criteria": {"appuyée": "le texte confirme l\'affirmation", "indéterminée": "le texte ne permet pas de savoir", "contredite": "le texte dit le contraire"}}, "indéterminée"], ["Logique", "quantificateur « tous / certains »", "Texte : Certains élèves de la classe ont réussi l\'examen.\\nAffirmation : Tous les élèves ont réussi l\'examen.", {"type": "choice", "instructions": "L\'affirmation est-elle appuyée, contredite, ou le texte ne permet-il pas de trancher ?", "criteria": {"appuyée": "le texte confirme l\'affirmation", "indéterminée": "le texte ne permet pas de savoir", "contredite": "le texte dit le contraire"}}, "indéterminée"], ["Logique", "inversion des rôles", "Texte : Le chat a été poursuivi par le chien dans le jardin.\\nAffirmation : Le chat poursuivait le chien.", {"type": "choice", "instructions": "L\'affirmation est-elle appuyée, contredite, ou le texte ne permet-il pas de trancher ?", "criteria": {"appuyée": "le texte confirme l\'affirmation", "indéterminée": "le texte ne permet pas de savoir", "contredite": "le texte dit le contraire"}}, "contredite"], ["Logique", "négation cachée", "Texte : Le ministre a refusé de confirmer sa démission.\\nAffirmation : Le ministre a confirmé sa démission.", {"type": "choice", "instructions": "L\'affirmation est-elle appuyée, contredite, ou le texte ne permet-il pas de trancher ?", "criteria": {"appuyée": "le texte confirme l\'affirmation", "indéterminée": "le texte ne permet pas de savoir", "contredite": "le texte dit le contraire"}}, "contredite"], ["Paraphrase", "mêmes mots, sens inversé", "Phrase 1 : Paul a prêté de l\'argent à Julie.\\nPhrase 2 : Julie a prêté de l\'argent à Paul.", {"type": "noul", "instructions": "Les deux phrases ont-elles exactement le même sens ?"}, false], ["Paraphrase", "mots différents, même sens", "Phrase 1 : Le magasin ouvre à neuf heures.\\nPhrase 2 : L\'ouverture de la boutique a lieu à 9h.", {"type": "noul", "instructions": "Les deux phrases ont-elles exactement le même sens ?"}, true], ["Toxicité", "insulte polie / déguisée", "Avec tout le respect que je vous dois, vous êtes d\'une stupidité rare.", {"type": "noul", "instructions": "Ce message est-il toxique ou insultant ?"}, true], ["Toxicité", "gros mot mais bienveillant", "Putain, t\'es trop fort, bravo pour ton concours !", {"type": "noul", "instructions": "Ce message est-il toxique ou insultant ?"}, false], ["Toxicité", "critique ferme mais respectueuse", "Je ne suis pas du tout d\'accord avec votre analyse, les chiffres disent l\'inverse.", {"type": "noul", "instructions": "Ce message est-il toxique ou insultant ?"}, false], ["Intention", "demande indirecte", "Je vais finir par être en retard demain si personne ne me réveille à 6h30...", {"type": "choice", "instructions": "Que demande l\'utilisateur ?", "criteria": {"régler une alarme": "alarm set", "météo": "weather query", "jouer de la musique": "play music", "envoyer un message": "email send"}}, "régler une alarme"], ["Intention", "mot-piège « musique »", "Est-ce qu\'il va pleuvoir pendant le festival de musique samedi ?", {"type": "choice", "instructions": "Que demande l\'utilisateur ?", "criteria": {"régler une alarme": "alarm set", "météo": "weather query", "jouer de la musique": "play music", "envoyer un message": "email send"}}, "météo"], ["Question", "bon thème mais pas de réponse", "Question : En quelle année la tour Eiffel a-t-elle été construite ?\\nPassage : La tour Eiffel est le monument le plus visité de Paris, avec ses 330 mètres de hauteur.", {"type": "noul", "instructions": "Le passage répond-il à la question ?"}, false], ["Question", "réponse formulée autrement", "Question : Qui a écrit Les Misérables ?\\nPassage : Publié en 1862, ce roman fleuve est l\'œuvre de Victor Hugo, alors en exil à Guernesey.", {"type": "noul", "instructions": "Le passage répond-il à la question ?"}, true], ["Matière", "sujet scolaire", "On calcule la dérivée de f(x)=x² pour trouver la pente de la tangente en x=3.", {"type": "choice", "instructions": "De quelle matière scolaire parle ce texte ?", "criteria": {"mathématiques": "maths", "histoire": "histoire", "français": "français", "physique": "physique", "biologie": "SVT"}}, "mathématiques"], ["Matière", "piège : vocabulaire mixte", "Newton publie ses Principia en 1687, un tournant qui change la vision de la gravitation.", {"type": "choice", "instructions": "De quelle matière scolaire parle ce texte ?", "criteria": {"mathématiques": "maths", "histoire": "histoire", "français": "français", "physique": "physique", "biologie": "SVT"}}, "physique"], ["Inédit", "urgence d\'un message", "Bonjour, la canalisation vient d\'exploser, l\'eau coule partout dans l\'appartement !", {"type": "choice", "instructions": "Quel est le niveau d\'urgence ?", "criteria": {"urgent": "doit être traité tout de suite", "normal": "peut attendre quelques jours"}}, "urgent"], ["Inédit", "demande de remboursement", "Le produit est arrivé cassé, je souhaite récupérer mon argent.", {"type": "noul", "instructions": "Le client veut-il être remboursé ?"}, true], ["Inédit", "spam", "FÉLICITATIONS !!! Vous avez gagné un iPhone, cliquez vite ici pour réclamer votre cadeau", {"type": "noul", "instructions": "Ce message est-il une arnaque ou un spam ?"}, true], ["Inédit", "dialogue de dresseur Pokémon", "Hé toi ! Nos regards se sont croisés, tu sais ce que ça veut dire : combat !", {"type": "choice", "instructions": "Qui parle probablement ?", "criteria": {"dresseur": "un dresseur qui veut se battre", "vendeur": "un vendeur de boutique", "infirmière": "l\'infirmière du centre de soins"}}, "dresseur"]]')
groups = collections.defaultdict(list)
for i, r in enumerate(rows): groups[json.dumps(r["questions"], sort_keys=True)].append(i)

def dec(a):
    if a["type"] == "noul": return a["noul"] >= .5, a["noul"]
    if a["type"] == "score":
        pr = a["probabilities"]; b = max(pr, key=pr.get); return int(b), pr[b]
    return a["choice"], a["probabilities"][a["choice"]]

def run(agent):
    out = [None] * len(rows)
    for qk, idx in groups.items():
        q = json.loads(qk)
        for j in range(0, len(idx), 32):
            sub = idx[j:j+32]
            res = agent.predict_batch([rows[i]["state"] for i in sub], q)
            for i, r in zip(sub, res): out[i] = dec(r["answers"]["q"])
    p = [dec(agent.predict(s, {"q": q})["answers"]["q"]) for c, pi, s, q, e in T]
    return out, p

def score(out, p):
    ok = collections.defaultdict(list)
    for r, (d, c) in zip(rows, out):
        e = r["expected"]["q"]
        ok[r["task"]].append(float(d == (bool(e) if isinstance(d, bool) else (int(e) if isinstance(d, int) else e))))
    res = {t: round(sum(v)/len(v), 4) for t, v in sorted(ok.items())}
    res["MOYENNE"] = round(sum(res.values())/len(res), 4)
    res["pieges"] = sum(d == (t[4] if not isinstance(d, int) or isinstance(d, bool) else int(t[4])) for (d, c), t in zip(p, T))
    return res

def fq(w, group):
    shape = w.shape; w = w.float()
    w = w.reshape(-1, shape[1]) if group == "row" else w.reshape(-1, group)
    s = w.abs().amax(1, keepdim=True).clamp(min=1e-8) / 127
    return (torch.round(w / s).clamp(-127, 127) * s).reshape(shape)

agent = laya.Agent(M, device="cuda")
base = {k: v.clone() for k, v in agent.model.state_dict().items()}
VARIANTES = [("fp16 (référence)", None, None), ("int8 par ligne", "row", "row"), ("int8 bloc 128", 128, 128),
             ("int8 bloc 64", 64, 64), ("int8 bloc 32", 32, 32), ("int8 bloc 32, emb par ligne", 32, "row")]
rapport = {}; ref = None
for name, g, ge in VARIANTES:
    t0 = time.time(); sd = {}; nb = 0
    for k, v in base.items():
        if g and v.ndim == 2 and v.numel() > 10000:
            gg = ge if "tok_embeddings" in k else g
            if gg == "row" or v.numel() % gg == 0:
                sd[k] = fq(v, gg).to(v.dtype); nb += 1; continue
        sd[k] = v
    agent.model.load_state_dict(sd)
    out, p = run(agent)
    res = score(out, p)
    if ref is None: ref = (out, p)
    acc = sum(a[0] == b[0] for a, b in zip(out, ref[0])) / len(out)
    diff = sum(abs(float(a[1]) - float(b[1])) for a, b in zip(out, ref[0])) / len(out)
    res["accord_avec_fp16"] = round(acc, 4); res["ecart_confiance"] = round(diff, 4); res["matrices_quantifiees"] = nb
    res["duree_s"] = round(time.time() - t0)
    rapport[name] = res
    print(name, json.dumps(res, ensure_ascii=False), flush=True)
    json.dump(rapport, open("/kaggle/working/rapport_int8.json", "w"), ensure_ascii=False, indent=1)
print("FINI", flush=True)
