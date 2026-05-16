# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Schilling2009 - ERK distributive."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schilling2009ErkDistributiveModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000270'
    _TITLE = 'Schilling2009 - ERK distributive'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'source_defined_erk1_state': ('ERK1',
                                   'native SBML value',
                                   'Source Defined ERK1 State. Maps to SBML symbol `ERK1` and is '
                                   'emitted in native SBML units.'),
     'source_defined_erk2_state': ('ERK2',
                                   'native SBML value',
                                   'Source Defined ERK2 State. Maps to SBML symbol `ERK2` and is '
                                   'emitted in native SBML units.'),
     'pperk1': ('ppERK1',
                'native SBML value',
                'PPERK1. Maps to SBML symbol `ppERK1` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_jak2': ('JAK2',
                      0.0,
                      'native SBML value',
                      'Initial level of JAK2. Maps to SBML symbol `JAK2`; exposed as a traceable '
                      'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'JAK2': 'JAK2',
     'EpoR': 'Erythropoietin Receptor',
     'SHP1': 'SHP1 phosphatase Phosphatase Phosphatase Phosphatase Phosphatase Phosphatase',
     'SOS': 'Source Defined SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor '
            'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
            'Exchange Factor State',
     'Raf': 'RAF',
     'MEK2': 'Source Defined MEK2 State',
     'MEK1': 'Source Defined MEK1 State',
     'ERK1': 'Source Defined ERK1 State',
     'ERK2': 'Source Defined ERK2 State',
     'pJAK2': 'Source Defined Phosphorylated JAK2 State',
     'pEpoR': 'Phospho Erythropoietin R',
     'mSHP1': 'Source Defined MSHP1 State',
     'actSHP1': 'ACTSHP1',
     'mSOS': 'Source Defined MSOS State',
     'pRaf': 'Phospho RAF',
     'ppMEK2': 'PPMEK2',
     'ppMEK1': 'PPMEK1',
     'ppERK1': 'PPERK1',
     'ppERK2': 'PPERK2',
     'pSOS': 'Phospho SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor '
             'Guanine Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
             'Exchange Factor',
     'pMEK2': 'Source Defined PMEK2 State',
     'pMEK1': 'Source Defined PMEK1 State',
     'pERK1': 'Source Defined PERK1 State',
     'pERK2': 'Source Defined PERK2 State',
     'Delay01_mSHP1': 'DELAY01 MSHP1',
     'Delay02_mSHP1': 'DELAY02 MSHP1',
     'Delay03_mSHP1': 'DELAY03 MSHP1',
     'Delay04_mSHP1': 'DELAY04 MSHP1',
     'Delay05_mSHP1': 'DELAY05 MSHP1',
     'Delay06_mSHP1': 'DELAY06 MSHP1',
     'Delay07_mSHP1': 'DELAY07 MSHP1',
     'Delay08_mSHP1': 'DELAY08 MSHP1',
     'Epo': 'Erythropoietin'}
    _STATE_OUTPUT_ALIASES = {'JAK2': 'jak2',
     'EpoR': 'erythropoietin_receptor',
     'SHP1': 'shp1_phosphatase_phosphatase_phosphatase_phosphatase_phosphatase_phosphatase',
     'SOS': 'source_defined_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_state',
     'Raf': 'raf',
     'MEK2': 'source_defined_mek2_state',
     'MEK1': 'source_defined_mek1_state',
     'ERK1': 'source_defined_erk1_state',
     'ERK2': 'source_defined_erk2_state',
     'pJAK2': 'source_defined_phosphorylated_jak2_state',
     'pEpoR': 'phospho_erythropoietin_r',
     'mSHP1': 'source_defined_mshp1_state',
     'actSHP1': 'actshp1',
     'mSOS': 'source_defined_msos_state',
     'pRaf': 'phospho_raf',
     'ppMEK2': 'ppmek2',
     'ppMEK1': 'ppmek1',
     'ppERK1': 'pperk1',
     'ppERK2': 'pperk2',
     'pSOS': 'phospho_sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor',
     'pMEK2': 'source_defined_pmek2_state',
     'pMEK1': 'source_defined_pmek1_state',
     'pERK1': 'source_defined_perk1_state',
     'pERK2': 'source_defined_perk2_state',
     'Delay01_mSHP1': 'delay01_mshp1',
     'Delay02_mSHP1': 'delay02_mshp1',
     'Delay03_mSHP1': 'delay03_mshp1',
     'Delay04_mSHP1': 'delay04_mshp1',
     'Delay05_mSHP1': 'delay05_mshp1',
     'Delay06_mSHP1': 'delay06_mshp1',
     'Delay07_mSHP1': 'delay07_mshp1',
     'Delay08_mSHP1': 'delay08_mshp1',
     'Epo': 'erythropoietin'}

    def __init__(self, model_path: str = 'data/BIOMD0000000270.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Schilling2009ErkDistributiveBiomd0000000270Model = Schilling2009ErkDistributiveModel
