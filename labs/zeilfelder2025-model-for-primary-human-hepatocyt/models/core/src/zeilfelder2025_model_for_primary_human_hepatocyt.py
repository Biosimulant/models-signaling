# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Zeilfelder2025 - Model for primary human hepatocytes (PHH)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zeilfelder2025ModelForPrimaryHumanHepatocytModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL2503270002'
    _TITLE = 'Zeilfelder2025 - Model for primary human hepatocytes (PHH)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'inactive_receptor': ('JAK1_gp130',
                           'native SBML value',
                           'Inactive Receptor. Maps to SBML symbol `JAK1_gp130` and is emitted in '
                           'native SBML units.'),
     'total_phosphorylated_receptor': ('pJAK1_pgp130',
                                       'native SBML value',
                                       'Total Phosphorylated Receptor. Maps to SBML symbol '
                                       '`pJAK1_pgp130` and is emitted in native SBML units.'),
     'unphosphorylated_stat3': ('STAT3',
                                'native SBML value',
                                'Unphosphorylated STAT3. Maps to SBML symbol `STAT3` and is emitted in '
                                'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_input_apap_level': ('input_apap',
                                  0.0,
                                  'unit_0',
                                  'Input Apap source parameter. Maps to SBML symbol `input_apap` and '
                                  'preserves the bundled default.'),
     'initial_input_cyclo_level': ('input_cyclo',
                                   0.0,
                                   'native SBML value',
                                   'Input Cyclo source parameter. Maps to SBML symbol `input_cyclo` '
                                   'and preserves the bundled default.'),
     'initial_input_dcf_level': ('input_dcf',
                                 0.0,
                                 'unit_1',
                                 'Input Dcf source parameter. Maps to SBML symbol `input_dcf` and '
                                 'preserves the bundled default.')}
    _SPECIES_LABELS = {'JAK1_gp130': 'Inactive Receptor',
     'pJAK1_pgp130': 'Total Phosphorylated Receptor',
     'STAT3': 'Unphosphorylated STAT3',
     'cpSTAT3': 'active Cytoplasmic STAT3',
     'npSTAT3': 'active nuclear STAT3',
     'nSOCS3RNA1': 'SOCS3 Transcriptional Delay',
     'nSOCS3RNA2': 'SOCS3 Transcriptional Delay 2',
     'nSOCS3RNA3': 'SOCS3 Transcriptional Delay 3',
     'nSOCS3RNA4': 'SOCS3 Transcriptional Delay 4',
     'nSOCS3RNA5': 'SOCS3 Transcriptional Delay 5',
     'SOCS3RNA': 'SOCS3 M RNA',
     'SOCS3': 'SOCS3 Protein',
     'nHAMPRNA1': 'HAMP Transcriptional Delay',
     'nHAMPRNA2': 'HAMP Transcriptional Delay 2',
     'nHAMPRNA3': 'HAMP Transcriptional Delay 3',
     'nHAMPRNA4': 'HAMP Transcriptional Delay 4',
     'nHAMPRNA5': 'HAMP Transcriptional Delay 5',
     'nHAMPRNA6': 'HAMP Transcriptional Delay 6',
     'nHAMPRNA7': 'HAMP Transcriptional Delay 7',
     'HAMPRNA': 'HAMP M RNA'}
    _STATE_OUTPUT_ALIASES = {'JAK1_gp130': 'inactive_receptor',
     'pJAK1_pgp130': 'total_phosphorylated_receptor',
     'STAT3': 'unphosphorylated_stat3',
     'cpSTAT3': 'active_cytoplasmic_stat3',
     'npSTAT3': 'active_nuclear_stat3',
     'nSOCS3RNA1': 'socs3_transcriptional_delay',
     'nSOCS3RNA2': 'socs3_transcriptional_delay_2',
     'nSOCS3RNA3': 'socs3_transcriptional_delay_3',
     'nSOCS3RNA4': 'socs3_transcriptional_delay_4',
     'nSOCS3RNA5': 'socs3_transcriptional_delay_5',
     'SOCS3RNA': 'socs3_m_rna',
     'SOCS3': 'socs3_protein',
     'nHAMPRNA1': 'hamp_transcriptional_delay',
     'nHAMPRNA2': 'hamp_transcriptional_delay_2',
     'nHAMPRNA3': 'hamp_transcriptional_delay_3',
     'nHAMPRNA4': 'hamp_transcriptional_delay_4',
     'nHAMPRNA5': 'hamp_transcriptional_delay_5',
     'nHAMPRNA6': 'hamp_transcriptional_delay_6',
     'nHAMPRNA7': 'hamp_transcriptional_delay_7',
     'HAMPRNA': 'hamp_m_rna'}

    def __init__(self, model_path: str = 'data/MODEL2503270002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Zeilfelder2025ModelForPrimaryHumanHepatocytModel2503270002Model = Zeilfelder2025ModelForPrimaryHumanHepatocytModel
