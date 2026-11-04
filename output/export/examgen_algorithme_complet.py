# examgen — code complet de l'algorithme
# 35 fichiers. Chaque fichier commence par une ligne « # ===== chemin ===== ».

# ===== examgen/__init__.py =====
# Les jeux de données sont petits : plusieurs threads OpenMP se gênent (jusqu'à 300 fois plus lent).
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
try:
    from threadpoolctl import threadpool_limits

    threadpool_limits(1)
except ImportError:
    pass


# ===== examgen/analysis.py =====
"""Analyse des annales et du cours : 14 modèles qui extraient la logique des épreuves.

 1. Espace sémantique commun questions + cours (TF-IDF -> LSA)
 2. Correspondance notion <-> sections du cours, poids de chaque notion dans le cours
 3. Archétypes de questions (forme, indépendante du thème) : KMeans, k choisi par silhouette
 4. Affinité notion x archétype  P(archétype | notion)
 5. Chaîne de Markov des enchaînements d'archétypes et de niveaux de Bloom dans un exercice
 6. Graphe de co-occurrence des notions (PMI), centralité, communautés = blocs thématiques cachés
 7. Modèle de difficulté (Gradient Boosting sur la position relative) + importances
 8. Facteurs latents (SVD sur les variables) + règles d'association (lift)
 9. Tendances par année et prévision pondérée par récence ; écarts cours/épreuves
10. Comparaison des régimes 2021-22 / 2023+ (chi2, Jensen-Shannon)
11. Logique de construction d'un sujet (diversité des domaines, courbe de Bloom, barèmes)
12. Scénarios / contextes d'exercice (NMF sur les préambules)
13. Questions atypiques (Isolation Forest)
14. Classifieur texte -> notions (sert au validateur) + typologie de l'épreuve pratique
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from itertools import combinations

import joblib
import networkx as nx
import numpy as np
from scipy.spatial.distance import jensenshannon
from scipy import sparse
from scipy.stats import chi2_contingency
from sklearn.cluster import KMeans
from sklearn.decomposition import NMF, TruncatedSVD
from sklearn.ensemble import GradientBoostingRegressor, IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, silhouette_score
from sklearn.model_selection import GroupKFold, cross_val_predict
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler

from . import features as F
from .config import CORPUS, MODEL_DIR, SEED
from .ingest import read_jsonl

STOP = set("""
a au aux avec ce ces cet cette dans de des du elle en et eux il ils je la le les leur leurs lui ma mais me meme mes moi mon ne nos notre nous on ou par pas pour qu que qui sa se ses son sur ta te tes toi ton tu un une vos votre vous c d j l m n s t y est sont ete etre avoir a ont fait faire peut peuvent doit doivent sera seront cela ceci celle celui ceux si dont donc ainsi alors plus moins tres tout tous toute toutes chaque autre autres entre sans sous lors puis afin comme deja encore ici la-dessus suivant suivante suivantes suivants ci dessous dessus question questions exercice partie on considere soit soient
""".split())


def tok(s: str) -> str:
    return F.norm(s)


def tfidf(**kw) -> TfidfVectorizer:
    return TfidfVectorizer(preprocessor=tok, stop_words=list(STOP), token_pattern=r"(?u)\b[a-z_][a-z0-9_]+\b", **kw)


def smooth_dist(counter: Counter, keys: list, alpha: float = 0.5) -> dict:
    tot = sum(counter.get(k, 0) for k in keys) + alpha * len(keys)
    return {k: (counter.get(k, 0) + alpha) / tot for k in keys}


class Analyzer:
    def __init__(self):
        self.exams = read_jsonl(CORPUS / "exams.jsonl")
        self.course = read_jsonl(CORPUS / "course.jsonl")
        self.written = [e for e in self.exams if e["type"] == "ecrit"]
        self.practical = [e for e in self.exams if e["type"] == "pratique"]
        self.rows = F.build_question_table(self.written)
        for r in self.rows:
            r["main"] = F.main_concepts(r)
        self.report: dict = {"corpus": {
            "sujets_ecrits": len(self.written), "sujets_pratiques": len(self.practical),
            "questions_ecrit": len(self.rows),
            "exercices_ecrit": sum(len(e["exercises"]) for e in self.written),
            "exercices_pratique": sum(len(e["exercises"]) for e in self.practical),
            "sections_cours": len(self.course),
            "annees": dict(sorted(Counter(e["year"] for e in self.written).items())),
            "centres": dict(Counter(e["center"] or "?" for e in self.written).most_common()),
        }}
        self.art: dict = {}

    # ------------------------------------------------------------------ 1. espace commun
    def semantic_space(self):
        q_texts = [r["text"] + "\n" + r["context"][-400:] for r in self.rows]
        c_texts = [s["title"] + "\n" + s["text"] for s in self.course]
        self.vec = tfidf(ngram_range=(1, 2), min_df=2, max_df=0.5, sublinear_tf=True, max_features=60000)
        self.vec.fit(q_texts + c_texts)
        self.Xq = self.vec.transform(q_texts)
        self.Xc = self.vec.transform(c_texts)
        self.svd = TruncatedSVD(n_components=150, random_state=SEED).fit(self.vec.transform(q_texts + c_texts))
        self.Lq = self.svd.transform(self.Xq)
        self.Lc = self.svd.transform(self.Xc)
        self.Lq /= np.linalg.norm(self.Lq, axis=1, keepdims=True) + 1e-9
        self.Lc /= np.linalg.norm(self.Lc, axis=1, keepdims=True) + 1e-9
        self.report["espace_semantique"] = {
            "vocabulaire": len(self.vec.vocabulary_),
            "variance_expliquee_LSA_150": round(float(self.svd.explained_variance_ratio_.sum()), 3),
        }

    # ------------------------------------------------------------------ 2. cours <-> notions
    def course_mapping(self):
        sec_hits = [F.concept_hits(s["title"] + " " + s["text"]) for s in self.course]
        course_weight = Counter()
        for h in sec_hits:
            for c, n in h.items():
                course_weight[c] += np.log1p(n)
        exam_weight = Counter(c for r in self.rows for c in r["main"][:2])
        cw = smooth_dist(course_weight, F.CONCEPT_NAMES, 0.1)
        ew = smooth_dist(exam_weight, F.CONCEPT_NAMES, 0.1)
        concept_sections, concept_centroid = {}, {}
        for c in F.CONCEPT_NAMES:
            idx = [i for i, r in enumerate(self.rows) if c in r["main"][:2]]
            if idx:
                cen = self.Lq[idx].mean(0)
                cen /= np.linalg.norm(cen) + 1e-9
            else:
                cen = np.zeros(self.Lq.shape[1])
            concept_centroid[c] = cen
            sim = self.Lc @ cen
            lex = np.array([np.log1p(h.get(c, 0)) for h in sec_hits])
            score = sim + 0.25 * lex / (lex.max() + 1e-9)
            concept_sections[c] = [int(i) for i in np.argsort(-score)[:6]]
        gaps = sorted(((c, cw[c] - ew[c]) for c in F.CONCEPT_NAMES), key=lambda t: -t[1])
        self.art.update(concept_sections=concept_sections, course_share=cw, exam_share=ew,
                        concept_centroid={c: v.tolist() for c, v in concept_centroid.items()})
        self.report["cours_vs_epreuves"] = {
            "sous_evaluees_par_rapport_au_cours": [(c, round(g, 4)) for c, g in gaps[:10]],
            "sur_evaluees_par_rapport_au_cours": [(c, round(g, 4)) for c, g in gaps[-10:]][::-1],
            "sections_du_cours_par_notion": {
                c: [f"{self.course[i]['chapter']} > {self.course[i]['lesson']} > {self.course[i]['title']}"[:110]
                    for i in v[:3]] for c, v in concept_sections.items()},
        }

    # ------------------------------------------------------------------ 3. archétypes
    def archetypes(self):
        Xf, names = F.feature_matrix(self.rows)
        form_cols = [i for i, n in enumerate(names) if not n.startswith("concept=")]
        stems = [" ".join(F.norm(r["text"]).split()[:18]) for r in self.rows]
        self.stem_vec = tfidf(ngram_range=(1, 3), min_df=3, max_df=0.6, sublinear_tf=True)
        S = self.stem_vec.fit_transform(stems)
        self.stem_svd = TruncatedSVD(n_components=25, random_state=SEED).fit(S)
        St = self.stem_svd.transform(S)
        self.form_scaler = StandardScaler().fit(Xf[:, form_cols])
        Z = np.hstack([self.form_scaler.transform(Xf[:, form_cols]), 3.0 * St / (np.linalg.norm(St, axis=1, keepdims=True) + 1e-9)])
        self.form_cols, self.feat_names = form_cols, names
        rng = np.random.RandomState(SEED)
        sample = rng.choice(len(Z), size=min(1500, len(Z)), replace=False)
        best = None
        sil = {}
        for k in range(10, 31, 2):
            km = KMeans(n_clusters=k, n_init=8, random_state=SEED).fit(Z)
            s = silhouette_score(Z[sample], km.labels_[sample])
            sil[k] = round(float(s), 4)
            # léger bonus de granularité : on veut des archétypes assez fins pour générer
            if best is None or s + 0.002 * k > best[0]:
                best = (s + 0.002 * k, k, km)
        _, k, km = best
        self.km = km
        labels = km.labels_
        for r, l in zip(self.rows, labels):
            r["arch"] = int(l)
        inv = {v: k for k, v in self.stem_vec.vocabulary_.items()}
        arch_info = {}
        for a in range(k):
            members = [r for r in self.rows if r["arch"] == a]
            Sm = np.asarray(S[[i for i, r in enumerate(self.rows) if r["arch"] == a]].mean(0)).ravel()
            top_ng = [inv[i] for i in np.argsort(-Sm)[:6]]
            task = Counter(r["task"] for r in members).most_common(2)
            fmt = Counter(f for r in members for f in r["formats"]).most_common(2)
            bl = Counter(r["bloom_name"] for r in members).most_common(1)[0][0]
            conc = Counter(c for r in members for c in r["main"][:1]).most_common(4)
            cen_d = np.linalg.norm(Z[labels == a] - km.cluster_centers_[a], axis=1)
            proto = [members[i]["text"][:260] for i in np.argsort(cen_d)[:3]]
            name = f"{task[0][0]} / {fmt[0][0]} / {bl}"
            arch_info[a] = {
                "nom": name, "effectif": len(members), "taches": task, "formats": fmt, "bloom": bl,
                "bloom_moyen": round(float(np.mean([r["bloom"] for r in members])), 2),
                "position_moyenne": round(float(np.mean([r["rel_pos"] for r in members])), 2),
                "avec_code": round(float(np.mean([r["has_code"] for r in members])), 2),
                "depend_d_avant": round(float(np.mean([r["n_deps"] > 0 for r in members])), 2),
                "notions_frequentes": conc, "formulations": top_ng, "prototypes": proto,
            }
        self.arch_info = arch_info
        self.report["archetypes"] = {"k_choisi": k, "silhouette_par_k": sil, "detail": arch_info}

    def arch_features(self, rows: list[dict]) -> np.ndarray:
        Xf, _ = F.feature_matrix(rows)
        stems = [" ".join(F.norm(r["text"]).split()[:18]) for r in rows]
        St = self.stem_svd.transform(self.stem_vec.transform(stems))
        return np.hstack([self.form_scaler.transform(Xf[:, self.form_cols]),
                          3.0 * St / (np.linalg.norm(St, axis=1, keepdims=True) + 1e-9)])

    # ------------------------------------------------------------------ 4. affinité notion x archétype
    def concept_archetype(self):
        k = self.km.n_clusters
        ci = {c: i for i, c in enumerate(F.CONCEPT_NAMES)}
        C = np.zeros((len(F.CONCEPT_NAMES), k))
        for r in self.rows:
            for w, c in zip((1.0, 0.5), r["main"][:2]):
                C[ci[c], r["arch"]] += w
        prior = np.bincount([r["arch"] for r in self.rows], minlength=k) / len(self.rows)
        # Lissage hiérarchique (bayésien) : une notion rare emprunte le profil de son domaine,
        # lui-même lissé vers le profil global. Évite qu'une notion vue 4 fois reçoive des formes au hasard.
        dom = {d: np.zeros(k) for d, _ in F.CONCEPTS.values()}
        for c, (d, _) in F.CONCEPTS.items():
            dom[d] += C[ci[c]]
        dom = {d: (v + 10 * prior) / (v.sum() + 10) for d, v in dom.items()}
        M = np.array([C[ci[c]] + 6 * dom[F.CONCEPTS[c][0]] for c in F.CONCEPT_NAMES])
        P = M / M.sum(1, keepdims=True)
        lift = P / (prior + 1e-9)
        self.art["concept_arch"] = P.tolist()
        self.report["affinite_notion_archetype"] = {
            c: [(self.arch_info[int(a)]["nom"], round(float(lift[ci[c], a]), 2)) for a in np.argsort(-lift[ci[c]])[:3]]
            for c in F.CONCEPT_NAMES if sum(c in r["main"][:2] for r in self.rows) >= 8}

    # ------------------------------------------------------------------ 5. Markov
    def markov(self):
        k = self.km.n_clusters
        T = np.full((k + 1, k + 1), 0.2)  # index k = START (ligne) / END (colonne)
        B = np.full((7, 7), 0.2)          # Bloom 0 = START
        by_ex = defaultdict(list)
        for r in self.rows:
            by_ex[(r["exam_id"], r["exercise"])].append(r)
        lengths = Counter()
        for seq in by_ex.values():
            seq.sort(key=lambda r: r["pos"])
            lengths[len(seq)] += 1
            prev, pb = k, 0
            for r in seq:
                T[prev, r["arch"]] += 1
                B[pb, r["bloom"]] += 1
                prev, pb = r["arch"], r["bloom"]
            T[prev, k] += 1
        T /= T.sum(1, keepdims=True)
        B /= B.sum(1, keepdims=True)
        # entropie du chaînage : faible = enchaînement très codifié
        H = -(T * np.log2(T)).sum(1)
        stat = np.linalg.matrix_power(T[:k, :k] / T[:k, :k].sum(1, keepdims=True), 50)[0]
        self.art.update(markov=T.tolist(), bloom_markov=B.tolist(),
                        ex_lengths={str(a): b for a, b in lengths.items()})
        top_tr = []
        for a in range(k):
            for b in range(k):
                if T[a, b] > 0.18:
                    top_tr.append((self.arch_info[a]["nom"], self.arch_info[b]["nom"], round(float(T[a, b]), 2)))
        self.report["markov"] = {
            "ouvertures_frequentes": [(self.arch_info[int(a)]["nom"], round(float(T[k, a]), 3)) for a in np.argsort(-T[k, :k])[:5]],
            "fermetures_frequentes": [(self.arch_info[int(a)]["nom"], round(float(T[a, k]), 3)) for a in np.argsort(-T[:k, k])[:5]],
            "transitions_fortes": sorted(top_tr, key=lambda t: -t[2])[:20],
            "entropie_moyenne_bits": round(float(H.mean()), 2),
            "bloom_transition": {f"{a}->{b}": round(float(B[a, b]), 2) for a in range(7) for b in range(1, 7) if B[a, b] > 0.25},
            "distribution_stationnaire_top": [(self.arch_info[int(a)]["nom"], round(float(stat[a]), 3)) for a in np.argsort(-stat)[:6]],
        }

    # ------------------------------------------------------------------ 6. graphe des notions
    def concept_graph(self):
        ex_sets = []
        for e in self.written:
            for x in e["exercises"]:
                rs = [r for r in self.rows if r["exam_id"] == e["id"] and r["exercise"] == x["number"]]
                if not rs:
                    continue
                sc = Counter(c for r in rs for c in r["main"])
                for c in F.concept_hits(x.get("theme_sentence") or ""):
                    sc[c] += 3
                tot = sum(sc.values())
                s = {c for c, n in sc.items() if n / tot >= 0.06 and c not in F.GENERIC}
                ex_sets.append((e, x, s))
        self.ex_sets = ex_sets
        N = len(ex_sets)
        cnt = Counter(c for _, _, s in ex_sets for c in s)
        pair = Counter(p for _, _, s in ex_sets for p in combinations(sorted(s), 2))
        G = nx.Graph()
        for c, n in cnt.items():
            G.add_node(c, freq=n)
        pmi = {}
        for (a, b), n in pair.items():
            if n < 3:  # une association vue 1-2 fois n'est pas une loi
                continue
            v = np.log((n * N) / (cnt[a] * cnt[b]))
            pmi[f"{a}|{b}"] = round(float(v), 3)
            if v > 0:
                G.add_edge(a, b, weight=float(v) * n, pmi=float(v), n=n)
        cen = nx.pagerank(G, weight="weight") if G.number_of_edges() else {}
        btw = nx.betweenness_centrality(G, weight=None) if G.number_of_edges() else {}
        comms = list(nx.algorithms.community.greedy_modularity_communities(G, weight="weight")) if G.number_of_edges() else []
        self.art.update(pmi=pmi, concept_freq_ex=dict(cnt), n_ex=N)
        self.G = G
        self.report["graphe_notions"] = {
            "exercices": N,
            "notions_par_exercice_moyenne": round(float(np.mean([len(s) for _, _, s in ex_sets])), 2),
            "associations_fortes_PMI": sorted(((k, v, pair[tuple(k.split("|"))]) for k, v in pmi.items() if pair[tuple(k.split("|"))] >= 3), key=lambda t: -t[1])[:20],
            "notions_pivots_pagerank": sorted(((c, round(v, 3)) for c, v in cen.items()), key=lambda t: -t[1])[:10],
            "notions_ponts_betweenness": sorted(((c, round(v, 3)) for c, v in btw.items()), key=lambda t: -t[1])[:8],
            "blocs_thematiques_caches": [sorted(c) for c in comms],
        }

    # ------------------------------------------------------------------ 7. difficulté
    def difficulty(self):
        X, names = F.feature_matrix(self.rows)
        keep = [i for i, n in enumerate(names) if n not in ("rel_pos",)]
        Xd = np.hstack([X[:, keep], self.Lq[:, :30]])
        dnames = [names[i] for i in keep] + [f"lsa{i}" for i in range(30)]
        y = np.array([r["rel_pos"] for r in self.rows])
        groups = [r["exam_id"] for r in self.rows]
        gb = GradientBoostingRegressor(n_estimators=300, max_depth=3, learning_rate=0.05, subsample=0.8, random_state=SEED)
        pred = cross_val_predict(gb, Xd, y, cv=GroupKFold(5), groups=groups)
        r2 = 1 - ((pred - y) ** 2).sum() / ((y - y.mean()) ** 2).sum()
        gb.fit(Xd, y)
        pi = permutation_importance(gb, Xd, y, n_repeats=5, random_state=SEED)
        imp = sorted(zip(dnames, pi.importances_mean), key=lambda t: -t[1])
        # effet de chaque variable binaire sur la position (où la placent les concepteurs)
        eff = []
        for j, n in enumerate(names):
            if n == "rel_pos":
                continue
            col = X[:, j]
            if set(np.unique(col)) <= {0, 1} and 25 <= col.sum() <= len(col) - 25:
                eff.append((n, round(float(y[col == 1].mean() - y[col == 0].mean()), 3), int(col.sum())))
        eff.sort(key=lambda t: t[1])
        self.gb, self.gb_keep = gb, keep
        self.report["difficulte"] = {
            "cible": "position relative dans l'exercice (0 = début, 1 = fin), proxy de difficulté",
            "R2_validation_croisee_par_sujet": round(float(r2), 3),
            "variables_les_plus_predictives": [(n, round(float(v), 4)) for n, v in imp[:15]],
            "placees_en_debut": eff[:10], "placees_en_fin": eff[-10:][::-1],
        }

    def predict_position(self, rows: list[dict], L: np.ndarray) -> np.ndarray:
        X, _ = F.feature_matrix(rows)
        return self.gb.predict(np.hstack([X[:, self.gb_keep], L[:, :30]]))

    # ------------------------------------------------------------------ 8. facteurs latents + règles
    def latent_factors(self):
        X, names = F.feature_matrix(self.rows)
        Xs = StandardScaler().fit_transform(X)
        svd = TruncatedSVD(n_components=8, random_state=SEED).fit(Xs)
        factors = []
        for i, comp in enumerate(svd.components_):
            o = np.argsort(comp)
            factors.append({
                "facteur": i + 1, "variance": round(float(svd.explained_variance_ratio_[i]), 3),
                "pole_positif": [names[j] for j in o[::-1][:6]], "pole_negatif": [names[j] for j in o[:6]],
            })
        B = (X > 0).astype(int)
        bin_cols = [j for j, n in enumerate(names) if set(np.unique(X[:, j])) <= {0, 1} or n.startswith(("bloom=", "task=", "format=", "concept="))]
        sup = B.mean(0)
        rules = []
        for a, b in combinations(bin_cols, 2):
            if names[a].split("=")[0] == names[b].split("=")[0] and "=" in names[a]:
                continue
            sab = (B[:, a] & B[:, b]).mean()
            if sab < 0.02:
                continue
            lift = sab / (sup[a] * sup[b] + 1e-9)
            if lift > 1.8:
                rules.append((names[a], names[b], round(float(sab), 3), round(float(lift), 2),
                              round(float(sab / sup[a]), 2), round(float(sab / sup[b]), 2)))
        rules.sort(key=lambda t: -t[3])
        self.report["facteurs_latents"] = factors
        self.report["regles_association"] = {
            "colonnes": "A, B, support, lift, P(B|A), P(A|B)", "regles": rules[:35]}

    # ------------------------------------------------------------------ 9. tendances
    def trends(self):
        years = sorted({e["year"] for e, _, _ in self.ex_sets if e["year"]})
        share = {c: [] for c in F.CONCEPT_NAMES}
        for y in years:
            sets = [s for e, _, s in self.ex_sets if e["year"] == y]
            for c in F.CONCEPT_NAMES:
                share[c].append(sum(c in s for s in sets) / max(len(sets), 1))
        last = max(years)
        w = np.array([0.5 ** ((last - y) / 1.5) for y in years])
        forecast, slopes = {}, {}
        for c in F.CONCEPT_NAMES:
            v = np.array(share[c])
            forecast[c] = float((v * w).sum() / w.sum())
            slopes[c] = float(np.polyfit(years, v, 1)[0]) if len(years) > 2 else 0.0
        self.art.update(forecast=forecast, slopes=slopes, years=years)
        self.report["tendances"] = {
            "annees": years,
            "en_hausse": sorted(((c, round(s, 3)) for c, s in slopes.items()), key=lambda t: -t[1])[:8],
            "en_baisse": sorted(((c, round(s, 3)) for c, s in slopes.items()), key=lambda t: t[1])[:8],
            "probabilite_attendue_par_exercice": sorted(((c, round(v, 3)) for c, v in forecast.items()), key=lambda t: -t[1])[:15],
            "part_par_annee": {c: [round(x, 2) for x in share[c]] for c in F.CONCEPT_NAMES if max(share[c]) > 0.08},
        }

    # ------------------------------------------------------------------ 10. régimes
    def regimes(self):
        regs = sorted({r["regime"] for r in self.rows})
        tab = np.array([[sum(1 for r in self.rows if r["regime"] == g and r["main"] and r["main"][0] == c) for c in F.CONCEPT_NAMES] for g in regs]) + 0.5
        chi2, p, dof, _ = chi2_contingency(tab)
        js = jensenshannon(tab[0] / tab[0].sum(), tab[1] / tab[1].sum()) if len(regs) > 1 else 0
        comp = {}
        for g in regs:
            rs = [r for r in self.rows if r["regime"] == g]
            exs = {(r["exam_id"], r["exercise"]) for r in rs}
            comp[g] = {
                "questions": len(rs), "questions_par_exercice": round(len(rs) / len(exs), 1),
                "bloom_moyen": round(float(np.mean([r["bloom"] for r in rs])), 2),
                "part_ecrire_code": round(float(np.mean([r["task"] in ("ecrire_fonction", "completer_code") for r in rs])), 3),
                "part_sql": round(float(np.mean([r["has_sql"] or "sql" in r["formats"] for r in rs])), 3),
                "part_dependances": round(float(np.mean([r["n_deps"] > 0 for r in rs])), 3),
                "mots_par_question": round(float(np.mean([r["len_words"] for r in rs])), 1),
            }
        self.report["regimes"] = {"chi2": round(float(chi2), 1), "p_value": float(p), "jensen_shannon": round(float(js), 3), "comparaison": comp}

    # ------------------------------------------------------------------ 11. logique d'un sujet
    def exam_logic(self):
        dom = {c: d for c, (d, _) in F.CONCEPTS.items()}
        overlaps, rnd = [], []
        all_dom_sets = []
        by_exam = defaultdict(list)
        for e, x, s in self.ex_sets:
            ds = {dom[c] for c in s}
            by_exam[e["id"]].append(ds)
            all_dom_sets.append(ds)
        rng = np.random.RandomState(SEED)
        for sets in by_exam.values():
            for a, b in combinations(sets, 2):
                if a and b:
                    overlaps.append(len(a & b) / len(a | b))
                    i, j = rng.choice(len(all_dom_sets), 2, replace=False)
                    A, Bs = all_dom_sets[i], all_dom_sets[j]
                    if A and Bs:
                        rnd.append(len(A & Bs) / len(A | Bs))
        cover = [len(set().union(*s)) for s in by_exam.values()]
        deciles = defaultdict(list)
        for r in self.rows:
            deciles[min(int(r["rel_pos"] * 5), 4)].append(r)
        curve = {f"{i*20}-{i*20+20}%": {
            "bloom": round(float(np.mean([r["bloom"] for r in v])), 2),
            "code": round(float(np.mean([r["task"] in ("ecrire_fonction", "completer_code") for r in v])), 2),
            "dependance": round(float(np.mean([r["n_deps"] > 0 for r in v])), 2),
            "mots": round(float(np.mean([r["len_words"] for r in v])), 1)} for i, v in sorted(deciles.items())}
        pts = Counter(x.get("points") for e in self.written for x in e["exercises"] if x.get("points"))
        dom_pairs = Counter()
        for sets in by_exam.values():
            u = set().union(*sets)
            for p in combinations(sorted(u), 2):
                dom_pairs[p] += 1
        self.art["ex_points"] = {str(k): v for k, v in pts.items()}
        self.report["logique_des_sujets"] = {
            "recouvrement_domaines_entre_exercices_d_un_sujet": round(float(np.mean(overlaps)), 3),
            "recouvrement_si_exercices_tires_au_hasard": round(float(np.mean(rnd)), 3),
            "lecture": "plus bas que le hasard = les concepteurs répartissent les domaines entre exercices",
            "domaines_couverts_par_sujet_moyenne": round(float(np.mean(cover)), 2),
            "courbe_dans_un_exercice": curve,
            "baremes_exercices": dict(pts.most_common()),
            "domaines_souvent_reunis_dans_un_sujet": [(" + ".join(p), n) for p, n in dom_pairs.most_common(8)],
        }

    # ------------------------------------------------------------------ 12. scénarios
    def scenarios(self):
        pre = []
        meta = []
        for e, x, s in self.ex_sets:
            t = (x["preamble"] or "")[:1500]
            if len(t.split()) > 25:
                pre.append(t)
                meta.append((e["id"], x["number"], sorted(s)))
        nsi_words = set()
        for _, rx in F.CONCEPTS.values():
            nsi_words |= set(re.findall(r"[a-z]{4,}", rx))
        vec = tfidf(min_df=3, max_df=0.15, max_features=6000)
        vec.stop_words = list(STOP | nsi_words | {"python", "fonction", "programme", "code", "valeur", "donnees", "exemple", "ligne", "lignes", "elements", "element", "nombre", "liste", "table", "tableau"})
        X = vec.fit_transform(pre)
        nmf = NMF(n_components=18, random_state=SEED, init="nndsvda", max_iter=600).fit(X)
        W = nmf.transform(X)
        inv = vec.get_feature_names_out()
        topics = []
        for t, comp in enumerate(nmf.components_):
            words = [inv[i] for i in np.argsort(-comp)[:8]]
            ex = [meta[i] for i in np.argsort(-W[:, t])[:3]]
            conc = Counter(c for i in np.argsort(-W[:, t])[:15] for c in meta[i][2]).most_common(3)
            topics.append({"mots": words, "notions_associees": conc, "exemples": [f"{a}#ex{b}" for a, b, _ in ex]})
        self.art["scenarios"] = topics
        self.report["scenarios"] = topics

    # ------------------------------------------------------------------ 13. atypiques
    def anomalies(self):
        X, _ = F.feature_matrix(self.rows)
        Z = np.hstack([StandardScaler().fit_transform(X), self.Lq[:, :20] * 3])
        iso = IsolationForest(n_estimators=400, contamination=0.03, random_state=SEED).fit(Z)
        s = iso.score_samples(Z)
        idx = np.argsort(s)[:12]
        self.report["questions_atypiques"] = [
            {"annee": self.rows[i]["year"], "centre": self.rows[i]["center"], "tache": self.rows[i]["task"],
             "texte": self.rows[i]["text"][:220]} for i in idx]

    # ------------------------------------------------------------------ 14. classifieur + pratique
    def classifier(self):
        texts = [r["text"] + "\n" + r["context"][-300:] for r in self.rows]
        labels = [r["main"][:2] for r in self.rows]
        mlb = MultiLabelBinarizer(classes=F.CONCEPT_NAMES).fit(labels)
        Y = mlb.transform(labels)
        Xt = self.vec.transform(texts)
        clf = OneVsRestClassifier(LogisticRegression(C=8, max_iter=2000, class_weight="balanced"))
        groups = [r["exam_id"] for r in self.rows]
        cols = Y.sum(0) >= 5
        Pr = np.zeros(Y.shape)
        for tr, te in GroupKFold(5).split(Xt, Y, groups):
            m = OneVsRestClassifier(LogisticRegression(C=8, max_iter=2000, class_weight="balanced")).fit(Xt[tr], Y[tr][:, cols])
            Pr[np.ix_(te, np.where(cols)[0])] = m.predict_proba(Xt[te])
        top3 = np.argsort(-Pr, 1)[:, :3]
        hit = np.mean([Y[i, top3[i]].any() for i in range(len(Y)) if Y[i].any()])
        f1 = f1_score(Y[:, cols], (Pr[:, cols] > 0.5).astype(int), average="micro")
        # auto-apprentissage : la matière d'exposition (CodEx, QCM, cours et fiches d'enseignants)
        # sert d'entraînement supplémentaire (étiquettes lexicales), puis de pseudo-étiquettes pour
        # ce que le lexique ne reconnaît pas (prédictions sûres du modèle). Chaque variante n'est
        # gardée que si elle améliore le top-3 sur des sujets d'écrit tenus à l'écart.
        expo = read_jsonl(CORPUS / "exposure.jsonl") if (CORPUS / "exposure.jsonl").exists() else []
        er = F.build_question_table(expo)
        for r in er:
            r["main"] = F.main_concepts(r)
        Xe = self.vec.transform([r["text"] + "\n" + r["context"][-300:] for r in er]) if er else None
        Ye = mlb.transform([r["main"][:2] for r in er]) if er else None
        has = Ye.any(1) if er else None
        variants = {"base": (hit, f1, None)}
        if er:
            def cv_variant(pseudo: bool):
                Pv = np.zeros(Y.shape)
                for tr, te in GroupKFold(5).split(Xt, Y, groups):
                    XA, YA = sparse.vstack([Xt[tr], Xe[has]]), np.vstack([Y[tr], Ye[has]])
                    m = OneVsRestClassifier(LogisticRegression(C=8, max_iter=2000, class_weight="balanced")).fit(XA, YA[:, cols])
                    if pseudo:
                        P = m.predict_proba(Xe[~has])
                        conf = P.max(1) >= 0.8
                        YP = np.zeros((conf.sum(), Y.shape[1]), dtype=int)
                        YP[np.arange(conf.sum())[:, None], np.where(cols)[0][np.argsort(-P[conf], 1)[:, :1]]] = 1
                        m = OneVsRestClassifier(LogisticRegression(C=8, max_iter=2000, class_weight="balanced")).fit(
                            sparse.vstack([XA, Xe[~has][conf]]), np.vstack([YA, YP])[:, cols])
                    Pv[np.ix_(te, np.where(cols)[0])] = m.predict_proba(Xt[te])
                t3 = np.argsort(-Pv, 1)[:, :3]
                h = np.mean([Y[i, t3[i]].any() for i in range(len(Y)) if Y[i].any()])
                return h, f1_score(Y[:, cols], (Pv[:, cols] > 0.5).astype(int), average="micro")
            variants["exposition"] = (*cv_variant(False), None)
            variants["exposition+pseudo"] = (*cv_variant(True), None)
        best = max(variants, key=lambda k: variants[k][0])
        if best == "base":
            clf.fit(Xt, Y[:, cols])
        else:
            XA, YA = sparse.vstack([Xt, Xe[has]]), np.vstack([Y, Ye[has]])
            clf.fit(XA, YA[:, cols])
            if best == "exposition+pseudo":
                P = clf.predict_proba(Xe[~has])
                conf = P.max(1) >= 0.8
                YP = np.zeros((conf.sum(), Y.shape[1]), dtype=int)
                YP[np.arange(conf.sum())[:, None], np.where(cols)[0][np.argsort(-P[conf], 1)[:, :1]]] = 1
                clf = OneVsRestClassifier(LogisticRegression(C=8, max_iter=2000, class_weight="balanced")).fit(
                    sparse.vstack([XA, Xe[~has][conf]]), np.vstack([YA, YP])[:, cols])
        hit, f1 = variants[best][:2]
        self.clf, self.clf_classes = clf, [c for c, k in zip(F.CONCEPT_NAMES, cols) if k]
        self.report["classifieur_notions"] = {"top3_hit_rate_cv": round(float(hit), 3), "micro_f1_cv": round(float(f1), 3), "notions": len(self.clf_classes),
                                              "auto_apprentissage": {"variante_retenue": best, "unites_d_exposition": len(er),
                                                                     **{k: {"top3": round(float(v[0]), 3), "f1": round(float(v[1]), 3)} for k, v in variants.items()}}}
        print(f"  classifieur notions : {', '.join(f'{k}={v[0]:.3f}' for k, v in variants.items())} -> {best}")

    def practical_typology(self):
        exs = [(e, x) for e in self.practical for x in e["exercises"] if not x.get("duplicate_of_previous_year")]
        texts = [x["raw"] for _, x in exs]
        vec = tfidf(ngram_range=(1, 2), min_df=3, max_df=0.4, sublinear_tf=True)
        X = vec.fit_transform(texts)
        L = TruncatedSVD(n_components=40, random_state=SEED).fit_transform(X)
        L /= np.linalg.norm(L, axis=1, keepdims=True) + 1e-9
        km = KMeans(n_clusters=14, n_init=10, random_state=SEED).fit(L)
        inv = vec.get_feature_names_out()
        types = []
        for c in range(14):
            idx = np.where(km.labels_ == c)[0]
            m = np.asarray(X[idx].mean(0)).ravel()
            num = Counter(exs[i][1]["number"] for i in idx)
            conc = Counter(cc for i in idx for cc, _ in Counter(F.concept_hits(texts[i])).most_common(2)).most_common(3)
            types.append({"effectif": len(idx), "mots": [inv[i] for i in np.argsort(-m)[:7]],
                          "exercice_1_ou_2": dict(num), "notions": conc,
                          "exemple": texts[idx[0]][:240].replace("\n", " ")})
        types.sort(key=lambda t: -t["effectif"])
        self.art["practical_types"] = types
        self.report["epreuve_pratique"] = {
            "exercices_uniques": len(exs),
            "ex1_ecrire_algo_connu_vs_ex2_completer": "ex1 = écrire une fonction classique ; ex2 = compléter un code à trous",
            "typologie": types,
        }

    # ------------------------------------------------------------------ run + save
    def run(self):
        steps = [self.semantic_space, self.course_mapping, self.archetypes, self.concept_archetype, self.markov,
                 self.concept_graph, self.difficulty, self.latent_factors, self.trends, self.regimes,
                 self.exam_logic, self.scenarios, self.anomalies, self.classifier, self.practical_typology]
        for s in steps:
            print(f"  · {s.__name__}")
            s()
        self.save()

    def save(self):
        bundle = {k: getattr(self, k) for k in ("vec", "svd", "stem_vec", "stem_svd", "form_scaler", "form_cols", "km", "gb", "gb_keep", "clf", "clf_classes")}
        bundle["Lq"], bundle["Lc"] = self.Lq, self.Lc
        bundle["arch_info"] = self.arch_info
        joblib.dump(bundle, MODEL_DIR / "models.joblib", compress=3)
        slim_rows = [{k: r[k] for k in ("exam_id", "year", "center", "regime", "exercise", "label", "pos", "rel_pos", "text", "context",
                                        "bloom", "task", "formats", "main", "arch", "n_deps", "has_code", "ex_n_questions")} for r in self.rows]
        joblib.dump({"rows": slim_rows, "course": self.course, "art": self.art}, MODEL_DIR / "data.joblib", compress=3)
        (MODEL_DIR / "analysis.json").write_text(json.dumps(self.report, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
        print(f"[ok] modèles -> {MODEL_DIR}")


def run():
    a = Analyzer()
    a.run()
    return a


if __name__ == "__main__":
    run()


# ===== examgen/blueprint.py =====
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


# ===== examgen/cli.py =====
"""Point d'entrée.

  python -m examgen.cli ingest              # PDF / Markdown -> data/corpus
  python -m examgen.cli analyze             # 14 modèles -> data/model + rapport
  python -m examgen.cli plan --sujets 2 --par-notion 4
  python -m examgen.cli write --backend api|agents
  python -m examgen.cli validate
  python -m examgen.cli all                 # tout sauf la rédaction par agents
"""
from __future__ import annotations

import argparse
import json

from .config import OUT


def main():
    ap = argparse.ArgumentParser(prog="examgen")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ingest")
    sub.add_parser("analyze")
    p = sub.add_parser("plan")
    p.add_argument("--sujets", type=int, default=2)
    p.add_argument("--par-notion", type=int, default=4)
    p.add_argument("--seed", type=int, default=42)
    w = sub.add_parser("write")
    w.add_argument("--backend", choices=["api", "agents"], default="agents")
    sub.add_parser("discover")
    i = sub.add_parser("inedit")
    i.add_argument("--combinaisons", type=int, default=3)
    i.add_argument("--savoirs", type=int, default=1)
    sub.add_parser("validate")
    sub.add_parser("report")
    a = sub.add_parser("all")
    a.add_argument("--sujets", type=int, default=2)
    a.add_argument("--par-notion", type=int, default=4)
    args = ap.parse_args()

    if args.cmd in ("ingest", "all"):
        from . import ingest
        ingest.run()
    if args.cmd in ("analyze", "all"):
        from . import analysis, report
        analysis.run()
        report.run()
    if args.cmd == "report":
        from . import report
        report.run()
    if args.cmd in ("discover", "all"):
        from . import discovery
        discovery.run()
    if args.cmd == "inedit":
        from . import inedit, llm
        llm.export_prompts(inedit.make_plans(args.combinaisons, args.savoirs))
    if args.cmd in ("plan", "all"):
        from . import blueprint, llm
        plans = blueprint.make_plans(args.sujets, args.par_notion, getattr(args, "seed", 42))
        llm.export_prompts(plans)
    if args.cmd == "write":
        from . import llm
        plans = [p for n in ("plans.json", "plans_inedit.json") if (OUT / n).exists()
                 for p in json.loads((OUT / n).read_text(encoding="utf-8"))]
        if args.backend == "api":
            llm.generate_api(plans)
        else:
            llm.export_prompts(plans)
            print("Consignes prêtes : faire rédiger chaque output/prompts/<id>.md par un agent Opus 5.5 (effort low)"
                  " qui écrit output/generated/<id>.json au format output/prompts/_schema.json.")
    if args.cmd == "validate":
        from . import validate
        validate.run()
        validate.render_markdown()


if __name__ == "__main__":
    main()


# ===== examgen/config.py =====
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SOURCES = DATA / "sources"
CORPUS = DATA / "corpus"      # textes extraits (jsonl)
MODEL_DIR = DATA / "model"    # artefacts d'analyse (joblib / json)
OUT = ROOT / "output"         # plans de questions + questions générées

for p in (CORPUS, MODEL_DIR, OUT):
    p.mkdir(parents=True, exist_ok=True)

# Modèle LLM qui rédige les questions (choix de l'utilisateur : Opus 5.5, effort low)
LLM_MODEL = "claude-opus-5-5"
LLM_EFFORT = "low"

SEED = 42


# ===== examgen/discovery.py =====
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
from sklearn.metrics import f1_score, silhouette_score
from .fast import auc as roc_auc_score
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


def stable_kmeans(Z, ks, seed=SEED, n_boot=6, min_stab=0.6, sample=4000, label=""):
    """Facettes auto-corrigées. Pour chaque k candidat : KMeans complet + KMeans sur des
    sous-échantillons ; la stabilité d'une facette est le Jaccard moyen avec la facette la plus
    proche des réplicats (Hennig, clusterboot). Le k retenu maximise silhouette × stabilité.
    Puis on dissout une fois les facettes instables (stabilité < min_stab) : leurs questions vont à la
    facette stable la plus proche et on réajuste. Un seul tour : dissoudre en cascade faisait
    s'effondrer le découpage (20 -> 6 facettes) ; celles qui restent instables sont seulement
    marquées fragiles et écartées à la génération."""
    rng = np.random.default_rng(seed)
    sub = rng.choice(len(Z), min(sample, len(Z)), replace=False)

    def stability(km):
        lab = km.predict(Z[sub])
        per = np.zeros(km.n_clusters)
        for b in range(n_boot):
            bi = rng.choice(len(sub), int(0.8 * len(sub)), replace=False)
            kb = KMeans(km.n_clusters, n_init=3, random_state=seed + 100 + b).fit(Z[sub][bi])
            lb = kb.labels_
            la = lab[bi]
            for f in range(km.n_clusters):
                A = la == f
                if not A.any():
                    continue
                per[f] += max((A & (lb == g)).sum() / max((A | (lb == g)).sum(), 1) for g in range(km.n_clusters)) / n_boot
        return per

    trials = {}
    for k in ks:
        km = KMeans(k, n_init=4, random_state=seed).fit(Z[sub])
        sil = silhouette_score(Z[sub], km.labels_)
        st = stability(km)
        trials[k] = (float(sil), float(st.mean()), float(sil * st.mean()))
    bk = max(trials, key=lambda k: trials[k][2])
    km = KMeans(bk, n_init=8, random_state=seed).fit(Z)
    history = []
    for rnd in range(2):
        st = stability(km)
        history.append({"tour": rnd, "k": int(km.n_clusters), "stabilite_moyenne": round(float(st.mean()), 3),
                        "instables": int((st < min_stab).sum())})
        bad = st < min_stab
        if rnd == 1 or not bad.any() or km.n_clusters - bad.sum() < 4:
            break
        km = KMeans(int((~bad).sum()), init=km.cluster_centers_[~bad], n_init=1, random_state=seed).fit(Z)
    st = stability(km)
    sil = float(silhouette_score(Z[sub], km.predict(Z[sub])))
    print(f"    {label}: k={km.n_clusters} (essais {', '.join(f'{k}:{v[2]:.2f}' for k, v in trials.items())}) ; "
          f"stabilité {st.mean():.2f} ; tours {[h['k'] for h in history]}")
    return km, st, {"essais_k": {str(k): {"silhouette": round(v[0], 3), "stabilite": round(v[1], 3)} for k, v in trials.items()},
                    "auto_correction": history, "silhouette_finale": round(sil, 3),
                    "stabilite_finale": round(float(st.mean()), 3)}


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
        expo = read_jsonl(CORPUS / "exposure.jsonl") if (CORPUS / "exposure.jsonl").exists() else []
        groups = defaultdict(list)
        for e in expo:
            groups[e["type"]].append(e)
        self.u = []
        for src, ex in (("ecrit", written), ("pratique", practical), ("cours", fake), *sorted(groups.items())):
            for r in F.build_question_table(ex) if src != "cours" else self._course_rows(fake):
                r["src"] = src
                r["main"] = F.main_concepts(r)
                r["text"], r["context"] = neutral(r["text"]), neutral(r["context"])
                if r["text"].strip():
                    self.u.append(r)
        self.difficulty_of = {e["id"]: e["difficulty"] for e in expo if e.get("difficulty")}
        self.preambles = {}
        for e in written + practical + fake + expo:
            for x in e["exercises"]:
                self.preambles[(e["id"], x["number"])] = neutral((x.get("preamble") or "") + " " + (x.get("theme_sentence") or ""))
        self.course = read_jsonl(CORPUS / "course.jsonl")
        self.course_extra = read_jsonl(CORPUS / "course_extra.jsonl") if (CORPUS / "course_extra.jsonl").exists() else []
        self.rep = {}
        self.clean_exposure()
        self.W_idx = [i for i, r in enumerate(self.u) if r["src"] == "ecrit"]
        self.rep["corpus_d_exposition"] = dict(Counter(r["src"] for r in self.u))
        self.m: dict = {}
        print(f"  unités d'entraînement : {self.rep['corpus_d_exposition']}")

    # -------------------------------------------------------------- 0. auto-nettoyage de la matière
    def clean_exposure(self):
        """La matière ajoutée (CodEx, QCM, cours et fiches d'enseignants) est extraite automatiquement
        et contient du bruit : paragraphes d'explication pris pour des consignes, conseils, titres.
        Le modèle apprend seul ce qu'est une question : positifs = vraies questions d'épreuve,
        négatifs = phrases explicatives du cours. Les unités d'exposition qu'il juge être du cours
        plutôt qu'une question sont écartées. Seuil choisi par validation croisée (F1 max)."""
        pos = [r["text"] for r in self.u if r["src"] in ("ecrit", "pratique")]
        neg = []
        for s_ in self.course:
            for para in re.split(r"\n\s*\n", neutral(s_["text"])):
                para = re.sub(r"\s+", " ", para).strip()
                if 40 <= len(para) <= 600 and is_prose(para) and "?" not in para:
                    neg.append(para)
        rng = np.random.default_rng(SEED)
        neg = [neg[i] for i in rng.choice(len(neg), min(len(neg), 2 * len(pos)), replace=False)]
        txt = pos + neg
        y = np.r_[np.ones(len(pos)), np.zeros(len(neg))]
        vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4), min_df=5, sublinear_tf=True, max_features=60000)
        X = vec.fit_transform([F.norm(t[:300]) for t in txt])
        best = None
        for C in (0.3, 1.0, 3.0):
            p = cross_val_predict(LogisticRegression(C=C, max_iter=3000), X, y, cv=5, method="predict_proba")[:, 1]
            auc = roc_auc_score(y, p)
            if best is None or auc > best[0]:
                best = (auc, C, p)
        auc, C, p = best
        thr = max(np.linspace(0.1, 0.9, 33), key=lambda t: f1_score(y, p >= t))
        clf = LogisticRegression(C=C, max_iter=3000).fit(X, y)
        ex = [i for i, r in enumerate(self.u) if r["src"] not in ("ecrit", "pratique")]
        q = clf.predict_proba(vec.transform([F.norm(self.u[i]["text"][:300]) for i in ex]))[:, 1]
        drop = {i for i, v in zip(ex, q) if v < thr}
        by = Counter(self.u[i]["src"] for i in ex)
        dropped = Counter(self.u[i]["src"] for i in drop)
        examples = [snippet(self.u[ex[j]]["text"], 140) for j in np.argsort(q)[:8]]
        self.u = [r for i, r in enumerate(self.u) if i not in drop]
        self.rep["auto_nettoyage"] = {
            "principe": "classifieur question / phrase de cours appris seul, seuil par F1 en validation croisée",
            "AUC_validation_croisee": round(float(auc), 3), "C_choisi": C, "seuil": round(float(thr), 3),
            "ecartees_par_source": {k: f"{dropped[k]}/{by[k]}" for k in by}, "exemples_ecartes": examples}
        print(f"    auto-nettoyage : AUC={auc:.3f}, {len(drop)} unités écartées sur {len(ex)} ({dict(dropped)})")

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
        # Les facettes décrivent la manière dont les SUJETS demandent : on les ajuste sur les questions
        # d'examen ; le reste du corpus d'exposition a déjà servi à apprendre le vocabulaire (NMF).
        ex = np.array([i for i, u in enumerate(self.u) if u["src"] in ("ecrit", "pratique")])
        Zs, Zu = rownorm(self.Ws), rownorm(self.Wu)
        self.kms, self.st_s, info_s = stable_kmeans(Zs[ex], [16, 20, 25, 30, 36], label="manières de demander")
        self.kmu, self.st_u, info_u = stable_kmeans(Zu[ex], [8, 12, 16, 20], label="types de support")
        s1, s2 = info_s["silhouette_finale"], info_u["silhouette_finale"]
        self.fs = self.kms.predict(Zs)
        self.fu = self.kmu.predict(Zu)

        def describe(km, W, fac, vars_, st):
            out = {}
            for f in range(km.n_clusters):
                idx = np.where(fac == f)[0]
                prof = km.cluster_centers_[f]
                comps = [vars_[j]["id"] for j in np.argsort(-prof)[:2]]
                w_idx = [i for i in idx if self.u[i]["src"] == "ecrit"]
                ex = sorted(idx, key=lambda i: -float((rownorm(W[i:i + 1]) @ prof)[0]))
                out[f] = {"effectif": int(len(idx)), "a_l_ecrit": len(w_idx), "stabilite": round(float(st[f]), 3),
                          "coherence_interne": round(float((rownorm(W[idx]) @ rownorm(prof[None])[0]).mean()), 3) if len(idx) else 0.0,
                          "part_ecrit": round(len(w_idx) / max(len(idx), 1), 2),
                          "composantes": comps, "termes": vars_[int(np.argmax(prof))]["termes"][:6],
                          "exemples": [snippet(self.u[i]["text"], 200) for i in ex[:3]],
                          "position_moyenne": round(float(np.mean([self.u[i]["rel_pos"] for i in w_idx])), 2) if w_idx else None,
                          "notions_frequentes": [c for c, _ in Counter(self.u[i]["main"][0] for i in idx if self.u[i]["main"]).most_common(4)]}
            return out
        self.style_facets = describe(self.kms, self.Ws, self.fs, self.vars["consigne"], self.st_s)
        self.support_facets = describe(self.kmu, self.Wu, self.fu, self.vars["support"], self.st_u)
        self.rep["facettes"] = {"manieres_de_demander": {"k": self.kms.n_clusters, "silhouette": round(s1, 3), **info_s},
                                "types_de_support": {"k": self.kmu.n_clusters, "silhouette": round(s2, 3), **info_u}}
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
        # réglage choisi seul (validation croisée par sujet) : force de régularisation et degré d'interaction
        trials = {}
        for deg in (1, 2):
            for C in (0.1, 0.3, 1.0, 3.0):
                pipe = make_pipeline(OneHotEncoder(handle_unknown="ignore"),
                                     *( [PolynomialFeatures(2, interaction_only=True, include_bias=False)] if deg == 2 else []),
                                     LogisticRegression(C=C, max_iter=3000))
                pp = cross_val_predict(pipe, X, y, groups=g, cv=GroupKFold(5), method="predict_proba")[:, 1]
                trials[(deg, C)] = (roc_auc_score(y, pp), pipe)
        (deg, C), (auc, self.plaus) = max(trials.items(), key=lambda kv: kv[1][0])
        self.rep["reglages_auto"] = {"plausibilite": {"degre_interactions": deg, "C": C,
                                                      "essais": {f"deg{d}_C{c}": round(float(v[0]), 3) for (d, c), v in trials.items()}}}
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
    def self_label_course(self):
        """Auto-apprentissage (self-training) : les sections de cours des enseignants n'ont pas de
        chapitre. Un classifieur appris sur le cours étiqueté leur en attribue un ; on n'ajoute que
        les étiquettes sûres, puis on vérifie sur des leçons tenues à l'écart que l'ajout améliore
        (ou ne dégrade pas) la précision. Sinon la matière ajoutée est refusée."""
        lab = [c for c in self.course if c["source"] != "BO"]
        if not self.course_extra:
            return
        y = np.array([c["chapter"] for c in lab])
        g = np.array([c["lesson"] for c in lab])
        vec = TfidfVectorizer(token_pattern=r"[a-z_][a-z_0-9]{2,}", ngram_range=(1, 2), min_df=2, max_df=0.4,
                              sublinear_tf=True, max_features=50000)
        vec.fit([F.norm(c["text"]) for c in lab + self.course_extra])
        XL = vec.transform([F.norm(c["title"] + " " + c["text"]) for c in lab])
        XU = vec.transform([F.norm(c["title"] + " " + c["text"]) for c in self.course_extra])
        base_acc, self_acc = [], []
        for tr, te in GroupKFold(5).split(XL, y, g):
            m0 = LogisticRegression(C=5, max_iter=3000, class_weight="balanced").fit(XL[tr], y[tr])
            base_acc.append((m0.predict(XL[te]) == y[te]).mean())
            P = m0.predict_proba(XU)
            ok = P.max(1) >= 0.7
            m1 = LogisticRegression(C=5, max_iter=3000, class_weight="balanced").fit(
                sparse.vstack([XL[tr], XU[ok]]), np.r_[y[tr], m0.classes_[P[ok].argmax(1)]])
            self_acc.append((m1.predict(XL[te]) == y[te]).mean())
        m0 = LogisticRegression(C=5, max_iter=3000, class_weight="balanced").fit(XL, y)
        P = m0.predict_proba(XU)
        ok = P.max(1) >= 0.7
        accept = np.mean(self_acc) >= np.mean(base_acc) - 0.01
        added = 0
        if accept:
            for c, k, pr in zip(self.course_extra, ok, P):
                if k:
                    self.course.append(dict(c, chapter=str(m0.classes_[pr.argmax()]), pseudo=True))
                    added += 1
        self.rep["auto_apprentissage_cours"] = {
            "sections_non_etiquetees": len(self.course_extra), "etiquetees_avec_confiance_0.7": int(ok.sum()),
            "precision_lecons_tenues_a_l_ecart_avant": round(float(np.mean(base_acc)), 3),
            "precision_apres_auto_apprentissage": round(float(np.mean(self_acc)), 3),
            "accepte": bool(accept), "sections_ajoutees": added,
            "repartition": dict(Counter(str(m0.classes_[p.argmax()]) for p, k in zip(P, ok) if k))}
        print(f"    auto-apprentissage du cours : {base_acc and np.mean(base_acc):.3f} -> {np.mean(self_acc):.3f} ; "
              f"{added} sections ajoutées")

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
        qtexts = [F.norm(self.u[i]["text"] + " " + self.u[i]["context"][-300:]) for i in range(len(self.u)) if self.u[i]["src"] in ("ecrit", "pratique")]
        qidx = [i for i in range(len(self.u)) if self.u[i]["src"] in ("ecrit", "pratique")]
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
        # difficulté externe : CodEx note chaque exercice (étiquette faible). Le modèle apprend cette
        # difficulté depuis les variables découvertes, puis on vérifie seul si elle prédit la
        # progression réelle dans les exercices d'écrit (validation croisée entre corpus).
        cdx = [i for i, r in enumerate(self.u) if r["src"] == "codex" and self.difficulty_of.get(r["exam_id"])]
        ext = {}
        if len(cdx) >= 50:
            Xd = np.hstack([rownorm(self.Ws)[cdx], rownorm(self.Wu)[cdx], rownorm(self.Wc)[cdx]])
            yd = np.log([self.difficulty_of[self.u[i]["exam_id"]] for i in cdx])
            gbd = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_leaf_nodes=10, random_state=SEED)
            pd_ = cross_val_predict(gbd, Xd, yd, cv=5)
            gbd.fit(Xd, yd)
            dW = gbd.predict(X)
            ext = {"exercices_codex": len(cdx), "rho_validation_croisee_codex": round(float(spearmanr(yd, pd_).correlation), 3),
                   "rho_difficulte_codex_predite_vs_position_ecrit": round(float(spearmanr(dW, y).correlation), 3)}
            r2_ext = r2_of(np.hstack([X, dW[:, None]]))
            ext["R2_position_avec_difficulte_codex"] = round(r2_ext, 3)
            print(f"    difficulté CodEx : rho cv={ext['rho_validation_croisee_codex']}, rho vs position écrit={ext['rho_difficulte_codex_predite_vs_position_ecrit']}")
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
                           "R2_les_deux": both, "principales": top, "difficulte_externe_codex": ext},
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
                  self.label_components, self.facets, self.combination_grammar, self.self_label_course, self.course_atoms,
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


# ===== examgen/fast.py =====
"""Accélérations qui ne changent aucun résultat.

- `auc` : aire sous la courbe ROC par la formule exacte des rangs (Mann-Whitney, ex aequo comptés
  pour moitié), identique à `sklearn.metrics.roc_auc_score` mais sans ses vérifications coûteuses.
- `pmap` : applique une fonction à une liste sur plusieurs cœurs, dans l'ordre (processus forkés,
  donc les objets déjà chargés sont partagés sans copie). `EXAMGEN_JOBS=1` désactive.
"""
from __future__ import annotations

import multiprocessing as mp
import os

import numpy as np
from scipy.stats import rankdata


def auc(y, s) -> float:
    y = np.asarray(y)
    u = np.unique(y)
    if len(u) != 2:
        raise ValueError("il faut exactement deux classes")
    y = y == u[1]  # comme scikit-learn : la plus grande étiquette est la classe positive
    n1 = int(y.sum())
    n0 = len(y) - n1
    r = rankdata(np.asarray(s, float))
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def jobs() -> int:
    try:
        return max(1, int(os.environ.get("EXAMGEN_JOBS", "0")) or len(os.sched_getaffinity(0)))
    except (ValueError, AttributeError):
        return os.cpu_count() or 1


_FN = None


def _call(x):
    return _FN(x)


def pmap(fn, items, n: int | None = None) -> list:
    """Comme [fn(x) for x in items], sur plusieurs processus si possible (même ordre, mêmes résultats)."""
    global _FN
    items = list(items)
    n = min(n or jobs(), len(items))
    if n <= 1 or mp.current_process().daemon:
        return [fn(x) for x in items]
    _FN = fn
    try:
        with mp.get_context("fork").Pool(n) as pool:
            return pool.map(_call, items, chunksize=1)
    finally:
        _FN = None


# ===== examgen/features.py =====
"""Extraction des variables de chaque question.

Chaque question réelle devient une ligne avec environ 60 variables :
  - notions du programme touchées (lexique de 45 notions + voisinage dans le cours)
  - niveau de Bloom (verbe d'action), format de réponse attendu, type de tâche
  - présence de code / SQL / tableau / figure dans l'énoncé
  - dépendances vers les questions précédentes (graphe)
  - position relative, longueur, sous-question, partie, barème, régime d'épreuve
"""
from __future__ import annotations

import re
import unicodedata
from collections import Counter

import networkx as nx
import numpy as np

# --------------------------------------------------------------------------- lexique des notions

# Notions du programme de Terminale NSI (+ rappels de Première les plus évalués).
# Chaque notion : (domaine, regex sur texte minuscule sans accents)
CONCEPTS: dict[str, tuple[str, str]] = {
    # T1 Structures de données
    "poo": ("Structures de données", r"\bclass\b|classe|objet|attributs? de (la|l.)classe|methode|__init__|self\.|instanc|encapsul|constructeur"),
    "pile": ("Structures de données", r"\bpiles?\b|empiler|depiler|lifo|sommet de la pile"),
    "file": ("Structures de données", r"\bfiles?\b(?! d'attente d'impression)|enfiler|defiler|fifo|file d'attente"),
    "liste_chainee": ("Structures de données", r"liste chainee|maillon|cellule|listes? chainees|tete de (la )?liste|queue de (la )?liste"),
    "dictionnaire": ("Structures de données", r"dictionnaire|\bdict\b|\.keys\(|\.values\(|\.items\(|cles?\b.*valeurs?"),
    "arbre_binaire": ("Structures de données", r"arbre binaire|arbres binaires|sous-arbre|feuilles?\b|noeud|racine|hauteur de l'arbre|taille de l'arbre|\bfils\b"),
    "abr": ("Structures de données", r"arbre binaire de recherche|\babr\b"),
    "parcours_arbre": ("Algorithmique", r"parcours (en )?(prefixe|infixe|suffixe|postfixe|en largeur|en profondeur)|prefixe|infixe|postfixe|suffixe"),
    "graphe": ("Structures de données", r"\bgraphes?\b|sommets?\b|aretes?\b|\barcs?\b|matrice d'adjacence|liste d'adjacence|voisins?\b|oriente"),
    "parcours_graphe": ("Algorithmique", r"parcours en largeur|parcours en profondeur|\bbfs\b|\bdfs\b|plus court chemin|dijkstra|cycle|chemin"),
    "interface_tad": ("Structures de données", r"interface|type abstrait|primitive|implementation|implementer"),
    "tableau_liste": ("Programmation", r"\btableau|\bliste\b|\blistes\b|append\(|len\(|indice|\[\s*i\s*\]|par comprehension"),
    "tuple": ("Programmation", r"\btuples?\b|p-uplet|n-uplet|couple"),
    "matrice": ("Programmation", r"matrice|tableau a deux dimensions|tableau de tableaux|grille|\[i\]\[j\]|pixels?"),
    # T2 Programmation
    "recursivite": ("Programmation", r"recursi|appel recursif|cas de base|cas d'arret|pile d'appels"),
    "modularite": ("Programmation", r"module|import |bibliotheque|\bapi\b|documentation|docstring"),
    "mise_au_point": ("Programmation", r"assert|test(s)? unitaire|jeu de test|bug|erreur|exception|precondition|postcondition|mise au point"),
    "paradigmes": ("Programmation", r"paradigme|programmation fonctionnelle|imperati|effet de bord|immuable|mutable|fonction (d'ordre superieur|lambda)|lambda"),
    "calculabilite": ("Programmation", r"calculabilit|decidabilit|probleme de l'arret|programme en tant que donnee|halt"),
    "boucles": ("Programmation", r"\bfor\b|\bwhile\b|boucle|iteration|invariant"),
    "fonctions": ("Programmation", r"\bdef\b|fonction|parametre|renvoie|return|valeur de retour|appel"),
    "chaines": ("Programmation", r"chaine de caracteres|chaines? de caracteres|\bstr\b|caractere|\.split|\.join|lettre|mot\b"),
    "booleens": ("Programmation", r"booleen|true|false|\band\b|\bor\b|\bnot\b|table de verite|logique"),
    "representation_nombres": ("Programmation", r"(?<!arbre )(?<!arbres )binaires?\b(?! de recherche)|hexadecimal|base 2|base 16|complement a deux|bits?\b|octets?\b|flottant|codage|ascii|unicode|utf"),
    # T3 Algorithmique
    "tri": ("Algorithmique", r"\btri\b|trier|tri par (selection|insertion|fusion)|trie|ordre croissant|ordre decroissant|sorted\("),
    "recherche_dichotomique": ("Algorithmique", r"dichotom|recherche binaire"),
    "diviser_regner": ("Algorithmique", r"diviser pour regner|tri fusion|fusion"),
    "prog_dynamique": ("Algorithmique", r"programmation dynamique|memoisation|memoiser|sous-probleme|rendu de monnaie|bottom|top-down"),
    "glouton": ("Algorithmique", r"glouton|gloutonne|sac a dos|rendu de monnaie"),
    "recherche_textuelle": ("Algorithmique", r"boyer|moore|horspool|recherche textuelle|motif|occurrence"),
    "complexite": ("Algorithmique", r"complexite|cout (en temps|temporel|de l.algorithme|d.execution)|lineaire|quadratique|logarithmique|o\(n|o\(1|o\(log|nombre d'operations|efficac"),
    "k_ppv": ("Algorithmique", r"plus proches voisins|k-nn|knn|k plus proches|distance euclidienne"),
    "algo_simples": ("Algorithmique", r"maximum|minimum|moyenne|somme des|compter|nombre d'occurrences|recherche (sequentielle|d'un element)"),
    # T4 Bases de données
    "modele_relationnel": ("Bases de données", r"modele relationnel|relation\b|relations\b|schema relationnel|cle primaire|cle etrangere|attribut|domaine|contrainte|entite"),
    "sql": ("Bases de données", r"\bselect\b|\bfrom\b|\bwhere\b|\bjoin\b|\binsert\b|\bupdate\b|\bdelete\b|requete|\bsql\b|order by|group by|count\(|distinct"),
    "sgbd": ("Bases de données", r"sgbd|systeme de gestion de bases? de donnees|transaction|acid|concurren|integrite|persistance"),
    # T5 Architecture, OS, réseaux, sécurité
    "processus": ("Architecture, OS et réseaux", r"processus|ordonnanc|interblocage|\bpid\b|ppid|\bps\b|etat (pret|bloque|elu)|elu\b|section critique|thread|round robin|tourniquet|interruption|ressource"),
    "os_commandes": ("Architecture, OS et réseaux", r"linux|terminal|commande|chmod|\bls\b|\bcd\b|\bmkdir\b|droits|repertoire|arborescence|chemin (absolu|relatif)|shell"),
    "routage": ("Architecture, OS et réseaux", r"routage|routeur|\brip\b|\bospf\b|table de routage|passerelle|saut|metrique|bande passante|debit"),
    "reseau_ip": ("Architecture, OS et réseaux", r"adresse ip|ipv4|ipv6|masque|sous-reseau|/24|/16|reseau local|\blan\b|\bwan\b|\btcp\b|\budp\b|paquet|protocole|switch|commutateur"),
    "soc_architecture": ("Architecture, OS et réseaux", r"systeme sur puce|\bsoc\b|microprocesseur|processeur|memoire|\bram\b|\bcpu\b|gpu|von neumann|circuit|composant|transistor|assembleur|registre"),
    "securite_crypto": ("Architecture, OS et réseaux", r"chiffr|crypt|cle (publique|privee)|symetrique|asymetrique|\brsa\b|https|certificat|\btls\b|\bssl\b|cesar|vigenere|xor|hach|signature|authentific"),
    "web_http": ("Architecture, OS et réseaux", r"\bhttp\b|\bhtml\b|\bcss\b|javascript|formulaire|\bget\b|\bpost\b|serveur web|client|url|cookie"),
    "donnees_tables": ("Programmation", r"\bcsv\b|fichier|table de donnees|enregistrement|descripteur|open\("),
}

DOMAINS = sorted({d for d, _ in CONCEPTS.values()})
CONCEPT_NAMES = list(CONCEPTS)
_CONCEPT_RX = {k: re.compile(v[1]) for k, v in CONCEPTS.items()}

# Un mot qui apparaît partout (fonction, liste, boucle) compte moins qu'une notion pointue.
GENERIC = {"fonctions", "tableau_liste", "boucles", "booleens", "interface_tad", "chaines"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def concept_hits(text: str) -> dict[str, int]:
    t = norm(text)
    out = {}
    for k, rx in _CONCEPT_RX.items():
        n = len(rx.findall(t))
        if n:
            out[k] = n
    return out


# --------------------------------------------------------------------------- Bloom, format, tâche

BLOOM = [  # (niveau, nom, regex verbes en tête de consigne)
    (6, "créer", r"\becri(re|vez)\b|\bproposer\b|\bconcevoir\b|\bimplement|\bprogrammer\b|\bconstruire\b|\bredige|\bdefinir une (fonction|classe|methode)"),
    (5, "évaluer", r"\bjustifi|\bcritiquer\b|\bdiscuter\b|\bverifier\b|\bmontrer\b|\bdemontrer\b|\bprouver\b|\bevaluer\b|\best-ce que\b|\bavantages?\b|\binconvenients?\b"),
    (4, "analyser", r"\banalyser\b|\bcomparer\b|\ben deduire\b|\bdeduire\b|\bidentifier\b|\bexpliquer pourquoi\b|\brole\b|\bdifference\b|\bcomplexite\b|\bque fait\b|\bque calcule\b|\berreur\b|\bcorriger\b"),
    (3, "appliquer", r"\bcalculer\b|\bdeterminer\b|\bcompleter\b|\brecopier\b|\bdessiner\b|\brepresenter\b|\bappliquer\b|\bexecuter\b|\btracer\b|\bmodifier\b|\bdonner (la|le|les) (valeur|resultat|liste|contenu|etat|affichage|table|requete|adresse|nombre)|\bque (renvoie|affiche|retourne)\b|\bqu'affiche\b|\btraduire\b|\breecrire\b"),
    (2, "comprendre", r"\bexpliquer\b|\bdecrire\b|\binterpreter\b|\bdire\b|\bpreciser\b|\bindiquer\b|\bquel est\b|\bquelle est\b|\bquels sont\b|\bquelles sont\b|\bpourquoi\b|\bcomment\b"),
    (1, "se souvenir", r"\bciter\b|\bnommer\b|\bdonner (le nom|un exemple|la definition)|\bdefinir\b|\brappeler\b|\benoncer\b|\bque signifie\b|\bsignification\b|\bdonner\b"),
]
_BLOOM_RX = [(lvl, name, re.compile(rx)) for lvl, name, rx in BLOOM]

FORMATS = {
    "code_python": r"ecrire (une|la|le) (fonction|methode|code|programme|instruction|script|classe|boucle)|\bcompleter (le|la|les) (code|fonction|methode|programme|ligne)|en python|\bdef\b.*:|implement",
    "sql": r"requete|\bsql\b|\bselect\b",
    "valeur": r"que (renvoie|affiche|retourne|vaut|contient)|qu'affiche|valeur|resultat|combien|calculer|nombre de|donner la liste|contenu",
    "explication": r"expliquer|justifier|pourquoi|decrire|commenter|interpreter|en quoi|argument",
    "schema": r"dessiner|representer|schema|tracer|arbre obtenu|graphe obtenu|figure|diagramme",
    "tableau": r"tableau|table de routage|compl[e]ter le tableau|recopier (et completer )?le tableau|table de verite",
    "qcm_choix": r"cocher|parmi les (propositions|reponses|suivantes)|choisir|laquelle|lequel|\bvrai\b|\bfaux\b|proposition",
    "complexite": r"complexite|\bo\(|cout en temps|nombre d'operations",
}
_FORMAT_RX = {k: re.compile(v) for k, v in FORMATS.items()}

TASKS = [  # ordre = priorité
    ("trace_execution", r"que (renvoie|affiche|retourne|vaut|contient)|qu'affiche|valeur (renvoyee|de la variable|prise)|resultat de l'(appel|execution)|apres (l'execution|execution|l'appel)|etat de la (pile|file)|contenu de"),
    ("corriger_code", r"erreur|corriger|bug|ne fonctionne pas|probleme dans|incorrect"),
    ("completer_code", r"completer|compl[e]ter les lignes|recopier et completer|trous|\.\.\.|lignes? manquantes?"),
    ("ecrire_sql", r"ecrire (une|la) requete|requete sql|requete permettant|donner (une|la) requete|requete qui"),
    ("lire_sql", r"(que renvoie|resultat de|que fait|decrire|expliquer) (cette|la) requete|requete suivante"),
    ("ecrire_fonction", r"ecrire (une|la) fonction|ecrire (une|la) methode|ecrire (le|un) (code|programme|script)|definir (une|la) fonction|implementer|programmer (une|la)|ecrire une version"),
    ("complexite", r"complexite|\bo\(|cout (en temps|temporel|d.execution)|nombre de comparaisons|nombre d'operations|efficac"),
    ("dessiner_structure", r"dessiner|representer|tracer|schema|arbre obtenu|graphe (obtenu|correspondant)"),
    ("calcul_numerique", r"calculer|convertir|binaire|hexadecimal|adresse (ip|reseau|de diffusion)|masque|nombre (maximal|de machines|d'adresses)|cout\b|debit"),
    ("table_routage", r"table de routage|route|chemin emprunte|routeurs? (traverses|par lesquels)|saut"),
    ("modele_donnees", r"schema relationnel|cle (primaire|etrangere)|relation|attribut|modele"),
    ("justifier_choix", r"justifier|expliquer pourquoi|pourquoi|avantage|inconvenient|interet|en quoi"),
    ("definir_notion", r"definir|donner la definition|que signifie|citer|nommer|qu'est-ce"),
    ("ordonnancement", r"ordonnanc|chronogramme|processus|interblocage|elu|bloque"),
    ("expliquer", r"expliquer|decrire|indiquer|preciser|dire"),
]
_TASK_RX = [(k, re.compile(v)) for k, v in TASKS]

DEP_RX = re.compile(
    r"question (precedente|\d+|[a-e]\.\d+)|precedemment|ci-dessus|en deduire|deduire|a l'aide de (la|cette) fonction|"
    r"en utilisant (la|les) fonctions?|reprendre|meme (fonction|maniere|methode)|definie? (a la|en) question|"
    r"realisee? (a la|en) question|precedent"
)
FUNC_RX = re.compile(r"\b([a-z_][a-z0-9_]{2,})\s*\(")
PY_KW = set("print len range int str float list dict set tuple return def class if else elif for while and or not in is none true false append pop insert sorted max min sum abs open input type isinstance zip enumerate map filter round".split())


def bloom_level(stem: str) -> tuple[int, str]:
    t = norm(stem)
    for lvl, name, rx in _BLOOM_RX:
        if rx.search(t):
            return lvl, name
    return (2, "comprendre") if "?" in stem else (3, "appliquer")


def answer_formats(stem: str) -> list[str]:
    t = norm(stem)
    f = [k for k, rx in _FORMAT_RX.items() if rx.search(t)]
    return f or ["explication"]


def task_type(stem: str) -> str:
    t = norm(stem)
    for k, rx in _TASK_RX:
        if rx.search(t):
            return k
    return "autre"


def code_lines(text: str) -> int:
    n = 0
    for ln in text.splitlines():
        s = ln.strip()
        if re.match(r"^\d{1,3}\s+\S", s) and not re.match(r"^\d{1,2}\s*[\.)]\s", s):
            n += 1
        elif re.search(r"^(def |class |return\b|for .* in .*:|while .*:|if .*:|else:|elif |import |>>> )", s):
            n += 1
        elif re.search(r"^(SELECT|FROM|WHERE|INSERT|UPDATE|DELETE|JOIN|ORDER BY|GROUP BY)\b", s):
            n += 1
    return n


def defined_functions(text: str) -> set[str]:
    return set(re.findall(r"def\s+([a-zA-Z_]\w*)\s*\(", text)) | set(re.findall(r"fonction\s+([a-z_]\w+)", norm(text)))


# --------------------------------------------------------------------------- table des questions

def regime(exam: dict) -> str:
    if exam["type"] == "pratique":
        return "pratique"
    y = exam.get("year") or 0
    return "2021-2022 (5 ex. dont 3 au choix)" if y <= 2022 or exam["n_exercises"] >= 5 else "2023+ (3 ex. obligatoires)"


def build_question_table(exams: list[dict]) -> list[dict]:
    rows = []
    for e in exams:
        reg = regime(e)
        for x in e["exercises"]:
            qs = x["questions"]
            if not qs:
                continue
            ex_hits = concept_hits(x["raw"])
            ex_theme_hits = concept_hits(x.get("theme_sentence") or "")
            prev_funcs: set[str] = set(defined_functions(x["preamble"]))
            n = len(qs)
            G = nx.DiGraph()
            for i, q in enumerate(qs):
                stem = q["text"]
                full = (q.get("context_before") or "") + "\n" + stem
                t = norm(stem)
                hits = concept_hits(full)
                called = {f for f in FUNC_RX.findall(norm(stem)) if f not in PY_KW}
                dep_funcs = called & prev_funcs
                explicit = bool(DEP_RX.search(t))
                deps = []
                if explicit and i > 0:
                    deps.append(i - 1)
                for j in range(i):
                    if dep_funcs & defined_functions(qs[j]["text"]):
                        deps.append(j)
                    m = re.search(r"question\s+(\d+)", t)
                    if m and qs[j]["label"].split(".")[0] == m.group(1):
                        deps.append(j)
                deps = sorted(set(deps))
                G.add_node(i)
                for d in deps:
                    G.add_edge(d, i)
                prev_funcs |= defined_functions(stem)
                lvl, bname = bloom_level(stem)
                fm = answer_formats(stem)
                cl = code_lines(full)
                rows.append({
                    "exam_id": e["id"], "exam_type": e["type"], "year": e.get("year"), "center": e.get("center"),
                    "regime": reg, "exercise": x["number"], "ex_points": x.get("points"),
                    "ex_theme": x.get("theme_sentence"), "ex_n_questions": n,
                    "label": q["label"], "part": q.get("part"), "is_sub": q.get("is_sub", False),
                    "pos": i, "rel_pos": i / max(n - 1, 1),
                    "text": stem, "context": q.get("context_before") or "",
                    "len_words": len(stem.split()), "ctx_words": len((q.get("context_before") or "").split()),
                    "code_lines": cl, "has_code": cl >= 2,
                    "has_sql": bool(re.search(r"\b(SELECT|FROM|WHERE|JOIN|INSERT|UPDATE)\b", full)),
                    "has_table": bool(re.search(r"tableau|table\b|\|", norm(full))),
                    "has_figure": bool(re.search(r"figure|schema|ci-dessous|ci-contre|graphique", norm(full))),
                    "has_example_call": ">>>" in full or bool(re.search(r"exemple", t)),
                    "question_mark": "?" in stem,
                    "bloom": lvl, "bloom_name": bname, "formats": fm, "task": task_type(stem),
                    "concepts": hits, "ex_concepts": ex_hits, "ex_theme_concepts": ex_theme_hits,
                    "deps": deps, "explicit_dep": explicit, "n_deps": len(deps),
                })
            # profondeur dans le graphe de dépendances de l'exercice
            depth = {}
            for node in nx.topological_sort(G):
                preds = list(G.predecessors(node))
                depth[node] = 0 if not preds else 1 + max(depth[p] for p in preds)
            base = len(rows) - n
            for i in range(n):
                rows[base + i]["dep_depth"] = depth.get(i, 0)
                rows[base + i]["n_dependents"] = G.out_degree(i)
    return rows


def main_concepts(row: dict, k: int = 3) -> list[str]:
    """Notions principales d'une question : celles de la question, sinon de l'exercice,
    les notions génériques pèsent moitié moins."""
    score = Counter()
    for c, n in row["concepts"].items():
        score[c] += n * (0.5 if c in GENERIC else 1.5)
    for c, n in row["ex_theme_concepts"].items():
        score[c] += 2.0 * (0.5 if c in GENERIC else 1.0)
    for c, n in row["ex_concepts"].items():
        score[c] += 0.15 * min(n, 10) * (0.3 if c in GENERIC else 1.0)
    return [c for c, _ in score.most_common(k)]


STRUCT_FEATURES = [
    "rel_pos", "len_words", "ctx_words", "code_lines", "has_code", "has_sql", "has_table", "has_figure",
    "has_example_call", "question_mark", "is_sub", "n_deps", "explicit_dep", "dep_depth", "n_dependents",
    "ex_n_questions",
]
TASK_NAMES = [t for t, _ in TASKS] + ["autre"]
FORMAT_NAMES = list(FORMATS)


def feature_matrix(rows: list[dict]) -> tuple[np.ndarray, list[str]]:
    """Matrice numérique interprétable (sans le texte) : une colonne = une variable."""
    names = list(STRUCT_FEATURES)
    names += [f"bloom={i}" for i in range(1, 7)]
    names += [f"format={f}" for f in FORMAT_NAMES]
    names += [f"task={t}" for t in TASK_NAMES]
    names += [f"concept={c}" for c in CONCEPT_NAMES]
    X = np.zeros((len(rows), len(names)), dtype=float)
    idx = {n: i for i, n in enumerate(names)}
    for r, row in enumerate(rows):
        for f in STRUCT_FEATURES:
            v = row.get(f, 0)
            X[r, idx[f]] = float(v) if v is not None else 0.0
        X[r, idx[f"bloom={row['bloom']}"]] = 1
        for f in row["formats"]:
            X[r, idx[f"format={f}"]] = 1
        X[r, idx[f"task={row['task']}"]] = 1
        for c in main_concepts(row):
            X[r, idx[f"concept={c}"]] = 1
    # échelles comparables
    for f in ("len_words", "ctx_words", "code_lines", "ex_n_questions"):
        j = idx[f]
        X[:, j] = np.log1p(X[:, j])
    return X, names


# ===== examgen/inedit.py =====
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
        """Facette fragile : jugée instable par le bootstrap (critère appris) ou incohérente à la lecture."""
        info = (self.sf if kind == "consigne" else self.uf)[f]
        return info.get("stabilite", 1.0) < 0.6 or self.names.get(kind, {}).get(str(f), {}).get("coherence") == "faible"

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


# ===== examgen/ingest.py =====
"""Ingestion : PDF / Markdown -> corpus structuré.

Sorties (data/corpus/) :
  exams.jsonl   un sujet par ligne : métadonnées + exercices + questions
  course.jsonl  une section de cours par ligne : chapitre, titre, texte
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .config import CORPUS, SOURCES

# --------------------------------------------------------------------------- utils

CENTERS = {
    "ME": "Métropole", "G1": "Centres étrangers", "G11": "Centres étrangers",
    "AN": "Amérique du Nord", "AS": "Amérique du Sud", "JA": "Asie", "PO": "Polynésie",
    "NC": "Nouvelle-Calédonie", "LI": "Liban", "AG": "Antilles-Guyane", "IN": "Inde",
    "MA": "Mayotte", "RE": "La Réunion", "PE": "Sujet zéro", "SU": "Suède",
}
NAME_CENTERS = [
    ("amerique-sud", "Amérique du Sud"), ("amerique_sud", "Amérique du Sud"), ("metropole", "Métropole"), ("etranger", "Centres étrangers"), ("amerique", "Amérique du Nord"),
    ("asie", "Asie"), ("polynesie", "Polynésie"), ("caledonie", "Nouvelle-Calédonie"),
    ("antilles", "Antilles-Guyane"), ("mayotte", "Mayotte"), ("liban", "Liban"), ("sujet_0", "Sujet zéro"),
    ("amerique-sud", "Amérique du Sud"), ("nouv-caledonie", "Nouvelle-Calédonie"), ("reunion", "La Réunion"),
    ("suede", "Suède"), ("metro", "Métropole"), ("-zero", "Sujet zéro"),
    ("sujet0", "Sujet zéro"), ("blanc", "Bac blanc"), ("amnord", "Amérique du Nord"),
]


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


PDF_CACHE = CORPUS.parent / "cache" / "pdf"


def pdf_text(path: Path) -> str:
    if not path.is_file():
        return ""
    key = hashlib.md5(f"{path}:{path.stat().st_size}".encode()).hexdigest()
    cached = PDF_CACHE / f"{key}.txt"
    if cached.exists():
        return cached.read_text(encoding="utf-8")
    try:
        reader = PdfReader(str(path))
        if len(reader.pages) > 60:  # recueils / livres : hors sujet
            txt = ""
        else:
            txt = "\n".join((p.extract_text() or "") for p in reader.pages)
    except Exception as e:  # PDF corrompu / chiffré
        print(f"  ! {path.name}: {e}")
        txt = ""
    PDF_CACHE.mkdir(parents=True, exist_ok=True)
    cached.write_text(txt, encoding="utf-8")
    return txt


HEADER_RE = re.compile(
    r"^\s*(\d{2}[-_ ]?NSI\w*|NSI\w*)?\s*(Page\s*:?\s*)?\d+\s*/\s*\d+\s*$|"
    r"^\s*\d{2}[-_ ]?NSI[A-Z0-9]+\s+Page\s*:?\s*\d+\s*/\s*\d+.*$|"
    r"^\s*Page\s+\d+\s+(sur|/)\s+\d+\s*$",
    re.I,
)


def clean_pdf_text(t: str) -> str:
    t = t.replace(" ", " ").replace("’", "'").replace("", "•")
    lines = [ln.rstrip() for ln in t.splitlines() if not HEADER_RE.match(ln)]
    t = "\n".join(lines)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()


# --------------------------------------------------------------------------- métadonnées

CODE_RE = re.compile(r"(\d{2})[-_ ]?NSI(?:J(\d))?([A-Z]{2})(\d{1,2})", re.I)


def exam_metadata(path: Path, text: str) -> dict:
    name = path.stem
    low = strip_accents(name.lower())
    m = CODE_RE.search(name.upper()) or CODE_RE.search(text[:400].upper())
    year = None
    if (s := re.search(r"SESSION\s+(20\d\d)", text[:1500], re.I)):
        year = int(s.group(1))
    elif m:
        year = 2000 + int(m.group(1))
    elif (s := re.search(r"(20\d\d)", name)):
        year = int(s.group(1))
    elif (s := re.search(r"^(\d{2})[-_]", name)):
        year = 2000 + int(s.group(1))
    day = None
    if m and m.group(2):
        day = int(m.group(2))
    elif (d := re.search(r"J(\d)", name, re.I)):
        day = int(d.group(1))
    elif (d := re.search(r"-(\d)-sujet", low)):
        day = int(d.group(1))
    center = None
    for key, val in NAME_CENTERS:
        if key in low:
            center = val
            break
    if center is None and m:
        center = CENTERS.get(m.group(3).upper(), m.group(3).upper())
    kind = "blanc" if "blanc" in low else ("sujet0" if ("sujet_0" in low or "sujet0" in low or "sujet 0" in low or "-zero" in low) else "officiel")
    if year is None and (s := re.search(r"(20\d\d)", str(path))):
        year = int(s.group(1))
    duration = None
    if (dm := re.search(r"Durée de l'épreuve\s*:\s*(\d)\s*heures?\s*(\d+)?", text[:2500], re.I)):
        duration = int(dm.group(1)) * 60 + int(dm.group(2) or 0)
    return {"year": year, "day": day, "center": center, "kind": kind, "duration_min": duration}


# --------------------------------------------------------------------------- segmentation écrit

EX_RE = re.compile(
    r"^\s*EXERCICE\s*(?:N°\s*)?(\d)\s*(?:[\(:\-–]\s*)?(?:sur\s*)?(?:(\d+(?:[,.]\d+)?)\s*points?)?",
    re.I | re.M,
)
THEME_RE = re.compile(
    r"(Cet exercice|L'exercice|Ce exercice)\s+(porte|traite|aborde|concerne|est consacré|utilise|mobilise|étudie)"
    r"[^.]*?(?:sur|de|à|des|les|la|le)?\s*(.+?)\.(?:\s|$)",
    re.I | re.S,
)
PART_RE = re.compile(r"^\s*Partie\s+([A-E]|\d)\b\s*[:\-–]?\s*(.*)$", re.I)
Q_RES = [
    # "Question A.1", "Question 3 :", "Question 2.b"
    re.compile(r"^\s*Question\s+((?:[A-E][\.\-]?)?\d{1,2}(?:[\.\-]?[a-z\d])?)\s*[\.:\-–)]?\s*(.*)$", re.I),
    # "A.1. ", "B.3) "
    re.compile(r"^\s*([A-E]\.\d{1,2}(?:\.[a-z\d])?)\s*[\.)]\s*(.+)$"),
    # "1.a. ", "2.b) ", "3.2. "
    re.compile(r"^\s*(\d{1,2}\.(?:[a-h]|\d))\s*[\.)]\s*(.+)$"),
    # "1. Écrire ..."  (pas "1. 0" ni numéros de lignes de code)
    re.compile(r"^\s*(\d{1,2})\s*[\.)]\s+([A-ZÉÈÀÂÇÎÔa-zéèêàç«\"'(].*)$"),
    # "Q1. ", "Q.3 "
    re.compile(r"^\s*Q\.?\s?(\d{1,2}(?:\.[a-z\d])?)\s*[\.:)\-–]?\s*(.+)$"),
]
SUBQ_RE = re.compile(r"^\s*([a-h])\s*[\.)]\s+(.+)$")
INSTR_VERBS = (
    "écrire|ecrire|donner|expliquer|justifier|compléter|completer|recopier|déterminer|determiner|"
    "indiquer|proposer|calculer|montrer|démontrer|dessiner|représenter|representer|citer|préciser|"
    "preciser|décrire|decrire|identifier|modifier|implémenter|implementer|lister|établir|etablir|"
    "construire|tracer|nommer|traduire|vérifier|verifier|justifie|quel|quelle|quels|quelles|"
    "combien|pourquoi|comment|que|qu'|définir|definir|énoncer|enoncer|exprimer|évaluer|evaluer|"
    "choisir|associer|réécrire|reecrire|dire|écrivez|donnez|expliquez|complétez|corriger|"
    "estimer|comparer|déduire|deduire|rédiger|rediger|recopiez|sélectionner|selectionner|en déduire"
)
INSTR_RE = re.compile(rf"\b({INSTR_VERBS})\b", re.I)


def looks_like_code(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    return bool(
        re.match(r"^\d{1,3}\s{1,}\S", s) and not re.match(r"^\d{1,2}\s*[\.)]\s", s)
        or re.search(r"(def |return |class |for .* in |while |if .*:|==|!=|\[\d*\]|\(\)|=\s*\S|SELECT|FROM|WHERE|>>>)", s)
    )


def split_stem_context(lines: list[str]) -> tuple[str, str]:
    """Sépare l'énoncé propre de la question du texte de contexte qui suit
    (et qui sert en réalité de préambule à la question suivante)."""
    stem, ctx = [], []
    has_instr = False
    for i, ln in enumerate(lines):
        if ctx:
            ctx.append(ln)
            continue
        prev = stem[-1].strip() if stem else ""
        sentence_closed = prev.endswith((".", "?", "!")) or looks_like_code(prev)
        starts_new = bool(re.match(r"^\s*[A-ZÉÈÀÇ][a-zéèàêç]", ln)) and not looks_like_code(ln)
        if has_instr and sentence_closed and starts_new and not INSTR_RE.search(ln[:40]) and i > 0:
            ctx.append(ln)
            continue
        stem.append(ln)
        if INSTR_RE.search(ln):
            has_instr = True
    return "\n".join(stem).strip(), "\n".join(ctx).strip()


def segment_questions(body: str) -> tuple[str, list[dict]]:
    """Découpe le corps d'un exercice en questions. Renvoie (préambule, questions)."""
    lines = body.splitlines()
    starts = []  # (index_ligne, label, partie)
    part = None
    last_num, last_part = 0, None
    for i, ln in enumerate(lines):
        if (pm := PART_RE.match(ln)) and len(ln) < 120:
            part = pm.group(1).upper()
            starts.append((i, None, part, "part"))
            last_num = 0
            continue
        for rx in Q_RES:
            if (qm := rx.match(ln)):
                label = qm.group(1)
                # filtre : une liste numérotée sans verbe dans un préambule n'est pas une question,
                # sauf si elle suit exactement la numérotation attendue
                window = " ".join(lines[i:i + 8])
                top = re.match(r"(?:[A-E][\.\-]?)?(\d{1,2})", label)
                n = int(top.group(1)) if top else None
                sequential = n is not None and (n == last_num + 1 or (n == 1 and part != last_part))
                if (INSTR_RE.search(window) or "?" in window) and (sequential or n is None or n > last_num):
                    starts.append((i, label, part, "q"))
                    if n is not None:
                        last_num, last_part = n, part
                elif sequential:
                    starts.append((i, label, part, "q"))
                    last_num, last_part = n, part
                break
        else:
            if (sm := SUBQ_RE.match(ln)) and starts and starts[-1][3] in ("q", "sub"):
                window = " ".join(lines[i:i + 3])
                if INSTR_RE.search(window) or "?" in window:
                    starts.append((i, sm.group(1), part, "sub"))
    if not starts:
        return body.strip(), []
    preamble = "\n".join(lines[: starts[0][0]]).strip()
    questions = []
    carry = ""
    parent = None
    for k, (i, label, prt, typ) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        block = lines[i:end]
        if typ == "part":
            carry = (carry + "\n" + "\n".join(block)).strip()
            parent = None
            continue
        stem, ctx = split_stem_context(block)
        if typ == "q":
            parent = label
            full_label = label
        else:
            full_label = f"{parent}.{label}" if parent else label
        questions.append({
            "label": full_label, "part": prt, "is_sub": typ == "sub",
            "context_before": carry, "text": stem,
        })
        carry = ctx
    return preamble, questions


def segment_exam(text: str) -> list[dict]:
    matches = list(EX_RE.finditer(text))
    # pour chaque numéro d'exercice, préférer l'occurrence qui annonce un barème « (x points) »
    # et qui n'est pas une annexe ; garder l'ordre croissant
    best = {}
    for m in matches:
        n = int(m.group(1))
        tail = text[m.end():m.end() + 40].lower()
        score = (m.group(2) is not None) * 2 - ("annexe" in tail) * 3
        if n not in best or score > best[n][0]:
            best[n] = (score, m)
    kept, last = [], -1
    for n in sorted(best):
        m = best[n][1]
        if m.start() > last:
            kept.append(m)
            last = m.start()
    exercises = []
    for k, m in enumerate(kept):
        start = m.end()
        end = kept[k + 1].start() if k + 1 < len(kept) else len(text)
        body = text[start:end]
        pts = m.group(2)
        theme = None
        if (tm := THEME_RE.search(body[:900])):
            theme = re.sub(r"\s+", " ", tm.group(3)).strip()
        preamble, qs = segment_questions(body)
        exercises.append({
            "number": int(m.group(1)),
            "points": float(pts.replace(",", ".")) if pts else None,
            "theme_sentence": theme,
            "preamble": preamble,
            "questions": qs,
            "raw": body.strip(),
        })
    return exercises


# --------------------------------------------------------------------------- écrit

EXCLUDE = re.compile(r"corr|correc|corrig|solution", re.I)


def is_official(raw: str) -> bool:
    h = strip_accents(raw[:2500].lower())
    return "baccalaureat" in h and "numerique et sciences informatiques" in h and (
        "session" in h or "epreuve de l'enseignement de specialite" in h or "duree de l'epreuve" in h)


def ingest_written() -> list[dict]:
    pdfs = []
    for base in [
        SOURCES / "trahobisoa_Terminale_NSI" / "Sujets Epreuve Ecrite",
        SOURCES / "glassus_terminale_nsi" / "docs" / "T6_Annales" / "data",
        SOURCES / "sujetdebac",
    ]:
        if base.exists():
            pdfs += [(p, False) for p in base.rglob("*.pdf") if not EXCLUDE.search(p.name)]
    # dépôts d'enseignants : on ne garde comme « écrit » que les PDF portant l'en-tête officiel
    for base in sorted(SOURCES.glob("forge_*")):
        pdfs += [(p, True) for p in base.rglob("*.pdf") if not EXCLUDE.search(str(p.relative_to(base)))]
    print(f"[écrit] {len(pdfs)} PDF candidats")
    exams = []
    for p, need_header in sorted(pdfs):
        raw = pdf_text(p)
        if len(raw) < 2000:
            continue
        txt = clean_pdf_text(raw)
        head = strip_accents(txt[:3000].lower())
        if "correction" in head[:600] or "corrige" in head[:600] or "elements de correction" in head:
            continue
        if need_header and not is_official(raw):
            continue
        meta = exam_metadata(p, txt)
        exs = segment_exam(txt)
        if len(exs) < 2:
            continue
        exams.append({
            "id": hashlib.md5(txt.encode()).hexdigest()[:10],
            "type": "ecrit", "source": str(p.relative_to(SOURCES)), **meta,
            "n_exercises": len(exs), "exercises": exs, "text": txt,
        })
    # déduplication (le même sujet existe dans plusieurs dépôts)
    vec = TfidfVectorizer(max_features=20000, ngram_range=(1, 2)).fit([e["text"] for e in exams])
    X = vec.transform([e["text"] for e in exams])
    sim = cosine_similarity(X)
    keep, dropped = [], set()
    order = sorted(range(len(exams)), key=lambda i: -sum(len(x["questions"]) for x in exams[i]["exercises"]))
    for i in order:
        if i in dropped:
            continue
        keep.append(exams[i])
        for j in range(len(exams)):
            if j != i and sim[i, j] > 0.80:
                dropped.add(j)
    print(f"[écrit] {len(exams)} sujets extraits -> {len(keep)} après déduplication")
    return sorted(keep, key=lambda e: (e["year"] or 0, e["center"] or "", e["day"] or 0))


# --------------------------------------------------------------------------- pratique

def ingest_practical() -> list[dict]:
    base = SOURCES / "glassus_terminale_nsi" / "includes"
    exams = {}
    for f in sorted(base.glob("*/files/*_*/enonce.md")):
        year = int(f.parts[-4])
        sujet, num = f.parent.name.split("_")[:2]
        txt = f.read_text(encoding="utf-8", errors="ignore").strip()
        if len(txt) < 80:
            continue
        key = (year, sujet)
        e = exams.setdefault(key, {
            "id": f"P{year}-{sujet}", "type": "pratique", "source": str(f.parent.parent.relative_to(SOURCES)),
            "year": year, "day": None, "center": "BNS", "kind": "officiel", "duration_min": 60,
            "exercises": [], "text": "",
        })
        e["exercises"].append({
            "number": int(num) if num.isdigit() else len(e["exercises"]) + 1,
            "points": 10.0, "theme_sentence": None, "preamble": "",
            "questions": [{"label": "1", "part": None, "is_sub": False, "context_before": "", "text": txt}],
            "raw": txt,
        })
        e["text"] += "\n\n" + txt
    out = list(exams.values())
    for e in out:
        e["n_exercises"] = len(e["exercises"])
    # dédupliquer les exercices identiques d'une année sur l'autre (la BNS est reconduite)
    seen, n_dup = set(), 0
    for e in out:
        for ex in e["exercises"]:
            h = hashlib.md5(re.sub(r"\W+", "", ex["raw"].lower()).encode()).hexdigest()
            ex["duplicate_of_previous_year"] = h in seen
            n_dup += h in seen
            seen.add(h)
    print(f"[pratique] {len(out)} sujets, {sum(e['n_exercises'] for e in out)} exercices ({n_dup} reconduits)")
    return out


# --------------------------------------------------------------------------- cours

MD_NOISE = [
    (re.compile(r"!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?"), ""),       # images
    (re.compile(r"\{\{[^}]*\}\}"), ""),                          # macros mkdocs
    (re.compile(r"\{[:.][^}]*\}"), ""),                          # attributs
    (re.compile(r"^\s*(!!!|\?\?\?\+?|===)\s*\w*\s*(\"[^\"]*\")?", re.M), ""),
    (re.compile(r"--8<--.*$", re.M), ""),
    (re.compile(r"\[([^\]]+)\]\([^)]*\)"), r"\1"),               # liens
    (re.compile(r"<[^>]+>"), ""),
]

CHAPTER_NAMES = {
    "T1": "Structures de données", "T2": "Programmation", "T3": "Algorithmique",
    "T4": "Bases de données", "T5": "Architecture, OS et réseaux",
    "T6_2": "Rappels de Première", "T6_5": "Algorithmes de Première",
}
PDF_PREFIX = {
    "ALGO": "Algorithmique", "AMSER": "Architecture, OS et réseaux", "BDD": "Bases de données",
    "LP": "Programmation", "SD": "Structures de données",
}


def clean_md(t: str) -> str:
    for rx, rep in MD_NOISE:
        t = rx.sub(rep, t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def split_md_sections(text: str) -> list[tuple[str, str]]:
    parts, title, buf = [], "Introduction", []
    for ln in text.splitlines():
        if re.match(r"^#{1,3}\s", ln):
            if buf:
                parts.append((title, "\n".join(buf)))
            title, buf = ln.lstrip("#").strip(), []
        else:
            buf.append(ln)
    if buf:
        parts.append((title, "\n".join(buf)))
    return parts


def ingest_course() -> list[dict]:
    secs = []
    docs = SOURCES / "glassus_terminale_nsi" / "docs"
    for f in sorted(docs.glob("T[1-5]_*/*/*.md")) + sorted(docs.glob("T6_[25]_*/cours.md")):
        if "Copie en conflit" in f.name:
            continue
        top = f.parts[len(docs.parts)]
        key = "T6_2" if top.startswith("T6_2") else "T6_5" if top.startswith("T6_5") else top[:2]
        chapter = CHAPTER_NAMES.get(key, top)
        lesson = f.parent.name if not top.startswith("T6") else top
        lesson = re.sub(r"^[\d.]+_", "", lesson).replace("_", " ")
        kind = "exercices" if "exercice" in f.stem else ("tp" if "TP" in f.stem else "cours")
        body = clean_md(f.read_text(encoding="utf-8", errors="ignore"))
        for title, txt in split_md_sections(body):
            if len(txt.strip()) < 120:
                continue
            secs.append({"source": "glassus", "chapter": chapter, "lesson": lesson,
                         "kind": kind, "title": title, "text": txt.strip()})
    tdir = SOURCES / "trahobisoa_Terminale_NSI"
    for f in sorted(tdir.glob("*.pdf")):
        pre = re.match(r"([A-Z]+)\d+", f.name)
        if not pre or pre.group(1) not in PDF_PREFIX:
            continue
        txt = clean_pdf_text(pdf_text(f))
        lesson = re.sub(r"^[A-Z]+\d+-", "", f.stem).replace("_", " ")
        # découpe en blocs ~1500 caractères sur frontières de paragraphes
        buf = ""
        for para in re.split(r"\n\s*\n", txt):
            buf += para + "\n\n"
            if len(buf) > 1500:
                secs.append({"source": "trahobisoa", "chapter": PDF_PREFIX[pre.group(1)], "lesson": lesson,
                             "kind": "cours", "title": lesson, "text": buf.strip()})
                buf = ""
        if len(buf) > 200:
            secs.append({"source": "trahobisoa", "chapter": PDF_PREFIX[pre.group(1)], "lesson": lesson,
                         "kind": "cours", "title": lesson, "text": buf.strip()})
    bo = tdir / "BO progamme Term NSI.pdf"
    if bo.exists():
        secs.append({"source": "BO", "chapter": "Programme officiel", "lesson": "Programme",
                     "kind": "programme", "title": "Programme officiel de Terminale NSI",
                     "text": clean_pdf_text(pdf_text(bo))})
    print(f"[cours] {len(secs)} sections ({sum(len(s['text']) for s in secs)//1000} k caractères)")
    return secs


def write_jsonl(path: Path, rows: list[dict]):
    with path.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.open(encoding="utf-8")]


def run():
    written = ingest_written()
    practical = ingest_practical()
    course = ingest_course()
    write_jsonl(CORPUS / "exams.jsonl", written + practical)
    write_jsonl(CORPUS / "course.jsonl", course)
    write_jsonl(CORPUS / "course_exercises.jsonl", ingest_course_exercises())
    from . import ingest_extra
    ingest_extra.run()
    nq = sum(len(x["questions"]) for e in written for x in e["exercises"])
    print(f"[ok] {len(written)} sujets écrits ({nq} questions), {len(practical)} sujets pratiques")



# ---------------------------------------------------------------------------------------------
# Exercices du cours (blocs « !!! example » de glassus) : exposition supplémentaire pour la
# découverte non supervisée des façons d'interroger. Les corrections sont retirées.
EX_HEAD = re.compile(r'^!!! (?:example|question|exercice)\b.*$', re.M | re.I)
SUBQ = re.compile(r"(?m)^\s*(?:\*\*)?(Q\d+|\d+[.)]|[a-h][.)])(?:\*\*)?\s+(?=\S)")


def ingest_course_exercises() -> list[dict]:
    docs = SOURCES / "glassus_terminale_nsi" / "docs"
    out = []
    for f in sorted(docs.glob("T[1-5]_*/*/*.md")) + sorted(docs.glob("T6_[25]_*/*.md")):
        if "Copie en conflit" in f.name:
            continue
        txt = f.read_text(encoding="utf-8", errors="ignore")
        top = f.parts[len(docs.parts)]
        key = "T6_2" if top.startswith("T6_2") else "T6_5" if top.startswith("T6_5") else top[:2]
        lesson = re.sub(r"^[\d.]+_", "", f.parent.name if not top.startswith("T6") else top).replace("_", " ")
        for m in EX_HEAD.finditer(txt):
            body = []
            for ln in txt[m.end():].split("\n")[1:]:
                if ln.strip() and not ln.startswith(("    ", "\t")):
                    break
                body.append(ln[4:] if ln.startswith("    ") else ln.lstrip("\t"))
            b = "\n".join(body)
            b = re.split(r"\{\{\s*correction|\?\?\?[+]? *(success|note|tip)|=== *\"Correction", b)[0]
            b = re.sub(r"\{\{.*?\}\}", " ", b, flags=re.S)
            b = clean_md(b).strip()
            if len(b) < 60:
                continue
            cuts = [s.start() for s in SUBQ.finditer(b)]
            if len(cuts) >= 2:
                pre, parts = b[:cuts[0]], [b[s:e].strip() for s, e in zip(cuts, cuts[1:] + [len(b)])]
            else:
                pre, parts = "", [b]
            qs = [{"label": str(i + 1), "part": None, "is_sub": False,
                   "context_before": pre[-600:] if i == 0 else "", "text": p[:1500]} for i, p in enumerate(parts) if len(p) > 15]
            if qs:
                out.append({"chapter": CHAPTER_NAMES.get(key, top), "lesson": lesson, "file": f.name,
                            "preamble": pre, "questions": qs})
    print(f"[cours] {len(out)} exercices de cours, {sum(len(e['questions']) for e in out)} questions")
    return out


if __name__ == "__main__":
    run()


# ===== examgen/ingest_extra.py =====
"""Matière supplémentaire d'exposition (aucune variable ajoutée à la main).

Sources :
  codex          exercices CodEx (forge.apps.education.fr) : énoncé + tags + difficulté (étiquettes faibles)
  qcm            banque de QCM de Terminale (forge projets-qcm)
  prof           exercices extraits des cours d'enseignants (blocs !!! / ??? et sections « Exercice »)
  entrainement   fiches PDF « type bac » non officielles des dépôts d'enseignants

Sorties (data/corpus/) :
  exposure.jsonl       même format que exams.jsonl (exercices -> questions), type = source
  course_extra.jsonl   sections de cours d'enseignants, sans chapitre (le modèle les étiquettera seul)
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

from .config import CORPUS, SOURCES
from .ingest import (EXCLUDE, clean_md, clean_pdf_text, is_official, pdf_text, segment_exam,
                     segment_questions, split_md_sections, strip_accents, write_jsonl)

CODEX = SOURCES / "forge_codex_codex.forge.apps.education.fr"
QCM = SOURCES / "forge_projets-qcm_qcm-nsi-terminale"
SKIP_REPOS = {CODEX.name, QCM.name}

ADM = re.compile(r"^(?P<ind>[ \t]*)(?:!!!|\?\?\?\+?)\s*(?P<typ>[\w-]+)(?P<title>[^\n]*)$", re.M)
SOLUTION = re.compile(r"solution|correction|corrig|réponse|reponse|indice|aide|astuce", re.I)
EXO_TYPES = {"example", "question", "exercice", "exo", "exercise", "ex", "travail", "faq", "abstract", "done"}
SUBQ = re.compile(r"(?m)^\s*(?:\*\*)?(Q\d+|\d+[.)]|[a-h][.)])(?:\*\*)?\s+(?=\S)")
FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)


def _hid(*parts) -> str:
    return hashlib.md5("|".join(map(str, parts)).encode()).hexdigest()[:10]


def _exam(typ, src, exercises, **meta):
    exercises = [x for x in exercises if x["questions"]]
    return {"id": f"{typ}-{_hid(src)}", "type": typ, "source": src, "year": None, "center": None, "day": None,
            "kind": typ, "duration_min": None, "n_exercises": len(exercises), "exercises": exercises, **meta}


def _exercise(num, preamble, questions, **extra):
    raw = preamble + "\n" + "\n".join(q["text"] for q in questions)
    return {"number": str(num), "points": None, "theme_sentence": None, "preamble": preamble,
            "raw": raw, "questions": questions, **extra}


def split_block(b: str) -> tuple[str, list[dict]]:
    """Découpe un bloc d'exercice en questions (sous-questions numérotées, sinon bloc unique :
    la consigne est le dernier paragraphe impératif, le reste sert de support)."""
    pre, qs = segment_questions(b)
    if len(qs) >= 2:
        return pre, qs
    cuts = [s.start() for s in SUBQ.finditer(b)]
    if len(cuts) >= 2:
        pre = b[:cuts[0]]
        parts = [b[s:e].strip() for s, e in zip(cuts, cuts[1:] + [len(b)])]
        return pre, [{"label": str(i + 1), "part": None, "is_sub": False,
                      "context_before": pre[-600:] if i == 0 else "", "text": p[:1500]}
                     for i, p in enumerate(parts) if len(p) > 15]
    paras = [p for p in re.split(r"\n\s*\n", b) if p.strip()]
    if not paras:
        return "", []
    from .ingest import INSTR_RE
    k = max((i for i, p in enumerate(paras) if INSTR_RE.search(p) or "?" in p), default=len(paras) - 1)
    # la consigne peut se prolonger par une liste à puces
    end = k + 1
    while end < len(paras) and re.match(r"\s*[-*•]", paras[end]):
        end += 1
    stem = "\n\n".join(paras[k:end])
    ctx = "\n\n".join(paras[:k] + paras[end:])
    return "", [{"label": "1", "part": None, "is_sub": False, "context_before": ctx[-1500:], "text": stem[:1500]}]


# ----------------------------------------------------------------------------------- CodEx
def _front(txt):
    m = FRONT.match(txt)
    meta = {}
    if not m:
        return meta, txt
    cur = None
    for ln in m.group(1).splitlines():
        if (kv := re.match(r"^(\w+):\s*(.*)$", ln)):
            cur = kv.group(1)
            meta[cur] = kv.group(2).strip() or []
        elif cur and (it := re.match(r"^\s+-\s*(.+)$", ln)) and isinstance(meta[cur], list):
            meta[cur].append(it.group(1).strip())
    return meta, txt[m.end():]


def _strip_solutions(txt: str) -> str:
    """Retire les blocs-réponses (admonitions dont le titre parle de solution/correction)."""
    out, skip_ind = [], None
    for ln in txt.splitlines():
        if skip_ind is not None:
            if not ln.strip() or len(ln) - len(ln.lstrip()) > skip_ind:
                continue
            skip_ind = None
        m = ADM.match(ln)
        if m and (SOLUTION.search(m.group("title")) or m.group("typ") in ("success", "done", "check")):
            skip_ind = len(m.group("ind").expandtabs(4))
            continue
        out.append(ln)
    return "\n".join(out)


def ingest_codex() -> list[dict]:
    out = []
    for kind in ("exercices", "exam"):
        for f in sorted((CODEX / "docs" / kind).glob("*/index.md")):
            meta, body = _front(f.read_text(encoding="utf-8", errors="ignore"))
            body = re.sub(r"`#!py ([^`]*)`", r"`\1`", _strip_solutions(body))
            body = re.sub(r"\{\{\s*IDE\([^}]*\}\}", "\n", body)
            b = clean_md(body)
            if len(b) < 80:
                continue
            pre, qs = split_block(b)
            if not qs:
                continue
            diff = meta.get("difficulty")
            tags = meta.get("tags") if isinstance(meta.get("tags"), list) else []
            ex = _exercise(1, pre, qs, title=meta.get("title"), tags=tags,
                           difficulty=int(diff) if isinstance(diff, str) and diff.isdigit() else None)
            out.append(_exam("codex", str(f.relative_to(SOURCES)), [ex], tags=tags,
                             difficulty=ex["difficulty"], center=meta.get("title")))
    print(f"[codex] {len(out)} exercices, {sum(len(x['questions']) for e in out for x in e['exercises'])} questions")
    return out


# ----------------------------------------------------------------------------------- QCM
def _txt(h: str) -> str:
    h = re.sub(r"<br\s*/?>|</p>|</li>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    return re.sub(r"[ \t\xa0]+", " ", html.unescape(h)).strip()


def ingest_qcm() -> list[dict]:
    seen, exams = set(), []
    for f in sorted(QCM.rglob("*.json")):
        try:
            data = json.load(f.open(encoding="utf-8"))
        except Exception:
            continue
        qs = data.get("questions") if isinstance(data, dict) else None
        if not isinstance(qs, list):
            continue
        exs = []
        for q in qs:
            if not (isinstance(q, list) and len(q) >= 2 and isinstance(q[1], list)):
                continue
            stem = _txt(q[0])
            key = re.sub(r"\W+", "", stem.lower())[:200]
            if len(stem) < 15 or key in seen:
                continue
            seen.add(key)
            choices = "\n".join(f"{chr(65 + i)}. {_txt(c)}" for i, c in enumerate(q[1]))
            exs.append(_exercise(len(exs) + 1, "", [{"label": "1", "part": None, "is_sub": False,
                                                     "context_before": "", "text": stem + "\n" + choices}]))
        if exs:
            exams.append(_exam("qcm", str(f.relative_to(SOURCES)), exs))
    n = sum(len(e["exercises"]) for e in exams)
    print(f"[qcm] {n} questions distinctes")
    return exams


# ----------------------------------------------------------------------------------- enseignants
def _md_files():
    for repo in sorted(SOURCES.glob("forge_*")):
        if repo.name in SKIP_REPOS:
            continue
        for f in sorted(repo.rglob("*.md")):
            if any(p.startswith(".") for p in f.relative_to(repo).parts) or EXCLUDE.search(f.name):
                continue
            yield repo, f


def _admonition_blocks(txt: str):
    lines = txt.splitlines()
    i = 0
    while i < len(lines):
        m = ADM.match(lines[i])
        if m and (m.group("typ").lower() in EXO_TYPES and not SOLUTION.search(m.group("title"))
                  or re.search(r"exercice|question|à faire", m.group("title"), re.I)):
            ind = len(m.group("ind").expandtabs(4))
            body = []
            j = i + 1
            while j < len(lines) and (not lines[j].strip() or len(lines[j].expandtabs(4)) - len(lines[j].expandtabs(4).lstrip()) > ind):
                body.append(lines[j].expandtabs(4)[ind + 4:] if lines[j].strip() else "")
                j += 1
            yield m.group("title").strip(' "'), "\n".join(body)
            i = j
        else:
            i += 1


def _heading_blocks(txt: str):
    for title, body in split_md_sections(txt):
        if re.search(r"\bexercices?\b|\bexo\b", title, re.I):
            yield title, body


def ingest_teacher_md() -> tuple[list[dict], list[dict]]:
    exams, course, seen = [], [], set()
    for repo, f in _md_files():
        raw = f.read_text(encoding="utf-8", errors="ignore")
        raw = FRONT.sub("", raw)
        exs = []
        for title, body in list(_admonition_blocks(raw)) + list(_heading_blocks(raw)):
            b = clean_md(re.sub(r"\{\{.*?\}\}", " ", _strip_solutions(body), flags=re.S)).strip()
            key = re.sub(r"\W+", "", b.lower())[:300]
            if len(b) < 60 or key in seen:
                continue
            seen.add(key)
            pre, qs = split_block(b)
            if qs:
                exs.append(_exercise(len(exs) + 1, pre, qs, title=title))
        rel = str(f.relative_to(SOURCES))
        if exs:
            exams.append(_exam("prof", rel, exs, center=f.parent.name))
        # sections de cours (hors fichiers d'exercices) : matière non étiquetée
        if not re.search(r"exo|exercice|td|tp|correction|qcm", f.stem, re.I):
            body = clean_md(_strip_solutions(re.sub(r"\{\{.*?\}\}", " ", raw, flags=re.S)))
            for title, txt in split_md_sections(body):
                key = re.sub(r"\W+", "", txt.lower())[:300]
                if len(txt.strip()) >= 200 and key not in seen:
                    seen.add(key)
                    course.append({"source": repo.name.removeprefix("forge_"), "chapter": None,
                                   "lesson": f.parent.name, "kind": "cours", "title": title,
                                   "file": rel, "text": txt.strip()[:6000]})
    print(f"[prof] {len(exams)} fichiers, {sum(len(e['exercises']) for e in exams)} exercices, "
          f"{sum(len(x['questions']) for e in exams for x in e['exercises'])} questions ; {len(course)} sections de cours")
    return exams, course


def ingest_training_pdfs() -> list[dict]:
    """Fiches PDF non officielles (TD, « type bac », bacs blancs) : énoncés sans correction."""
    out = []
    for repo in sorted(SOURCES.glob("forge_*")):
        for p in sorted(repo.rglob("*.pdf")):
            if EXCLUDE.search(str(p.relative_to(repo))):
                continue
            raw = pdf_text(p)
            if len(raw) < 800 or is_official(raw):
                continue
            txt = clean_pdf_text(raw)
            head = strip_accents(txt[:1500].lower())
            if "correction" in head or "corrige" in head or "solution" in head:
                continue
            exs = segment_exam(txt)
            if len(exs) < 2:
                pre, qs = segment_questions(txt)
                if len(qs) < 2:
                    continue
                exs = [_exercise(1, pre[-2000:], qs)]
            out.append(_exam("entrainement", str(p.relative_to(SOURCES)), exs, center=p.stem))
    print(f"[entraînement] {len(out)} fiches PDF, {sum(len(x['questions']) for e in out for x in e['exercises'])} questions")
    return out


def run():
    exposure = ingest_codex() + ingest_qcm()
    tex, course = ingest_teacher_md()
    exposure += tex + ingest_training_pdfs()
    write_jsonl(CORPUS / "exposure.jsonl", exposure)
    write_jsonl(CORPUS / "course_extra.jsonl", course)


if __name__ == "__main__":
    run()


# ===== examgen/llm.py =====
"""Rédaction des questions par le LLM (Opus 5.5, effort low).

Deux chemins :
  api     : appel direct à l'API Anthropic (nécessite ANTHROPIC_API_KEY)
  agents  : export des consignes dans output/prompts/*.md ; des agents Claude Code
            (Opus 5.5, effort low) écrivent output/generated/<id>.json
Les deux produisent le même format JSON (OUTPUT_SCHEMA).
"""
from __future__ import annotations

import json
import os
import sys

from .config import LLM_EFFORT, LLM_MODEL, OUT

PROMPTS = OUT / "prompts"
GENERATED = OUT / "generated"
for p in (PROMPTS, GENERATED):
    p.mkdir(parents=True, exist_ok=True)

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "exercices": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "numero": {"type": "integer"},
                "titre": {"type": "string"},
                "contexte": {"type": "string"},
                "questions": {"type": "array", "items": {
                    "type": "object",
                    "properties": {
                        "slot": {"type": "integer"},
                        "notion": {"type": "string"},
                        "enonce": {"type": "string"},
                        "points": {"type": "number"},
                        "reponse_attendue": {"type": "string"},
                    },
                    "required": ["slot", "notion", "enonce", "points", "reponse_attendue"],
                    "additionalProperties": False,
                }},
            },
            "required": ["numero", "titre", "contexte", "questions"],
            "additionalProperties": False,
        }},
    },
    "required": ["id", "exercices"],
    "additionalProperties": False,
}

SYSTEM = """Tu es concepteur de sujets du baccalauréat, spécialité NSI (Terminale).
Tu rédiges des questions NOUVELLES à partir d'un plan produit par une analyse statistique
de 83 sujets officiels (2021-2026) et du cours. Le plan fixe, question par question :
la notion visée, l'archétype (forme de la question), le niveau de Bloom, la position et le barème.

Règles :
- Respecte le plan dans l'ordre : une question par « slot », même notion, même archétype.
- Style officiel : consignes à l'infinitif (« Écrire une fonction… », « Justifier… »),
  code Python 3 complet et exécutable, lignes de code numérotées quand on demande de compléter,
  requêtes SQL standard, tableaux en Markdown.
- Le contexte d'exercice est original (pas de copie des exemples réels, qui ne servent qu'au ton).
- Chaque question est autonome dans sa formulation mais s'appuie sur le contexte de l'exercice ;
  quand le plan dit « dépend de la précédente », réutilise explicitement le résultat ou la
  fonction de la question précédente.
- Reste strictement dans le programme de Terminale NSI (extraits de cours fournis).
- reponse_attendue : corrigé bref mais exact (code complet si c'est du code).
- En mode banque, chaque question porte son propre mini-contexte dans « enonce » ; un seul
  exercice numéro 0 regroupe les questions.
Réponds uniquement avec le JSON demandé."""


def render_prompt(plan: dict) -> str:
    lines = [f"# Plan {plan['id']} ({plan['type']})", ""]
    if plan["type"] == "sujet":
        lines.append(plan["format"])
        for ex in plan["exercices"]:
            lines += ["", f"## Exercice {ex['numero']} ({ex['points']} points)",
                      f"Notions : {', '.join(ex['notions'])} — domaines : {', '.join(ex['domaines'])}",
                      f"Pistes de contexte (mots fréquents d'anciens scénarios, à réinventer) : {', '.join(ex['idee_de_contexte'])}",
                      "Extraits du cours :"]
            for c in ex["cours"]:
                lines.append(f"> [{c['ref']}]\n> " + c["texte"][:700].replace("\n", "\n> "))
            lines.append("Questions à rédiger :")
            for q in ex["questions"]:
                lines.append(
                    f"- slot {q['slot']} | notion={q['notion']} | archétype={q['archetype']} | Bloom={q['bloom_cible']} | "
                    f"{q['points']} pt | position={q['position_cible']} | dépend de la précédente={'oui' if q['depend_de_la_precedente'] else 'non'} | "
                    f"formulations typiques : {', '.join(q['formulations_typiques'])}")
                for ex_ in q["exemples_reels_de_style"]:
                    lines.append(f"    style réel : « {ex_[:220].strip()} »")
    elif plan["type"] == "inedit":
        lines += [f"Notion : {plan['notion']} ({plan['domaine']}) — questions JAMAIS POSÉES aux annales", "",
                  "Ces questions viennent d'une analyse non supervisée. Elle a appris, sans lexique écrit à la main, les "
                  "manières de demander (facettes de consigne) et les types de matériau fourni (facettes de support) des "
                  "vraies questions. Chaque slot ci-dessous associe la notion à une manière de demander ou à un support que "
                  "les annales n'ont jamais utilisés pour elle. Le modèle juge pourtant ce mélange aussi plausible qu'une "
                  "vraie question. Ou bien le slot vise un détail du cours jamais interrogé.", "",
                  "Règles propres à ce mode :",
                  "- Une question = un exercice : numero = slot ; contexte = mise en situation et matériau (code, table, "
                  "schéma décrit, appel…), conforme au support demandé ; enonce = la consigne SEULE, une ou deux phrases.",
                  "- La consigne applique le geste de la facette à la notion visée. Les exemples viennent d'autres notions : "
                  "imite leur MANIÈRE de demander et le détail qu'ils évaluent, jamais leur sujet.",
                  "- La question doit rester faisable par un élève de Terminale et corrigeable sans ambiguïté.",
                  "", "Extraits du cours :"]
        for c in plan["cours"]:
            lines.append(f"> [{c['ref']}]\n> " + c["texte"][:900].replace("\n", "\n> "))
        lines.append("")
        lines.append("Questions à rédiger (points = 1 par défaut) :")
        for q in plan["questions"]:
            c = q["consigne"]
            lines += ["", f"- slot {q['slot']} | {q['mode']} | {q['nouveaute']} | position visée : {q['position']}",
                      f"    manière de demander {c['id']} : {c['nom']}" + (f" — {c['geste']}" if c["geste"] else "")]
            if c["gabarit"]:
                lines.append(f"    gabarit : {c['gabarit']}")
            for e in q["exemples_de_consigne_autres_notions"]:
                lines.append(f"    exemple réel (autre notion) : « {e[:240]} »")
            if q["mode"] == "combinaison_inedite":
                s = q["support"]
                lines.append(f"    support {s['id']} : {s['nom']}" + (f" — {s['geste']}" if s["geste"] else ""))
                for e in q["exemple_de_support_autre_notion"]:
                    lines.append(f"    exemple de support (autre notion) : « {e[:260]} »")
            else:
                lines.append(f"    détail du cours à évaluer ({q['lecon']}) : « {q['atome_du_cours']} »")
    else:
        lines += [f"Notion : {plan['notion']} ({plan['domaine']}) — banque de questions isolées", "Extraits du cours :"]
        for c in plan["cours"]:
            lines.append(f"> [{c['ref']}]\n> " + c["texte"][:900].replace("\n", "\n> "))
        lines.append("Questions à rédiger (exercice numéro 0, points = 1 par défaut) :")
        for q in plan["questions"]:
            lines.append(f"- slot {q['slot']} | archétype={q['archetype']} | Bloom={q['bloom_cible']} | formulations typiques : {', '.join(q['formulations_typiques'])}")
            for ex_ in q["exemples_reels_de_style"]:
                lines.append(f"    style réel : « {ex_[:220].strip()} »")
    lines += ["", f"Le champ id vaut « {plan['id']} »."]
    return "\n".join(lines)


def export_prompts(plans: list[dict]) -> list[str]:
    ids = []
    for pl in plans:
        (PROMPTS / f"{pl['id']}.md").write_text(render_prompt(pl), encoding="utf-8")
        ids.append(pl["id"])
    (PROMPTS / "_system.md").write_text(SYSTEM, encoding="utf-8")
    (PROMPTS / "_schema.json").write_text(json.dumps(OUTPUT_SCHEMA, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[ok] {len(ids)} consignes -> {PROMPTS}")
    return ids


def generate_api(plans: list[dict]) -> None:
    """Chemin API direct : Opus 5.5, effort low, sortie JSON contrainte par schéma."""
    import anthropic

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY absent : utiliser le chemin « agents » (voir README).")
    client = anthropic.Anthropic()
    for pl in plans:
        out = GENERATED / f"{pl['id']}.json"
        if out.exists():
            continue
        with client.messages.stream(
            model=LLM_MODEL,
            max_tokens=32000,
            system=SYSTEM,
            messages=[{"role": "user", "content": render_prompt(pl)}],
            output_config={"effort": LLM_EFFORT, "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA}},
        ) as stream:
            msg = stream.get_final_message()
        if msg.stop_reason == "refusal":
            print(f"  ! {pl['id']} refusé")
            continue
        if msg.stop_reason == "max_tokens":
            print(f"  ! {pl['id']} tronqué")
            continue
        text = next(b.text for b in msg.content if b.type == "text")
        out.write_text(json.dumps(json.loads(text), ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  · {pl['id']} ({msg.usage.output_tokens} tokens)")


# ===== examgen/meta/__init__.py =====
"""Méta-apprentissage : apprendre au moteur à s'entraîner seul sur n'importe quelle matière, à
partir de deux choses seulement (anciens sujets + cours). Voir learn.py."""


# ===== examgen/meta/align.py =====
"""Méta-apprentissage de l'alignement question -> cours, sans vérité terrain au moment de l'emploi.

Le problème : sur une matière nouvelle, il n'y a pas forcément de corrigés qui disent quelle
partie du cours chaque question évalue. Le moteur doit alors régler seul sa lecture du texte
(représentation, poids de l'énoncé, de la situation, des documents, des références communes).

L'idée (apprendre à apprendre) :
  1. des signaux auto-supervisés, calculables sur n'importe quel corpus sans étiquette :
       coherence_partie   les questions d'une même partie visent des sections voisines, et des
                          parties différentes des sections différentes (information mutuelle) ;
       accord_des_vues    l'énoncé seul et la situation + documents seuls désignent la même section ;
       retrouve_partie    projetée sur le cours, une question retrouve sa propre partie ;
       marge              l'alignement tranche (écart entre la 1re et la 2e section) ;
       diversite          le cours entier est utilisé (pas d'effondrement sur une section) ;
  2. des épisodes : sous-ensembles de sujets et de chapitres du cours, dans chaque matière
     disponible ; pour chaque réglage candidat on mesure les signaux ET la vraie réussite
     (étiquettes d'évaluation, cachées au moteur) ;
  3. le méta-modèle apprend quelle combinaison des signaux désigne les bons réglages ;
  4. preuve de généralité : appris sur une matière, appliqué à l'autre qu'il n'a jamais vue
     (matière exclue), comparé au réglage par défaut et au meilleur réglage possible (oracle).
"""
from __future__ import annotations

import itertools

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import normalized_mutual_info_score as nmi

CFGS = [dict(analyzer=an, ngram=ng, a=a) for an, ng in (("word", (1, 1)), ("word", (1, 2)), ("char_wb", (3, 5)))
        for a in (0.2, 0.5, 0.8)]
WGRID = [(wa, wx, ws, wi) for wa in (0, 1) for wx in (0, 0.5, 1) for ws in (0, 0.25, 0.5) for wi in (0, 1)]
PROXIES = ["coherence_partie", "accord_des_vues", "retrouve_partie", "marge", "diversite"]


def views(t, cfg: dict) -> dict:
    """Matrices question x section pour chaque source de texte, sous un réglage de lecture."""
    t.cfg = dict(cfg)
    t._fit_vectorizer()
    Q = t.Q
    anx = [" ".join(a + " " + x for a, x in q.annexes)[:8000] for q in Q]
    V = {"stem": t.sec_scores([q.stem + " " + q.preamble for q in Q]),
         "ans": t.sec_scores([q.answer or q.stem for q in Q]),
         "anx": t.sec_scores(anx),
         "sit": t.sec_scores([q.situation[:3000] for q in Q]),
         "ids": t.id_bonus([q.stem + " " + q.answer + " " + a for q, a in zip(Q, anx)]),
         "has_ans": np.array([bool(q.answer) for q in Q])}
    parts = {}
    V["part"] = np.array([parts.setdefault((q.exam, q.part), len(parts)) for q in Q])
    V["exam"] = np.array([q.exam for q in Q])
    return V


def combine(V: dict, w) -> np.ndarray:
    return V["stem"] + w[0] * np.where(V["has_ans"][:, None], V["ans"], 0) + w[1] * V["anx"] + w[2] * V["sit"] + w[3] * V["ids"]


def _rownorm(M):
    return M / (np.linalg.norm(M, axis=1, keepdims=True) + 1e-9)


def proxies(V: dict, S: np.ndarray, idx: np.ndarray, cols: np.ndarray) -> dict:
    S = S[np.ix_(idx, cols)]
    top = S.argmax(1)
    srt = np.sort(S, 1)
    ctx = (V["sit"] + V["anx"])[np.ix_(idx, cols)]
    stem = V["stem"][np.ix_(idx, cols)]
    part = V["part"][idx]
    # retrouver sa partie : énoncé projeté sur le cours vs contexte projeté de chaque partie
    up = np.unique(part)
    P = _rownorm(np.vstack([ctx[part == p].mean(0) for p in up]))
    R = _rownorm(stem) @ P.T
    own = R[np.arange(len(part)), np.searchsorted(up, part)]
    rank = (R > own[:, None]).sum(1) + 1
    cnt = np.bincount(top, minlength=len(cols)) / len(top)
    ent = -(cnt[cnt > 0] * np.log(cnt[cnt > 0])).sum() / np.log(len(cols))
    return {"coherence_partie": nmi(part, top),
            "accord_des_vues": nmi(stem.argmax(1), ctx.argmax(1)),
            "retrouve_partie": float(np.mean(1 / rank)),
            "marge": float(np.mean((srt[:, -1] - srt[:, -2]) / (srt[:, -1] + 1e-9))) if len(cols) > 1 else 0.0,
            "diversite": float(ent)}


def truth(S: np.ndarray, labels: dict, idx: np.ndarray, cols: np.ndarray) -> float | None:
    """Réussite top 3 sur les questions étiquetées de l'épisode (évaluation seulement)."""
    pos = {c: j for j, c in enumerate(cols)}
    hits = []
    for i in idx:
        if i not in labels:
            continue
        lab = {pos[c] for c in labels[i] if c in pos}
        if not lab:
            continue
        top3 = set(np.argsort(-S[i, cols])[:3])
        hits.append(bool(lab & top3))
    return float(np.mean(hits)) if len(hits) >= 10 else None


def episodes(t, labels: dict, n: int, rng) -> list[tuple[np.ndarray, np.ndarray]]:
    """Sous-ensembles (questions, sections) : 60 % des sujets, et la moitié des épisodes sur une
    partie seulement des chapitres du cours (une « nouvelle matière » simulée)."""
    exams = np.array(sorted({q.exam for q in t.Q}))
    qex = np.array([q.exam for q in t.Q])
    parents = sorted({s.parent for s in t.sections})
    out = []
    tries = 0
    while len(out) < n and tries < n * 20:
        tries += 1
        ex = rng.choice(exams, size=max(3, int(0.6 * len(exams))), replace=False)
        idx = np.where(np.isin(qex, ex))[0]
        cols = np.arange(len(t.sections))
        if len(out) % 2 and len(parents) >= 3:
            keep = set(rng.choice(parents, size=max(2, int(0.6 * len(parents))), replace=False))
            cols = np.array([i for i, s in enumerate(t.sections) if s.parent in keep])
            # on garde les questions dont la notion est dans les chapitres retenus, plus autant
            # de questions non étiquetées (le moteur ne sait pas lesquelles le sont)
            cs = set(cols.tolist())
            idx = np.array([i for i in idx if i not in labels or labels[i] & cs])
        if len(idx) >= 30 and len(cols) >= 4:
            out.append((idx, cols))
    return out


def collect(t, labels: dict, n_ep: int = 16, seed: int = 0) -> list[dict]:
    """Pour chaque épisode et chaque réglage candidat : signaux auto-supervisés + vraie réussite."""
    rng = np.random.default_rng(seed)
    eps = episodes(t, labels, n_ep, rng)
    rows = []
    for ci, cfg in enumerate(CFGS):
        V = views(t, cfg)
        for wi, w in enumerate(WGRID):
            if w[0] and not V["has_ans"].any():
                continue
            S = combine(V, w)
            for ei, (idx, cols) in enumerate(eps):
                tr = truth(S, labels, idx, cols)
                if tr is None:
                    continue
                rows.append({"episode": ei, "cfg": ci, "w": wi, "vrai": tr, **proxies(V, S, idx, cols)})
    return rows


def _z(x):
    x = np.asarray(x, float)
    return (x - x.mean()) / (x.std() + 1e-9)


def design(rows: list[dict]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Signaux standardisés dans chaque épisode (on compare des réglages entre eux, pas des épisodes)."""
    eps = np.array([r["episode"] for r in rows])
    X = np.zeros((len(rows), len(PROXIES)))
    y = np.zeros(len(rows))
    for e in np.unique(eps):
        m = eps == e
        for j, p in enumerate(PROXIES):
            X[m, j] = _z([rows[i][p] for i in np.where(m)[0]])
        y[m] = _z([rows[i]["vrai"] for i in np.where(m)[0]])
    return X, y, eps


def fit_meta(rows: list[dict]) -> Ridge:
    X, y, _ = design(rows)
    return Ridge(alpha=1.0, fit_intercept=False).fit(X, y)


def pick(model: Ridge, rows: list[dict]) -> dict:
    """Dans chaque épisode, le réglage que le méta-modèle choisit, sans voir la vérité."""
    X, _, eps = design(rows)
    pred = model.predict(X)
    chosen, oracle, default, worst = [], [], [], []
    d_cfg = CFGS.index(dict(analyzer="word", ngram=(1, 2), a=0.5))
    for e in np.unique(eps):
        ids = np.where(eps == e)[0]
        chosen.append(rows[ids[pred[ids].argmax()]]["vrai"])
        oracle.append(max(rows[i]["vrai"] for i in ids))
        worst.append(min(rows[i]["vrai"] for i in ids))
        dd = [rows[i]["vrai"] for i in ids if rows[i]["cfg"] == d_cfg and rows[i]["w"] == 0]
        default.append(dd[0] if dd else np.nan)
    return {"choisi_par_le_meta_modele": round(float(np.mean(chosen)), 3),
            "reglage_par_defaut": round(float(np.nanmean(default)), 3),
            "meilleur_possible_oracle": round(float(np.mean(oracle)), 3),
            "pire_reglage": round(float(np.mean(worst)), 3),
            "episodes": int(len(np.unique(eps)))}


def self_tune(t, model_coef: list[float]) -> tuple[dict, tuple, dict]:
    """Emploi sur une matière nouvelle, sans étiquette : le moteur essaie les réglages et garde
    celui que la règle méta-apprise juge le meilleur."""
    idx = np.arange(len(t.Q))
    cols = np.arange(len(t.sections))
    cand = []
    for cfg in CFGS:
        V = views(t, cfg)
        for w in WGRID:
            if w[0] and not V["has_ans"].any():
                continue
            cand.append((cfg, w, proxies(V, combine(V, w), idx, cols)))
    X = np.column_stack([_z([c[2][p] for c in cand]) for p in PROXIES])
    best = int((X @ np.asarray(model_coef)).argmax())
    cfg, w, px = cand[best]
    t.cfg = dict(cfg)
    t._fit_vectorizer()
    return cfg, w, px


# ===== examgen/meta/autoprog.py =====
"""Auto-progression de la prévision par méta-apprentissage.

Le moteur ne reçoit que les anciens sujets et le cours. À partir de là :
  1. il FABRIQUE des familles de variables candidates, sans rien de propre à une matière :
     mémoire pondérée (oubli appris), voisinage dans le cours, proximité avec ce qui a déjà été
     demandé, lexique du professeur (ses énoncés et corrigés), rotation des chapitres, thèmes
     découverts dans le cours ;
  2. génération après génération, il ajoute la famille qui améliore le plus ses résultats, jugés
     sur ses propres années passées seulement (validation « année exclue ») ; il s'arrête quand
     plus rien n'aide ;
  3. méta-apprentissage entre matières : ce qui a marché ailleurs devient un a priori (bonus
     aux familles retenues par les autres matières, choix du modèle), utile quand une matière
     a trop peu d'années pour trancher seule ;
  4. deux objectifs appris séparément : « ce qui va tomber » (tout le cours) et « ce qui peut
     tomber pour la première fois » (passages jamais demandés).
Preuve : pour chaque année testée, TOUT (variables, modèle) est choisi sans cette année ni les
suivantes, puis comparé au vrai sujet.
  python -m examgen.meta.autoprog droit nsi eco
"""
from __future__ import annotations

import json
import os

import sys
import warnings
from pathlib import Path

import numpy as np
from scipy.stats import rankdata
from sklearn.linear_model import LogisticRegression
from ..fast import auc as roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from . import loop as LP

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "meta" / "autoprog.json"
RULE = ROOT / "data" / "model" / "autoprog.json"
LAMBDA = 0.5  # poids de l'a priori venu des autres matières (même valeur partout)
TOP = 0.10

GROUPS = ["recence", "memoire_ponderee", "voisinage", "proximite_au_deja_demande", "lexique_du_professeur",
          "rotation_des_chapitres", "themes_du_cours"]


class Vars:
    """Variables d'un passage pour une année cible, calculées à partir des seules années `hist`."""

    def __init__(self, fc):
        self.fc, t = fc, fc.t
        self.n, self.ps = fc.n, np.asarray(t.pass_sec)
        self.K = len(t.sections)
        self.P = t.P
        qtext = {}
        for i, q in enumerate(t.Q):
            if q.year:
                qtext.setdefault(q.year, []).append(q.stem + " " + q.situation[:1500] + " " + (q.answer or "")[:1500])
        self.Qy = {y: t.vec.transform(v) for y, v in qtext.items()}
        self.cache = {}

    def get(self, target: int, hist: list[int]) -> dict:
        key = (target, tuple(hist))
        if key in self.cache:
            return self.cache[key]
        fc, n, ps, K = self.fc, self.n, self.ps, self.K
        X = fc.rows(target, hist)
        hist = [z for z in hist if z != target] or [z for z in fc.years if z != target]
        tested = {z: np.array([p in fc.tested[z] for p in range(n)], float) for z in hist}
        pf = X[:, 10]
        g = {"base": X[:, :12], "recence": X[:, 12:15]}
        # mémoire pondérée : une année compte d'autant moins qu'elle est loin de la cible
        cols = []
        for h in (1.0, 3.0):
            w = {z: 0.5 ** (abs(target - z) / h) for z in hist}
            pw = sum(w[z] * tested[z] for z in hist) / sum(w.values())
            sw = np.array([pw[ps == s].max() if (ps == s).any() else 0 for s in range(K)])
            cols += [pw, sw[ps]]
        g["memoire_ponderee"] = np.column_stack(cols)
        # voisinage : les passages voisins (même chapitre) déjà demandés
        nb = np.zeros(n)
        mates = np.zeros(n)
        for p in range(n):
            v = [pf[p + d] for d in (-2, -1, 1, 2) if 0 <= p + d < n and ps[p + d] == ps[p]]
            nb[p] = np.mean(v) if v else 0
            m = ps == ps[p]
            mates[p] = (pf[m].sum() - pf[p]) / max(1, m.sum() - 1)
        g["voisinage"] = np.column_stack([nb, mates])
        # proximité (contenu) avec ce qui a déjà été demandé, et avec l'an dernier
        seen = np.where(sum(tested.values()) > 0)[0]
        before = [z for z in hist if z < target]
        last = np.where(tested[max(before)] > 0)[0] if before else np.array([], int)
        def sim_to(idx):
            if not len(idx):
                return np.zeros(n), np.zeros(n)
            S = (self.P @ self.P[idx].T).toarray()
            S[np.arange(n)[:, None] == idx[None, :]] = 0  # pas de soi-même
            top3 = -np.sort(-S, 1)[:, :3].mean(1)
            return S.max(1), top3
        a, b = sim_to(seen)
        c, _ = sim_to(last)
        g["proximite_au_deja_demande"] = np.column_stack([a, b, c])
        # lexique du professeur : ce dont parlent ses énoncés et corrigés des années connues
        Q = [self.Qy[z] for z in hist if z in self.Qy]
        if Q:
            from scipy.sparse import vstack
            Qm = vstack(Q)
            S = (self.P @ Qm.T).toarray()
            cen = np.asarray(Qm.mean(0)).ravel()
            cs = self.P @ cen / (np.linalg.norm(cen) + 1e-9)
            g["lexique_du_professeur"] = np.column_stack([S.max(1), -np.sort(-S, 1)[:, :5].mean(1), np.asarray(cs).ravel()])
        else:
            g["lexique_du_professeur"] = np.zeros((n, 3))
        # rotation : un chapitre tombé l'an dernier, ou souvent, a-t-il moins de chances ?
        sec_years = np.array([sum(tested[z][ps == s].any() for z in hist) for s in range(K)], float) / len(hist)
        streak = np.zeros(K)
        for s in range(K):
            for z in sorted(before, reverse=True):
                if tested[z][ps == s].any():
                    streak[s] += 1
                else:
                    break
        share = np.array([(ps == s).mean() for s in range(K)])
        g["rotation_des_chapitres"] = np.column_stack([sec_years[ps], streak[ps], sec_years[ps] - share[ps] * len(set(ps))])
        g["themes_du_cours"] = np.hstack([fc.T, fc.T * pf[:, None]])
        self.cache[key] = g
        return g

    def matrix(self, target, hist, groups) -> np.ndarray:
        g = self.get(target, hist)
        return np.hstack([g["base"]] + [g[k] for k in groups])


# ---------------------------------------------------------------------------- modèles
def _lr():
    return make_pipeline(StandardScaler(), LogisticRegression(C=0.3, max_iter=3000, class_weight="balanced"))


MODELS = {"logistique": _lr, "arbres": LP._hgb}


def fit_predict(model, Xtr, ytr, Xte):
    if model == "melange":
        return np.mean([rankdata(fit_predict(m, Xtr, ytr, Xte)) for m in MODELS], 0) / len(Xte)
    return MODELS[model]().fit(Xtr, ytr).predict_proba(Xte)[:, 1]


MODEL_NAMES = list(MODELS) + ["melange"]


class Search:
    """Évalue une configuration (familles de variables, modèle, objectif) sur des années données."""

    def __init__(self, fc):
        self.fc, self.V = fc, Vars(fc)
        self.n = fc.n
        self.memo = {}

    def y(self, z):
        return np.array([p in self.fc.tested[z] for p in range(self.n)], int)

    def predict(self, groups, model, target, train, objective="prevision"):
        key = (tuple(sorted(groups)), model, target, tuple(train), objective)
        if key in self.memo:
            return self.memo[key]
        if model == "melange":  # réutilise les deux modèles déjà appris
            p = np.mean([rankdata(self.predict(groups, m, target, train, objective)) for m in MODELS], 0) / self.n
            self.memo[key] = p
            return p
        Xs, ys = [], []
        for z in train:
            X, yz = self.V.matrix(z, train, groups), self.y(z)
            if objective == "nouveaute":  # apprendre sur les passages encore jamais demandés cette année-là
                others = [w for w in train if w != z]
                fresh = ~np.any([self.y(w) for w in others], 0) if others else np.ones(self.n, bool)
                X, yz = X[fresh], yz[fresh]
            Xs.append(X)
            ys.append(yz)
        Xtr, ytr = np.vstack(Xs), np.concatenate(ys)
        p = np.zeros(self.n) if len(set(ytr)) < 2 else fit_predict(model, Xtr, ytr, self.V.matrix(target, train, groups))
        self.memo[key] = p
        return p

    def score(self, p, target, past, objective):
        """Prévision : questions couvertes par 10 % du cours (+ 0,1 AUC).
        Nouveauté : nouvelles questions couvertes par le quart des passages jamais demandés (+ 0,1 AUC)."""
        fc, yt = self.fc, self.y(target)
        qs = fc.q_of[target]
        if objective == "prevision":
            sel = set(np.argsort(-p)[:max(1, int(TOP * self.n))])
            cov = np.mean([int(fc.it.pas[i]) in sel for i in qs]) if qs else 0
            auc = roc_auc_score(yt, p) if len(set(yt)) > 1 else 0.5
            return {"couverture": cov, "auc": auc, "score": cov + 0.1 * auc}
        seen = set().union(*(fc.tested[z] for z in past)) if past else set()
        fresh = np.array([q not in seen for q in range(self.n)])
        idx = np.where(fresh)[0]
        if len(idx) < 10 or len(set(yt[fresh])) < 2:
            return None
        sel = set(idx[np.argsort(-p[idx])[:max(1, int(0.25 * len(idx)))]].tolist())
        new = [i for i in qs if int(fc.it.pas[i]) not in seen]
        cov = np.mean([int(fc.it.pas[i]) in sel for i in new]) if new else 0
        auc = roc_auc_score(yt[fresh], p[fresh])
        return {"couverture": cov, "auc": auc, "score": cov + 0.1 * auc, "n": len(new)}

    def inner(self, groups, model, past, objective) -> float:
        """Validation « année exclue » à l'intérieur des années passées seulement."""
        sc = []
        for z in past:
            tr = [w for w in past if w != z]
            if len(tr) < 2:
                continue
            p = self.predict(groups, model, z, tr, objective)
            r = self.score(p, z, tr, objective)
            if r:
                sc.append(r["score"])
        return float(np.mean(sc)) if sc else 0.0

    def choose(self, past, objective, prior=None):
        """Configuration choisie par générations. Le choix est fait sur peu d'années, donc bruité :
        la prédiction finale moyenne ses rangs avec ceux de l'ancienne méthode (vérifié sur les
        trois matières : AUC meilleure partout, couverture meilleure ou égale 5 fois sur 6)."""
        return self.grow(past, objective, prior)

    def final(self, gs, m, target, train, objective):
        a = _reference(self, target, train, objective)
        c = self.predict(gs, m, target, train, objective)
        return (rankdata(a) + rankdata(c)) / (2 * self.n)

    def grow(self, past, objective, prior=None, log=None):
        """Générations : on part des 12 variables génériques et on ajoute, une par une, la famille
        qui améliore le plus le score interne (+ a priori des autres matières)."""
        prior = prior or {}
        bonus = lambda gs, m: LAMBDA * 0.05 * (sum(prior.get("groupes", {}).get(k, 0) for k in gs) / max(1, len(gs))
                                               + prior.get("modeles", {}).get(m, 0))
        chosen, hist = [], []
        best_m = max(MODEL_NAMES, key=lambda m: self.inner([], m, past, objective) + bonus([], m))
        best = self.inner(chosen, best_m, past, objective)
        hist.append({"generation": 0, "familles": [], "modele": best_m, "score_interne": round(best, 3)})
        while True:
            cand = []
            for k in [g for g in GROUPS if g not in chosen]:
                for m in MODEL_NAMES:
                    s = self.inner(chosen + [k], m, past, objective)
                    cand.append((s + bonus(chosen + [k], m), s, k, m))
            if not cand:
                break
            tot, s, k, m = max(cand)
            if tot <= best + bonus(chosen, best_m) + 1e-3:
                break
            chosen, best, best_m = chosen + [k], s, m
            hist.append({"generation": len(hist), "familles": list(chosen), "modele": m, "score_interne": round(s, 3)})
            if log:
                log(f"      + {k} ({m}) -> {s:.3f}")
        return chosen, best_m, hist


# ---------------------------------------------------------------------------- preuve
def honest(name, fc, prior, min_hist=3, log=print) -> dict:
    """Pour chaque année testée : variables et modèle choisis sur les années d'avant, puis vrai sujet."""
    S = Search(fc)
    tests = [y for y in fc.years if len([z for z in fc.years if z < y]) >= min_hist]
    out = {}
    for obj in ("prevision", "nouveaute"):
        rows = []
        for y in tests:
            past = [z for z in fc.years if z < y]
            gs, m, hist = S.choose(past, obj, prior.get(obj))
            r = S.score(S.final(gs, m, y, past, obj), y, past, obj)
            ref = S.score(_reference(S, y, past, obj), y, past, obj)
            if r is None:
                continue
            rows.append({"annee": y, "familles": gs, "modele": m, "couverture": round(r["couverture"], 3),
                         "auc": round(r["auc"], 3), "avant_couverture": round(ref["couverture"], 3),
                         "avant_auc": round(ref["auc"], 3), "generations": hist})
            log(f"  {name} {obj} {y} : {gs} {m} couverture {ref['couverture']:.3f} -> {r['couverture']:.3f}, AUC {ref['auc']:.3f} -> {r['auc']:.3f}")
        mean = lambda k: round(float(np.mean([r[k] for r in rows])), 3) if rows else None
        out[obj] = {"annees": rows, "couverture": mean("couverture"), "auc": mean("auc"),
                    "avant_couverture": mean("avant_couverture"), "avant_auc": mean("avant_auc")}
    return out


def _reference(S, y, past, obj):
    """Ancienne méthode, pour comparer : popularité pour la prévision ; logistique sur les 10
    variables sans historique pour la nouveauté."""
    fc = S.fc
    X = fc.rows(y, past)
    if obj == "prevision":
        return X[:, 10] + 0.01 * X[:, 11]
    Xtr, ytr = fc._train(past)
    return _lr().fit(Xtr[:, :10], ytr).predict_proba(X[:, :10])[:, 1]


def apply(fc, name=None, log=print) -> dict:
    """Prévision réelle de l'année suivante avec les variables et le modèle que le moteur choisit
    seul sur toutes ses années, aidé par la règle apprise sur les autres matières."""
    rule = json.loads(RULE.read_text(encoding="utf-8")) if RULE.exists() else {}
    S = Search(fc)
    nxt = fc.years[-1] + 1
    out = {}
    for obj in ("prevision", "nouveaute"):
        prior = rule.get(obj, {})
        if name and name in prior.get("appris_sur", []) and len(prior["appris_sur"]) > 1:
            prior = {}  # la règle contient déjà cette matière : on ne se donne pas son propre avis
        gs, m, hist = S.choose(fc.years, obj, prior)
        out[obj] = {"familles": gs, "modele": m, "generations": hist, "p": S.final(gs, m, nxt, fc.years, obj)}
        log(f"  auto-progression ({obj}) : {gs} / {m}")
    return out


def adopted(S, years, obj) -> tuple[list, str]:
    gs, m, _ = S.grow(years, obj)
    return gs, m


CACHE = ROOT / "data" / "cache"


def _fc(name):
    from ..prof.forecast import Forecast, reading
    t, _, it, lr = reading(name, log=lambda *a: None)
    return Forecast(t, it, lr)


def stage_own(name):
    """Ce que la matière retient seule, sur toutes ses années (sert d'a priori aux autres)."""
    S = Search(_fc(name))
    r = {obj: adopted(S, S.fc.years, obj) for obj in ("prevision", "nouveaute")}
    (CACHE / f"autoprog_own_{name}.json").write_text(json.dumps(r, ensure_ascii=False), encoding="utf-8")
    print(name, "retient seule :", r, flush=True)


def _prior(name, own):
    prior = {}
    for obj in ("prevision", "nouveaute"):
        others = [own[k][obj] for k in own if k != name]
        prior[obj] = {"groupes": {g: float(np.mean([g in o[0] for o in others])) for g in GROUPS} if others else {},
                      "modeles": {m: float(np.mean([m == o[1] for o in others])) for m in MODEL_NAMES} if others else {}}
    return prior


def _own(names):
    return {n: json.loads((CACHE / f"autoprog_own_{n}.json").read_text(encoding="utf-8")) for n in names}


def stage_honest(name, names):
    r = honest(name, _fc(name), _prior(name, _own(names)))
    (CACHE / f"autoprog_honest_{name}.json").write_text(json.dumps(r, ensure_ascii=False, default=float), encoding="utf-8")


def combine(names):
    own = _own(names)
    rep = {"retenu_seul": {n: {o: {"familles": v[0], "modele": v[1]} for o, v in d.items()} for n, d in own.items()},
           "preuve": {n: json.loads((CACHE / f"autoprog_honest_{n}.json").read_text(encoding="utf-8")) for n in names}}
    rule = {}
    for obj in ("prevision", "nouveaute"):
        rule[obj] = {"groupes": {g: round(float(np.mean([g in own[k][obj][0] for k in own])), 3) for g in GROUPS},
                     "modeles": {m: round(float(np.mean([m == own[k][obj][1] for k in own])), 3) for m in MODEL_NAMES},
                     "appris_sur": list(own)}
    RULE.write_text(json.dumps(rule, ensure_ascii=False, indent=1), encoding="utf-8")
    rep["regle"] = rule
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    for n, r in rep["preuve"].items():
        print(n, {o: {k: v for k, v in x.items() if k != "annees"} for o, x in r.items()})


def main(argv):
    """autoprog [own|honest] NOM... ; sans étape : tout, matière par matière, puis bilan."""
    warnings.filterwarnings("ignore")
    if argv and argv[0] in ("own", "honest", "combine"):
        st, names = argv[0], argv[1:] or ["droit", "nsi", "eco"]
        if st == "own":
            for n in names:
                stage_own(n)
        elif st == "honest":
            stage_honest(names[0], names[1:] or ["droit", "nsi", "eco"])
        else:
            combine(names)
        return
    names = argv or ["droit", "nsi", "eco"]
    for n in names:
        stage_own(n)
    for n in names:
        stage_honest(n, names)
    combine(names)


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main(sys.argv[1:])


# ===== examgen/meta/controle.py =====
"""Le correcteur se critique : ses seuils sont calibrés sur le vrai professeur.

Le contrôle des exercices générés (prof/check.py) refuse un énoncé ou une situation trop proche
d'un ancien sujet. Mais à partir de quand est-ce « trop proche » ? Plutôt que de le décider à la
main, on regarde ce que fait le professeur lui-même : chaque année, ses nouvelles questions
ressemblent plus ou moins aux anciennes. Un bon contrôle doit laisser passer presque toutes ses
vraies questions (sinon il exige d'un exercice généré plus que le professeur ne fait) et pas
davantage (sinon il laisse passer des copies).

Pour chaque matière et chaque année (avec au moins 3 années avant), les vraies questions de l'année
sont passées au contrôle face aux années précédentes seulement (vocabulaire appris sur elles). Deux façons de
fixer le seuil, apprises sur les AUTRES matières puis mesurées sur la matière exclue :
  commun  le plus strict qui laisse passer au moins 90 % des vraies questions ;
  propre  un quantile de ce que CE professeur s'est permis les années d'avant (le quantile est
          appris sur les autres matières) : strict là où il ne se répète jamais, souple là où il
          reprend toujours la même mise en situation.
Est adoptée la plus stricte de celles qui laissent passer ≥ 90 % des vraies questions sans faire
échouer aucune matière (sinon le seuil d'origine reste).

    python -m examgen.meta.controle droit nsi eco ...
"""
from __future__ import annotations

import json
import sys

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from . import autoprog as AP
from ..prof.check import _mask, Checker

OUT = AP.ROOT / "output" / "meta" / "controle.json"
GRID = np.round(np.arange(0.50, 0.991, 0.01), 2)
CIBLE = 0.90
ACTUEL = 0.85  # seuil écrit à la main jusqu'ici (énoncé et situation)


def _vec(t, docs):
    c = t.cfg
    kw = dict(analyzer="char_wb", ngram_range=(3, 5)) if c["analyzer"] == "char_wb" else dict(ngram_range=tuple(c["ngram"]))
    return TfidfVectorizer(sublinear_tf=True, strip_accents="unicode", min_df=2, max_df=0.5, **kw).fit(list(t.pass_text) + docs)


def measures(name, min_hist=3):
    return measures_teacher(joblib.load(AP.ROOT / "data" / "cache" / f"lecture_{name}.joblib")[0], min_hist)


def measures_teacher(t, min_hist=3):
    """Pour chaque vraie question d'une année testée : proximité max aux anciens énoncés (masqués),
    excuse « formule rituelle », proximité max de sa situation aux anciennes situations."""
    qs = [q for q in t.qs if q.year]
    years = sorted({q.year for q in qs})
    out = []
    for y in years:
        past = [q for q in qs if q.year < y]
        if len({q.year for q in past}) < min_hist:
            continue
        new = [q for q in qs if q.year == y]
        V = _vec(t, [q.stem + " " + q.situation[:1500] for q in past])
        Pm = V.transform([_mask(q.stem) for q in past])
        exams = np.array([q.exam for q in past])
        need = max(3, int(0.1 * len(set(exams))))
        by = {}
        for q in past:
            for g in Checker._head(q.stem):
                by.setdefault(g, set()).add(q.exam)
        heads = {g for g, e in by.items() if len(e) >= need}
        PP = (Pm @ Pm.T).toarray()
        ritual = np.array([len(set(exams[PP[i] > 0.7])) >= need or bool(Checker._head(past[i].stem) & heads)
                           for i in range(len(past))])
        sits = {}
        for q in past:
            if len(q.situation or "") > 80:
                sits.setdefault((q.exam, q.part), _mask(q.situation))
        Ps = V.transform(list(sits.values())) if sits else None
        seen_sit = set()
        for q in new:
            s = (V.transform([_mask(q.stem)]) @ Pm.T).toarray().ravel()
            j = int(s.argmax())
            row = {"annee": y, "enonce": float(s[j]), "rituel": bool(ritual[j] or (Checker._head(q.stem) & heads))}
            key = (q.exam, q.part)
            if Ps is not None and len(q.situation or "") > 80 and key not in seen_sit:
                seen_sit.add(key)  # une situation par partie
                row["situation"] = float((V.transform([_mask(q.situation)]) @ Ps.T).max())
            out.append(row)
    return out


QS = (0.8, 0.9, 0.95, 0.98, 1.0)


def _vals(rows, what):
    return [r[what] for r in rows if what in r and not (what == "enonce" and r["rituel"])]


def own_tau(rows, y, what, q, fallback):
    """Seuil propre à la matière : quantile q des proximités de ses vraies questions des années
    testées avant y (ce que ce professeur s'autorise d'habitude) ; à défaut, le seuil commun."""
    h = _vals([r for r in rows if r["annee"] < y], what)
    return float(np.quantile(h, q)) if len(h) >= 5 else fallback


def passes(rows, what, tau=None, q=None, fallback=0.85):
    v = []
    for r in rows:
        if what not in r:
            continue
        t = tau if q is None else own_tau(rows, r["annee"], what, q, fallback)
        v.append(r[what] < t or (what == "enonce" and r["rituel"]))
    return float(np.mean(v)) if v else None


def mean_tau(rows, what, q, fallback):
    t = [own_tau(rows, r["annee"], what, q, fallback) for r in rows if what in r]
    return float(np.mean(t)) if t else None


def learn(M, what):
    """Seuil commun : le plus strict qui laisse passer ≥ 90 % des vraies questions (moyenne par
    matière). Seuil propre : le plus petit quantile qui fait de même."""
    tau = float(GRID[-1])
    for x in GRID:
        r = [v for v in (passes(M[n], what, x) for n in M) if v is not None]
        if r and np.mean(r) >= CIBLE:
            tau = float(x)
            break
    q = QS[-1]
    for x in QS:
        r = [v for v in (passes(M[n], what, q=x, fallback=tau) for n in M) if v is not None]
        if r and np.mean(r) >= CIBLE:
            q = x
            break
    return tau, q


def main(names):
    M = {n: measures(n) for n in names}
    rep = {"principe": __doc__.split("\n\n")[0], "cible": CIBLE, "matieres": {}, "synthese": {}, "seuils": {}}
    for what in ("enonce", "situation"):
        held = {}
        for n in names:
            tau, q = learn({m: M[m] for m in names if m != n}, what)
            held[n] = {"commun": {"seuil": tau, "passe": passes(M[n], what, tau)},
                       "propre": {"quantile": q, "seuil_moyen": mean_tau(M[n], what, q, tau),
                                  "passe": passes(M[n], what, q=q, fallback=tau)},
                       "actuel": {"seuil": ACTUEL, "passe": passes(M[n], what, ACTUEL)}}
        ok = [h for h in held.values() if h["actuel"]["passe"] is not None]
        S = {}
        for m in ("actuel", "commun", "propre"):
            v = [h[m]["passe"] for h in ok]
            t = [h[m].get("seuil", h[m].get("seuil_moyen")) for h in ok]
            S[m] = {"vraies_questions_acceptees": round(float(np.mean(v)), 3), "pire_matiere": round(float(min(v)), 3),
                    "matieres_sous_80": int(sum(x < 0.8 for x in v)), "seuil_moyen": round(float(np.mean(t)), 3)}
        # adoption : la méthode la plus stricte (seuil moyen le plus bas) parmi celles qui, matière
        # exclue, laissent passer ≥ 90 % des vraies questions sans faire échouer de matière
        good = [m for m in S if S[m]["vraies_questions_acceptees"] >= CIBLE - 0.01 and S[m]["matieres_sous_80"] == 0]
        win = min(good, key=lambda m: S[m]["seuil_moyen"]) if good else "actuel"
        tau, q = learn(M, what)
        rep["synthese"][what] = {**S, "adoptee": win, "matieres": len(ok)}
        rep["seuils"][what] = {"methode": win, "commun": tau if win != "actuel" else ACTUEL, "quantile": q if win == "propre" else None}
        for n in names:
            rep["matieres"].setdefault(n, {})[what] = held[n]
    rep["questions_reelles_testees"] = {n: len(M[n]) for n in names}
    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print(json.dumps({k: rep[k] for k in ("synthese", "seuils")}, ensure_ascii=False, indent=1))


def seuils(t=None) -> dict:
    """Seuils pour prof/check.py : appris (commun, ou propre à la matière d'après ses propres années)
    ; seuil d'origine s'ils n'ont pas encore été appris."""
    try:
        S = json.loads(OUT.read_text(encoding="utf-8"))["seuils"]
    except (OSError, KeyError, ValueError):
        return {"enonce": ACTUEL, "situation": ACTUEL}
    out = {w: S[w]["commun"] for w in S}
    if t is not None and any(S[w]["methode"] == "propre" for w in S):
        rows = measures_teacher(t)
        nxt = max([r["annee"] for r in rows], default=0) + 1
        for w in S:
            if S[w]["methode"] == "propre":
                out[w] = own_tau(rows, nxt, w, S[w]["quantile"], S[w]["commun"])
    return out


if __name__ == "__main__":
    main(sys.argv[1:])


# ===== examgen/meta/critique.py =====
"""Autocritique méta-apprise : le moteur examine ses propres ratés et cherche seul quoi changer.

Rien n'est écrit pour une matière. Le point de départ est la stratégie actuelle (règle apprise sur
plusieurs matières). Puis, à chaque tour :

1. Autocritique. Sur les matières d'entraînement, le moteur relève les questions tombées qu'il
   n'avait pas retenues et cherche ce qui les aurait attrapées :
   - « rattrapage » : la part de ces ratés que chaque autre réglage (famille de variables × modèle)
     plaçait dans sa propre sélection ;
   - « chapitres oubliés » : les ratés sont-ils surreprésentés dans les chapitres où il n'a rien
     retenu ? Si oui, sa sélection est trop concentrée ; si non et qu'il diversifie déjà, trop dispersée.
2. Remèdes. De ce diagnostic seulement naissent des propositions : mêler un peu (ou beaucoup) d'un
   réglage qui rattrape ; diversifier davantage ou moins les chapitres retenus.
3. Preuve. Une proposition n'est gardée que si elle améliore le critère prudent appris (moyenne et
   bas de la distribution des gains par domaine). Sinon le moteur s'arrête : il ne change pas pour
   changer.

Toute la recherche est refaite sans la matière testée (validation « matière exclue »), puis la
stratégie trouvée est appliquée à elle. Elle n'est adoptée en production que si elle bat la
stratégie actuelle selon ce même critère.

Auto-jugement appris : au lieu d'une marge fixe, un méta-modèle prédit, à partir des traits du
domaine et de ce que donne le rejeu sur les années passées, la couverture attendue et l'erreur
probable ; la largeur de la fourchette est calibrée pour contenir le vrai résultat 85 % du temps
(calibration elle aussi faite sans la matière testée).

    python -m examgen.meta.critique droit nsi eco ...
"""
from __future__ import annotations

import json
import sys
import warnings

import joblib
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor

from . import transfer as TR
from ..fast import auc, pmap

OUT = TR.AP.ROOT / "output" / "meta" / "critique.json"
JUGE = TR.AP.ROOT / "output" / "meta" / "critique_juge.joblib"
BASE = TR.BASE
IX = {(tuple(gs), m): j for j, (gs, m) in enumerate(BASE)}
WEIGHTS = (0.25, 0.5, 1.0)  # part du réglage ajouté, relative au mélange courant
LAMBDAS = (0.0, 0.1, 0.25, 0.5, 1.0)  # diversification des chapitres (0 = aucune)
N_PROP = 6  # réglages « rattrapeurs » essayés à chaque tour
EPS = 0.002  # gain minimal pour accepter un changement
STEPS = 6
CIBLE = 0.85  # part des fourchettes qui doivent contenir le vrai résultat


# ---------------------------------------------------------------------------- données
def load(names):
    out = []
    for n in names:
        T = json.loads((TR.CACHE / f"transfer_tasks_{n}.json").read_text(encoding="utf-8"))
        E = joblib.load(TR.CACHE / f"critique_preds_{n}.joblib")
        for t, e in zip(T, E):
            t["matiere"], t["sec"], t["ev"] = n, np.unique(e["sec"], return_inverse=True)[1], e["ev"]
            out.append(t)
    return out


def weights_of(c):
    """Un candidat de transfer.py écrit comme mélange de rangs des réglages de base."""
    gs, m, mix = c
    w = np.zeros(len(BASE))
    if m == "melange":
        w[IX[(tuple(gs), "logistique")]] += 0.5
        w[IX[(tuple(gs), "arbres")]] += 0.5
    else:
        w[IX[(tuple(gs), m)] if m != "ancienne" else 0] += 1.0
    if mix:
        w = 0.5 * w / w.sum()
        w[0] += 0.5
    return w / w.sum()


# ---------------------------------------------------------------------------- noter
def _diversify(p, sec, lam):
    """Rabote le score des passages d'un chapitre déjà bien servi : p / (1 + k)^λ, k = nombre de
    passages du même chapitre mieux classés."""
    if lam == 0:
        return p
    o = np.argsort(-p, kind="stable")
    s = sec[o]
    g = np.argsort(s, kind="stable")
    first = np.r_[0, np.flatnonzero(np.diff(s[g])) + 1]
    k = np.empty(len(p))
    k[g] = np.arange(len(p)) - np.repeat(first, np.diff(np.r_[first, len(p)]))
    out = np.empty(len(p))
    out[o] = p[o] / (1.0 + k) ** lam
    return out


def judge(p, e, sec, obj, lam=0.0):
    """Même notation que transfer.Domain.score ; renvoie aussi ce qu'il faut pour l'autocritique."""
    y, q, seen = e["y"], e["q"], e["seen"]
    pool = ~seen if obj == "nouveaute" else np.ones(len(p), bool)
    qq = q[pool[q]]
    if not len(qq) or len(set(y[pool])) < 2 or (obj == "nouveaute" and pool.sum() < 10):
        return None
    ix = np.flatnonzero(pool)
    pp = _diversify(p[ix], sec[ix], lam)
    k = max(1, int((TR.TOP if obj == "prevision" else 0.25) * len(ix)))
    sel = np.zeros(len(p), bool)
    sel[ix[np.argsort(-pp, kind="stable")[:k]]] = True
    cov = float(sel[qq].mean())
    a = auc(y[ix], pp)
    return {"couverture": cov, "auc": a, "score": cov + 0.1 * a, "sel": sel, "rates": qq[~sel[qq]], "pool": pool, "k": k}


def blend(w, P):
    return w @ P


class Bench:
    """Tâches d'un objectif, prêtes à noter vite n'importe quelle stratégie (w, λ)."""

    def __init__(self, tasks, obj):
        self.T = [t for t in tasks if t["objectif"] == obj and judge(t["ev"][0]["P"][0], t["ev"][0], t["sec"], obj)]
        self.obj = obj
        doms = sorted({(t["matiere"], t["domaine"] == "complet") for t in self.T})
        self.d = np.array([doms.index((t["matiere"], t["domaine"] == "complet")) for t in self.T])
        self.nd = len(doms)
        self.ref = np.array([judge(t["ev"][0]["P"][0], t["ev"][0], t["sec"], obj)["score"] for t in self.T])

    def run(self, st, i):
        t = self.T[i]
        return judge(blend(st[0], t["ev"][0]["P"]), t["ev"][0], t["sec"], self.obj, st[1])

    def gains(self, st):
        return np.array([self.run(st, i)["score"] for i in range(len(self.T))]) - self.ref

    def dom_mean(self, v):
        return np.array([v[self.d == k].mean() for k in range(self.nd)])

    def value(self, st, agg):
        return float(TR.AGGS[agg](self.dom_mean(self.gains(st))))


# ---------------------------------------------------------------------------- autocritique
def critique(B, st):
    """Ce que le moteur se reproche, mesuré sur ses ratés."""
    resc, over = np.zeros((len(B.T), len(BASE))), np.zeros(len(B.T))
    for i, t in enumerate(B.T):
        r = B.run(st, i)
        miss = r["rates"]
        if not len(miss):
            continue
        e = t["ev"][0]
        ix = np.flatnonzero(r["pool"])
        for j in range(len(BASE)):  # le réglage j aurait-il retenu ces ratés ?
            sj = np.zeros(len(r["pool"]), bool)
            sj[ix[np.argsort(-e["P"][j][ix], kind="stable")[:r["k"]]]] = True
            resc[i, j] = sj[miss].mean()
        sec = t["sec"]
        empty = ~np.isin(sec, np.unique(sec[r["sel"]]))  # chapitres où rien n'est retenu
        rest = r["pool"] & ~r["sel"]
        over[i] = empty[miss].mean() / max(1e-9, empty[rest].mean()) if empty[rest].any() else 1.0
    return {"_resc": np.array([B.dom_mean(resc[:, j]).mean() for j in range(len(BASE))]),
            "chapitres_oublies": float(B.dom_mean(over).mean())}


def proposals(st, diag):
    w, lam = st
    out = []
    for j in np.argsort(-diag["_resc"])[:N_PROP]:
        for a in WEIGHTS:
            nw = w + a * np.eye(len(BASE))[j]
            out.append(((nw / nw.sum(), lam), f"mêler {name(j)} (part {a:g})"))
    li = LAMBDAS.index(lam)
    if diag["chapitres_oublies"] > 1 and li + 1 < len(LAMBDAS):
        out.append(((w, LAMBDAS[li + 1]), f"diversifier les chapitres (λ={LAMBDAS[li + 1]})"))
    if diag["chapitres_oublies"] < 1 and li > 0:
        out.append(((w, LAMBDAS[li - 1]), f"moins diversifier (λ={LAMBDAS[li - 1]})"))
    return out


def name(j):
    gs, m = BASE[j]
    return "ancienne méthode" if m == "ancienne" else f"{'+'.join(gs) or 'base'}/{m}"


def describe(st):
    w, lam = st
    return {"melange": {name(j): round(float(w[j]), 3) for j in np.flatnonzero(w > 1e-9)}, "diversification": lam}


def search(tasks, obj, agg, start, log=None):
    B = Bench(tasks, obj)
    st = (weights_of(start), 0.0)
    cur = B.value(st, agg)
    journal = [{"etat": describe(st), "valeur": round(cur, 4)}]
    for _ in range(STEPS):
        diag = critique(B, st)
        props = proposals(st, diag)
        vals = [B.value(s, agg) for s, _ in props]
        b = int(np.argmax(vals))
        entry = {"chapitres_oublies": round(diag["chapitres_oublies"], 3),
                 "rattrapeurs": [[name(j), round(float(diag["_resc"][j]), 3)] for j in np.argsort(-diag["_resc"])[:3]],
                 "meilleure_proposition": props[b][1], "valeur_proposee": round(vals[b], 4)}
        if vals[b] - cur <= EPS:
            entry["decision"] = "refusée : pas de gain prouvé, arrêt"
            journal.append(entry)
            break
        st, cur = props[b][0], vals[b]
        entry["decision"] = "acceptée"
        journal.append(entry)
        if log:
            log(f"  {obj} : {props[b][1]} -> {cur:.4f}")
    return st, journal


# ---------------------------------------------------------------------------- auto-jugement appris
def replay_scores(t, st, obj):
    out = []
    for e in t["ev"][1:]:
        r = judge(blend(st[0], e["P"]), e, t["sec"], obj, st[1])
        if r:
            out.append(r["score"])
    return out


def jfeat(traits, ins, obj):
    ins = np.asarray(ins) if len(ins) else np.zeros(1)
    return list(traits.values()) + [float(obj == "prevision"), ins.mean(), ins.min(), ins.max(), ins.std(), len(ins)]


def _et(leaf=15):
    return ExtraTreesRegressor(n_estimators=150, min_samples_leaf=leaf, max_features=0.6, random_state=0, n_jobs=-1)


def fit_interval(X, y):
    """Centre et erreur typique appris ; le facteur k est calibré à part."""
    m = _et().fit(X, y)
    # erreur typique apprise sur des résidus hors échantillon (sinon trop optimiste)
    res = np.zeros(len(y))
    for f in range(5):
        tr = np.arange(len(y)) % 5 != f
        res[~tr] = np.abs(y[~tr] - _et().fit(X[tr], y[tr]).predict(X[~tr]))
    s = _et(25).fit(X, res)
    return {"centre": m, "erreur": s}


def interval(J, X, k):
    c, s = J["centre"].predict(X), np.maximum(J["erreur"].predict(X), 0.01)
    return np.clip(c - k * s, 0, 1), np.clip(c + k * s, 0, 1)


# ---------------------------------------------------------------------------- validation
_CTX = {}


def _fold(n):
    tasks, every_obj = _CTX["tasks"], _CTX["objs"]
    tr = [t for t in tasks if t["matiere"] != n]
    res = {}
    for obj in every_obj:
        agg = TR.choose_agg(tr, obj)
        cur = TR.select_rule(tr, obj)
        st, jr = search(tr, obj, agg, cur)
        te = Bench([t for t in tasks if t["matiere"] == n], obj)
        full = np.array([t["domaine"] == "complet" for t in te.T])
        R = {m: [te.run(s, i) for i in range(len(te.T))] for m, s in
             (("ancienne", (weights_of([[], "ancienne", False]), 0.0)), ("regle", (weights_of(cur), 0.0)), ("critique", st))}
        f = lambda v: round(float(np.mean(v)), 4) if len(v) else None
        res[obj] = {m: {"couverture": f([r["couverture"] for r, k in zip(R[m], full) if k]),
                        "auc": f([r["auc"] for r, k in zip(R[m], full) if k]),
                        "gain": f([r["score"] - a["score"] for r, a, k in zip(R[m], R["ancienne"], full) if k]),
                        "pseudo_gain": f([r["score"] - a["score"] for r, a, k in zip(R[m], R["ancienne"], full) if not k])}
                    for m in R}
        res[obj]["strategie_trouvee"] = describe(st)
        res[obj]["prudence"] = agg
        res[obj]["tours_acceptes"] = sum(e.get("decision") == "acceptée" for e in jr)
        # pour l'auto-jugement : choix fait à l'aveugle, ce que dit le rejeu, résultat réel
        res[obj]["_aveugle"] = [(t["traits"], replay_scores(t, st, obj), r["couverture"])
                                for t, r in zip(te.T, R["critique"])]
        print(n, obj, {m: (res[obj][m]["couverture"], res[obj][m]["gain"]) for m in R}, describe(st), flush=True)
    return n, res


def main(names):
    warnings.filterwarnings("ignore")
    tasks = load(names)
    _CTX.update(tasks=tasks, objs=TR.OBJ)
    folds = dict(pmap(_fold, names))
    rep = {"principe": __doc__.split("\n\n")[0] + " " + __doc__.split("\n\n")[1].split("\n")[0],
           "appris_sur": names, "matieres": {}, "synthese": {}, "adoptee": {}, "journal": {}}
    blind = {}
    for n in names:
        rep["matieres"][n] = {o: {k: v for k, v in folds[n][o].items() if k != "_aveugle"} for o in TR.OBJ}
        for o in TR.OBJ:
            blind.setdefault(o, []).extend([(n, *x) for x in folds[n][o]["_aveugle"]])
    for obj in TR.OBJ:
        agg = TR.choose_agg(tasks, obj)
        S = {}
        for m in ("ancienne", "regle", "critique"):
            g = np.array([rep["matieres"][n][obj][m]["gain"] for n in names])
            S[m] = {"gain_moyen": round(float(g.mean()), 4), "pire_matiere": round(float(g.min()), 4),
                    "matieres_gagnees": int((g > 0.005).sum()), "matieres_perdues": int((g < -0.005).sum()),
                    "couverture_moyenne": round(float(np.mean([rep["matieres"][n][obj][m]["couverture"] for n in names])), 3),
                    "auc_moyenne": round(float(np.mean([rep["matieres"][n][obj][m]["auc"] for n in names])), 3),
                    "critere": round(float(TR.AGGS[agg](g)), 4)}
        rep["synthese"][obj] = S
        st, jr = search(tasks, obj, agg, TR.select_rule(tasks, obj), log=print)
        rep["journal"][obj] = jr
        win = "critique" if S["critique"]["critere"] > S["regle"]["critere"] + 1e-4 else "regle"
        rep["adoptee"][obj] = {"strategie": win, "prudence": agg,
                               **(describe(st) if win == "critique" else {"regle": TR.select_rule(tasks, obj)}),
                               "poids": st[0].round(6).tolist() if win == "critique" else None}
    # ---- auto-jugement : fourchette apprise vs fourchette à marge fixe, toutes deux matière exclue
    aj, X, Y, G = {}, [], [], []
    for obj in TR.OBJ:
        for n, tr_, ins, cov in blind[obj]:
            X.append(jfeat(tr_, ins, obj))
            Y.append(cov)
            G.append(n)
    X, Y, G = np.array(X), np.array(Y), np.array(G)
    lo_l, hi_l, lo_f, hi_f = (np.zeros(len(Y)) for _ in range(4))
    for n in names:
        tr, te = G != n, G == n
        J = fit_interval(X[tr], Y[tr])
        k = calib_k_oof(X[tr], Y[tr], G[tr])  # calibré sans la matière testée
        lo_l[te], hi_l[te] = interval(J, X[te], k)
        # marge fixe calibrée de la même façon (sans la matière)
        im, imn = X[:, -5], X[:, -4]
        for mg in np.arange(0, 0.61, 0.025):
            lo, hi = np.maximum(0, imn - mg), np.minimum(1, 2 * im - imn + mg)
            if np.mean(((lo <= Y) & (Y <= hi))[tr]) >= CIBLE:
                break
        lo_f[te], hi_f[te] = lo[te], hi[te]
    for m, lo, hi in (("marge_fixe", lo_f, hi_f), ("appris", lo_l, hi_l)):
        aj[m] = {"fourchette_juste": round(float(np.mean((lo <= Y) & (Y <= hi))), 3),
                 "largeur_moyenne": round(float(np.mean(hi - lo)), 3), "taches": int(len(Y))}
    J = fit_interval(X, Y)
    k = calib_k_oof(X, Y, G)
    aj["k"] = round(k, 3)
    joblib.dump({"juge": J, "k": k}, JUGE, compress=3)
    ok = aj["appris"]["fourchette_juste"] >= CIBLE - 0.02 and aj["appris"]["largeur_moyenne"] < aj["marge_fixe"]["largeur_moyenne"]
    aj["adopte"] = "appris" if ok else "marge_fixe"
    rep["auto_jugement"] = aj
    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print(json.dumps({"synthese": rep["synthese"], "adoptee": {o: {k: v for k, v in a.items() if k != "poids"}
                                                               for o, a in rep["adoptee"].items()},
                      "auto_jugement": aj}, ensure_ascii=False, indent=1))


def calib_k_oof(X, Y, G, groups=5):
    """k : calibré sur des prédictions hors matière (matières réparties en quelques paquets,
    chaque paquet prédit par un juge appris sans lui)."""
    subs = sorted(set(G))
    if len(subs) < 2:
        return 2.0
    pk = {n: i % groups for i, n in enumerate(subs)}
    g = np.array([pk[n] for n in G])
    C, S = np.zeros(len(Y)), np.zeros(len(Y))
    for f in range(min(groups, len(subs))):
        J = fit_interval(X[g != f], Y[g != f])
        C[g == f] = J["centre"].predict(X[g == f])
        S[g == f] = np.maximum(J["erreur"].predict(X[g == f]), 0.01)
    for k in np.arange(0.25, 6.01, 0.05):
        if np.mean(np.abs(Y - C) <= k * S) >= CIBLE:
            return float(k)
    return 6.0


if __name__ == "__main__":
    main(sys.argv[1:])


# ===== examgen/meta/deep.py =====
"""Variables d'intention à grande échelle : « qu'est-ce qui fait qu'un passage du cours tombe ? »

  1. expansion combinatoire : les 12 variables de base d'un passage (place, longueur, centralité,
     insistance, historique...) sont déclinées en vues invariantes d'échelle (z-score et rang dans
     l'année, haut du classement, carré) puis croisées deux à deux (produits, écarts, maximum).
     Plusieurs centaines de variables, aucune écrite à la main pour une matière ;
  2. sélection par stabilité : un modèle parcimonieux (L1) est réappris sur 40 sous-échantillons ;
     on ne garde que les variables choisies dans au moins 60 % des cas (le bruit, lui, change) ;
  3. preuves : année exclue dans la matière, et transfert à froid (appris sur une matière,
     appliqué tel quel à l'autre), comparés aux 12 variables de base et à la simple popularité.
"""
from __future__ import annotations

import itertools

import numpy as np
from scipy.stats import rankdata
from sklearn.linear_model import LogisticRegression
from ..fast import auc as roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

SHORT = {"rang_du_passage_dans_la_section": "rang", "longueur_du_passage": "longueur", "centralite_du_passage": "centralite",
         "redondance_du_passage": "redondance", "insistance_typographique": "insistance", "passage_avec_reference": "reference",
         "densite_symboles_du_passage": "symboles", "place_de_la_section_dans_le_cours": "place_section",
         "taille_de_la_section": "taille_section", "centralite_de_la_section": "centralite_section",
         "frequence_passee_du_passage": "deja_tombe", "frequence_passee_de_la_section": "section_deja_tombee"}


def expand(X: np.ndarray, g: np.ndarray, names: list[str]) -> tuple[np.ndarray, list[str]]:
    """Vues calculées dans chaque année (groupe) : invariantes à l'échelle propre à une matière."""
    nm = [SHORT.get(n, n) for n in names]
    Z = np.zeros_like(X, float)
    R = np.zeros_like(X, float)
    for y in np.unique(g):
        m = g == y
        Z[m] = (X[m] - X[m].mean(0)) / (X[m].std(0) + 1e-9)
        R[m] = np.column_stack([(rankdata(X[m, j]) - 1) / max(m.sum() - 1, 1) for j in range(X.shape[1])])
    cols, out = [], []
    for j, n in enumerate(nm):
        cols += [Z[:, j], R[:, j], (R[:, j] > 0.9).astype(float), Z[:, j] ** 2]
        out += [f"{n}", f"rang({n})", f"haut({n})", f"extreme({n})"]
    for i, j in itertools.combinations(range(len(nm)), 2):
        a, b = nm[i], nm[j]
        cols += [Z[:, i] * Z[:, j], R[:, i] * R[:, j], np.abs(R[:, i] - R[:, j]), np.maximum(R[:, i], R[:, j])]
        out += [f"{a}×{b}", f"rang({a})×rang({b})", f"ecart({a},{b})", f"max({a},{b})"]
    return np.column_stack(cols), out


def _lr(C=0.3):
    return make_pipeline(StandardScaler(), LogisticRegression(C=C, max_iter=3000, class_weight="balanced"))


def stability(X, y, n: int = 40, frac: float = 0.5, C: float = 0.02, thr: float = 0.6, seed: int = 0):
    rng = np.random.default_rng(seed)
    cnt = np.zeros(X.shape[1])
    Xs = StandardScaler().fit_transform(X)
    for _ in range(n):
        idx = rng.choice(len(y), int(frac * len(y)), replace=False)
        m = LogisticRegression(penalty="l1", C=C, solver="liblinear", class_weight="balanced").fit(Xs[idx], y[idx])
        cnt += m.coef_[0] != 0
    f = cnt / n
    return np.where(f >= thr)[0], f


def _auc_by_group(m, X, y, g):
    s = [roc_auc_score(y[g == k], m.predict_proba(X[g == k])[:, 1]) for k in np.unique(g) if len(set(y[g == k])) > 1]
    return float(np.mean(s))


def year_out(X, y, g, select: bool):
    """Année exclue ; la sélection par stabilité est refaite sans l'année testée."""
    sc = []
    for k in np.unique(g):
        tr, te = g != k, g == k
        if len(set(y[te])) < 2:
            continue
        cols = stability(X[tr], y[tr])[0] if select else np.arange(X.shape[1])
        if len(cols) == 0:
            cols = np.arange(X.shape[1])
        m = _lr().fit(X[tr][:, cols], y[tr])
        sc.append(roc_auc_score(y[te], m.predict_proba(X[te][:, cols])[:, 1]))
    return round(float(np.mean(sc)), 3)


def study(data: dict) -> dict:
    """data : matière -> (X_base, y, groupes, noms). Rapport par matière + transfert à froid."""
    E = {n: expand(X, g, nm) for n, (X, y, g, nm) in data.items()}
    rep = {"variables_generees": len(next(iter(E.values()))[1]), "par_matiere": {}, "transfert_a_froid": {}}
    stable = {}
    for n, (X, y, g, nm) in data.items():
        XE, en = E[n]
        cols, f = stability(XE, y)
        stable[n] = (cols, f)
        m = _lr().fit(XE[:, cols], y)
        coef = m[-1].coef_[0]
        rep["par_matiere"][n] = {
            "auc_annee_exclue_popularite": round(float(np.mean([roc_auc_score(y[g == k], X[g == k, -2]) for k in np.unique(g)
                                                                  if len(set(y[g == k])) > 1])), 3),
            "auc_annee_exclue_12_variables": year_out(X, y, g, select=False),
            "auc_annee_exclue_variables_stables": year_out(XE, y, g, select=True),
            "variables_stables": len(cols),
            "variables_par_matiere_rejetees": int(XE.shape[1] - len(cols)),
            "regles": [{"variable": en[c], "frequence": round(float(f[c]), 2), "sens": "+" if w > 0 else "-"}
                       for c, w in sorted(zip(cols, coef), key=lambda r: -abs(r[1]))][:12]}
    names = list(data)
    for a, b in itertools.permutations(names, 2):
        XA, yA, gA = E[a][0], data[a][1], data[a][2]
        XB, yB, gB = E[b][0], data[b][1], data[b][2]
        ca = stable[a][0]
        Zb = np.zeros_like(data[b][0], float)  # 12 variables : mises à l'échelle par année aussi, pour être juste
        Za = np.zeros_like(data[a][0], float)
        for Zx, (Xx, gx) in ((Za, (data[a][0], gA)), (Zb, (data[b][0], gB))):
            for k in np.unique(gx):
                mm = gx == k
                Zx[mm] = (Xx[mm] - Xx[mm].mean(0)) / (Xx[mm].std(0) + 1e-9)
        base = _lr().fit(Za, yA)
        deep = _lr().fit(XA[:, ca], yA)
        both = sorted(set(stable[a][0]) & set(stable[b][0]))
        rep["transfert_a_froid"][f"{a}->{b}"] = {
            "auc_12_variables": round(_auc_by_group(base, Zb, yB, gB), 3),
            "auc_variables_stables": round(_auc_by_group(deep, XB[:, ca], yB, gB), 3),
            "auc_appris_dans_la_matiere": rep["par_matiere"][b]["auc_annee_exclue_variables_stables"]}
    for n, r in rep["par_matiere"].items():  # choix fait par la matière elle-même, sur ses années passées
        r["modele_retenu"] = "variables stables" if r["auc_annee_exclue_variables_stables"] > r["auc_annee_exclue_12_variables"] else "12 variables"
        r["auc_modele_retenu"] = max(r["auc_annee_exclue_variables_stables"], r["auc_annee_exclue_12_variables"])
    common = sorted(set(stable[names[0]][0]).intersection(*[set(stable[n][0]) for n in names[1:]])) if len(names) > 1 else []
    en = next(iter(E.values()))[1]
    rep["regles_universelles"] = [en[c] for c in common]
    return rep


# ===== examgen/meta/domain.py =====
"""Chargement d'un domaine (sujets + cours) pour le méta-apprentissage.

Le moteur ne reçoit que les sujets et le cours. Une vérité terrain sert uniquement à JUGER le
méta-apprentissage, jamais au moteur lui-même :
  - droit : « références au programme » des corrigés officiels ;
  - NSI   : phrase de thème des exercices officiels (« Cet exercice porte sur… »).
"""
from __future__ import annotations

import re
from pathlib import Path

import joblib

from ..prof import docs as D
from ..prof.profile import Teacher

ROOT = Path(__file__).resolve().parents[2]
DOMAINS = {
    "droit": ("data/sources/droit_stmg", "data/droit/cours"),
    "nsi": ("data/sources/sujetdebac", "data/nsi/cours"),
}
# registre extensible : toute matière ajoutée par « python -m examgen.prof tout » (sujets + cours)
REGISTRY = ROOT / "data" / "domaines.json"


def _registry() -> dict:
    import json
    try:
        return {k: tuple(v) for k, v in json.loads(REGISTRY.read_text(encoding="utf-8")).items()}
    except (OSError, ValueError):
        return {}


DOMAINS.update(_registry())


def register(name: str, sujets: str | Path, cours: str | Path):
    import json
    rel = lambda p: str(Path(p).resolve().relative_to(ROOT)) if Path(p).resolve().is_relative_to(ROOT) else str(Path(p).resolve())
    reg = _registry()
    reg[name] = (rel(sujets), rel(cours))
    REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")
    DOMAINS[name] = reg[name]


def out_dir(name: str) -> Path:
    return ROOT / "output" / {"droit": "droit", "nsi": "nsi_prof"}.get(name, name)


def load(name: str, refresh: bool = False) -> Teacher:
    cache = ROOT / "data" / "cache" / f"meta_{name}.joblib"
    if cache.exists() and not refresh:
        return joblib.load(cache)
    s, c = DOMAINS[name]
    t = Teacher(ROOT / s, ROOT / c)
    t.relevant_parts()
    t.Q = [t.qs[i] for i in t.keep_idx]
    t.domain = name
    cache.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(t, cache)
    return t


def _toks(s: str) -> set[str]:
    return {w[:5] for w in re.findall(r"[a-z]{3,}", D.norm(s)) if w not in ("les", "des", "une", "sur", "langage")}


def eval_labels(t: Teacher) -> dict[int, set[int]]:
    """Index de question (dans t.Q) -> sections attendues. Évaluation seulement."""
    out = {}
    if any(t.refs.values()):
        for i, q in enumerate(t.Q):
            r = t.refs.get(q.exam)
            if r:
                out[i] = {int(x[1:]) for x in r}
        return out
    titles = [_toks(s.title) for s in t.sections]
    for i, q in enumerate(t.Q):
        m = re.search(r"[^.\n]*\b(porte|traite|aborde)\b[^.]*\.", q.situation[:600].replace("\n", " "))
        if not m:
            continue
        sent = _toks(m.group(0))
        hit = {si for si, tt in enumerate(titles) if tt and tt <= sent}
        if hit:
            out[i] = hit
    return out


# ===== examgen/meta/intent.py =====
"""Intentions de l'enseignant : pourquoi cette notion, tirée de cette partie du cours, posée ainsi.

Aucune variable d'intention n'est écrite à la main. On construit mécaniquement un large ensemble
de descripteurs RELATIONNELS entre la question et le cours (le même pour toute matière) :
  - pour chaque texte de la question (énoncé, situation, documents, corrigé) et chaque cible du
    cours (le passage visé, la section) : proximité, et part du vocabulaire propre au passage que
    le texte nomme explicitement ;
  - la place du passage visé dans le cours (rang dans la section, dans le cours), son poids
    (longueur, centralité, redondance ailleurs dans le cours, marques typographiques d'insistance),
  - l'histoire de la section dans les autres sujets (fréquence, années depuis la dernière fois),
  - la forme et la place de la question.
Puis scikit-learn décide ce qui compte, au moyen de tâches auto-supervisées que l'on peut poser sur
n'importe quel corpus (aucune étiquette humaine) :
  testabilite   quels passages du cours tombent l'année suivante (année exclue) ;
  consigne      la manière de demander s'explique-t-elle par la relation au cours, au-delà du rang ?
  ordre         la place d'une question dans la partie s'explique-t-elle par ce qu'elle demande ?
  bareme        le poids d'une question au barème (quand le sujet le donne) ;
Une variable est retenue si l'enlever (permutation) dégrade la tâche sur les sujets exclus ; elle
est dite universelle si elle est retenue dans plusieurs matières avec le même sens d'effet.
Les types d'intention sont ensuite découverts par mélange gaussien sur les variables retenues.
"""
from __future__ import annotations

import math
import re
from collections import Counter, defaultdict

import numpy as np
from scipy.stats import spearmanr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import log_loss
from ..fast import auc as roc_auc_score
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from ..prof import docs as D

SEED = 7
EMPH = re.compile(r"\*\*|__|`|^\s*[-•▪*]\s|^\s*\d+[.)]\s|!|:", re.M)


def _cos_rows(A, B):
    """cosinus ligne à ligne entre deux matrices creuses normalisées (tf-idf)."""
    return np.asarray(A.multiply(B).sum(1)).ravel()


class Intent:
    def __init__(self, t, S: np.ndarray):
        self.t, self.S = t, S
        Q = t.Q
        self.sec = S.argmax(1)
        # vocabulaire de mots (indépendant du réglage de lecture) pour « nommer » une notion
        self.wv = TfidfVectorizer(sublinear_tf=True, strip_accents="unicode", min_df=2, max_df=0.3,
                                  token_pattern=r"(?u)\b[^\W\d_]{4,}\b").fit(t.pass_text)
        self.Pw = self.wv.transform(t.pass_text)
        self.Pv = t.P  # passages, représentation choisie
        # passage visé : dans la section alignée, le passage le plus proche de la question entière
        full = [q.stem + " " + q.answer + " " + q.situation[:1500] for q in Q]
        X = t.vec.transform(full)
        sims = (X @ self.Pv.T).toarray()
        self.pas = np.array([int(np.where(t.pass_sec == s)[0][sims[i, t.pass_sec == s].argmax()]) for i, s in enumerate(self.sec)])
        self.pas_sim = sims
        self._course_stats()

    # ------------------------------------------------------------------ cours
    def _course_stats(self):
        t = self.t
        P = self.Pv
        n = P.shape[0]
        G = (P @ P.T).toarray()
        np.fill_diagonal(G, 0)
        self.p_central = G.mean(1)
        other = t.pass_sec[None, :] != t.pass_sec[:, None]
        self.p_redund = ((G > 0.35) & other).sum(1)
        self.p_len = np.log1p([len(x) for x in t.pass_text])
        self.p_emph = np.array([len(EMPH.findall(x)) / max(len(x), 1) * 100 for x in t.pass_text])
        self.p_ref = np.array([float(bool(t.ref_ids(x))) for x in t.pass_text])
        self.p_sym = np.array([sum(not c.isalnum() and not c.isspace() for c in x) / max(len(x), 1) for x in t.pass_text])
        rank = np.zeros(n)
        for s in range(len(t.sections)):
            ids = np.where(t.pass_sec == s)[0]
            rank[ids] = np.arange(len(ids)) / max(len(ids) - 1, 1)
        self.p_rank = rank
        self.s_order = np.array([s.order for s in t.sections], float) / max(len(t.sections) - 1, 1)
        self.s_size = np.log1p([len(s.passages) for s in t.sections])
        C = (t.C @ t.C.T).toarray()
        np.fill_diagonal(C, 0)
        self.s_central = C.mean(1)

    # ------------------------------------------------------------------ descripteurs
    def features(self) -> tuple[np.ndarray, list[str]]:
        t, Q = self.t, self.t.Q
        texts = {"enonce": [q.stem for q in Q], "situation": [q.situation[:3000] for q in Q],
                 "documents": [" ".join(x for _, x in q.annexes)[:6000] for q in Q],
                 "corrige": [q.answer for q in Q]}
        has_c = any(texts["corrige"])
        P = self.Pv[self.pas]
        Sec = t.C[self.sec]
        Pw = self.Pw[self.pas]
        F, names = [], []
        for k, tx in texts.items():
            if k == "corrige" and not has_c:
                continue
            X = t.vec.transform(tx)
            Xw = self.wv.transform(tx)
            F += [_cos_rows(X, P), _cos_rows(X, Sec)]
            names += [f"proximite_{k}_passage", f"proximite_{k}_section"]
            # part du vocabulaire propre au passage que ce texte nomme
            Xb = (Xw > 0).astype(float)
            Pb = Pw.copy()
            num = np.asarray(Pb.multiply(Xb).sum(1)).ravel()
            den = np.asarray(Pb.sum(1)).ravel() + 1e-9
            F.append(num / den)
            names.append(f"notion_nommee_dans_{k}")
        idx = {n: i for i, n in enumerate(names)}
        ref = "corrige" if has_c else "situation"
        F.append(F[idx[f"proximite_{ref}_passage"]] - F[idx["proximite_enonce_passage"]])
        names.append("notion_implicite_dans_l_enonce")
        Sr = self.S / (self.S.max(1, keepdims=True) + 1e-9)
        F.append((Sr > 0.8).sum(1))
        names.append("largeur_du_cours_mobilise")
        part_secs = defaultdict(set)
        for q, s in zip(Q, self.sec):
            part_secs[(q.exam, q.part)].add(s)
        F.append([len(part_secs[(q.exam, q.part)]) for q in Q])
        names.append("sections_dans_la_partie")
        # passage visé et sa section
        for arr, nm in ((self.p_rank, "rang_du_passage_dans_la_section"), (self.p_len, "longueur_du_passage"),
                        (self.p_central, "centralite_du_passage"), (self.p_redund, "redondance_du_passage"),
                        (self.p_emph, "insistance_typographique"), (self.p_ref, "passage_avec_reference"),
                        (self.p_sym, "densite_symboles_du_passage")):
            F.append(arr[self.pas]); names.append(nm)
        for arr, nm in ((self.s_order, "place_de_la_section_dans_le_cours"), (self.s_size, "taille_de_la_section"),
                        (self.s_central, "centralite_de_la_section")):
            F.append(arr[self.sec]); names.append(nm)
        fr, since = self._history()
        F += [fr, since]
        names += ["frequence_passee_de_la_section", "annees_depuis_la_derniere_fois"]
        # forme et place de la question
        F += [[q.position / max(q.n_in_part - 1, 1) for q in Q], [q.n_in_part for q in Q],
              np.log1p([len(q.stem) for q in Q]), [float(q.stem.rstrip().endswith("?")) for q in Q],
              [self._foreign(q.stem) for q in Q]]
        names += ["rang_dans_la_partie", "questions_dans_la_partie", "longueur_enonce", "forme_interrogative",
                  "vocabulaire_hors_cours_dans_l_enonce"]
        self.names = names
        self.F = np.column_stack([np.asarray(f, float) for f in F])
        return self.F, names

    def _foreign(self, s):
        w = re.findall(r"[a-z]{4,}", D.norm(s))
        voc = self.wv.vocabulary_
        return sum(x not in voc for x in w) / max(len(w), 1)

    def _history(self):
        Q = self.t.Q
        ex_secs = defaultdict(set)
        yr = {}
        for q, s in zip(Q, self.sec):
            ex_secs[q.exam].add(s)
            yr[q.exam] = q.year
        exams = list(ex_secs)
        fr, since = [], []
        for q, s in zip(Q, self.sec):
            others = [e for e in exams if e != q.exam]
            fr.append(np.mean([s in ex_secs[e] for e in others]) if others else 0)
            past = [yr[e] for e in others if s in ex_secs[e] and yr[e] and q.year and yr[e] < q.year]
            since.append((q.year - max(past)) if past else 5)
        return np.array(fr), np.array(since, float)

    # ------------------------------------------------------------------ tâches auto-supervisées
    def _imp(self, model, X, y, groups, metric, scoring, cols):
        """Score sur sujets exclus + importance par permutation (moyenne sur les plis)."""
        gkf = GroupKFold(n_splits=min(5, len(set(groups))))
        sc, base_sc, imps = [], [], []
        for tr, te in gkf.split(X, y, groups):
            if len(set(y[tr])) < 2 and scoring != "r2":
                continue
            m = model().fit(X[tr][:, cols], y[tr])
            sc.append(metric(m, X[te][:, cols], y[te]))
            pi = permutation_importance(m, X[te][:, cols], y[te], scoring=scoring, n_repeats=8, random_state=SEED)
            imps.append(pi.importances_mean)
        I = np.array(imps)
        return float(np.mean(sc)), I.mean(0), I.std(0) / math.sqrt(max(len(I), 1)), len(I)

    def tasks(self) -> dict:
        t, Q, F, names = self.t, self.t.Q, self.F, self.names
        groups = np.array([q.exam for q in Q])
        all_cols = np.arange(F.shape[1])
        res = {}
        lr = lambda: make_pipeline(StandardScaler(), LogisticRegression(C=0.3, max_iter=2000))
        rg = lambda: make_pipeline(StandardScaler(), Ridge(alpha=3.0))
        auc = lambda m, X, y: roc_auc_score(y, m.predict_proba(X)[:, 1]) if len(set(y)) > 1 else 0.5

        # ordre : la place d'une question s'explique-t-elle par ce qu'elle demande ?
        y = F[:, names.index("rang_dans_la_partie")]
        cols = np.array([i for i, n in enumerate(names) if n not in ("rang_dans_la_partie", "questions_dans_la_partie")])
        sp = lambda m, X, yy: spearmanr(m.predict(X), yy)[0]
        s, imp, se, k = self._imp(rg, F, y, groups, sp, "r2", cols)
        res["ordre"] = self._pack(s, "corrélation de rang (0 = rien)", imp, se, cols, F, y)

        # consigne : au-delà du rang, la relation au cours explique-t-elle la manière de demander ?
        if hasattr(Q[0], "facet"):
            yf = np.array([q.facet for q in Q])
            ll = lambda m, X, yy: -log_loss(yy, m.predict_proba(X), labels=m.classes_) if set(yy) <= set(m.classes_) else np.nan
            r_cols = np.array([names.index("rang_dans_la_partie"), names.index("questions_dans_la_partie")])
            s0, _, _, _ = self._imp(lr, F, yf, groups, ll, "neg_log_loss", r_cols)
            s1, imp, se, k = self._imp(lr, F, yf, groups, ll, "neg_log_loss", all_cols)
            res["consigne"] = self._pack(s1 - s0, "gain de log-vraisemblance sur le seul rang (> 0 = la relation au cours explique la consigne)",
                                         imp, se, all_cols, F, None)
            res["consigne"]["log_loss_rang_seul"] = round(-s0, 3)
            res["consigne"]["log_loss_avec_relation_au_cours"] = round(-s1, 3)

        # barème : poids de la question dans sa partie
        pts = np.array([q.points or np.nan for q in Q], float)
        if np.isfinite(pts).sum() > 60:
            tot = defaultdict(float)
            for q in Q:
                tot[(q.exam, q.part)] += q.points or 0
            share = np.array([(q.points or np.nan) / max(tot[(q.exam, q.part)], 1e-9) for q in Q])
            m = np.isfinite(share)
            s, imp, se, k = self._imp(rg, F[m], share[m], groups[m], sp, "r2", all_cols)
            res["bareme"] = self._pack(s, "corrélation de rang (0 = rien)", imp, se, all_cols, F[m], share[m])

        res["testabilite"] = self._testability()
        return res

    def _pack(self, score, unit, imp, se, cols, F, y):
        names = self.names
        keep = []
        for j, c in enumerate(cols):
            if imp[j] > 2 * se[j] and imp[j] > 0.002:
                d = None
                if y is not None:
                    d = float(np.sign(spearmanr(F[:, c], y)[0])) if np.std(F[:, c]) > 0 else 0.0
                keep.append({"variable": names[c], "importance": round(float(imp[j]), 4), "sens": d})
        keep.sort(key=lambda r: -r["importance"])
        return {"score_sujets_exclus": round(float(score), 3), "unite": unit, "variables_retenues": keep}

    def testability_data(self):
        """Passages : lesquels tombent une année donnée ? Variables calculées sans l'année visée."""
        t, Q = self.t, self.t.Q
        years = sorted({q.year for q in Q if q.year})
        n = len(t.pass_text)
        tested = defaultdict(set)
        for q, p in zip(Q, self.pas):
            if q.year:
                tested[q.year].add(int(p))
        names = ["rang_du_passage_dans_la_section", "longueur_du_passage", "centralite_du_passage", "redondance_du_passage",
                 "insistance_typographique", "passage_avec_reference", "densite_symboles_du_passage",
                 "place_de_la_section_dans_le_cours", "taille_de_la_section", "centralite_de_la_section",
                 "frequence_passee_du_passage", "frequence_passee_de_la_section"]
        X_all, y_all, g_all = [], [], []
        sec_of = t.pass_sec
        for y in years:
            others = [z for z in years if z != y]
            if not others:
                continue
            pf = np.array([np.mean([p in tested[z] for z in others]) for p in range(n)])
            sf = np.array([np.mean([any(sec_of[p] == s for p in tested[z]) for z in others]) for s in range(len(t.sections))])
            X = np.column_stack([self.p_rank, self.p_len, self.p_central, self.p_redund, self.p_emph, self.p_ref, self.p_sym,
                                 self.s_order[sec_of], self.s_size[sec_of], self.s_central[sec_of], pf, sf[sec_of]])
            X_all.append(X)
            y_all.append(np.array([p in tested[y] for p in range(n)], int))
            g_all.append(np.full(n, y))
        if len(X_all) < 3:
            return None
        return np.vstack(X_all), np.concatenate(y_all), np.concatenate(g_all), names

    def _testability(self) -> dict:
        d = self.testability_data()
        if d is None:
            return {}
        X, yv, g, names = d
        n = len(self.t.pass_text)
        lr = lambda: make_pipeline(StandardScaler(), LogisticRegression(C=0.3, max_iter=2000, class_weight="balanced"))
        auc = lambda m, A, b: roc_auc_score(b, m.predict_proba(A)[:, 1]) if len(set(b)) > 1 else 0.5
        old = self.names
        self.names = names
        cols = np.arange(X.shape[1])
        s, imp, se, k = self._imp(lr, X, yv, g, auc, "roc_auc", cols)
        pop = np.mean([roc_auc_score(yv[g == y], X[g == y, -1]) for y in np.unique(g) if len(set(yv[g == y])) > 1])
        pop_p = np.mean([roc_auc_score(yv[g == y], X[g == y, -2]) for y in np.unique(g) if len(set(yv[g == y])) > 1])
        out = self._pack(s, "AUC, année exclue (0,5 = hasard)", imp, se, cols, X, yv)
        self.names = old
        out["auc_popularite_de_la_section"] = round(float(pop), 3)
        out["auc_popularite_du_passage"] = round(float(pop_p), 3)
        out["passages"] = n
        return out

    # ------------------------------------------------------------------ types d'intention
    def types(self, keep: list[str]) -> dict:
        names = self.names
        cols = [names.index(k) for k in keep if k in names]
        if len(cols) < 2:
            cols = list(range(len(names)))
        Z = StandardScaler().fit_transform(self.F[:, cols])
        best = min(range(2, 8), key=lambda k: GaussianMixture(k, random_state=SEED, n_init=3).fit(Z).bic(Z))
        gm = GaussianMixture(best, random_state=SEED, n_init=5).fit(Z)
        lab = gm.predict(Z)
        out = []
        Q = self.t.Q
        for k in range(best):
            ids = np.where(lab == k)[0]
            mu = Z[ids].mean(0)
            fort = [names[cols[j]] for j in np.argsort(-mu)[:3] if mu[j] > 0.4]
            faible = [names[cols[j]] for j in np.argsort(mu)[:3] if mu[j] < -0.4]
            ex = ids[np.argsort(-gm.predict_proba(Z[ids])[:, k])[:3]]
            out.append({"id": k, "n": int(len(ids)), "part": round(len(ids) / len(Z), 3), "fort": fort, "faible": faible,
                        "exemples": [{"enonce": Q[i].stem[:220], "notion_du_cours": self.t.pass_text[self.pas[i]][:200]} for i in ex]})
        self.labels = lab
        return {"k": best, "variables_utilisees": [names[c] for c in cols], "types": out}

    def implicit(self, i: int, k: int = 6) -> list[str]:
        """Ce que la question évalue sans le dire : mots propres au passage visé, absents de
        l'énoncé et de la situation (présents dans le corrigé quand il existe)."""
        q = self.t.Q[i]
        row = self.Pw[self.pas[i]].toarray().ravel()
        voc = self.wv.get_feature_names_out()
        said = set(re.findall(r"[a-z]{4,}", D.norm(q.stem + " " + q.situation[:3000])))
        ans = set(re.findall(r"[a-z]{4,}", D.norm(q.answer))) if q.answer else None
        out = []
        for j in np.argsort(-row):
            if row[j] <= 0 or len(out) >= k:
                break
            w = voc[j]
            if w not in said and (ans is None or w in ans):
                out.append(w)
        return out


# ===== examgen/meta/learn.py =====
"""Apprendre à se débrouiller sur une matière inconnue, puis le prouver.

  python -m examgen.meta.learn            # toutes les matières de domain.DOMAINS

1. Alignement : méta-règle (quels signaux auto-supervisés désignent le bon réglage de lecture).
   Preuve : apprise sur une matière, appliquée à l'autre (matière exclue). La règle finale,
   apprise sur toutes les matières, est écrite dans data/model/meta.json ; le moteur l'emploie
   seul quand une matière nouvelle n'a pas de corrigé (Teacher.align).
2. Auto-entraînement : v0 (lecture auto-réglée) -> v1 -> ... chaque version entraîne la suivante,
   avec un garde-fou sans étiquette ; règle de lecture apprise SANS la matière évaluée.
3. Intentions : variables relationnelles cours <-> question, retenues par tâches auto-supervisées,
   puis bilan d'universalité (retenues dans plusieurs matières avec le même sens d'effet).
   Mesurées avant et après auto-entraînement (meilleur alignement -> meilleures intentions ?).
   Puis boucle (loop.py) : ce qu'il comprend des intentions de la matière (variables propres
   découvertes dans le cours, modèle choisi seul) corrige l'alignement, génération après génération.
4. Variables d'intention à grande échelle (deep.py) : centaines de variables générées, sélection
   par stabilité, transfert à froid entre matières.
Sortie : output/meta/rapport.json.
"""
from __future__ import annotations

import json
import sys
import warnings
from collections import defaultdict
from pathlib import Path

import joblib
import numpy as np

from . import align as A
from .domain import DOMAINS, eval_labels, load
from .intent import Intent
from . import deep as DP, loop as LP, selftrain as ST
from ..prof.profile import DEFAULT_CFG

ROOT = Path(__file__).resolve().parents[2]
META = ROOT / "data" / "model" / "meta.json"
OUT = ROOT / "output" / "meta"
ROWS = ROOT / "data" / "cache" / "meta_align_rows.joblib"


def alignment(names: list[str], refresh: bool = False) -> dict:
    rows = joblib.load(ROWS) if ROWS.exists() and not refresh else {}
    for n in names:
        if n not in rows:
            t = load(n)
            rows[n] = A.collect(t, eval_labels(t), n_ep=12)
    joblib.dump(rows, ROWS)
    rep = {"matiere_exclue": {}, "correlation_signal_reussite": {}}
    for te in names:
        tr = [r for n in names if n != te for r in rows[n]]
        if not tr:
            continue
        m = A.fit_meta(tr)
        rep["matiere_exclue"][f"appris_sans_{te}"] = {"poids": dict(zip(A.PROXIES, np.round(m.coef_, 3).tolist())), **A.pick(m, rows[te])}
    for n in names:
        X, y, _ = A.design(rows[n])
        rep["correlation_signal_reussite"][n] = {p: round(float(np.corrcoef(X[:, j], y)[0, 1]), 2) for j, p in enumerate(A.PROXIES)}
    # règle finale : toutes les matières, épisodes renumérotés pour rester distincts
    pooled = [dict(r, episode=f"{n}:{r['episode']}") for n in names for r in rows[n]]
    final = A.fit_meta(pooled)
    rule = {"signaux": A.PROXIES, "poids": np.round(final.coef_, 4).tolist(), "appris_sur": names}
    META.parent.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps(rule, ensure_ascii=False, indent=1), encoding="utf-8")
    rep["regle_finale"] = rule
    return rep


def selftraining(names: list[str]) -> tuple[dict, dict]:
    rows = joblib.load(ROWS)
    rep, start = {}, {}
    for n in names:
        others = [r for k in names if k != n for r in rows.get(k, [])]
        coef = A.fit_meta(others).coef_ if others else json.loads(META.read_text())["poids"]
        t = load(n)
        cfg, w, _ = A.self_tune(t, coef)
        S0 = A.combine(A.views(t, cfg), w)
        S, hist = ST.improve(t, S0, labels=eval_labels(t))
        S, cyc, it_rep = LP.run(t, S, labels=eval_labels(t))
        rep[n] = {"regle_de_lecture_apprise_sans_cette_matiere": True, "generations": hist,
                  "boucle_intentions_alignement": cyc, "intentions_propres_a_la_matiere": it_rep}
        start[n] = (t, S0, S)
        print(n, [h.get("vrai_top3") for h in hist])
    return rep, start


def _intent(t, S):
    t.rep = getattr(t, "rep", {})
    for q, s in zip(t.Q, S.argmax(1)):
        q.sec = int(s)
    t.consigne_vocab()
    t.consigne_facets()
    it = Intent(t, S)
    it.features()
    return it


def intentions(names: list[str], start: dict) -> dict:
    per, avant_apres, tdata = {}, {}, {}
    for n in names:
        t, S0, S = start[n]
        it0 = _intent(t, S0)
        r0 = it0.tasks()
        it = _intent(t, S)
        res = it.tasks()
        tdata[n] = it.testability_data()
        sc = lambda r, k: r.get(k, {}).get("score_sujets_exclus")
        avant_apres[n] = {k: {"avant": sc(r0, k), "apres": sc(res, k)} for k in res if sc(res, k) is not None}
        keep = sorted({v["variable"] for k, r in res.items() if k != "testabilite" for v in r.get("variables_retenues", [])})
        ty = it.types(keep)
        step = max(1, len(t.Q) // 6)
        per[n] = {"questions": len(t.Q), "taches": res, "types_d_intention": ty,
                  "ce_qui_est_evalue_sans_etre_dit": [{"enonce": t.Q[i].stem[:180], "mots": it.implicit(i)} for i in range(0, len(t.Q), step)]}
    # universalité : même tâche, même variable, retenue partout, même sens
    uni = defaultdict(list)
    for n, r in per.items():
        for task, tr in r["taches"].items():
            for v in tr.get("variables_retenues", []):
                uni[(task, v["variable"])].append((n, v["sens"], v["importance"]))
    universal = []
    for (task, var), lst in uni.items():
        if len({x[0] for x in lst}) == len(names) > 1:
            signs = {x[1] for x in lst}
            universal.append({"tache": task, "variable": var, "meme_sens": len(signs) == 1,
                              "importance": {x[0]: x[2] for x in lst}, "sens": lst[0][1] if len(signs) == 1 else "variable"})
    universal.sort(key=lambda r: (r["tache"], -min(r["importance"].values())))
    deep = DP.study({n: d for n, d in tdata.items() if d is not None})
    return {"par_matiere": per, "universelles": universal, "avant_apres_auto_entrainement": avant_apres, "grande_echelle": deep}


def main(argv=None):
    warnings.filterwarnings("ignore")
    names = (argv or sys.argv[1:]) or list(DOMAINS)
    rep = {"alignement": alignment(names)}
    rep["auto_entrainement"], start = selftraining(names)
    rep["intentions"] = intentions(names, start)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "rapport.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    for k, v in rep["alignement"]["matiere_exclue"].items():
        print(k, {x: v[x] for x in ("choisi_par_le_meta_modele", "reglage_par_defaut", "meilleur_possible_oracle")})
    print("avant/après", rep["intentions"]["avant_apres_auto_entrainement"])
    print("grande échelle", {k: v for k, v in rep["intentions"]["grande_echelle"].items() if k != "par_matiere"})
    for u in rep["intentions"]["universelles"]:
        print("universelle", u["tache"], u["variable"], u["sens"], u["importance"])
    print("->", OUT / "rapport.json", "et", META)


if __name__ == "__main__":
    main()


# ===== examgen/meta/loop.py =====
"""Boucle complète sur une matière inconnue : rien que ses anciens sujets et son cours.

Chaque génération :
  1. le moteur relie les questions au cours (version actuelle) ;
  2. il découvre les variables PROPRES à la matière dans le cours lui-même : des thèmes (NMF sur
     les mots des passages) et des formes (NMF sur les suites de caractères : code, dates,
     formules...), nommés par leurs mots les plus forts ;
  3. il apprend « quel passage tombe quelle année » sur les autres années, avec plusieurs
     familles de modèles (logistique sur les 12 variables génériques, arbres boostés sur les
     12, arbres boostés sur génériques + propres à la matière + croisements) ; il choisit la
     famille lui-même, par validation emboîtée sur ses propres années passées ;
  4. ce qu'il a compris des intentions (probabilité qu'une section tombe cette année-là, prédite
     sans cette année) devient un a priori qui corrige l'alignement : version suivante ;
  5. garde-fou sans étiquette : diversité du cours conservée, arrêt à la convergence.
Aucune règle n'est apprise sur une autre matière : seule la procédure est commune.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import spearmanr
from sklearn.decomposition import NMF
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from ..fast import auc as roc_auc_score
from ..fast import pmap

from . import align as A, deep as DP, selftrain as ST
from .intent import Intent

PRIOR = 0.5  # poids de l'a priori d'intention dans l'alignement (même valeur pour toute matière)


def course_variables(pass_text: list[str], k_words: int = 12, k_form: int = 6):
    out, names = [], []
    for k, kw, tag in ((k_words, dict(token_pattern=r"(?u)\b[^\W\d_]{3,}\b"), "theme"),
                       (k_form, dict(analyzer="char_wb", ngram_range=(2, 4)), "forme")):
        v = TfidfVectorizer(sublinear_tf=True, strip_accents="unicode", min_df=2, max_df=0.5, **kw)
        X = v.fit_transform(pass_text)
        k = min(k, X.shape[1] - 1, X.shape[0] - 1)
        m = NMF(k, init="nndsvda", random_state=0, max_iter=400)
        W = m.fit_transform(X)
        voc = np.array(v.get_feature_names_out())
        out.append(W / (W.sum(1, keepdims=True) + 1e-9))
        names += [f"{tag}:" + "/".join(x.strip() or "_" for x in voc[np.argsort(-c)[:3]]) for c in m.components_]
    return np.hstack(out), names


def _hgb():
    return HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=200, l2_regularization=1.0,
                                          class_weight="balanced", random_state=0)


FAMILIES = {"logistique_12_generiques": ("base", DP._lr), "arbres_12_generiques": ("base", _hgb),
            "arbres_generiques_et_propres_a_la_matiere": ("full", _hgb)}


def _design(X, nm, T, n_pass):
    pidx = np.arange(len(X)) % n_pass
    Tm = T[pidx]
    deja = X[:, [nm.index("frequence_passee_du_passage")]]
    sec = X[:, [nm.index("frequence_passee_de_la_section")]]
    return np.hstack([X, Tm, Tm * deja, Tm * sec])


def _fit_pred(fam, Xb, Xf, y, tr, te):
    kind, mk = FAMILIES[fam]
    Z = Xb if kind == "base" else Xf
    return mk().fit(Z[tr], y[tr]).predict_proba(Z[te])[:, 1]


def testability(X, y, g, nm, T, tnames, n_pass) -> dict:
    """Validation emboîtée par année : pour chaque année testée, la famille est choisie sur les
    autres années seulement. Renvoie aussi les probabilités hors année (pour l'a priori)."""
    Xf = _design(X, nm, T, n_pass)
    years = [k for k in np.unique(g) if len(set(y[g == k])) > 1]
    per = {f: [] for f in FAMILIES}
    chosen, auc_chosen, prob = [], [], np.zeros(len(y))
    def one(k):  # une année testée : indépendante des autres
        tr, te = g != k, g == k
        inner = {}
        for f in FAMILIES:
            sc = []
            for j in [j for j in years if j != k][:6]:  # 6 années internes suffisent à départager
                itr, ite = tr & (g != j), g == j
                sc.append(roc_auc_score(y[ite], _fit_pred(f, X, Xf, y, itr, ite)))
            inner[f] = np.mean(sc)
        best = max(inner, key=inner.get)
        return best, {f: _fit_pred(f, X, Xf, y, tr, te) for f in FAMILIES}

    ks = list(np.unique(g))
    for k, (best, p) in zip(ks, pmap(one, ks)):
        te = g == k
        prob[te] = p[best]
        if k in years:
            for f in FAMILIES:
                per[f].append(roc_auc_score(y[te], p[f]))
            chosen.append(best)
            auc_chosen.append(roc_auc_score(y[te], p[best]))
    final = max(set(chosen), key=chosen.count)
    rules = _rules(final, X, Xf, y, nm, tnames)
    return {"auc_par_famille": {f: round(float(np.mean(v)), 3) for f, v in per.items()},
            "auc_famille_choisie_seule": round(float(np.mean(auc_chosen)), 3),
            "famille_choisie": final, "choix_par_annee": {f: chosen.count(f) for f in set(chosen)},
            "auc_popularite": round(float(np.mean([roc_auc_score(y[g == k], X[g == k, -2]) for k in years])), 3),
            "regles_decouvertes": rules, "_prob": prob}


def _rules(fam, X, Xf, y, nm, tnames, top: int = 10):
    """Variables qui pèsent le plus dans le modèle final (permutation sur un échantillon) et sens."""
    kind, mk = FAMILIES[fam]
    Z = X if kind == "base" else Xf
    names = list(nm) + ([f"{t}" for t in tnames] + [f"{t} × déjà tombé" for t in tnames] + [f"{t} × section déjà tombée" for t in tnames]
                        if kind == "full" else [])
    m = mk().fit(Z, y)
    rng = np.random.default_rng(0)
    idx = rng.choice(len(y), min(len(y), 4000), replace=False)
    Zs, ys = Z[idx], y[idx]
    base = roc_auc_score(ys, m.predict_proba(Zs)[:, 1])
    imp = []
    for j in range(Z.shape[1]):
        Zp = Zs.copy()
        Zp[:, j] = rng.permutation(Zp[:, j])
        imp.append(base - roc_auc_score(ys, m.predict_proba(Zp)[:, 1]))
    pred = m.predict_proba(Zs)[:, 1]
    out = []
    for j in np.argsort(imp)[::-1][:top]:
        if imp[j] <= 0.001:
            break
        r = spearmanr(Zs[:, j], pred)[0] if Zs[:, j].std() > 0 else 0
        out.append({"variable": DP.SHORT.get(names[j], names[j]), "importance": round(float(imp[j]), 4),
                    "sens": "+" if r > 0 else "-", "propre_a_la_matiere": bool(j >= len(nm))})
    return out


def section_prior(t, prob, g, n_pass) -> np.ndarray:
    """Pour chaque question : z-score du log de la probabilité (prédite sans son année) que
    chaque section tombe cette année-là."""
    K, ps = len(t.sections), np.asarray(t.pass_sec)
    by_year = {}
    for k in np.unique(g):
        p = prob[g == k]
        by_year[k] = np.log(np.array([p[ps == s].max() if (ps == s).any() else 1e-3 for s in range(K)]) + 1e-3)
    Pm = np.array([by_year.get(q.year, np.zeros(K)) for q in t.Q])
    return (Pm - Pm.mean(1, keepdims=True)) / (Pm.std(1, keepdims=True) + 1e-9)


def run(t, S, labels=None, gens: int = 3, log=print):
    """S : alignement après auto-entraînement (selftrain.improve). Renvoie l'alignement final,
    l'historique et le dernier bilan d'intentions."""
    allx = (np.arange(len(t.Q)), np.arange(len(t.sections)))
    meas = (lambda M: round(A.truth(M, labels, *allx), 3)) if labels else (lambda M: None)
    T, tnames = course_variables(t.pass_text)
    d0 = ST.diversity(S)
    S_start = ST.rz(S)  # ancre : l'a priori corrige la version de départ, il ne s'accumule pas
    hist, rep = [], None
    for gen in range(gens + 1):
        for q, s in zip(t.Q, S.argmax(1)):
            q.sec = int(s)
        it = Intent(t, S)
        it.features()
        d = it.testability_data()
        if d is None:
            break
        X, y, g, nm = d
        rep = testability(X, y, g, nm, T, tnames, len(t.pass_text))
        hist.append({"generation": gen, "vrai_top3": meas(S), "auc_intention": rep["auc_famille_choisie_seule"],
                     "famille": rep["famille_choisie"], "diversite": round(ST.diversity(S), 3)})
        log(f"    génération {gen} : {hist[-1]}")
        if gen == gens:
            break
        new = S_start + PRIOR * section_prior(t, rep["_prob"], g, len(t.pass_text))
        changed = float(np.mean(new.argmax(1) != S.argmax(1)))
        if ST.diversity(new) < ST.GARDE * d0 or changed < 0.01:
            hist[-1]["arret"] = "diversité écrasée" if changed >= 0.01 else "convergence"
            break
        S = new
    rep.pop("_prob", None)
    rep["variables_propres_decouvertes"] = tnames
    return S, hist, rep


# ===== examgen/meta/selftrain.py =====
"""Auto-entraînement par générations : chaque version du moteur entraîne la suivante.

  v0  lecture du cours auto-réglée (align.self_tune) ;
  vk+1 un « élève » est entraîné sur ce que vk sait :
         - les passages du cours, étiquetés gratuitement par leur section ;
         - les questions sur lesquelles vk est le plus sûr de lui (pseudo-étiquettes),
           toujours prédites hors pli (sujet exclu), pour qu'il ne recopie pas son maître ;
       puis l'élève est fusionné avec son maître.
  Plusieurs candidats sont produits à chaque génération (part de pseudo-étiquettes, poids
  de l'élève). Une RÈGLE D'ACCEPTATION méta-apprise choisit le candidat, ou garde la version
  actuelle (arrêt). Elle ne voit que des signaux auto-supervisés : elle a appris, sur d'autres
  matières, quels signaux annoncent un vrai progrès. Aucune étiquette au moment de l'emploi.
"""
from __future__ import annotations

import numpy as np
from scipy.sparse import vstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge, SGDClassifier
from sklearn.model_selection import GroupKFold

from . import align as A

PROXIES = A.PROXIES + ["stabilite", "confiance", "accord_eleve", "accord_v0", "accord_lecteur_du_cours", "precision_estimee"]
QFRAC = (0.0, 0.3, 0.6)
BETA = (0.25, 0.5, 0.75, 1.0)


def rz(S):
    return (S - S.mean(1, keepdims=True)) / (S.std(1, keepdims=True) + 1e-9)


def margin(S):
    s = np.sort(rz(S), 1)
    return s[:, -1] - s[:, -2]


class Student:
    """Lecteur indépendant du maître (mots 1-2), réutilisé à chaque génération."""

    def __init__(self, t):
        Q = t.Q
        qt = [" ".join([q.stem, q.preamble, q.situation[:3000], " ".join(x for _, x in q.annexes)[:4000], q.answer]) for q in Q]
        v = TfidfVectorizer(sublinear_tf=True, strip_accents="unicode", min_df=2, max_df=0.5, ngram_range=(1, 2),
                            token_pattern=r"(?u)\b\w\w+\b").fit(t.pass_text + qt)
        self.XP, self.XQ = v.transform(t.pass_text), v.transform(qt)
        self.yP = np.asarray(t.pass_sec)
        self.K = len(t.sections)
        self.groups = np.array([q.exam for q in Q])
        self._course_only = None

    def _fit(self, X, y, w):
        return SGDClassifier(loss="log_loss", alpha=2e-5, max_iter=12, tol=None, random_state=0).fit(X, y, sample_weight=w)

    def _place(self, clf, X):
        out = np.full((X.shape[0], self.K), -20.0)
        out[:, clf.classes_] = clf.predict_log_proba(X)
        return out

    def predict(self, S_teacher, qfrac: float) -> np.ndarray:
        if qfrac == 0:
            if self._course_only is None:
                self._course_only = self._place(self._fit(self.XP, self.yP, np.ones(len(self.yP))), self.XQ)
            return self._course_only
        lab, conf = S_teacher.argmax(1), margin(S_teacher)
        sel = conf >= np.quantile(conf, 1 - qfrac)
        out = np.zeros((self.XQ.shape[0], self.K))
        n = min(4, len(set(self.groups)))
        for tr, te in GroupKFold(n_splits=n).split(self.XQ, groups=self.groups):
            ts = tr[sel[tr]]
            X = vstack([self.XP, self.XQ[ts]])
            y = np.concatenate([self.yP, lab[ts]])
            w = np.concatenate([np.ones(len(self.yP)), 1 + conf[ts] / (conf[ts].mean() + 1e-9)])
            out[te] = self._place(self._fit(X, y, w), self.XQ[te])
        return out


def candidates(cur, prev_top, stu: Student):
    out = [("garder", cur)]
    for q in QFRAC:
        P = rz(stu.predict(cur, q))
        for b in BETA:
            out.append(((q, b), (1 - b) * rz(cur) + b * P))
    return out


def signals(V, S, idx, cols, prev, stu, v0, course) -> dict:
    """prev, stu, v0, course : matrices de scores (version actuelle, élève du candidat,
    version de départ, lecteur entraîné sur le seul cours)."""
    p = A.proxies(V, S, idx, cols)
    sub = lambda M: M[np.ix_(idx, cols)].argmax(1)
    top = sub(S)
    p["stabilite"] = float(np.mean(top == sub(prev)))
    p["confiance"] = float(np.mean(margin(S[np.ix_(idx, cols)])))
    p["accord_eleve"] = float(np.mean(top == sub(stu)))
    p["accord_v0"] = float(np.mean(top == sub(v0)))
    p["accord_lecteur_du_cours"] = float(np.mean(top == sub(course)))
    p["precision_estimee"] = triplet(top, [sub(V["stem"]), sub(V["sit"] + V["anx"]), sub(course)])
    return p


def triplet(top, views) -> float:
    """Précision estimée sans étiquette : si deux lecteurs indépendants X, Y ont des précisions
    pX, pY, ils s'accordent environ pX*pY fois ; donc p(S)^2 ~ accord(S,X)*accord(S,Y)/accord(X,Y)."""
    ag = lambda a, b: max(float(np.mean(a == b)), 1e-3)
    est = []
    for i in range(len(views)):
        for j in range(i + 1, len(views)):
            est.append(np.sqrt(ag(top, views[i]) * ag(top, views[j]) / ag(views[i], views[j])))
    return float(np.median(est))


def _z(x):
    x = np.asarray(x, float)
    return (x - x.mean()) / (x.std() + 1e-9)


def design(rows):
    eps = np.array([r["episode"] for r in rows])
    X = np.zeros((len(rows), len(PROXIES)))
    y = np.zeros(len(rows))
    for e in np.unique(eps):
        m = np.where(eps == e)[0]
        for j, p in enumerate(PROXIES):
            X[m, j] = _z([rows[i][p] for i in m])
        y[m] = _z([rows[i]["vrai"] for i in m])
    return X, y, eps


def fit_rule(rows, min_sign=0.75) -> list[float]:
    """Règle invariante : on ne garde que les signaux dont l'effet a le même sens dans au moins
    min_sign des épisodes d'entraînement (sous-matières simulées) ; les autres sont propres à
    une matière et ne se transfèrent pas."""
    X, y, eps = design(rows)
    keep = []
    for j in range(X.shape[1]):
        c = [np.corrcoef(X[eps == e, j], y[eps == e])[0, 1] for e in np.unique(eps) if X[eps == e, j].std() > 0 and y[eps == e].std() > 0]
        c = np.nan_to_num(c)
        keep.append(len(c) > 0 and max(np.mean(c > 0), np.mean(c < 0)) >= min_sign)
    coef = np.zeros(X.shape[1])
    if any(keep):
        k = np.array(keep)
        coef[k] = Ridge(alpha=1.0, fit_intercept=False).fit(X[:, k], y).coef_
    return coef.tolist()


def run(t, align_coef, rule=None, labels=None, gens: int = 6, n_ep: int = 8, follow="regle", seed=0, log=print):
    """Boucle de générations. follow='regle' : la règle d'acceptation choisit (emploi réel) ;
    follow='oracle' : on suit le meilleur candidat selon la vérité (seulement pour produire des
    exemples d'apprentissage de la règle, sur une matière d'entraînement)."""
    cfg, w, _ = A.self_tune(t, align_coef)
    V = A.views(t, cfg)
    cur = A.combine(V, w)
    stu = Student(t)
    course = stu.predict(cur, 0)
    v0 = cur
    rng = np.random.default_rng(seed)
    eps = A.episodes(t, labels or {}, n_ep, rng) if labels else []
    allx = (np.arange(len(t.Q)), np.arange(len(t.sections)))
    hist, rows = [], []
    truth = lambda S: A.truth(S, labels, *allx) if labels else None
    hist.append({"version": 0, "reglage": "lecture auto-réglée", "vrai_top3": truth(cur)})
    log(f"    v0 {hist[-1]}")
    prev_top = cur.argmax(1)
    for g in range(1, gens + 1):
        C = candidates(cur, prev_top, stu)
        studs = {q: stu.predict(cur, q) for q in QFRAC}
        sig = []
        for k, S in C:
            st = studs[k[0]] if k != "garder" else course
            sig.append(signals(V, S, *allx, cur, st, v0, course))
            for ei, (idx, cols) in enumerate(eps):
                tr = A.truth(S, labels, idx, cols)
                if tr is not None:
                    rows.append({"episode": f"{t.domain}:{seed}:{g}:{ei}", "cand": str(k), "vrai": tr,
                                 **signals(V, S, idx, cols, cur, st, v0, course)})
        if follow == "oracle":
            best = int(np.argmax([truth(S) for _, S in C]))
        elif follow == "hasard":  # états variés pour apprendre la règle (pas seulement le chemin idéal)
            best = int(rng.integers(1, len(C)))
        else:
            X = np.column_stack([_z([s[p] for s in sig]) for p in PROXIES])
            best = int((X @ np.asarray(rule)).argmax())
        k, S = C[best]
        if k == "garder":
            log(f"    v{g}: la règle garde la version précédente -> arrêt")
            break
        prev_top, cur = cur.argmax(1), S
        hist.append({"version": g, "reglage": {"part_pseudo_etiquettes": k[0], "poids_eleve": k[1]}, "vrai_top3": truth(cur)})
        log(f"    v{g} {hist[-1]}")
    t.S_self = cur
    return cur, hist, rows


POLICIES = [(q, b) for q in (0.0, 0.3, 0.6) for b in (0.25, 0.5, 1.0)]


def run_policy(t, align_coef, policy, gens: int = 5, labels=None, tol: float = 0.01, stu=None, start=None):
    """Politique fixe (part de pseudo-étiquettes, poids de l'élève) répétée génération après
    génération ; arrêt quand la nouvelle version change moins de tol des réponses (convergence)."""
    if start is None:
        cfg, w, _ = A.self_tune(t, align_coef)
        start = A.combine(A.views(t, cfg), w)
    stu = stu or Student(t)
    q, b = policy
    cur = start
    allx = (np.arange(len(t.Q)), np.arange(len(t.sections)))
    hist = [A.truth(cur, labels, *allx) if labels else None]
    for g in range(gens):
        new = (1 - b) * rz(cur) + b * rz(stu.predict(cur, q))
        changed = float(np.mean(new.argmax(1) != cur.argmax(1)))
        cur = new
        hist.append(A.truth(cur, labels, *allx) if labels else None)
        if changed < tol:
            break
    return cur, hist


# ---------------------------------------------------------------------------------------------
# Procédure retenue (la même pour toutes les matières, validée matière exclue) :
#   1. cohérence de partie : les questions d'une même partie d'un sujet portent sur un même thème ;
#      chaque question emprunte une part LISSAGE du profil moyen de sa partie ;
#   2. générations : l'élève (cours seul, poids ELEVE) corrige son maître, puis on relisse ;
#   3. garde-fou sans étiquette : une génération est refusée si elle écrase la diversité du cours
#      (moins de GARDE x la diversité de départ) ou ne change presque plus rien (convergence).
# Les règles par signal (ci-dessus) ne se transféraient pas d'une matière à l'autre ; cette
# procédure, si : droit 0,78 -> 0,87, NSI 0,77 -> 0,82 (top 3, vérité cachée au moteur).
LISSAGE, ELEVE, GARDE = 0.75, 0.25, 0.9


def diversity(S) -> float:
    c = np.bincount(S.argmax(1), minlength=S.shape[1]) / len(S)
    c = c[c > 0]
    return float(-(c * np.log(c)).sum() / np.log(S.shape[1]))


def smooth(t, S, g: float = LISSAGE):
    Z = rz(S)
    key = np.array([hash((q.exam, q.part)) for q in t.Q])
    out = Z.copy()
    for k in np.unique(key):
        m = key == k
        out[m] = (1 - g) * Z[m] + g * Z[m].mean(0)
    return out


def improve(t, S0, gens: int = 5, labels=None, stu=None):
    """v0 -> v1 -> ... ; chaque version est entraînée par la précédente. labels : seulement pour
    mesurer (jamais pour décider)."""
    stu = stu or Student(t)
    allx = (np.arange(len(t.Q)), np.arange(len(t.sections)))
    meas = (lambda S: round(A.truth(S, labels, *allx), 3)) if labels else (lambda S: None)
    d0 = diversity(S0)
    hist = [{"version": "v0 lecture auto-réglée", "vrai_top3": meas(S0), "diversite": round(d0, 3)}]
    cur = smooth(t, S0)
    hist.append({"version": "v1 cohérence de partie", "vrai_top3": meas(cur), "diversite": round(diversity(cur), 3)})
    for g in range(gens):
        new = smooth(t, (1 - ELEVE) * rz(cur) + ELEVE * rz(stu.predict(cur, 0)))
        changed = float(np.mean(new.argmax(1) != cur.argmax(1)))
        if diversity(new) < GARDE * d0:
            hist.append({"version": f"v{g + 2} refusée", "raison": "diversité du cours écrasée", "vrai_top3": meas(new)})
            break
        if changed < 0.01:
            hist.append({"version": f"v{g + 2} inutile", "raison": "convergence (moins de 1 % de réponses changées)"})
            break
        cur = new
        hist.append({"version": f"v{g + 2} entraînée par v{g + 1}", "vrai_top3": meas(cur), "diversite": round(diversity(cur), 3),
                     "reponses_changees": round(changed, 3)})
    return cur, hist


# ===== examgen/meta/transfer.py =====
"""Méta-entraînement pour les domaines inconnus : apprendre à se juger et à se choisir.

But : sur une matière jamais vue (cours + anciens sujets seulement), choisir les bonnes variables
et le bon modèle, et annoncer à l'avance quelle qualité on peut en attendre.

1. Tâches. Chaque (matière, année testée) est une tâche. Pour en avoir beaucoup, chaque cours est
   aussi découpé en « pseudo-domaines » : la moitié de ses chapitres, tirée au hasard. Une tâche ne
   voit que les années d'avant l'année testée.
2. Candidats. Familles de variables (y compris des croisements construits automatiquement) ×
   modèles, purs ou mêlés à l'ancienne méthode. Pour chaque candidat : son score en validation
   interne (années passées seulement) et son vrai score sur l'année testée.
3. Juge. Un méta-modèle apprend, à partir de traits du domaine (taille, répétition des questions,
   concentration des chapitres…) et du score interne de chaque candidat, à prédire son vrai gain
   sur l'ancienne méthode. Il corrige l'optimisme de la validation interne selon le domaine.
4. Preuve « matière inconnue ». Le juge est appris sans la matière testée (ni ses pseudo-domaines),
   puis appliqué à elle. On compare à l'ancienne méthode et à l'auto-progression précédente.
   Il annonce aussi le score attendu ; on mesure l'écart avec le score réel (auto-jugement).

    python -m examgen.meta.transfer tasks droit      # (une matière par processus)
    python -m examgen.meta.transfer judge droit nsi eco
    python -m examgen.meta.transfer rule droit nsi eco   # règle universelle retenue (voir plus bas)
"""
from __future__ import annotations

import json
import sys
import warnings
from itertools import product

import joblib
import numpy as np
from scipy.stats import rankdata
from sklearn.ensemble import ExtraTreesRegressor
from ..fast import auc as roc_auc_score

from . import autoprog as AP
from ..fast import pmap

CACHE = AP.CACHE
OUT = AP.ROOT / "output" / "meta" / "transfer.json"
MODEL = AP.ROOT / "data" / "model" / "transfer.joblib"
TOP = AP.TOP
GROUPS = AP.GROUPS + ["croisements"]
SETS = [()] + [(g,) for g in GROUPS] + [tuple(GROUPS)]
FIT_MODELS = ["logistique", "arbres"]
N_MASKS = 5
OBJ = ("prevision", "nouveaute")


# ---------------------------------------------------------------------------- variables construites
class TVars(AP.Vars):
    """Ajoute une famille construite sans intervention : chaque famille croisée avec la popularité."""

    def get(self, target, hist):
        g = super().get(target, hist)
        if "croisements" not in g:
            pf = g["base"][:, 10:11]
            g["croisements"] = np.hstack([pf * g[k][:, :1] for k in AP.GROUPS] + [pf * g["base"][:, :10]])
        return g


# ---------------------------------------------------------------------------- domaine masqué
class Domain:
    """Une matière, ou un pseudo-domaine (sous-ensemble de chapitres)."""

    def __init__(self, fc, V, mask):
        self.fc, self.V, self.mask = fc, V, mask
        self.idx = np.where(mask)[0]
        self.n = len(self.idx)
        self.memo = {}
        m = set(self.idx.tolist())
        self.Y = {z: np.array([p in fc.tested[z] for p in self.idx], int) for z in fc.years}
        self.Q = {z: [int(fc.it.pas[i]) for i in fc.q_of[z] if int(fc.it.pas[i]) in m] for z in fc.years}

    def y(self, z):
        return self.Y[z]

    def qs(self, z):
        return self.Q[z]

    def X(self, target, train, groups):
        return self.V.matrix(target, train, list(groups))[self.idx]

    def predict(self, groups, model, target, train, obj):
        key = (groups, model, target, tuple(train), obj)
        if key in self.memo:
            return self.memo[key]
        if model == "melange":
            p = (rankdata(self.predict(groups, "logistique", target, train, obj)) +
                 rankdata(self.predict(groups, "arbres", target, train, obj))) / (2 * self.n)
        elif model == "ancienne":
            p = self.reference(target, train, obj)
        else:
            Xs, ys = [], []
            for z in train:
                X, yz = self.X(z, train, groups), self.y(z)
                if obj == "nouveaute":
                    others = [w for w in train if w != z]
                    fresh = ~np.any([self.y(w) for w in others], 0) if others else np.ones(self.n, bool)
                    X, yz = X[fresh], yz[fresh]
                Xs.append(X)
                ys.append(yz)
            Xtr, ytr = np.vstack(Xs), np.concatenate(ys)
            p = np.zeros(self.n) if len(set(ytr)) < 2 else AP.fit_predict(model, Xtr, ytr, self.X(target, train, groups))
        self.memo[key] = p
        return p

    def reference(self, target, train, obj):
        B = self.V.get(target, train)["base"][self.idx]
        if obj == "prevision":
            return B[:, 10] + 0.01 * B[:, 11]
        Xtr = np.vstack([self.V.get(z, train)["base"][self.idx][:, :10] for z in train])
        ytr = np.concatenate([self.y(z) for z in train])
        return AP._lr().fit(Xtr, ytr).predict_proba(B[:, :10])[:, 1] if len(set(ytr)) > 1 else np.zeros(self.n)

    def score(self, p, target, past, obj):
        yt, qs = self.y(target), self.qs(target)
        pos = {int(g): k for k, g in enumerate(self.idx)}
        if obj == "prevision":
            if not qs or len(set(yt)) < 2:
                return None
            sel = set(np.argsort(-p)[:max(1, int(TOP * self.n))].tolist())
            cov = float(np.mean([pos[q] in sel for q in qs]))
            return {"couverture": cov, "auc": float(roc_auc_score(yt, p)), "score": cov + 0.1 * float(roc_auc_score(yt, p))}
        seen = np.any([self.y(z) for z in past], 0) if past else np.zeros(self.n, bool)
        fr = np.where(~seen)[0]
        new = [pos[q] for q in qs if not seen[pos[q]]]
        if len(fr) < 10 or len(set(yt[fr])) < 2 or not new:
            return None
        sel = set(fr[np.argsort(-p[fr])[:max(1, int(0.25 * len(fr)))]].tolist())
        cov = float(np.mean([q in sel for q in new]))
        auc = float(roc_auc_score(yt[fr], p[fr]))
        return {"couverture": cov, "auc": auc, "score": cov + 0.1 * auc}

    def traits(self, past):
        """Ce qu'on sait du domaine avant l'année testée (rien de l'année testée)."""
        fc, ps = self.fc, np.asarray(self.fc.t.pass_sec)[self.idx]
        qn = [len(self.qs(z)) for z in past]
        rep = []
        for k, z in enumerate(past[1:], 1):
            before = np.any([self.y(w) for w in past[:k]], 0)
            q = self.qs(z)
            pos = {int(g): i for i, g in enumerate(self.idx)}
            if q:
                rep.append(np.mean([before[pos[x]] for x in q]))
        ever = np.any([self.y(z) for z in past], 0)
        secs = ps[ever]
        _, c = np.unique(secs, return_counts=True) if len(secs) else (None, np.array([1]))
        pr = c / c.sum()
        ent = float(-(pr * np.log(pr)).sum() / np.log(max(2, len(set(ps)))))
        return {"log_passages": float(np.log(self.n)), "annees_passees": len(past),
                "questions_par_an": float(np.mean(qn)), "log_questions_par_passage": float(np.log((np.mean(qn) + 1) / self.n)),
                "repetition": float(np.mean(rep)) if rep else 0.0, "part_deja_tombee": float(ever.mean()),
                "dispersion_des_chapitres": ent, "chapitres": float(len(set(ps)))}


def candidates():
    """(familles, modèle, mêlé à l'ancienne méthode ?) ; l'ancienne méthode seule est un candidat."""
    out = [((), "ancienne", False)]
    for gs, m in product(SETS, FIT_MODELS + ["melange"]):
        out += [(gs, m, False), (gs, m, True)]
    return out


def cand_pred(D, c, target, train, obj):
    gs, m, mix = c
    p = D.predict(gs, m, target, train, obj)
    if mix:
        p = (rankdata(p) + rankdata(D.predict((), "ancienne", target, train, obj))) / (2 * D.n)
    return p


def run_task(D, y, past, obj):
    """Score interne et vrai score de chaque candidat pour une tâche."""
    rows = []
    for c in candidates():
        ins = []
        for z in past:
            tr = [w for w in past if w != z]
            if len(tr) < 2:
                continue
            r = D.score(cand_pred(D, c, z, tr, obj), z, tr, obj)
            if r:
                ins.append(r["score"])
        out = D.score(cand_pred(D, c, y, past, obj), y, past, obj)
        if out is None or not ins:
            continue
        rows.append({"c": [list(c[0]), c[1], c[2]], "interne": float(np.mean(ins)), "interne_min": float(np.min(ins)), **out})
    return rows


def _fc(name):
    fc = AP._fc(name)
    return fc, TVars(fc)


_CTX = {}  # matière en cours, partagée avec les processus forkés sans copie


def _mask_tasks(k):
    """Toutes les tâches d'un domaine (ou pseudo-domaine) ; indépendant des autres domaines."""
    name, fc, V, tests = _CTX["name"], _CTX["fc"], _CTX["V"], _CTX["tests"]
    mname, mask = _CTX["masks"][k]
    D = Domain(fc, V, mask)
    out = []
    for y in tests:
        past = [z for z in fc.years if z < y]
        tr = D.traits(past)
        for obj in OBJ:
            rows = run_task(D, y, past, obj)
            if rows:
                out.append({"matiere": name, "domaine": mname, "annee": y, "objectif": obj, "traits": tr, "candidats": rows,
                            "_preds": preds_of(D, y, past, obj)})
        print(name, mname, y, flush=True)
    return out


BASE = [((), "ancienne")] + [(gs, m) for gs in SETS for m in FIT_MODELS]  # tout candidat en est un mélange de rangs


def preds_of(D, y, past, obj):
    """Rangs (0..1) de chaque candidat de base sur l'année testée puis sur chaque année rejouée,
    avec de quoi les noter : sert à l'autocritique (critique.py) sans tout recalculer."""
    pos = {int(g): k for k, g in enumerate(D.idx)}
    ev = []
    for z, tr in [(y, past)] + [(z, [w for w in past if w != z]) for z in past]:
        if len(tr) < 2 and z != y:
            continue
        P = np.stack([rankdata(D.predict(gs, m, z, tr, obj)) / D.n for gs, m in BASE]).astype(np.float32)
        seen = np.any([D.y(w) for w in tr], 0) if tr else np.zeros(D.n, bool)
        ev.append({"P": P, "y": D.y(z).astype(bool), "q": np.array([pos[q] for q in D.qs(z)], np.int32), "seen": seen})
    return {"sec": np.asarray(D.fc.t.pass_sec)[D.idx], "ev": ev}


def stage_tasks(name, min_hist=3, seed=0):
    fc, V = _fc(name)
    secs = sorted(set(np.asarray(fc.t.pass_sec).tolist()))
    rng = np.random.default_rng(seed)
    masks = [("complet", np.ones(fc.n, bool))]
    for k in range(N_MASKS):
        keep = set(rng.choice(secs, max(2, len(secs) // 2), replace=False).tolist())
        masks.append((f"moitie_{k}", np.isin(np.asarray(fc.t.pass_sec), list(keep))))
    tests = [y for y in fc.years if len([z for z in fc.years if z < y]) >= min_hist]
    # chaque domaine sur son cœur : mêmes calculs, même ordre de sortie
    _CTX.update(name=name, fc=fc, V=V, tests=tests, masks=masks)
    tasks = [t for part in pmap(_mask_tasks, range(len(masks))) for t in part]
    joblib.dump([t.pop("_preds") for t in tasks], CACHE / f"critique_preds_{name}.joblib", compress=3)
    (CACHE / f"transfer_tasks_{name}.json").write_text(json.dumps(tasks), encoding="utf-8")


# ---------------------------------------------------------------------------- le juge
def featurize(task, row, ref_in):
    gs, m, mix = row["c"]
    f = list(task["traits"].values())
    f += [float(task["objectif"] == "prevision")]
    f += [float(g in gs) for g in GROUPS] + [len(gs) / len(GROUPS)]
    f += [float(m == k) for k in ("ancienne", "logistique", "arbres", "melange")] + [float(mix)]
    f += [row["interne"], row["interne"] - ref_in, row["interne_min"]]
    return f


def FEATURE_NAMES(task):
    return (list(task["traits"]) + ["objectif_prevision"] + [f"famille_{g}" for g in GROUPS] + ["nb_familles"] +
            [f"modele_{k}" for k in ("ancienne", "logistique", "arbres", "melange")] + ["mele_a_l_ancienne"] +
            ["score_interne", "gain_interne", "score_interne_pire_annee"])


def _ref(task):
    return next(r for r in task["candidats"] if r["c"][1] == "ancienne")


def dataset(tasks):
    X, yg, ya = [], [], []
    for t in tasks:
        ref = _ref(t)
        for r in t["candidats"]:
            X.append(featurize(t, r, ref["interne"]))
            yg.append(r["score"] - ref["score"])
            ya.append(r["couverture"])
    return np.array(X), np.array(yg), np.array(ya)


def fit_judge(tasks):
    X, yg, ya = dataset(tasks)
    mk = lambda: ExtraTreesRegressor(n_estimators=300, min_samples_leaf=20, max_features=0.5, random_state=0, n_jobs=1)
    return {"gain": mk().fit(X, yg), "couverture": mk().fit(X, ya)}


def decide(J, task, k=3):
    """Choix du juge : les k candidats au plus fort gain prédit, mêlés ; l'ancienne méthode s'il
    n'en voit aucun qui gagne. Renvoie aussi la couverture qu'il s'attend à obtenir."""
    ref = _ref(task)
    X = np.array([featurize(task, r, ref["interne"]) for r in task["candidats"]])
    g = J["gain"].predict(X)
    order = np.argsort(-g)
    top = [i for i in order[:k] if g[i] > 0] or [next(i for i, r in enumerate(task["candidats"]) if r["c"][1] == "ancienne")]
    exp = float(np.mean(J["couverture"].predict(X[top])))
    return top, g, exp


def evaluate_choice(D, task, rows_idx):
    """Vrai score du mélange des candidats retenus (recalculé sur l'année testée)."""
    cs = [task["candidats"][i]["c"] for i in rows_idx]
    y, obj = task["annee"], task["objectif"]
    past = [z for z in D.fc.years if z < y]
    p = sum(rankdata(cand_pred(D, (tuple(gs), m, mix), y, past, obj)) for gs, m, mix in cs)
    return D.score(p, y, past, obj)


def stage_judge(names):
    warnings.filterwarnings("ignore")
    allt = {n: json.loads((CACHE / f"transfer_tasks_{n}.json").read_text(encoding="utf-8")) for n in names}
    auto = {n: json.loads((CACHE / f"autoprog_honest_{n}.json").read_text(encoding="utf-8"))
            for n in names if (CACHE / f"autoprog_honest_{n}.json").exists()}
    rep = {"principe": __doc__.split("\n\n")[0], "matieres": {}}
    for n in names:
        train = [t for m in names if m != n for t in allt[m]]  # ni la matière, ni ses pseudo-domaines
        J = fit_judge(train)
        # meilleur candidat fixe sur les autres matières (référence « règle unique »)
        gains = {}
        for t in train:
            ref = _ref(t)
            for r in t["candidats"]:
                gains.setdefault((t["objectif"], json.dumps(r["c"])), []).append(r["score"] - ref["score"])
        fc, V = _fc(n)
        D = Domain(fc, V, np.ones(fc.n, bool))
        res = {}
        for obj in OBJ:
            fixed = max((k for k in gains if k[0] == obj), key=lambda k: np.mean(gains[k]))
            rows = []
            for t in [t for t in allt[n] if t["domaine"] == "complet" and t["objectif"] == obj]:
                top, g, exp = decide(J, t)
                r = evaluate_choice(D, t, top)
                ref = _ref(t)
                fx = next(x for x in t["candidats"] if json.dumps(x["c"]) == fixed[1])
                ap = next((a for a in auto.get(n, {}).get(obj, {}).get("annees", []) if a["annee"] == t["annee"]), None)
                rows.append({"annee": t["annee"], "choix": [t["candidats"][i]["c"] for i in top],
                             "ancienne": [ref["couverture"], ref["auc"]], "regle_unique": [fx["couverture"], fx["auc"]],
                             "auto_progression": [ap["couverture"], ap["auc"]] if ap else None,
                             "juge": [r["couverture"], r["auc"]], "couverture_annoncee": exp})
                print(n, obj, t["annee"], "ancienne", ref["couverture"], "juge", round(r["couverture"], 3), "annoncé", round(exp, 3), flush=True)
            m = lambda k, i: round(float(np.mean([r[k][i] for r in rows if r[k]])), 3)
            res[obj] = {"annees": rows, **{f"{k}_{s}": m(k, i) for k in ("ancienne", "regle_unique", "auto_progression", "juge")
                                            for i, s in ((0, "couverture"), (1, "auc"))},
                        "ecart_auto_jugement": round(float(np.mean([abs(r["couverture_annoncee"] - r["juge"][0]) for r in rows])), 3),
                        "regle_unique": json.loads(fixed[1])}
        rep["matieres"][n] = res
    # juge final, appris sur tout : sert aux matières nouvelles ; et ce qu'il a appris (pistes)
    every = [t for n in names for t in allt[n]]
    J = fit_judge(every)
    fn = FEATURE_NAMES(every[0])
    imp = sorted(zip(fn, J["gain"].feature_importances_), key=lambda x: -x[1])
    rep["ce_qui_guide_le_choix"] = [[k, round(float(v), 3)] for k, v in imp[:12]]
    rep["domaines_d_entrainement"] = {n: sorted({t["domaine"] for t in allt[n]}) for n in names}
    joblib.dump({"juge": J, "noms": fn, "traits_vus": {n: allt[n][0]["traits"] for n in names},
                 "appris_sur": names}, MODEL)
    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    for n, r in rep["matieres"].items():
        print(n, {o: {k: v for k, v in x.items() if k not in ("annees", "regle_unique")} for o, x in r.items()})
    print("guide :", rep["ce_qui_guide_le_choix"][:8])


# ---------------------------------------------------------------------------- règle universelle
# Résultat du méta-entraînement : le juge appris (ci-dessus) se trompe sur une matière inconnue,
# car deux matières d'entraînement ne suffisent pas à apprendre quand changer de choix. Une seule
# règle, la même pour tous les domaines, fait mieux. Elle est choisie pour marcher partout
# (moyenne + pire domaine), jamais pour une matière précise.
RULE_OUT = AP.ROOT / "output" / "meta" / "regle.json"
DEFAULT_RULE = {"prevision": [["lexique_du_professeur"], "arbres", False],
                "nouveaute": [["lexique_du_professeur"], "melange", True]}
MARGE = 0.275  # élargit la fourchette annoncée ; recalibrée sur 643 choix faits à l'aveugle (20 matières)


# Prudence du choix : « moyenne + pire domaine » devient plus frileux à chaque domaine ajouté (le
# minimum de 120 domaines est presque toujours mauvais). Le degré de prudence est donc lui aussi
# appris : celui dont la règle marche le mieux sur des matières laissées de côté (ordre = du plus
# prudent au moins prudent ; à égalité, le plus prudent).
AGGS = {"moyenne+pire": lambda g: g.mean() + g.min(),
        "moyenne+q10": lambda g: g.mean() + np.quantile(g, 0.10),
        "moyenne+q25": lambda g: g.mean() + np.quantile(g, 0.25),
        "moyenne": lambda g: g.mean()}


def _gains(tasks, obj):
    """Candidat -> domaine -> gains de score sur l'ancienne méthode."""
    rows = {}
    for t in tasks:
        if t["objectif"] != obj:
            continue
        ref = _ref(t)
        dom = (t["matiere"], t["domaine"] == "complet")
        for r in t["candidats"]:
            rows.setdefault(json.dumps(r["c"]), {}).setdefault(dom, []).append(r["score"] - ref["score"])
    return rows


def _select(tasks, obj, agg):
    rows = _gains(tasks, obj)
    doms = set.intersection(*[set(d) for d in rows.values()])
    crit = {k: AGGS[agg](np.array([np.mean(d[x]) for x in doms])) for k, d in rows.items()}
    return json.loads(max(crit, key=crit.get))


def _held_out(tasks, obj, agg):
    """Gain de score de la règle sur chaque matière, choisie sans elle (domaine complet)."""
    subs = sorted({t["matiere"] for t in tasks})
    out = []
    for n in subs:
        c = _select([t for t in tasks if t["matiere"] != n], obj, agg)
        T = [t for t in tasks if t["matiere"] == n and t["domaine"] == "complet" and t["objectif"] == obj]
        if T:
            out.append(np.mean([next(x for x in t["candidats"] if x["c"] == c)["score"] - _ref(t)["score"] for t in T]))
    return np.array(out)


def choose_agg(tasks, obj):
    if len({t["matiere"] for t in tasks}) < 4:
        return "moyenne+pire"
    sc = {a: round(float(_held_out(tasks, obj, a).mean()), 4) for a in AGGS}
    return max(AGGS, key=lambda a: sc[a])  # max garde le premier à égalité : le plus prudent


def select_rule(tasks, obj):
    """La règle, avec le degré de prudence qui généralise le mieux d'une matière à l'autre."""
    return _select(tasks, obj, choose_agg(tasks, obj))


def fourchette(interne, interne_min, marge=MARGE):
    return [max(0.0, interne_min - marge), min(1.0, 2 * interne - interne_min + marge)]


def stage_rule(names):
    """Preuve « matière inconnue » de la règle : choisie sans la matière, testée sur elle."""
    allt = {n: json.loads((CACHE / f"transfer_tasks_{n}.json").read_text(encoding="utf-8")) for n in names}
    every = [t for n in names for t in allt[n]]
    final = {o: select_rule(every, o) for o in OBJ}
    rep = {"principe": "Une seule règle pour tous les domaines, choisie pour marcher partout ; "
                       "chaque matière est testée avec la règle choisie sans elle.",
           "regle": final, "appris_sur": names, "matieres": {}}
    get = lambda t, c: next(x for x in t["candidats"] if x["c"] == c)
    for n in names:
        res = {}
        for obj in OBJ:
            c = select_rule([t for m in names if m != n for t in allt[m]], obj)
            T = [t for t in allt[n] if t["domaine"] == "complet" and t["objectif"] == obj]
            P = [t for t in allt[n] if t["domaine"] != "complet" and t["objectif"] == obj]
            mean = lambda ts, k, cc: round(float(np.mean([get(t, cc)[k] for t in ts])), 3)
            anc = [[], "ancienne", False]
            res[obj] = {"regle_sans_cette_matiere": c,
                        "avant_couverture": mean(T, "couverture", anc), "couverture": mean(T, "couverture", c),
                        "avant_auc": mean(T, "auc", anc), "auc": mean(T, "auc", c),
                        "regle_finale_couverture": mean(T, "couverture", final[obj]),
                        "pseudo_domaines": {"avant": mean(P, "couverture", anc), "apres": mean(P, "couverture", final[obj]),
                                            "n": len(P)}}
        rep["matieres"][n] = res
    hit, wid = [], []
    for t in every:
        x = get(t, final[t["objectif"]])
        lo, hi = fourchette(x["interne"], x["interne_min"])
        hit.append(lo <= x["couverture"] <= hi)
        wid.append(hi - lo)
    rep["auto_jugement"] = {"principe": "Avant de répondre, le moteur rejoue la règle sur ses propres années passées "
                                        "et annonce une fourchette de couverture.",
                            "fourchette_juste": round(float(np.mean(hit)), 3), "largeur_moyenne": round(float(np.mean(wid)), 3),
                            "taches": len(every)}
    RULE_OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print(json.dumps(rep, ensure_ascii=False, indent=1, default=float))


# ---------------------------------------------------------------------------- apprendre à apprendre
# Avec beaucoup de matières, on ne cherche plus seulement « le » bon réglage : on apprend une
# manière de se régler. Le méta-entraînement retient une courte liste de réglages robustes (ordre =
# a priori) et un seuil ; sur un domaine neuf, le moteur choisit seul dans cette liste en rejouant
# ses propres années passées, et ne quitte le premier réglage que si la preuve interne dépasse le
# seuil. Liste et seuil sont choisis en laissant de côté chaque matière d'entraînement tour à tour.
LEARN_OUT = AP.ROOT / "output" / "meta" / "apprendre.json"
KS = (1, 2, 3, 4, 6, 8)
DELTAS = (0.0, 0.02, 0.05, 0.1, 0.2)


def _dom(t):
    return (t["matiere"], t["domaine"] == "complet")


class _M:
    """Tâches d'un objectif en matrices : gain sur l'ancienne (G) et score interne (I) par candidat."""
    def __init__(self, tasks, keys=None):
        self.keys = keys or sorted({json.dumps(r["c"]) for t in tasks for r in t["candidats"]})
        ix = {k: j for j, k in enumerate(self.keys)}
        n, c = len(tasks), len(self.keys)
        self.G, self.I = np.zeros((n, c)), np.full((n, c), -np.inf)
        self.C, self.A, self.Im = np.zeros((n, c)), np.zeros((n, c)), np.zeros((n, c))
        for i, t in enumerate(tasks):
            ref = _ref(t)
            self.C[i], self.A[i] = ref["couverture"], ref["auc"]
            for r in t["candidats"]:
                j = ix[json.dumps(r["c"])]
                self.G[i, j], self.I[i, j] = r["score"] - ref["score"], r["interne"]
                self.C[i, j], self.A[i, j], self.Im[i, j] = r["couverture"], r["auc"], r["interne_min"]
        doms = sorted({_dom(t) for t in tasks})
        self.d = np.array([doms.index(_dom(t)) for t in tasks])
        self.nd = len(doms)

    def robust(self, g):
        """Moyenne des domaines + pire domaine (même critère que la règle universelle) ; g : (n,) ou (n, k)."""
        g = g.reshape(len(self.d), -1)
        m = np.stack([g[self.d == k].mean(0) for k in range(self.nd)])
        return m.mean(0) + m.min(0)

    def pick(self, short, delta):
        """Indice choisi par tâche : le meilleur interne de la liste s'il bat le premier de plus du seuil."""
        sub = self.I[:, short]
        b = np.array(short)[np.argmax(sub, 1)]
        r = np.arange(len(self.d))
        return np.where(self.I[r, b] - self.I[:, short[0]] > delta, b, short[0])

    def greedy(self, first, K, delta):
        """Liste gloutonne : chaque ajout est le réglage qui améliore le plus la politique."""
        short, r = [first], np.arange(len(self.d))
        while len(short) < K:
            sub = self.I[:, short]
            bI = sub.max(1)
            b = np.array(short)[np.argmax(sub, 1)]
            nb = np.where(self.I > bI[:, None], np.arange(self.I.shape[1])[None, :], b[:, None])
            ch = np.where(self.I[r[:, None], nb] - self.I[:, [short[0]]] > delta, nb, short[0])
            val = self.robust(self.G[r[:, None], ch])
            val[short] = -np.inf
            short.append(int(np.argmax(val)))
        return short


def _first(M):
    return int(np.argmax(M.robust(M.G)))  # = la règle universelle


def learn_policy(tasks, obj):
    """(K, seuil) choisis en laissant de côté chaque matière d'entraînement ; puis liste finale."""
    T = [t for t in tasks if t["objectif"] == obj]
    keys = sorted({json.dumps(r["c"]) for t in T for r in t["candidats"]})
    names = sorted({t["matiere"] for t in T})
    Mall = _M(T, keys)
    gains = {(K, d): np.zeros(len(T)) for K in KS for d in DELTAS}
    for m in names:
        tr = np.array([t["matiere"] != m for t in T])
        Mtr = _M([t for t, k in zip(T, tr) if k], keys)
        Mte = _M([t for t, k in zip(T, tr) if not k], keys)
        f = _first(Mtr)
        for d in DELTAS:
            sh = Mtr.greedy(f, max(KS), d)
            for K in KS:
                ch = Mte.pick(sh[:K], d)
                gains[(K, d)][~tr] = Mte.G[np.arange(len(ch)), ch]
    grid = {k: float(Mall.robust(v)[0]) for k, v in gains.items()}
    K, d = max(grid, key=lambda k: (round(grid[k], 4), -k[0], k[1]))
    sh = Mall.greedy(_first(Mall), K, d)
    return {"K": K, "seuil": d, "liste": [json.loads(keys[j]) for j in sh],
            "grille": {f"K={k[0]} seuil={k[1]}": round(v, 4) for k, v in grid.items()}}


def choose(cands, pol):
    """Production : dans la liste apprise, le moteur choisit seul d'après ses propres années passées.
    cands : {json(c): score interne}."""
    sh = [json.dumps(c) for c in pol["liste"] if json.dumps(c) in cands]
    best = max(sh, key=cands.get)
    return json.loads(best if cands[best] - cands[sh[0]] > pol["seuil"] else sh[0])


def stage_learn(names):
    """Compare, matière par matière (chaque matière absente de son propre entraînement) :
    ancienne méthode, règle universelle, juge appris, et « se régler soi-même »."""
    warnings.filterwarnings("ignore")
    allt = {n: json.loads((CACHE / f"transfer_tasks_{n}.json").read_text(encoding="utf-8")) for n in names}
    for n in names:
        for t in allt[n]:
            t["matiere"] = n
    every = [t for n in names for t in allt[n]]
    meth = ("ancienne", "regle", "juge", "se_regler")
    rep = {"principe": "Chaque matière est traitée comme un domaine inconnu : tout ce qui est appris "
                       "(règle, juge, liste de réglages, seuil) l'est sans elle.", "matieres": {}}
    blind = {m: [] for m in meth}  # (interne, interne_min, vraie couverture) des choix faits à l'aveugle
    for n in names:
        tr = [t for t in every if t["matiere"] != n]
        J = fit_judge(tr)
        res = {}
        for obj in OBJ:
            Ttr = [t for t in tr if t["objectif"] == obj]
            keys = sorted({json.dumps(r["c"]) for t in Ttr for r in t["candidats"]})
            Mtr = _M(Ttr, keys)
            pol = learn_policy(tr, obj)
            sh = [keys.index(json.dumps(c)) for c in pol["liste"]]
            te = [t for t in allt[n] if t["objectif"] == obj]
            Mte = _M(te, keys)
            jsel = []
            for t in te:
                ref = _ref(t)
                X = np.array([featurize(t, r, ref["interne"]) for r in t["candidats"]])
                g = J["gain"].predict(X)
                c = t["candidats"][int(np.argmax(g))]["c"] if g.max() > 0 else ref["c"]
                jsel.append(keys.index(json.dumps(c)))
            ri = np.arange(len(te))
            sel = {"ancienne": np.full(len(te), keys.index(json.dumps(_ref(te[0])["c"]))),
                   "regle": np.full(len(te), keys.index(json.dumps(select_rule(Ttr, obj)))), "juge": np.array(jsel),
                   "se_regler": Mte.pick(sh, pol["seuil"])}
            full = np.array([t["domaine"] == "complet" for t in te])
            for m, s_ in sel.items():
                blind[m] += list(zip(Mte.I[ri, s_], Mte.Im[ri, s_], Mte.C[ri, s_]))
            f = lambda v: round(float(np.mean(v)), 3) if len(v) else None
            res[obj] = {m: {"couverture": f(Mte.C[ri, s][full]), "auc": f(Mte.A[ri, s][full]),
                            "gain": f(Mte.G[ri, s][full]), "pseudo_gain": f(Mte.G[ri, s][~full])}
                        for m, s in sel.items()}
            res[obj]["politique"] = {"K": pol["K"], "seuil": pol["seuil"], "liste": pol["liste"]}
            print(n, obj, {m: (res[obj][m]["couverture"], res[obj][m]["gain"], res[obj][m]["pseudo_gain"]) for m in meth}, flush=True)
        rep["matieres"][n] = res
    summ = {}
    for obj in OBJ:
        summ[obj] = {}
        for m in meth:
            v = lambda k: [rep["matieres"][n][obj][m][k] for n in names]
            g = v("gain")
            summ[obj][m] = {"gain_moyen": round(float(np.mean(g)), 4), "pire_matiere": round(float(min(g)), 4),
                            "matieres_gagnees": int(sum(x > 0.005 for x in g)),
                            "matieres_perdues": int(sum(x < -0.005 for x in g)),
                            "pseudo_gain_moyen": round(float(np.mean(v("pseudo_gain"))), 4),
                            "couverture_moyenne": round(float(np.mean(v("couverture"))), 3),
                            "auc_moyenne": round(float(np.mean(v("auc"))), 3)}
    rep["synthese"] = summ
    rep["politique_finale"] = {obj: learn_policy(every, obj) for obj in OBJ}
    # adoption : la stratégie de production est celle qui gagne en moyenne ET dans la pire matière
    # (le juge, trop dépendant des matières vues, n'est retenu que comme témoin)
    rep["adoptee"] = {}
    for obj in OBJ:
        agg = choose_agg(every, obj)  # même prudence que celle apprise pour la règle
        gm = lambda m: np.array([rep["matieres"][n][obj][m]["gain"] for n in names])
        crit = {m: float(AGGS[agg](gm(m))) for m in ("ancienne", "regle", "se_regler")}
        win = max(crit, key=lambda m: (round(crit[m], 4), m == "regle"))
        pf = rep["politique_finale"][obj]
        liste = {"ancienne": [[[], "ancienne", False]], "regle": [select_rule(every, obj)], "se_regler": pf["liste"]}[win]
        rep["adoptee"][obj] = {"strategie": win, "liste": liste, "seuil": pf["seuil"] if win == "se_regler" else 0.0,
                               "prudence": agg, "critere": {m: round(v, 4) for m, v in crit.items()}}
    # auto-jugement : la plus petite marge dont la fourchette contient le vrai résultat ≥ 85 % du temps
    rep["auto_jugement"] = {}
    for m in meth:
        b = np.array(blind[m])
        cal = {}
        for mg in np.arange(0.0, 0.41, 0.025):
            lo, hi = np.maximum(0, b[:, 1] - mg), np.minimum(1, 2 * b[:, 0] - b[:, 1] + mg)
            cal[round(float(mg), 3)] = (float(np.mean((lo <= b[:, 2]) & (b[:, 2] <= hi))), float(np.mean(hi - lo)))
        mg = min([k for k, v in cal.items() if v[0] >= 0.85] or [max(cal)])
        rep["auto_jugement"][m] = {"marge": mg, "fourchette_juste": round(cal[mg][0], 3),
                                   "largeur_moyenne": round(cal[mg][1], 3), "taches": len(b)}
    for obj in OBJ:
        rep["adoptee"][obj]["marge"] = rep["auto_jugement"][rep["adoptee"][obj]["strategie"]]["marge"]
    rep["appris_sur"] = names
    LEARN_OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print(json.dumps({"synthese": summ, "adoptee": rep["adoptee"], "auto_jugement": rep["auto_jugement"], "politique_finale": {o: {k: v for k, v in p.items() if k != "grille"}
                                                              for o, p in rep["politique_finale"].items()}},
                     ensure_ascii=False, indent=1))


def _replay(D, c, ys, obj):
    ins = []
    for z in ys:  # auto-jugement : le réglage rejoué sur ses propres années (même calcul qu'à la calibration)
        tr = [w for w in ys if w != z]
        if len(tr) >= 2:
            r = D.score(cand_pred(D, c, z, tr, obj), z, tr, obj)
            if r:
                ins.append(r["score"])
    return ins


def blend_pred(D, w, lam, target, train, obj):
    """Mélange de rangs des réglages de base trouvé par l'autocritique (meta/critique.py)."""
    from .critique import _diversify
    p = sum(wj * rankdata(D.predict(gs, m, target, train, obj)) / D.n for wj, (gs, m) in zip(w, BASE) if wj > 0)
    return _diversify(np.asarray(p, float), np.asarray(D.fc.t.pass_sec)[D.idx], lam) if lam else p


def _critique_adoptee():
    f = AP.ROOT / "output" / "meta" / "critique.json"
    try:
        return {o: a for o, a in json.loads(f.read_text(encoding="utf-8"))["adoptee"].items() if a["strategie"] == "critique"}
    except (OSError, KeyError, ValueError):
        return {}


def apply(fc, log=print) -> dict:
    """Production, aucun choix propre à la matière : le moteur rejoue sur ses années passées les
    réglages de la liste apprise (méta-entraînement multi-matières) et choisit seul ; sans liste,
    la règle universelle."""
    pol = json.loads(LEARN_OUT.read_text(encoding="utf-8")).get("adoptee", {}) if LEARN_OUT.exists() else {}
    rule = json.loads(RULE_OUT.read_text(encoding="utf-8"))["regle"] if RULE_OUT.exists() else DEFAULT_RULE
    D = Domain(fc, TVars(fc), np.ones(fc.n, bool))
    nxt, ys = fc.years[-1] + 1, list(fc.years)
    out, crit = {}, _critique_adoptee()
    for obj in OBJ:
        if obj in crit:  # mélange que le moteur a trouvé en se critiquant, gagnant matière exclue
            a = crit[obj]
            w, lam = np.asarray(a["poids"]), a.get("diversification", 0.0)
            ins = []
            for z in ys:
                tr = [v for v in ys if v != z]
                if len(tr) >= 2:
                    r = D.score(blend_pred(D, w, lam, z, tr, obj), z, tr, obj)
                    if r:
                        ins.append(r["score"])
            f = fourchette(float(np.mean(ins)), float(np.min(ins)), pol.get(obj, {}).get("marge", MARGE)) if ins else None
            out[obj] = {"autocritique": a["melange"], "diversification": lam, "score_rejoue": [round(v, 3) for v in ins],
                        "fourchette": f, "p": blend_pred(D, w, lam, nxt, ys, obj)}
            log(f"  mélange trouvé par autocritique ({obj}) : {a['melange']}, fourchette {f}")
            continue
        liste = pol[obj]["liste"] if obj in pol else [rule[obj]]
        rej = {json.dumps(c): _replay(D, (tuple(c[0]), c[1], c[2]), ys, obj) for c in liste}
        rej = {k: v for k, v in rej.items() if v}
        if rej:
            c = choose({k: float(np.mean(v)) for k, v in rej.items()},
                       pol.get(obj, {"liste": liste, "seuil": 0.0})) if obj in pol else liste[0]
            ins = rej[json.dumps(c)]
        else:
            c, ins = liste[0], []
        gs, m, mix = c
        f = fourchette(float(np.mean(ins)), float(np.min(ins)), pol.get(obj, {}).get("marge", MARGE)) if ins else None
        out[obj] = {"familles": gs, "modele": m, "mele_a_l_ancienne": mix,
                    "essayes": {k: round(float(np.mean(v)), 3) for k, v in rej.items()},
                    "score_rejoue": [round(v, 3) for v in ins], "fourchette": f,
                    "p": cand_pred(D, (tuple(gs), m, mix), nxt, ys, obj)}
        log(f"  réglage choisi seul ({obj}, parmi {len(liste)}) : {gs} / {m}{' + ancienne' if mix else ''}, fourchette {f}")
    return out


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    st, names = sys.argv[1], sys.argv[2:] or ["droit", "nsi", "eco"]
    if st == "tasks":
        for n in names:
            stage_tasks(n)
    elif st == "judge":
        stage_judge(names)
    elif st == "learn":
        stage_learn(names)
    else:
        stage_rule(names)


# ===== examgen/prof/__init__.py =====


# ===== examgen/prof/__main__.py =====
"""python -m examgen.prof {profil,plan,probable,check} --sujets DIR --cours DIR --out DIR

Tout d'un coup, pour n'importe quelle matière (anciens sujets + cours suffisent) :
  python -m examgen.prof tout --nom eco --sujets data/sources/droit_stmg --cours data/eco/cours
profil -> prévision (preuve comme en vrai) -> programme sur tout le cours -> plans -> rédaction
(API ou prompts) avec boucle vérifier-corriger -> contrôle -> livrable."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib

from . import check, plan, redige
from .profile import Teacher


def load(a) -> Teacher:
    cache = Path(a.out) / "teacher.joblib"
    if cache.exists() and not a.refit:
        return joblib.load(cache)
    t = Teacher(Path(a.sujets), Path(a.cours)).run()
    t.save(Path(a.out))
    joblib.dump(t, cache)
    return t


def main():
    ap = argparse.ArgumentParser(prog="examgen.prof")
    ap.add_argument("cmd", choices=["profil", "plan", "probable", "check", "redige", "tout"])
    ap.add_argument("--nom", default=None, help="nom de la matière (registre data/domaines.json)")
    ap.add_argument("--sujets", default="data/sources/droit_stmg")
    ap.add_argument("--cours", default="data/droit/cours")
    ap.add_argument("--out", default="output/droit")
    ap.add_argument("--refit", action="store_true")
    ap.add_argument("--plans", default="plans.json")
    a = ap.parse_args()
    if a.cmd == "tout":
        return tout(a)
    Path(a.out).mkdir(parents=True, exist_ok=True)
    if a.cmd == "profil":
        a.refit = True
        load(a)
    elif a.cmd == "plan":
        ps = plan.write(load(a), Path(a.out))
        print(f"{len(ps)} plans -> {a.out}/plans/")
    elif a.cmd == "probable":
        prev = json.loads((Path(a.out) / "previsions.json").read_text(encoding="utf-8"))
        ps = plan.Planner(load(a)).probables(prev)
        (Path(a.out) / "plans_probables.json").write_text(json.dumps(ps, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
        print(f"{len(ps)} plans probables -> {a.out}/plans_probables.json")
    elif a.cmd == "redige":
        t = load(a)
        ps = json.loads((Path(a.out) / a.plans).read_text(encoding="utf-8"))
        prob = a.plans != "plans.json"
        print(redige.run(t, ps, Path(a.out), a.nom or Path(a.out).name, gen_sub="generated_probables" if prob else "generated"))
    else:
        t = load(a)
        ps = json.loads((Path(a.out) / a.plans).read_text(encoding="utf-8"))
        prob = a.plans != "plans.json"
        s = check.run(t, ps, Path(a.out) / ("generated_probables" if prob else "generated"),
                      Path(a.out) / ("validation_probables.json" if prob else "validation.json"))
        t.save(Path(a.out))
        print(json.dumps(s, ensure_ascii=False))


def tout(a):
    import subprocess
    import sys

    from ..meta import domain
    from . import forecast
    nom = a.nom or Path(a.cours).parent.name
    if a.sujets and a.cours and nom not in ("droit", "nsi"):
        domain.register(nom, a.sujets, a.cours)
    s, c = domain.DOMAINS[nom]
    a.sujets, a.cours, a.out = s, c, str(domain.out_dir(nom))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    print(f"[1/6] profil du professeur ({nom})")
    t = load(a)
    print("[2/6] plans d'exercices sur tout le cours")
    ps = plan.write(t, out)
    print("[3/6] prévision, preuve comme en vrai, programme")
    rep = forecast.run(nom)
    pp = plan.Planner(t).probables(rep)
    (out / "plans_probables.json").write_text(json.dumps(pp, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print("[4/6] rédaction (boucle vérifier-corriger)")
    for plans, sub in ((pp, "generated_probables"), (ps, "generated")):
        print("   ", redige.run(t, plans, out, nom, gen_sub=sub))
    print("[5/6] contrôle")
    for plans, sub, v in ((ps, "generated", "validation.json"), (pp, "generated_probables", "validation_probables.json")):
        if any((out / sub).glob("*.json")):
            print("   ", sub, json.dumps(check.run(t, plans, out / sub, out / v), ensure_ascii=False))
    t.save(out)
    print("[6/6] livrable")
    subprocess.run([sys.executable, str(Path(__file__).resolve().parents[2] / "scripts" / "build_livrable.py")], check=False)
    nv = rep["preuve_sur_les_nouveautes"]
    print(f"fini : {len(rep['programme'])} chapitres au programme ; nouveautés couvertes {nv.get('nouvelles_couvertes_par_le_quart_retenu')} "
          f"(hasard {nv.get('hasard')})")


if __name__ == "__main__":
    main()


# ===== examgen/prof/check.py =====
"""Validateur : les modèles appris jouent le rôle de correcteur (la « récompense » de la boucle
écrire → vérifier → réviser). Chaque question générée est notée sur :

  facette_ok    la manière de demander reconnue (top 2 du modèle de consignes) est celle du plan ;
  section_ok    l'alignement appris place la section visée (ou sa partenaire) dans le top 3 ;
  articles_ok   chaque référence citée (identifiant dont la forme est apprise sur le cours, ex.
                « article 1240 ») existe dans le cours ou dans les documents réels ;
  annexes_ok    une annexe qui ressemble à une source (article, arrêt) la recopie fidèlement ;
                une annexe inventée n'est admise que dans un type de support où le professeur
                invente aussi (extraits de contrat, règlement…), ce que mesure le taux de reprise
                des sources réelles par type de support, appris sur les anciens sujets ;
  nouveaute_ok  la situation n'est pas une ancienne situation (cosinus sous le seuil appris par
                meta/controle.py, 0,85 tant qu'aucun meilleur n'a été trouvé) et l'énoncé n'est
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
from .profile import Teacher


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
        # seuils de nouveauté calibrés sur le vrai professeur (meta/controle.py), 0,85 à défaut
        from ..meta.controle import seuils
        self.tau = seuils(t)
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
        self.known_ids = set().union(*t.sec_ids) | set().union(*(t.ref_ids(s) for s in self.src)) | \
            set().union(*(t.ref_ids(q.answer) for q in t.qs if q.answer))
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
        hid = (plan.get("intention_cachee") or {}).get("evaluer_sans_le_dire") or []
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
            cited = {re.sub(r"[.\s]", "", str(c)).upper() for c in q.get("articles_cites", [])} | self.t.ref_ids(ans)
            cited = {re.sub(r"^ARTICLES?", "", c) for c in cited}
            unknown = sorted(c for c in cited if c and c not in self.known_ids and c not in self.t.ref_ids(anx_text))
            r["articles_inconnus"] = unknown
            r["articles_ok"] = not unknown
            sims = (t.vec.transform([_mask(stem)]) @ self.past.T).toarray().ravel() if stem else np.zeros(1)
            nov = float(sims.max())
            r["nouveaute_sim_max"] = round(nov, 3)
            r["formule_rituelle"] = bool(nov >= self.tau["enonce"] and (self.ritual[int(sims.argmax())] or bool(self._head(stem) & self.rit_heads)))
            ss = float((t.vec.transform([_mask(situation)]) @ self.past_sit.T).max()) if self.past_sit is not None and len(situation) > 80 else 0.0
            r["situation_sim_max"] = round(ss, 3)
            r["nouveaute_ok"] = (nov < self.tau["enonce"] or r["formule_rituelle"]) and ss < self.tau["situation"]
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
            if hid:  # intention cachée : notion évaluée sans être dite
                said = set(re.findall(r"[a-z]{4,}", _n(stem)))
                req = set(re.findall(r"[a-z]{4,}", _n(ans)))
                r["intention_dite_dans_l_enonce"] = sorted(w for w in hid if w in said)
                r["intention_exigee_dans_le_corrige"] = sorted(w for w in hid if w in req)
                if r["intention_dite_dans_l_enonce"]:
                    fb.append(f"l'énoncé nomme {r['intention_dite_dans_l_enonce']} alors que le professeur l'évalue sans le dire")
            if fb:
                res["revision"].append(f"Question {q.get('slot')} : " + " ; ".join(fb))
        if hid:
            got = set().union(*[set(x.get("intention_exigee_dans_le_corrige", [])) for x in res["questions"]])
            res["intention_cachee_couverte"] = round(len(got & set(hid)) / len(hid), 2)
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


# ===== examgen/prof/docs.py =====
"""Lecture et découpage génériques : sujets, corrigés, cours.

Rien ici ne dépend de la matière : on lit des PDF / Markdown / texte, on repère la numérotation
des questions, les titres de parties et d'annexes, et les titres du cours. Les seules hypothèses
sont typographiques (une question commence par « 1. », « 2) », « Question 3 », un cours a des titres).
"""
from __future__ import annotations

import os
import re
import subprocess
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

CORR = re.compile(r"(corrig|correction|bareme|barème|solution)", re.I)
YEAR = re.compile(r"(?<!\d)(19[89]\d|20[0-4]\d)(?!\d)")


TEXT_CACHE = Path(__file__).resolve().parents[2] / "data" / "cache" / "textes"


def read_text(path: Path) -> str:
    """Texte d'un fichier. Un PDF déjà lu (même contenu, où qu'il soit) n'est pas relu."""
    path = Path(path)
    if path.suffix.lower() != ".pdf":
        return path.read_text(encoding="utf-8", errors="ignore")
    import hashlib
    f = TEXT_CACHE / (hashlib.sha1(path.read_bytes()).hexdigest() + ".txt")
    try:
        return f.read_text(encoding="utf-8")
    except OSError:
        pass
    txt = subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True).stdout
    try:
        TEXT_CACHE.mkdir(parents=True, exist_ok=True)
        tmp = f.with_suffix(f".{os.getpid()}.tmp")
        tmp.write_text(txt, encoding="utf-8")
        tmp.replace(f)
    except OSError:
        pass
    return txt


def read_many(paths) -> dict:
    """Lit plusieurs fichiers en parallèle (pdftotext tourne hors de Python)."""
    from concurrent.futures import ThreadPoolExecutor
    paths = list(dict.fromkeys(Path(p) for p in paths))
    with ThreadPoolExecutor(max(1, min(8, len(paths)))) as ex:
        return dict(zip(paths, ex.map(read_text, paths)))


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c)).replace("’", "'")


def strip_noise(text: str) -> list[str]:
    """Retire en-têtes / pieds de page : lignes courtes répétées sur plusieurs pages, numéros de page."""
    lines = [l.rstrip() for l in text.replace("\f", "\n").splitlines()]
    # numéro de question seul sur sa ligne (« 1 » puis l'énoncé plus bas) : on recolle
    merged, i = [], 0
    bare = lambda l: re.fullmatch(r"\s*(\d{1,2})\s*[.)]?\s*", l)
    while i < len(lines):
        # colonne de numéros (« 1. 2. 3. ») puis colonne d'énoncés : on apparie dans l'ordre
        run = []
        while i + len(run) < len(lines) and bare(lines[i + len(run)]):
            run.append(bare(lines[i + len(run)]).group(1))
        if len(run) >= 2 and [int(x) for x in run] == list(range(int(run[0]), int(run[0]) + len(run))):
            j, groups, buf = i + len(run), [], []
            while j < len(lines) and len(groups) < len(run):
                t = lines[j].strip()
                if t:
                    buf.append(t)
                    if re.search(r"[.?!]\s*[»\"]?\s*$", t):
                        groups.append(" ".join(buf)); buf = []
                j += 1
            if len(groups) == len(run):
                merged += [f"{n}. {g}" for n, g in zip(run, groups)] + [""]
                i = j
                continue
        m = re.fullmatch(r"\s*(\d{1,2})\s*[.)]?\s*", lines[i])
        if m:
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r"\s*[A-ZÉÈÀÂÎ][a-zéèêàâîôûç]", lines[j]) and j - i <= 3:
                merged.append(f"{m.group(1)}. {lines[j].strip()}")
                i = j + 1
                continue
        merged.append(lines[i])
        i += 1
    lines = merged
    cnt = Counter(l.strip() for l in lines if l.strip())
    out = []
    for l in lines:
        s = l.strip()
        if re.fullmatch(r"(page\s*)?\d+\s*(/|sur)\s*\d+", s, re.I) or re.fullmatch(r"\d{1,3}", s):
            continue
        if s and cnt[s] >= 3 and len(s) < 40:
            continue
        out.append(l)
    return out


# ------------------------------------------------------------------------------- sujets
@dataclass
class Question:
    exam: str
    part: str
    num: int
    stem: str
    preamble: str = ""          # texte d'amorce placé juste avant la question
    situation: str = ""         # mise en situation de la partie
    annexes: list = field(default_factory=list)   # [(titre, texte)]
    position: int = 0           # rang dans la partie (0..n-1)
    n_in_part: int = 0
    points: float | None = None
    answer: str = ""            # texte du corrigé
    year: int | None = None


QNUM = re.compile(r"^\s*(?:Question\s+)?(\d{1,2})\s*(?:[.)°]|-(?!\d)|–)\s*(?=\S)", re.I)
PART = re.compile(r"^\s*(PARTIE|Partie|EXERCICE|Exercice|DOSSIER|Dossier|SUJET|Sujet)\b[^.?]{0,60}$")
ANNEX = re.compile(r"^\s*(ANNEXE|Annexe|DOCUMENT|Document)\s*[A-Z0-9]{0,3}\b")
POINTS = re.compile(r"\(?\s*(\d{1,2}(?:[,.]\d+)?)\s*points?\s*\)?", re.I)


def _blocks(lines: list[str]):
    """Découpe en blocs typés : ('part', titre) | ('annex', titre) | ('q', num, ligne) | ('txt', ligne)."""
    for l in lines:
        s = l.strip()
        if not s:
            yield ("blank",)
        elif PART.match(s) and len(s) < 70:
            yield ("part", s)
        elif ANNEX.match(s) and len(s) < 160:
            yield ("annex", s)
        elif QNUM.match(s) and len(s) > 12:
            yield ("q", int(QNUM.match(s).group(1)), QNUM.sub("", s))
        else:
            yield ("txt", s)


BARE_Q = re.compile(r"^\s*(?:QUESTION|Question)\s*(\d{1,2})?\s*[:.)–-]?\s*(.*)$")


def _join_bare_questions(lines: list[str]) -> list[str]:
    """« QUESTION 2 : » seul sur sa ligne (énoncé dessous) ou « QUESTION : énoncé » sans numéro :
    on réécrit en « n. énoncé » pour que la numérotation commune s'applique."""
    out, auto, i = [], 0, 0
    while i < len(lines):
        m = BARE_Q.match(lines[i])
        if m and not POINTS.fullmatch(m.group(2).strip() or "x") and not re.search(r"\.{4,}", lines[i]):
            num = int(m.group(1)) if m.group(1) else None
            rest = m.group(2).strip()
            j = i + 1
            while not rest and j < len(lines) and j - i <= 3:
                rest = lines[j].strip()
                j += 1
            if rest and len(rest) > 8:
                auto = num if num else auto + 1
                out.append(f"{auto}. {rest}")
                i = j if not m.group(2).strip() else i + 1
                continue
        out.append(lines[i])
        i += 1
    return out


def parse_exam(text: str, exam_id: str) -> list[Question]:
    lines = _join_bare_questions(strip_noise(text))
    parts: list[dict] = []
    cur = {"title": "Sujet", "pre": [], "qs": [], "annexes": [], "mode": "pre"}
    parts.append(cur)
    last_q, major = None, ""
    for b in _blocks(lines):
        if b[0] == "part":
            title = b[1]
            # « SUJET 2 » sous une « PARTIE … » : sous-partie au choix, on garde la partie englobante
            if re.match(r"(?i)sujet\b", title) and major:
                title = f"{major} / {title}"
            elif not re.match(r"(?i)sujet\b", title):
                major = title
            cur = {"title": title, "pre": [], "qs": [], "annexes": [], "mode": "pre"}
            parts.append(cur)
            last_q = None
        elif b[0] == "annex":
            cur["annexes"].append([b[1], []])
            cur["mode"] = "annex"
        elif b[0] == "q" and cur["mode"] != "annex":
            expected = (last_q["num"] + 1) if last_q else 1
            if b[1] == expected or (last_q is None and b[1] <= 2):
                last_q = {"num": b[1], "lines": [b[2]], "pre": [], "open": True}
                cur["qs"].append(last_q)
                cur["mode"] = "q"
                continue
            _add_text(cur, last_q, b[2])
        elif b[0] == "txt":
            _add_text(cur, last_q, b[1])
        elif b[0] == "blank" and last_q is not None:
            last_q["open"] = False
    out = []
    year = YEAR.search(exam_id)
    for p in parts:
        if len(p["qs"]) == 1 and p["title"] != "Sujet":
            pass  # partie à une seule consigne (dissertation, exercice, étude de documents)
        elif len(p["qs"]) == 0 and p["title"] != "Sujet":
            body = "\n".join(p["pre"]).strip()
            if len(body) < 200 and not (len(body) >= 25 and "?" in body):
                continue
            # partie sans question numérotée : la partie entière est l'unité interrogée
            p["qs"] = [{"num": 1, "lines": [body[:1500]], "pre": []}]
            p["pre"] = []
        elif len(p["qs"]) < 2:
            continue
        sit = "\n".join(p["pre"]).strip()
        anx = [(t, "\n".join(x).strip()) for t, x in p["annexes"]]
        n = len(p["qs"])
        for i, q in enumerate(p["qs"]):
            stem = " ".join(q["lines"]).strip()
            m = POINTS.search(stem)
            pts = float(m.group(1).replace(",", ".")) if m and float(m.group(1).replace(",", ".")) <= 20 else None
            stem = POINTS.sub("", stem).strip() if pts else stem
            out.append(Question(exam_id, p["title"], q["num"], stem, " ".join(q["pre"]).strip(), sit, anx, i, n,
                                pts, "", int(year.group(1)) if year else None))
    return out


def _add_text(cur, last_q, s):
    if cur["mode"] == "annex" and cur["annexes"]:
        cur["annexes"][-1][1].append(s)
    elif last_q is None:
        cur["pre"].append(s)
    elif last_q["open"] and not re.search(r"[?.!]\s*$", " ".join(last_q["lines"])):
        last_q["lines"].append(s)       # suite de l'énoncé
    else:
        last_q["open"] = False
        # texte après une question terminée : amorce de la question suivante
        cur.setdefault("_pending", []).append(s)
        cur["pre_next"] = cur.get("pre_next", []) + [s]
        last_q.setdefault("after", []).append(s)


def attach_preambles(qs: list[Question], raw_parts=None):
    return qs


# ------------------------------------------------------------------------------- corrigés
def parse_correction(text: str, qs: list[Question], sim) -> dict:
    """Associe à chaque question du sujet son passage de corrigé : parmi les lignes numérotées du
    corrigé portant le même numéro, celle dont le texte ressemble le plus à l'énoncé."""
    lines = strip_noise(text)
    marks = []
    for i, l in enumerate(lines):
        m = QNUM.match(l.strip())
        if m and len(l.strip()) > 12:
            marks.append((i, int(m.group(1)), QNUM.sub("", l.strip())))
    if not marks:
        return {}
    # appariement un-à-un, glouton par similarité décroissante, en respectant l'ordre du sujet
    cands = sorted(((sim(q.stem, t + " " + " ".join(lines[i + 1:i + 3])), qi, i)
                    for qi, q in enumerate(qs) for i, n, t in marks if n == q.num), reverse=True)
    chosen, used = {}, set()
    for s, qi, i in cands:
        if s <= 0.25 or qi in chosen or i in used:
            continue
        before = [chosen[k] for k in chosen if k < qi]
        after = [chosen[k] for k in chosen if k > qi]
        if (before and i < max(before)) or (after and i > min(after)):
            continue
        chosen[qi] = i
        used.add(i)
    starts = sorted(set(chosen.values()))
    res = {}
    all_marks = [i for i, _, _ in marks]
    for qi, i in chosen.items():
        nxt = [j for j in starts if j > i]
        # fin : prochaine question retenue, ou prochain titre de partie
        end = nxt[0] if nxt else len(lines)
        for j in range(i + 1, end):
            if PART.match(lines[j].strip()) and len(lines[j].strip()) < 70:
                end = j
                break
        head = lines[i]
        m = POINTS.search(head) or POINTS.search(" ".join(lines[i + 1:i + 3]))
        pts = float(m.group(1).replace(",", ".")) if m else None
        body = "\n".join(lines[i + 1:end]).strip()
        res[qi] = {"answer": body[:6000], "points": pts if pts and pts <= 20 else None}
    return res


def course_refs(text: str, sections: list["Section"]) -> list[str]:
    """Sections du cours explicitement citées dans un corrigé (évaluation seulement)."""
    t = norm(text.split("Proposition de corrig")[0][:20000])
    hits = []
    for s in sections:
        if not s.num:
            continue
        title_words = {w for w in re.findall(r"[a-z]{4,}", norm(s.title))}
        for m in re.finditer(r"(?<![\d.])" + re.escape(s.num) + r"(?:\.\d)*\.?\s+([^\n]{0,80})", t):
            # le numéro doit être suivi d'un mot du titre (sinon : autre matière, autre numérotation)
            if title_words & set(re.findall(r"[a-z]{4,}", m.group(1))):
                hits.append(s.id)
                break
    return hits


# ------------------------------------------------------------------------------- cours
@dataclass
class Section:
    id: str
    num: str
    title: str
    parent: str
    text: str
    passages: list = field(default_factory=list)
    order: int = 0


def parse_course(paths: list[Path]) -> list[Section]:
    """Sections = titres de niveau 2 (## ou numérotation « 1.2 ») ; passages = paragraphes et
    sous-titres de niveau 3. Les titres de niveau 1 donnent le parent."""
    secs, parent, cur = [], "", None
    for p in sorted(paths):
        for raw in read_text(p).splitlines():
            l = raw.rstrip()
            m1 = re.match(r"^#\s+(.+)", l)
            m2 = re.match(r"^##\s+(.+)", l) or (re.match(r"^\s*((\d+\.\d+)\.?\s+[A-ZÉ].{3,80})$", l) if p.suffix == ".pdf" else None)
            if m1 and not l.startswith("##"):
                parent = m1.group(1).strip()
                continue
            if m2:
                title = m2.group(1).strip()
                num = re.match(r"(\d+(?:\.\d+)*)", title)
                cur = Section(f"s{len(secs)}", num.group(1) if num else "", title, parent, "", [], len(secs))
                secs.append(cur)
                continue
            if cur is None:
                continue
            cur.text += l + "\n"
    for s in secs:
        chunks = re.split(r"\n\s*\n|\n(?=### )", s.text)
        buf = []
        for c in chunks:
            c = c.strip()
            if not c:
                continue
            if c.startswith("### ") and "\n" not in c:
                buf.append(c[4:])  # titre seul : il sera collé au paragraphe suivant
                continue
            if buf:
                c = " — ".join(buf) + " : " + c
                buf = []
            if len(c) > 40:
                s.passages.append(re.sub(r"\s+", " ", c.replace("### ", "")))
    return [s for s in secs if s.passages]


# ------------------------------------------------------------------------------- lots
def pair_files(d: Path) -> list[tuple[str, Path, Path | None]]:
    files = [f for f in d.rglob("*") if f.suffix.lower() in (".pdf", ".md", ".txt")]
    key = lambda f: re.sub(r"[-_ ]*(sujet|officiel|enonce|énoncé|corrige|corrigé|correction|bareme)[-_ ]*", "-",
                           f.stem.lower()).strip("-")
    sujets = {key(f): f for f in files if not CORR.search(f.stem)}
    corr = {key(f): f for f in files if CORR.search(f.stem)}
    return [(k, f, corr.get(k)) for k, f in sorted(sujets.items())]


# ===== examgen/prof/forecast.py =====
"""Prévoir le sujet suivant : quels passages du cours tomberont, posés comment, avec quelle intention.

Le moteur ne reçoit que les anciens sujets et le cours (aucune règle propre à une matière) :
  1. lecture des anciens sujets (auto-réglage, auto-entraînement, boucle intentions <-> alignement) ;
  2. pour chaque passage du cours, probabilité de tomber l'année suivante. Variables : les 12
     génériques (place, poids, centralité, historique...) + récence (tombé l'an dernier, années
     depuis) + variables propres à la matière découvertes dans le cours (thèmes, formes) ;
  3. preuve « comme en vrai » : pour chaque année récente, le modèle n'apprend QUE sur les années
     d'avant, prédit, puis on regarde le vrai sujet de l'année (couverture des questions réelles) ;
  4. pour chaque passage prévu : manière de demander la plus probable, type d'intention, et
     intention cachée = ce que l'enseignant évalue sans le dire (mots du passage que ses énoncés
     taisent mais que ses corrigés exigent).
  python -m examgen.prof.forecast droit nsi
"""
from __future__ import annotations

import json
import re
import sys
import warnings
from collections import Counter, defaultdict
from pathlib import Path

import joblib
import numpy as np
from ..fast import auc as roc_auc_score

from ..meta import align as A, loop as LP, selftrain as ST
from ..meta.domain import eval_labels, load
from ..meta.intent import Intent
from . import docs as D

ROOT = Path(__file__).resolve().parents[2]
TOP = 0.10  # part du cours « à réviser » : les 10 % de passages jugés les plus probables
EXTRA = ["section_tombee_l_an_dernier", "annees_depuis_la_section", "passage_tombe_l_an_dernier"]


def reading(name: str, log=print):
    """Lecture complète des anciens sujets (mise en cache : c'est la partie longue)."""
    cache = ROOT / "data" / "cache" / f"lecture_{name}.joblib"
    if cache.exists():
        t, S, loop_rep = joblib.load(cache)  # t compris : le réglage choisi le modifie
    else:
        t = load(name)
        meta = json.loads((ROOT / "data" / "model" / "meta.json").read_text())
        cfg, w, _ = A.self_tune(t, meta["poids"])
        S, _ = ST.improve(t, A.combine(A.views(t, cfg), w))
        S, _, loop_rep = LP.run(t, S, gens=2, log=log)
        joblib.dump((t, S, loop_rep), cache)
    t.rep = getattr(t, "rep", {})
    for q, s in zip(t.Q, S.argmax(1)):
        q.sec = int(s)
    t.consigne_vocab()
    t.consigne_facets()
    it = Intent(t, S)
    it.features()
    return t, S, it, loop_rep


class Forecast:
    def __init__(self, t, it, loop_rep):
        self.t, self.it, self.lr = t, it, loop_rep
        self.n = len(t.pass_text)
        self.T, self.tnames = LP.course_variables(t.pass_text)
        self.tested = defaultdict(set)
        self.q_of = defaultdict(list)
        for i, (q, p) in enumerate(zip(t.Q, it.pas)):
            if q.year:
                self.tested[q.year].add(int(p))
                self.q_of[q.year].append(i)
        self.years = sorted(self.tested)
        qw = [set(re.findall(r"[a-z]{4,}", D.norm(q.stem + " " + q.situation[:2000]))) for q in t.Q]
        df = Counter(w for x in qw for w in x)
        self.generic = {w for w, c in df.items() if c > 0.12 * len(qw)}
        self.base = ["rang_du_passage_dans_la_section", "longueur_du_passage", "centralite_du_passage", "redondance_du_passage",
                     "insistance_typographique", "passage_avec_reference", "densite_symboles_du_passage",
                     "place_de_la_section_dans_le_cours", "taille_de_la_section", "centralite_de_la_section",
                     "frequence_passee_du_passage", "frequence_passee_de_la_section"]

    # ------------------------------------------------------------------ variables d'une année
    def rows(self, target: int, hist: list[int]) -> np.ndarray:
        it, ps, K = self.it, self.t.pass_sec, len(self.t.sections)
        hist = [z for z in hist if z != target] or [z for z in self.years if z != target]
        pf = np.array([np.mean([p in self.tested[z] for z in hist]) for p in range(self.n)])
        sec_t = {z: {int(ps[p]) for p in self.tested[z]} for z in hist}
        sf = np.array([np.mean([s in sec_t[z] for z in hist]) for s in range(K)])
        before = [z for z in hist if z < target]
        last = max(before) if before else None
        s_last = np.array([float(last is not None and s in sec_t[last]) for s in range(K)])
        since = np.array([min([target - z for z in before if s in sec_t[z]] or [8]) for s in range(K)], float)
        p_last = np.array([float(last is not None and p in self.tested[last]) for p in range(self.n)])
        X = np.column_stack([it.p_rank, it.p_len, it.p_central, it.p_redund, it.p_emph, it.p_ref, it.p_sym,
                             it.s_order[ps], it.s_size[ps], it.s_central[ps], pf, sf[ps], s_last[ps], since[ps], p_last])
        return X

    def design(self, X):
        """Base + récence ; et, pour les arbres, variables propres à la matière et croisements."""
        Xb = X
        nm = self.base + EXTRA
        Xf = np.hstack([LP._design(X[:, :12], self.base, self.T, self.n), X[:, 12:]])
        return Xb, Xf

    def _train(self, train_years: list[int]):
        """Une ligne par (année d'entraînement, passage) ; historique = les autres années d'entraînement."""
        Xs, ys = [], []
        for z in train_years:
            Xs.append(self.rows(z, train_years))
            ys.append(np.array([p in self.tested[z] for p in range(self.n)], int))
        return np.vstack(Xs), np.concatenate(ys)

    def _fit_predict(self, fam: str, Xtr, ytr, Xte) -> np.ndarray:
        if fam == "popularite":
            return Xte[:, 10] + 0.01 * Xte[:, 11]
        if fam == "ensemble":  # moyenne des rangs des trois familles
            from scipy.stats import rankdata
            return np.mean([rankdata(self._fit_predict(f, Xtr, ytr, Xte)) for f in LP.FAMILIES], 0) / len(Xte)
        kind, mk = LP.FAMILIES[fam]
        Btr, Ftr = self.design(Xtr)
        Bte, Fte = self.design(Xte)
        A_, B_ = (Btr, Bte) if kind == "base" else (Ftr, Fte)
        return mk().fit(A_, ytr).predict_proba(B_)[:, 1]

    # ------------------------------------------------------------------ preuve : comme en vrai
    def backtest(self, k_years: int = 5, min_hist: int = 3) -> dict:
        """Chaque année testée : apprentissage sur les seules années d'avant. La famille « choisie
        seule » pour une année est celle qui a le mieux prévu les années testées précédentes."""
        learned = list(LP.FAMILIES) + ["ensemble"]
        fams = ["popularite"] + learned
        tests = [y for y in self.years if len([z for z in self.years if z < y]) >= min_hist][-k_years:]
        res = {f: defaultdict(list) for f in fams + ["choisie_seule"]}
        top = max(1, int(TOP * self.n))
        self.choices = []
        for y in tests:
            past = [z for z in self.years if z < y]
            Xtr, ytr = self._train(past)
            Xte = self.rows(y, past)
            yte = np.array([p in self.tested[y] for p in range(self.n)], int)
            qs = self.q_of[y]
            prev = {f: self._score(res[f]) for f in learned}
            pick = max(prev, key=prev.get) if res[learned[0]]["auc"] else self.lr.get("famille_choisie", learned[-2])
            self.choices.append(pick)
            P = {f: self._fit_predict(f, Xtr, ytr, Xte) for f in fams}
            P["choisie_seule"] = P[pick]
            for f, p in P.items():
                sel = set(np.argsort(-p)[:top])
                near = self._near(sel)
                res[f]["auc"].append(roc_auc_score(yte, p) if len(set(yte)) > 1 else 0.5)
                res[f]["questions_couvertes"].append(np.mean([self.it.pas[i] in sel for i in qs]))
                res[f]["questions_couvertes_a_un_passage_pres"].append(np.mean([self.it.pas[i] in near for i in qs]))
                real = {int(self.t.pass_sec[self.it.pas[i]]) for i in qs}
                res[f]["chapitres_prevus_tombes_sur_5"].append(len(set(self._top_sections(p, 5)) & real))
        self.final = max(learned, key=lambda f: self._score(res[f]))
        out = {"annees_testees": tests, "passages_du_cours": self.n, "passages_prevus": top,
               "hasard_questions_couvertes": round(top / self.n, 3), "choix_par_annee": dict(zip(map(str, tests), self.choices)),
               "famille_pour_l_annee_prevue": self.final}
        for f, r in res.items():
            out[f] = {k: round(float(np.mean(v)), 3) for k, v in r.items()}
            out[f]["par_annee"] = {str(y): round(float(v), 3) for y, v in zip(tests, r["questions_couvertes"])}
        return out

    @staticmethod
    def _score(r) -> float:
        return float(np.mean(r["questions_couvertes"]) + 0.1 * np.mean(r["auc"])) if r["auc"] else 0.0

    def _near(self, sel: set) -> set:
        """Passage prévu ou son voisin immédiat dans la même section."""
        ps = self.t.pass_sec
        out = set(sel)
        for p in sel:
            for d in (-1, 1):
                if 0 <= p + d < self.n and ps[p + d] == ps[p]:
                    out.add(p + d)
        return out

    def _top_sections(self, p, k):
        ps = self.t.pass_sec
        sp = np.array([p[ps == s].max() if (ps == s).any() else 0 for s in range(len(self.t.sections))])
        return [int(s) for s in np.argsort(-sp)[:k]]

    # ------------------------------------------------------------------ l'année suivante
    def next_year(self) -> np.ndarray:
        fam = getattr(self, "final", None) or self.lr.get("famille_choisie", "arbres_generiques_et_propres_a_la_matiere")
        Xtr, ytr = self._train(self.years)
        nxt = self.years[-1] + 1
        self.prob = self._fit_predict(fam, Xtr, ytr, self.rows(nxt, self.years))
        self.annee = nxt
        return self.prob

    def hidden(self, p: int, k: int = 6) -> dict:
        """Ce que l'enseignant évalue sans le dire, appris de ses questions sur cette section."""
        t, it = self.t, self.it
        s = int(t.pass_sec[p])
        voc = it.wv.get_feature_names_out()
        row = it.Pw[p].toarray().ravel()
        terms = [voc[j] for j in np.argsort(-row)[:25] if row[j] > 0]
        past = [i for i, q in enumerate(t.Q) if int(t.pass_sec[it.pas[i]]) == s]
        if not past:  # section jamais tombée : questions sur les passages les plus proches
            sims = (t.P[it.pas] @ t.P[p].T).toarray().ravel()
            past = list(np.argsort(-sims)[:8])
        said = [set(re.findall(r"[a-z]{4,}", D.norm(t.Q[i].stem + " " + t.Q[i].situation[:3000]))) for i in past]
        ans = [set(re.findall(r"[a-z]{4,}", D.norm(t.Q[i].answer))) for i in past if t.Q[i].answer]
        # mot propre au chapitre : bien plus fréquent dans ses passages que dans le reste du cours
        col = {w: it.wv.vocabulary_[w] for w in terms}
        insec = np.asarray((it.Pw[t.pass_sec == s] > 0).mean(0)).ravel()
        allc = np.asarray((it.Pw > 0).mean(0)).ravel()
        if not hasattr(self, "_spread"):  # part des chapitres où le mot apparaît : un mot de liaison est partout
            ps = np.asarray(t.pass_sec)
            M = np.vstack([np.asarray((it.Pw[ps == z] > 0).max(0).todense()).ravel() for z in np.unique(ps)])
            self._spread = M.mean(0)
        terms = [w for w in terms if insec[col[w]] >= 2.5 * allc[col[w]] and w not in self.generic and allc[col[w]] < 0.06
                 and self._spread[col[w]] < 0.3]
        if not hasattr(self, "_all_ans"):  # tous les corrigés : pour écarter les mots de liaison
            self._all_ans = [set(re.findall(r"[a-z]{4,}", D.norm(q.answer))) for q in t.Q if q.answer]
            ex_w = defaultdict(set)  # sans corrigés : vocabulaire réellement employé par l'enseignant
            for q in t.Q:
                for w in set(re.findall(r"[a-z]{4,}", D.norm(q.stem + " " + q.situation))):
                    ex_w[w].add(q.exam)
            self._exam_n = {w: len(e) for w, e in ex_w.items()}
        cachee, dite = [], []
        for w in terms:
            r_said = np.mean([w in x for x in said])
            r_ans = np.mean([w in x for x in ans]) if ans else None
            r_all = np.mean([w in x for x in self._all_ans]) if self._all_ans else 0
            if r_ans is None:  # pas de corrigé : mot de l'enseignant (≥ 3 sujets) et récurrent dans le chapitre
                spec = self._exam_n.get(w, 0) >= 3 and insec[col[w]] >= 0.1
            else:
                spec = r_ans >= 2 * r_all  # propre aux corrigés de ce chapitre
            if r_said < 0.2 and spec and (r_ans is None or r_ans >= max(0.25, 2 * r_said)):
                cachee.append(w)
            elif r_said >= 0.4:
                dite.append(w)
        fac = Counter(t.Q[i].facet for i in past)
        ex = sorted(past, key=lambda i: -float((t.P[it.pas[i]] @ t.P[p].T).toarray()[0, 0]))[:2]
        types = Counter(int(it.labels[i]) for i in past) if hasattr(it, "labels") else Counter()
        return {"evalue_sans_etre_dit": cachee[:k], "toujours_nomme": dite[:4],
                "manieres_de_demander": [{"facette": int(f), "nom": t.facets[f]["nom"], "part": round(c / len(past), 2)} for f, c in fac.most_common(3)],
                "type_d_intention": types.most_common(1)[0][0] if types else None,
                "questions_passees_proches": [{"sujet": t.Q[i].exam, "enonce": t.Q[i].stem[:220]} for i in ex]}

    def ranking(self, n_top: int = 15, per_section: int = 2) -> list[dict]:
        t = self.t
        out, cnt = [], Counter()
        for p in np.argsort(-self.prob):
            s = int(t.pass_sec[p])
            if cnt[s] >= per_section:
                continue
            cnt[s] += 1
            out.append({"passage": int(p), "section": s, "section_titre": t.sections[s].title,
                        "probabilite": round(float(self.prob[p]), 3), "texte": t.pass_text[p][:600],
                        "deja_tombe": int(sum(p in self.tested[z] for z in self.years)), **self.hidden(int(p))})
            if len(out) == n_top:
                break
        return out

    # ------------------------------------------------------------------ tout le cours
    def _pot_model(self, train_years):
        """Manière de l'enseignant sans l'historique : quel GENRE de passage il choisit
        (place, centralité, insistance, références...), donc applicable à un passage jamais tombé."""
        Xtr, ytr = self._train(train_years)
        from sklearn.linear_model import LogisticRegression
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        return make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight="balanced")).fit(Xtr[:, :10], ytr)

    def novelty_proof(self, min_hist: int = 3) -> dict:
        """Preuve « comme en vrai » sur les questions NOUVELLES : passage jamais interrogé avant
        l'année testée. Le potentiel les classe-t-il mieux que le hasard ?"""
        aucs, cov, n_new, tests = [], [], 0, []
        for y in [z for z in self.years if len([w for w in self.years if w < z]) >= min_hist]:
            past = [z for z in self.years if z < y]
            seen = set().union(*(self.tested[z] for z in past))
            fresh = np.array([p not in seen for p in range(self.n)])
            yte = np.array([p in self.tested[y] for p in range(self.n)], int)
            if fresh.sum() < 10 or len(set(yte[fresh])) < 2:
                continue
            pot = self._pot_model(past).predict_proba(self.rows(y, past)[:, :10])[:, 1]
            aucs.append(roc_auc_score(yte[fresh], pot[fresh]))
            idx = np.where(fresh)[0]
            sel = set(idx[np.argsort(-pot[idx])[:max(1, int(0.25 * len(idx)))]].tolist())
            qs = [i for i in self.q_of[y] if int(self.it.pas[i]) not in seen]
            n_new += len(qs)
            if qs:
                cov.append(np.mean([int(self.it.pas[i]) in sel for i in qs]))
            tests.append(y)
        return {"annees_testees": tests, "questions_nouvelles": n_new,
                "auc_potentiel_sur_passages_jamais_tombes": round(float(np.mean(aucs)), 3) if aucs else None,
                "nouvelles_couvertes_par_le_quart_retenu": round(float(np.mean(cov)), 3) if cov else None, "hasard": 0.25}

    def programme(self, per_sec: int = 3) -> list[dict]:
        """Chaque chapitre du cours, classé par priorité d'entraînement."""
        t, ps, K = self.t, np.asarray(self.t.pass_sec), len(self.t.sections)
        if getattr(self, "pot", None) is None:
            self.pot = self._pot_model(self.years).predict_proba(self.rows(self.annee, self.years)[:, :10])[:, 1]
        from scipy.stats import rankdata
        rp, rq = rankdata(self.prob) / self.n, rankdata(self.pot) / self.n
        sec_years = {s: sum(any(int(ps[p]) == s for p in self.tested[z]) for z in self.years) for s in range(K)}
        rows = []
        for s in range(K):
            idx = np.where(ps == s)[0]
            if not len(idx):
                continue
            score = 0.6 * rp[idx] + 0.4 * rq[idx]
            rows.append({"section": s, "titre": t.sections[s].title, "passages": int(len(idx)),
                         "proba": round(float(self.prob[idx].max()), 3), "potentiel": round(float(self.pot[idx].max()), 3),
                         "annees_tombees": int(sec_years[s]), "sur": len(self.years),
                         "priorite": round(float(score.max()), 3), "_top": idx[np.argsort(-score)[:per_sec]].tolist()})
        rows.sort(key=lambda r: -r["priorite"])
        q = np.quantile([r["priorite"] for r in rows], [0.5, 0.75])
        qp = np.quantile([r["potentiel"] for r in rows], 0.5)
        for r in rows:
            if r["priorite"] >= q[1] and r["annees_tombees"] >= 2:
                r["niveau"] = "incontournable"
            elif r["annees_tombees"] <= 1 and r["potentiel"] >= qp:
                r["niveau"] = "peu ou jamais tombé, mais dans la manière du professeur"
            elif r["priorite"] >= q[0]:
                r["niveau"] = "probable"
            else:
                r["niveau"] = "à connaître"
            r["passages_cles"] = [{"passage": int(p), "texte": t.pass_text[p][:400], "proba": round(float(self.prob[p]), 3),
                                   "potentiel": round(float(self.pot[p]), 3),
                                   "deja_tombe": int(sum(p in self.tested[z] for z in self.years)), **self.hidden(int(p))}
                                  for p in r.pop("_top")]
        return rows


def run(name: str, log=print) -> dict:
    warnings.filterwarnings("ignore")
    t, S, it, loop_rep = reading(name, log)
    rp = json.loads((ROOT / "output" / "meta" / "rapport.json").read_text())
    keep = rp["intentions"]["par_matiere"].get(name, {}).get("types_d_intention", {}).get("variables_utilisees", [])
    ty = it.types(keep) if keep else {"types": []}
    fc = Forecast(t, it, loop_rep)
    log(f"{name} : {len(fc.years)} années, {fc.n} passages")
    bt = fc.backtest()
    log(f"  preuve : {json.dumps({k: v for k, v in bt.items() if isinstance(v, dict)}, ensure_ascii=False)[:600]}")
    fc.next_year()
    from ..meta import transfer as TR
    auto = TR.apply(fc, log)  # même règle pour tous les domaines, sans choix propre à la matière
    # le classement vient de la règle universelle ; les probabilités affichées gardent la loi de
    # l'ancien modèle (même nombre attendu de passages), réordonnées selon ce classement
    order = np.argsort(np.argsort(auto["prevision"]["p"], kind="stable"), kind="stable")
    fc.prob, fc.pot = np.sort(fc.prob)[order], auto["nouveaute"]["p"]
    rk = fc.ranking()
    nov = fc.novelty_proof()
    log(f"  nouveautés : {nov}")
    prog = fc.programme()
    lab = {x["id"]: x for x in ty["types"]}
    for r in rk + [x for g in prog for x in g["passages_cles"]]:
        k = r.pop("type_d_intention")
        r["intention"] = {"fort": lab[k]["fort"], "faible": lab[k]["faible"]} if k in lab else None
    rep = {"matiere": name, "annee_prevue": fc.annee, "annees_connues": fc.years, "preuve_comme_en_vrai": bt,
           "famille_choisie": fc.final, "passages_les_plus_probables": rk,
           "preuve_sur_les_nouveautes": nov, "programme": prog,
           "auto_progression": {o: {k: v for k, v in a.items() if k != "p"} for o, a in auto.items()}}
    if TR.RULE_OUT.exists():
        rg = json.loads(TR.RULE_OUT.read_text(encoding="utf-8"))
        rep["preuve_auto_progression"] = {**rg["matieres"].get(name, {}), "auto_jugement": rg["auto_jugement"]}
    crit = TR.AP.ROOT / "output" / "meta" / "critique.json"
    if crit.exists():
        cr = json.loads(crit.read_text(encoding="utf-8"))
        rep["preuve_autocritique"] = {"matiere_exclue": cr["matieres"].get(name), "synthese": cr["synthese"]}
    from ..meta.domain import out_dir
    out = out_dir(name)
    out.mkdir(parents=True, exist_ok=True)
    (out / "previsions.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    joblib.dump((t, fc.prob, rk), ROOT / "data" / "cache" / f"prevision_{name}.joblib")
    return rep


if __name__ == "__main__":
    for n in sys.argv[1:] or ["droit", "nsi"]:
        run(n)


# ===== examgen/prof/pdfcours.py =====
"""Cours PDF quelconque -> markdown lisible par `docs.parse_course`.

Aucune règle propre à une matière : la structure vient de la typographie.
- taille de police au-dessus du corps de texte -> titres (# pour la plus grande, ## ensuite) ;
- ligne courte en gras, à la taille du corps -> ### (collé au paragraphe suivant) ;
- tableaux -> une ligne de tableau = un passage « colonne 1 — colonne 2 : … » ;
- en-têtes / pieds de page répétés et numéros de page retirés.
Sert à l'entraînement (programmes officiels) et en production (cours envoyés en PDF).
"""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

import pdfplumber


def _clean(s: str) -> str:
    s = re.sub(r"\(cid:\d+\)", "", s)  # glyphes sans correspondance unicode
    s = s.replace("\u00a0", " ").replace("\uf0b7", "•").replace("\uf0a7", "•").replace("\uf0d8", "•")
    return re.sub(r"\s+", " ", s).strip()


def _sentences_chunks(text: str, max_len: int = 450) -> list[str]:
    if len(text) <= max_len:
        return [text]
    sents = re.split(r"(?<=[.!?;])\s+(?=[A-ZÉÈÀÂÎÔ«•\-–])", text)
    out, buf = [], ""
    for s in sents:
        if buf and len(buf) + len(s) > max_len:
            out.append(buf)
            buf = s
        else:
            buf = f"{buf} {s}".strip()
    if buf:
        out.append(buf)
    return out


def _lines(page, tables_bbox):
    def inside(l):
        cx, cy = (l["x0"] + l["x1"]) / 2, (l["top"] + l["bottom"]) / 2
        return any(b[0] - 2 <= cx <= b[2] + 2 and b[1] - 2 <= cy <= b[3] + 2 for b in tables_bbox)

    for l in page.extract_text_lines(return_chars=True):
        if inside(l):
            continue
        chars = [c for c in l["chars"] if c["text"].strip()]
        if not chars:
            continue
        letters = [c for c in chars if c["text"].isalpha()] or chars
        sizes = collections.Counter(round(c["size"]) for c in letters)
        bold = sum("bold" in c["fontname"].lower() for c in letters) / len(letters)
        col = collections.Counter(str(c.get("non_stroking_color")) for c in letters).most_common(1)[0][0]
        yield {"text": _clean(l["text"]), "size": sizes.most_common(1)[0][0], "bold": bold > 0.6,
               "color": col, "top": l["top"], "bottom": l["bottom"], "page": page.page_number}


def _blocks(path: Path) -> list[tuple]:
    """Suite de blocs : ("h", rang_de_style, texte) | ("p", texte) | ("row", intitulé, [passages])."""
    pdf = pdfplumber.open(str(path))
    items = []
    for page in pdf.pages:
        tabs = [t for t in page.find_tables() if len(t.rows) >= 2]
        for t in tabs:
            for row in t.extract():
                cells = [c for c in (_clean(c or "") for c in row) if c]
                if cells:
                    items.append((page.page_number, t.bbox[1], "row", cells))
        for l in _lines(page, [t.bbox for t in tabs]):
            items.append((l["page"], l["top"], "line", l))
    items.sort(key=lambda x: (x[0], x[1]))
    lines = [x[3] for x in items if x[2] == "line"]
    if not lines:
        return []
    rep = collections.Counter(re.sub(r"\d+", "#", l["text"]) for l in lines)
    noise = {k for k, v in rep.items() if v >= max(3, len(pdf.pages) // 3) and len(k) < 120}
    style = lambda l: (l["size"], l["bold"], l["color"])
    vol = collections.Counter()
    for l in lines:
        vol[style(l)] += len(l["text"])
    body = vol.most_common(1)[0][0]
    total = sum(vol.values())
    cand = [st for st in vol if st != body and vol[st] < 0.15 * total and
            (st[0] > body[0] or st[1] or st[2] != body[2]) and st[0] >= body[0]]
    rank = {st: i for i, st in enumerate(sorted(cand, key=lambda st: (-st[0], not st[2] != body[2], not st[1])))}

    out, para, last, header_seen = [], [], None, False
    def flush():
        if para:
            for c in _sentences_chunks(_clean(" ".join(para))):
                out.append(("p", c))
            para.clear()

    for _, _, kind, x in items:
        if kind == "row":
            flush()
            cells, last = x, None
            if not header_seen and all(len(c) < 60 for c in cells):
                header_seen = True  # en-tête de tableau
                continue
            rest = " ".join(cells[1:])
            if len(cells) >= 2 and len(cells[0]) < 200 and len(rest) > len(cells[0]):
                ps = [c for b in re.split(r"\s(?=[-•▪–]\s)", rest) for c in _sentences_chunks(b.strip(" -•▪–"))]
                out.append(("row", cells[0], ps))
            else:
                for c in _sentences_chunks(" : ".join([cells[0], " ; ".join(cells[1:])]) if len(cells) > 1 else cells[0], 600):
                    out.append(("p", c))
            continue
        header_seen = False
        l, t = x, x["text"]
        if re.sub(r"\d+", "#", t) in noise or re.fullmatch(r"[\d\s/.\-–]+", t):
            continue
        r = rank.get(style(l))
        if r is not None and len(t) < 150 and not t.endswith((",", ";")):
            flush()
            if out and out[-1][0] == "h" and out[-1][1] == r and last is not None and last.get("h") \
                    and l["page"] == last["page"] and l["top"] - last["bottom"] < l["size"] * 1.2:
                out[-1] = ("h", r, out[-1][2] + " " + t)  # titre sur deux lignes
            else:
                out.append(("h", r, t.lstrip("•▪ ").strip()))
            last = {**l, "h": True}
            continue
        if (last is None or last.get("h") or l["page"] != last["page"]
                or l["top"] - last["bottom"] > l["size"] * 0.9 or t[:1] in "•-–▪◦"):
            flush()
        para.append(t)
        last = l
    flush()
    return out


def _render(blocks, k: int) -> str:
    md = []
    for b in blocks:
        if b[0] == "p":
            md.append(b[1])
        elif b[0] == "row":
            md.append(f"## {b[1]}")
            md += b[2]
        else:
            md.append(("#" if b[1] < k else "##" if b[1] == k else "###") + " " + b[2])
    return "\n\n".join(md) + "\n"


def _score(md: str) -> int:
    from . import docs
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(md)
    secs = docs.parse_course([Path(f.name)])
    Path(f.name).unlink()
    return sum(len(s.passages) >= 2 for s in secs)


def pdf_to_markdown(path: Path) -> str:
    """Le niveau de titre qui devient « section » est choisi sur le document lui-même :
    celui qui donne le plus de sections exploitables (au moins deux passages)."""
    blocks = _blocks(path)
    tiers = sorted({b[1] for b in blocks if b[0] == "h"})
    if not tiers:
        return _render(blocks, 0)
    best = max(tiers, key=lambda k: (_score(_render(blocks, k)), -k))
    return _render(blocks, best)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(pdf_to_markdown(Path(a)))


# ===== examgen/prof/plan.py =====
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

from .profile import Teacher


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
        arts = [p for p in s.passages if self.t.ref_ids.starts_with_ref(p)]
        txt = [p for p in s.passages if not self.t.ref_ids.starts_with_ref(p)]
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

    def probables(self, prev: dict, n_ex: int = 8) -> list[dict]:
        """Plans tirés de la prévision : passages les plus probables l'an prochain, posés comme
        l'enseignant les pose, avec ce qu'il évalue sans le dire. Puis le sujet le plus probable."""
        t = self.t
        top = prev["passages_les_plus_probables"]

        def enrich(pl, r):
            pl.update({"passage_vise": r["texte"], "probabilite_de_tomber": r["probabilite"], "deja_tombe": r["deja_tombe"],
                       "intention_cachee": {"evaluer_sans_le_dire": r["evalue_sans_etre_dit"], "deja_nomme_d_habitude": r["toujours_nomme"],
                                            "type": r.get("intention")},
                       "manieres_probables": r["manieres_de_demander"], "questions_passees_proches": r["questions_passees_proches"],
                       "regle": "La question la plus lourde porte sur le passage visé. L'énoncé ne nomme pas les notions de "
                                "« evaluer_sans_le_dire » ; le corrigé les exige."})
            return pl
        out, seen = [], set()
        for k, r in enumerate(top):
            if len(out) == n_ex:
                break
            if r["section"] in seen:
                continue
            seen.add(r["section"])
            out.append(enrich(self.cas(r["section"], f"P{len(out) + 1}", kind="probable"), r))
        per_exam = Counter(e for e, _ in t.parts)
        n_parts = max(1, int(np.median(list(per_exam.values()))))
        mock, themes = [], set()
        for r in top:
            th = t.sections[r["section"]].parent
            if th in themes and len(themes) < len({s.parent for s in t.sections}):
                continue
            themes.add(th)
            mock.append(enrich(self.cas(r["section"], f"SP-{len(mock) + 1}", kind="sujet_le_plus_probable"), r))
            if len(mock) == n_parts:
                break
        return out + mock

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
{d['references_citees_par_reponse_moyenne']} référence(s) citée(s) par réponse en moyenne.
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


# ===== examgen/prof/profile.py =====
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
from ..fast import auc as roc_auc_score
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
        texts = D.read_many([f for _, s, c in pairs for f in (s, c) if f])
        for key, s, c in pairs:
            qs = D.parse_exam(texts[Path(s)], key)
            self.qs += qs
            if c:
                raw_corr[key] = texts[Path(c)]
        self.ref_ids = RefModel(self.sections)
        self._fit_vectorizer()
        memo = {}
        vec = lambda a: memo[a] if a in memo else memo.setdefault(a, self.vec.transform([a]))
        sim = lambda a, b: float((vec(a) @ vec(b).T).toarray()[0, 0])
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
        if len(keys) < 6:  # trop peu de parties pour un mélange : on garde tout
            z = None
        g1 = None if z is None else GaussianMixture(1, covariance_type="diag", random_state=SEED).fit(z)
        g2 = None if z is None else GaussianMixture(2, covariance_type="diag", random_state=SEED, n_init=8).fit(z)
        keep = np.ones(len(keys), bool)
        if z is not None and g2.bic(z) < g1.bic(z):
            hi = int(np.argmax(g2.means_.sum(1)))
            keep = g2.predict(z) == hi
            # lissage par titre de partie (même mise en page d'un sujet à l'autre) : vote majoritaire
            tkey = lambda k: re.sub(r"\s*/\s*sujet\s*\d+", "", D.norm(k[1]))
            vote = defaultdict(list)
            for k, ok in zip(keys, keep):
                vote[tkey(k)].append(ok)
            keep = np.array([np.mean(vote[tkey(k)]) > 0.5 if len(vote[tkey(k)]) >= 3 else ok for k, ok in zip(keys, keep)])
            if keep.mean() < 0.2:  # presque tout « hors cours » : le mélange n'a pas isolé d'intrus, on garde tout
                keep = np.ones(len(keys), bool)
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
        # sans corrigé qui cite le cours : le moteur règle seul sa lecture avec la règle méta-apprise
        self.meta_tune = None
        meta = Path(__file__).resolve().parents[2] / "data" / "model" / "meta.json"
        if not any(self.refs.get(q.exam) for q in Q) and meta.exists():
            from ..meta.align import self_tune
            self.Q = Q
            cfg, w_meta, px = self_tune(self, json.loads(meta.read_text(encoding="utf-8"))["poids"])
            self.meta_tune = {"reglage_de_lecture": {**cfg, "ngram": list(cfg["ngram"])}, "poids": list(w_meta),
                              "signaux": {k: round(float(v), 3) for k, v in px.items()}}
            print(f"  alignement auto-réglé (méta) : {cfg} poids {w_meta}")
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
        self.w = tuple(self.meta_tune["poids"]) if self.meta_tune else max(grid, key=lambda w: score(combo(w), labelled))
        S = combo(self.w)
        if self.meta_tune:  # sans corrigé : auto-entraînement par générations (meta/selftrain.py)
            try:
                from ..meta.selftrain import improve
                S, hist = improve(self, S)
                self.meta_tune["auto_entrainement"] = hist
                print(f"  auto-entraînement : {len(hist)} étapes")
            except Exception as e:  # le moteur reste utilisable avec la lecture auto-réglée
                print("  auto-entraînement ignoré :", e)
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
            "auto_reglage_meta": self.meta_tune,
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


# ===== examgen/prof/redige.py =====
"""Rédaction générique, pour n'importe quelle matière, puis boucle « vérifier → corriger ».

Rien n'est propre à une matière : les consignes du rédacteur sont tirées du profil appris
(manières de demander, supports recopiés ou inventés, longueur des corrigés, intention cachée).
Chaque exercice rédigé passe au contrôle (check.Checker) ; ce que le contrôle reproche est
renvoyé au rédacteur, jusqu'à `tours` fois.

Deux chemins, même format de sortie (<out>/generated/<id>.json) :
  api     : appel direct à l'API Anthropic si ANTHROPIC_API_KEY est définie ;
  agents  : sinon, un prompt complet par plan dans <out>/prompts/<id>.md (avec les reproches
            du dernier contrôle s'il y en a), à faire rédiger par un agent.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

import numpy as np

from ..config import LLM_MODEL
from . import check
from .plan import teacher_brief

FORMAT = """{
  "id": "<id du plan>",
  "type": "<type du plan>",
  "titre": "titre court",
  "situation": "texte de la situation (cas et sujet complet)",
  "annexes": [{"titre": "Annexe 1 – …", "texte": "…", "source": "cours|documents_reels|invente"}],
  "questions": [
    {"slot": 1, "situation": "(exercices seulement : mini-cas de 3 à 6 lignes)",
     "enonce": "…", "points": 2, "reponse_attendue": "…", "articles_cites": []}
  ]
}"""


def consignes(t, name: str) -> str:
    """Consignes du rédacteur, écrites à partir de ce que le modèle a appris du professeur."""
    ck = check.Checker(t, [])
    nom = lambda f: "« " + (t.sup_facets[f].get("exemples_de_titres") or [t.sup_facets[f]["nom"]])[0][:70] + " »"
    recopie = [nom(f) for f, r in ck.src_rate.items() if r > 0.5]
    invente = [nom(f) for f, r in ck.src_rate.items() if r <= 0.5]
    d = t.detail_stats
    refs = d.get("references_citees_par_reponse_moyenne", 0) or 0
    sym = np.mean([len(re.findall(r"[(){}\[\]=<>;:_#]", q.stem)) / max(1, len(q.stem)) for q in t.Q]) if t.Q else 0
    L = [f"# Consignes du rédacteur ({name})", "",
         "Tu écris comme le professeur qui a conçu les anciens sujets. Le PROFIL ci-dessous est ce qu'un modèle",
         "scikit-learn a appris de lui. Pour chaque plan, tu rends un JSON au format donné à la fin.", "",
         "## Penser comme le professeur",
         "- Étudie `anciens_sujets_proches` : comment il pose une situation, annonce les documents, tourne chaque",
         "  question et ce que son corrigé attend. Ne recopie jamais une situation ancienne.",
         "- Pour chaque `questions[slot]`, reprends la manière de demander de la facette : imite la tournure de",
         "  ses `exemples_reels` (même verbe de consigne, même construction), sans les copier.",
         "- Le contenu vient de `cours` (et `cours_partenaire`) : la question fait travailler les notions de la",
         "  section visée. Si `inedit` est vrai, la section n'est jamais ou presque tombée : écris la question",
         "  qu'il pourrait poser, avec sa façon de faire.",
         "- Si le plan a une `intention_cachee` : la question la plus lourde porte sur `passage_vise` ;",
         "  l'énoncé ne nomme PAS les notions de `evaluer_sans_le_dire`, le corrigé les exige.", "",
         "## Documents"]
    if recopie:
        L.append(f"- Types que ce professeur reprend tels quels ({'; '.join(recopie)}) : recopie mot pour mot un texte fourni"
                 " dans `cours` ou `documents_reels` (coupe avec « […] »). N'invente ni texte, ni date, ni référence.")
    if invente:
        L.append(f"- Types qu'il fabrique pour le cas ({'; '.join(invente)}) : invente-les, cohérents avec la situation ;"
                 " un document chiffré inventé porte la mention « données fictives ».")
    L.append("- Indique pour chaque document `source` : `cours`, `documents_reels` ou `invente`.")
    L += ["", "## Corrigé",
          "- Écris le corrigé comme les siens, longueur `longueur_cible_car` (dans `longueur_reponse_car`)."]
    if refs >= 0.3:
        L.append("- `articles_cites` : seulement des références présentes dans les textes fournis.")
    if sym > 0.03:
        L.append("- Code et notations : complets, exacts et exécutables quand c'est du code.")
    L += ["", "## Format (JSON valide, rien d'autre)", "```json", FORMAT, "```",
          "Pour le type `exercices`, chaque question a sa courte `situation`. Garde les `slot` et `points` du plan."]
    return "\n".join(L)


def _user(plan: dict, revision: list[str] | None) -> str:
    u = "PLAN\n```json\n" + json.dumps(plan, ensure_ascii=False, indent=1, default=float) + "\n```"
    if revision:
        u += "\n\nLe contrôle automatique a relevé dans ta version précédente :\n" + "\n".join(f"- {r}" for r in revision) + \
             "\nRéécris l'exercice complet en corrigeant ces points."
    return u


def _parse(txt: str) -> dict:
    m = re.search(r"\{.*\}", txt, re.S)
    return json.loads(m.group(0)) if m else {}


def _ask(client, system: str, user: str) -> str:
    msgs = [{"role": "user", "content": user}]
    with client.messages.stream(model=LLM_MODEL, max_tokens=16000, system=system, messages=msgs,
                                thinking={"type": "adaptive"}) as s:
        m = s.get_final_message()
    return "".join(b.text for b in m.content if b.type == "text")


def run(t, plans: list[dict], out: Path, name: str, tours: int = 2, gen_sub: str = "generated", log=print) -> dict:
    out = Path(out)
    gen, pr = out / gen_sub, out / "prompts"
    gen.mkdir(parents=True, exist_ok=True)
    system = consignes(t, name) + "\n\n" + teacher_brief(t)
    (out / "consignes_redacteur_auto.md").write_text(system, encoding="utf-8")
    ck = check.Checker(t, plans)
    key = os.environ.get("ANTHROPIC_API_KEY")
    stats = {"plans": len(plans), "chemin": "api" if key else "agents", "corriges_par_la_boucle": 0, "ok_au_premier_jet": 0}
    if not key:
        pr.mkdir(parents=True, exist_ok=True)
        n = 0
        for p in plans:
            f = gen / f"{p['id']}.json"
            rev = None
            if f.exists():  # déjà rédigé : on renvoie seulement ce que le contrôle reproche
                try:
                    rev = ck.check_item(json.loads(f.read_text(encoding="utf-8")))["revision"] or None
                except (ValueError, KeyError):
                    rev = ["JSON invalide"]
                if not rev:
                    continue
            (pr / f"{p['id']}.md").write_text(f"{system}\n\n{_user(p, rev)}\n\nÉcris le résultat dans `{f}`.\n", encoding="utf-8")
            n += 1
        stats["prompts"] = n
        log(f"  {stats['prompts']} prompts -> {pr} (pas de clé API : à faire rédiger par un agent)")
        return stats
    import anthropic
    client = anthropic.Anthropic()
    for p in plans:
        rev, g = None, {}
        for k in range(tours + 1):
            try:
                g = _parse(_ask(client, system, _user(p, rev)))
            except (ValueError, anthropic.APIError) as e:
                rev = [f"réponse illisible : {e}"]
                continue
            g["id"] = p["id"]
            rev = ck.check_item(g)["revision"]
            if not rev:
                stats["ok_au_premier_jet" if k == 0 else "corriges_par_la_boucle"] += 1
                break
        (gen / f"{p['id']}.json").write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"  {p['id']} : {'ok' if not rev else f'{len(rev)} reproche(s) restants'}")
    return stats


# ===== examgen/report.py =====
"""Rapport d'analyse lisible (output/rapport_analyse.md) à partir de data/model/analysis.json."""
from __future__ import annotations

import json

from .config import MODEL_DIR, OUT


def fmt_pairs(pairs, n=10):
    return ", ".join(f"{a} ({b})" for a, b, *_ in pairs[:n])


def run():
    r = json.loads((MODEL_DIR / "analysis.json").read_text(encoding="utf-8"))
    c = r["corpus"]
    L = ["# Analyse des annales NSI (Terminale)", "",
         f"Corpus : {c['sujets_ecrits']} sujets écrits uniques ({c['exercices_ecrit']} exercices, {c['questions_ecrit']} questions), "
         f"{c['sujets_pratiques']} sujets pratiques ({c['exercices_pratique']} exercices), {c['sections_cours']} sections de cours.",
         f"Années : {c['annees']}", ""]

    a = r["archetypes"]
    L += [f"## 1. Archétypes de questions ({a['k_choisi']} formes, KMeans + silhouette)", "",
          "| # | archétype (tâche / format / Bloom) | n | position moy. | code | dépend d'avant | formulations |", "|---|---|---|---|---|---|---|"]
    for k, v in sorted(a["detail"].items(), key=lambda t: -t[1]["effectif"]):
        L.append(f"| {k} | {v['nom']} | {v['effectif']} | {v['position_moyenne']} | {v['avec_code']} | {v['depend_d_avant']} | {', '.join(v['formulations'][:4])} |")

    m = r["markov"]
    L += ["", "## 2. Enchaînement des questions (chaîne de Markov)", "",
          f"- Ouvertures typiques : {fmt_pairs(m['ouvertures_frequentes'], 4)}",
          f"- Fermetures typiques : {fmt_pairs(m['fermetures_frequentes'], 4)}",
          f"- Entropie moyenne des transitions : {m['entropie_moyenne_bits']} bits",
          "- Transitions les plus fortes :"]
    L += [f"  - {x} → {y} ({p})" for x, y, p in m["transitions_fortes"][:10]]

    g = r["graphe_notions"]
    L += ["", "## 3. Relations entre notions (graphe PMI)", "",
          f"- {g['notions_par_exercice_moyenne']} notions par exercice en moyenne",
          f"- Notions pivots (PageRank) : {fmt_pairs(g['notions_pivots_pagerank'], 8)}",
          f"- Notions ponts (betweenness) : {fmt_pairs(g['notions_ponts_betweenness'], 6)}",
          "- Associations fortes (PMI, nb d'exercices) :"]
    L += [f"  - {k.replace('|', ' + ')} : PMI {v}, {n} exercices" for k, v, n in g["associations_fortes_PMI"][:12]]
    L += ["- Blocs thématiques cachés (communautés) :"] + [f"  - {', '.join(b)}" for b in g["blocs_thematiques_caches"]]

    s = r["logique_des_sujets"]
    L += ["", "## 4. Logique de construction d'un sujet", "",
          f"- Recouvrement des domaines entre exercices d'un même sujet : {s['recouvrement_domaines_entre_exercices_d_un_sujet']} "
          f"(hasard : {s['recouvrement_si_exercices_tires_au_hasard']}) → {s['lecture']}",
          f"- Domaines couverts par sujet : {s['domaines_couverts_par_sujet_moyenne']} sur 5",
          f"- Barèmes d'exercices : {s['baremes_exercices']}",
          "- Courbe à l'intérieur d'un exercice :", "", "| position | Bloom moyen | part code | part dépendante | mots |", "|---|---|---|---|---|"]
    L += [f"| {k} | {v['bloom']} | {v['code']} | {v['dependance']} | {v['mots']} |" for k, v in s["courbe_dans_un_exercice"].items()]

    d = r["difficulte"]
    L += ["", "## 5. Difficulté (Gradient Boosting, cible = position relative)", "",
          f"- R² en validation croisée par sujet : {d['R2_validation_croisee_par_sujet']}",
          f"- Placé en début d'exercice : {fmt_pairs(d['placees_en_debut'], 6)}",
          f"- Placé en fin d'exercice : {fmt_pairs(d['placees_en_fin'], 6)}"]

    L += ["", "## 6. Facteurs latents (SVD sur ~90 variables)", ""]
    for f in r["facteurs_latents"][:6]:
        L.append(f"- F{f['facteur']} ({f['variance']}) : + {', '.join(f['pole_positif'][:4])}  /  − {', '.join(f['pole_negatif'][:4])}")
    L += ["", "## 7. Règles d'association (lift)", ""]
    L += [f"- {x} ⇒ {y} : lift {l}, P(B|A)={pba}" for x, y, _, l, pba, _ in r["regles_association"]["regles"][:15]]

    t = r["tendances"]
    L += ["", "## 8. Tendances et prévision", "",
          f"- En hausse : {fmt_pairs(t['en_hausse'], 6)}",
          f"- En baisse : {fmt_pairs(t['en_baisse'], 6)}",
          f"- Probabilité attendue par exercice (pondérée par récence) : {fmt_pairs(t['probabilite_attendue_par_exercice'], 12)}"]
    cv = r["cours_vs_epreuves"]
    L += [f"- Enseigné mais peu évalué : {fmt_pairs(cv['sous_evaluees_par_rapport_au_cours'], 8)}",
          f"- Très évalué par rapport au cours : {fmt_pairs(cv['sur_evaluees_par_rapport_au_cours'], 6)}"]

    g2 = r["regimes"]
    L += ["", "## 9. Changement de format 2022 → 2023", "",
          f"- χ² = {g2['chi2']} (p = {g2['p_value']:.1e}), Jensen-Shannon = {g2['jensen_shannon']}"]
    for k, v in g2["comparaison"].items():
        L.append(f"- {k} : {v}")

    L += ["", "## 10. Scénarios d'exercices (NMF)", ""]
    L += [f"- {', '.join(x['mots'][:6])} → {', '.join(n for n, _ in x['notions_associees'])}" for x in r["scenarios"]]
    p = r["epreuve_pratique"]
    L += ["", f"## 11. Épreuve pratique ({p['exercices_uniques']} exercices uniques)", ""]
    L += [f"- {x['effectif']} ex. : {', '.join(x['mots'][:5])} (ex1/ex2 : {x['exercice_1_ou_2']})" for x in p["typologie"]]
    cl = r["classifieur_notions"]
    L += ["", "## 12. Classifieur texte → notions (validateur)", "",
          f"- Top-3 correct en validation croisée : {cl['top3_hit_rate_cv']} ; micro-F1 : {cl['micro_f1_cv']}"]
    L += ["", "## 13. Questions atypiques (Isolation Forest)", ""]
    L += [f"- {q['annee']} {q['centre']} [{q['tache']}] {q['texte'][:150]}" for q in r["questions_atypiques"][:8]]
    (OUT / "rapport_analyse.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"[ok] {OUT / 'rapport_analyse.md'}")


if __name__ == "__main__":
    run()


# ===== examgen/validate.py =====
"""Validation des questions générées par les modèles appris sur les annales.

Pour chaque question : on la repasse dans la même chaîne d'extraction que les vraies questions puis
  - notion   : le classifieur texte -> notions place-t-il la notion visée dans son top 3 ?
  - forme    : l'archétype prédit (KMeans) est-il celui du plan, ou au moins le même type de tâche ?
  - Bloom    : le verbe de consigne donne-t-il le niveau visé (à ±1) ?
  - nouveauté: similarité max avec les 2 668 vraies questions (> 0.92 = quasi-copie)
  - ancrage  : similarité max avec les sections du cours
  - code     : le code Python du corrigé compile-t-il ? le code SQL a-t-il une forme valide ?
  - difficulté (sujets) : la position prédite par le modèle croît-elle avec la position voulue ?
"""
from __future__ import annotations

import ast
import json
import re
import textwrap
from collections import defaultdict

import joblib
import numpy as np
from scipy.stats import spearmanr

from . import features as F
from .config import MODEL_DIR, OUT
from .llm import GENERATED


def code_blocks(text: str) -> list[str]:
    blocks = re.findall(r"```(?:python|py)?\s*\n(.*?)```", text, re.S)
    if blocks:
        return blocks
    # sans balises : on garde le texte à partir de la première ligne qui ressemble à du code
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if re.match(r"\s*(def |class |from \w+ import|import \w+)", l)), None)
    return ["\n".join(lines[start:])] if start is not None else []


def python_ok(code: str) -> bool | None:
    # une méthode « à compléter » est souvent donnée indentée comme dans la classe
    lines = [l for l in code.splitlines() if l.strip()]
    if lines and all(re.match(r"\s*\d{1,3}\s+\S", l) for l in lines):
        # lignes numérotées du sujet (« ligne 10 : … ») : on retire les numéros
        code = "\n".join(re.sub(r"^\s*\d{1,3} ", "", l) for l in code.splitlines())
    code = textwrap.dedent(code)
    if re.search(r"\b(SELECT|INSERT|UPDATE|DELETE)\b", code):
        return None
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


def sql_ok(text: str) -> bool | None:
    # on ne vérifie que les requêtes écrites comme du code (bloc ``` ou ligne qui commence par le mot-clé),
    # pas les phrases du corrigé qui citent « SELECT … FROM … »
    blocks = re.findall(r"```[a-zA-Z]*\n(.*?)```", text, re.S)
    src = "\n".join(blocks) if blocks else text
    q = re.findall(r"^\s*((?:SELECT|INSERT|UPDATE|DELETE)\b.*?(?:;|\Z))", src, re.S | re.I | re.M)
    q = [s for s in q if "…" not in s]
    if not q:
        return None
    for s in q:
        s_up = s.upper()
        if s_up.startswith("SELECT") and " FROM " not in s_up.replace("\n", " "):
            return False
        if s.count("(") != s.count(")") or s.count("'") % 2:
            return False
    return True


def run() -> dict:
    m = joblib.load(MODEL_DIR / "models.joblib")
    plans = {}
    for name in ("plans.json", "plans_inedit.json"):
        if (OUT / name).exists():
            plans.update({p["id"]: p for p in json.loads((OUT / name).read_text(encoding="utf-8"))})
    fm = obs = ref = None
    if any(p["type"] == "inedit" for p in plans.values()) and (MODEL_DIR / "discovery_models.joblib").exists():
        from .discovery import FacetModel
        fm = FacetModel()
        dd = joblib.load(MODEL_DIR / "discovery_data.joblib")
        obs = {(n, int(c), int(s_)) for u, c, s_ in zip(dd["units"], dd["fs"], dd["fu"]) if u["src"] == "ecrit" for n in u["main"][:1]}
        ref = json.loads((MODEL_DIR / "discovery.json").read_text(encoding="utf-8"))["grammaire_des_combinaisons"]["plausibilite_mediane_des_vraies_questions"]
    gen = {}
    for f in sorted(GENERATED.glob("*.json")):
        try:
            g = json.loads(f.read_text(encoding="utf-8"))
            gen[g.get("id", f.stem)] = g
        except json.JSONDecodeError:
            print(f"  ! JSON invalide : {f.name}")
    vec, svd = m["vec"], m["svd"]
    km, clf, classes = m["km"], m["clf"], m["clf_classes"]
    Lq, Lc = m["Lq"], m["Lc"]
    results = []
    for pid, g in gen.items():
        plan = plans.get(pid)
        if not plan:
            continue
        plan_ex = {ex["numero"]: ex for ex in plan["exercices"]} if "exercices" in plan else {0: plan}
        for ex in g["exercices"]:
            pex = plan_ex.get(ex["numero"]) or next(iter(plan_ex.values()))
            pslots = {q["slot"]: q for q in pex["questions"]}
            qs = sorted(ex["questions"], key=lambda q: q["slot"])
            fake = {"id": pid, "type": "ecrit", "year": 2026, "center": "généré", "n_exercises": 3,
                    "exercises": [{"number": ex["numero"], "points": None, "theme_sentence": None,
                                   "preamble": ex["contexte"], "raw": ex["contexte"] + "\n" + "\n".join(q["enonce"] for q in qs),
                                   "questions": [{"label": str(q["slot"]), "text": q["enonce"],
                                                  "context_before": ex["contexte"][-400:] if plan["type"] in ("sujet", "inedit") else ""} for q in qs]}]}
            rows = F.build_question_table([fake])
            for r in rows:
                r["main"] = F.main_concepts(r)
            if not rows:
                continue
            texts = [r["text"] + "\n" + r["context"][-300:] for r in rows]
            X = vec.transform(texts)
            L = svd.transform(X)
            L /= np.linalg.norm(L, axis=1, keepdims=True) + 1e-9
            Xf, _ = F.feature_matrix(rows)
            stems = [" ".join(F.norm(r["text"]).split()[:18]) for r in rows]
            St = m["stem_svd"].transform(m["stem_vec"].transform(stems))
            Z = np.hstack([m["form_scaler"].transform(Xf[:, m["form_cols"]]), 3.0 * St / (np.linalg.norm(St, axis=1, keepdims=True) + 1e-9)])
            arch_pred = km.predict(Z)
            proba = clf.predict_proba(X)
            pos_pred = m["gb"].predict(np.hstack([Xf[:, m["gb_keep"]], L[:, :30]]))
            nov = (L @ Lq.T).max(1)
            grd = (L @ Lc.T).max(1)
            for i, (q, r) in enumerate(zip(qs, rows)):
                ps = pslots.get(q["slot"], {})
                target = ps.get("notion", q.get("notion"))
                top3 = [classes[j] for j in np.argsort(-proba[i])[:3]]
                a_plan = ps.get("archetype_id")
                info = m["arch_info"].get(a_plan, {}) if a_plan is not None else {}
                plan_task = info.get("taches", [[None]])[0][0]
                lvl_target = {"se souvenir": 1, "comprendre": 2, "appliquer": 3, "analyser": 4, "évaluer": 5, "créer": 6}.get(ps.get("bloom_cible"), None)
                pys = [python_ok(c) for c in code_blocks(q["reponse_attendue"])]
                pys = [p for p in pys if p is not None]
                sq = sql_ok(q["reponse_attendue"]) if target in ("sql", "modele_relationnel", "sgbd") else None
                results.append({
                    "id": pid, "type": plan["type"], "exercice": ex["numero"], "slot": q["slot"],
                    "notion": target, "notion_top3": top3,
                    "notion_ok": (target in top3) if target in classes else None,
                    "notion_lexique_ok": target in r["concepts"] or target in r["ex_concepts"],
                    "archetype_plan": a_plan, "archetype_predit": int(arch_pred[i]),
                    "archetype_ok": (int(arch_pred[i]) == a_plan) if a_plan is not None else None,
                    "tache_ok": (r["task"] == plan_task or m["arch_info"][int(arch_pred[i])]["taches"][0][0] == plan_task) if plan_task is not None else None,
                    "bloom_plan": lvl_target, "bloom_mesure": r["bloom"],
                    "bloom_ok": abs(r["bloom"] - lvl_target) <= 1 if lvl_target is not None else None,
                    "nouveaute_sim_max": round(float(nov[i]), 3), "quasi_copie": bool(nov[i] > 0.92),
                    "ancrage_cours": round(float(grd[i]), 3),
                    "python_ok": all(pys) if pys else None, "sql_ok": sq,
                    "position_cible": ps.get("position_cible"), "position_predite": round(float(pos_pred[i]), 3),
                })
                if plan["type"] == "inedit" and fm is not None:
                    fc = fm.facets(r["text"], r["context"])
                    c_plan, s_plan = ps.get("consigne_id"), ps.get("support_id")
                    pl = fm.plausibility(target, fc["consigne"], fc["support"], ps.get("position_bin", 1))
                    results[-1].update({
                        "mode": ps.get("mode"), "consigne_plan": c_plan, "consigne_mesuree": fc["consigne"],
                        "consigne_ok": fc["consigne"] == c_plan if c_plan is not None else None,
                        "consigne_top3_ok": fc["rang_consigne"][c_plan] < 3 if c_plan is not None else None,
                        "support_ok": fc["support"] == s_plan if s_plan is not None else None,
                        "support_top3_ok": fc["rang_support"][s_plan] < 3 if s_plan is not None else None,
                        "plausibilite_mesuree": round(pl, 3), "plausible": pl >= ref,
                        "combinaison_jamais_vue": (target, fc["consigne"], fc["support"]) not in obs,
                    })
    summary = summarize(results)
    (OUT / "validation.json").write_text(json.dumps({"resume": summary, "detail": results}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    return summary


def rate(rs, key):
    v = [r.get(key) for r in rs if r.get(key) is not None]
    return round(float(np.mean(v)), 3) if v else None


def summarize(results: list[dict]) -> dict:
    out = {"questions_validees": len(results)}
    for k in ("notion_ok", "notion_lexique_ok", "archetype_ok", "tache_ok", "bloom_ok", "python_ok", "sql_ok", "quasi_copie"):
        out[k] = rate(results, k)
    ined = [r for r in results if r["type"] == "inedit"]
    if ined:
        out["inedit"] = {"n": len(ined), **{k: rate(ined, k) for k in (
            "notion_ok", "notion_lexique_ok", "consigne_ok", "consigne_top3_ok", "support_ok", "support_top3_ok",
            "plausible", "combinaison_jamais_vue", "quasi_copie", "python_ok", "sql_ok")},
            "nouveaute_sim_max_moyenne": round(float(np.mean([r["nouveaute_sim_max"] for r in ined])), 3),
            "par_mode": {md: {"n": len(rs), "consigne_top3_ok": rate(rs, "consigne_top3_ok"), "notion_ok": rate(rs, "notion_ok")}
                         for md in {r["mode"] for r in ined} for rs in [[r for r in ined if r["mode"] == md]]}}
    out["nouveaute_sim_max_moyenne"] = round(float(np.mean([r["nouveaute_sim_max"] for r in results])), 3) if results else None
    out["ancrage_cours_moyen"] = round(float(np.mean([r["ancrage_cours"] for r in results])), 3) if results else None
    by_ex = defaultdict(list)
    for r in results:
        if r["type"] == "sujet" and r["position_cible"] is not None:
            by_ex[(r["id"], r["exercice"])].append(r)
    rhos = []
    for rs in by_ex.values():
        if len(rs) >= 4:
            rho = spearmanr([r["position_cible"] for r in rs], [r["position_predite"] for r in rs]).correlation
            if not np.isnan(rho):
                rhos.append(rho)
    out["difficulte_spearman_moyen"] = round(float(np.mean(rhos)), 3) if rhos else None
    per_type = defaultdict(list)
    for r in results:
        per_type[r["type"]].append(r)
    out["par_type"] = {t: {"n": len(rs), "notion_ok": rate(rs, "notion_ok"), "tache_ok": rate(rs, "tache_ok"), "bloom_ok": rate(rs, "bloom_ok")} for t, rs in per_type.items()}
    weak = defaultdict(list)
    for r in results:
        weak[r["notion"]].append(r["notion_ok"])
    out["notions_mal_reconnues"] = sorted(((n, round(float(np.mean([v for v in vs if v is not None])), 2)) for n, vs in weak.items() if any(v is not None for v in vs) and np.mean([v for v in vs if v is not None]) < 0.6), key=lambda t: t[1])
    return out


def render_markdown() -> None:
    """Fichier lisible : toutes les questions générées."""
    lines = ["# Questions générées (NSI Terminale)", ""]
    for f in sorted(GENERATED.glob("*.json")):
        g = json.loads(f.read_text(encoding="utf-8"))
        lines.append(f"## {g['id']}")
        for ex in g["exercices"]:
            if ex["numero"]:
                lines += [f"### Exercice {ex['numero']} — {ex['titre']}", "", ex["contexte"], ""]
            else:
                lines += [f"### {ex['titre']}", ""]
            for q in sorted(ex["questions"], key=lambda q: q["slot"]):
                lines += [f"**Q{q['slot']}** ({q['points']} pt, {q['notion']}) {q['enonce']}", "",
                          "<details><summary>Corrigé</summary>", "", q["reponse_attendue"], "", "</details>", ""]
    (OUT / "questions.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"[ok] {OUT / 'questions.md'}")

