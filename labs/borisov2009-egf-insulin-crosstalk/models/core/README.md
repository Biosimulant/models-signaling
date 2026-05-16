# Borisov2009_EGF_Insulin_Crosstalk

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000223`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000223.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `rasgap` maps to SBML `RasGAP`.
- `rp_rasgap` maps to SBML `Rp_RasGAP`.
- `irp_rasgap` maps to SBML `IRp_RasGAP`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
