# Hornberg2005 - MAPKsignalling

Tellurium-backed Biosimulant core wrapper for `BIOMD0000000667`.

Scientific source of truth:
- Bundled SBML file: `data/BIOMD0000000667.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `egf_egfri_2_gap_grb2_sos_ras_gdp` maps to SBML `_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GDP`.
- `egf_egfri_2_gap_grb2_sos_ras_gtp` maps to SBML `_EGF_EGFRi__2_GAP_Grb2_Sos_Ras_GTP`.
- `ras_gdp` maps to SBML `Ras_GDP`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
