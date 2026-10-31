"""Plans de génération : le profil appris du professeur appliqué à tout le cours.

Pour chaque section du cours (y compris celles qui ne sont jamais tombées) :
  - un cas pratique complet qui suit le squelette découvert (nombre de questions, manière de
    demander par rang, barème par rang, longueur attendue par point), avec une section partenaire
    choisie par co-occurrence dans les anciens sujets ;
  - des exercices courts, un par manière de demander plausible pour cette section ;
Puis quelques sujets blancs complets, sections tirées selon la probabilité apprise pour l'année
suivante.

Chaque plan transporte ses exemples réels (un ancien sujet proche, ses questions, son corrigé),
le cours de la section (texte et articles), et des documents réels réutilisables (annexes des
anciens sujets). Aucune règle de style n'est écrite ici : tout vient du profil.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import numpy as np

from .profile import Teacher, art_ids


def _clip(t: str, n: int) -> str:
    t = re.sub(r"[ \t]+", " ", t or "").strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + " […]"


class Planner:
    def __init__(self, t: Teacher):
        self.t = t
        self.qpos = {id(q): i for i, q in enumerate(t.Q)}
        n_q = t.n_q.most_common(1)[0][0]
        self.n_q = n_q
        tot = [sum(t.qs[i].points or 0 for i in idx) for idx in t.parts.values()]
        tot = [x for x in tot if x > 0]
        self.total_points = float(np.median(tot)) if tot else 10.0
        pr = t.detail_stats["points_par_rang"]
        share = np.array([pr.get(str(p), 1 / n_q) for p in range(n_q)], float)
        self.points = [max(1, round(x)) for x in share / share.sum() * self.total_points]
        self.cpp = t.detail_stats["chars_par_point_p10_p50_p90"]
        # opération mentale dominante par rang
        self.op_by_pos = {}
        for p in range(n_q):
            c = Counter(q.op for q in t.Q if q.position == p)
            if c:
                self.op_by_pos[p] = c.most_common(1)[0][0]
        self._annex_bank()

    # ------------------------------------------------------------------ matériaux réels
    def _annex_bank(self):
        t = self.t
        items = []
        seen = set()
        for (exam, part), idx in t.parts.items():
            for title, body in t.qs[idx[0]].annexes:
                key = re.sub(r"\W+", "", body[:200].lower())
                if len(body) < 150 or key in seen:
                    continue
                seen.add(key)
                items.append({"exam": exam, "titre": title.strip(), "texte": body.strip()})
        self.bank = items
        self.bank_S = t.sec_scores([b["titre"] + " " + b["texte"][:4000] for b in items]) if items else np.zeros((0, len(t.sections)))

    def bank_for(self, si: int, k: int = 4) -> list[dict]:
        order = np.argsort(-self.bank_S[:, si])[:k]
        return [{"source": self.bank[i]["exam"], "titre": self.bank[i]["titre"], "texte": _clip(self.bank[i]["texte"], 2200)}
                for i in order if self.bank_S[i, si] > 0.05]

    def course_of(self, si: int) -> dict:
        s = self.t.sections[si]
        arts = [p for p in s.passages if p.startswith("Article ")]
        txt = [p for p in s.passages if not p.startswith("Article ")]
        return {"section": s.title, "theme": s.parent, "texte": _clip("\n".join(txt), 3500),
                "articles": [_clip(a, 1200) for a in arts[:10]]}

    def exemplar_parts(self, si: int, k: int = 2) -> list[dict]:
        t = self.t
        rows = []
        for key, idx in t.parts.items():
            js = [self.qpos[id(t.qs[i])] for i in idx if id(t.qs[i]) in self.qpos]
            if not js:
                continue
            sc = float(np.mean(t.S[js, si]))
            has = sum(bool(t.qs[i].answer) for i in idx)
            rows.append((sc, has, key, idx))
        rows.sort(key=lambda r: -r[0])
        pick = rows[:1]
        with_ans = [r for r in rows[1:12] if r[1]]
        if with_ans and not pick[0][1]:
            pick.append(with_ans[0])
        elif len(rows) > 1:
            pick.append(rows[1])
        out = []
        for sc, has, (exam, part), idx in pick[:k]:
            q0 = t.qs[idx[0]]
            out.append({"sujet": exam, "situation": _clip(q0.situation, 1800),
                        "annexes": [_clip(a, 90) for a, _ in q0.annexes],
                        "questions": [{"enonce": t.qs[i].stem, "points": t.qs[i].points,
                                       "corrige": _clip(t.qs[i].answer, 900) if t.qs[i].answer else None} for i in idx]})
        return out

    def partner(self, si: int) -> int | None:
        t = self.t
        best, bs = None, 0.0
        for (a, b), n in t.co.items():
            if si not in (a, b) or n < 2:
                continue
            j = b if a == si else a
            lift = n / max(t.sec_freq.get(j, 0) * len(t.ex_secs), 1)
            if lift > bs:
                best, bs = j, lift
        return best

    def facet_card(self, f: int, si: int | None = None) -> dict:
        t = self.t
        fc = t.facets[f]
        ex = list(fc["exemples"][:3])
        if si is not None:  # exemple de cette manière de demander pris sur une section proche si possible
            near = [q.stem for q in t.Q if q.facet == f and q.sec == si]
            ex = (near[:1] + ex)[:3]
        return {"facette": f, "nom": fc["nom"], "exemples_reels": [_clip(e, 260) for e in ex]}

    def op_card(self, o: int) -> dict:
        op = self.t.ops[o]
        return {"operation": o, "fort": op["fort"], "faible": op["faible"]}

    # ------------------------------------------------------------------ plans
    def cas(self, si: int, pid: str, kind: str = "cas") -> dict:
        t = self.t
        j = self.partner(si)
        slots = []
        for p in range(self.n_q):
            f = t.by_pos[p].most_common(1)[0][0] if t.by_pos.get(p) else t.typical[-1]
            pts = self.points[p]
            slots.append({"slot": p + 1, **self.facet_card(f, si), **({"operation_mentale": self.op_card(self.op_by_pos[p])} if p in self.op_by_pos else {}),
                          "points": pts, "longueur_reponse_car": [self.cpp[0] * pts, self.cpp[2] * pts] if self.cpp else None,
                          "longueur_cible_car": self.cpp[1] * pts if self.cpp else None})
        return {"id": pid, "type": kind, "section": si, "section_titre": t.sections[si].title,
                "partenaire": j, "partenaire_titre": t.sections[j].title if j is not None else None,
                "frequence_passee": round(t.sec_freq.get(si, 0), 2), "inedit": t.sec_freq.get(si, 0) <= 0.05,
                "proba_annee_suivante": round(float(t.p_next[si]), 3),
                "questions": slots, "nb_annexes": int(np.median([len(t.qs[i[0]].annexes) for i in t.parts.values() if t.qs[i[0]].annexes])),
                "cours": self.course_of(si), "cours_partenaire": self.course_of(j) if j is not None else None,
                "documents_reels": self.bank_for(si) + (self.bank_for(j, 2) if j is not None else []),
                "anciens_sujets_proches": self.exemplar_parts(si)}

    def drills(self, si: int, pid: str, n: int = 4) -> dict:
        t = self.t
        kf = len(t.facets)
        marg = Counter(q.facet for q in t.Q)
        here = Counter(q.facet for q in t.Q if q.sec == si)
        p = np.array([(here[f] + 2 * marg[f] / len(t.Q)) / (sum(here.values()) + 2) for f in range(kf)])
        fs = [int(f) for f in np.argsort(-p)[:n]]
        return {"id": pid, "type": "exercices", "section": si, "section_titre": t.sections[si].title,
                "frequence_passee": round(t.sec_freq.get(si, 0), 2), "inedit": t.sec_freq.get(si, 0) <= 0.05,
                "questions": [{"slot": k + 1, **self.facet_card(f, si), "points": 2,
                               "longueur_reponse_car": [self.cpp[0] * 2, self.cpp[2] * 2] if self.cpp else None,
                               "longueur_cible_car": self.cpp[1] * 2 if self.cpp else None}
                              for k, f in enumerate(fs)],
                "cours": self.course_of(si), "documents_reels": self.bank_for(si, 2),
                "anciens_sujets_proches": self.exemplar_parts(si, 1)}

    def mocks(self, n: int, used: set[int] | None = None) -> list[dict]:
        t = self.t
        order = [int(s) for s in np.argsort(-t.p_next)]
        out, themes = [], set()
        for si in order:
            if len(out) == n:
                break
            th = t.sections[si].parent
            if th in themes:
                continue
            themes.add(th)
            out.append(self.cas(si, f"M{len(out) + 1}", kind="sujet_blanc"))
        return out

    def all(self, n_drill: int = 4, n_mock: int = 3) -> list[dict]:
        plans = []
        for si, s in enumerate(self.t.sections):
            num = s.num or str(si)
            plans.append(self.cas(si, f"C{num}"))
            plans.append(self.drills(si, f"E{num}", n_drill))
        plans += self.mocks(n_mock)
        return plans


def teacher_brief(t: Teacher) -> str:
    """Ce que le modèle a appris du professeur, en clair, pour l'agent rédacteur."""
    r = t.rep
    sq = r["squelette"]
    d = t.detail_stats
    fac = "\n".join(f"  - F{f['id']} « {f['nom']} » ({f['n']} questions, place moyenne {f['position_moyenne']}) ; ex. : {f['exemples'][0][:200]}"
                    for f in t.facets)
    sup = "\n".join(f"  - {s['nom']} ({s['n']}) ; titres réels : {' | '.join(x[:70] for x in s['exemples_de_titres'])}" for s in t.sup_facets)
    ops = "\n".join(f"  - O{o['id']} : fort en {', '.join(o['fort']) or '—'} ; faible en {', '.join(o['faible']) or '—'}" for o in t.ops)
    cons = "\n".join(f"  - « {c} »" for c in d["consignes_de_correction"][:10])
    return f"""PROFIL DU PROFESSEUR (appris par scikit-learn sur {r['corpus']['fichiers_sujets']} anciens sujets et {r['corpus']['corriges']} corrigés)

Squelette d'une partie : {dict(sq['questions_par_partie'])} questions par partie (le plus souvent {t.n_q.most_common(1)[0][0]}).
Ordre typique des manières de demander : {' → '.join(sq['squelette_typique'])}.
Verdict : {r['previsibilite_consigne']['verdict']} — la forme de la question dépend surtout de sa place dans le sujet.

Manières de demander découvertes :
{fac}

Types de documents en annexe :
{sup}
Annexes par sujet : {r['types_de_supports'].get('annexes_par_sujet')}.

Opérations mentales (ce que la question fait faire) :
{ops}

Niveau de détail attendu dans le corrigé : {d['chars_par_point_p10_p50_p90']} caractères par point (bas / médian / haut),
{d['articles_cites_par_reponse_moyenne']} article(s) cité(s) par réponse en moyenne.
Expressions typiques des corrigés : {', '.join(d['gestes_attendus_du_correcteur'][:20])}.
Ce que disent les corrigés au correcteur :
{cons}
"""


def write(t: Teacher, out: Path, batch: int = 5) -> list[dict]:
    pl = Planner(t)
    plans = pl.all()
    out.mkdir(parents=True, exist_ok=True)
    (out / "plans.json").write_text(json.dumps(plans, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    (out / "brief.txt").write_text(teacher_brief(t), encoding="utf-8")
    pd = out / "plans"
    pd.mkdir(exist_ok=True)
    for f in pd.glob("*.json"):
        f.unlink()
    for i in range(0, len(plans), batch):
        (pd / f"lot_{i // batch + 1:02d}.json").write_text(json.dumps(plans[i:i + batch], ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    return plans
