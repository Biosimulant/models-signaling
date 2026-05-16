# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for DallePezze2012 - TSC-independent mTORC2 regulation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dallepezze2012TscIndependentMtorc2RegulationModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000581'
    _TITLE = 'DallePezze2012 - TSC-independent mTORC2 regulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'akt_p_t308': ('species_3',
                    'native SBML value',
                    'AKT P T308. Maps to SBML symbol `species_3` and is emitted in native SBML units.'),
     'pras40': ('species_9',
                'native SBML value',
                'PRAS40. Maps to SBML symbol `species_9` and is emitted in native SBML units.'),
     'pras40_p_s183': ('species_12',
                       'native SBML value',
                       'PRAS40 P S183. Maps to SBML symbol `species_12` and is emitted in native SBML '
                       'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_amino_acids': ('species_28',
                             100.0,
                             'native SBML value',
                             'Initial level of Amino Acids. Maps to SBML symbol `species_28`; exposed '
                             'as a traceable initial-condition perturbation.'),
     'initial_insulin': ('species_41',
                         100.0,
                         'native SBML value',
                         'Initial level of Insulin. Maps to SBML symbol `species_41`; exposed as a '
                         'traceable initial-condition perturbation.'),
     'initial_pi3k': ('species_23',
                      2.965,
                      'native SBML value',
                      'Initial level of PI3K. Maps to SBML symbol `species_23`; exposed as a traceable '
                      'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'species_20': 'insulin receptor beta response parameter',
     'species_21': 'insulin receptor beta response parameter P Y1146',
     'species_15': 'insulin receptor beta response parameter Refractory',
     'species_41': 'Insulin',
     'species_28': 'Amino Acids',
     'species_1': 'sink species',
     'species_5': 'M TORC2',
     'species_2': 'M TORC1 P S2448',
     'species_11': 'M TORC1',
     'species_19': 'IRS1 P S636 PI3K',
     'species_7': 'IRS1 P PI3K',
     'species_22': 'M TORC2 P S2481',
     'species_17': 'P70s6k P T389',
     'species_42': 'IRS1 PI3K',
     'species_3': 'AKT P T308',
     'species_6': 'TSC Clx',
     'species_9': 'PRAS40',
     'species_12': 'PRAS40 P S183',
     'species_10': 'PRAS40 P T246',
     'species_27': 'AKT',
     'species_4': 'AKT P T308 P S473',
     'species_47': 'P70s6k',
     'species_8': 'TSC P Clx',
     'species_13': 'source-defined PDK2 state',
     'species_14': 'PDK2 P',
     'species_16': 'PI3K Variant P',
     'species_18': 'PI3K Variant',
     'species_23': 'PI3K'}
    _STATE_OUTPUT_ALIASES = {'species_20': 'insulin_receptor_beta_response_parameter',
     'species_21': 'insulin_receptor_beta_response_parameter_p_y1146',
     'species_15': 'insulin_receptor_beta_response_parameter_refractory',
     'species_41': 'insulin',
     'species_28': 'amino_acids',
     'species_1': 'sink_species',
     'species_5': 'm_torc2',
     'species_2': 'm_torc1_p_s2448',
     'species_11': 'm_torc1',
     'species_19': 'irs1_p_s636_pi3k',
     'species_7': 'irs1_p_pi3k',
     'species_22': 'm_torc2_p_s2481',
     'species_17': 'p70s6k_p_t389',
     'species_42': 'irs1_pi3k',
     'species_3': 'akt_p_t308',
     'species_6': 'tsc_clx',
     'species_9': 'pras40',
     'species_12': 'pras40_p_s183',
     'species_10': 'pras40_p_t246',
     'species_27': 'akt',
     'species_4': 'akt_p_t308_p_s473',
     'species_47': 'p70s6k',
     'species_8': 'tsc_p_clx',
     'species_13': 'source_defined_pdk2_state',
     'species_14': 'pdk2_p',
     'species_16': 'pi3k_variant_p',
     'species_18': 'pi3k_variant',
     'species_23': 'pi3k'}

    def __init__(self, model_path: str = 'data/BIOMD0000000581.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Dallepezze2012TscIndependentMtorc2RegulationBiomd0000000581Model = Dallepezze2012TscIndependentMtorc2RegulationModel
