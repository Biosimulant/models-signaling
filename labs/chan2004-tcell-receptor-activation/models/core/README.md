# Chan2004_TCell_receptor_activation

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000120`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000120.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `inactive_lck` maps to SBML `lck_inactive`.
- `active_lck` maps to SBML `lck_active`.
- `inactive_phosphatase` maps to SBML `phosphatase_inactive`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
