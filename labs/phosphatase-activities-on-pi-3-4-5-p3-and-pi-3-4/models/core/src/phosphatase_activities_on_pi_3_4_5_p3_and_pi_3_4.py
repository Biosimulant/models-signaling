# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Phosphatase activities on PI(3,4,5)P3 and PI(3,4)P2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class PhosphataseActivitiesOnPi345P3AndPi34Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1704190000'
    _TITLE = 'Phosphatase activities on PI(3,4,5)P3 and PI(3,4)P2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'egf': ('EGF',
             'native SBML value',
             'EGF. Maps to SBML symbol `EGF` and is emitted in native SBML units.'),
     'egfr': ('EGFR',
              'native SBML value',
              'EGFR. Maps to SBML symbol `EGFR` and is emitted in native SBML units.'),
     'egfr_p': ('EGFR_P',
                'native SBML value',
                'EGFR P. Maps to SBML symbol `EGFR_P` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_inpp4ab': ('INPP4AB',
                         1.0,
                         'native SBML value',
                         'Initial level of INPP4AB. Maps to SBML symbol `INPP4AB`; exposed as a '
                         'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_egf_sig_level': ('EGF_sig',
                               0.00157,
                               'native SBML value',
                               'EGF Sig source parameter. Maps to SBML symbol `EGF_sig` and preserves '
                               'the bundled default.'),
     'initial_for_egf_sig_level': ('ModelValue_13',
                                   0.00157,
                                   'native SBML value',
                                   'Initial For EGF Sig source parameter. Maps to SBML symbol '
                                   '`ModelValue_13` and preserves the bundled default.')}
    _SPECIES_LABELS = {'EGF': 'EGF',
     'EGFR': 'EGFR',
     'EGFR_P': 'EGFR P',
     'PI3Keff1': 'Pi3keff1',
     'PI_4_5_P2': 'PI 4 5 P2',
     'PI_3_4_5_P3': 'PI 3 4 5 P3',
     'PI_103_ext': 'PI 103 Ext',
     'PI_103_int': 'PI 103 Int',
     'PTEN': 'source-defined PTEN state',
     'PI_3_4_P2': 'PI 3 4 P2',
     'SHIP2': 'source-defined SHIP2 state',
     'INPP4AB': 'INPP4AB',
     'PI_3_P': 'PI 3 P',
     'PI_4_P': 'PI 4 P',
     'X': 'response node X',
     'mode_PI_103_diff': 'Mode PI 103 Diff',
     'Y': 'source-defined Y state',
     'PI_Y_P': 'source-defined PI(Y)P state'}
    _STATE_OUTPUT_ALIASES = {'EGF': 'egf',
     'EGFR': 'egfr',
     'EGFR_P': 'egfr_p',
     'PI3Keff1': 'pi3keff1',
     'PI_4_5_P2': 'pi_4_5_p2',
     'PI_3_4_5_P3': 'pi_3_4_5_p3',
     'PI_103_ext': 'pi_103_ext',
     'PI_103_int': 'pi_103_int',
     'PTEN': 'source_defined_pten_state',
     'PI_3_4_P2': 'pi_3_4_p2',
     'SHIP2': 'source_defined_ship2_state',
     'INPP4AB': 'inpp4ab',
     'PI_3_P': 'pi_3_p',
     'PI_4_P': 'pi_4_p',
     'X': 'response_node_x',
     'mode_PI_103_diff': 'mode_pi_103_diff',
     'Y': 'source_defined_y_state',
     'PI_Y_P': 'source_defined_pi_y_p_state'}

    def __init__(self, model_path: str = 'data/MODEL1704190000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


PhosphataseActivitiesOnPi345P3AndPi34Model1704190000Model = PhosphataseActivitiesOnPi345P3AndPi34Model
