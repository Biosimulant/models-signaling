# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Fujita2010_Akt_Signalling_NGF."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fujita2010AktSignallingNgfModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000263'
    _TITLE = 'Fujita2010_Akt_Signalling_NGF'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'p_trk_a_akt': ('pTrkA_Akt',
                     'native SBML value',
                     'P Trk A AKT. Maps to SBML symbol `pTrkA_Akt` and is emitted in native SBML '
                     'units.'),
     'akt': ('Akt',
             'native SBML value',
             'AKT. Maps to SBML symbol `Akt` and is emitted in native SBML units.'),
     'source_defined_pakt_state': ('pAkt',
                                   'native SBML value',
                                   'source-defined PAKT state. Maps to SBML symbol `pAkt` and is '
                                   'emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_nerve_growth_factor': ('NGF',
                                     0.0,
                                     'ng',
                                     'Initial level of nerve growth factor. Maps to SBML symbol `NGF`; '
                                     'exposed as a traceable initial-condition perturbation.'),
     'initial_pro_trk_a': ('pro_TrkA',
                           8.52065090518276,
                           'native SBML value',
                           'Initial level of Pro Trk A. Maps to SBML symbol `pro_TrkA`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_p_akt_scale_factor_level': ('pAkt_scaleFactor',
                                          2.42381211094508,
                                          'ng',
                                          'P AKT Scale Factor source parameter. Maps to SBML symbol '
                                          '`pAkt_scaleFactor` and preserves the bundled default.')}
    _SPECIES_LABELS = {'NGF': 'nerve growth factor',
     'TrkA': 'source-defined TRKA state',
     'pTrkA': 'P Trk A',
     'pTrkA_Akt': 'P Trk A AKT',
     'Akt': 'AKT',
     'pAkt': 'source-defined PAKT state',
     'S6': 'source-defined S6 state',
     'pAkt_S6': 'P AKT S6',
     'pS6': 'source-defined PS6 state',
     'pro_TrkA': 'Pro Trk A',
     'NGF_TrkA': 'nerve growth factor Trk A'}
    _STATE_OUTPUT_ALIASES = {'NGF': 'nerve_growth_factor',
     'TrkA': 'source_defined_trka_state',
     'pTrkA': 'p_trk_a',
     'pTrkA_Akt': 'p_trk_a_akt',
     'Akt': 'akt',
     'pAkt': 'source_defined_pakt_state',
     'S6': 'source_defined_s6_state',
     'pAkt_S6': 'p_akt_s6',
     'pS6': 'source_defined_ps6_state',
     'pro_TrkA': 'pro_trk_a',
     'NGF_TrkA': 'nerve_growth_factor_trk_a'}

    def __init__(self, model_path: str = 'data/BIOMD0000000263.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Fujita2010AktSignallingNgfBiomd0000000263Model = Fujita2010AktSignallingNgfModel
