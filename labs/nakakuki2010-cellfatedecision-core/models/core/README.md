# Nakakuki2010_CellFateDecision_Core

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000251`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000251.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `pperk_nucleus` maps to SBML `ppERKn`.
- `pperk_cytosol` maps to SBML `ppERKc`.
- `dusp` maps to SBML `DUSP`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
