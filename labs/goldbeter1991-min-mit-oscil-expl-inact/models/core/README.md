# Goldbeter1991 - Min Mit Oscil, Expl Inact

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000004`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000004.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `active_cdc_2_kinase` maps to SBML `M`.
- `active_cyclin_protease` maps to SBML `X`.
- `inactive_cdc_2_kinase` maps to SBML `MI`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
