# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for PetelenzKuehn_osmoadaptation_hog1D."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class PetelenzkuehnOsmoadaptationHog1dModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000606'
    _TITLE = 'PetelenzKuehn_osmoadaptation_hog1D'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'glycerol_i': ('glycerol_i',
                    'native SBML value',
                    'Glycerol I. Maps to SBML symbol `glycerol_i` and is emitted in native SBML '
                    'units.'),
     'intracellular_concentration_input': ('cin',
                                           'native SBML value',
                                           'intracellular concentration input. Maps to SBML symbol '
                                           '`cin` and is emitted in native SBML units.'),
     'glucose_i': ('glucose_i',
                   'native SBML value',
                   'Glucose I. Maps to SBML symbol `glucose_i` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_e': ('glucose_e',
                           0.116231,
                           'native SBML value',
                           'Initial level of Glucose E. Maps to SBML symbol `glucose_e`; exposed as a '
                           'traceable initial-condition perturbation.'),
     'initial_glucose_i': ('glucose_i',
                           1.31176,
                           'native SBML value',
                           'Initial level of Glucose I. Maps to SBML symbol `glucose_i`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_t_stress_level': ('t_stress',
                                3600.0,
                                'native SBML value',
                                'T Stress source parameter. Maps to SBML symbol `t_stress` and '
                                'preserves the bundled default.')}
    _SPECIES_LABELS = {'glycerol_i': 'Glycerol I',
     'cin': 'intracellular concentration input',
     'glucose_i': 'Glucose I',
     'G6P': 'G6P',
     'trehalose': 'Trehalose',
     'F16DP': 'F16DP',
     'F26DP': 'F26DP',
     'trioseP': 'Triose P',
     'Gpd1': 'source-defined GPD1 state',
     'pyruvate': 'Pyruvate',
     'acetate_i': 'Acetate I',
     'ethanol_i': 'Ethanol I',
     'Hog1': 'source-defined HOG1 state',
     'Hog1PP': 'Hog1pp',
     'Pfk2627a': 'Pfk2627a',
     'Pfk2627i': 'Pfk2627i',
     'AOG': 'source-defined AOG state',
     'gpd1mRNA': 'Gpd1m RNA',
     'stl1mRNA': 'Stl1m RNA',
     'Stl1': 'source-defined STL1 state',
     'AOGi': 'source-defined AOGI state',
     'Fps1r': 'Fps1r',
     'biomass': 'Biomass',
     'cellvol': 'Cellvol',
     'glycerol_e': 'Glycerol E',
     'glucose_e': 'Glucose E',
     'acetate_e': 'Acetate E',
     'ethanol_e': 'Ethanol E',
     'trehalose_e': 'Trehalose E'}
    _STATE_OUTPUT_ALIASES = {'glycerol_i': 'glycerol_i',
     'cin': 'intracellular_concentration_input',
     'glucose_i': 'glucose_i',
     'G6P': 'g6p',
     'trehalose': 'trehalose',
     'F16DP': 'f16dp',
     'F26DP': 'f26dp',
     'trioseP': 'triose_p',
     'Gpd1': 'source_defined_gpd1_state',
     'pyruvate': 'pyruvate',
     'acetate_i': 'acetate_i',
     'ethanol_i': 'ethanol_i',
     'Hog1': 'source_defined_hog1_state',
     'Hog1PP': 'hog1pp',
     'Pfk2627a': 'pfk2627a',
     'Pfk2627i': 'pfk2627i',
     'AOG': 'source_defined_aog_state',
     'gpd1mRNA': 'gpd1m_rna',
     'stl1mRNA': 'stl1m_rna',
     'Stl1': 'source_defined_stl1_state',
     'AOGi': 'source_defined_aogi_state',
     'Fps1r': 'fps1r',
     'biomass': 'biomass',
     'cellvol': 'cellvol',
     'glycerol_e': 'glycerol_e',
     'glucose_e': 'glucose_e',
     'acetate_e': 'acetate_e',
     'ethanol_e': 'ethanol_e',
     'trehalose_e': 'trehalose_e'}

    def __init__(self, model_path: str = 'data/BIOMD0000000606.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


PetelenzkuehnOsmoadaptationHog1dBiomd0000000606Model = PetelenzkuehnOsmoadaptationHog1dModel
