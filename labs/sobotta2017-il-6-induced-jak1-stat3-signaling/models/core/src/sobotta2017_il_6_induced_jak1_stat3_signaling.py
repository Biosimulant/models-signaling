# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Sobotta2017 - IL-6-induced JAK1-STAT3-signaling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sobotta2017Il6InducedJak1Stat3SignalingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2307050001'
    _TITLE = 'Sobotta2017 - IL-6-induced JAK1-STAT3-signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'unphosphorylated_receptor': ('JAK1_gp130',
                                   'nmol',
                                   'Unphosphorylated Receptor. Maps to SBML symbol `JAK1_gp130` and is '
                                   'emitted in native SBML units.'),
     'phosphorylated_jak1_receptor': ('pJAK1_gp130',
                                      'nmol',
                                      'Phosphorylated JAK1 Receptor. Maps to SBML symbol `pJAK1_gp130` '
                                      'and is emitted in native SBML units.'),
     'active_receptor': ('pJAK1_pgp130',
                         'nmol',
                         'active Receptor. Maps to SBML symbol `pJAK1_pgp130` and is emitted in native '
                         'SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_input_rux1_level': ('input_rux1',
                                  500.0,
                                  'nmolperL',
                                  'Input Rux1 source parameter. Maps to SBML symbol `input_rux1` and '
                                  'preserves the bundled default.'),
     'initial_input_rux2_level': ('input_rux2',
                                  187.0,
                                  'nmolperL',
                                  'Input Rux2 source parameter. Maps to SBML symbol `input_rux2` and '
                                  'preserves the bundled default.'),
     'initial_input_rux3_level': ('input_rux3',
                                  187.0,
                                  'nmolperL',
                                  'Input Rux3 source parameter. Maps to SBML symbol `input_rux3` and '
                                  'preserves the bundled default.')}
    _SPECIES_LABELS = {'JAK1_gp130': 'Unphosphorylated Receptor',
     'pJAK1_gp130': 'Phosphorylated JAK1 Receptor',
     'pJAK1_pgp130': 'active Receptor',
     'STAT3': 'Unphosphorylated Cytoplasmic STAT3',
     'tpSTAT3': 'Phosphorylated STAT3',
     'nSTAT3': 'Unphosphorylated nuclear STAT3',
     'nSOCS3RNA1': 'SOCS3 Transcriptional Delay',
     'nSOCS3RNA2': 'SOCS3 Transcriptional Delay',
     'nSOCS3RNA3': 'SOCS3 Transcriptional Delay',
     'nSOCS3RNA4': 'SOCS3 Transcriptional Delay',
     'nSOCS3RNA5': 'SOCS3 Transcriptional Delay',
     'SOCS3RNA': 'SOCS3 M RNA',
     'SOCS3': 'SOCS3 Protein',
     'nIL33RNA1': 'IL33 Transcriptional Delay',
     'nIL33RNA2': 'IL33 Transcriptional Delay',
     'nIL33RNA3': 'IL33 Transcriptional Delay',
     'nIL33RNA4': 'IL33 Transcriptional Delay',
     'nIL33RNA5': 'IL33 Transcriptional Delay',
     'nCXCL10RNA1': 'CXCL10 Transcriptional Delay',
     'nCXCL10RNA2': 'CXCL10 Transcriptional Delay',
     'nCXCL10RNA3': 'CXCL10 Transcriptional Delay',
     'nFGGRNA1': 'FGG Transcriptional Delay',
     'nFGGRNA2': 'FGG Transcriptional Delay',
     'nFGGRNA3': 'FGG Transcriptional Delay',
     'nFGGRNA4': 'FGG Transcriptional Delay',
     'nFGGRNA5': 'FGG Transcriptional Delay',
     'nHPRNA1': 'HP Transcriptional Delay',
     'nHPXRNA1': 'HPX Transcriptional Delay',
     'CXCL10RNA': 'CXCL10 M RNA',
     'FGGRNA': 'FGG M RNA',
     'HAMPRNA': 'HAMP M RNA',
     'IL33RNA': 'IL33 M RNA',
     'APCSRNA': 'APCS M RNA',
     'HPRNA': 'HP M RNA',
     'HPXRNA': 'HPX M RNA'}
    _STATE_OUTPUT_ALIASES = {'JAK1_gp130': 'unphosphorylated_receptor',
     'pJAK1_gp130': 'phosphorylated_jak1_receptor',
     'pJAK1_pgp130': 'active_receptor',
     'STAT3': 'unphosphorylated_cytoplasmic_stat3',
     'tpSTAT3': 'phosphorylated_stat3',
     'nSTAT3': 'unphosphorylated_nuclear_stat3',
     'nSOCS3RNA1': 'socs3_transcriptional_delay',
     'nSOCS3RNA2': 'socs3_transcriptional_delay_2',
     'nSOCS3RNA3': 'socs3_transcriptional_delay_3',
     'nSOCS3RNA4': 'socs3_transcriptional_delay_4',
     'nSOCS3RNA5': 'socs3_transcriptional_delay_5',
     'SOCS3RNA': 'socs3_m_rna',
     'SOCS3': 'socs3_protein',
     'nIL33RNA1': 'il33_transcriptional_delay',
     'nIL33RNA2': 'il33_transcriptional_delay_2',
     'nIL33RNA3': 'il33_transcriptional_delay_3',
     'nIL33RNA4': 'il33_transcriptional_delay_4',
     'nIL33RNA5': 'il33_transcriptional_delay_5',
     'nCXCL10RNA1': 'cxcl10_transcriptional_delay',
     'nCXCL10RNA2': 'cxcl10_transcriptional_delay_2',
     'nCXCL10RNA3': 'cxcl10_transcriptional_delay_3',
     'nFGGRNA1': 'fgg_transcriptional_delay',
     'nFGGRNA2': 'fgg_transcriptional_delay_2',
     'nFGGRNA3': 'fgg_transcriptional_delay_3',
     'nFGGRNA4': 'fgg_transcriptional_delay_4',
     'nFGGRNA5': 'fgg_transcriptional_delay_5',
     'nHPRNA1': 'hp_transcriptional_delay',
     'nHPXRNA1': 'hpx_transcriptional_delay',
     'CXCL10RNA': 'cxcl10_m_rna',
     'FGGRNA': 'fgg_m_rna',
     'HAMPRNA': 'hamp_m_rna',
     'IL33RNA': 'il33_m_rna',
     'APCSRNA': 'apcs_m_rna',
     'HPRNA': 'hp_m_rna',
     'HPXRNA': 'hpx_m_rna'}

    def __init__(self, model_path: str = 'data/MODEL2307050001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Sobotta2017Il6InducedJak1Stat3SignalingModel2307050001Model = Sobotta2017Il6InducedJak1Stat3SignalingModel
