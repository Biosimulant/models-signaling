# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Machado2014 - Curcumin production pathway in Escherichia coli."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Machado2014CurcuminProductionPathwayInEscheModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000565'
    _TITLE = 'Machado2014 - Curcumin production pathway in Escherichia coli'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'phosphoenol_pyruvate': ('cpep',
                              'native SBML value',
                              'Phosphoenol Pyruvate. Maps to SBML symbol `cpep` and is emitted in '
                              'native SBML units.'),
     'glucose_6_phosphate': ('cg6p',
                             'native SBML value',
                             'Glucose 6 Phosphate. Maps to SBML symbol `cg6p` and is emitted in native '
                             'SBML units.'),
     'fructose_6_phosphate': ('cf6p',
                              'native SBML value',
                              'Fructose 6 Phosphate. Maps to SBML symbol `cf6p` and is emitted in '
                              'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_extracellular_glucose': ('cglcex',
                                       55.5,
                                       'native SBML value',
                                       'Initial level of Extracellular Glucose. Maps to SBML symbol '
                                       '`cglcex`; exposed as a traceable initial-condition '
                                       'perturbation.'),
     'initial_glucose_1_phosphate': ('cg1p',
                                     0.653,
                                     'native SBML value',
                                     'Initial level of Glucose 1 Phosphate. Maps to SBML symbol '
                                     '`cg1p`; exposed as a traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {'initial_camp_level': ('camp',
                            0.955,
                            'mM',
                            'cAMP source parameter. Maps to SBML symbol `camp` and preserves the '
                            'bundled default.')}
    _SPECIES_LABELS = {'cpep': 'Phosphoenol Pyruvate',
     'cglcex': 'Extracellular Glucose',
     'cg6p': 'Glucose 6 Phosphate',
     'cpyr': 'Pyruvate',
     'cf6p': 'Fructose 6 Phosphate',
     'cg1p': 'Glucose 1 Phosphate',
     'cpg': '6 Phosphogluconate',
     'cfdp': 'Fructose 1 6 Bisphosphate',
     'csed7p': 'Sedoheptulose 7 Phosphate',
     'cgap': 'Glyceraldehyde 3 Phosphate',
     'ce4p': 'Erythrose 4 Phosphate',
     'cxyl5p': 'Xylulose 5 Phosphate',
     'crib5p': 'Ribose 5 Phosphate',
     'cdhap': 'Dihydroxyacetonephosphate',
     'cpgp': '1 3 Diphosphosphoglycerate',
     'cpg3': '3 Phosphoglycerate',
     'cpg2': '2 Phosphoglycerate',
     'cribu5p': 'Ribulose 5 Phosphate',
     'accoa': 'Accoa',
     'malcoa': 'Malcoa',
     'fer': 'Source Defined FER State',
     'fer_ext': 'Fer Ext',
     'fercoa': 'Fercoa',
     'ferdicoa': 'Ferdicoa',
     'cur': 'Source Defined CUR State',
     'cur_ext': 'Cur Ext'}
    _STATE_OUTPUT_ALIASES = {'cpep': 'phosphoenol_pyruvate',
     'cglcex': 'extracellular_glucose',
     'cg6p': 'glucose_6_phosphate',
     'cpyr': 'pyruvate',
     'cf6p': 'fructose_6_phosphate',
     'cg1p': 'glucose_1_phosphate',
     'cpg': 'source_6_phosphogluconate',
     'cfdp': 'fructose_1_6_bisphosphate',
     'csed7p': 'sedoheptulose_7_phosphate',
     'cgap': 'glyceraldehyde_3_phosphate',
     'ce4p': 'erythrose_4_phosphate',
     'cxyl5p': 'xylulose_5_phosphate',
     'crib5p': 'ribose_5_phosphate',
     'cdhap': 'dihydroxyacetonephosphate',
     'cpgp': 'source_1_3_diphosphosphoglycerate',
     'cpg3': 'source_3_phosphoglycerate',
     'cpg2': 'source_2_phosphoglycerate',
     'cribu5p': 'ribulose_5_phosphate',
     'accoa': 'accoa',
     'malcoa': 'malcoa',
     'fer': 'source_defined_fer_state',
     'fer_ext': 'fer_ext',
     'fercoa': 'fercoa',
     'ferdicoa': 'ferdicoa',
     'cur': 'source_defined_cur_state',
     'cur_ext': 'cur_ext'}

    def __init__(self, model_path: str = 'data/BIOMD0000000565.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Machado2014CurcuminProductionPathwayInEscheBiomd0000000565Model = Machado2014CurcuminProductionPathwayInEscheModel
