# Kholodenko1999 - EGFR signaling

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000048`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000048.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `epidermal_growth_factor` maps to SBML `EGF`.
- `egfr` maps to SBML `R`.
- `egf_egfr` maps to SBML `Ra`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
