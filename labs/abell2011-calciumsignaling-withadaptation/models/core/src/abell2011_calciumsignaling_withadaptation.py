# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Abell2011_CalciumSignaling_WithAdaptation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Abell2011CalciumsignalingWithadaptationModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000355'
    _TITLE = 'Abell2011_CalciumSignaling_WithAdaptation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'intracellular_calcium': ('CaI',
                               'native SBML value',
                               'intracellular calcium. Maps to SBML symbol `CaI` and is emitted in '
                               'native SBML units.'),
     'pmca_calcium_pump': ('mwaf195932_a72c_4552_8cf2_b349b15d39c4',
                           'native SBML value',
                           'PMCA calcium pump. Maps to SBML symbol '
                           '`mwaf195932_a72c_4552_8cf2_b349b15d39c4` and is emitted in native SBML '
                           'units.'),
     'serca_calcium_pump': ('mw0ebc76ad_49d7_4845_8f88_04d443fbe7f3',
                            'native SBML value',
                            'SERCA calcium pump. Maps to SBML symbol '
                            '`mw0ebc76ad_49d7_4845_8f88_04d443fbe7f3` and is emitted in native SBML '
                            'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_intracellular_calcium': ('CaI',
                                       0.0,
                                       'native SBML value',
                                       'Initial level of intracellular calcium. Maps to SBML symbol '
                                       '`CaI`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'CaI': 'intracellular calcium',
     'IP3': 'IP3',
     'g': 'source-defined G state',
     'mwaf195932_a72c_4552_8cf2_b349b15d39c4': 'PMCA calcium pump',
     'mw0ebc76ad_49d7_4845_8f88_04d443fbe7f3': 'SERCA calcium pump',
     'mw7cb2644a_384a_4bbb_93fd_fd686e01d7cb': 'STIM calcium sensor',
     'mwd6b792d8_c983_42c1_b3bc_2494d6a3363e': 'extracellular calcium',
     'mw013a7c64_a9ec_483c_b3b8_ed658337ee95': 'calmodulin',
     'CaS': 'stored calcium'}
    _STATE_OUTPUT_ALIASES = {'CaI': 'intracellular_calcium',
     'IP3': 'ip3',
     'g': 'source_defined_g_state',
     'mwaf195932_a72c_4552_8cf2_b349b15d39c4': 'pmca_calcium_pump',
     'mw0ebc76ad_49d7_4845_8f88_04d443fbe7f3': 'serca_calcium_pump',
     'mw7cb2644a_384a_4bbb_93fd_fd686e01d7cb': 'stim_calcium_sensor',
     'mwd6b792d8_c983_42c1_b3bc_2494d6a3363e': 'extracellular_calcium',
     'mw013a7c64_a9ec_483c_b3b8_ed658337ee95': 'calmodulin',
     'CaS': 'stored_calcium'}

    def __init__(self, model_path: str = 'data/BIOMD0000000355.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Abell2011CalciumsignalingWithadaptationBiomd0000000355Model = Abell2011CalciumsignalingWithadaptationModel
