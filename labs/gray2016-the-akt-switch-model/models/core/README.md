# Gray2016 - The Akt switch model

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000854`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000854.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `model_state_ac` maps to SBML `Ac`.
- `model_state_pc` maps to SBML `Pc`.
- `model_state_ap` maps to SBML `Ap`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
