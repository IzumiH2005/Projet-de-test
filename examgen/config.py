from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SOURCES = DATA / "sources"
CORPUS = DATA / "corpus"      # textes extraits (jsonl)
MODEL_DIR = DATA / "model"    # artefacts d'analyse (joblib / json)
OUT = ROOT / "output"         # plans de questions + questions générées

for p in (CORPUS, MODEL_DIR, OUT):
    p.mkdir(parents=True, exist_ok=True)

# Modèle LLM qui rédige les questions (choix de l'utilisateur : Opus 5.5, effort low)
LLM_MODEL = "claude-opus-5-5"
LLM_EFFORT = "low"

SEED = 42
