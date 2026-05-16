# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Lee2008 - ERK and PI3K signal integration by Myc."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lee2008ErkAndPi3kSignalIntegrationByMycModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000818'
    _TITLE = 'Lee2008 - ERK and PI3K signal integration by Myc'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'akt': ('AKT',
             'native SBML value',
             'AKT. Maps to SBML symbol `AKT` and is emitted in native SBML units.'),
     'phosphorylated_akt': ('AKTp',
                            'native SBML value',
                            'phosphorylated AKT. Maps to SBML symbol `AKTp` and is emitted in native '
                            'SBML units.'),
     'erk': ('ERK',
             'native SBML value',
             'ERK. Maps to SBML symbol `ERK` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_myc_transcription_factor_total': ('Myc_total',
                                                0.0,
                                                'native SBML value',
                                                'Initial level of MYC transcription factor Total. Maps '
                                                'to SBML symbol `Myc_total`; exposed as a traceable '
                                                'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'Myc': 'MYC transcription factor',
     'AKT': 'AKT',
     'AKTp': 'phosphorylated AKT',
     'PI3K': 'PI3K',
     'GSK3B': 'GSK3B',
     'GSK3Bp': 'Gsk3bp',
     'ERK': 'ERK',
     'Myc_ser62': 'MYC transcription factor Ser62',
     'Myc_thr58': 'MYC transcription factor Thr58',
     'GF': 'source-defined GF state',
     'Myc_total': 'MYC transcription factor Total'}
    _STATE_OUTPUT_ALIASES = {'Myc': 'myc_transcription_factor',
     'AKT': 'akt',
     'AKTp': 'phosphorylated_akt',
     'PI3K': 'pi3k',
     'GSK3B': 'gsk3b',
     'GSK3Bp': 'gsk3bp',
     'ERK': 'erk',
     'Myc_ser62': 'myc_transcription_factor_ser62',
     'Myc_thr58': 'myc_transcription_factor_thr58',
     'GF': 'source_defined_gf_state',
     'Myc_total': 'myc_transcription_factor_total'}

    def __init__(self, model_path: str = 'data/BIOMD0000000818.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Lee2008ErkAndPi3kSignalIntegrationByMycBiomd0000000818Model = Lee2008ErkAndPi3kSignalIntegrationByMycModel
