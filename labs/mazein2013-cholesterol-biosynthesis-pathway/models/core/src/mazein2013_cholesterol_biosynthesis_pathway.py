# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Mazein2013 - Cholesterol biosynthesis pathway."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mazein2013CholesterolBiosynthesisPathwayModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1409170000'
    _TITLE = 'Mazein2013 - Cholesterol biosynthesis pathway'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_acat2_state': ('s80',
                                    'native SBML value',
                                    'source-defined ACAT2 state. Maps to SBML symbol `s80` and is '
                                    'emitted in native SBML units.'),
     'acety_co_a': ('s1',
                    'native SBML value',
                    'Acety Co A. Maps to SBML symbol `s1` and is emitted in native SBML units.'),
     'acetoacetyl_co_a': ('s2',
                          'native SBML value',
                          'Acetoacetyl Co A. Maps to SBML symbol `s2` and is emitted in native SBML '
                          'units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_acety_co_a': ('s1',
                            0.0,
                            'native SBML value',
                            'Initial level of Acety Co A. Maps to SBML symbol `s1`; exposed as a '
                            'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'s1': 'Acety Co A',
     's2': 'Acetoacetyl Co A',
     's3': '3 Hydroxy 3 Methylglutaryl Co A',
     's4': 'Mevalonate',
     's5': 'Acetoacetate',
     's6': 'HMGCR',
     's7': 'HMGCL',
     's8': 'source-defined AKAT1 state',
     's9': 'HMGCS2',
     's10': 'Mevalonate P',
     's11': 'source-defined MVK state',
     's16': 'Mevalonate PP',
     's17': 'source-defined PMVK state',
     's20': 'Isopentenyl PP',
     's21': 'source-defined MVD state',
     's22': 'Dimethylallyl PP',
     's23': 'Geranyl PP',
     's26': 'Presqualene PP',
     's27': 'Squalene',
     's29': 'source-defined FDPS state',
     's31': 'source-defined GGPS1 state',
     's38': 'source-defined IDI2 state',
     's39': 'source-defined IDI1 state',
     's40': 'source-defined FDFT1 state',
     's77': 'Geranylgeranyl PP',
     's78': 'Farnesyl PP',
     's79': 'HMGCS1',
     's80': 'source-defined ACAT2 state',
     's81': 'source-defined AKAT1 state',
     's82': 'Acetoacetate',
     's83': 'Acety Co A',
     's84': 'HMGCL',
     's85': 'HMGCR',
     's86': 'Acetoacetyl Co A',
     's87': 'HMGCS2',
     's88': '3 Hydroxy 3 Methylglutaryl Co A',
     's89': 'Mevalonate',
     's90': 'Farnesyl PP',
     's91': '3 Hydroxy 3 Methylglutaryl Co A',
     's97': 'Acety Co A',
     's98': 'Acetoacetyl Co A'}
    _STATE_OUTPUT_ALIASES = {'s1': 'acety_co_a',
     's2': 'acetoacetyl_co_a',
     's3': 'source_3_hydroxy_3_methylglutaryl_co_a',
     's4': 'mevalonate',
     's5': 'acetoacetate',
     's6': 'hmgcr',
     's7': 'hmgcl',
     's8': 'source_defined_akat1_state',
     's9': 'hmgcs2',
     's10': 'mevalonate_p',
     's11': 'source_defined_mvk_state',
     's16': 'mevalonate_pp',
     's17': 'source_defined_pmvk_state',
     's20': 'isopentenyl_pp',
     's21': 'source_defined_mvd_state',
     's22': 'dimethylallyl_pp',
     's23': 'geranyl_pp',
     's26': 'presqualene_pp',
     's27': 'squalene',
     's29': 'source_defined_fdps_state',
     's31': 'source_defined_ggps1_state',
     's38': 'source_defined_idi2_state',
     's39': 'source_defined_idi1_state',
     's40': 'source_defined_fdft1_state',
     's77': 'geranylgeranyl_pp',
     's78': 'farnesyl_pp',
     's79': 'hmgcs1',
     's80': 'source_defined_acat2_state',
     's81': 'source_defined_akat1_state_2',
     's82': 'acetoacetate_2',
     's83': 'acety_co_a_2',
     's84': 'hmgcl_2',
     's85': 'hmgcr_2',
     's86': 'acetoacetyl_co_a_2',
     's87': 'hmgcs2_2',
     's88': 'source_3_hydroxy_3_methylglutaryl_co_a_2',
     's89': 'mevalonate_2',
     's90': 'farnesyl_pp_2',
     's91': 'source_3_hydroxy_3_methylglutaryl_co_a_3',
     's97': 'acety_co_a_3',
     's98': 'acetoacetyl_co_a_3'}

    def __init__(self, model_path: str = 'data/MODEL1409170000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Mazein2013CholesterolBiosynthesisPathwayModel1409170000Model = Mazein2013CholesterolBiosynthesisPathwayModel
