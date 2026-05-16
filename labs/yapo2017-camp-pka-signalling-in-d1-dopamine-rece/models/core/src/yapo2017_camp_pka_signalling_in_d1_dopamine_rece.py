# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Yapo2017- cAMP/PKA signalling in D1 dopamine receptor expressing medium-spiny neurons."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yapo2017CampPkaSignallingInD1DopamineReceModel(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL1701170000'
    _TITLE = 'Yapo2017- cAMP/PKA signalling in D1 dopamine receptor expressing medium-spiny neurons'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'golf_g_protein': ('mw351f6cee_3e64_4b8e_8e60_24b1aca99a92',
                        'native SBML value',
                        'Golf G protein. Maps to SBML symbol `mw351f6cee_3e64_4b8e_8e60_24b1aca99a92` '
                        'and is emitted in native SBML units.'),
     'camp': ('mw1c97b02d_169a_4eb8_bc84_1be57c51a255',
              'native SBML value',
              'cAMP. Maps to SBML symbol `mw1c97b02d_169a_4eb8_bc84_1be57c51a255` and is emitted in '
              'native SBML units.'),
     'source_defined_ac5_state': ('mw724f1afe_8032_40ae_96ca_808ab7b8b943',
                                  'native SBML value',
                                  'source-defined AC5 state. Maps to SBML symbol '
                                  '`mw724f1afe_8032_40ae_96ca_808ab7b8b943` and is emitted in native '
                                  'SBML units.')}
    _INITIAL_CONDITION_INPUTS = {'initial_amp': ('mw9710c658_a2a1_4f49_b494_af109853f251',
                     0.0,
                     'native SBML value',
                     'Initial level of AMP. Maps to SBML symbol '
                     '`mw9710c658_a2a1_4f49_b494_af109853f251`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_atp': ('mw46dccec6_6f0f_40f6_a10c_2f34ae7a005a',
                     5000000.0,
                     'native SBML value',
                     'Initial level of ATP. Maps to SBML symbol '
                     '`mw46dccec6_6f0f_40f6_a10c_2f34ae7a005a`; exposed as a traceable '
                     'initial-condition perturbation.'),
     'initial_calcium': ('mwccd3a17c_e207_4663_9b16_327b78882497',
                         60.0,
                         'native SBML value',
                         'Initial level of calcium. Maps to SBML symbol '
                         '`mwccd3a17c_e207_4663_9b16_327b78882497`; exposed as a traceable '
                         'initial-condition perturbation.')}
    _PARAMETER_INPUTS = {}
    _SPECIES_LABELS = {'mwfed0682b_39f1_4b09_94e8_c45a51744092': 'Gaolf GDP',
     'mwaf471bc1_f98a_4115_b0ee_45c189ea20b5': 'Gbgolf',
     'mw8e34c23f_1891_4dc9_8f97_dc2f12a1706c': 'Gaolf GTP',
     'mw6b2f1c44_e0be_4406_bcef_ad5061d519e4': 'D1rdagolf',
     'mw351f6cee_3e64_4b8e_8e60_24b1aca99a92': 'Golf G protein',
     'mw0b46978f_b522_4cde_97f0_574cd7dbbae7': 'D1rgolf',
     'mwdb9dc389_2bf0_4039_9f09_282f5511958b': 'D1RDA',
     'mwe2fc02e6_2684_4071_932a_f7a8bd13b2fe': 'D1R',
     'mw1c97b02d_169a_4eb8_bc84_1be57c51a255': 'cAMP',
     'mwccd3a17c_e207_4663_9b16_327b78882497': 'calcium',
     'mw724f1afe_8032_40ae_96ca_808ab7b8b943': 'source-defined AC5 state',
     'mwfe9ed415_d5af_469c_a549_d8981f1eb01f': 'Ac5gaolf GTP',
     'mw4b358131_010c_4545_ac4a_13a6c8bc34c4': 'calmodulin',
     'mw65a14789_ffcf_4bfd_9d53_d2eb2f4d0896': 'calcium Mca2',
     'mw8a4a0733_64dd_4474_9aaf_7d750b27ae5b': 'calcium Mca4',
     'mwc783c5e7_7bc8_425a_9bb6_1f01d463365c': 'source-defined PKA state',
     'mw74e54eed_0d25_4fb0_b677_1192f238c03b': 'Pkac AMP2',
     'mwffd5a553_8e03_443d_a67e_0cf39d03f89f': 'Pkac AMP4',
     'mwcfcf2e7f_907a_4d25_812f_6c10a7293859': 'Pkareg',
     'mw68d3f409_9462_4515_8c07_bc105fa0eaf1': 'source-defined PKAC state',
     'mw25023179_9334_438e_bf3e_4e850f84406a': 'PP2B',
     'mw4855b1cd_d7bc_4072_9736_dca30bbe448d': 'Pp2bc',
     'mwfaf786e2_00b7_4e0c_b164_5aa1f4ef6356': 'Pp2bca M',
     'mwd1171b65_ed6c_4413_bf47_5ed80038a7bd': 'Pp2bca Mca2',
     'mw24435476_9c30_4878_b26f_4b3c5a0685c6': 'DARPP32',
     'mw4179e1ff_9035_4c67_a67c_099e25beb9b0': 'Pkac D32',
     'mw2f3e9c55_e57f_416e_b4b1_cc49a26192c0': 'D32p34',
     'mw522cacf1_5e61_4b95_8742_cf61cb824893': 'B72PP2A',
     'mwe8cc261d_af39_4e88_8a65_a4994dcea2ff': 'Pkac B56PP2A',
     'mw9417144e_14b1_40d9_bd4b_ccd9f4714305': 'B56pp2ap',
     'mw32351ce4_eaaf_4827_8efa_342224548d8a': 'source-defined CDK5 state',
     'mw06380287_79c9_4f85_aed6_fa34e7bcdff1': 'source-defined PP1 state',
     'mw0130a500_18e9_470f_9fac_70af44dc4a9e': 'CDK5 D32',
     'mw1184c368_03fc_435a_9086_dc6ed3067935': 'D32p75',
     'mwb320746f_6a8c_4c8b_ae55_23db454339d8': 'Pkac D32p75',
     'mw3fcd1ec2_a459_49d4_89f7_361e276096d6': 'B72ppa2ca',
     'mw3a3e53fb_bbbf_4433_9f75_a12610dbc312': 'B56pp2ap D32p75',
     'mw0459271f_3b39_40a4_948f_aed773482cfc': 'B72PP2A D32p75',
     'mw9bfd7713_4c48_492c_8583_006bf1b54a1b': 'B72pp2aca D32p75',
     'mwc57c3c2e_69d5_4336_aff5_d1f429420df2': 'Pp1d32p34',
     'mwcf1bb70c_9d0b_4e82_b58a_6f8e73208af9': 'Pp2bc D32p34',
     'mwbe974953_e869_4622_b4a8_745555c8d7fd': 'source-defined DA state',
     'mw9710c658_a2a1_4f49_b494_af109853f251': 'AMP',
     'mw081c9f7b_011e_440f_971d_d0316d2a1e6c': 'B56PP2A',
     'mwde741b91_d5bf_44a9_ad45_404d7259d051': 'B56PP2A D32p75',
     'mw3d9e6efb_8e12_49c9_a87f_e067914b951d': 'PDE10',
     'mw6e845d87_603e_4463_874d_866f554303df': 'PDE10 C AMP',
     'mw46dccec6_6f0f_40f6_a10c_2f34ae7a005a': 'ATP',
     'mw166e3335_56c3_41ef_af0f_b583860991c1': 'Ac5gaolf GTP ATP',
     'mw7086a13a_619e_4069_b163_d8a05fc55f42': 'AC5 ATP',
     'mw248002d1_aee0_4905_b013_252fa970dab0': 'Total active PKA',
     'mwdb407128_2e73_4988_a7fe_4410a964fcde': 'Total active PP1',
     'mw2cbc8461_db79_4c83_ab0b_4894c28f66e5': 'source-defined AKAR3 state',
     'mw323eab0d_c3e7_469f_8f83_ced6f0b34f47': 'Akar3p',
     'mw2fde5e42_278d_484f_b4b5_5e53ac9fd85c': 'PP1 Akar3p',
     'mw8574bd14_b18a_4a80_ba13_7c988ed786b6': 'Pkac AKAR3',
     'mwd306ba1d_8c96_4747_a8e7_3cd9c6b3b351': 'Total Akar3p',
     'mwce1fc5cd_3b9f_48e1_935d_17f9f1724684': 'EPAC C AMP',
     'mw364316fa_d429_4d47_91d8_8964c1f20abb': 'source-defined EPAC state'}
    _STATE_OUTPUT_ALIASES = {'mwfed0682b_39f1_4b09_94e8_c45a51744092': 'gaolf_gdp',
     'mwaf471bc1_f98a_4115_b0ee_45c189ea20b5': 'gbgolf',
     'mw8e34c23f_1891_4dc9_8f97_dc2f12a1706c': 'gaolf_gtp',
     'mw6b2f1c44_e0be_4406_bcef_ad5061d519e4': 'd1rdagolf',
     'mw351f6cee_3e64_4b8e_8e60_24b1aca99a92': 'golf_g_protein',
     'mw0b46978f_b522_4cde_97f0_574cd7dbbae7': 'd1rgolf',
     'mwdb9dc389_2bf0_4039_9f09_282f5511958b': 'd1rda',
     'mwe2fc02e6_2684_4071_932a_f7a8bd13b2fe': 'd1r',
     'mw1c97b02d_169a_4eb8_bc84_1be57c51a255': 'camp',
     'mwccd3a17c_e207_4663_9b16_327b78882497': 'calcium',
     'mw724f1afe_8032_40ae_96ca_808ab7b8b943': 'source_defined_ac5_state',
     'mwfe9ed415_d5af_469c_a549_d8981f1eb01f': 'ac5gaolf_gtp',
     'mw4b358131_010c_4545_ac4a_13a6c8bc34c4': 'calmodulin',
     'mw65a14789_ffcf_4bfd_9d53_d2eb2f4d0896': 'calcium_mca2',
     'mw8a4a0733_64dd_4474_9aaf_7d750b27ae5b': 'calcium_mca4',
     'mwc783c5e7_7bc8_425a_9bb6_1f01d463365c': 'source_defined_pka_state',
     'mw74e54eed_0d25_4fb0_b677_1192f238c03b': 'pkac_amp2',
     'mwffd5a553_8e03_443d_a67e_0cf39d03f89f': 'pkac_amp4',
     'mwcfcf2e7f_907a_4d25_812f_6c10a7293859': 'pkareg',
     'mw68d3f409_9462_4515_8c07_bc105fa0eaf1': 'source_defined_pkac_state',
     'mw25023179_9334_438e_bf3e_4e850f84406a': 'pp2b',
     'mw4855b1cd_d7bc_4072_9736_dca30bbe448d': 'pp2bc',
     'mwfaf786e2_00b7_4e0c_b164_5aa1f4ef6356': 'pp2bca_m',
     'mwd1171b65_ed6c_4413_bf47_5ed80038a7bd': 'pp2bca_mca2',
     'mw24435476_9c30_4878_b26f_4b3c5a0685c6': 'darpp32',
     'mw4179e1ff_9035_4c67_a67c_099e25beb9b0': 'pkac_d32',
     'mw2f3e9c55_e57f_416e_b4b1_cc49a26192c0': 'd32p34',
     'mw522cacf1_5e61_4b95_8742_cf61cb824893': 'b72pp2a',
     'mwe8cc261d_af39_4e88_8a65_a4994dcea2ff': 'pkac_b56pp2a',
     'mw9417144e_14b1_40d9_bd4b_ccd9f4714305': 'b56pp2ap',
     'mw32351ce4_eaaf_4827_8efa_342224548d8a': 'source_defined_cdk5_state',
     'mw06380287_79c9_4f85_aed6_fa34e7bcdff1': 'source_defined_pp1_state',
     'mw0130a500_18e9_470f_9fac_70af44dc4a9e': 'cdk5_d32',
     'mw1184c368_03fc_435a_9086_dc6ed3067935': 'd32p75',
     'mwb320746f_6a8c_4c8b_ae55_23db454339d8': 'pkac_d32p75',
     'mw3fcd1ec2_a459_49d4_89f7_361e276096d6': 'b72ppa2ca',
     'mw3a3e53fb_bbbf_4433_9f75_a12610dbc312': 'b56pp2ap_d32p75',
     'mw0459271f_3b39_40a4_948f_aed773482cfc': 'b72pp2a_d32p75',
     'mw9bfd7713_4c48_492c_8583_006bf1b54a1b': 'b72pp2aca_d32p75',
     'mwc57c3c2e_69d5_4336_aff5_d1f429420df2': 'pp1d32p34',
     'mwcf1bb70c_9d0b_4e82_b58a_6f8e73208af9': 'pp2bc_d32p34',
     'mwbe974953_e869_4622_b4a8_745555c8d7fd': 'source_defined_da_state',
     'mw9710c658_a2a1_4f49_b494_af109853f251': 'amp',
     'mw081c9f7b_011e_440f_971d_d0316d2a1e6c': 'b56pp2a',
     'mwde741b91_d5bf_44a9_ad45_404d7259d051': 'b56pp2a_d32p75',
     'mw3d9e6efb_8e12_49c9_a87f_e067914b951d': 'pde10',
     'mw6e845d87_603e_4463_874d_866f554303df': 'pde10_c_amp',
     'mw46dccec6_6f0f_40f6_a10c_2f34ae7a005a': 'atp',
     'mw166e3335_56c3_41ef_af0f_b583860991c1': 'ac5gaolf_gtp_atp',
     'mw7086a13a_619e_4069_b163_d8a05fc55f42': 'ac5_atp',
     'mw248002d1_aee0_4905_b013_252fa970dab0': 'total_active_pka',
     'mwdb407128_2e73_4988_a7fe_4410a964fcde': 'total_active_pp1',
     'mw2cbc8461_db79_4c83_ab0b_4894c28f66e5': 'source_defined_akar3_state',
     'mw323eab0d_c3e7_469f_8f83_ced6f0b34f47': 'akar3p',
     'mw2fde5e42_278d_484f_b4b5_5e53ac9fd85c': 'pp1_akar3p',
     'mw8574bd14_b18a_4a80_ba13_7c988ed786b6': 'pkac_akar3',
     'mwd306ba1d_8c96_4747_a8e7_3cd9c6b3b351': 'total_akar3p',
     'mwce1fc5cd_3b9f_48e1_935d_17f9f1724684': 'epac_c_amp',
     'mw364316fa_d429_4d47_91d8_8964c1f20abb': 'source_defined_epac_state'}

    def __init__(self, model_path: str = 'data/MODEL1701170000.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Yapo2017CampPkaSignallingInD1DopamineReceModel1701170000Model = Yapo2017CampPkaSignallingInD1DopamineReceModel
