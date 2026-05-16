# Nakakuki2010_CellFateDecision_Mechanistic

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000250`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000250.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `erk_c` maps to SBML `ERK_c`.
- `perk_c` maps to SBML `pERK_c`.
- `pperk_c` maps to SBML `ppERK_c`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
