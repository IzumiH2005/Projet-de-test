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
