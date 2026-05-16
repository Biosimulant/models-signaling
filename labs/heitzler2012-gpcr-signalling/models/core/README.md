# Heitzler2012 - GPCR signalling

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000842`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000842.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `erk` maps to SBML `ERK`.
- `gp_perk` maps to SBML `GpERK`.
- `b_perk` maps to SBML `bpERK`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
