"""Validateur : les modèles appris jouent le rôle de correcteur (la « récompense » de la boucle
écrire → vérifier → réviser). Chaque question générée est notée sur :

  facette_ok    la manière de demander reconnue (top 2 du modèle de consignes) est celle du plan ;
  section_ok    l'alignement appris place la section visée (ou sa partenaire) dans le top 3 ;
  articles_ok   chaque article cité existe dans le cours ou dans les documents réels ;
  annexes_ok    une annexe qui ressemble à une source (article, arrêt) la recopie fidèlement ;
                une annexe inventée n'est admise que dans un type de support où le professeur
                invente aussi (extraits de contrat, règlement…), ce que mesure le taux de reprise
                des sources réelles par type de support, appris sur les anciens sujets ;
  nouveaute_ok  la situation n'est pas une ancienne situation (cosinus < 0,85) et l'énoncé n'est
                pas un ancien énoncé, sauf formule rituelle : énoncé ou début d'énoncé (trigramme des
                premiers mots) que le professeur repose dans au moins 10 % des sujets (min. 3), détecté
                sur le corpus ; la comparaison ignore noms propres, guillemets et nombres ;
  longueur_ok   la réponse attendue a la longueur par point des vrais corrigés (p10–p90, avec marge).

Chaque échec produit une consigne de révision en clair pour l'agent rédacteur.
"""
from __future__ import annotations

import difflib
import json
import re
from pathlib import Path

import numpy as np

from . import docs as D
from .profile import Teacher, art_ids


def _mask(t: str) -> str:
    """Énoncé sans ce qui change d'un cas à l'autre : noms propres, textes entre guillemets, nombres."""
    t = re.sub(r"«[^»]{0,80}»|\"[^\"]{0,80}\"", " ", t or "")
    w = t.split()
    return " ".join(x for i, x in enumerate(w) if not (i and x[:1].isupper()) and not re.search(r"\d", x))


def _n(t: str) -> str:
    return re.sub(r"\s+", " ", D.norm(t or "")).strip()


class Checker:
    def __init__(self, t: Teacher, plans: list[dict]):
        self.t = t
        self.plans = {p["id"]: p for p in plans}
        self.past = t.vec.transform([_mask(q.stem) for q in t.qs])
        # sources réelles : passages du cours + annexes des anciens sujets
        src = [(p, "cours") for p in t.pass_text]
        for idx in t.parts.values():
            for title, body in t.qs[idx[0]].annexes:
                if len(body) > 150:
                    src.append((body, "annexe"))
        self.src = [s for s, _ in src]
        self.src_n = [_n(s) for s in self.src]
        self.Src = t.vec.transform(self.src)
        # index global des 6-grammes des sources : une annexe qui cumule plusieurs articles
        # doit retrouver chacun de ses morceaux quelque part, pas forcément dans un seul passage
        self.src_sh = set().union(*(self._shingles(x) for x in self.src_n))
        self._rituals()
        self.known_ids = set().union(*t.sec_ids) | set().union(*(art_ids(s) for s in self.src)) | \
            set().union(*(art_ids(q.answer) for q in t.qs if q.answer))
        self._support_source_rate()

    def _rituals(self):
        """Formules rituelles : énoncés que le professeur repose quasi à l'identique dans plusieurs
        sujets. Les reprendre fait partie de sa manière de faire, ce n'est pas une copie."""
        t = self.t
        P = (self.past @ self.past.T).toarray()
        exams = np.array([q.exam for q in t.qs])
        n_ex = len(set(exams))
        need = max(3, int(0.1 * n_ex))
        # tête d'énoncé rituelle : un trigramme du début de la consigne présent dans >= need sujets
        by = {}
        for q in t.qs:
            for g in self._head(q.stem):
                by.setdefault(g, set()).add(q.exam)
        self.rit_heads = {g for g, e in by.items() if len(e) >= need}
        self.ritual = np.array([len(set(exams[P[i] > 0.7])) >= need or bool(self._head(t.qs[i].stem) & self.rit_heads)
                                for i in range(len(t.qs))])
        rit = sorted({t.qs[i].stem.strip() for i in np.where(self.ritual)[0]}, key=len)[:8]
        heads = sorted(self.rit_heads, key=lambda g: -len(by[g]))[:12]
        t.rep["formules_rituelles"] = {"seuil_sujets": need, "n_enonces": int(self.ritual.sum()), "exemples": rit,
                                       "tetes": [{"debut": " ".join(g), "sujets": len(by[g])} for g in heads]}
        # situations passées (une par partie) : le vrai garde-fou contre la copie
        sits = [_mask(t.qs[idx[0]].situation) for idx in t.parts.values() if len(t.qs[idx[0]].situation or "") > 80]
        self.past_sit = t.vec.transform(sits) if sits else None

    @staticmethod
    def _head(stem: str, n: int = 8) -> set:
        w = re.findall(r"\w+", _mask(stem).lower())[:n]
        return {tuple(w[i:i + 3]) for i in range(max(len(w) - 2, 0))}

    def _support_source_rate(self):
        """Pour chaque type de support : part des anciennes annexes qui sont la reprise d'une source
        (passage du cours ou annexe d'un autre sujet)."""
        t = self.t
        self.src_rate = {}
        if not getattr(t, "sup_facets", None):
            return
        lab = t.km_sup.predict(self._sup_Z(t.anx_titles))
        X = t.vec.transform([b for _, _, b in t.anx_owner])
        sims = (X @ self.Src.T).toarray()
        for i, (k, title, body) in enumerate(t.anx_owner):
            # on exclut la source identique (l'annexe elle-même)
            row = sims[i]
            row[row > 0.98] = 0
            sims[i] = row
        reused = sims.max(1) > 0.5
        dated = np.array([bool(re.search(r"\b(1[89]|20)\d\d\b", tt)) for _, tt, _ in t.anx_owner])
        self.dated_rate = {}
        for f in range(t.km_sup.n_clusters):
            m = lab == f
            self.src_rate[f] = float(reused[m].mean()) if m.any() else 0.0
            # un document daté (décision de justice) est un document réel : jamais inventé
            self.dated_rate[f] = float(dated[m].mean()) if m.any() else 0.0
        t.rep.setdefault("types_de_supports", {})["taux_de_reprise_de_sources"] = {
            t.sup_facets[f]["nom"]: round(v, 2) for f, v in self.src_rate.items()}
        t.rep["types_de_supports"]["part_de_documents_dates"] = {
            t.sup_facets[f]["nom"]: round(v, 2) for f, v in self.dated_rate.items()}

    def _sup_Z(self, titles):
        Z = self.t.tv_sup.transform(titles).toarray()
        return Z / (np.linalg.norm(Z, axis=1, keepdims=True) + 1e-9)

    def _sup_title(self, t: str) -> str:
        t2 = re.sub(r"(?i)^(annexe|document)\s*[a-z0-9]{0,3}\s*[-–:.]?\s*", "", t)
        t2 = re.sub(r"\d+", " ", t2)
        return D.norm(" ".join(w for w in t2.split() if not (w[:1].isupper() and len(w) > 1 and not w.isupper()) or w.lower() in ("code", "cour", "conseil")))

    @staticmethod
    def _shingles(t: str, k: int = 6) -> set:
        w = re.findall(r"\w+", t)
        return {" ".join(w[i:i + k]) for i in range(max(len(w) - k + 1, 1))}

    def faithful(self, text: str) -> tuple[float, float]:
        """(proximité TF-IDF à la source la plus proche, part des 6-grammes de mots du texte que l'on
        retrouve dans l'une des 3 sources les plus proches : 1 = recopie fidèle)."""
        x = self.t.vec.transform([text])
        s = (x @ self.Src.T).toarray().ravel()
        sh = self._shingles(_n(re.sub(r"\[…\]|\(\.\.\.\)|…", " ", text)))
        fid = len(sh & self.src_sh) / max(len(sh), 1)
        return float(s.max()), float(fid)

    def check_item(self, g: dict) -> dict:
        t = self.t
        plan = self.plans.get(g["id"], {})
        pslots = {q["slot"]: q for q in plan.get("questions", [])}
        targets = {plan.get("section"), plan.get("partenaire")} - {None}
        annexes = g.get("annexes") or []
        anx_text = " ".join(a.get("titre", "") + " " + a.get("texte", "") for a in annexes)
        res = {"id": g["id"], "questions": [], "annexes": [], "revision": []}
        # annexes
        for a in annexes:
            body = a.get("texte", "")
            sim, fid = self.faithful(body) if len(body) > 60 else (0.0, 1.0)
            sup = int(t.km_sup.predict(self._sup_Z([self._sup_title(a.get("titre", ""))]))[0]) if getattr(t, "km_sup", None) is not None else -1
            rate = self.src_rate.get(sup, 0.0)
            # source réelle : type que le professeur reprend tel quel (taux appris), document daté
            # (décision), ou annexe que le rédacteur déclare tirée du cours / des documents réels
            looks_source = rate > 0.5 or self.dated_rate.get(sup, 0) > 0.5 or a.get("source") in ("cours", "documents_reels")
            ok = (fid >= 0.8) if looks_source else True
            res["annexes"].append({"titre": a.get("titre", ""), "type_support": t.sup_facets[sup]["nom"] if sup >= 0 else None,
                                   "taux_reprise_du_type": round(rate, 2), "proximite_source": round(sim, 2),
                                   "fidelite": round(fid, 2), "ok": bool(ok)})
            if not ok:
                res["revision"].append(f"Annexe « {a.get('titre', '')[:60]} » : ce type de document est, chez ce professeur, une source réelle "
                                       f"recopiée (article de loi, arrêt). Recopie mot pour mot un texte fourni dans « cours » ou « documents_reels » "
                                       f"(fidélité mesurée {fid:.0%}).")
        qs = g.get("questions", [])
        stems = [q.get("enonce", "") for q in qs]
        F = t.facet_of(stems) if stems else np.zeros((0, len(t.facets)))
        for k, q in enumerate(qs):
            ps = pslots.get(q.get("slot"), {})
            stem, ans = q.get("enonce", ""), q.get("reponse_attendue", "")
            situation = q.get("situation") or g.get("situation", "")
            r = {"slot": q.get("slot"), "facette_visee": ps.get("facette")}
            top2 = [int(x) for x in np.argsort(-F[k])[:2]]
            r["facette_lue"] = top2[0]
            r["facette_ok"] = ps.get("facette") in top2 if ps else None
            w = t.w
            S = (t.sec_scores([stem])[0] + w[0] * t.sec_scores([ans or stem])[0] + w[1] * t.sec_scores([anx_text[:8000]])[0]
                 + w[2] * t.sec_scores([situation[:3000]])[0] + w[3] * t.id_bonus([stem + " " + ans + " " + anx_text])[0])
            top3 = [int(x) for x in np.argsort(-S)[:3]]
            r["section_top3"] = [t.sections[x].num for x in top3]
            r["section_ok"] = bool(targets & set(top3)) if targets else None
            cited = {re.sub(r"[.\s]", "", str(c)).upper() for c in q.get("articles_cites", [])} | art_ids(ans)
            cited = {re.sub(r"^ARTICLES?", "", c) for c in cited}
            unknown = sorted(c for c in cited if c and c not in self.known_ids and c not in art_ids(anx_text))
            r["articles_inconnus"] = unknown
            r["articles_ok"] = not unknown
            sims = (t.vec.transform([_mask(stem)]) @ self.past.T).toarray().ravel() if stem else np.zeros(1)
            nov = float(sims.max())
            r["nouveaute_sim_max"] = round(nov, 3)
            r["formule_rituelle"] = bool(nov >= 0.85 and (self.ritual[int(sims.argmax())] or bool(self._head(stem) & self.rit_heads)))
            ss = float((t.vec.transform([_mask(situation)]) @ self.past_sit.T).max()) if self.past_sit is not None and len(situation) > 80 else 0.0
            r["situation_sim_max"] = round(ss, 3)
            r["nouveaute_ok"] = (nov < 0.85 or r["formule_rituelle"]) and ss < 0.85
            pts = q.get("points") or ps.get("points") or 1
            cpp = t.detail_stats["chars_par_point_p10_p50_p90"]
            L = len(ans)
            r["longueur_ok"] = (0.6 * cpp[0] * pts <= L <= 1.4 * cpp[2] * pts) if cpp else None
            r["car_par_point"] = round(L / pts)
            res["questions"].append(r)
            fb = []
            if r["facette_ok"] is False:
                fc = t.facets[ps["facette"]]
                fb.append(f"la manière de demander n'est pas reconnue comme « {fc['nom']} » ; reprends la tournure de : « {fc['exemples'][0][:160]} »")
            if r["section_ok"] is False:
                fb.append(f"la question ne porte pas assez sur « {plan.get('section_titre')} » (lue comme {r['section_top3']}) : ancre-la dans les notions et articles de cette section")
            if unknown:
                fb.append(f"articles non vérifiables {unknown} : n'utilise que les articles fournis")
            if not r["nouveaute_ok"]:
                fb.append("énoncé trop proche d'un ancien sujet : change la situation et la tournure")
            if r["longueur_ok"] is False:
                fb.append(f"réponse attendue de {L} caractères pour {pts} point(s) ; le professeur attend {cpp[0] * pts}–{cpp[2] * pts}")
            if fb:
                res["revision"].append(f"Question {q.get('slot')} : " + " ; ".join(fb))
        return res


def summarize(results: list[dict]) -> dict:
    qs = [q for r in results for q in r["questions"]]
    an = [a for r in results for a in r["annexes"]]
    keys = ["facette_ok", "section_ok", "articles_ok", "nouveaute_ok", "longueur_ok"]
    out = {k: round(float(np.mean([q[k] for q in qs if q.get(k) is not None])), 3) if qs else None for k in keys}
    out["annexes_ok"] = round(float(np.mean([a["ok"] for a in an])), 3) if an else None
    out["tout_ok"] = round(float(np.mean([all(q.get(k) is not False for k in keys) for q in qs])), 3) if qs else None
    out["questions"] = len(qs)
    out["annexes"] = len(an)
    out["lots"] = len(results)
    return out


def run(t: Teacher, plans: list[dict], gen_dir: Path, out: Path) -> dict:
    ck = Checker(t, plans)
    results = []
    for f in sorted(gen_dir.glob("*.json")):
        try:
            g = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            results.append({"id": f.stem, "questions": [], "annexes": [], "revision": [f"JSON invalide : {e}"]})
            continue
        results.append(ck.check_item(g))
    s = summarize(results)
    out.write_text(json.dumps({"resume": s, "detail": results}, ensure_ascii=False, indent=1), encoding="utf-8")
    return s
