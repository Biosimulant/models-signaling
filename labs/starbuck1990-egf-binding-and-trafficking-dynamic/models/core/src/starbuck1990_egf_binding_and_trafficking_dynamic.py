# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Starbuck1990 - EGF binding and trafficking dynamics in Fibroblast."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Starbuck1990EgfBindingAndTraffickingDynamicModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2003190005'
    _TITLE = 'Starbuck1990 - EGF binding and trafficking dynamics in Fibroblast'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _STATE_OUTPUT_ALIASES = {'Lo': 'source_defined_lo_state',
     'Rs': 'source_defined_rs_state',
     'Rii': 'source_defined_rii_state',
     'Ric': 'source_defined_ric_state',
     'Ts': 'source_defined_ts_state',
     'Ti': 'source_defined_ti_state',
     'Ps': 'source_defined_ps_state',
     'Pi': 'source_defined_pi_state',
     'Lii': 'source_defined_lii_state',
     'Cii': 'source_defined_cii_state',
     'Lic': 'source_defined_lic_state',
     'Cs': 'source_defined_cs_state',
     'Cic': 'source_defined_cic_state'}
    _SPECIES_LABELS = {'Lo': 'Source Defined LO State',
     'Rs': 'Source Defined RS State',
     'Rii': 'Source Defined RII State',
     'Ric': 'Source Defined RIC State',
     'Ts': 'Source Defined TS State',
     'Ti': 'Source Defined TI State',
     'Ps': 'Source Defined PS State',
     'Pi': 'Source Defined PI State',
     'Lii': 'Source Defined LII State',
     'Cii': 'Source Defined CII State',
     'Lic': 'Source Defined LIC State',
     'Cs': 'Source Defined CS State',
     'Cic': 'Source Defined CIC State'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_lo_state': ('Lo',
                                         0.0,
                                         'native SBML value',
                                         'Initial level of source-defined LO state. Maps to SBML '
                                         'symbol `Lo`; exposed as a traceable initial-condition '
                                         'perturbation.')}
    _HEADLINE_OUTPUTS = {'source_defined_rii_state': ('Rii',
                                  'native SBML value',
                                  'source-defined RII state. Maps to SBML symbol `Rii` and is emitted '
                                  'in native SBML units.'),
     'source_defined_ric_state': ('Ric',
                                  'native SBML value',
                                  'source-defined RIC state. Maps to SBML symbol `Ric` and is emitted '
                                  'in native SBML units.'),
     'source_defined_lii_state': ('Lii',
                                  'native SBML value',
                                  'source-defined LII state. Maps to SBML symbol `Lii` and is emitted '
                                  'in native SBML units.')}

    def __init__(self, model_path: str = 'data/MODEL2003190005.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Starbuck1990EgfBindingAndTraffickingDynamicModel2003190005Model = Starbuck1990EgfBindingAndTraffickingDynamicModel
