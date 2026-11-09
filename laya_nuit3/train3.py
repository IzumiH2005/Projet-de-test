"""Construit le jeu d'entraînement « décideur français + comparateur A/B » pour Laya."""
import json, random
from datasets import load_dataset

R = random.Random(11)
INTENTS = {
 'alarm_query':"consulter ses alarmes",'alarm_remove':"supprimer une alarme",'alarm_set':"régler une alarme",
 'audio_volume_down':"baisser le volume",'audio_volume_mute':"couper le son",'audio_volume_other':"autre réglage du son",
 'audio_volume_up':"monter le volume",'calendar_query':"consulter l'agenda",'calendar_remove':"supprimer un événement de l'agenda",
 'calendar_set':"ajouter un événement à l'agenda",'cooking_query':"question de cuisine",'cooking_recipe':"demander une recette",
 'datetime_convert':"convertir une heure ou un fuseau",'datetime_query':"demander la date ou l'heure",'email_addcontact':"ajouter un contact",
 'email_query':"consulter ses e-mails",'email_querycontact':"chercher les infos d'un contact",'email_sendemail':"envoyer un e-mail",
 'general_greet':"saluer",'general_joke':"demander une blague",'general_quirky':"question ou remarque décalée",
 'iot_cleaning':"lancer l'aspirateur ou le ménage",'iot_coffee':"faire du café",'iot_hue_lightchange':"changer la couleur des lumières",
 'iot_hue_lightdim':"baisser la lumière",'iot_hue_lightoff':"éteindre la lumière",'iot_hue_lighton':"allumer la lumière",
 'iot_hue_lightup':"augmenter la lumière",'iot_wemo_off':"éteindre une prise connectée",'iot_wemo_on':"allumer une prise connectée",
 'lists_createoradd':"créer une liste ou y ajouter",'lists_query':"consulter une liste",'lists_remove':"retirer d'une liste",
 'music_dislikeness':"dire qu'on n'aime pas une musique",'music_likeness':"dire qu'on aime une musique",'music_query':"demander quelle musique passe",
 'music_settings':"réglage de lecture (aléatoire, répétition)",'news_query':"demander les actualités",'play_audiobook':"écouter un livre audio",
 'play_game':"jouer à un jeu",'play_music':"jouer de la musique",'play_podcasts':"écouter un podcast",'play_radio':"écouter la radio",
 'qa_currency':"taux de change",'qa_definition':"définition d'un mot",'qa_factoid':"question de culture générale",'qa_maths':"calcul",
 'qa_stock':"cours de la bourse",'recommendation_events':"conseil de sortie ou d'événement",'recommendation_locations':"conseil de lieu",
 'recommendation_movies':"conseil de film",'social_post':"publier sur un réseau social",'social_query':"consulter un réseau social",
 'takeaway_order':"commander à emporter",'takeaway_query':"question sur une commande à emporter",'transport_query':"question de transport",
 'transport_taxi':"réserver un taxi",'transport_ticket':"acheter un billet",'transport_traffic':"état de la circulation",'weather_query':"météo"}

def pick(*xs): return R.choice(xs)
def cut(t, n=900): t = " ".join(t.split()); return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"
def row(state, q, exp, task): return {"state": state, "questions": {"q": q}, "expected": {"q": exp}, "task": task}

def intent_choice(d):
    keys = list(INTENTS)
    for x in d:
        opts = [x["label"]] + R.sample([k for k in keys if k != x["label"]], 7)
        R.shuffle(opts)
        yield row(x["text"], {"type": "choice", "instructions": pick("Que demande l'utilisateur ?", "Quelle est l'intention de ce message ?", "Quelle action l'assistant doit-il faire ?"),
                  "criteria": {INTENTS[k]: k.replace("_", " ") for k in opts}}, INTENTS[x["label"]], "intention")

NLI = ["appuyée", "indéterminée", "contredite"]
def nli_choice(d):
    for x in d:
        yield row(f"Texte : {x['premise']}\nAffirmation : {x['hypothesis']}",
                  {"type": "choice", "instructions": pick("Que dit le texte de l'affirmation ?", "L'affirmation est-elle appuyée, contredite, ou le texte ne permet-il pas de trancher ?"),
                   "criteria": {"appuyée": "le texte confirme l'affirmation", "indéterminée": "le texte ne permet pas de savoir", "contredite": "le texte dit le contraire"}},
                  NLI[x["label"]], "nli_choix")
def nli_noul(d):
    for x in d:
        yield row(f"Source : {x['premise']}\nAffirmation : {x['hypothesis']}",
                  {"type": "noul", "instructions": pick("L'affirmation est-elle confirmée par la source ?", "La source permet-elle d'affirmer cela ?")},
                  x["label"] == 0, "verif")
def paws(d):
    for x in d:
        yield row(f"Phrase 1 : {x['sentence1']}\nPhrase 2 : {x['sentence2']}",
                  {"type": "noul", "instructions": pick("Les deux phrases ont-elles exactement le même sens ?", "La phrase 2 est-elle une reformulation fidèle de la phrase 1 ?")},
                  x["label"] == 1, "paraphrase")
def allocine(d):
    for x in d:
        yield row(cut(x["review"]), {"type": "noul", "instructions": pick("Cette critique est-elle positive ?", "L'auteur a-t-il aimé le film ?")}, x["label"] == 1, "sentiment")
STARS = ["très négatif (1 étoile)", "négatif (2 étoiles)", "mitigé (3 étoiles)", "positif (4 étoiles)", "très positif (5 étoiles)"]
def stars(d):
    for x in d:
        yield row(cut(x["text"]), {"type": "score", "instructions": pick("Quelle note le client donne-t-il ?", "À quel point cet avis est-il satisfait ?"), "criteria": STARS}, x["label"], "note")

def ab(a, b, first_is_answer):
    return ("A", "B") if first_is_answer else ("B", "A")
def cmp_reviews(d, n):
    d = list(d); out = 0
    while out < n:
        x, y = R.sample(d, 2)
        if abs(x["label"] - y["label"]) < 2: continue
        best_pos = R.random() < .5
        want_more = R.random() < .5
        hi, lo = (x, y) if x["label"] > y["label"] else (y, x)
        good = hi if want_more else lo; bad = lo if want_more else hi
        A, B = (good, bad) if best_pos else (bad, good)
        yield row(f"Avis A : {cut(A['text'], 450)}\nAvis B : {cut(B['text'], 450)}",
                  {"type": "choice", "instructions": "Quel avis est le plus satisfait ?" if want_more else "Quel avis est le plus mécontent ?",
                   "criteria": {"A": "l'avis A", "B": "l'avis B"}}, "A" if best_pos else "B", "cmp_avis")
        out += 1
def cmp_nli(d, n):
    by = {}
    for x in d: by.setdefault(x["premise"], {}).setdefault(x["label"], x["hypothesis"])
    prem = [p for p, v in by.items() if 0 in v and 2 in v]; R.shuffle(prem)
    for p in prem[:n]:
        pos = R.random() < .5
        A, B = (by[p][0], by[p][2]) if pos else (by[p][2], by[p][0])
        yield row(f"Texte : {p}\nAffirmation A : {A}\nAffirmation B : {B}",
                  {"type": "choice", "instructions": "Quelle affirmation est appuyée par le texte ?", "criteria": {"A": "l'affirmation A", "B": "l'affirmation B"}},
                  "A" if pos else "B", "cmp_verif")
def cmp_intent(d, n):
    d = list(d)
    for _ in range(n):
        x, y = R.sample(d, 2)
        while y["label"] == x["label"]: y = R.choice(d)
        pos = R.random() < .5
        A, B = (x, y) if pos else (y, x)
        yield row(f"Message A : {A['text']}\nMessage B : {B['text']}",
                  {"type": "choice", "instructions": f"Quel message correspond à la demande : « {INTENTS[x['label']]} » ?", "criteria": {"A": "le message A", "B": "le message B"}},
                  "A" if pos else "B", "cmp_intention")

# ---------- nouvelles tâches (nuit 2) ----------
NLI3 = {0: "appuyée", 1: "indéterminée", 2: "contredite"}
def nli_hard_choice(d, task="nli_dur"):
    for x in d:
        yield row(f"Texte : {cut(x['premise'], 700)}\nAffirmation : {x['hypothesis']}",
                  {"type": "choice", "instructions": pick("Que dit le texte de l'affirmation ?", "L'affirmation est-elle appuyée, contredite, ou impossible à trancher avec ce texte ?"),
                   "criteria": {"appuyée": "le texte confirme l'affirmation", "indéterminée": "le texte ne permet pas de savoir", "contredite": "le texte dit le contraire"}},
                  NLI3[int(x["label"])], task)
def nli_hard_noul(d):
    for x in d:
        yield row(f"Source : {cut(x['premise'], 700)}\nAffirmation : {x['hypothesis']}",
                  {"type": "noul", "instructions": pick("L'affirmation est-elle confirmée par la source ?", "La source permet-elle d'affirmer cela ?", "Peut-on déduire cette affirmation de la source ?")},
                  int(x["label"]) == 0, "verif")

SIM = ["sens complètement différent", "quelques points communs", "sujet proche mais sens différent", "presque le même sens", "exactement le même sens"]
def sts(d):
    for x in d:
        s = float(x["similarity_score"]); lv = min(4, int(round(s * 4 / 5)))
        yield row(f"Phrase 1 : {x['sentence1']}\nPhrase 2 : {x['sentence2']}",
                  {"type": "score", "instructions": pick("À quel point ces deux phrases veulent-elles dire la même chose ?", "Quelle est la proximité de sens entre les deux phrases ?"), "criteria": SIM}, lv, "similarite")

def qa_items(d):
    out = []
    for x in d:
        a = x["answers"]; t = a["text"] if isinstance(a, dict) else []
        st = a.get("answer_start", []) if isinstance(a, dict) else []
        out.append({"title": x["title"], "ctx": " ".join(x["context"].split()) if False else x["context"], "q": x["question"],
                    "ans": t[0] if t else None, "start": int(st[0]) if st else None})
    return out
def sentences(ctx):
    import re
    spans, i = [], 0
    for m in re.finditer(r"(?<=[.!?])\s+", ctx):
        spans.append((i, m.start())); i = m.end()
    spans.append((i, len(ctx)))
    return [(a, b) for a, b in spans if b - a > 15]
def qa_noul(items, n):
    by = {}
    for it in items: by.setdefault(it["ctx"], it)
    ctxs = list(by)
    k = 0
    for it in items:
        if k >= n: break
        if it["ans"] is None:
            ctx, yes = it["ctx"], False
        elif R.random() < .5:
            ctx, yes = it["ctx"], True
        else:
            ctx = R.choice(ctxs)
            if ctx == it["ctx"] or (it["ans"] and it["ans"] in ctx): continue
            yes = False
        yield row(f"Question : {it['q']}\nPassage : {cut(ctx, 1100)}",
                  {"type": "noul", "instructions": pick("Le passage contient-il la réponse à la question ?", "Peut-on répondre à la question avec ce passage ?")}, yes, "qa_repond")
        k += 1
def qa_phrase(items, n):
    k = 0
    for it in items:
        if k >= n: break
        if it["ans"] is None or it["start"] is None: continue
        sp = sentences(it["ctx"])
        hit = [j for j, (a, b) in enumerate(sp) if a <= it["start"] < b]
        if not hit or len(sp) < 3: continue
        j = hit[0]; others = [i for i in range(len(sp)) if i != j]
        pick_ix = sorted([j] + R.sample(others, min(len(others), R.choice([2, 3, 4, 5]))))
        labels = "ABCDEF"
        opts = {labels[m]: " ".join(it["ctx"][sp[i][0]:sp[i][1]].split())[:300] for m, i in enumerate(pick_ix)}
        good = labels[pick_ix.index(j)]
        yield row(f"Question : {it['q']}",
                  {"type": "choice", "instructions": "Quelle phrase contient la réponse à la question ?", "criteria": opts}, good, "qa_phrase")
        k += 1
def cmp_qa(items, n):
    good = [it for it in items if it["ans"]]
    ctxs = list({it["ctx"] for it in items})
    k = 0
    while k < n:
        it = R.choice(good); other = R.choice(ctxs)
        if other == it["ctx"] or it["ans"] in other: continue
        pos = R.random() < .5
        A, B = (it["ctx"], other) if pos else (other, it["ctx"])
        yield row(f"Question : {it['q']}\nPassage A : {cut(A, 500)}\nPassage B : {cut(B, 500)}",
                  {"type": "choice", "instructions": "Quel passage permet de répondre à la question ?", "criteria": {"A": "le passage A", "B": "le passage B"}},
                  "A" if pos else "B", "cmp_qa")
        k += 1

def toxic(d):
    for x in d:
        yield row(cut(x["text"]), {"type": "noul", "instructions": pick("Ce message est-il toxique ou insultant ?", "Faut-il modérer ce message ?")}, int(x["toxic"]) == 1, "toxique")
TW = {0: "négatif", 1: "neutre", 2: "positif"}
def tweets(d):
    for x in d:
        yield row(x["text"], {"type": "choice", "instructions": pick("Quel est le ton de ce message ?", "Ce tweet est-il positif, neutre ou négatif ?"),
                  "criteria": {"négatif": "ton négatif", "neutre": "ni positif ni négatif", "positif": "ton positif"}}, TW[int(x["label"])], "ton_tweet")
SUBJ = {"french": "français", "math": "mathématiques", "science": "sciences", "history": "histoire", "geography": "géographie",
        "english": "anglais", "physics": "physique", "chemistry": "chimie", "biology": "biologie", "contemporary_world": "monde contemporain",
        "financial_ed": "éducation financière", "other": "autre"}
def theme(rows_, task, cats):
    for text, cat in rows_:
        opts = cats if len(cats) <= 8 else sorted(R.sample([c for c in cats if c != cat], 7) + [cat])
        yield row(cut(text, 700), {"type": "choice", "instructions": pick("De quel sujet parle ce texte ?", "Dans quelle catégorie ranger ce texte ?"),
                  "criteria": {c: c for c in opts}}, cat, task)
def books(d):
    for x in d:
        r = int(round(float(x["rating"]))) ; r = min(5, max(1, r))
        yield row(cut(x["reader_review"]), {"type": "score", "instructions": pick("Quelle note le lecteur donne-t-il au livre ?", "À quel point ce lecteur a-t-il aimé le livre ?"), "criteria": STARS}, r - 1, "note_livre")

# ---------- chargement ----------
def take(ds, n, off=0): ds = ds.shuffle(seed=11); return ds.select(range(off, min(off + n, len(ds))))
L = load_dataset
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

# ======================= NUIT 3 : entraîner la version int8 sur les cas difficiles =======================
import subprocess, sys, os, glob, time, collections, shutil
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "laya==0.4.30"], check=True)
import torch, laya
from laya.train import finetune, TrainConfig
T0 = time.time()
def h(): return round((time.time() - T0) / 3600, 2)
W = "/kaggle/working"; LOG = f"{W}/rapport_nuit3.json"; rapport = {}
def save(): json.dump(rapport, open(LOG, "w"), ensure_ascii=False, indent=1, default=str)
def log(*a): print(f"[{h()}h]", *a, flush=True)
D = os.path.dirname(glob.glob("/kaggle/input/**/train.jsonl", recursive=True)[0])
ORIG = os.path.dirname(glob.glob("/kaggle/input/**/model.safetensors", recursive=True)[0])
I8 = os.path.dirname(glob.glob("/kaggle/input/**/model_int8.safetensors", recursive=True)[0])
sys.path.insert(0, I8); import laya_int8
log("GPU", torch.cuda.get_device_name(0), "| orig", ORIG, "| int8", I8)

# ---------- 1. point de départ : la version 242 Mo (poids reconstruits) ----------
START = f"{W}/depart_int8"
laya_int8.charger(I8, device="cpu", cache=START)

# ---------- 2. réserve d'exemples : anciens + inédits ----------
pool = [json.loads(l) for l in open(f"{D}/train.jsonl")]
for r in pool: r["src"] = "ancien"
xnli = L("facebook/xnli", "fr"); pw = L("google-research-datasets/paws-x", "fr"); al = L("tblard/allocine")
am = L("SetFit/amazon_reviews_multi_fr"); fqa = L("CATIE-AQ/frenchQA")
HN = "MoritzLaurer/multilingual-NLI-26lang-2mil7"
hard = {s: L(HN, split=f"fr_{s}") for s in ["anli", "fever", "wanli", "ling", "mnli"]}
from datasets import concatenate_datasets
hard_all = concatenate_datasets([hard[s].select_columns(["premise", "hypothesis", "label"]).cast_column("label", hard["anli"].features["label"]) for s in hard]).shuffle(seed=11)
H_TR = hard_all.select(range(750, len(hard_all)))
xn = take(xnli["train"], 60000, 120000); amf = take(am["train"], 80000, 120000)
fq = qa_items(take(fqa["train"], 40000, 60000)); R.shuffle(fq)
nh = len(H_TR)
gens = [nli_choice(xn.select(range(0, 25000))), nli_noul(xn.select(range(25000, 35000))), cmp_nli(xn.select(range(35000, len(xn))), 6000),
        nli_hard_choice(H_TR.select(range(40000, min(nh, 80000)))), nli_hard_noul(H_TR.select(range(min(nh, 80000), min(nh, 95000)))),
        paws(take(pw["train"], 20000, 20000)), allocine(take(al["train"], 15000, 15000)),
        stars(amf.select(range(0, 40000))), cmp_reviews(amf.select(range(40000, len(amf))), 8000),
        qa_noul(fq[:15000], 8000), qa_phrase(fq[15000:30000], 8000), cmp_qa(fq[30000:], 5000)]
neuf = [r for g in gens for r in g]
for r in neuf: r["src"] = "inedit"
pool += neuf
log("réserve", len(pool), "dont inédits", len(neuf), collections.Counter(r["task"] for r in neuf))
rapport["reserve"] = {"total": len(pool), "inedits": len(neuf)}; save()

# ---------- 3. le modèle 459 Mo passe sur toute la réserve : où se trompe-t-il ? ----------
def grade(ans, exp):
    if ans["type"] == "noul":
        p = ans["noul"]; return (p >= .5) == bool(exp), max(p, 1 - p)
    if ans["type"] == "score":
        pr = ans["probabilities"]; b = int(max(pr, key=pr.get)); return b == int(exp), max(pr.values())
    return ans["choice"] == exp, ans["probabilities"][ans["choice"]]

a = laya.Agent(ORIG, device="cuda")
groups = collections.defaultdict(list)
for i, r in enumerate(pool): groups[json.dumps(r["questions"], sort_keys=True, ensure_ascii=False)].append(i)
done = 0
for k, ix in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    q = pool[ix[0]]["questions"]
    for j in range(0, len(ix), 512):
        part = ix[j:j + 512]
        out = a.predict_batch([pool[i]["state"] for i in part], q, batch_size=64, sort_by_length=True, max_len=384, head_max_len=192)
        for i, o in zip(part, out):
            ok, c = grade(o["answers"]["q"], pool[i]["expected"]["q"]); pool[i]["ok"] = ok; pool[i]["conf"] = c
        done += len(part)
        if done % 20000 < 512: log("analyse", done, "/", len(pool))
del a; torch.cuda.empty_cache()

st = collections.defaultdict(lambda: collections.Counter())
for r in pool:
    cat = "faux" if not r["ok"] else ("hesitant" if r["conf"] < .75 else "facile")
    r["cat"] = cat; st[r["task"]][cat] += 1
rapport["analyse_orig"] = {t: dict(c) for t, c in sorted(st.items())}
log("analyse", json.dumps(rapport["analyse_orig"], ensure_ascii=False)); save()

# ---------- 4. jeu d'entraînement ciblé ----------
# faux : x3 (inédit) / x2 (ancien)   hésitant : x1   facile : 20 % (pour ne rien oublier)
BUDGET = 280000
rnd = random.Random(3); train = []
for r in pool:
    if r["cat"] == "faux": n = 3 if r["src"] == "inedit" else 2
    elif r["cat"] == "hesitant": n = 1
    else: n = 1 if rnd.random() < .2 else 0
    train += [r] * n
if len(train) > BUDGET:
    hardp = [r for r in train if r["cat"] == "faux"]; rest = [r for r in train if r["cat"] != "faux"]
    rnd.shuffle(rest); train = hardp + rest[:max(0, BUDGET - len(hardp))]
rnd.shuffle(train)
TR = f"{W}/train3.jsonl"
with open(TR, "w") as f:
    for r in train: f.write(json.dumps({k: r[k] for k in ("state", "questions", "expected", "task")}, ensure_ascii=False) + "\n")
rapport["train"] = {"lignes": len(train), "par_cat": dict(collections.Counter(r["cat"] for r in train)),
                    "par_tache": dict(collections.Counter(r["task"] for r in train))}
log("train", json.dumps(rapport["train"], ensure_ascii=False)); save()
del pool, neuf, train

# ---------- 5. entraînement (depuis la version 242 Mo) ----------
OUT = f"{W}/laya_nuit3_fp16"
cfg = TrainConfig(epochs=2, encoder_lr=2e-5, calib_max=2000, max_len=384, head_max_len=192,
                  shuffle_options=("choice",), log_every=200)
t1 = time.time()
rapport["resume_finetune"] = json.loads(json.dumps(finetune(TR, START, OUT, cfg, device="cuda"), default=str))
rapport["duree_entrainement_h"] = round((time.time() - t1) / 3600, 2); save()
for d in glob.glob(f"{OUT}/checkpoint_*"): shutil.rmtree(d)

# ---------- 6. recompression int8 (bloc 128) ----------
FIN = f"{W}/laya_nuit3_int8"
laya_int8.compresser(OUT, FIN, 128); shutil.copy(f"{I8}/laya_int8.py", FIN)
for f in ["kept_token_ids.json", "README.md"]:
    if os.path.exists(f"{I8}/{f}") and not os.path.exists(f"{FIN}/{f}"): shutil.copy(f"{I8}/{f}", FIN)
FIN_FP = f"{W}/_fin_deq"; laya_int8.charger(FIN, device="cpu", cache=FIN_FP)
os.remove(f"{OUT}/model.safetensors")  # fp16 intermédiaire inutile en sortie

# ---------- 7. test final : 459 Mo (original) vs 242 Mo entraîné ----------
rows = [json.loads(l) for l in open(f"{D}/eval.jsonl")]
def evaluate(path):
    a = laya.Agent(path, device="cuda"); ok = collections.defaultdict(list); det = []
    for r in rows:
        g, c = grade(a.predict(r["state"], r["questions"])["answers"]["q"], r["expected"]["q"])
        ok[r["task"]].append(float(g)); det.append(g)
    pg = []
    for cat, piege, s, q, exp in T:
        ans = a.predict(s, {"q": q})["answers"]["q"]
        if ans["type"] == "noul": got = ans["noul"] >= .5
        elif ans["type"] == "score": pr = ans["probabilities"]; got = int(max(pr, key=pr.get))
        else: got = ans["choice"]
        pg.append({"cat": cat, "piege": piege, "attendu": exp, "rep": got, "ok": got == exp})
    del a; torch.cuda.empty_cache()
    res = {t: round(sum(v) / len(v), 3) for t, v in sorted(ok.items())}
    res["MOYENNE"] = round(sum(res.values()) / len(res), 4)
    return res, det, pg

ro, do, po = evaluate(ORIG); rn, dn, pn = evaluate(FIN_FP)
rapport["test"] = {"original_459": ro, "nuit3_int8_242": rn,
                   "pieges": {"original_459": sum(p["ok"] for p in po), "nuit3_int8_242": sum(p["ok"] for p in pn), "detail_original": po, "detail_nuit3": pn},
                   "cas_rates_par_original": {"nombre": sum(not x for x in do), "maintenant_reussis": sum((not x) and y for x, y in zip(do, dn))},
                   "cas_reussis_par_original": {"nombre": sum(do), "maintenant_rates": sum(x and not y for x, y in zip(do, dn))}}
log("ORIGINAL", ro["MOYENNE"], "| NUIT3 int8", rn["MOYENNE"], "| pièges", rapport["test"]["pieges"]["original_459"], "vs", rapport["test"]["pieges"]["nuit3_int8_242"])
rapport["duree_totale_h"] = h(); save()
shutil.rmtree(FIN_FP); shutil.rmtree(START)
log("FINI")
