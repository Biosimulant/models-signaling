# Levchenko2000_MAPK_Scaffold

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000014`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000014.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `mapk_phosphatase` maps to SBML `MAPKP`.
- `mek_phosphatase` maps to SBML `MEKP`.
- `raf_phosphatase` maps to SBML `RAFP`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
