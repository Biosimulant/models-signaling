# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Brännmark2013 - Insulin signalling in human adipocytes (diabetic condition)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class BrNnmark2013InsulinSignallingInHumanAdipocBiomd0000000449Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000449'
    _TITLE = 'Brännmark2013 - Insulin signalling in human adipocytes (diabetic condition)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'phosphorylated_insulin_receptor': ('IRp',
                                         'native SBML value',
                                         'phosphorylated insulin receptor. Maps to SBML symbol `IRp` '
                                         'and is emitted in native SBML units.'),
     'insulin_bound_insulin_receptor': ('IRins',
                                        'native SBML value',
                                        'insulin-bound insulin receptor. Maps to SBML symbol `IRins` '
                                        'and is emitted in native SBML units.'),
     'internalized_phosphorylated_insulin_receptor': ('IRip',
                                                      'native SBML value',
                                                      'internalized phosphorylated insulin receptor. '
                                                      'Maps to SBML symbol `IRip` and is emitted in '
                                                      'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_insulin_level': ('insulin',
                               10.0,
                               'native SBML value',
                               'Insulin source parameter. Maps to SBML symbol `insulin` and preserves '
                               'the bundled default.'),
     'initial_scale_glucose_level': ('scaleGLUCOSE',
                                     0.04051,
                                     'native SBML value',
                                     'Scale GLUCOSE source parameter. Maps to SBML symbol '
                                     '`scaleGLUCOSE` and preserves the bundled default.')}
    _SPECIES_LABELS = {'IR': 'insulin receptor',
     'IRp': 'phosphorylated insulin receptor',
     'IRins': 'insulin-bound insulin receptor',
     'IRip': 'internalized phosphorylated insulin receptor',
     'IRi': 'internalized insulin receptor',
     'IRS1': 'source-defined IRS1 state',
     'IRS1p': 'Irs1p',
     'IRS1p307': 'Irs1p307',
     'IRS1307': 'IRS1307',
     'X': 'response node X',
     'Xp': 'phosphorylated response node X',
     'PKB': 'source-defined PKB state',
     'PKB308p': 'Pkb308p',
     'PKB473p': 'Pkb473p',
     'PKB308p473p': 'Pkb308p473p',
     'mTORC1': 'M TORC1',
     'mTORC1a': 'M Torc1a',
     'mTORC2': 'M TORC2',
     'mTORC2a': 'M Torc2a',
     'AS160': 'AS160',
     'AS160p': 'As160p',
     'GLUT4m': 'Glut4m',
     'GLUT4': 'source-defined GLUT4 state',
     'S6K': 'S6K',
     'S6Kp': 'S6kp',
     'S6': 'source-defined S6 state',
     'S6p': 'S6p'}
    _STATE_OUTPUT_ALIASES = {'IR': 'insulin_receptor',
     'IRp': 'phosphorylated_insulin_receptor',
     'IRins': 'insulin_bound_insulin_receptor',
     'IRip': 'internalized_phosphorylated_insulin_receptor',
     'IRi': 'internalized_insulin_receptor',
     'IRS1': 'source_defined_irs1_state',
     'IRS1p': 'irs1p',
     'IRS1p307': 'irs1p307',
     'IRS1307': 'irs1307',
     'X': 'response_node_x',
     'Xp': 'phosphorylated_response_node_x',
     'PKB': 'source_defined_pkb_state',
     'PKB308p': 'pkb308p',
     'PKB473p': 'pkb473p',
     'PKB308p473p': 'pkb308p473p',
     'mTORC1': 'm_torc1',
     'mTORC1a': 'm_torc1a',
     'mTORC2': 'm_torc2',
     'mTORC2a': 'm_torc2a',
     'AS160': 'as160',
     'AS160p': 'as160p',
     'GLUT4m': 'glut4m',
     'GLUT4': 'source_defined_glut4_state',
     'S6K': 's6k',
     'S6Kp': 's6kp',
     'S6': 'source_defined_s6_state',
     'S6p': 's6p'}

    def __init__(self, model_path: str = 'data/BIOMD0000000449.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


BrNnmark2013InsulinSignallingInHumanAdipocBiomd0000000449Model = BrNnmark2013InsulinSignallingInHumanAdipocBiomd0000000449Model
