import sys, json, collections, laya
rows = [json.loads(l) for l in open("nuit2/data/eval.jsonl")]
def evaluate(path):
    a = laya.Agent(path, device="cpu"); ok = collections.defaultdict(list)
    for r in rows:
        ans = a.predict(r["state"], r["questions"])["answers"]["q"]; exp = r["expected"]["q"]
        if ans["type"] == "noul": good = (ans["noul"] >= .5) == bool(exp)
        elif ans["type"] == "score": pr = ans["probabilities"]; good = int(max(pr, key=pr.get)) == int(exp)
        else: good = ans["choice"] == exp
        ok[r["task"]].append(float(good))
    res = {t: round(sum(v)/len(v), 3) for t, v in sorted(ok.items())}
    res["MOYENNE"] = round(sum(res.values())/len(res), 3); return res
out = {p: evaluate(p) for p in sys.argv[1:-1]}
json.dump(out, open(sys.argv[-1], "w"), ensure_ascii=False, indent=1)
ks = list(out); print("tache", *ks)
for t in out[ks[0]]: print(f"{t:14}", *[out[k][t] for k in ks])
