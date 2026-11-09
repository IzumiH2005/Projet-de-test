# ======== ESSAI RAPIDE : moyenne des poids original (459 Mo) / nuit 3 ========
import subprocess, sys, os, glob, time, collections, shutil, json, hashlib
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "laya==0.4.30"], check=True)
import torch, laya
from safetensors.torch import load_file, save_file
T0 = time.time(); W = "/kaggle/working"; rapport = {}
def save(): json.dump(rapport, open(f"{W}/rapport_moyenne.json", "w"), ensure_ascii=False, indent=1, default=str)
def log(*a): print(f"[{round((time.time()-T0)/60)}min]", *a, flush=True)
D = os.path.dirname(glob.glob("/kaggle/input/**/eval.jsonl", recursive=True)[0])
ORIG = os.path.dirname(glob.glob("/kaggle/input/**/model.safetensors", recursive=True)[0])
N3 = os.path.dirname(glob.glob("/kaggle/input/**/model_int8.safetensors", recursive=True)[0])
sys.path.insert(0, N3); import laya_int8
log("orig", ORIG, "| nuit3", N3)

def grade(ans, exp):
    if ans["type"] == "noul": return (ans["noul"] >= .5) == bool(exp)
    if ans["type"] == "score": pr = ans["probabilities"]; return int(max(pr, key=pr.get)) == int(exp)
    return ans["choice"] == exp

rows = [json.loads(l) for l in open(f"{D}/eval.jsonl")]
# moitié A = choisir le dosage, moitié B = verdict (coupe stable par hachage du texte)
for r in rows: r["half"] = "A" if int(hashlib.md5(r["state"].encode()).hexdigest(), 16) % 2 == 0 else "B"
log("eval", len(rows), collections.Counter(r["half"] for r in rows))

def evaluate(path):
    a = laya.Agent(path, device="cuda"); det = []
    for r in rows: det.append(grade(a.predict(r["state"], r["questions"])["answers"]["q"], r["expected"]["q"]))
    pg = []
    for cat, piege, s, q, exp in T:
        ans = a.predict(s, {"q": q})["answers"]["q"]
        if ans["type"] == "noul": got = ans["noul"] >= .5
        elif ans["type"] == "score": pr = ans["probabilities"]; got = int(max(pr, key=pr.get))
        else: got = ans["choice"]
        pg.append({"piege": piege, "rep": got, "ok": got == exp})
    del a; torch.cuda.empty_cache()
    return det, pg

def summary(det, half):
    ok = collections.defaultdict(list)
    for r, g in zip(rows, det):
        if half is None or r["half"] == half: ok[r["task"]].append(float(g))
    res = {t: round(sum(v) / len(v), 3) for t, v in sorted(ok.items())}
    res["MOYENNE"] = round(sum(res.values()) / len(res), 4); return res

# poids
P0 = load_file(f"{ORIG}/model.safetensors")
P1 = laya_int8.dequantifier(N3)
assert set(P0) == set(P1), "clés différentes"
def build(alpha):
    d = f"{W}/mix_{int(alpha*100)}"
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(ORIG):
        if f != "model.safetensors":
            p = f"{ORIG}/{f}"; (shutil.copytree(p, f"{d}/{f}", dirs_exist_ok=True) if os.path.isdir(p) else shutil.copy(p, d))
    out = {k: ((1 - alpha) * v.float() + alpha * P1[k].float()).to(v.dtype) if v.is_floating_point() else v for k, v in P0.items()}
    save_file(out, f"{d}/model.safetensors"); return d

res = {}
for alpha in [0.0, 0.15, 0.3, 0.45, 0.6, 1.0]:
    path = ORIG if alpha == 0 else build(alpha)
    det, pg = evaluate(path)
    res[alpha] = {"det": det, "pieges": pg}
    if alpha not in (0.0,): shutil.rmtree(path)
    rapport[f"alpha_{alpha}"] = {"A": summary(det, "A")["MOYENNE"], "B": summary(det, "B")["MOYENNE"], "pieges": sum(p["ok"] for p in pg)}
    log("alpha", alpha, rapport[f"alpha_{alpha}"]); save()

# choix sur la moitié A uniquement (parmi les mélanges, pas 1.0 qu'on sait mauvais)
cands = [a for a in res if 0 < a < 1]
best = max(cands, key=lambda a: summary(res[a]["det"], "A")["MOYENNE"])
d0, d1 = res[0.0]["det"], res[best]["det"]
B0, B1 = summary(d0, "B"), summary(d1, "B")
pertes = {t: round(B1[t] - B0[t], 3) for t in B0 if t != "MOYENNE" and B1[t] - B0[t] < -0.02}
inB = [i for i, r in enumerate(rows) if r["half"] == "B"]
rapport["verdict"] = {
    "alpha_choisi_sur_A": best, "original_B": B0, "melange_B": B1,
    "gain_moyenne_B": round(B1["MOYENNE"] - B0["MOYENNE"], 4),
    "taches_qui_baissent_de_plus_de_2pts": pertes,
    "pieges": {"original": sum(p["ok"] for p in res[0.0]["pieges"]), "melange": sum(p["ok"] for p in res[best]["pieges"]),
               "detail": [{"piege": a["piege"], "orig": a["ok"], "melange": b["ok"]} for a, b in zip(res[0.0]["pieges"], res[best]["pieges"]) if a["ok"] != b["ok"]]},
    "B_rates_orig_maintenant_reussis": sum((not d0[i]) and d1[i] for i in inB), "B_rates_orig": sum(not d0[i] for i in inB),
    "B_reussis_orig_maintenant_rates": sum(d0[i] and not d1[i] for i in inB), "B_reussis_orig": sum(d0[i] for i in inB)}
v = rapport["verdict"]
v["accepte"] = v["gain_moyenne_B"] > 0.003 and v["pieges"]["melange"] >= v["pieges"]["original"] and not pertes
save(); log("VERDICT", json.dumps(v, ensure_ascii=False)[:600])
if v["accepte"]:
    d = build(best); laya_int8.compresser(d, f"{W}/laya_moyenne_int8", 128)
    shutil.copy(f"{N3}/laya_int8.py", f"{W}/laya_moyenne_int8/"); shutil.rmtree(d)
rapport["duree_min"] = round((time.time() - T0) / 60); save(); log("FINI")
