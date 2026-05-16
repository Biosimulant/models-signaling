# Komarova2005_TheoreticalFramework_BasicArchitecture

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000125`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000125.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `model_state_x1` maps to SBML `x1`.
- `model_state_x2` maps to SBML `x2`.
- `model_state_y2` maps to SBML `y2`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
