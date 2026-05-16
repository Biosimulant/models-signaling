# Vernoux2011_AuxinSignaling_AuxinSingleStepInput

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000351`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000351.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `aux_iaa` maps to SBML `I`.
- `arf` maps to SBML `A`.
- `aux_iaa_aux_iaa` maps to SBML `D_II`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
