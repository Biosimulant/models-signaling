# Lee2008 - ERK and PI3K signal integration by Myc

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000818`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000818.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `akt` maps to SBML `AKT`.
- `aktp` maps to SBML `AKTp`.
- `erk` maps to SBML `ERK`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
