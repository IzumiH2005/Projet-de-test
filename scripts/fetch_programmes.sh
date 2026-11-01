#!/usr/bin/env bash
# Programmes officiels (Éduscol / copies du BO) des matières d'entraînement, puis cours markdown.
set -euo pipefail
cd "$(dirname "$0")/.."
D=data/sources/programmes; mkdir -p "$D"
e(){ echo "https://eduscol.education.fr/document/$1/download"; }
get(){ [ -s "$D/$1.pdf" ] || curl -sSL -o "$D/$1.pdf" "$2"; }
for id in 23152 23155 23281 23284 24565 24568 23647 23650 24328 24331 22492 25012 25009 25018 22906 22912 22900 22909 24916; do get $id "$(e $id)"; done
get phys1 https://www.snes.edu/IMG/pdf/physique_spe_annexe_1eg_bo.pdf
get phys_t "https://perso.ens-lyon.fr/fabrice.fourcade/Lec%cc%a7ons/Programmes%20chimie/PCtermgenerale.pdf.pdf"
b(){ n=$1; shift; rm -rf "data/$n/cours"; python scripts/build_cours_pdf.py "$n" "${@/#/$D/}"; }
b ses 23152.pdf 23155.pdf
b svt 23281.pdf 23284.pdf
b physique phys1.pdf phys_t.pdf
b maths 24565.pdf 24568.pdf
b hggsp 23647.pdf 23650.pdf
b hlp 24328.pdf 24331.pdf
b si 22492.pdf
b management 25012.pdf 25009.pdf 25018.pdf
b sss 22906.pdf 22912.pdf
b cbph 22900.pdf 22909.pdf
b i2d 24916.pdf
