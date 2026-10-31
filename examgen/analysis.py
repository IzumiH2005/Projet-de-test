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
        M = np.full((len(F.CONCEPT_NAMES), k), 0.3)
        ci = {c: i for i, c in enumerate(F.CONCEPT_NAMES)}
        for r in self.rows:
            for w, c in zip((1.0, 0.5), r["main"][:2]):
                M[ci[c], r["arch"]] += w
        P = M / M.sum(1, keepdims=True)
        prior = np.bincount([r["arch"] for r in self.rows], minlength=k) / len(self.rows)
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
        clf.fit(Xt, Y[:, cols])
        self.clf, self.clf_classes = clf, [c for c, k in zip(F.CONCEPT_NAMES, cols) if k]
        self.report["classifieur_notions"] = {"top3_hit_rate_cv": round(float(hit), 3), "micro_f1_cv": round(float(f1), 3), "notions": len(self.clf_classes)}

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
