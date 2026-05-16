# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Levchenko2000_MAPK_noScaffold."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Levchenko2000MapkNoscaffoldModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000011'
    _TITLE = 'Levchenko2000_MAPK_noScaffold'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'mapk': ('MAPK',
              'native SBML value',
              'MAPK. Maps to SBML symbol `MAPK` and is emitted in native SBML units.'),
     'mapk_mek_pp': ('MAPKMEKpp',
                     'native SBML value',
                     'MAPK MEK PP. Maps to SBML symbol `MAPKMEKpp` and is emitted in native SBML '
                     'units.'),
     'mapk_p': ('MAPKp',
                'native SBML value',
                'MAPK P. Maps to SBML symbol `MAPKp` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_mapk': ('MAPK',
                      0.0,
                      'native SBML value',
                      'Initial level of MAPK. Maps to SBML symbol `MAPK`; exposed as a traceable '
                      'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'MAPK': 'MAPK',
     'MAPKMEKpp': 'MAPK MEK PP',
     'MAPKp': 'MAPK P',
     'MAPKPH': 'MAPK Phosphatase',
     'MAPKpMAPKPH': 'MAPK P Mapkpase',
     'MAPKpMEKpp': 'MAPK P MEK PP',
     'MAPKpp': 'MAPK PP',
     'MAPKppMAPKPH': 'MAPK PP Mapkpase',
     'MEK': 'MEK',
     'MEKp': 'source-defined MEK-P state',
     'MEKPH': 'MEK Phosphatase',
     'MEKpMEKPH': 'MEK P Mekpase',
     'MEKpp': 'MEK PP',
     'MEKppMEKPH': 'MEK PP Mekpase',
     'MEKpRAFp': 'MEK P RAF P',
     'MEKRAFp': 'MEK RAF P',
     'RAF': 'RAF',
     'RAFK': 'source-defined RAFK state',
     'RAFp': 'source-defined RAF-P state',
     'RAFPH': 'RAF Phosphatase',
     'RAFpRAFPH': 'RAF P Rafpase',
     'RAFRAFK': 'RAF RAFK'}
    _STATE_OUTPUT_ALIASES = {'MAPK': 'mapk',
     'MAPKMEKpp': 'mapk_mek_pp',
     'MAPKp': 'mapk_p',
     'MAPKPH': 'mapk_phosphatase',
     'MAPKpMAPKPH': 'mapk_p_mapkpase',
     'MAPKpMEKpp': 'mapk_p_mek_pp',
     'MAPKpp': 'mapk_pp',
     'MAPKppMAPKPH': 'mapk_pp_mapkpase',
     'MEK': 'mek',
     'MEKp': 'source_defined_mek_p_state',
     'MEKPH': 'mek_phosphatase',
     'MEKpMEKPH': 'mek_p_mekpase',
     'MEKpp': 'mek_pp',
     'MEKppMEKPH': 'mek_pp_mekpase',
     'MEKpRAFp': 'mek_p_raf_p',
     'MEKRAFp': 'mek_raf_p',
     'RAF': 'raf',
     'RAFK': 'source_defined_rafk_state',
     'RAFp': 'source_defined_raf_p_state',
     'RAFPH': 'raf_phosphatase',
     'RAFpRAFPH': 'raf_p_rafpase',
     'RAFRAFK': 'raf_rafk'}

    def __init__(self, model_path: str = 'data/BIOMD0000000011.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Levchenko2000MapkNoscaffoldBiomd0000000011Model = Levchenko2000MapkNoscaffoldModel
