# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Kofahl2004_PheromonePathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kofahl2004PheromonepathwayModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000032'
    _TITLE = 'Kofahl2004_PheromonePathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ste2active': ('Ste2a',
                    'native SBML value',
                    'Ste2active. Maps to SBML symbol `Ste2a` and is emitted in native SBML units.'),
     'complex_c': ('complexC',
                   'native SBML value',
                   'Complex C. Maps to SBML symbol `complexC` and is emitted in native SBML units.'),
     'complex_d': ('complexD',
                   'native SBML value',
                   'Complex D. Maps to SBML symbol `complexD` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_source_defined_p_state': ('p',
                                        0.0,
                                        'native SBML value',
                                        'Initial level of source-defined P state. Maps to SBML symbol '
                                        '`p`; exposed as a traceable initial-condition perturbation.'),
     'initial_factor': ('alpha',
                        100.0,
                        'native SBML value',
                        'Initial level of Factor. Maps to SBML symbol `alpha`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'alpha': 'Factor',
     'Ste2': 'Source Defined STE2 State',
     'Ste2a': 'Ste2active',
     'Gabc': 'source-defined GΑΒΓ state',
     'GaGTP': 'source-defined GΑGTP state',
     'Gbc': 'source-defined GΒΓ state',
     'GaGDP': 'source-defined GΑGDP state',
     'complexC': 'Complex C',
     'complexD': 'Complex D',
     'Ste5': 'Source Defined STE5 State',
     'Ste11': 'STE11',
     'complexA': 'Complex A',
     'Ste7': 'Source Defined STE7 State',
     'Fus3': 'Source Defined FUS3 State',
     'complexB': 'Complex B',
     'Ste20': 'STE20',
     'complexE': 'Complex E',
     'complexF': 'Complex F',
     'complexG': 'Complex G',
     'complexH': 'Complex H',
     'complexI': 'Complex I',
     'complexL': 'Complex L',
     'Fus3PP': 'Fus3pp',
     'complexK': 'Complex K',
     'Ste12': 'STE12',
     'Ste12a': 'Ste12active',
     'Bar1': 'Source Defined BAR1 State',
     'Bar1a': 'Bar1active',
     'Bar1aex': 'Bar1active Ex',
     'Far1': 'Source Defined FAR1 State',
     'Far1PP': 'Far1pp',
     'Far1U': 'Far1ubiquitin',
     'complexM': 'Complex M',
     'complexN': 'Complex N',
     'Cdc28': 'CDC28',
     'Sst2': 'Source Defined SST2 State',
     'p': 'Source Defined P State'}
    _STATE_OUTPUT_ALIASES = {'alpha': 'factor',
     'Ste2': 'source_defined_ste2_state',
     'Ste2a': 'ste2active',
     'Gabc': 'source_defined_g_beta_state',
     'GaGTP': 'source_defined_g_gtp_state',
     'Gbc': 'source_defined_gbeta_state',
     'GaGDP': 'source_defined_g_gdp_state',
     'complexC': 'complex_c',
     'complexD': 'complex_d',
     'Ste5': 'source_defined_ste5_state',
     'Ste11': 'ste11',
     'complexA': 'complex_a',
     'Ste7': 'source_defined_ste7_state',
     'Fus3': 'source_defined_fus3_state',
     'complexB': 'complex_b',
     'Ste20': 'ste20',
     'complexE': 'complex_e',
     'complexF': 'complex_f',
     'complexG': 'complex_g',
     'complexH': 'complex_h',
     'complexI': 'complex_i',
     'complexL': 'complex_l',
     'Fus3PP': 'fus3pp',
     'complexK': 'complex_k',
     'Ste12': 'ste12',
     'Ste12a': 'ste12active',
     'Bar1': 'source_defined_bar1_state',
     'Bar1a': 'bar1active',
     'Bar1aex': 'bar1active_ex',
     'Far1': 'source_defined_far1_state',
     'Far1PP': 'far1pp',
     'Far1U': 'far1ubiquitin',
     'complexM': 'complex_m',
     'complexN': 'complex_n',
     'Cdc28': 'cdc28',
     'Sst2': 'source_defined_sst2_state',
     'p': 'source_defined_p_state'}

    def __init__(self, model_path: str = 'data/BIOMD0000000032.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kofahl2004PheromonepathwayBiomd0000000032Model = Kofahl2004PheromonepathwayModel
