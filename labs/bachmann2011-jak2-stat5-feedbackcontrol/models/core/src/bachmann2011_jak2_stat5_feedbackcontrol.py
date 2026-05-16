# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Bachmann2011_JAK2-STAT5_FeedbackControl."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bachmann2011Jak2Stat5FeedbackcontrolModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000347'
    _TITLE = 'Bachmann2011_JAK2-STAT5_FeedbackControl'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'stat5': ('STAT5',
               'native SBML value',
               'STAT5. Maps to SBML symbol `STAT5` and is emitted in native SBML units.'),
     'phosphorylated_stat5': ('pSTAT5',
                              'native SBML value',
                              'phosphorylated STAT5. Maps to SBML symbol `pSTAT5` and is emitted in '
                              'native SBML units.'),
     'nuclear_phosphorylated_stat5': ('npSTAT5',
                                      'native SBML value',
                                      'nuclear phosphorylated STAT5. Maps to SBML symbol `npSTAT5` and '
                                      'is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_epo_receptor_jak2_complex': ('EpoRJAK2',
                                           0.0,
                                           'native SBML value',
                                           'Initial level of EPO receptor-JAK2 complex. Maps to SBML '
                                           'symbol `EpoRJAK2`; exposed as a traceable '
                                           'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'EpoRJAK2': 'EPO receptor-JAK2 complex',
     'EpoRpJAK2': 'phosphorylated EPO receptor-JAK2 complex',
     'p1EpoRpJAK2': 'site 1 phosphorylated EPO receptor-JAK2 complex',
     'p2EpoRpJAK2': 'site 2 phosphorylated EPO receptor-JAK2 complex',
     'p12EpoRpJAK2': 'dual-site phosphorylated EPO receptor-JAK2 complex',
     'EpoRJAK2_CIS': 'CIS-bound EPO receptor-JAK2 complex',
     'SHP1': 'SHP1 phosphatase',
     'SHP1Act': 'Shp1act',
     'STAT5': 'STAT5',
     'pSTAT5': 'phosphorylated STAT5',
     'npSTAT5': 'nuclear phosphorylated STAT5',
     'CISnRNA1': 'Cisn RNA1',
     'CISnRNA2': 'Cisn RNA2',
     'CISnRNA3': 'Cisn RNA3',
     'CISnRNA4': 'Cisn RNA4',
     'CISnRNA5': 'Cisn RNA5',
     'CISRNA': 'CISRNA',
     'CIS': 'CIS feedback regulator',
     'SOCS3nRNA1': 'Socs3n RNA1',
     'SOCS3nRNA2': 'Socs3n RNA2',
     'SOCS3nRNA3': 'Socs3n RNA3',
     'SOCS3nRNA4': 'Socs3n RNA4',
     'SOCS3nRNA5': 'Socs3n RNA5',
     'SOCS3RNA': 'SOCS3RNA',
     'SOCS3': 'SOCS3',
     'Epo': 'erythropoietin'}
    _STATE_OUTPUT_ALIASES = {'EpoRJAK2': 'epo_receptor_jak2_complex',
     'EpoRpJAK2': 'phosphorylated_epo_receptor_jak2_complex',
     'p1EpoRpJAK2': 'site_1_phosphorylated_epo_receptor_jak2_complex',
     'p2EpoRpJAK2': 'site_2_phosphorylated_epo_receptor_jak2_complex',
     'p12EpoRpJAK2': 'dual_site_phosphorylated_epo_receptor_jak2_complex',
     'EpoRJAK2_CIS': 'cis_bound_epo_receptor_jak2_complex',
     'SHP1': 'shp1_phosphatase',
     'SHP1Act': 'shp1act',
     'STAT5': 'stat5',
     'pSTAT5': 'phosphorylated_stat5',
     'npSTAT5': 'nuclear_phosphorylated_stat5',
     'CISnRNA1': 'cisn_rna1',
     'CISnRNA2': 'cisn_rna2',
     'CISnRNA3': 'cisn_rna3',
     'CISnRNA4': 'cisn_rna4',
     'CISnRNA5': 'cisn_rna5',
     'CISRNA': 'cisrna',
     'CIS': 'cis_feedback_regulator',
     'SOCS3nRNA1': 'socs3n_rna1',
     'SOCS3nRNA2': 'socs3n_rna2',
     'SOCS3nRNA3': 'socs3n_rna3',
     'SOCS3nRNA4': 'socs3n_rna4',
     'SOCS3nRNA5': 'socs3n_rna5',
     'SOCS3RNA': 'socs3rna',
     'SOCS3': 'socs3',
     'Epo': 'erythropoietin'}

    def __init__(self, model_path: str = 'data/BIOMD0000000347.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bachmann2011Jak2Stat5FeedbackcontrolBiomd0000000347Model = Bachmann2011Jak2Stat5FeedbackcontrolModel
