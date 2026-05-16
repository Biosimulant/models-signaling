# Sneyd2002_IP3_Receptor

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000057`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000057.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `receptor` maps to SBML `R`.
- `open_state` maps to SBML `O`.
- `inactivated_state_1` maps to SBML `I1`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
