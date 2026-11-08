import subprocess, sys, os, json, glob, time, collections
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "laya==0.4.30"], check=True)
import torch, laya
from laya.train import finetune, TrainConfig, resolve_checkpoint_dir

D = os.path.dirname(glob.glob("/kaggle/input/**/train.jsonl", recursive=True)[0])
OUT = "/kaggle/working/laya_fr"
LOG = "/kaggle/working/rapport.json"
print("GPU:", torch.cuda.get_device_name(0), "| data:", D, flush=True)
base = resolve_checkpoint_dir("convaiinnovations/laya-multilingual")
rows = [json.loads(l) for l in open(f"{D}/eval.jsonl")]

def evaluate(path):
    a = laya.Agent(path, device="cuda")
    ok, conf = collections.defaultdict(list), collections.defaultdict(list)
    for r in rows:
        ans = a.predict(r["state"], r["questions"])["answers"]["q"]; exp = r["expected"]["q"]
        if ans["type"] == "noul":
            good = (ans["noul"] >= .5) == bool(exp); c = max(ans["noul"], 1 - ans["noul"])
        elif ans["type"] == "score":
            pr = ans["probabilities"]; best = int(max(pr, key=pr.get)); good = best == int(exp); c = max(pr.values())
        else:
            good = ans["choice"] == exp; c = ans["probabilities"][ans["choice"]]
        ok[r["task"]].append(float(good)); conf[r["task"]].append(c)
    del a; torch.cuda.empty_cache()
    res = {t: round(sum(v) / len(v), 3) for t, v in sorted(ok.items())}
    res["MOYENNE"] = round(sum(res.values()) / len(res), 3)
    res["_confiance_moy"] = {t: round(sum(v) / len(v), 3) for t, v in sorted(conf.items())}
    return res

rapport = {"avant": evaluate(base)}
print("AVANT", json.dumps(rapport["avant"], ensure_ascii=False), flush=True)
json.dump(rapport, open(LOG, "w"), ensure_ascii=False, indent=1)

t0 = time.time()
cfg = TrainConfig(epochs=3, max_len=384, head_max_len=192, shuffle_options=("choice",), log_every=50,
                  eval_data=f"{D}/eval.jsonl")
summary = finetune(f"{D}/train.jsonl", base, OUT, cfg, device="cuda")
rapport["duree_h"] = round((time.time() - t0) / 3600, 2)
rapport["resume_finetune"] = json.loads(json.dumps(summary, default=str))
rapport["apres"] = evaluate(OUT)
print("APRES", json.dumps(rapport["apres"], ensure_ascii=False), flush=True)
json.dump(rapport, open(LOG, "w"), ensure_ascii=False, indent=1)
for d in glob.glob(f"{OUT}/checkpoint_*"):
    subprocess.run(["rm", "-rf", d])
print("FINI", flush=True)
