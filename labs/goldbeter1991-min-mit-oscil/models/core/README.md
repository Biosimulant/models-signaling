# Goldbeter1991 - Min Mit Oscil

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000003`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000003.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `cyclin` maps to SBML `C`.
- `cdc_2_kinase` maps to SBML `M`.
- `cyclin_protease` maps to SBML `X`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
