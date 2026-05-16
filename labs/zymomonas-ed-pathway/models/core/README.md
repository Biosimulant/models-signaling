# Zymomonas ED Pathway

Tellurium-backed Biosimulant core wrapper for `MODEL2008060001`.

Scientific source of truth:
- Bundled SBML file: `data/MODEL2008060001.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `ethanolex` maps to SBML `ETHANOLex`.
- `glucex` maps to SBML `GLUCex`.
- `pyrex` maps to SBML `PYRex`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
