"""Découverte non supervisée des façons de concevoir une question.

Ici, AUCUNE variable n'est écrite à la main : scikit-learn les apprend à partir du texte brut des
2 668 questions d'écrit, des questions d'épreuve pratique et des exercices du cours.

 1. Trois « vues » de chaque question, construites sans lexique métier :
      contenu   : de quoi parle la question (mots)
      consigne  : COMMENT on la pose. Les mots de contenu sont masqués automatiquement : un mot
                  est « de contenu » si sa distribution sur les thèmes appris est concentrée
                  (entropie faible, seuil choisi par un mélange gaussien), sinon c'est un mot de
                  consigne
      support   : la forme du matériau fourni (code, tableau, appel, liste…) après abstraction
                  des identifiants, nombres et chaînes
    plus une vue « mise en situation » au niveau de l'exercice (préambules).
 2. Pour chaque vue, une factorisation NMF dont le rang est choisi par stabilité bootstrap
    (appariement hongrois des composantes). Chaque composante est une variable découverte,
    étiquetée automatiquement (n-grammes dominants et questions les plus typiques) et notée en
    fiabilité.
 3. Les facettes discrètes (manières de demander, types de support) viennent d'un regroupement
    KMeans, avec un k choisi par silhouette.
 4. Grammaire des combinaisons. Un modèle de plausibilité (régression logistique sur les
    interactions de facettes, entraînée contre des combinaisons corrompues) est combiné à un
    filtrage collaboratif (PPMI + SVD) entre notions et facettes. On en tire les combinaisons
    jamais observées mais au moins aussi plausibles qu'une vraie question.
 5. Le cours découpé en « atomes » (phrases, items). Un apprentissage positif/non-étiqueté
    (Elkan & Noto) apprend ce qui rend un savoir évaluable, puis prédit les détails
    évaluables jamais évalués et la consigne la plus probable pour chacun.
 6. Les transitions entre questions successives sont regroupées en types de transition découverts,
    et les motifs de séquence sont comptés avec leur lift par rapport à une chaîne de Markov
    d'ordre 1.
 7. On mesure ce qui fait la difficulté (Gradient Boosting sur les variables découvertes,
    comparé aux variables manuelles), quels styles émergent dans le temps, quels styles
    s'entraînent en cours ou en pratique sans être jamais tombés à l'écrit, et quelles
    questions réelles sont atypiques.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict

import joblib
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
from sklearn.decomposition import NMF, TruncatedSVD
from sklearn.ensemble import HistGradientBoostingRegressor, IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, silhouette_score
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GroupKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from scipy import sparse

from . import features as F
from .config import CORPUS, MODEL_DIR, SEED
from .ingest import looks_like_code, read_jsonl

NOTIONS = [c for c in F.CONCEPT_NAMES if c not in ("boucles", "booleens")]

# ------------------------------------------------------------------------------- tokenisation
# Seuls des mots-outils du langage sont gardés tels quels (ils ne disent rien du sujet traité).
PY_KW = set("def return for while if else elif in not and or class self None True False import from "
            "range len append pop print lambda assert try except with is".split())
SQL_KW = set("SELECT FROM WHERE JOIN ON INSERT INTO UPDATE SET DELETE VALUES ORDER BY GROUP COUNT DISTINCT "
             "AND OR AS PRIMARY KEY FOREIGN REFERENCES CREATE TABLE MAX MIN SUM AVG LIKE ASC DESC".split())
TOK = re.compile(r">>>|\d+(?:[.,]\d+)?|[A-Za-zÀ-ÿ_][\wÀ-ÿ']*|[^\s\w]")
WORD = re.compile(r"[a-z][a-z'\-]+")


# Artefacts de mise en forme des sources (Markdown des cours / sujets pratiques, PDF des écrits) :
# sans ce nettoyage, l'algorithme « découvre » des styles qui ne sont que des différences de format.
MD = [(re.compile(r"\{\{.*?\}\}", re.S), " "), (re.compile(r"!\[[^\]]*\]\([^)]*\)"), " "),
      (re.compile(r"\{:[^}]*\}"), " "), (re.compile(r"```[a-z]*"), "\n"), (re.compile(r"linenums=['\"]\d+['\"]"), " "),
      (re.compile(r"(?m)^\s*(?:!!!|\?\?\?|===)[^\n]*$"), " "), (re.compile(r"`|\*\*|__|\$"), ""),
      (re.compile(r"[«»“”]"), '"'), (re.compile(r"(?m)^\s*\*\s"), "- ")]


def neutral(text: str) -> str:
    for p, s in MD:
        text = p.sub(s, text or "")
    return text


def is_prose(s: str) -> bool:
    if looks_like_code(s) or re.search(r"\bdef |>>>|\breturn\b|self\.|\w\(\)|[=<>]=|\w\s*=\s*\w|\[\d|\bprint\(", s):
        return False
    letters = sum(c.isalpha() or c.isspace() for c in s)
    return letters / max(len(s), 1) > 0.85


def shape_tokens(text: str) -> str:
    """Forme du matériau : identifiants -> ID, nombres -> N, prose -> W (une seule par passage)."""
    out = []
    for line in text.split("\n")[-40:]:
        if not line.strip():
            continue
        code = looks_like_code(line) or line.startswith(("    ", "\t")) or "|" in line
        out.append("NL")
        if code and line.startswith(("    ", "\t")):
            out.append("IND")
        for t in TOK.findall(line):
            if t in SQL_KW:
                out.append(t)
            elif t in PY_KW and code:
                out.append(t)
            elif t[0].isdigit():
                out.append("N")
            elif t[0].isalpha() or t[0] == "_":
                out.append("ID" if code or "_" in t else "W")
            elif t in "\"'":
                out.append("Q")
            else:
                out.append({"|": "BAR", "#": "H", "*": "STAR"}.get(t, t))
        # compacte les suites de prose
    comp = []
    for t in out:
        if t == "W" and comp and comp[-1] == "W":
            continue
        comp.append(t)
    return " ".join(comp)


def identifiers(text: str) -> set[str]:
    return set(re.findall(r"`+\s*([A-Za-z_]\w*)", text)) | set(re.findall(r"\b([a-z_]\w*_\w+|[a-z]\w*)\s*\(", text))


# ------------------------------------------------------------------------------- outils
def stable_nmf(X, ks, seed=SEED, n_boot=3, label=""):
    """Rang NMF choisi par stabilité : on refait la factorisation sur des sous-échantillons et on
    apparie les composantes (algorithme hongrois). On garde le plus grand rang dont la stabilité
    reste à 95 % de la meilleure."""
    rng = np.random.default_rng(seed)
    n = X.shape[0]
    stab = {}
    boots = {}
    for k in ks:
        Hs = []
        for b in range(n_boot):
            idx = rng.choice(n, int(0.8 * n), replace=False)
            H = NMF(k, init="nndsvda", random_state=seed + b, max_iter=500).fit(X[idx]).components_
            Hs.append(H / (np.linalg.norm(H, axis=1, keepdims=True) + 1e-12))
        sims = []
        for i in range(n_boot):
            for j in range(i + 1, n_boot):
                S = Hs[i] @ Hs[j].T
                r, c = linear_sum_assignment(-S)
                sims.append(S[r, c].mean())
        stab[k] = float(np.mean(sims))
        boots[k] = Hs
    best = max(stab.values())
    k = max(k for k, s in stab.items() if s >= 0.95 * best)
    model = NMF(k, init="nndsvda", random_state=seed, max_iter=800)
    W = model.fit_transform(X)
    H = model.components_ / (np.linalg.norm(model.components_, axis=1, keepdims=True) + 1e-12)
    per = np.zeros(k)
    for Hb in boots[k]:
        S = H @ Hb.T
        r, c = linear_sum_assignment(-S)
        per[r] += S[r, c] / len(boots[k])
    print(f"    {label}: rang {k} (stabilité {stab[k]:.2f} ; essais {', '.join(f'{a}:{b:.2f}' for a, b in stab.items())})")
    return model, W, per, stab


def pick_k(Z, ks, seed=SEED, sample=2500):
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(Z), min(sample, len(Z)), replace=False)
    best, bk = -1, ks[0]
    for k in ks:
        lab = KMeans(k, n_init=4, random_state=seed).fit_predict(Z[idx])
        s = silhouette_score(Z[idx], lab)
        if s > best:
            best, bk = s, k
    km = KMeans(bk, n_init=8, random_state=seed).fit(Z)
    return km, bk, best


def rownorm(W):
    return W / (np.linalg.norm(W, axis=1, keepdims=True) + 1e-9)


def snippet(t: str, n=160) -> str:
    return re.sub(r"\s+", " ", t).strip()[:n]


# ------------------------------------------------------------------------------- découverte
class Discoverer:
    def __init__(self):
        exams = read_jsonl(CORPUS / "exams.jsonl")
        written = [e for e in exams if e["type"] == "ecrit"]
        practical = [e for e in exams if e["type"] == "pratique"]
        for e in practical:
            e["exercises"] = [x for x in e["exercises"] if not x.get("duplicate_of_previous_year")]
        cex = read_jsonl(CORPUS / "course_exercises.jsonl") if (CORPUS / "course_exercises.jsonl").exists() else []
        fake = [{"id": f"cours-{i}", "type": "cours", "year": None, "center": e["lesson"], "n_exercises": 1,
                 "exercises": [{"number": "1", "points": None, "theme_sentence": None, "preamble": e["preamble"],
                                "raw": e["preamble"] + "\n" + "\n".join(q["text"] for q in e["questions"]),
                                "questions": e["questions"]}]} for i, e in enumerate(cex)]
        self.u = []
        for src, ex in (("ecrit", written), ("pratique", practical), ("cours", fake)):
            for r in F.build_question_table(ex) if src != "cours" else self._course_rows(fake):
                r["src"] = src
                r["main"] = F.main_concepts(r)
                r["text"], r["context"] = neutral(r["text"]), neutral(r["context"])
                self.u.append(r)
        self.preambles = {}
        for e in written + practical + fake:
            for x in e["exercises"]:
                self.preambles[(e["id"], x["number"])] = neutral((x.get("preamble") or "") + " " + (x.get("theme_sentence") or ""))
        self.course = read_jsonl(CORPUS / "course.jsonl")
        self.W_idx = [i for i, r in enumerate(self.u) if r["src"] == "ecrit"]
        self.rep: dict = {"corpus_d_exposition": dict(Counter(r["src"] for r in self.u))}
        self.m: dict = {}
        print(f"  unités d'entraînement : {self.rep['corpus_d_exposition']}")

    @staticmethod
    def _course_rows(fake):
        rows = []
        for e in fake:
            for r in F.build_question_table([dict(e, type="pratique")]):
                r["exam_type"] = "cours"
                rows.append(r)
        return rows

    # -------------------------------------------------------------- 1. vues + variables latentes
    def content_view(self):
        texts = [F.norm(r["text"] + " " + r["context"][-400:]) for r in self.u]
        self.cvec = TfidfVectorizer(token_pattern=r"[a-z_][a-z_0-9]{2,}", min_df=3, max_df=0.4, sublinear_tf=True, max_features=20000)
        X = self.cvec.fit_transform(texts)
        self.cnmf, self.Wc, self.cstab, s = stable_nmf(X, [20, 30, 40, 55], label="contenu")
        self.Xc = X

    def style_mask(self):
        """Sépare automatiquement mots de consigne et mots de contenu, à partir de deux signaux appris :
        - entropie de la distribution du mot sur les thèmes NMF (un mot de consigne est partout) ;
        - « grappage » : un mot de contenu revient en rafale dans les questions d'un même exercice,
          un mot de consigne est réparti comme au hasard (ratio exercices attendus / observés).
        Un mélange gaussien 2D tranche entre les deux populations."""
        P = rownorm(self.Wc) ** 2
        acc = defaultdict(lambda: np.zeros(self.Wc.shape[1]))
        df, exs = Counter(), defaultdict(set)
        ex_size = Counter((r["exam_id"], r["exercise"]) for r in self.u)
        for d, r in enumerate(self.u):
            for w in set(WORD.findall(F.norm(r["text"]))):
                acc[w] += P[d]
                df[w] += 1
                exs[w].add((r["exam_id"], r["exercise"]))
        words = sorted(w for w in acc if df[w] >= 8)
        N = len(self.u)
        sizes = np.array(list(ex_size.values()))
        feats = []
        for w in words:
            p = acc[w] / acc[w].sum()
            ent = -(p * np.log(p + 1e-12)).sum() / np.log(len(p))
            q = df[w] / N
            expected = (1 - (1 - q) ** sizes).sum()
            feats.append([ent, np.log(expected / len(exs[w]))])
        Z = np.array(feats)
        Zs = (Z - Z.mean(0)) / Z.std(0)
        gm = GaussianMixture(2, covariance_type="full", random_state=SEED, n_init=5).fit(Zs)
        score = gm.means_[:, 0] - gm.means_[:, 1]  # entropie haute, grappage faible
        st = int(np.argmax(score))
        keep = gm.predict_proba(Zs)[:, st] > 0.5
        self.style_words = {w for w, k in zip(words, keep) if k}
        sc = Zs[:, 0] - Zs[:, 1]
        order = np.argsort(-sc)
        self.rep["separation_consigne_contenu"] = {
            "mots_analyses": len(words), "mots_de_consigne_decouverts": int(keep.sum()),
            "signaux": "entropie thématique + grappage intra-exercice, mélange gaussien 2D",
            "exemples_consigne": [words[i] for i in order[:50]],
            "exemples_contenu": [words[i] for i in order[::-1][:30]],
            "frontiere_cote_consigne": [words[i] for i in order if keep[i]][-15:],
            "frontiere_cote_contenu": [words[i] for i in order if not keep[i]][:15],
        }
        print(f"    séparation : {keep.sum()} mots de consigne / {len(words)}")

    def style_text(self, stem: str) -> str:
        out = []
        for t in TOK.findall(stem)[:40]:
            tn = F.norm(t)
            if tn in self.style_words:
                out.append(tn)
            elif t[0].isdigit():
                out.append("N")
            elif t[0].isalpha():
                out.append("X")
            elif t in "?:(":
                out.append({"?": "QM", ":": "COLON", "(": "PAR"}[t])
        comp = []
        for t in out:
            if t == "X" and comp and comp[-1] == "X":
                continue
            comp.append(t)
        return " ".join(comp)

    def style_view(self):
        self.svec = TfidfVectorizer(token_pattern=r"\S+", ngram_range=(1, 4), min_df=4, max_df=0.08, sublinear_tf=True, lowercase=False)
        X = self.svec.fit_transform([self.style_text(r["text"]) for r in self.u])
        self.snmf, self.Ws, self.sstab, _ = stable_nmf(X, [15, 22, 30, 40], label="consigne")

    def support_view(self):
        self.uvec = TfidfVectorizer(token_pattern=r"\S+", ngram_range=(1, 4), min_df=4, max_df=0.6, sublinear_tf=True, lowercase=False)
        X = self.uvec.fit_transform([shape_tokens(r["context"][-700:] + "\nNL\n" + r["text"]) for r in self.u])
        self.unmf, self.Wu, self.ustab, _ = stable_nmf(X, [10, 15, 20, 28], label="support")

    def scenario_view(self):
        keys = sorted(self.preambles)
        texts = [F.norm(self.preambles[k]) for k in keys]
        self.pvec = TfidfVectorizer(token_pattern=r"[a-z][a-z]{3,}", min_df=3, max_df=0.3, sublinear_tf=True, max_features=8000)
        X = self.pvec.fit_transform(texts)
        self.pnmf, Wp, self.pstab, _ = stable_nmf(X, [12, 18, 25], label="mise en situation")
        self.scen_of = {k: int(np.argmax(w)) if w.sum() > 0 else -1 for k, w in zip(keys, Wp)}

    def label_components(self):
        """Étiquetage automatique : n-grammes dominants + questions les plus typiques."""
        def lab(model, vec, W, stab, prefix, texts):
            names = np.array(vec.get_feature_names_out())
            out = []
            for j, h in enumerate(model.components_):
                top = names[np.argsort(-h)[:8]].tolist()
                ex = [snippet(texts[i]) for i in np.argsort(-W[:, j])[:3]]
                srcs = Counter(self.u[i]["src"] for i in np.argsort(-W[:, j])[:60])
                out.append({"id": f"{prefix}{j}", "termes": top, "exemples": ex, "fiabilite": round(float(stab[j]), 2),
                            "poids_moyen": round(float(W[:, j].mean()), 4), "sources_typiques": dict(srcs)})
            return out
        texts = [r["text"] for r in self.u]
        self.vars = {
            "consigne": lab(self.snmf, self.svec, self.Ws, self.sstab, "C", texts),
            "support": lab(self.unmf, self.uvec, self.Wu, self.ustab, "S", [r["context"][-200:] + " ⏎ " + r["text"] for r in self.u]),
            "contenu": lab(self.cnmf, self.cvec, self.Wc, self.cstab, "T", texts),
        }
        names = np.array(self.pvec.get_feature_names_out())
        self.vars["mise_en_situation"] = [{"id": f"M{j}", "termes": names[np.argsort(-h)[:8]].tolist(),
                                           "fiabilite": round(float(self.pstab[j]), 2)} for j, h in enumerate(self.pnmf.components_)]
        n = sum(len(v) for v in self.vars.values())
        self.rep["variables_decouvertes"] = {"total": n, **{k: len(v) for k, v in self.vars.items()},
                                             "fiables_>=0.7": sum(x["fiabilite"] >= 0.7 for v in self.vars.values() for x in v)}
        print(f"    {n} variables latentes découvertes")

    # -------------------------------------------------------------- 3. facettes
    def facets(self):
        self.kms, _, s1 = pick_k(rownorm(self.Ws), [12, 16, 20, 25, 30])
        self.kmu, _, s2 = pick_k(rownorm(self.Wu), [8, 12, 16, 20])
        self.fs = self.kms.labels_
        self.fu = self.kmu.labels_

        def describe(km, W, fac, vars_):
            out = {}
            for f in range(km.n_clusters):
                idx = np.where(fac == f)[0]
                prof = km.cluster_centers_[f]
                comps = [vars_[j]["id"] for j in np.argsort(-prof)[:2]]
                w_idx = [i for i in idx if self.u[i]["src"] == "ecrit"]
                ex = sorted(idx, key=lambda i: -float((rownorm(W[i:i + 1]) @ prof)[0]))
                out[f] = {"effectif": int(len(idx)), "a_l_ecrit": len(w_idx),
                          "part_ecrit": round(len(w_idx) / max(len(idx), 1), 2),
                          "composantes": comps, "termes": vars_[int(np.argmax(prof))]["termes"][:6],
                          "exemples": [snippet(self.u[i]["text"], 200) for i in ex[:3]],
                          "position_moyenne": round(float(np.mean([self.u[i]["rel_pos"] for i in w_idx])), 2) if w_idx else None,
                          "notions_frequentes": [c for c, _ in Counter(self.u[i]["main"][0] for i in idx if self.u[i]["main"]).most_common(4)]}
            return out
        self.style_facets = describe(self.kms, self.Ws, self.fs, self.vars["consigne"])
        self.support_facets = describe(self.kmu, self.Wu, self.fu, self.vars["support"])
        self.rep["facettes"] = {"manieres_de_demander": {"k": self.kms.n_clusters, "silhouette": round(s1, 3)},
                                "types_de_support": {"k": self.kmu.n_clusters, "silhouette": round(s2, 3)}}
        print(f"    facettes : {self.kms.n_clusters} manières de demander, {self.kmu.n_clusters} types de support")

    # -------------------------------------------------------------- 4. grammaire des combinaisons
    def combination_grammar(self):
        W = self.W_idx
        nidx = {c: i for i, c in enumerate(NOTIONS)}
        rows = []
        groups = []
        for i in W:
            r = self.u[i]
            n = next((c for c in r["main"] if c in nidx), None)
            if n is None:
                continue
            rows.append([n, f"c{self.fs[i]}", f"s{self.fu[i]}", f"p{min(int(r['rel_pos'] * 3), 2)}"])
            groups.append(r["exam_id"])
        pos = np.array(rows, dtype=object)
        rng = np.random.default_rng(SEED)
        neg = []
        cols = [pos[:, j] for j in range(4)]
        for _ in range(3):
            for row in pos:
                x = row.copy()
                j = rng.integers(4)
                while True:
                    v = cols[j][rng.integers(len(pos))]
                    if v != row[j]:
                        break
                x[j] = v
                neg.append(x)
        neg = np.array(neg, dtype=object)
        obs = {tuple(r) for r in pos}
        neg = np.array([r for r in neg if tuple(r) not in obs], dtype=object)
        X = np.vstack([pos, neg])
        y = np.r_[np.ones(len(pos)), np.zeros(len(neg))]
        g = np.r_[groups, rng.choice(groups, len(neg))]
        self.plaus = make_pipeline(OneHotEncoder(handle_unknown="ignore"),
                                   PolynomialFeatures(2, interaction_only=True, include_bias=False),
                                   LogisticRegression(C=0.3, max_iter=3000))
        p = cross_val_predict(self.plaus, X, y, groups=g, cv=GroupKFold(5), method="predict_proba")[:, 1]
        auc = roc_auc_score(y, p)
        self.plaus.fit(X, y)
        ref = float(np.median(self.plaus.predict_proba(pos)[:, 1]))

        # filtrage collaboratif : transfert d'une façon de demander d'une notion à ses voisines
        def cf(col):
            M = np.zeros((len(NOTIONS), self.kms.n_clusters if col == 1 else self.kmu.n_clusters))
            for row in pos:
                M[nidx[row[0]], int(row[col][1:])] += 1
            tot = M.sum()
            pmi = np.log((M * tot + 1e-9) / (M.sum(1, keepdims=True) @ M.sum(0, keepdims=True) + 1e-9))
            pp = np.maximum(pmi, 0)
            svd = TruncatedSVD(min(8, min(pp.shape) - 1), random_state=SEED)
            R = svd.fit_transform(pp) @ svd.components_
            pct = R.argsort(axis=None).argsort().reshape(R.shape) / R.size
            return M, pct
        Mns, CFs = cf(1)
        Mnu, CFu = cf(2)
        tri = Counter((r[0], r[1], r[2]) for r in pos)
        cand = []
        for n in NOTIONS:
            for c in range(self.kms.n_clusters):
                for s in range(self.kmu.n_clusters):
                    for pb in range(3):
                        cand.append([n, f"c{c}", f"s{s}", f"p{pb}"])
        cand = np.array(cand, dtype=object)
        pr = self.plaus.predict_proba(cand)[:, 1]
        out = []
        for row, pv in zip(cand, pr):
            n, c, s = row[0], int(row[1][1:]), int(row[2][1:])
            if tri[(row[0], row[1], row[2])] > 0:
                continue
            new_pair_c, new_pair_s = Mns[nidx[n], c] == 0, Mnu[nidx[n], s] == 0
            cfv = (CFs[nidx[n], c] + CFu[nidx[n], s]) / 2
            score = float(pv) ** 0.6 * cfv ** 0.4
            if pv >= ref:
                out.append({"notion": n, "consigne": c, "support": s, "position": int(row[3][1:]),
                            "plausibilite": round(float(pv), 3), "transfert_cf": round(float(cfv), 3), "score": round(score, 3),
                            "nouveaute": "manière de demander jamais utilisée pour cette notion" if new_pair_c else
                                         "support jamais utilisé pour cette notion" if new_pair_s else "combinaison inédite d'éléments connus"})
        out.sort(key=lambda d: -d["score"])
        # une seule position par (notion, consigne, support)
        seen, best = set(), []
        for d in out:
            k = (d["notion"], d["consigne"], d["support"])
            if k not in seen:
                seen.add(k)
                best.append(d)
        self.candidates = best
        n_tot = len({(r[0], r[1], r[2]) for r in cand})
        self.rep["grammaire_des_combinaisons"] = {
            "AUC_vraie_vs_corrompue_validation_croisee": round(float(auc), 3),
            "plausibilite_mediane_des_vraies_questions": round(ref, 3),
            "combinaisons_possibles": n_tot, "combinaisons_observees": len(tri),
            "inedites_aussi_plausibles_que_le_reel": len(best),
            "par_type_de_nouveaute": dict(Counter(d["nouveaute"] for d in best)),
            "exemples": best[:25],
        }
        print(f"    plausibilité AUC={auc:.3f} ; {len(best)} combinaisons inédites plausibles sur {n_tot}")

    # -------------------------------------------------------------- 5. atomes du cours (PU)
    def course_atoms(self):
        atoms = []
        for si, s in enumerate(self.course):
            if s["source"] == "BO":
                continue
            for para in re.split(r"\n\s*\n|\n(?=[-*•] )", neutral(s["text"])):
                para = para.strip()
                if looks_like_code(para.split("\n")[0]) and len(para.split("\n")) > 2:
                    continue
                for sent in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý])", para):
                    sent = re.sub(r"\s+", " ", sent).strip(" -*•")
                    if 50 <= len(sent) <= 420 and is_prose(sent):
                        atoms.append({"sec": si, "text": sent, "lesson": s["lesson"], "chapter": s["chapter"]})
        texts_a = [F.norm(a["text"]) for a in atoms]
        qtexts = [F.norm(self.u[i]["text"] + " " + self.u[i]["context"][-300:]) for i in range(len(self.u)) if self.u[i]["src"] != "cours"]
        qidx = [i for i in range(len(self.u)) if self.u[i]["src"] != "cours"]
        vec = TfidfVectorizer(token_pattern=r"[a-z_][a-z_0-9]{2,}", ngram_range=(1, 2), min_df=2, max_df=0.3, sublinear_tf=True, max_features=40000)
        vec.fit(texts_a + qtexts)
        svd = TruncatedSVD(120, random_state=SEED).fit(vec.transform(texts_a + qtexts))
        A = rownorm(svd.transform(vec.transform(texts_a)))
        Q = rownorm(svd.transform(vec.transform(qtexts)))
        S = A @ Q.T
        best_q = S.argmax(1)
        smax = S.max(1)
        thr = float(np.quantile(smax, 0.85))
        lab = (smax >= thr).astype(int)
        # variables du savoir : forme de la phrase (sans le sujet) + contenu
        sty = TfidfVectorizer(token_pattern=r"\S+", ngram_range=(1, 3), min_df=3, lowercase=False, sublinear_tf=True)
        Xs = sty.fit_transform([self.style_text(a["text"]) + " | " + shape_tokens(a["text"]) for a in atoms])
        con = TfidfVectorizer(token_pattern=r"[a-z_][a-z_0-9]{2,}", min_df=3, max_df=0.3, sublinear_tf=True, max_features=15000)
        Xk = con.fit_transform(texts_a)
        X = sparse.hstack([Xs, Xk]).tocsr()
        clf = LogisticRegression(C=1.0, max_iter=3000, class_weight="balanced")
        p_cv = cross_val_predict(clf, X, lab, cv=5, method="predict_proba")[:, 1]
        c = float(p_cv[lab == 1].mean())  # Elkan & Noto : P(étiqueté | positif)
        clf.fit(X, lab)
        raw = clf.predict_proba(X)[:, 1]
        prob = np.clip(raw / c, 0, 1)
        # ce qui rend un savoir évaluable, appris (coefficients sur la forme de la phrase)
        fn = np.r_[np.array(sty.get_feature_names_out()), np.array(con.get_feature_names_out())]
        co = clf.coef_[0][: Xs.shape[1]]
        self.rep_evaluable = {"formes_qui_rendent_evaluable": fn[np.argsort(-co)[:20]].tolist(),
                              "formes_rarement_evaluees": fn[np.argsort(co)[:15]].tolist()}
        # types de savoir découverts
        nm = NMF(14, init="nndsvda", random_state=SEED, max_iter=600)
        Wt = nm.fit_transform(Xs)
        kind = Wt.argmax(1)
        names = np.array(sty.get_feature_names_out())
        kinds = []
        for j in range(nm.n_components):
            idx = np.where(kind == j)[0]
            if len(idx) == 0:
                continue
            kinds.append({"type": j, "termes": names[np.argsort(-nm.components_[j])[:8]].tolist(), "effectif": int(len(idx)),
                          "part_evaluee": round(float(lab[idx].mean()), 3), "evaluabilite_moyenne": round(float(prob[idx].mean()), 3),
                          "exemple": snippet(atoms[idx[np.argmax(Wt[idx, j])]]["text"], 180)})
        kinds.sort(key=lambda d: -d["evaluabilite_moyenne"])
        # consigne recommandée pour un atome jamais évalué : vote des atomes évalués les plus proches
        ev = np.where(lab == 1)[0]
        ev_style = np.array([self.fs[qidx[best_q[i]]] for i in ev])
        nev = np.where(lab == 0)[0]
        sim = A[nev] @ A[ev].T
        rec = []
        for row in sim:
            nn = np.argsort(-row)[:15]
            rec.append(Counter(ev_style[nn]).most_common(1)[0][0])
        rec_of = dict(zip(nev.tolist(), rec))
        by_notion = defaultdict(list)
        for i in nev:
            hits = F.concept_hits(atoms[i]["text"] + " " + atoms[i]["lesson"])
            for n in sorted(hits, key=lambda k: -hits[k])[:1]:
                if n in NOTIONS:
                    by_notion[n].append(i)
        top = {}
        for n, idx in by_notion.items():
            idx = sorted(idx, key=lambda i: -raw[i])[:12]
            top[n] = [{"atome": atoms[i]["text"], "lecon": atoms[i]["lesson"], "evaluabilite": round(float(prob[i]), 3),
                       "similarite_max_aux_annales": round(float(smax[i]), 3), "consigne_recommandee": int(rec_of[i])} for i in idx]
        self.atoms, self.atom_prob, self.atom_top = atoms, prob, top
        for n, v in top.items():
            for d, i in zip(v, sorted(by_notion[n], key=lambda i: -raw[i])):
                d["_score"] = float(raw[i])
        flat = sorted(((n, d) for n, v in top.items() for d in v[:3]), key=lambda t: -t[1]["_score"])
        for v in top.values():
            for d in v:
                d.pop("_score", None)
        self.rep["savoirs_du_cours"] = {
            "atomes": len(atoms), "deja_evalues": int(lab.sum()), "seuil_similarite": round(thr, 3),
            "c_Elkan_Noto": round(c, 3), **self.rep_evaluable,
            "types_de_savoir_decouverts": kinds,
            "evaluables_jamais_evalues_top": [{"notion": n, **d} for n, d in flat[:30]],
        }
        print(f"    {len(atoms)} atomes de cours ; {int(lab.sum())} déjà évalués ; c={c:.2f}")

    # -------------------------------------------------------------- 6. transitions et motifs
    def transitions(self):
        seqs = defaultdict(list)
        for i in self.W_idx:
            r = self.u[i]
            seqs[(r["exam_id"], r["exercise"])].append(i)
        Ws, Wc, Wu = rownorm(self.Ws), rownorm(self.Wc), rownorm(self.Wu)
        feats, meta = [], []
        for key, idx in seqs.items():
            idx.sort(key=lambda i: self.u[i]["pos"])
            for a, b in zip(idx, idx[1:]):
                ia, ib = identifiers(self.u[a]["text"]), identifiers(self.u[b]["text"])
                jac = len(ia & ib) / max(len(ia | ib), 1)
                dep = int(self.u[b]["pos"] - 1 in self.u[b]["deps"])
                f = np.r_[Ws[b] - Ws[a], 2 * float(Wc[a] @ Wc[b]), float(Wu[a] @ Wu[b]), 2 * jac, dep,
                          np.tanh((self.u[b]["len_words"] - self.u[a]["len_words"]) / 30)]
                feats.append(f)
                meta.append((a, b))
        Z = np.array(feats)
        km, k, sil = pick_k(Z, [6, 8, 10, 12, 14])
        names = [v["id"] for v in self.vars["consigne"]]
        ks = self.Ws.shape[1]
        types = []
        for t in range(k):
            m = np.where(km.labels_ == t)[0]
            cen = Z[m].mean(0)
            up = [names[j] + ":" + " ".join(self.vars["consigne"][j]["termes"][:2]) for j in np.argsort(-cen[:ks])[:2] if cen[j] > 0.05]
            dn = [names[j] + ":" + " ".join(self.vars["consigne"][j]["termes"][:2]) for j in np.argsort(cen[:ks])[:2] if cen[j] < -0.05]
            a, b = meta[m[np.argmin(((Z[m] - km.cluster_centers_[t]) ** 2).sum(1))]]
            types.append({"type": t, "effectif": int(len(m)), "meme_contenu": round(float(cen[ks] / 2), 2),
                          "meme_support": round(float(cen[ks + 1]), 2), "reutilise_identifiants": round(float(cen[ks + 2] / 2), 2),
                          "depend_explicitement": round(float(cen[ks + 3]), 2),
                          "la_consigne_glisse_vers": up, "en_quittant": dn,
                          "exemple": [snippet(self.u[a]["text"], 120), snippet(self.u[b]["text"], 120)]})
        self.trans_types = types
        # motifs de séquence (facettes de consigne) avec lift vs Markov d'ordre 1
        seq_f = [[int(self.fs[i]) for i in idx] for idx in seqs.values()]
        uni = Counter(f for s in seq_f for f in s)
        bi = Counter((a, b) for s in seq_f for a, b in zip(s, s[1:]))
        tri = Counter(tuple(s[i:i + 3]) for s in seq_f for i in range(len(s) - 2))
        N1 = sum(uni.values())
        motifs = []
        for (a, b, c), n in tri.items():
            if n < 4:
                continue
            exp = bi[(a, b)] * bi[(b, c)] / max(uni[b], 1)
            motifs.append({"motif": [a, b, c], "occurrences": n, "lift_vs_markov": round(n / max(exp, 1e-9), 2)})
        for (a, b), n in bi.items():
            if n >= 6:
                motifs.append({"motif": [a, b], "occurrences": n, "lift_vs_markov": round(n * N1 / (uni[a] * uni[b]), 2)})
        motifs.sort(key=lambda d: -(d["lift_vs_markov"] * np.log1p(d["occurrences"])))
        self.motifs = motifs
        T = np.full((self.kms.n_clusters + 1,) * 2, 0.3)
        for s in seq_f:
            prev = self.kms.n_clusters
            for f in s:
                T[prev, f] += 1
                prev = f
        self.style_T = T / T.sum(1, keepdims=True)
        self.rep["dynamique_des_exercices"] = {"types_de_transition_decouverts": types, "silhouette": round(sil, 3),
                                               "motifs_de_sequence": motifs[:20]}
        print(f"    {k} types de transition, {len(motifs)} motifs")

    # -------------------------------------------------------------- 7. difficulté, tendances, transferts
    def hidden_drivers(self):
        W = self.W_idx
        X = np.hstack([rownorm(self.Ws)[W], rownorm(self.Wu)[W], rownorm(self.Wc)[W]])
        names = [v["id"] for v in self.vars["consigne"]] + [v["id"] for v in self.vars["support"]] + [v["id"] for v in self.vars["contenu"]]
        y = np.array([self.u[i]["rel_pos"] for i in W])
        g = np.array([self.u[i]["exam_id"] for i in W])
        gb = HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, max_leaf_nodes=15, random_state=SEED)
        pred = cross_val_predict(gb, X, y, groups=g, cv=GroupKFold(5))
        r2 = 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()
        gb.fit(X, y)
        pi = permutation_importance(gb, X, y, n_repeats=5, random_state=SEED)
        lookup = {v["id"]: v for k in ("consigne", "support", "contenu") for v in self.vars[k]}
        top = []
        for j in np.argsort(-pi.importances_mean)[:12]:
            rho = spearmanr(X[:, j], y).correlation
            top.append({"variable": names[j], "termes": lookup[names[j]]["termes"][:5], "importance": round(float(pi.importances_mean[j]), 4),
                        "sens": "pousse vers la fin d'exercice" if rho > 0 else "pousse vers le début", "rho": round(float(rho), 3)})
        # comparaison à armes égales : variables manuelles seules, découvertes seules, les deux
        Xm, mn = F.feature_matrix([self.u[i] for i in W])
        Xm = Xm[:, [j for j, n in enumerate(mn) if n != "rel_pos"]]

        def r2_of(Xa):
            pr = cross_val_predict(HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, max_leaf_nodes=15, random_state=SEED),
                                   Xa, y, groups=g, cv=GroupKFold(5))
            return float(1 - ((y - pr) ** 2).sum() / ((y - y.mean()) ** 2).sum())
        manual = round(r2_of(Xm), 3)
        both = round(r2_of(np.hstack([Xm, X])), 3)
        # tendances temporelles par variable découverte
        years = np.array([self.u[i]["year"] or 0 for i in W])
        trends = []
        for j, nm in enumerate(names):
            if X[:, j].std() < 1e-6:
                continue
            rho = spearmanr(years, X[:, j]).correlation
            old, new = X[years <= 2022, j].mean(), X[years >= 2024, j].mean()
            trends.append({"variable": nm, "termes": lookup[nm]["termes"][:5], "rho_annee": round(float(rho), 3),
                           "ratio_recent_vs_2021_22": round(float((new + 1e-4) / (old + 1e-4)), 2)})
        trends.sort(key=lambda d: -d["rho_annee"])
        # styles entraînés en cours / pratique mais absents de l'écrit
        transfer = []
        for f, d in self.style_facets.items():
            if d["effectif"] >= 8 and d["part_ecrit"] < 0.25:
                transfer.append({"consigne": f, **{k: d[k] for k in ("effectif", "a_l_ecrit", "termes", "exemples")}})
        # atypiques réels (inspiration hors norme)
        Z = np.hstack([rownorm(self.Ws), rownorm(self.Wu)])[W]
        iso = IsolationForest(n_estimators=300, contamination=0.02, random_state=SEED).fit(Z)
        sc = iso.score_samples(Z)
        odd = [{"annee": self.u[W[i]]["year"], "texte": snippet(self.u[W[i]]["text"], 220)} for i in np.argsort(sc)[:12]]
        # contrôle : les variables découvertes encodent-elles la notion et le format d'épreuve ?
        notion = np.array([self.u[i]["main"][0] if self.u[i]["main"] else "aucune" for i in W])
        ok = np.isin(notion, [c for c, n in Counter(notion).items() if n >= 15])
        acc = (cross_val_predict(LogisticRegression(max_iter=3000, C=2.0), X[ok], notion[ok], groups=g[ok], cv=GroupKFold(5)) == notion[ok]).mean()
        reg = np.array([self.u[i]["regime"].startswith("2023") for i in W]).astype(int)
        auc = roc_auc_score(reg, cross_val_predict(LogisticRegression(max_iter=3000), X, reg, groups=g, cv=GroupKFold(5), method="predict_proba")[:, 1])
        self.rep["moteurs_caches"] = {
            "difficulte": {"R2_variables_decouvertes": round(float(r2), 3), "R2_variables_manuelles": manual,
                           "R2_les_deux": both, "principales": top},
            "styles_en_hausse": trends[:10], "styles_en_baisse": trends[::-1][:10],
            "styles_entraines_jamais_tombes_a_l_ecrit": transfer,
            "questions_reelles_atypiques": odd,
            "controle": {"precision_notion_depuis_variables_decouvertes": round(float(acc), 3),
                         "AUC_format_2023_depuis_variables_decouvertes": round(float(auc), 3)},
        }
        print(f"    difficulté R²={r2:.3f} (manuel {manual}, les deux {both}) ; notion acc={acc:.2f} ; format AUC={auc:.2f}")

    # -------------------------------------------------------------- sauvegarde
    def run(self):
        for s in (self.content_view, self.style_mask, self.style_view, self.support_view, self.scenario_view,
                  self.label_components, self.facets, self.combination_grammar, self.course_atoms,
                  self.transitions, self.hidden_drivers):
            print(f"  · {s.__name__}")
            s()
        self.save()

    def save(self):
        joblib.dump({
            "cvec": self.cvec, "cnmf": self.cnmf, "svec": self.svec, "snmf": self.snmf, "uvec": self.uvec, "unmf": self.unmf,
            "kms": self.kms, "kmu": self.kmu, "style_words": self.style_words, "plaus": self.plaus, "style_T": self.style_T,
        }, MODEL_DIR / "discovery_models.joblib", compress=3)
        units = [{k: r[k] for k in ("src", "exam_id", "exercise", "pos", "rel_pos", "text", "main")} for r in self.u]
        joblib.dump({"units": units, "fs": self.fs, "fu": self.fu, "candidates": self.candidates, "atom_top": self.atom_top,
                     "style_facets": self.style_facets, "support_facets": self.support_facets, "vars": self.vars,
                     "motifs": self.motifs, "trans_types": self.trans_types}, MODEL_DIR / "discovery_data.joblib", compress=3)
        self.rep["facettes"]["detail_manieres_de_demander"] = self.style_facets
        self.rep["facettes"]["detail_types_de_support"] = self.support_facets
        self.rep["variables"] = self.vars
        (MODEL_DIR / "discovery.json").write_text(json.dumps(self.rep, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
        print(f"[ok] découverte -> {MODEL_DIR / 'discovery.json'}")


# ------------------------------------------------------------------------------- inférence
class FacetModel:
    """Recalcule les facettes d'un texte nouveau (validation des questions générées)."""

    def __init__(self):
        self.m = joblib.load(MODEL_DIR / "discovery_models.joblib")
        self.d = Discoverer.__new__(Discoverer)
        self.d.style_words = self.m["style_words"]

    def facets(self, stem: str, context: str = "") -> dict:
        """Facette de consigne et de support d'un texte nouveau, avec le rang de chaque facette
        (0 = la plus proche) pour juger d'une correspondance approchée."""
        stem, context = neutral(stem), neutral(context)
        ws = rownorm(self.m["snmf"].transform(self.m["svec"].transform([self.d.style_text(stem)])))
        wu = rownorm(self.m["unmf"].transform(self.m["uvec"].transform([shape_tokens(context[-700:] + "\nNL\n" + stem)])))
        rc = np.argsort(self.m["kms"].transform(ws)[0])
        ru = np.argsort(self.m["kmu"].transform(wu)[0])
        return {"consigne": int(rc[0]), "support": int(ru[0]),
                "rang_consigne": {int(f): i for i, f in enumerate(rc)}, "rang_support": {int(f): i for i, f in enumerate(ru)}}

    def plausibility(self, notion: str, c: int, s: int, pos: int) -> float:
        return float(self.m["plaus"].predict_proba(np.array([[notion, f"c{c}", f"s{s}", f"p{pos}"]], dtype=object))[0, 1])


def run():
    d = Discoverer()
    d.run()
    return d


if __name__ == "__main__":
    run()
