"""Profil du professeur : ce que scikit-learn apprend des anciens sujets (et de leurs corrigés)
sur la façon de penser de celui qui les a écrits, sans variable écrite à la main.

Étapes (toutes apprises sur les données, avec auto-correction quand une vérité terrain existe) :
  1. pertinence des parties : un mélange gaussien sur la proximité au cours écarte les parties
     hors cours (ex. la partie économie d'un sujet « droit et économie ») ;
  2. alignement question -> section du cours : poids des signaux (énoncé, corrigé, annexes,
     identifiants de référence communs, appris sur le cours) réglés sur les « références au programme »
     des corrigés, avec un score honnête en validation croisée par sujet ;
  3. variables découvertes :
     - manières de demander (vocabulaire de consigne séparé du contenu par un mélange gaussien,
       puis facettes KMeans stables par bootstrap) ;
     - types de supports (titres d'annexes groupés) ;
     - opérations mentales (descripteurs relationnels : usage du cas, du cours, des documents,
       place dans le sujet, forme de la question… groupés par mélange gaussien choisi au BIC) ;
     - niveau de détail attendu (longueur et structure des corrigés par point de barème) ;
     - gestes attendus du correcteur (expressions sur-représentées dans les corrigés par rapport au
       cours : log-odds à prior de Dirichlet) ;
     - squelette d'un sujet (facette par rang, transitions, barème par rang) ;
     - couverture du cours, associations de sections, tendance par année ;
  4. tests prédictifs (le professeur est-il prévisible, et sur quoi ?) :
     - la manière de demander dépend-elle du rang (rituel) ou du contenu ? log-loss par sujet exclu ;
     - quelles sections tombent : année exclue, modèle appris vs simple popularité (AUC).
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

from ..discovery import stable_kmeans
from . import docs as D

SEED = 7
WORD = re.compile(r"[a-z]{3,}")
IDTOK = r"(?:[A-Z]\.?\s?)?\d+(?:[-‑.]\d+)*"


class RefModel:
    """Identifiants de référence appris sur le cours (aucune règle de matière) : un mot
    « introducteur » est un mot qui, dans le cours, précède souvent un identifiant numérique, avec
    des identifiants variés et chacun propre à peu de sections (ex. « article 1240 » en droit). Les
    années, quantités ou numéros de page ne passent pas ce filtre."""

    def __init__(self, sections):
        pairs = []
        for si, s in enumerate(sections):
            for m in re.finditer(r"(\w{3,})\.?\s+(" + IDTOK + ")", " ".join(s.passages)):
                pairs.append((self._k(m.group(1)), self._id(m.group(2)), si))
        occ = Counter(self._k(w) for s in sections for w in re.findall(r"\w{3,}", " ".join(s.passages)))
        by = defaultdict(list)
        for w, i, si in pairs:
            by[w].append((i, si))
        self.intro = set()
        self.stats = {}
        for w, v in by.items():
            ids = [i for i, _ in v]
            if len(v) < 5 or w.isdigit():
                continue
            secs_per_id = defaultdict(set)
            for i, si in v:
                secs_per_id[i].add(si)
            div = len(set(ids)) / len(ids)
            spec = float(np.mean([len(x) <= 3 for x in secs_per_id.values()]))
            year = float(np.mean([bool(re.fullmatch(r"(19|20)\d\d", i)) for i in ids]))
            follow = len(v) / max(occ[w], 1)
            longid = float(np.median([len(re.sub(r"\D", "", i)) for i in ids]))
            if div >= 0.4 and spec >= 0.8 and year < 0.5 and follow >= 0.3 and longid >= 3:
                self.intro.add(w)
                self.stats[w] = {"n": len(v), "diversite": round(div, 2), "taux_suivi": round(follow, 2)}

    @staticmethod
    def _k(w):
        w = D.norm(w)
        return w[:-1] if w.endswith("s") and len(w) > 4 else w

    @staticmethod
    def _id(x):
        return re.sub(r"[.\s‑]", "", x).replace("‑", "-").upper()

    def __call__(self, text: str) -> set[str]:
        out = set()
        if not self.intro:
            return out
        for m in re.finditer(r"(\w{3,})\.?\s+((?:" + IDTOK + r")(?:\s*(?:,|et|and|ou|or|/)\s*(?:" + IDTOK + r"))*)", text):
            if self._k(m.group(1)) in self.intro:
                for n in re.findall(IDTOK, m.group(2)):
                    out.add(self._id(n))
        return out

    def starts_with_ref(self, passage: str) -> bool:
        return bool(self(passage[:60]))


DEFAULT_CFG = {"analyzer": "word", "ngram": (1, 2), "a": 0.5}


class Teacher:
    def __init__(self, sujets_dir: Path, cours_dir: Path, cfg: dict | None = None):
        self.rep: dict = {}
        self.cfg = dict(DEFAULT_CFG, **(cfg or {}))
        self.sections = D.parse_course([p for p in Path(cours_dir).rglob("*") if p.suffix.lower() in (".md", ".txt", ".pdf")])
        self.qs: list[D.Question] = []
        self.refs: dict[str, list[str]] = {}
        self.grading: dict[str, str] = {}
        pairs = D.pair_files(Path(sujets_dir))
        self.n_files = len(pairs)
        raw_corr = {}
        for key, s, c in pairs:
            qs = D.parse_exam(D.read_text(s), key)
            self.qs += qs
            if c:
                raw_corr[key] = D.read_text(c)
        self.ref_ids = RefModel(self.sections)
        self._fit_vectorizer()
        sim = lambda a, b: float((self.vec.transform([a]) @ self.vec.transform([b]).T).toarray()[0, 0])
        for key, txt in raw_corr.items():
            idx = [i for i, q in enumerate(self.qs) if q.exam == key]
            res = D.parse_correction(txt, [self.qs[i] for i in idx], sim)
            for j, v in res.items():
                q = self.qs[idx[j]]
                q.answer = v["answer"]
                q.points = q.points or v["points"]
            self.refs[key] = D.course_refs(txt, self.sections)
            self.grading[key] = txt
        self.rep["corpus"] = {"fichiers_sujets": self.n_files, "corriges": len(raw_corr),
                              "questions_lues": len(self.qs), "sections_du_cours": len(self.sections),
                              "passages_du_cours": sum(len(s.passages) for s in self.sections)}

    # ------------------------------------------------------------------ représentations
    def _fit_vectorizer(self):
        self.pass_text, self.pass_sec = [], []
        for si, s in enumerate(self.sections):
            for p in s.passages:
                self.pass_text.append(p)
                self.pass_sec.append(si)
        self.pass_sec = np.array(self.pass_sec)
        qdocs = [q.stem + " " + q.situation[:1500] for q in self.qs]
        c = self.cfg
        kw = dict(analyzer="char_wb", ngram_range=(3, 5)) if c["analyzer"] == "char_wb" else dict(ngram_range=tuple(c["ngram"]))
        self.vec = TfidfVectorizer(sublinear_tf=True, strip_accents="unicode", min_df=2, max_df=0.5, **kw).fit(self.pass_text + qdocs)
        self.P = self.vec.transform(self.pass_text)
        sec_docs = [" ".join(s.passages) + " " + s.title * 3 for s in self.sections]
        self.C = self.vec.transform(sec_docs)
        self.sec_ids = [self.ref_ids(" ".join(s.passages)) for s in self.sections]

    def sec_scores(self, texts: list[str], a: float | None = None) -> np.ndarray:
        a = self.cfg["a"] if a is None else a
        X = self.vec.transform(texts)
        cen = (X @ self.C.T).toarray()
        pas = (X @ self.P.T).toarray()
        pmax = np.zeros_like(cen)
        for si in range(len(self.sections)):
            m = self.pass_sec == si
            if m.any():
                pmax[:, si] = pas[:, m].max(1)
        return a * cen + (1 - a) * pmax

    def id_bonus(self, texts: list[str]) -> np.ndarray:
        B = np.zeros((len(texts), len(self.sections)))
        for i, t in enumerate(texts):
            ids = self.ref_ids(t)
            if ids:
                for si, sid in enumerate(self.sec_ids):
                    B[i, si] = len(ids & sid) / len(ids)
        return B

    # ------------------------------------------------------------------ 1. pertinence
    def relevant_parts(self):
        parts = defaultdict(list)
        for i, q in enumerate(self.qs):
            parts[(q.exam, q.part)].append(i)
        keys = list(parts)
        first = [self.qs[parts[k][0]] for k in keys]
        sig = np.c_[self.sec_scores([" ".join(self.qs[i].stem for i in parts[k]) for k in keys]).max(1),
                    self.sec_scores([" ".join(x for _, x in q.annexes)[:8000] or q.situation[:3000] for q in first]).max(1),
                    self.sec_scores([q.situation[:3000] for q in first]).max(1)]
        z = StandardScaler().fit_transform(np.log(sig + 1e-3))
        g1 = GaussianMixture(1, covariance_type="diag", random_state=SEED).fit(z)
        g2 = GaussianMixture(2, covariance_type="diag", random_state=SEED, n_init=8).fit(z)
        keep = np.ones(len(keys), bool)
        if g2.bic(z) < g1.bic(z):
            hi = int(np.argmax(g2.means_.sum(1)))
            keep = g2.predict(z) == hi
            # lissage par titre de partie (même mise en page d'un sujet à l'autre) : vote majoritaire
            tkey = lambda k: re.sub(r"\s*/\s*sujet\s*\d+", "", D.norm(k[1]))
            vote = defaultdict(list)
            for k, ok in zip(keys, keep):
                vote[tkey(k)].append(ok)
            keep = np.array([np.mean(vote[tkey(k)]) > 0.5 if len(vote[tkey(k)]) >= 3 else ok for k, ok in zip(keys, keep)])
        self.keep_idx = [i for k, ok in zip(keys, keep) if ok for i in parts[k]]
        self.parts = {k: parts[k] for k, ok in zip(keys, keep) if ok}
        dropped = Counter(k[1] for k, ok in zip(keys, keep) if not ok)
        kept = Counter(k[1] for k, ok in zip(keys, keep) if ok)
        self.rep["pertinence_des_parties"] = {
            "methode": "mélange gaussien (choisi au BIC) sur la proximité maximale de chaque partie au cours",
            "parties_gardees": len(self.parts), "parties_ecartees": int((~keep).sum()),
            "signaux": "proximité au cours des énoncés, des annexes, de la situation ; puis vote par titre de partie",
            "titres_gardes": dict(kept.most_common(6)), "titres_ecartes": dict(dropped.most_common(6)),
            "questions_gardees": len(self.keep_idx)}
        print(f"  parties : {len(self.parts)} gardées, {(~keep).sum()} écartées ({dict(dropped.most_common(3))})")

    # ------------------------------------------------------------------ 2. alignement
    def align(self):
        Q = [self.qs[i] for i in self.keep_idx]
        S_stem = self.sec_scores([q.stem + " " + q.preamble for q in Q])
        S_ans = self.sec_scores([q.answer or q.stem for q in Q])
        anx = [" ".join(t + " " + x for t, x in q.annexes)[:8000] for q in Q]
        S_anx = self.sec_scores(anx)
        S_sit = self.sec_scores([q.situation[:3000] for q in Q])
        B = self.id_bonus([q.stem + " " + q.answer + " " + a for q, a in zip(Q, anx)])
        has_ans = np.array([bool(q.answer) for q in Q])
        labelled = [i for i, q in enumerate(Q) if self.refs.get(q.exam)]
        exams = sorted({Q[i].exam for i in labelled})

        def combo(w):
            S = S_stem + w[0] * np.where(has_ans[:, None], S_ans, 0) + w[1] * S_anx + w[2] * S_sit + w[3] * B
            return S

        def score(S, idx):
            h1 = h3 = 0
            for i in idx:
                r = {int(x[1:]) for x in self.refs[Q[i].exam]}
                top = np.argsort(-S[i])[:3]
                h1 += top[0] in r
                h3 += bool(r & set(top))
            return h1 / max(len(idx), 1), h3 / max(len(idx), 1)

        grid = [(a, b, c, d) for a in (0, 0.5, 1, 2) for b in (0, 0.25, 0.5, 1) for c in (0, 0.25, 0.5)
                for d in (0, 0.5, 1, 2)]
        base = score(combo((0, 0, 0, 0)), labelled)
        # validation croisée par sujet : les poids sont choisis sans voir le sujet évalué
        loo1 = loo3 = n = 0
        for e in exams:
            tr = [i for i in labelled if Q[i].exam != e]
            te = [i for i in labelled if Q[i].exam == e]
            w = max(grid, key=lambda w: score(combo(w), tr))
            s1, s3 = score(combo(w), te)
            loo1 += s1 * len(te); loo3 += s3 * len(te); n += len(te)
        self.w = max(grid, key=lambda w: score(combo(w), labelled))
        S = combo(self.w)
        # popularité : la section la plus citée par les autres corrigés
        pop = Counter(x for e in exams for x in self.refs[e])
        pop_h = np.mean([int(pop.most_common(1)[0][0][1:]) in {int(x[1:]) for x in self.refs[Q[i].exam]} for i in labelled]) if labelled else 0
        self.S = S
        self.Q = Q
        self.top = np.argsort(-S, 1)
        for q, row in zip(Q, self.top):
            q.sec = int(row[0])
        self.rep["alignement_sur_le_cours"] = {
            "verite_terrain": "« références au programme » lues dans les corrigés",
            "sujets_avec_references": len(exams), "questions_evaluees": len(labelled),
            "poids_appris": dict(zip(["corrige", "annexes", "situation", "identifiants_communs"], self.w)),
            "enonce_seul_top1_top3": [round(x, 3) for x in base],
            "appris_validation_croisee_top1_top3": [round(loo1 / max(n, 1), 3), round(loo3 / max(n, 1), 3)],
            "popularite_top1": round(float(pop_h), 3),
            "hasard_top1": round(float(np.mean([len(self.refs[Q[i].exam]) for i in labelled]) / len(self.sections)), 3) if labelled else 0}
        print(f"  alignement : énoncé seul {base[0]:.2f}/{base[1]:.2f} -> appris (VC) {loo1 / max(n, 1):.2f}/{loo3 / max(n, 1):.2f}"
              f" ; popularité {pop_h:.2f} ; poids {self.w}")

    # ------------------------------------------------------------------ 3a. consignes
    def consigne_vocab(self):
        Q = self.Q
        occ, exams_w, secs_w, sit_w = Counter(), defaultdict(set), defaultdict(Counter), Counter()
        for q in Q:
            sit = set(WORD.findall(D.norm(q.situation)))
            for w in set(WORD.findall(D.norm(q.stem))):
                occ[w] += 1
                exams_w[w].add(q.exam)
                secs_w[w][q.sec] += 1
                sit_w[w] += w in sit
        course = Counter(WORD.findall(D.norm(" ".join(self.pass_text))))
        ntok_c = sum(course.values())
        ntok_q = sum(len(WORD.findall(D.norm(q.stem))) for q in Q)
        words = sorted(w for w in occ if occ[w] >= 3)
        feats = []
        for w in words:
            p = np.array(list(secs_w[w].values()), float); p /= p.sum()
            ent = -(p * np.log(p)).sum() / math.log(len(self.sections))
            situ = sit_w[w] / occ[w]
            ratio = math.log((course[w] + 1) / ntok_c) - math.log(occ[w] / ntok_q)
            feats.append([ent, situ, ratio])
        Z = StandardScaler().fit_transform(np.array(feats))
        gm = GaussianMixture(2, covariance_type="full", random_state=SEED, n_init=5).fit(Z)
        sc = gm.means_[:, 0] - gm.means_[:, 1] - gm.means_[:, 2]
        st = int(np.argmax(sc))
        keep = gm.predict_proba(Z)[:, st] > 0.5
        self.style_words = {w for w, k in zip(words, keep) if k}
        order = np.argsort(-(Z[:, 0] - Z[:, 1] - Z[:, 2]))
        self.rep["vocabulaire_de_consigne"] = {
            "signaux": "dispersion sur les sections, présence dans le cas, rareté dans le cours ; mélange gaussien",
            "mots_analyses": len(words), "mots_de_consigne": int(keep.sum()),
            "exemples_consigne": [words[i] for i in order if keep[i]][:40],
            "exemples_contenu": [words[i] for i in order[::-1] if not keep[i]][:25]}
        print(f"  consigne : {keep.sum()} mots rituels / {len(words)}")

    def style_text(self, stem: str) -> str:
        out = []
        for t in re.findall(r"\w+|[?:]", D.norm(stem))[:45]:
            if t in self.style_words:
                out.append(t)
            elif t == "?":
                out.append("QM")
            elif t == ":":
                out.append("COLON")
            elif not out or out[-1] != "X":
                out.append("X")
        return " ".join(out)

    def consigne_facets(self):
        st = [self.style_text(q.stem) for q in self.Q]
        self.cv = TfidfVectorizer(ngram_range=(1, 3), min_df=2, token_pattern=r"\S+").fit(st)
        Z = self.cv.transform(st).toarray()
        Z = Z / (np.linalg.norm(Z, axis=1, keepdims=True) + 1e-9)
        km, stab, rep = stable_kmeans(Z, range(3, 10), seed=SEED, n_boot=8, min_stab=0.6, label="manières de demander")
        self.km_c = km
        lab = km.predict(Z)
        for q, l in zip(self.Q, lab):
            q.facet = int(l)
        names = self.cv.get_feature_names_out()
        fac = []
        for f in range(km.n_clusters):
            idx = [i for i, l in enumerate(lab) if l == f]
            cen = km.cluster_centers_[f]
            top = [names[j] for j in np.argsort(-cen)[:6] if " " in names[j] or names[j] not in ("x",)][:4]
            ex = sorted(idx, key=lambda i: -float(Z[i] @ cen))[:4]
            fac.append({"id": f, "nom": " / ".join(top), "n": len(idx), "stabilite": round(float(stab[f]), 2),
                        "position_moyenne": round(float(np.mean([self.Q[i].position / max(self.Q[i].n_in_part - 1, 1) for i in idx])), 2),
                        "exemples": [self.Q[i].stem[:240] for i in ex]})
        self.facets = fac
        self.rep["manieres_de_demander"] = {"k": km.n_clusters, **rep, "facettes": fac}

    def facet_of(self, stems: list[str]) -> np.ndarray:
        Z = self.cv.transform([self.style_text(s) for s in stems]).toarray()
        Z = Z / (np.linalg.norm(Z, axis=1, keepdims=True) + 1e-9)
        return -((Z[:, None, :] - self.km_c.cluster_centers_[None]) ** 2).sum(-1)  # plus grand = plus proche

    # ------------------------------------------------------------------ 3b. supports
    def supports(self):
        titles, owner = [], []
        for k, idx in self.parts.items():
            for t, body in self.qs[idx[0]].annexes:
                t2 = re.sub(r"(?i)^(annexe|document)\s*[a-z0-9]{0,3}\s*[-–:.]?\s*", "", t)
                t2 = re.sub(r"\d+", " ", t2)
                t2 = " ".join(w for w in t2.split() if not (w[:1].isupper() and len(w) > 1 and not w.isupper()) or w.lower() in ("code", "cour", "conseil"))
                if len(t2) > 3:
                    titles.append(D.norm(t2))
                    owner.append((k, t, body))
        self.anx_titles, self.anx_owner = titles, owner
        if len(titles) < 10:
            self.sup_facets = []
            return
        tv = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), min_df=2, sublinear_tf=True).fit(titles)
        Z = tv.transform(titles).toarray()
        Z /= np.linalg.norm(Z, axis=1, keepdims=True) + 1e-9
        km, stab, rep = stable_kmeans(Z, range(3, 10), seed=SEED, n_boot=8, label="types de supports")
        lab = km.labels_ if len(km.labels_) == len(Z) else km.predict(Z)
        out = []
        for f in range(km.n_clusters):
            idx = [i for i, l in enumerate(lab) if l == f]
            common = Counter(w for i in idx for w in set(WORD.findall(titles[i])))
            ex = Counter(owner[i][1] for i in idx).most_common(3)
            lens = [len(owner[i][2]) for i in idx]
            out.append({"id": f, "nom": " ".join(w for w, _ in common.most_common(4)), "n": len(idx),
                        "stabilite": round(float(stab[f]), 2), "exemples_de_titres": [e for e, _ in ex],
                        "longueur_mediane": int(np.median(lens)) if lens else 0,
                        "exemple_texte": owner[idx[0]][2][:500] if idx else ""})
        self.sup_facets = out
        self.tv_sup, self.km_sup = tv, km
        per_part = Counter(len(self.qs[idx[0]].annexes) for idx in self.parts.values())
        self.rep["types_de_supports"] = {"k": km.n_clusters, **rep, "annexes_par_sujet": dict(sorted(per_part.items())),
                                         "types": out}

    # ------------------------------------------------------------------ 3c. opérations mentales
    def operations(self):
        Q = self.Q
        stems = [q.stem for q in Q]
        X = self.vec.transform(stems)
        sit = self.vec.transform([q.situation[:3000] for q in Q])
        anx = self.vec.transform([" ".join(x for _, x in q.annexes)[:8000] for q in Q])
        f_scen = np.asarray(X.multiply(sit).sum(1)).ravel()
        f_anx = np.asarray(X.multiply(anx).sum(1)).ravel()
        Ss = self.sec_scores(stems)
        f_course = Ss.max(1)
        f_breadth = (Ss > 0.6 * Ss.max(1, keepdims=True)).sum(1)
        f_pos = np.array([q.position / max(q.n_in_part - 1, 1) for q in Q])
        f_q = np.array([q.stem.rstrip().endswith("?") for q in Q], float)
        f_actor = np.array([sum(1 for w in re.findall(r"\b[A-ZÉ][a-zé]+|\b[A-Z]{2,}\b", q.stem[1:]) if w in q.situation) for q in Q], float)
        f_len = np.log1p([len(q.stem) for q in Q])
        F = np.c_[f_scen, f_anx, f_course, f_breadth, f_pos, f_q, f_actor, f_len]
        names = ["appui_sur_le_cas", "appui_sur_les_documents", "appui_sur_le_cours", "largeur_du_cours",
                 "rang_dans_le_sujet", "forme_interrogative", "acteurs_nommes", "longueur_enonce"]
        Z = StandardScaler().fit_transform(F)
        best = min(range(2, 7), key=lambda k: GaussianMixture(k, random_state=SEED, n_init=4).fit(Z).bic(Z))
        gm = GaussianMixture(best, random_state=SEED, n_init=6).fit(Z)
        lab = gm.predict(Z)
        ops = []
        for k in range(best):
            idx = np.where(lab == k)[0]
            mu = Z[idx].mean(0)
            hi = [names[j] for j in np.argsort(-mu)[:3] if mu[j] > 0.3]
            lo = [names[j] for j in np.argsort(mu)[:2] if mu[j] < -0.3]
            ex = sorted(idx, key=lambda i: -gm.predict_proba(Z[i:i + 1])[0, k])[:3]
            ops.append({"id": k, "n": int(len(idx)), "fort": hi, "faible": lo,
                        "profil": {n: round(float(m), 2) for n, m in zip(names, mu)},
                        "exemples": [Q[i].stem[:220] for i in ex]})
        for q, l in zip(Q, lab):
            q.op = int(l)
        self.ops = ops
        self.rep["operations_mentales"] = {"methode": "8 descripteurs relationnels, mélange gaussien, k au BIC",
                                           "k": best, "operations": ops}
        print(f"  opérations mentales : k={best}")

    # ------------------------------------------------------------------ 3d. niveau de détail
    def detail(self):
        A = [q for q in self.Q if q.answer]
        rows = []
        for q in A:
            pts = q.points or np.nan
            rows.append({"chars": len(q.answer), "pts": pts, "items": len(re.findall(r"(?m)^\s*([-•▪✓]|\d+[.)])\s", q.answer)),
                         "articles": len(self.ref_ids(q.answer)), "facet": q.facet, "pos": q.position})
        ch = np.array([r["chars"] for r in rows], float)
        pp = np.array([r["pts"] for r in rows], float)
        cpp = ch[~np.isnan(pp)] / pp[~np.isnan(pp)]
        by_f = defaultdict(list)
        for r in rows:
            by_f[r["facet"]].append(r["chars"])
        # gestes attendus : expressions sur-représentées dans les corrigés (log-odds, prior de Dirichlet).
        # Deux contrastes : contre le cours (ce n'est pas du savoir brut) et contre les énoncés/situations
        # des sujets (ce n'est pas le registre de la prose ordinaire) ; on garde le plus petit des deux z.
        ans = [q.answer for q in A]
        prose = sorted({q.situation for q in self.Q if q.situation}) + [q.stem for q in self.Q]
        cv = CountVectorizer(ngram_range=(1, 3), strip_accents="unicode", min_df=3, token_pattern=r"(?u)\b\w\w+\b")
        cv.fit(ans + self.pass_text + prose)

        def z_of(a, c, k=500):
            prior = (a + c) / (a + c).sum() * k
            la = np.log((a + prior) / (a.sum() + prior.sum() - a - prior))
            lc = np.log((c + prior) / (c.sum() + prior.sum() - c - prior))
            return (la - lc) / np.sqrt(1 / (a + prior) + 1 / (c + prior))
        # troisième contraste : le méta-texte des corrigés (en-têtes, barème, consignes au correcteur)
        meta = []
        for t in self.grading.values():
            for x in ans:
                t = t.replace(x[:3000], " ")
            meta.append(t)
        Xa = cv.transform(ans)
        a = np.asarray(Xa.sum(0)).ravel()
        z = np.minimum.reduce([z_of(a, np.asarray(cv.transform(ref).sum(0)).ravel())
                               for ref in (self.pass_text, prose, meta)])
        df_a = np.asarray((Xa > 0).sum(0)).ravel() / max(len(ans), 1)
        voc = cv.get_feature_names_out()
        cand = [i for i in np.argsort(-z) if z[i] > 2 and a[i] >= 4 and df_a[i] < 0.5 and not re.search(r"\d", voc[i])]
        marks = []
        for i in cand:  # pas de doublon d'un n-gramme déjà retenu
            if not any(voc[i] in m or m in voc[i] for m in marks):
                marks.append(voc[i])
            if len(marks) == 30:
                break
        # consignes de correction : phrases des corrigés qui disent ce qui est attendu
        att = Counter()
        for t in self.grading.values():
            for s in re.split(r"(?<=[.!])\s+", re.sub(r"\s+", " ", t)):
                if re.search(r"(?i)attendu|valoris|on accept|ne sera pas exig|doit (?:être|faire)|il convient", s) and 30 < len(s) < 260:
                    att[s.strip()] += 1
        self.detail_stats = {"chars_par_point_p10_p50_p90": [int(x) for x in np.percentile(cpp, [10, 50, 90])] if len(cpp) else [],
                             "chars_par_question_p50": int(np.median(ch)) if len(ch) else 0,
                             "references_citees_par_reponse_moyenne": round(float(np.mean([r["articles"] for r in rows])), 2) if rows else 0,
                             "enumerations_par_reponse_moyenne": round(float(np.mean([r["items"] for r in rows])), 2) if rows else 0,
                             "longueur_mediane_par_facette": {str(f): int(np.median(v)) for f, v in sorted(by_f.items())},
                             "points_par_rang": self._points_by_rank(),
                             "gestes_attendus_du_correcteur": marks,
                             "consignes_de_correction": [s for s, _ in att.most_common(14)]}
        self.rep["niveau_de_detail"] = {"reponses_de_corrige": len(A), **self.detail_stats}
        print(f"  détail : {len(A)} réponses, {self.detail_stats['chars_par_point_p10_p50_p90']} car./point ; gestes {marks[:8]}")

    def _points_by_rank(self):
        d = defaultdict(list)
        for q in self.Q:
            if q.points:
                d[q.position].append(q.points / max(sum((x.points or 0) for x in self.Q if x.exam == q.exam and x.part == q.part), 1))
        return {str(k): round(float(np.median(v)), 3) for k, v in sorted(d.items()) if len(v) >= 3}

    # ------------------------------------------------------------------ 3e. squelette, couverture
    def skeleton(self):
        seqs = defaultdict(list)
        for q in self.Q:
            seqs[(q.exam, q.part)].append((q.position, q.facet, q.op))
        trans, by_pos, n_q = Counter(), defaultdict(Counter), Counter()
        for s in seqs.values():
            s.sort()
            n_q[len(s)] += 1
            prev = "début"
            for p, f, _ in s:
                by_pos[p][f] += 1
                trans[(prev, f)] += 1
                prev = f
            trans[(prev, "fin")] += 1
        self.by_pos = by_pos
        self.n_q = n_q
        typical = [by_pos[p].most_common(1)[0][0] for p in sorted(by_pos) if sum(by_pos[p].values()) >= 0.5 * len(seqs)]
        self.typical = typical
        self.rep["squelette"] = {"questions_par_partie": dict(sorted(n_q.items())),
                                 "facette_par_rang": {str(p): dict(c.most_common()) for p, c in sorted(by_pos.items())},
                                 "squelette_typique": [self.facets[f]["nom"] for f in typical],
                                 "transitions": {f"{a}->{b}": n for (a, b), n in trans.most_common(14)}}

    def coverage(self):
        ex_secs = defaultdict(set)
        for q in self.Q:
            ex_secs[q.exam].add(q.sec)
        for e, r in self.refs.items():
            if r and e in ex_secs:
                ex_secs[e] |= {int(x[1:]) for x in r}  # vérité terrain quand elle existe
        self.ex_secs = ex_secs
        cnt = Counter(s for v in ex_secs.values() for s in v)
        co = Counter()
        for v in ex_secs.values():
            for a in v:
                for b in v:
                    if a < b:
                        co[(a, b)] += 1
        self.co = co
        years = defaultdict(Counter)
        yr = {q.exam: q.year for q in self.Q}
        for e, v in ex_secs.items():
            for s in v:
                years[s][yr.get(e)] += 1
        n_ex = len(ex_secs)
        self.sec_freq = {si: cnt.get(si, 0) / n_ex for si in range(len(self.sections))}
        self.rep["couverture_du_cours"] = {
            "sujets": n_ex,
            "frequence_par_section": {self.sections[s].title: round(cnt.get(s, 0) / n_ex, 2) for s in range(len(self.sections))},
            "jamais_ou_presque": [self.sections[s].title for s in range(len(self.sections)) if cnt.get(s, 0) <= 1],
            "associations_frequentes": [f"{self.sections[a].title[:40]} + {self.sections[b].title[:40]} ({n})" for (a, b), n in co.most_common(10)]}

    # ------------------------------------------------------------------ 4. prévisibilité
    def predictability(self):
        """La manière de demander s'explique-t-elle par le rang (rituel) ou par la section (contenu) ?"""
        Q = self.Q
        kf = len(self.facets)
        exams = sorted({q.exam for q in Q})

        def ll(cond):
            tot = n = 0
            for e in exams:
                tr = [q for q in Q if q.exam != e]
                te = [q for q in Q if q.exam == e]
                cnt = defaultdict(Counter)
                for q in tr:
                    cnt[cond(q)][q.facet] += 1
                for q in te:
                    c = cnt[cond(q)]
                    p = (c[q.facet] + 1) / (sum(c.values()) + kf)
                    tot -= math.log(p); n += 1
            return tot / n
        res = {"marginale": ll(lambda q: 0), "selon_le_rang": ll(lambda q: min(q.position, 4)),
               "selon_la_section": ll(lambda q: q.sec), "selon_rang_et_dernier": ll(lambda q: (min(q.position, 4), q.position == q.n_in_part - 1))}
        verdict = "rituel (le rang explique la consigne)" if res["selon_le_rang"] < min(res["selon_la_section"], res["marginale"]) - 0.05 else \
            ("dépend du contenu" if res["selon_la_section"] < res["marginale"] - 0.05 else "peu prévisible")
        self.rep["previsibilite_consigne"] = {"log_loss_sujet_exclu": {k: round(v, 3) for k, v in res.items()},
                                              "verdict": verdict}
        print(f"  consigne : {verdict} {res}")
        # sections qui tombent : année exclue
        yr = {q.exam: q.year for q in Q}
        ys = sorted({y for y in yr.values() if y})
        S = len(self.sections)
        out = {"popularite": [], "modele": []}
        coef = None
        for y in ys[2:]:
            past = [e for e in self.ex_secs if yr.get(e) and yr[e] < y]
            test = [e for e in self.ex_secs if yr.get(e) == y]
            if not past or not test:
                continue

            def feats(es, upto):
                fr = np.array([sum(si in self.ex_secs[e] for e in es) / len(es) for si in range(S)])
                last = np.array([max([yr[e] for e in es if si in self.ex_secs[e]] or [ys[0] - 1]) for si in range(S)])
                parent = defaultdict(float)
                for si in range(S):
                    parent[self.sections[si].parent] += fr[si]
                pf = np.array([parent[self.sections[si].parent] for si in range(S)])
                size = np.array([len(self.sections[si].passages) for si in range(S)], float)
                return np.c_[fr, upto - last, pf, np.log1p(size)]
            Xtr, ytr = [], []
            for y2 in ys:
                if y2 >= y or y2 <= ys[0]:
                    continue
                p2 = [e for e in past if yr[e] < y2]
                t2 = [e for e in past if yr[e] == y2]
                if not p2:
                    continue
                F2 = feats(p2, y2)
                for e in t2:
                    Xtr.append(F2); ytr.append([si in self.ex_secs[e] for si in range(S)])
            Ft = feats(past, y)
            yt = np.array([[si in self.ex_secs[e] for si in range(S)] for e in test], int).ravel()
            pop = np.tile(Ft[:, 0], len(test))
            if len(set(yt)) < 2:
                continue
            out["popularite"].append(roc_auc_score(yt, pop))
            if Xtr:
                Xa, ya = np.vstack(Xtr), np.array(ytr, int).ravel()
                if len(set(ya)) == 2:
                    sc = StandardScaler().fit(Xa)
                    lr = LogisticRegression(C=0.5, max_iter=500).fit(sc.transform(Xa), ya)
                    coef = dict(zip(["frequence_passee", "annees_depuis_derniere", "frequence_du_theme", "taille_section"],
                                    np.round(lr.coef_[0], 2)))
                    out["modele"].append(roc_auc_score(yt, np.tile(lr.predict_proba(sc.transform(Ft))[:, 1], len(test))))
        # probabilité pour l'année suivante : même modèle, appris sur toutes les années
        self.p_next = np.array([self.sec_freq[si] for si in range(S)])
        if ys and "feats" in locals():
            ynext = ys[-1] + 1
            Xtr, ytr = [], []
            for y2 in ys[1:]:
                p2 = [e for e in self.ex_secs if yr.get(e) and yr[e] < y2]
                t2 = [e for e in self.ex_secs if yr.get(e) == y2]
                if p2:
                    F2 = feats(p2, y2)
                    for e in t2:
                        Xtr.append(F2); ytr.append([si in self.ex_secs[e] for si in range(S)])
            allp = [e for e in self.ex_secs if yr.get(e)]
            if Xtr and allp:
                Xa, ya = np.vstack(Xtr), np.array(ytr, int).ravel()
                if len(set(ya)) == 2:
                    sc = StandardScaler().fit(Xa)
                    lr = LogisticRegression(C=0.5, max_iter=500).fit(sc.transform(Xa), ya)
                    self.p_next = lr.predict_proba(sc.transform(feats(allp, ynext)))[:, 1]
        self.rep["probabilite_annee_suivante"] = {self.sections[si].title: round(float(self.p_next[si]), 3)
                                                  for si in np.argsort(-self.p_next)}
        self.rep["previsibilite_sections"] = {
            "methode": "pour chaque année, appris sur les années précédentes seulement ; AUC (0,5 = hasard)",
            "auc_popularite": round(float(np.mean(out["popularite"])), 3) if out["popularite"] else None,
            "auc_modele": round(float(np.mean(out["modele"])), 3) if out["modele"] else None,
            "annees_testees": len(out["popularite"]), "coefficients": {k: float(v) for k, v in (coef or {}).items()}}
        print(f"  sections : AUC popularité {self.rep['previsibilite_sections']['auc_popularite']}, modèle {self.rep['previsibilite_sections']['auc_modele']}")

    # ------------------------------------------------------------------ pipeline
    def run(self):
        self.relevant_parts()
        self.align()
        self.consigne_vocab()
        self.align_rounds()
        self.consigne_facets()
        self.supports()
        self.operations()
        self.detail()
        self.skeleton()
        self.coverage()
        self.predictability()
        return self

    def align_rounds(self):
        """Second tour : on retire les mots de consigne du texte des énoncés avant d'aligner (ils
        n'informent pas sur le contenu) ; gardé seulement si le score sur les corrigés s'améliore."""
        before = self.rep["alignement_sur_le_cours"]["appris_validation_croisee_top1_top3"]
        keep_w = self.w
        old = [q.stem for q in self.Q]
        sw = self.style_words
        for q in self.Q:
            q._orig = q.stem
            q.stem = " ".join(t for t in q.stem.split() if D.norm(t).strip(".,;:?!()«»") not in sw)
        rep_old = self.rep["alignement_sur_le_cours"]
        idx_backup = self.keep_idx
        self.align()
        after = self.rep["alignement_sur_le_cours"]["appris_validation_croisee_top1_top3"]
        for q, s in zip(self.Q, old):
            q.stem = s
        if after[0] + after[1] < before[0] + before[1]:
            self.rep["alignement_sur_le_cours"] = rep_old
            self.w = keep_w
            self.keep_idx = idx_backup
            self.align()
            self.rep["alignement_sur_le_cours"]["second_tour_sans_mots_de_consigne"] = {"garde": False, "score": after}
        else:
            self.rep["alignement_sur_le_cours"]["second_tour_sans_mots_de_consigne"] = {"garde": True, "avant": before}

    def save(self, out: Path):
        out.mkdir(parents=True, exist_ok=True)
        (out / "profil.json").write_text(json.dumps(self.rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
