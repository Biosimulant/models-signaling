# Bachmann2011_JAK2-STAT5_FeedbackControl

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000347`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000347.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `stat5` maps to SBML `STAT5`.
- `pstat5` maps to SBML `pSTAT5`.
- `npstat5` maps to SBML `npSTAT5`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
