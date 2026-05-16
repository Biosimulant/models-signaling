# Becker2010_EpoR_CoreModel

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000271`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000271.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `epor` maps to SBML `EpoR`.
- `epo` maps to SBML `Epo`.
- `epo_epor` maps to SBML `Epo_EpoR`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
