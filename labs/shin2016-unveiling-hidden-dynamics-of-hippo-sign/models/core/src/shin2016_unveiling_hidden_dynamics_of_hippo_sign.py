# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Shin2016 - Unveiling Hidden Dynamics of Hippo Signalling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shin2016UnveilingHiddenDynamicsOfHippoSignModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000832'
    _TITLE = 'Shin2016 - Unveiling Hidden Dynamics of Hippo Signalling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'akt': ('Akt',
             'native SBML value',
             'AKT. Maps to SBML symbol `Akt` and is emitted in native SBML units.'),
     'rassf1a': ('RASSF1A',
                 'native SBML value',
                 'RASSF1A. Maps to SBML symbol `RASSF1A` and is emitted in native SBML units.'),
     'a_mst2u_rassf1a': ('aMST2uRASSF1A',
                         'native SBML value',
                         'A Mst2u RASSF1A. Maps to SBML symbol `aMST2uRASSF1A` and is emitted in '
                         'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_a_egfr_level': ('aEGFR',
                              500.0,
                              'native SBML value',
                              'A EGFR source parameter. Maps to SBML symbol `aEGFR` and preserves the '
                              'bundled default.')}
    _SPECIES_LABELS = {'Akt': 'AKT',
     'RASSF1A': 'RASSF1A',
     'MST2': 'source-defined MST2 state',
     'dMST2': 'source-defined DMST2 state',
     'aMST2': 'source-defined AMST2 state',
     'aMST2uRASSF1A': 'A Mst2u RASSF1A',
     'MST2uRASSF1A': 'Mst2u RASSF1A',
     'iMST2': 'source-defined IMST2 state',
     'iRaf1uiMST2': 'I Raf1ui MST2',
     'aLATS1': 'A LATS1',
     'LATS1': 'source-defined LATS1 state',
     'iRaf1': 'source-defined IRAF1 state',
     'Raf1': 'RAF1',
     'aRaf1': 'source-defined ARAF1 state',
     'ipRaf1': 'Ip RAF1',
     'RasGDP': 'RAS GDP',
     'RasGTP': 'RAS GTP',
     'ERK': 'ERK',
     'ppERK': 'Pp ERK',
     'pAkt': 'source-defined PAKT state'}
    _STATE_OUTPUT_ALIASES = {'Akt': 'akt',
     'RASSF1A': 'rassf1a',
     'MST2': 'source_defined_mst2_state',
     'dMST2': 'source_defined_dmst2_state',
     'aMST2': 'source_defined_amst2_state',
     'aMST2uRASSF1A': 'a_mst2u_rassf1a',
     'MST2uRASSF1A': 'mst2u_rassf1a',
     'iMST2': 'source_defined_imst2_state',
     'iRaf1uiMST2': 'i_raf1ui_mst2',
     'aLATS1': 'a_lats1',
     'LATS1': 'source_defined_lats1_state',
     'iRaf1': 'source_defined_iraf1_state',
     'Raf1': 'raf1',
     'aRaf1': 'source_defined_araf1_state',
     'ipRaf1': 'ip_raf1',
     'RasGDP': 'ras_gdp',
     'RasGTP': 'ras_gtp',
     'ERK': 'erk',
     'ppERK': 'pp_erk',
     'pAkt': 'source_defined_pakt_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000832.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Shin2016UnveilingHiddenDynamicsOfHippoSignBiomd0000000832Model = Shin2016UnveilingHiddenDynamicsOfHippoSignModel
