# Becker2010_EpoR_AuxiliaryModel

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000272`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000272.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `epor` maps to SBML `EpoR`.
- `sav` maps to SBML `SAv`.
- `sav_epor` maps to SBML `SAv_EpoR`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
