# Zeilfelder2025 - Model for primary human hepatocytes (PHH)

Tellurium-backed Biosimulant core wrapper for `MODEL2503270002`.

Scientific source of truth:
- Bundled SBML file: `data/MODEL2503270002.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `inactive_receptor` maps to SBML `JAK1_gp130`.
- `total_phosphorylated_receptor` maps to SBML `pJAK1_pgp130`.
- `unphosphorylated_stat3` maps to SBML `STAT3`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
