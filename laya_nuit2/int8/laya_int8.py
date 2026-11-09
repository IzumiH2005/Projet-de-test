"""Laya en int8 : compresser un modèle, puis le recharger.

  python laya_int8.py compresser <modele_fp16> <sortie> [groupe]   # groupe : row (défaut), 128, 64, 32
  import laya_int8; agent = laya_int8.charger("<sortie>")

Chaque grande matrice est stockée en int8 (+ une échelle float32 par ligne ou par bloc).
Au chargement, on reconstruit les poids fp16 exactement comme pendant le test de qualité.
"""
import os, sys, json, shutil, tempfile
import torch
from safetensors.torch import load_file, save_file

AUTRES = ["encoder", "tokenizer", "rl_agent_config.json", "questions.json", "train_report.json",
          "config.json", "kept_token_ids.json", "README.md"]


def _quant(w, groupe):
    shape = w.shape; w = w.float()
    w = w.reshape(-1, shape[1]) if groupe == "row" else w.reshape(-1, groupe)
    s = w.abs().amax(1, keepdim=True).clamp(min=1e-8) / 127
    return torch.round(w / s).clamp(-127, 127).to(torch.int8).reshape(shape), s


def compresser(src, dst, groupe="row"):
    groupe = groupe if groupe == "row" else int(groupe)
    sd = load_file(f"{src}/model.safetensors"); out = {}; meta = {"groupe": str(groupe), "int8": []}
    for k, v in sd.items():
        if v.ndim == 2 and v.numel() > 10000 and (groupe == "row" or v.numel() % groupe == 0):
            q, s = _quant(v, groupe); out[k + ".q"] = q; out[k + ".s"] = s.contiguous()
            meta["int8"].append(k)
        else:
            out[k] = v.contiguous()
    os.makedirs(dst, exist_ok=True)
    save_file(out, f"{dst}/model_int8.safetensors", metadata={"laya_int8": json.dumps(meta)})
    for f in AUTRES:
        p = f"{src}/{f}"
        if os.path.isdir(p): shutil.copytree(p, f"{dst}/{f}", dirs_exist_ok=True)
        elif os.path.exists(p): shutil.copy(p, f"{dst}/{f}")


def dequantifier(path):
    from safetensors import safe_open
    with safe_open(f"{path}/model_int8.safetensors", "pt") as f:
        meta = json.loads(f.metadata()["laya_int8"]); sd = {k: f.get_tensor(k) for k in f.keys()}
    out = {}
    for k in meta["int8"]:
        q, s = sd.pop(k + ".q"), sd.pop(k + ".s"); shape = q.shape
        w = q.float().reshape(s.shape[0], -1) * s
        out[k] = w.reshape(shape).to(torch.float16)
    out.update(sd)
    return out


def charger(path, device=None, cache=None):
    """Reconstruit un dossier fp16 (une seule fois, dans `cache`) puis charge Laya."""
    import laya
    cache = cache or os.path.join(tempfile.gettempdir(), "laya_int8_" + os.path.basename(os.path.abspath(path)))
    if not os.path.exists(f"{cache}/model.safetensors"):
        os.makedirs(cache, exist_ok=True)
        for f in AUTRES:
            p = f"{path}/{f}"
            if os.path.isdir(p): shutil.copytree(p, f"{cache}/{f}", dirs_exist_ok=True)
            elif os.path.exists(p): shutil.copy(p, f"{cache}/{f}")
        save_file(dequantifier(path), f"{cache}/model.safetensors")
    return laya.Agent(cache, device=device) if device else laya.load(cache)


if __name__ == "__main__" and sys.argv[1] == "compresser":
    compresser(*sys.argv[2:])
