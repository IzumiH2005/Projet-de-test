"""Plans de questions « jamais posées mais plausibles », tirés de la découverte non supervisée.

Deux sources d'inédit, toutes deux apprises (discovery.py) :
  combinaison_inedite   : une notion × une manière de demander × un type de support que les annales
                          n'ont jamais réunis, mais que le modèle de plausibilité et le filtrage
                          collaboratif jugent aussi crédibles qu'une vraie question. Le style est
                          montré par de vraies questions d'AUTRES notions (transfert de style).
  savoir_jamais_evalue  : un détail du cours que le modèle positif/non-étiqueté juge évaluable mais
                          qu'aucune annale n'a encore interrogé, posé avec la manière de demander que
                          les savoirs voisins déjà évalués ont reçue.
La sélection est diversifiée (pénalité MMR sur les facettes déjà utilisées, globalement et par notion).
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict

import joblib
import numpy as np

from .blueprint import DOMAIN_OF, Planner
from .config import MODEL_DIR, OUT, SEED

POS = {0: "début d'exercice (question d'entrée)", 1: "milieu d'exercice", 2: "fin d'exercice (question qui conclut)"}


class InventPlanner:
    def __init__(self, seed: int = SEED):
        d = joblib.load(MODEL_DIR / "discovery_data.joblib")
        self.u, self.fs, self.fu = d["units"], d["fs"], d["fu"]
        self.cands, self.atoms = d["candidates"], d["atom_top"]
        self.sf, self.uf = d["style_facets"], d["support_facets"]
        p = MODEL_DIR / "facet_names.json"
        self.names = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"consigne": {}, "support": {}}
        self.base = Planner(seed)
        self.rng = np.random.default_rng(seed)
        self.used = Counter()
        self.used_ex: set[int] = set()

    # ------------------------------------------------------------ descriptions des facettes
    def facet(self, kind: str, f: int) -> dict:
        n = self.names.get(kind, {}).get(str(f), {})
        info = (self.sf if kind == "consigne" else self.uf)[f]
        return {"id": f"{kind[0].upper()}{f}", "nom": n.get("nom", " / ".join(info["termes"][:3])),
                "geste": n.get("geste", ""), "gabarit": n.get("gabarit", ""), "coherence": n.get("coherence", "?")}

    def weak(self, kind: str, f: int) -> bool:
        return self.names.get(kind, {}).get(str(f), {}).get("coherence") == "faible"

    def examples(self, lab, f: int, notion: str, k: int, with_context: bool) -> list[str]:
        """De vraies questions de la facette, prises dans d'AUTRES notions : on transfère la manière, pas le fond."""
        idx = [i for i, u in enumerate(self.u) if lab[i] == f and notion not in u["main"][:2] and i not in self.used_ex]
        pref = [i for i in idx if self.u[i]["src"] == "ecrit"] or idx
        if not pref:
            return []
        pick = [int(i) for i in self.rng.choice(pref, min(k, len(pref)), replace=False)]
        self.used_ex.update(pick)
        return [(self.u[i]["text"][:260] if not with_context else self.u[i]["text"][:300]).strip().replace("\n", " ") for i in pick]

    # ------------------------------------------------------------ sélection diversifiée
    def pick_combos(self, notion: str, n: int) -> list[dict]:
        pool = [c for c in self.cands if c["notion"] == notion and not self.weak("consigne", c["consigne"])]
        out, local = [], Counter()
        for _ in range(n):
            if not pool:
                break
            sc = [c["score"] * 0.8 ** self.used[("c", c["consigne"])] * 0.4 ** local[c["consigne"]] * 0.7 ** local[("s", c["support"])]
                  for c in pool]
            c = pool.pop(int(np.argmax(sc)))
            out.append(c)
            local[c["consigne"]] += 1
            local[("s", c["support"])] += 1
            self.used[("c", c["consigne"])] += 1
        return out

    def plan_notion(self, notion: str, n_combo: int, n_atom: int) -> dict | None:
        qs = []
        for c in self.pick_combos(notion, n_combo):
            qs.append({
                "slot": len(qs) + 1, "notion": notion, "mode": "combinaison_inedite", "nouveaute": c["nouveaute"],
                "plausibilite": c["plausibilite"], "position": POS[c["position"]], "position_bin": c["position"],
                "consigne": self.facet("consigne", c["consigne"]), "consigne_id": c["consigne"],
                "exemples_de_consigne_autres_notions": self.examples(self.fs, c["consigne"], notion, 2, False),
                "support": self.facet("support", c["support"]), "support_id": c["support"],
                "exemple_de_support_autre_notion": self.examples(self.fu, c["support"], notion, 1, True),
            })
        for a in self.atoms.get(notion, [])[:n_atom]:
            f = a["consigne_recommandee"]
            qs.append({
                "slot": len(qs) + 1, "notion": notion, "mode": "savoir_jamais_evalue",
                "nouveaute": "détail du cours évaluable jamais interrogé aux annales",
                "atome_du_cours": a["atome"], "lecon": a["lecon"], "evaluabilite": a["evaluabilite"],
                "position": POS[1], "position_bin": 1,
                "consigne": self.facet("consigne", f), "consigne_id": f,
                "exemples_de_consigne_autres_notions": self.examples(self.fs, f, notion, 1, False),
            })
        if not qs:
            return None
        return {"type": "inedit", "id": f"I-{notion}", "notion": notion, "domaine": DOMAIN_OF[notion],
                "cours": self.base.course_excerpts(notion, 2, 900), "questions": qs}

    def plan_all(self, n_combo: int = 3, n_atom: int = 1) -> list[dict]:
        notions = sorted({c["notion"] for c in self.cands} | set(self.atoms))
        order = sorted(notions, key=lambda n: -max([c["score"] for c in self.cands if c["notion"] == n] or [0]))
        return [p for n in order if (p := self.plan_notion(n, n_combo, n_atom))]


def make_plans(n_combo: int = 3, n_atom: int = 1, seed: int = SEED) -> list[dict]:
    plans = InventPlanner(seed).plan_all(n_combo, n_atom)
    (OUT / "plans_inedit.json").write_text(json.dumps(plans, ensure_ascii=False, indent=1), encoding="utf-8")
    modes = Counter(q["mode"] for p in plans for q in p["questions"])
    print(f"[ok] {len(plans)} plans inédits, {sum(modes.values())} questions ({dict(modes)}) -> {OUT / 'plans_inedit.json'}")
    return plans


if __name__ == "__main__":
    make_plans()
