#!/usr/bin/env bash
# Télécharge les annales (sujets + corrigés) 2021-2026 d'autres spécialités depuis sujetdebac.fr.
# Usage : scripts/fetch_matieres.sh [chemin_sujetdebac:nom ...]
set -uo pipefail
cd "$(dirname "$0")/../data/sources"
list=("$@")
[ ${#list[@]} -gt 0 ] || list=(
  specialites/spe-sciences-eco-sociales:ses
  specialites/spe-sciences-vie-terre:svt
  specialites/spe-physique-chimie:physique
  specialites/spe-mathematiques:maths
  specialites/spe-hg-geopolitique-sciences-po:hggsp
  specialites/spe-humanites-litterature-philo:hlp
  specialites/spe-sciences-ingenieur:si
  serie-stmg/spe-management-gestion-numerique:management
  serie-st2s/spe-sciences-sanitaires-sociales:sss
  serie-st2s/spe-chimie-bio-physiopat-humaines:cbph
  serie-sti2d/spe-2i2d-innovation-techno-eco:i2d
)
for e in "${list[@]}"; do
  path=${e%%:*}; name=${e##*:}; slug=${path##*/}
  mkdir -p "annales_$name"
  for y in 2021 2022 2023 2024 2025 2026; do
    curl -fsSL "https://www.sujetdebac.fr/annales/$path/$y/" \
      | grep -oE "/annales/[a-z0-9-]*$slug-$y-[a-z0-9-]+" | sort -u \
      | while read -r page; do
          curl -fsSL "https://www.sujetdebac.fr$page" | grep -oE "/annales-pdf/$y/[^\"']*\.pdf" | sort -u \
            | while read -r u; do
                f="annales_$name/$(basename "$u")"
                [ -s "$f" ] || curl -fsSL "https://www.sujetdebac.fr$u" -o "$f" || echo "! $u"
              done
        done
  done
  echo "ok $name ($(ls annales_$name | wc -l) PDF, $(du -sh annales_$name | cut -f1))"
done
