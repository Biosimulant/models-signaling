# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Brown2004 - NGF and EGF signaling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Brown2004NgfAndEgfSignalingModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'BIOMD0000000033'
    _TITLE = 'Brown2004 - NGF and EGF signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'free_egfreceptor': ('freeEGFReceptor',
                          'native SBML value',
                          'free Egfreceptor. Maps to SBML symbol `freeEGFReceptor` and is emitted in '
                          'native SBML units.'),
     'bound_egfreceptor': ('boundEGFReceptor',
                           'native SBML value',
                           'bound Egfreceptor. Maps to SBML symbol `boundEGFReceptor` and is emitted '
                           'in native SBML units.'),
     'free_ngfreceptor': ('freeNGFReceptor',
                          'native SBML value',
                          'free Ngfreceptor. Maps to SBML symbol `freeNGFReceptor` and is emitted in '
                          'native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_source_defined_kegf_state_level': ('kEGF',
                                                 694.731,
                                                 'native SBML value',
                                                 'source-defined KEGF state source parameter. Maps to '
                                                 'SBML symbol `kEGF` and preserves the bundled '
                                                 'default.'),
     'initial_km_egf_level': ('KmEGF',
                              6086070.0,
                              'native SBML value',
                              'Km EGF source parameter. Maps to SBML symbol `KmEGF` and preserves the '
                              'bundled default.'),
     'initial_krb_egf_level': ('krbEGF',
                               2.18503e-05,
                               'native SBML value',
                               'Krb EGF source parameter. Maps to SBML symbol `krbEGF` and preserves '
                               'the bundled default.')}
    _SPECIES_LABELS = {'EGF': 'EGF',
     'NGF': 'Source Defined Nerve Growth Factor State',
     'freeEGFReceptor': 'free Egfreceptor',
     'boundEGFReceptor': 'bound Egfreceptor',
     'freeNGFReceptor': 'free Ngfreceptor',
     'boundNGFReceptor': 'bound Ngfreceptor',
     'SosInactive': 'SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor Guanine '
                    'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
                    'Exchange Factor Inactive',
     'SosActive': 'SOS guanine-nucleotide exchange factor Guanine Nucleotide Exchange Factor Guanine '
                  'Nucleotide Exchange Factor Guanine Nucleotide Exchange Factor Guanine Nucleotide '
                  'Exchange Factor active',
     'P90RskInactive': 'P90rsk Inactive',
     'P90RskActive': 'P90rsk active',
     'RasInactive': 'RAS Inactive',
     'RasActive': 'RAS active',
     'RasGapActive': 'active RAS GAP',
     'Raf1Inactive': 'Raf1inactive',
     'Raf1Active': 'Raf1active',
     'BRafInactive': 'Braf Inactive',
     'BRafActive': 'Braf active',
     'MekInactive': 'MEK Inactive',
     'MekActive': 'MEK active',
     'ErkInactive': 'ERK Inactive',
     'ErkActive': 'ERK active',
     'PI3KInactive': 'Pi3kinactive',
     'PI3KActive': 'Pi3kactive',
     'AktInactive': 'AKT Inactive',
     'AktActive': 'AKT active',
     'C3GInactive': 'C3ginactive',
     'C3GActive': 'C3gactive',
     'Rap1Inactive': 'Rap1inactive',
     'Rap1Active': 'Rap1active',
     'RapGapActive': 'Rap Gap active',
     'PP2AActive': 'Pp2aactive',
     'Raf1PPtase': 'Raf1pptase'}
    _STATE_OUTPUT_ALIASES = {'EGF': 'egf',
     'NGF': 'source_defined_nerve_growth_factor_state',
     'freeEGFReceptor': 'free_egfreceptor',
     'boundEGFReceptor': 'bound_egfreceptor',
     'freeNGFReceptor': 'free_ngfreceptor',
     'boundNGFReceptor': 'bound_ngfreceptor',
     'SosInactive': 'sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_inactive',
     'SosActive': 'sos_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_guanine_nucleotide_exchange_factor_active',
     'P90RskInactive': 'p90rsk_inactive',
     'P90RskActive': 'p90rsk_active',
     'RasInactive': 'ras_inactive',
     'RasActive': 'ras_active',
     'RasGapActive': 'active_ras_gap',
     'Raf1Inactive': 'raf1inactive',
     'Raf1Active': 'raf1active',
     'BRafInactive': 'braf_inactive',
     'BRafActive': 'braf_active',
     'MekInactive': 'mek_inactive',
     'MekActive': 'mek_active',
     'ErkInactive': 'erk_inactive',
     'ErkActive': 'erk_active',
     'PI3KInactive': 'pi3kinactive',
     'PI3KActive': 'pi3kactive',
     'AktInactive': 'akt_inactive',
     'AktActive': 'akt_active',
     'C3GInactive': 'c3ginactive',
     'C3GActive': 'c3gactive',
     'Rap1Inactive': 'rap1inactive',
     'Rap1Active': 'rap1active',
     'RapGapActive': 'rap_gap_active',
     'PP2AActive': 'pp2aactive',
     'Raf1PPtase': 'raf1pptase'}

    def __init__(self, model_path: str = 'data/BIOMD0000000033.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Brown2004NgfAndEgfSignalingBiomd0000000033Model = Brown2004NgfAndEgfSignalingModel
