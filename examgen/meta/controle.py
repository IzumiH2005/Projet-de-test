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
