# Dupont1992_Ca_dpt_protein_phospho

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000113`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000113.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `phosphorylated_protein` maps to SBML `W_star`.
- `total_protein` maps to SBML `Wt`.
- `model_state_z` maps to SBML `Z`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
