"""Construit le jeu d'entraînement « décideur français + comparateur A/B » pour Laya."""
import json, random
from datasets import load_dataset

R = random.Random(7)
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

def take(ds, n): return ds.shuffle(seed=7).select(range(min(n, len(ds))))

massive = load_dataset("mteb/amazon_massive_intent", "fr")
xnli = load_dataset("facebook/xnli", "fr")
pw = load_dataset("google-research-datasets/paws-x", "fr")
al = load_dataset("tblard/allocine")
am = load_dataset("SetFit/amazon_reviews_multi_fr")

xn_tr = take(xnli["train"], 60000)
plans = {
 "train": [intent_choice(take(massive["train"], 6000)), nli_choice(xn_tr.select(range(0, 4000))), nli_noul(xn_tr.select(range(4000, 7000))),
           paws(take(pw["train"], 4000)), allocine(take(al["train"], 3000)), stars(take(am["train"], 5000)),
           cmp_reviews(take(am["train"], 40000).select(range(5000, 40000)), 3000), cmp_nli(xn_tr.select(range(7000, 60000)), 2500),
           cmp_intent(take(massive["train"], 11514).select(range(6000, 11514)), 2000)],
 "eval": [intent_choice(take(massive["test"], 250)), nli_choice(take(xnli["test"], 250)), nli_noul(take(xnli["test"], 500).select(range(250, 500))),
          paws(take(pw["test"], 250)), allocine(take(al["test"], 250)), stars(take(am["test"], 250)),
          cmp_reviews(take(am["test"], 2000), 250), cmp_nli(xnli["test"], 250), cmp_intent(massive["test"], 250)],
}
for split, gens in plans.items():
    rows = [r for g in gens for r in g]; R.shuffle(rows)
    from collections import Counter; print(split, len(rows), Counter(r["task"] for r in rows))
    with open(f"/home/user/laya/nuit/data/{split}.jsonl", "w") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
