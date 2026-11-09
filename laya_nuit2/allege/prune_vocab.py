"""Élague le vocabulaire de laya-multilingual pour ne garder que l'anglais et le français.

Garde : tokens spéciaux, octets <0xNN>, et tout token écrit uniquement avec
l'alphabet anglais/français + chiffres + ponctuation. Les fusions BPE entre
tokens gardés sont conservées, donc un texte en/fr se découpe exactement pareil.
"""
import json, struct, sys, re, os, shutil
import numpy as np

SRC, DST = sys.argv[1], sys.argv[2]
KEEP_FILE = sys.argv[3] if len(sys.argv) > 3 else None
ALLOWED = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
              "àâäçéèêëîïôöùûüÿœæÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸŒÆ"
              " ▁\n\t\r!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~«»’‘“”…–—€£°§·")
BYTE = re.compile(r"^<0x[0-9A-F]{2}>$")

tok = json.load(open(f"{SRC}/tokenizer/tokenizer.json"))
vocab = tok["model"]["vocab"]
special = {a["content"] for a in tok["added_tokens"]}
if KEEP_FILE:  # liste issue de select_tokens.py (tokens réellement utilisés en/fr)
    keep = sorted(set(json.load(open(KEEP_FILE))) | {vocab[t] for t in special})
else:
    keep = sorted(i for t, i in vocab.items()
                  if t in special or BYTE.match(t) or set(t) <= ALLOWED)
old2new = {o: n for n, o in enumerate(keep)}
inv = {i: t for t, i in vocab.items()}
tok["model"]["vocab"] = {inv[o]: n for o, n in old2new.items()}
kept = tok["model"]["vocab"]
tok["model"]["merges"] = [m for m in tok["model"]["merges"]
                          if m[0] in kept and m[1] in kept and (m[0] + m[1]) in kept]
for a in tok["added_tokens"]:
    a["id"] = old2new[a["id"]]
def remap(o):  # met à jour les ids dans le post-processeur
    if isinstance(o, dict):
        if "ids" in o and isinstance(o["ids"], list): o["ids"] = [old2new[i] for i in o["ids"]]
        for v in o.values(): remap(v)
    elif isinstance(o, list):
        for v in o: remap(v)
remap(tok["post_processor"])

os.makedirs(f"{DST}/tokenizer", exist_ok=True); os.makedirs(f"{DST}/encoder", exist_ok=True)
json.dump(tok, open(f"{DST}/tokenizer/tokenizer.json", "w"), ensure_ascii=False)
for f in ["config.json", "rl_agent_config.json", "tokenizer/tokenizer_config.json", "questions.json", "train_report.json"]:
    if os.path.exists(f"{SRC}/{f}"): shutil.copy(f"{SRC}/{f}", f"{DST}/{f}")
cfg = json.load(open(f"{SRC}/encoder/config.json"))
for k in ["pad_token_id", "bos_token_id", "eos_token_id", "cls_token_id", "sep_token_id", "mask_token_id"]:
    cfg[k] = old2new[cfg[k]]
cfg["vocab_size"] = len(keep)
json.dump(cfg, open(f"{DST}/encoder/config.json", "w"), indent=2)

# Poids : on ne garde que les lignes d'embedding des tokens conservés.
f = open(f"{SRC}/model.safetensors", "rb"); n = struct.unpack("<Q", f.read(8))[0]
hdr = json.loads(f.read(n)); base = 8 + n
DT = {"F16": np.float16, "F32": np.float32, "BF16": np.uint16}
out, blobs, off = {}, [], 0
for k, v in hdr.items():
    if k == "__metadata__": out[k] = v; continue
    a, b = v["data_offsets"]; f.seek(base + a)
    arr = np.frombuffer(f.read(b - a), dtype=DT[v["dtype"]]).reshape(v["shape"])
    if arr.ndim == 2 and arr.shape[0] == len(vocab):
        arr = arr[keep]
    raw = np.ascontiguousarray(arr).tobytes()
    out[k] = {"dtype": v["dtype"], "shape": list(arr.shape), "data_offsets": [off, off + len(raw)]}
    blobs.append(raw); off += len(raw)
h = json.dumps(out, separators=(",", ":")).encode(); h += b" " * (-len(h) % 8)
with open(f"{DST}/model.safetensors", "wb") as g:
    g.write(struct.pack("<Q", len(h))); g.write(h)
    for r in blobs: g.write(r)
json.dump(keep, open(f"{DST}/kept_token_ids.json", "w"))
print(f"tokens : {len(vocab)} -> {len(keep)} | fusions : {len(tok['model']['merges'])}")
