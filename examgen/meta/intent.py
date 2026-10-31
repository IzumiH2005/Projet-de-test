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
from sklearn.metrics import log_loss, roc_auc_score
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
