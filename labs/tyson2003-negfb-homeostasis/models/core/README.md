# Tyson2003_NegFB_Homeostasis

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000309`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000309.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `model_state_r` maps to SBML `R`.
- `model_state_s` maps to SBML `S`.
- `model_state_ep` maps to SBML `Ep`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
