# Pinto2022 - Hybrid SBML/ANN model

Tellurium-backed Biosimulant core wrapper for `MODEL2207280001`.

Scientific source of truth:
- Bundled SBML file: `data/MODEL2207280001.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `adp` maps to SBML `adp`.
- `asa` maps to SBML `asa`.
- `asp` maps to SBML `asp`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
