# Nyman2012_InsulinSignalling

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000423`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000423.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `irins` maps to SBML `IRins`.
- `irp` maps to SBML `IRp`.
- `irip` maps to SBML `IRiP`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
