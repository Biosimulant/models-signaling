# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Huarat2016 -Starvation-induced Ser/Thr protein kinase ArnS (Saci_1181) (Model 14)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Huarat2016StarvationInducedSerThrProteinKiModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1607210000'
    _TITLE = 'Huarat2016 -Starvation-induced Ser/Thr protein kinase ArnS (Saci_1181) (Model 14)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_nfb_state': ('nFB',
                                  'native SBML value',
                                  'source-defined NFB state. Maps to SBML symbol `nFB` and is emitted '
                                  'in native SBML units.'),
     'source_defined_nfb2_state': ('nFB2',
                                   'native SBML value',
                                   'source-defined NFB2 state. Maps to SBML symbol `nFB2` and is '
                                   'emitted in native SBML units.'),
     'source_defined_arns_state': ('saci1181',
                                   'native SBML value',
                                   'source-defined ARNS state. Maps to SBML symbol `saci1181` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_arns_state': ('saci1181',
                                           0.0,
                                           'native SBML value',
                                           'Initial level of source-defined ARNS state. Maps to SBML '
                                           'symbol `saci1181`; exposed as a traceable '
                                           'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'saci1181': 'source-defined ARNS state',
     'Saci1181': 'source-defined ARNS state',
     'arnR': 'source-defined ARNR state',
     'ArnR': 'source-defined ARNR state',
     'nFB': 'source-defined NFB state',
     'flaB': 'source-defined FLAB state',
     'AbfR_P': 'Abf R P',
     'AbfR': 'source-defined ABFR state',
     'FlaB': 'source-defined FLAB state',
     'nFB2': 'source-defined NFB2 state'}
    _STATE_OUTPUT_ALIASES = {'saci1181': 'source_defined_arns_state',
     'Saci1181': 'source_defined_arns_state_2',
     'arnR': 'source_defined_arnr_state',
     'ArnR': 'source_defined_arnr_state_2',
     'nFB': 'source_defined_nfb_state',
     'flaB': 'source_defined_flab_state',
     'AbfR_P': 'abf_r_p',
     'AbfR': 'source_defined_abfr_state',
     'FlaB': 'source_defined_flab_state_2',
     'nFB2': 'source_defined_nfb2_state'}

    def __init__(self, model_path: str = 'data/MODEL1607210000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Huarat2016StarvationInducedSerThrProteinKiModel1607210000Model = Huarat2016StarvationInducedSerThrProteinKiModel
