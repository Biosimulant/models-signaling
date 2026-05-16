# Hettling2011_CreatineKinase

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000408`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000408.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `adpi` maps to SBML `ADPi`.
- `atpi` maps to SBML `ATPi`.
- `cri` maps to SBML `Cri`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
