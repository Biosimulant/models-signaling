# Hayashi1999_NOSynth_Phospho

Tellurium-backed Biosimulant core wrapper for `MODEL4780784080`.

Scientific source of truth:
- Bundled SBML file: `data/MODEL4780784080.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `nos_ca_camnnos` maps to SBML `NOS_slash_Ca_minus_CaMnNOS`.
- `nos_ca_camnnos_kenz_kenz_cplx` maps to SBML `NOS_slash_Ca_minus_CaMnNOS_slash_kenz_slash_kenz_cplx`.
- `nos_camkiv_kenz_kenz_cplx` maps to SBML `NOS_slash_CaMKIV_slash_kenz_slash_kenz_cplx`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
