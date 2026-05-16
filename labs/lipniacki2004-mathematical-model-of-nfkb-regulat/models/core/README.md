# Lipniacki2004 - Mathematical model of NFKB regulatory module

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000786`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000786.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `ikk_active` maps to SBML `IKK_active`.
- `ikkactive_ikb` maps to SBML `IKKactive_IkB`.
- `ikkactive_ikb_nfkb` maps to SBML `IKKactive_IkB_NFKB`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
