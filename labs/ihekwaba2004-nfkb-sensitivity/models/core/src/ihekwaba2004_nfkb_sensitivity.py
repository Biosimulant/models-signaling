# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Ihekwaba2004_NFkB_Sensitivity."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ihekwaba2004NfkbSensitivityModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000230'
    _TITLE = 'Ihekwaba2004_NFkB_Sensitivity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'nfkb': ('NFkB',
              'native SBML value',
              'NF-kB. Maps to SBML symbol `NFkB` and is emitted in native SBML units.'),
     'ikkik_ba_nfk_b': ('IKKIkBaNFkB',
                        'native SBML value',
                        'Ikkik Ba Nfk B. Maps to SBML symbol `IKKIkBaNFkB` and is emitted in native '
                        'SBML units.'),
     'ikkik_complement_factor_bb_nfk_b': ('IKKIkBbNFkB',
                                          'native SBML value',
                                          'Ikkik complement factor Bb Nfk B. Maps to SBML symbol '
                                          '`IKKIkBbNFkB` and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_sink_species': ('sink',
                              0.0,
                              'native SBML value',
                              'Initial level of sink species. Maps to SBML symbol `sink`; exposed as a '
                              'traceable initial-condition perturbation.'),
     'initial_source': ('source',
                        1.0,
                        'native SBML value',
                        'Initial level of Source. Maps to SBML symbol `source`; exposed as a traceable '
                        'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'NFkB': 'NF-kB',
     'IKKIkBa': 'Ikkik Ba',
     'IKKIkBaNFkB': 'Ikkik Ba Nfk B',
     'IKK': 'source-defined IKK state',
     'IkBa': 'source-defined IKBA state',
     'IKKIkBb': 'Ikkik complement factor Bb',
     'IKKIkBbNFkB': 'Ikkik complement factor Bb Nfk B',
     'IkBb': 'source-defined IKBB state',
     'IKKIkBe': 'Ikkik Be',
     'IKKIkBeNFkB': 'Ikkik Be Nfk B',
     'IkBe': 'source-defined IKBE state',
     'IkBaNFkB': 'Ik Ba Nfk B',
     'IkBbNFkB': 'Ik complement factor Bb Nfk B',
     'IkBeNFkB': 'Ik Be Nfk B',
     'source': 'Source',
     'IkBat': 'Ik Bat',
     'sink': 'sink species',
     'NFkBn': 'Nfk Bn',
     'IkBan': 'Ik Ban',
     'IkBanNFkBn': 'Ik Ban Nfk Bn',
     'IkBbn': 'Ik Bbn',
     'IkBbnNFkBn': 'Ik Bbn Nfk Bn',
     'IkBbt': 'Ik Bbt',
     'IkBen': 'Ik Ben',
     'IkBenNFkBn': 'Ik Ben Nfk Bn',
     'IkBet': 'Ik Bet'}
    _STATE_OUTPUT_ALIASES = {'NFkB': 'nfkb',
     'IKKIkBa': 'ikkik_ba',
     'IKKIkBaNFkB': 'ikkik_ba_nfk_b',
     'IKK': 'source_defined_ikk_state',
     'IkBa': 'source_defined_ikba_state',
     'IKKIkBb': 'ikkik_complement_factor_bb',
     'IKKIkBbNFkB': 'ikkik_complement_factor_bb_nfk_b',
     'IkBb': 'source_defined_ikbb_state',
     'IKKIkBe': 'ikkik_be',
     'IKKIkBeNFkB': 'ikkik_be_nfk_b',
     'IkBe': 'source_defined_ikbe_state',
     'IkBaNFkB': 'ik_ba_nfk_b',
     'IkBbNFkB': 'ik_complement_factor_bb_nfk_b',
     'IkBeNFkB': 'ik_be_nfk_b',
     'source': 'source',
     'IkBat': 'ik_bat',
     'sink': 'sink_species',
     'NFkBn': 'nfk_bn',
     'IkBan': 'ik_ban',
     'IkBanNFkBn': 'ik_ban_nfk_bn',
     'IkBbn': 'ik_bbn',
     'IkBbnNFkBn': 'ik_bbn_nfk_bn',
     'IkBbt': 'ik_bbt',
     'IkBen': 'ik_ben',
     'IkBenNFkBn': 'ik_ben_nfk_bn',
     'IkBet': 'ik_bet'}

    def __init__(self, model_path: str = 'data/BIOMD0000000230.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Ihekwaba2004NfkbSensitivityBiomd0000000230Model = Ihekwaba2004NfkbSensitivityModel
