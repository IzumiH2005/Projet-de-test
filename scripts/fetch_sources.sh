#!/usr/bin/env bash
# Télécharge les sources publiques (annales + cours NSI) dans data/sources/.
set -euo pipefail
cd "$(dirname "$0")/../data"
mkdir -p sources && cd sources
repos=(
  glassus/terminale_nsi          # cours Terminale NSI (Markdown) + annales écrit + BNS pratique
  trahobisoa/Terminale_NSI       # cours (PDF) + annales écrit 2021-2026 + pratique 2023
  Nota-yob/ECE-NSI-2024          # 48 sujets d'épreuve pratique 2024
)
for r in "${repos[@]}"; do
  d=$(echo "$r" | tr / _)
  [ -d "$d" ] || git clone -q --depth 1 "https://github.com/$r.git" "$d"
  echo "ok $r"
done

# Dépôts d'enseignants et banques d'exercices sur la Forge des communs numériques éducatifs
forge=(
  codex/codex.forge.apps.education.fr      # CodEx : ~350 exercices avec tags et difficulté
  projets-qcm/qcm-nsi-terminale            # banque de QCM de Terminale
  cours-nsi/terminale
  mcoilhac/term
  peio/cours-term
  nsi-clemenceau/nsi-terminale
  LDM_terminale/terminale
  sallardpa/terminale-nsi
  florian.picard/cours-terminale-nsi
)
for r in "${forge[@]}"; do
  d="forge_$(echo "$r" | tr / _)"
  [ -d "$d" ] || git clone -q --depth 1 --filter=blob:limit=3m "https://forge.apps.education.fr/$r.git" "$d" || echo "! $r"
  echo "ok forge $r"
done

# Sujets officiels 2021-2026 (sujetdebac.fr)
mkdir -p sujetdebac
for y in 2021 2022 2023 2024 2025 2026; do
  curl -fsSL "https://www.sujetdebac.fr/annales/specialites/spe-numerique-informatique/$y/" \
    | grep -oE "/annales/spe-numerique-informatique-$y-[a-z0-9-]+" | sort -u \
    | while read -r page; do
        curl -fsSL "https://www.sujetdebac.fr$page" | grep -oE "/annales-pdf/$y/[^\"']*sujet-officiel\.pdf" | sort -u \
          | while read -r u; do
              f="sujetdebac/$(basename "$u")"
              [ -s "$f" ] || curl -fsSL "https://www.sujetdebac.fr$u" -o "$f" || echo "! $u"
            done
      done
done
echo "ok sujetdebac ($(ls sujetdebac | wc -l) PDF)"

# Droit : annales STMG droit-économie (sujets + corrigés) et matière du cours
mkdir -p droit_stmg droit_cours
for y in 2021 2022 2023 2024 2025 2026; do
  curl -fsSL "https://www.sujetdebac.fr/annales/serie-stmg/spe-droit-economie/$y/" \
    | grep -oE "/annales/stmg-spe-droit-economie-$y-[a-z0-9-]+" | sort -u \
    | while read -r page; do
        curl -fsSL "https://www.sujetdebac.fr$page" | grep -oE "/annales-pdf/$y/[^\"']*\.pdf" | sort -u \
          | while read -r u; do
              f="droit_stmg/$(basename "$u")"
              [ -s "$f" ] || curl -fsSL "https://www.sujetdebac.fr$u" -o "$f" || echo "! $u"
            done
      done
done
echo "ok droit_stmg ($(ls droit_stmg | wc -l) PDF)"
# programmes et indications complémentaires Éduscol (1re, Tle)
for id in 25015 25021 25252; do
  [ -s "droit_cours/eduscol_$id.pdf" ] || curl -fsSL "https://eduscol.education.fr/document/$id/download" -o "droit_cours/eduscol_$id.pdf"
done
# codes en vigueur (tricoteuses.fr), puis : python scripts/build_droit_cours.py data/sources/codes
mkdir -p codes
for c in code_civil code_du_travail code_de_la_consommation code_de_commerce; do
  [ -d "codes/$c" ] || git clone -q --depth 1 "https://git.tricoteuses.fr/codes/$c.git" "codes/$c"
done
