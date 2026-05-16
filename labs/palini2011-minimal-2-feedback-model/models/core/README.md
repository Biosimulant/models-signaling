# Palini2011_Minimal_2_Feedback_Model

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000325`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000325.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `model_state_l` maps to SBML `L`.
- `model_state_r` maps to SBML `R`.
- `model_state_c` maps to SBML `C`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
