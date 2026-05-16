# Kubota2012_InsulinAction_AKTpathway

Tellurium-backed Biosimulant core wrapper for `MODEL1204060000`.

Scientific source of truth:
- Bundled SBML file: `data/MODEL1204060000.xml`
- Equations, parameters, units, and initial values are not manually reimplemented.

Public headline outputs:
- `proir_complex` maps to SBML `proIR_complex`.
- `ir_complex` maps to SBML `IR_complex`.
- `p2ir_complex` maps to SBML `p2IR_complex`.

Caveat:
- Values are native SBML quantities; equations, parameters, and initial values remain in the bundled source file.
