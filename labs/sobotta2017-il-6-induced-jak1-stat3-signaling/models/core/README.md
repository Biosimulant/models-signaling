# Sobotta2017 - IL-6-induced JAK1-STAT3-signaling

Tellurium-backed Biosimulant core wrapper for `MODEL2307050001`.

Scientific source of truth:
- Bundled SBML file: `data/MODEL2307050001.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `unphosphorylated_receptor` maps to SBML `JAK1_gp130`.
- `phosphorylated_jak1_receptor` maps to SBML `pJAK1_gp130`.
- `active_receptor` maps to SBML `pJAK1_pgp130`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
