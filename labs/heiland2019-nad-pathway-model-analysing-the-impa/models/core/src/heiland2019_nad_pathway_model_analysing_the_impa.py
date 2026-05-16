# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Heiland2019 - NAD pathway model analysing the impact of NNMT on pathway dynamics and evolution."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Heiland2019NadPathwayModelAnalysingTheImpaModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1905220001'
    _TITLE = 'Heiland2019 - NAD pathway model analysing the impact of NNMT on pathway dynamics and evolution'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'nicotinate_mononucleotide': ('NaMN',
                                   'substance',
                                   'nicotinate mononucleotide. Maps to SBML symbol `NaMN` and is '
                                   'emitted in native SBML units.'),
     'nicotinamide': ('NAM',
                      'substance',
                      'nicotinamide. Maps to SBML symbol `NAM` and is emitted in native SBML units.'),
     'nad': ('NAD', 'substance', 'NAD. Maps to SBML symbol `NAD` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_adp': ('ADP',
                     1.0,
                     'substance',
                     'Initial level of ADP. Maps to SBML symbol `ADP`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_amp': ('AMP',
                     1.0,
                     'substance',
                     'Initial level of AMP. Maps to SBML symbol `AMP`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_atp': ('ATP',
                     1.0,
                     'substance',
                     'Initial level of ATP. Maps to SBML symbol `ATP`; exposed as a traceable '
                     'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'NA': 'source-defined NA state',
     'NaMN': 'nicotinate mononucleotide',
     'NAM': 'nicotinamide',
     'NAD': 'NAD',
     'NaAD': 'source-defined NAAD state',
     'NMN': 'source-defined NMN state',
     'NAR': 'source-defined NAR state',
     'H2O': 'H2O',
     'ADP': 'ADP',
     'ATP': 'ATP',
     'PPi': 'source-defined PPI state',
     'PRPP': 'source-defined PRPP state',
     '_1_methyl_NAM': '1 Methyl nicotinamide',
     'SAH': 'source-defined SAH state',
     'SAM': 'source-defined SAM state',
     'AMP': 'AMP',
     'Gln': 'source-defined GLN state',
     'Glu': 'glutamate',
     'H3_ac': 'H3 Ac',
     'H3_deac': 'H3 Deac',
     'Pi': 'source-defined PI state',
     'NR': 'source-defined NR state',
     'NADbound': 'Nadbound'}
    _STATE_OUTPUT_ALIASES = {'NA': 'source_defined_na_state',
     'NaMN': 'nicotinate_mononucleotide',
     'NAM': 'nicotinamide',
     'NAD': 'nad',
     'NaAD': 'source_defined_naad_state',
     'NMN': 'source_defined_nmn_state',
     'NAR': 'source_defined_nar_state',
     'H2O': 'h2o',
     'ADP': 'adp',
     'ATP': 'atp',
     'PPi': 'source_defined_ppi_state',
     'PRPP': 'source_defined_prpp_state',
     '_1_methyl_NAM': 'source_1_methyl_nicotinamide',
     'SAH': 'source_defined_sah_state',
     'SAM': 'source_defined_sam_state',
     'AMP': 'amp',
     'Gln': 'source_defined_gln_state',
     'Glu': 'glutamate',
     'H3_ac': 'h3_ac',
     'H3_deac': 'h3_deac',
     'Pi': 'source_defined_pi_state',
     'NR': 'source_defined_nr_state',
     'NADbound': 'nadbound'}

    def __init__(self, model_path: str = 'data/MODEL1905220001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Heiland2019NadPathwayModelAnalysingTheImpaModel1905220001Model = Heiland2019NadPathwayModelAnalysingTheImpaModel
