# Levchenko2000_MAPK_noScaffold

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000011`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000011.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `mapk` maps to SBML `MAPK`.
- `mapk_mek_pp` maps to SBML `MAPKMEKpp`.
- `mapk_p` maps to SBML `MAPKp`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
