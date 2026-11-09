"""Réserve de données d'entraînement pour Laya (tâches sans données neuves en nuit 3).
Sortie : <tache>.jsonl.gz (format Laya : state / questions / expected / task / src / split)."""
import json, gzip, random, collections, re, sys
from datasets import load_dataset as L
R = random.Random(7); OUT = {}
def pick(*xs): return R.choice(xs)
def cut(t, n=900): t = " ".join(str(t).split()); return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"
def add(task, src, state, q, exp):
    OUT.setdefault(task, []).append({"state": state, "questions": {"q": q}, "expected": {"q": exp}, "task": task, "src": src})
def nl(i): return {"type": "noul", "instructions": i}
STARS = ["très négatif (1 étoile)", "négatif (2 étoiles)", "mitigé (3 étoiles)", "positif (4 étoiles)", "très positif (5 étoiles)"]
def safe(name, f):
    try: f(); print("ok", name, flush=True)
    except Exception as e: print("ÉCHEC", name, repr(e)[:200], flush=True)

# ---- ton des tweets ----
TONQ = {"négatif": "ton négatif", "neutre": "ni positif ni négatif", "positif": "ton positif"}
def ton():
    d = L("ia-bentebib/tweet_eval_sentiment_fr")
    for sp in d:
        for x in d[sp]:
            add("ton_tweet", "tweet_eval_fr", cut(x["text"].strip('"')), {"type": "choice", "instructions": pick("Quel est le ton de ce message ?", "Ce tweet est-il positif, neutre ou négatif ?"), "criteria": TONQ},
                ["négatif", "neutre", "positif"][int(x["labels"])])
safe("ton", ton)

# ---- matière scolaire (vraies questions d'élèves Alloprof) ----
SUBJ = {"french": "français", "math": "mathématiques", "science": "sciences", "history": "histoire", "geography": "géographie",
        "english": "anglais", "physics": "physique", "chemistry": "chimie", "biology": "biologie", "contemporary_world": "monde contemporain",
        "financial_ed": "éducation financière", "other": "autre"}
def matiere():
    d = L("lyon-nlp/alloprof", "queries")
    cats = sorted(set(SUBJ.values()) - {"autre"})
    for sp in d:
        for x in d[sp]:
            c = SUBJ.get(x["subject"], x["subject"])
            if c == "autre" or c not in cats: continue
            opts = sorted(R.sample([k for k in cats if k != c], 5) + [c])
            add("matiere", "alloprof_questions", cut(x["text"], 700), {"type": "choice", "instructions": pick("De quelle matière scolaire parle cette question ?", "Dans quelle matière ranger cette question d'élève ?"),
                "criteria": {k: k for k in opts}}, c)
safe("matiere", matiere)

# ---- toxicité ----
TOXQ = ("Ce message est-il toxique ou insultant ?", "Faut-il modérer ce message ?", "Ce message est-il haineux ou offensant ?")
FRW = re.compile(r"\b(le|la|les|des|est|pas|une|que|qui|et|je|tu|vous|nous|c'est)\b", re.I)
def toxique():
    d = L("FrancophonIA/multilingual-hatespeech-dataset", "French_test")["test"]
    for x in d: add("toxique", "hatespeech_fr", cut(x["text"]), nl(pick(*TOXQ)), x["label"] >= .5)
    m = L("FrancophonIA/multilingual-hatespeech-dataset", "Multilingual_train")["train"]
    by = collections.defaultdict(list)
    for x in m: by[x["language"]].append(x)
    fr = max(by, key=lambda k: sum(bool(FRW.search(x["text"] or "")) * 1.0 for x in by[k][:500]) / max(1, min(500, len(by[k])))
           if not any("ا" in (x["text"] or "") for x in by[k][:50]) else -1)
    print("  langue fr =", fr, len(by[fr]), [x["text"][:60] for x in by[fr][:3]])
    for x in by[fr]: add("toxique", "hatespeech_fr_train", cut(x["text"]), nl(pick(*TOXQ)), x["label"] >= .5)
safe("toxique", toxique)
def toxique_en():
    for x in L("valurank/offensive-multi")["train"]:
        add("toxique_en", "offensive_multi_en", cut(x["text"]), nl(pick(*TOXQ)), int(x["label"]) == 1)
    for cfg in ["offensive", "hate"]:
        d = L("cardiffnlp/tweet_eval", cfg)
        for sp in d:
            for x in d[sp]: add("toxique_en", f"tweet_eval_{cfg}", cut(x["text"]), nl(pick(*TOXQ)), int(x["label"]) == 1)
safe("toxique_en", toxique_en)

# ---- ironie / sarcasme ----
IRQ = ("Ce message est-il ironique ou sarcastique ?", "L'auteur dit-il le contraire de ce qu'il pense ?", "Y a-t-il de l'ironie dans ce texte ?")
def ironie():
    d = L("tlam25/iSarcasm_taskA")
    for sp in d:
        for x in d[sp]:
            t = x.get("tweet") or x["org_tweet"]
            add("ironie", "isarcasm_en", cut(t), nl(pick(*IRQ)), int(x["sarcastic"]) == 1)
            if x.get("rephrase"):   # même idée dite sans ironie : paire contrastée
                add("ironie", "isarcasm_rephrase_en", cut(x["rephrase"]), nl(pick(*IRQ)), False)
    d = L("cardiffnlp/tweet_eval", "irony")
    for sp in d:
        for x in d[sp]: add("ironie", "tweet_eval_irony_en", cut(x["text"]), nl(pick(*IRQ)), int(x["label"]) == 1)
    for x in L("Heschmat/news-headlines-dataset-sarcasm-detection")["train"]:
        add("ironie", "headlines_en", cut(x["headline"]), nl(pick("Ce titre est-il ironique ou satirique ?", *IRQ[:1])), int(x["is_sarcastic"]) == 1)
    for x in L("Bixente-san/humour-taquin-francais")["train"]:
        msg = x["messages"]; u = [m["content"] for m in msg if m["role"] == "user"]; a = [m["content"] for m in msg if m["role"] == "assistant"]
        if u and a: add("ironie", "humour_taquin_fr", cut(f"Question : {u[0]}\nRéponse : {a[0]}"), nl("La réponse est-elle ironique ou moqueuse ?"), True)
safe("ironie", ironie)

# ---- émotions ----
EMO6 = ["tristesse", "joie", "amour", "colère", "peur", "surprise"]
def emotion():
    d = L("JusteLeo/French-emotion"); labs = sorted({x["label"] for x in d["train"]})
    for sp in d:
        for x in d[sp]:
            lab = {"colere": "colère", "degout": "dégoût"}.get(x["label"], x["label"]); add("emotion", "french_emotion", cut(x["text"]), {"type": "choice", "instructions": pick("Quelle émotion exprime ce texte ?", "Quel sentiment domine dans ce message ?"),
                "criteria": {k: k for k in [{"colere": "colère", "degout": "dégoût"}.get(l, l) for l in labs]}}, lab)
    d = L("TPM-28/emotion-FR")
    for sp in d:
        for x in d[sp]:
            add("emotion", "emotion_fr_6", cut(x["text"]), {"type": "choice", "instructions": pick("Quelle émotion exprime ce texte ?", "Quel sentiment domine dans ce message ?"),
                "criteria": {k: k for k in EMO6}}, EMO6[int(x["label"])])
    d = L("romainm4/french-emotion-movie-reviews")
    for sp in d:
        for x in d[sp]:
            v = x["valence"];  # -1..1 → 5 niveaux
            if v is None: continue
            lv = min(4, max(0, int(round((float(v) + 1) * 2))))
            add("note_nuance", "movie_emotion_valence", cut(x["text"]), {"type": "score", "instructions": pick("Quelle note le spectateur donne-t-il ?", "À quel point cette critique est-elle positive ?"), "criteria": STARS}, lv)
safe("emotion", emotion)

# ---- similarité (SICK-fr) + NLI simple ----
SIM = ["sens complètement différent", "quelques points communs", "sujet proche mais sens différent", "presque le même sens", "exactement le même sens"]
NLI = {"ENTAILMENT": "appuyée", "NEUTRAL": "indéterminée", "CONTRADICTION": "contredite"}
def sick():
    d = L("maximoss/sick-fr"); s = L("Lajavaness/SICK-fr"); rel = {}
    for sp in s:
        for x in s[sp]: rel[(x["sentence_A"].rstrip(" ."), x["sentence_B"].rstrip(" ."))] = x["relatedness_score"]
    for sp in d:
        for x in d[sp]:
            A, B = x["sentence_A"], x["sentence_B"]; r = rel.get((A.rstrip(" ."), B.rstrip(" .")))
            if r is not None:
                add("similarite", "sick_fr", f"Phrase 1 : {A}\nPhrase 2 : {B}", {"type": "score", "instructions": pick("À quel point ces deux phrases veulent-elles dire la même chose ?", "Quelle est la proximité de sens entre les deux phrases ?"), "criteria": SIM},
                    min(4, max(0, int(round(float(r) - 1)))))
            add("nli_choix", "sick_fr", f"Texte : {A}\nAffirmation : {B}", {"type": "choice", "instructions": "L'affirmation est-elle appuyée, contredite, ou le texte ne permet-il pas de trancher ?",
                "criteria": {"appuyée": "le texte confirme l'affirmation", "indéterminée": "le texte ne permet pas de savoir", "contredite": "le texte dit le contraire"}}, NLI[x["entailment_label"]])
    for sp in ["train", "test"]:
        for x in L("mteb/sts22-crosslingual-sts", "fr")[sp]:
            add("similarite", "sts22_fr", f"Texte 1 : {cut(x['sentence1'], 500)}\nTexte 2 : {cut(x['sentence2'], 500)}", {"type": "score", "instructions": "Ces deux articles parlent-ils de la même chose ?", "criteria": SIM},
                min(4, max(0, int(round(4 - float(x["score"]) + 1 - 1)))))  # sts22 : 1 = identique, 4 = différent
safe("sick", sick)

# ---- critiques de films (binaire) ----
def films():
    for x in L("SergeiZu/french-film-reviews")["train"]:
        add("sentiment", "film_reviews_fr", cut(x["review"]), nl(pick("Cette critique est-elle positive ?", "L'auteur a-t-il aimé le film ?")), int(x["label"]) == 1)
safe("films", films)

# ---- écriture : dédoublonnage + 10 % mis de côté pour tester ----
stats = {}
for t, rows in OUT.items():
    seen = set(); uniq = []
    for r in rows:
        k = (r["state"], json.dumps(r["expected"]))
        if k in seen: continue
        seen.add(k); uniq.append(r)
    R.shuffle(uniq); n_test = min(1000, len(uniq) // 10)
    for i, r in enumerate(uniq): r["split"] = "test" if i < n_test else "train"
    with gzip.open(f"{t}.jsonl.gz", "wt", encoding="utf-8") as f:
        for r in uniq: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    stats[t] = {"total": len(uniq), "test": n_test, "sources": dict(collections.Counter(r["src"] for r in uniq)),
                "etiquettes": dict(collections.Counter(str(r["expected"]["q"]) for r in uniq).most_common(8))}
json.dump(stats, open("stats.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(stats, ensure_ascii=False, indent=1))
