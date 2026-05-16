# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: MIT
"""Tellurium-backed SBML wrapper for Basak_Cell_2007."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class BasakCell2007Model(TelluriumSBMLBioModule):
    """Faithful Tellurium execution of the bundled SBML source model."""

    _SBML_ID = 'MODEL8478881246'
    _TITLE = 'Basak_Cell_2007'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _EXPOSE_INTEGRATION_STEP_INPUT = False
    _HEADLINE_OUTPUTS = {'ik_ba_nfk_b': ('mwB5B12B45_0F61_44BD_9781_989D8B015906',
                     'MWPREFIXUNIT_micromole',
                     'Ik Ba Nfk B. Maps to SBML symbol `mwB5B12B45_0F61_44BD_9781_989D8B015906` and is '
                     'emitted in native SBML units.'),
     'ik_ba_nfk_bn': ('mwA7D14F2B_20BE_4FF7_83B7_8B24C34D94A6',
                      'MWPREFIXUNIT_micromole',
                      'Ik Ba Nfk Bn. Maps to SBML symbol `mwA7D14F2B_20BE_4FF7_83B7_8B24C34D94A6` and '
                      'is emitted in native SBML units.'),
     'ik_ba_ikknfk_b': ('mw67E597F5_E642_45A3_A377_0BD9CE41467B',
                        'MWPREFIXUNIT_micromole',
                        'Ik Ba Ikknfk B. Maps to SBML symbol `mw67E597F5_E642_45A3_A377_0BD9CE41467B` '
                        'and is emitted in native SBML units.')}
    _INITIAL_CONDITION_INPUTS = {}
    _PARAMETER_INPUTS = {'initial_a_c_2pnq_level': ('mw67DBC35D_6ABA_4E03_A921_AA3E88FCDA17',
                                4.2,
                                'per_uM_per_min',
                                'A C 2pnq source parameter. Maps to SBML symbol '
                                '`mw67DBC35D_6ABA_4E03_A921_AA3E88FCDA17` and preserves the bundled '
                                'default.')}
    _SPECIES_LABELS = {'mw19ABBAB9_033D_45B4_89B0_1173C750EF0F': 'Ik Bat',
     'mwA05350ED_74C7_4D0A_8F6B_B721B3D9E44E': 'source-defined IKBA state',
     'mw124FBB79_9937_4631_B70F_17512CD6BE95': 'Ik Ban',
     'mwEC71C2D7_4FC4_4D3C_B099_8CC05CD5361E': 'Ik Ba IKK',
     'mwB5B12B45_0F61_44BD_9781_989D8B015906': 'Ik Ba Nfk B',
     'mwA7D14F2B_20BE_4FF7_83B7_8B24C34D94A6': 'Ik Ba Nfk Bn',
     'mw67E597F5_E642_45A3_A377_0BD9CE41467B': 'Ik Ba Ikknfk B',
     'mw1DF2B13D_BF44_4896_9AC6_554C12929DBB': 'NF-kB',
     'mw1C5A01D2_C490_429F_9B15_7A0246F16CDD': 'source-defined IKK2 state',
     'mw807513FD_512B_4B7D_B297_31F8E5FDB3EA': 'Nfk Bn',
     'mw171FF6BD_54E3_440D_AD36_6C127E5F5A18': 'source-defined IKK1 state',
     'mw5B93183E_9221_4104_850B_679B8EDE5D7D': 'Ik complement factor Bb IKK',
     'mw1A1F1D84_F419_4E1B_AD93_FCD15689B185': 'Ik complement factor Bb Ikknfk B',
     'mwBBB3546E_7D79_4382_B60F_D01B602988E5': 'Ik complement factor Bb Nfk Bn',
     'mw572EB043_9C5E_4679_B2C4_C1BBC358A670': 'Ik complement factor Bb Nfk B',
     'mwEA317F18_0AF8_452F_B4F6_F61C308092D7': 'Ik Bbn',
     'mwF092F3EF_E400_41EA_9937_B9308631961D': 'source-defined IKBB state',
     'mw4E1A652C_4BB8_4005_ACEF_0D7B8AD3E76D': 'Ik Bbt',
     'mw3A36107D_B022_4E96_8F5C_DE79794A8D15': 'Ik Bet',
     'mw552B855A_A60D_4BF6_8434_4E4FB8D052D0': 'source-defined IKBE state',
     'mw0F6EFE80_312A_4680_9FF3_B165FAFD19C8': 'Ik Ben',
     'mwEEA2DEF3_8860_4318_83FB_C798C715DCFE': 'Ik Be Nfk B',
     'mwE5D6951D_2500_4DEE_AC30_6C413267A867': 'Ik Be Nfk Bn',
     'mw9D25D350_B758_45F9_8CD7_2D474639A826': 'Ik Be Ikknfk B',
     'mw1BEBD247_3F43_41C8_8F32_D14E332E62A8': 'Ik Be IKK',
     'mwE1F2CEA4_DEC3_41D9_998F_4F78D61BEAE8': 'P100IKK1',
     'mw4AFF3981_A98D_458E_971E_2B0E42EFAE8F': 'P100ikk1nfk B',
     'mw7552004F_E763_4D5C_8110_F907EC909679': 'P100nfk Bn',
     'mw0B4B042A_7998_4874_8240_64407B7B008A': 'P100nfk B',
     'mw8424C3D4_C230_48AA_A166_AC9CBD2F8CF6': 'P100n',
     'mw8F6EBB6C_78A7_46A1_8805_18993C85ECCC': 'Abstract source state P100',
     'mw8F36FAC3_F3D4_4951_B279_F14D69873B90': 'P100t'}
    _STATE_OUTPUT_ALIASES = {'mw19ABBAB9_033D_45B4_89B0_1173C750EF0F': 'ik_bat',
     'mwA05350ED_74C7_4D0A_8F6B_B721B3D9E44E': 'source_defined_ikba_state',
     'mw124FBB79_9937_4631_B70F_17512CD6BE95': 'ik_ban',
     'mwEC71C2D7_4FC4_4D3C_B099_8CC05CD5361E': 'ik_ba_ikk',
     'mwB5B12B45_0F61_44BD_9781_989D8B015906': 'ik_ba_nfk_b',
     'mwA7D14F2B_20BE_4FF7_83B7_8B24C34D94A6': 'ik_ba_nfk_bn',
     'mw67E597F5_E642_45A3_A377_0BD9CE41467B': 'ik_ba_ikknfk_b',
     'mw1DF2B13D_BF44_4896_9AC6_554C12929DBB': 'nfkb',
     'mw1C5A01D2_C490_429F_9B15_7A0246F16CDD': 'source_defined_ikk2_state',
     'mw807513FD_512B_4B7D_B297_31F8E5FDB3EA': 'nfk_bn',
     'mw171FF6BD_54E3_440D_AD36_6C127E5F5A18': 'source_defined_ikk1_state',
     'mw5B93183E_9221_4104_850B_679B8EDE5D7D': 'ik_complement_factor_bb_ikk',
     'mw1A1F1D84_F419_4E1B_AD93_FCD15689B185': 'ik_complement_factor_bb_ikknfk_b',
     'mwBBB3546E_7D79_4382_B60F_D01B602988E5': 'ik_complement_factor_bb_nfk_bn',
     'mw572EB043_9C5E_4679_B2C4_C1BBC358A670': 'ik_complement_factor_bb_nfk_b',
     'mwEA317F18_0AF8_452F_B4F6_F61C308092D7': 'ik_bbn',
     'mwF092F3EF_E400_41EA_9937_B9308631961D': 'source_defined_ikbb_state',
     'mw4E1A652C_4BB8_4005_ACEF_0D7B8AD3E76D': 'ik_bbt',
     'mw3A36107D_B022_4E96_8F5C_DE79794A8D15': 'ik_bet',
     'mw552B855A_A60D_4BF6_8434_4E4FB8D052D0': 'source_defined_ikbe_state',
     'mw0F6EFE80_312A_4680_9FF3_B165FAFD19C8': 'ik_ben',
     'mwEEA2DEF3_8860_4318_83FB_C798C715DCFE': 'ik_be_nfk_b',
     'mwE5D6951D_2500_4DEE_AC30_6C413267A867': 'ik_be_nfk_bn',
     'mw9D25D350_B758_45F9_8CD7_2D474639A826': 'ik_be_ikknfk_b',
     'mw1BEBD247_3F43_41C8_8F32_D14E332E62A8': 'ik_be_ikk',
     'mwE1F2CEA4_DEC3_41D9_998F_4F78D61BEAE8': 'p100ikk1',
     'mw4AFF3981_A98D_458E_971E_2B0E42EFAE8F': 'p100ikk1nfk_b',
     'mw7552004F_E763_4D5C_8110_F907EC909679': 'p100nfk_bn',
     'mw0B4B042A_7998_4874_8240_64407B7B008A': 'p100nfk_b',
     'mw8424C3D4_C230_48AA_A166_AC9CBD2F8CF6': 'p100n',
     'mw8F6EBB6C_78A7_46A1_8805_18993C85ECCC': 'abstract_source_state_p100',
     'mw8F36FAC3_F3D4_4951_B279_F14D69873B90': 'p100t'}

    def __init__(self, model_path: str = 'data/MODEL8478881246.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


BasakCell2007Model8478881246Model = BasakCell2007Model
