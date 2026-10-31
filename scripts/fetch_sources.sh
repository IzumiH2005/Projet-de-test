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
