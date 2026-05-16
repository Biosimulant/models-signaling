# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Fujita2010_Akt_Signalling_EGF."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fujita2010AktSignallingEgfModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000262'
    _TITLE = 'Fujita2010_Akt_Signalling_EGF'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'p_egfr_akt': ('pEGFR_Akt',
                    'native SBML value',
                    'P EGFR AKT. Maps to SBML symbol `pEGFR_Akt` and is emitted in native SBML units.'),
     'akt': ('Akt',
             'native SBML value',
             'AKT. Maps to SBML symbol `Akt` and is emitted in native SBML units.'),
     'source_defined_pakt_state': ('pAkt',
                                   'native SBML value',
                                   'source-defined PAKT state. Maps to SBML symbol `pAkt` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_egf_conc_impulse_level': ('EGF_conc_impulse',
                                        0.0,
                                        'ng_per_ml',
                                        'EGF Conc Impulse source parameter. Maps to SBML symbol '
                                        '`EGF_conc_impulse` and preserves the bundled default.'),
     'initial_egf_conc_ramp_level': ('EGF_conc_ramp',
                                     30.0,
                                     'ng_per_ml',
                                     'EGF Conc Ramp source parameter. Maps to SBML symbol '
                                     '`EGF_conc_ramp` and preserves the bundled default.'),
     'initial_egf_conc_step_level': ('EGF_conc_step',
                                     0.0,
                                     'ng_per_ml',
                                     'EGF Conc Step source parameter. Maps to SBML symbol '
                                     '`EGF_conc_step` and preserves the bundled default.')}
    _SPECIES_LABELS = {'EGF': 'EGF',
     'EGFR': 'EGFR',
     'pEGFR': 'P EGFR',
     'pEGFR_Akt': 'P EGFR AKT',
     'Akt': 'AKT',
     'pAkt': 'source-defined PAKT state',
     'S6': 'source-defined S6 state',
     'pAkt_S6': 'P AKT S6',
     'pS6': 'source-defined PS6 state',
     'pro_EGFR': 'Pro EGFR',
     'EGF_EGFR': 'EGF EGFR'}
    _STATE_OUTPUT_ALIASES = {'EGF': 'egf',
     'EGFR': 'egfr',
     'pEGFR': 'p_egfr',
     'pEGFR_Akt': 'p_egfr_akt',
     'Akt': 'akt',
     'pAkt': 'source_defined_pakt_state',
     'S6': 'source_defined_s6_state',
     'pAkt_S6': 'p_akt_s6',
     'pS6': 'source_defined_ps6_state',
     'pro_EGFR': 'pro_egfr',
     'EGF_EGFR': 'egf_egfr'}

    def __init__(self, model_path: str = 'data/BIOMD0000000262.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Fujita2010AktSignallingEgfBiomd0000000262Model = Fujita2010AktSignallingEgfModel
