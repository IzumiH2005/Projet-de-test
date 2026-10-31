"""Plans de questions : on échantillonne dans les lois apprises par l'analyse.

Deux modes :
  sujet  : sujets complets au format 2023+ (3 exercices 6/6/8 points). Les notions de chaque
           exercice viennent du graphe PMI, les domaines sont répartis entre exercices comme le
           font les concepteurs, la suite des questions suit la chaîne de Markov des archétypes
           pondérée par l'affinité notion x archétype, avec courbe de difficulté et dépendances.
  banque : questions isolées couvrant TOUT le programme ; pour chaque notion, des archétypes
           tirés de P(archétype | notion) avec diversité (pénalité de répétition type MMR).

Chaque plan embarque : extraits du cours, prototypes de l'archétype, questions réelles proches
(pour le style, pas pour être copiées) et la cible de position/difficulté.
"""
from __future__ import annotations

import json
from collections import Counter

import joblib
import numpy as np

from . import features as F
from .config import MODEL_DIR, OUT, SEED

DOMAIN_OF = {c: d for c, (d, _) in F.CONCEPTS.items()}


class Planner:
    def __init__(self, seed: int = SEED):
        self.m = joblib.load(MODEL_DIR / "models.joblib")
        d = joblib.load(MODEL_DIR / "data.joblib")
        self.rows, self.course, self.art = d["rows"], d["course"], d["art"]
        self.arch = self.m["arch_info"]
        self.k = len(self.arch)
        self.T = np.array(self.art["markov"])
        self.CA = np.array(self.art["concept_arch"])
        self.ci = {c: i for i, c in enumerate(F.CONCEPT_NAMES)}
        self.rng = np.random.default_rng(seed)
        self.Lq = self.m["Lq"]
        self.pmi = {tuple(k.split("|")): v for k, v in self.art["pmi"].items()}

    # ------------------------------------------------------------ poids des notions
    def concept_weights(self, mode: str) -> dict[str, float]:
        """Poids = probabilité attendue (récence) + bonus d'écart cours/épreuves.
        En mode banque on aplatit fortement pour couvrir tout le programme."""
        fc, cs, es = self.art["forecast"], self.art["course_share"], self.art["exam_share"]
        w = {}
        for c in F.CONCEPT_NAMES:
            if c in F.GENERIC and mode == "sujet":
                continue
            base = fc.get(c, 0) + 0.02
            gap = max(cs[c] - es[c], 0) * 4  # notion enseignée mais peu tombée -> à surveiller
            w[c] = (base + gap) ** (0.35 if mode == "banque" else 0.8)
        s = sum(w.values())
        return {c: v / s for c, v in w.items()}

    def pick(self, weights: dict, exclude=()) -> str:
        keys = [k for k in weights if k not in exclude]
        p = np.array([weights[k] for k in keys])
        return keys[self.rng.choice(len(keys), p=p / p.sum())]

    # ------------------------------------------------------------ notions d'un exercice
    def exercise_concepts(self, weights, used_domains: Counter) -> list[str]:
        w = {c: v * (0.25 ** used_domains[DOMAIN_OF[c]]) for c, v in weights.items()}
        anchor = self.pick(w)
        chosen = [anchor]
        n_extra = self.rng.choice([1, 2, 3], p=[0.45, 0.4, 0.15])  # moyenne observée ~3.3 notions/exercice
        for _ in range(n_extra):
            cand = {}
            for c in weights:
                if c in chosen:
                    continue
                s = sum(max(self.pmi.get(tuple(sorted((c, a))), -1), -1) for a in chosen)
                if s > 0:
                    cand[c] = np.exp(s) * weights[c]
            if not cand:
                break
            chosen.append(self.pick(cand))
        return chosen

    # ------------------------------------------------------------ suite d'archétypes
    def archetype_sequence(self, concepts: list[str], n: int, beta: float = 1.3) -> list[tuple[int, str]]:
        aff = np.mean([self.CA[self.ci[c]] for c in concepts], axis=0) ** beta
        prev, seq, used = self.k, [], Counter()
        for i in range(n):
            p = self.T[prev, : self.k] * aff
            p = p * (0.55 ** np.array([used[a] for a in range(self.k)]))  # diversité
            # fin d'exercice : favoriser les archétypes qui « ferment » (écrire du code, complexité)
            if i >= n - 2:
                p = p * (0.5 + 3 * self.T[: self.k, self.k])
            p /= p.sum()
            a = int(self.rng.choice(self.k, p=p))
            # notion ciblée par cette question : celle qui aime le plus cet archétype
            sc = np.array([self.CA[self.ci[c], a] for c in concepts])
            c = concepts[int(self.rng.choice(len(concepts), p=sc / sc.sum()))]
            seq.append((a, c))
            used[a] += 1
            prev = a
        return seq

    # ------------------------------------------------------------ matériaux d'appui
    def exemplars(self, arch: int, concept: str, k: int = 2, exclude: set | None = None) -> list[str]:
        idx = [i for i, r in enumerate(self.rows) if r["arch"] == arch and concept in r["main"][:2]]
        if len(idx) < k:
            idx += [i for i, r in enumerate(self.rows) if r["arch"] == arch and i not in idx]
        idx = [i for i in idx if not exclude or i not in exclude]
        if not idx:
            return []
        pick = list(self.rng.choice(idx, size=min(k, len(idx)), replace=False))
        if exclude is not None:
            exclude.update(pick)
        return [self.rows[i]["text"][:350] for i in pick]

    def course_excerpts(self, concept: str, k: int = 2, chars: int = 900) -> list[dict]:
        secs = self.art["concept_sections"][concept][: k + 2]
        out = []
        for i in self.rng.permutation(secs)[:k]:
            s = self.course[int(i)]
            out.append({"ref": f"{s['chapter']} > {s['lesson']} > {s['title']}", "texte": s["text"][:chars]})
        return out

    def scenario_hint(self, concepts: list[str]) -> list[str]:
        best, score = None, -1
        for t in self.art["scenarios"]:
            s = sum(n for c, n in t["notions_associees"] if c in concepts) + self.rng.random() * 2
            if s > score:
                best, score = t, s
        return best["mots"][:6] if best else []

    def points_split(self, total: float, seq) -> list[float]:
        w = np.array([0.6 + 0.25 * self.arch[a]["bloom_moyen"] for a, _ in seq])
        raw = total * w / w.sum()
        pts = np.maximum(np.round(raw * 2) / 2, 0.5)
        pts[np.argmax(pts)] += total - pts.sum()
        return [float(p) for p in pts]

    # ------------------------------------------------------------ modes
    def plan_exam(self, sujet_id: int) -> dict:
        weights = self.concept_weights("sujet")
        used = Counter()
        exercises, used_ex = [], set()
        lens = {int(k): v for k, v in self.art["ex_lengths"].items() if 6 <= int(k) <= 16}
        L, P = np.array(list(lens)), np.array(list(lens.values()), float)
        for num, total in zip((1, 2, 3), (6.0, 6.0, 8.0)):
            concepts = self.exercise_concepts(weights, used)
            for c in concepts:
                used[DOMAIN_OF[c]] += 1
            n = int(self.rng.choice(L, p=P / P.sum())) + (1 if total == 8 else 0)
            seq = self.archetype_sequence(concepts, n)
            pts = self.points_split(total, seq)
            qs = []
            for i, ((a, c), p) in enumerate(zip(seq, pts)):
                info = self.arch[a]
                qs.append({
                    "slot": i + 1, "notion": c, "archetype_id": a, "archetype": info["nom"],
                    "bloom_cible": info["bloom"], "points": p,
                    "position_cible": round(i / max(n - 1, 1), 2),
                    "depend_de_la_precedente": bool(i > 0 and self.rng.random() < info["depend_d_avant"] * 2.2),
                    "formulations_typiques": info["formulations"][:4],
                    "exemples_reels_de_style": self.exemplars(a, c, 2, used_ex),
                })
            exercises.append({
                "numero": num, "points": total, "notions": concepts,
                "domaines": sorted({DOMAIN_OF[c] for c in concepts}),
                "idee_de_contexte": self.scenario_hint(concepts),
                "cours": [x for c in concepts[:2] for x in self.course_excerpts(c, 1)],
                "questions": qs,
            })
        return {"type": "sujet", "id": f"S{sujet_id:02d}", "format": "Bac NSI écrit, 3h30, 3 exercices obligatoires", "exercices": exercises}

    def plan_bank(self, per_concept: int = 4, concepts: list[str] | None = None) -> list[dict]:
        weights = self.concept_weights("banque")
        concepts = concepts or [c for c in F.CONCEPT_NAMES if c not in ("boucles", "booleens")]
        jobs = []
        for c in concepts:
            n = max(2, int(round(per_concept * (0.6 + 12 * weights[c]))))
            aff = self.CA[self.ci[c]].copy()
            used, items, used_ex = Counter(), [], set()
            for j in range(n):
                p = aff ** 1.5 * (0.35 ** np.array([used[a] for a in range(self.k)]))
                a = int(self.rng.choice(self.k, p=p / p.sum()))
                used[a] += 1
                info = self.arch[a]
                items.append({
                    "slot": j + 1, "notion": c, "archetype_id": a, "archetype": info["nom"],
                    "bloom_cible": info["bloom"], "formulations_typiques": info["formulations"][:4],
                    "exemples_reels_de_style": self.exemplars(a, c, 1, used_ex),
                })
            jobs.append({"type": "banque", "id": f"B-{c}", "notion": c, "domaine": DOMAIN_OF[c],
                         "cours": self.course_excerpts(c, 2, 1100), "questions": items})
        return jobs


def make_plans(n_sujets: int = 2, per_concept: int = 4, seed: int = SEED) -> list[dict]:
    p = Planner(seed)
    plans = [p.plan_exam(i + 1) for i in range(n_sujets)] + p.plan_bank(per_concept)
    (OUT / "plans.json").write_text(json.dumps(plans, ensure_ascii=False, indent=1), encoding="utf-8")
    nq = sum(len(x["questions"]) for pl in plans for x in (pl.get("exercices") or [pl]))
    print(f"[ok] {len(plans)} plans, {nq} questions planifiées -> {OUT / 'plans.json'}")
    return plans
