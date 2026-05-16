# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bhalla2004_PKC_2003."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bhalla2004Pkc2003Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL9080388197'
    _TITLE = 'Bhalla2004_PKC_2003'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'calcium_bound_pkc': ('PKC_slash_PKC_minus_Ca',
                           'native SBML value',
                           'Calcium bound PKC. Maps to SBML symbol `PKC_slash_PKC_minus_Ca` and is '
                           'emitted in native SBML units.'),
     'arachidonic_acid_active_calcium_bound_pkc': ('PKC_slash_PKC_minus_Ca_minus_AA_star_',
                                                   'native SBML value',
                                                   'Arachidonic Acid active Calcium bound PKC. Maps to '
                                                   'SBML symbol '
                                                   '`PKC_slash_PKC_minus_Ca_minus_AA_star_` and is '
                                                   'emitted in native SBML units.'),
     'membrane_active_calcium_bound_pkc': ('PKC_slash_PKC_minus_Ca_minus_memb_star_',
                                           'native SBML value',
                                           'Membrane active Calcium bound PKC. Maps to SBML symbol '
                                           '`PKC_slash_PKC_minus_Ca_minus_memb_star_` and is emitted '
                                           'in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_dag': ('DAG',
                     11.0,
                     'native SBML value',
                     'Initial level of DAG. Maps to SBML symbol `DAG`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_source_defined_aa_state': ('AA',
                                         5.0,
                                         'native SBML value',
                                         'Initial level of source-defined AA state. Maps to SBML '
                                         'symbol `AA`; exposed as a traceable initial-condition '
                                         'perturbation.'),
     'initial_calcium': ('Ca',
                         0.08,
                         'native SBML value',
                         'Initial level of calcium. Maps to SBML symbol `Ca`; exposed as a traceable '
                         'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'PKC_slash_PKC_minus_Ca': 'Calcium bound PKC',
     'PKC_slash_PKC_minus_DAG_minus_AA_star_': 'DAG And Arachidonic Acid active PKC',
     'PKC_slash_PKC_minus_Ca_minus_AA_star_': 'Arachidonic Acid active Calcium bound PKC',
     'PKC_slash_PKC_minus_Ca_minus_memb_star_': 'Membrane active Calcium bound PKC',
     'PKC_slash_PKC_minus_DAG_minus_memb_star_': 'Membrane active DAG bound PKC',
     'PKC_slash_PKC_minus_basal_star_': 'Basal active PKC',
     'PKC_slash_PKC_minus_AA_star_': 'Arachidonic Acid active PKC',
     'PKC_slash_PKC_minus_Ca_minus_DAG': 'Calcium And DAG bound PKC',
     'PKC_slash_PKC_minus_DAG': 'DAG bound PKC',
     'PKC_slash_PKC_minus_DAG_minus_AA': 'DAG And Arachidonic Acid bound PKC',
     'PKC_slash_PKC_minus_cytosolic': 'cytosolic PKC',
     'DAG': 'DAG',
     'Ca': 'Calcium',
     'AA': 'Source Defined AA State',
     'PKC_minus_active': 'active PKC'}
    _STATE_OUTPUT_ALIASES = {'PKC_slash_PKC_minus_Ca': 'calcium_bound_pkc',
     'PKC_slash_PKC_minus_DAG_minus_AA_star_': 'dag_and_arachidonic_acid_active_pkc',
     'PKC_slash_PKC_minus_Ca_minus_AA_star_': 'arachidonic_acid_active_calcium_bound_pkc',
     'PKC_slash_PKC_minus_Ca_minus_memb_star_': 'membrane_active_calcium_bound_pkc',
     'PKC_slash_PKC_minus_DAG_minus_memb_star_': 'membrane_active_dag_bound_pkc',
     'PKC_slash_PKC_minus_basal_star_': 'basal_active_pkc',
     'PKC_slash_PKC_minus_AA_star_': 'arachidonic_acid_active_pkc',
     'PKC_slash_PKC_minus_Ca_minus_DAG': 'calcium_and_dag_bound_pkc',
     'PKC_slash_PKC_minus_DAG': 'dag_bound_pkc',
     'PKC_slash_PKC_minus_DAG_minus_AA': 'dag_and_arachidonic_acid_bound_pkc',
     'PKC_slash_PKC_minus_cytosolic': 'cytosolic_pkc',
     'DAG': 'dag',
     'Ca': 'calcium',
     'AA': 'source_defined_aa_state',
     'PKC_minus_active': 'active_pkc'}

    def __init__(self, model_path: str = 'data/MODEL9080388197.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bhalla2004Pkc2003Model9080388197Model = Bhalla2004Pkc2003Model
