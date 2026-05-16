# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Hoffmann2002_WT_IkBNFkB_Signaling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hoffmann2002WtIkbnfkbSignalingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000140'
    _TITLE = 'Hoffmann2002_WT_IkBNFkB_Signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'nfkb': ('NFkB',
              'native SBML value',
              'NF-kB. Maps to SBML symbol `NFkB` and is emitted in native SBML units.'),
     'ik_balpha_nf_k_b': ('IkBalpha_NFkB',
                          'native SBML value',
                          'Ik Balpha NF K B. Maps to SBML symbol `IkBalpha_NFkB` and is emitted in '
                          'native SBML units.'),
     'ik_bbeta_nf_k_b': ('IkBbeta_NFkB',
                         'native SBML value',
                         'Ik Bbeta NF K B. Maps to SBML symbol `IkBbeta_NFkB` and is emitted in native '
                         'SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_ik_balpha': ('IkBalpha',
                           0.0,
                           'native SBML value',
                           'Initial level of Ik Balpha. Maps to SBML symbol `IkBalpha`; exposed as a '
                           'traceable initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'IkBalpha': 'Ik Balpha',
     'NFkB': 'NF-kB',
     'IkBalpha_NFkB': 'Ik Balpha NF K B',
     'IkBbeta': 'Ik Bbeta',
     'IkBbeta_NFkB': 'Ik Bbeta NF K B',
     'IkBeps': 'Ik Beps',
     'IkBeps_NFkB': 'Ik Beps NF K B',
     'IKK_IkBalpha': 'IKK Ik Balpha',
     'IKK_IkBalpha_NFkB': 'IKK Ik Balpha NF K B',
     'IKK': 'Source Defined IKK State',
     'IKK_IkBbeta': 'IKK Ik Bbeta',
     'IKK_IkBbeta_NFkB': 'IKK Ik Bbeta NF K B',
     'IKK_IkBeps': 'IKK Ik Beps',
     'IKK_IkBeps_NFkB': 'IKK Ik Beps NF K B',
     'NFkB_nuc': 'NF K B Nuc',
     'IkBalpha_nuc': 'Ik Balpha Nuc',
     'IkBalpha_nuc_NFkB_nuc': 'Ik Balpha Nuc NF K B Nuc',
     'IkBbeta_nuc': 'Ik Bbeta Nuc',
     'IkBbeta_nuc_NFkB_nuc': 'Ik Bbeta Nuc NF K B Nuc',
     'IkBeps_nuc': 'Ik Beps Nuc',
     'IkBalpha_transcript': 'Ik Balpha Transcript',
     'IkBbeta_transcript': 'Ik Bbeta Transcript',
     'IkBeps_transcript': 'Ik Beps Transcript',
     'IkBeps_nuc_NFkB_nuc': 'Ik Beps Nuc NF K B Nuc'}
    _STATE_OUTPUT_ALIASES = {'IkBalpha': 'ik_balpha',
     'NFkB': 'nfkb',
     'IkBalpha_NFkB': 'ik_balpha_nf_k_b',
     'IkBbeta': 'ik_bbeta',
     'IkBbeta_NFkB': 'ik_bbeta_nf_k_b',
     'IkBeps': 'ik_beps',
     'IkBeps_NFkB': 'ik_beps_nf_k_b',
     'IKK_IkBalpha': 'ikk_ik_balpha',
     'IKK_IkBalpha_NFkB': 'ikk_ik_balpha_nf_k_b',
     'IKK': 'source_defined_ikk_state',
     'IKK_IkBbeta': 'ikk_ik_bbeta',
     'IKK_IkBbeta_NFkB': 'ikk_ik_bbeta_nf_k_b',
     'IKK_IkBeps': 'ikk_ik_beps',
     'IKK_IkBeps_NFkB': 'ikk_ik_beps_nf_k_b',
     'NFkB_nuc': 'nf_k_b_nuc',
     'IkBalpha_nuc': 'ik_balpha_nuc',
     'IkBalpha_nuc_NFkB_nuc': 'ik_balpha_nuc_nf_k_b_nuc',
     'IkBbeta_nuc': 'ik_bbeta_nuc',
     'IkBbeta_nuc_NFkB_nuc': 'ik_bbeta_nuc_nf_k_b_nuc',
     'IkBeps_nuc': 'ik_beps_nuc',
     'IkBalpha_transcript': 'ik_balpha_transcript',
     'IkBbeta_transcript': 'ik_bbeta_transcript',
     'IkBeps_transcript': 'ik_beps_transcript',
     'IkBeps_nuc_NFkB_nuc': 'ik_beps_nuc_nf_k_b_nuc'}

    def __init__(self, model_path: str = 'data/BIOMD0000000140.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Hoffmann2002WtIkbnfkbSignalingBiomd0000000140Model = Hoffmann2002WtIkbnfkbSignalingModel
