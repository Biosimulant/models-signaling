# Sasagawa2005_MAPK

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000049`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000049.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `rasgap` maps to SBML `RasGAP`.
- `erk` maps to SBML `ERK`.
- `ras_gdp` maps to SBML `Ras_GDP`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
