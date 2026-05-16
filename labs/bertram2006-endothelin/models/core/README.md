# Bertram2006_Endothelin

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000128`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000128.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `cytosolic_calcium_concentration` maps to SBML `c`.
- `er_calcium_concentration` maps to SBML `cer`.
- `camp` maps to SBML `cAMP`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
