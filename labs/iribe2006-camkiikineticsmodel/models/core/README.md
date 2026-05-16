# Iribe2006_CaMKIIkineticsModel

Tellurium-backed Biosimulant core wrapper for `MODEL1006230085`.

Scientific source of truth:
- Bundled SBML file: `data/MODEL1006230085.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `f_camk` maps to SBML `F_CaMK`.
- `f_srca_ryr` maps to SBML `F_SRCa_RyR`.
- `cmdn_ca` maps to SBML `Cmdn_Ca`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
