# PetelenzKuehn_osmoadaptation_hog1D

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000606`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000606.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `glycerol_i` maps to SBML `glycerol_i`.
- `cin` maps to SBML `cin`.
- `glucose_i` maps to SBML `glucose_i`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
