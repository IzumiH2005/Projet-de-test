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
massive = L("mteb/amazon_massive_intent", "fr"); xnli = L("facebook/xnli", "fr"); pw = L("google-research-datasets/paws-x", "fr")
al = L("tblard/allocine"); am = L("SetFit/amazon_reviews_multi_fr")
HN = "MoritzLaurer/multilingual-NLI-26lang-2mil7"
hard = {s: L(HN, split=f"fr_{s}") for s in ["anli", "fever", "wanli", "ling", "mnli"]}
from datasets import concatenate_datasets
hard_all = concatenate_datasets([hard[s].select_columns(["premise", "hypothesis", "label"]).cast_column("label", hard["anli"].features["label"]) for s in hard]).shuffle(seed=11)
print("hard nli", len(hard_all), {s: len(hard[s]) for s in hard})
H_EV = hard_all.select(range(0, 750)); H_TR = hard_all.select(range(750, len(hard_all)))
stsb = L("PhilipMay/stsb_multi_mt", "fr")
fqa = L("CATIE-AQ/frenchQA")
print("frenchQA", {k: len(v) for k, v in fqa.items()})
fq_tr = qa_items(take(fqa["train"], 60000)); R.shuffle(fq_tr)
fq_ev = qa_items(take(fqa["validation" if "validation" in fqa else "test"], 3000)) if len(fqa) > 1 else qa_items(take(fqa["train"], 3000, 60000))
tox = L("textdetox/multilingual_toxicity_dataset", split="fr").shuffle(seed=11)
tw = L("mteb/tweet_sentiment_multilingual", "french")
ap = L("lyon-nlp/alloprof", "documents", split="test").shuffle(seed=11)
mk = L("masakhane/masakhanews", "fra")
sib = L("Davlan/sib200", "fra_Latn")
bk = L("Abirate/french_book_reviews", split="train").shuffle(seed=11)
print("sizes tox", len(tox), "alloprof", len(ap), "books", len(bk))

ap_rows = [(x["text"], SUBJ.get(x["topic"], x["topic"])) for x in ap]
ap_cats = sorted({c for _, c in ap_rows})
mk_cats = sorted(set(mk["train"]["category"])); sib_cats = sorted(set(sib["train"]["category"]))
MK = {"business": "économie", "entertainment": "divertissement", "health": "santé", "politics": "politique", "religion": "religion", "sports": "sport", "technology": "technologie"}
SIB = {"science/technology": "science et technologie", "travel": "voyage", "politics": "politique", "sports": "sport", "health": "santé", "entertainment": "divertissement", "geography": "géographie"}
def mkr(ds): return [(x["headline"] + ". " + x["text"], MK.get(x["category"], x["category"])) for x in ds]
def sibr(ds): return [(x["text"], SIB.get(x["category"], x["category"])) for x in ds]
mk_c = sorted({MK.get(c, c) for c in mk_cats}); sib_c = sorted({SIB.get(c, c) for c in sib_cats})

xn = take(xnli["train"], 120000)
am_tr = take(am["train"], 120000)
mtr = massive["train"].shuffle(seed=11)
plans = {
 "train": [
  intent_choice(mtr), cmp_intent(mtr, 8000),
  nli_choice(xn.select(range(0, 20000))), nli_noul(xn.select(range(20000, 35000))), cmp_nli(xn.select(range(35000, 120000)), 12000),
  nli_hard_choice(H_TR.select(range(0, 25000))), nli_hard_noul(H_TR.select(range(25000, 40000))),
  paws(take(pw["train"], 20000)), allocine(take(al["train"], 15000)),
  stars(am_tr.select(range(0, 25000))), cmp_reviews(am_tr.select(range(25000, 120000)), 15000),
  sts(stsb["train"]),
  qa_noul(fq_tr[:25000], 15000), qa_phrase(fq_tr[25000:45000], 10000), cmp_qa(fq_tr[45000:], 10000),
  toxic(tox.select(range(500, len(tox)))), tweets(tw["train"]),
  theme(ap_rows[500:], "matiere", ap_cats), theme(mkr(mk["train"]), "theme_info", mk_c), theme(sibr(sib["train"]), "theme_info", sib_c),
  books(bk.select(range(500, len(bk)))),
 ],
 "eval_new": [
  nli_hard_choice(H_EV.select(range(0, 250))), nli_hard_noul(H_EV.select(range(250, 500))), sts(stsb["test"].shuffle(seed=11).select(range(250))),
  qa_noul(fq_ev, 250), qa_phrase(fq_ev, 250), cmp_qa(fq_ev, 250),
  toxic(tox.select(range(0, 250))), tweets(tw["test"].shuffle(seed=11).select(range(250))),
  theme(ap_rows[:250], "matiere", ap_cats), theme(mkr(mk["test"]) + sibr(sib["test"]), "theme_info", None) if False else theme(mkr(mk["test"])[:250], "theme_info", mk_c),
  books(bk.select(range(0, 250))),
 ],
}
from collections import Counter
for split, gens in plans.items():
    rows = [r for g in gens for r in g]; R.shuffle(rows)
    print(split, len(rows), Counter(r["task"] for r in rows))
    with open(f"/home/user/laya/nuit2/data/{split}.jsonl", "w") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
