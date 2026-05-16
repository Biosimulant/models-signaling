# Hoffmann2002_WT_IkBNFkB_Signaling

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000140`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000140.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `nfkb` maps to SBML `NFkB`.
- `ikbalpha_nfkb` maps to SBML `IkBalpha_NFkB`.
- `ikbbeta_nfkb` maps to SBML `IkBbeta_NFkB`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
