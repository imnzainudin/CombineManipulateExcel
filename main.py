def main(condition_list=None):
    from P1Plot import P1P
    # condition_list = ['AVK_SMV_1D_Disc-RXBIAS_LP5.xlsx','AVK_SMV_1D_Disc-RxBiasRload_LP5.xlsx','AVK_SMV_1D_Disc-TXEQ_LP5.xlsx','AVK_SMV_1D_Disc-RX-ODT_LP5.xlsx',
    #                     'AVK_SMV_1D_Disc-TX-RON_LP5.xlsx','AVK_SMV_1D_Disc_TX-DQ-TCO_LP5.xlsx','AVK_SMV_1D_Disc_TX-DQS-TCO_LP5.xlsx']
    for condition in condition_list:
        if condition =='AVK_SMV_1D_Disc-RXUDFE-Unmatch_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_RX-UDFE_RX'
            sheetname = '1D_Disc-RXUDFE'
            print('=======================RXUDFE=========================')

        elif condition =='AVK_SMV_1D_Disc-RXDQSCTLE-Match_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_RX-DQSCTLE_RX'
            sheetname = '1D_Disc-RXDQSCTLE'
            print('=======================RXDQSCTLE=========================')

        elif condition =='AVK_SMV_1D_Disc-RXBIAS_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_RX-BIAS_RX'
            sheetname = '1D_Disc-RXBIAS'
            print('=======================RXBIAS=========================')

        elif condition =='AVK_SMV_1D_Disc-RxBiasRload_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_Rx-BiasRload'
            sheetname = '1D_Disc-RxBiasRload'
            print('=======================RXBIAS_Rload=========================')

        elif condition =='AVK_SMV_1D_Disc-TXEQ_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_TX-EQ_TX'
            sheetname = '1D_Disc-TXEQ'
            print('=======================TXEQ=========================')

        elif condition =='AVK_SMV_1D_Disc-RX-ODT_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_RX-ODT'
            sheetname = '1D_Disc-RX-ODT'
            print('=======================RXODT=========================')

        elif condition =='AVK_SMV_1D_Disc-TX-RON_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_TX-RON'
            sheetname = '1D_Disc-TX-RON'
            print('=======================TXRON=========================')

        elif condition =='AVK_SMV_1D_Disc_TX-DQ-TCO_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_TX-DQTCO'
            sheetname = '1D_Disc-TX-DQ-TCO'
            print('=======================TXDQTCO=========================')

        elif condition =='AVK_SMV_1D_Disc_TX-DQS-TCO_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_TX-DQSTCO'
            sheetname = '1D_Disc-TX-DQS-TCO'
            print('=======================TXDQSTCO=========================')

        elif condition =='AVK_SMV_1D_Disc-CMD_EQ_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_CMD-EQ_CMD'
            sheetname = '1D_Disc-CMDEQ'
            print('=======================TXCMDEQ=========================')

        elif condition =='AVK_SMV_1D_Disc_TXRXWCK_TCO_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_TXRX-WCKTCO'
            sheetname = '1D_Disc-WCKTCO'
            print('=======================TXRXWCKTO=========================')

        elif condition =='AVK_SMV_1D_Disc-CLK_TCO_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_CLK-TCO_RX'
            sheetname = '1D_Disc-CMDCLKTCO'
            print('=======================CLKTCO=========================')

        elif condition =='AVK_SMV_1D_Disc-CMD_TCO_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_CCC-CMDTCO_CMD'
            sheetname = '1D_Disc-CMDTCO'
            print('=======================CMDTCO=========================')

        elif condition =='AVK_SMV_1D_Disc-CMD_SlewRate_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_CCC-SlewRate_CMD'
            sheetname = '1D_Disc-CMDSlewRate'
            print('=======================CMDSlewRate=========================')

        elif condition =='AVK_SMV_1D_Disc-CMD-RON_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_CMD-RON'
            sheetname = '1D_Disc-CMD-RON'
            print('=======================CMDRON=========================')

        elif condition =='AVK_SMV_1D_Disc-DRAM-CA-ODT_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_DRAMCCCODT'
            sheetname = 'Dram_CA-ODT'
            print('=======================DRAMCAODT=========================')

        elif condition =='AVK_SMV_1D_Disc-DRAM-RON_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_DRAMRON'
            sheetname = 'Dram_RON_RX'
            print('=======================DRAMRON=========================')

        elif condition =='AVK_SMV_1D_Disc-DRAM-DQ-ODT_LPR5.xlsx':
            filters = 'AVK_SMV_1D_Disc_DRAMODT_TX'
            sheetname = 'Dram_DQ-ODT'
            print('=======================DRAMDQOCT=========================')

        elif condition =='AVK_SMV_1D_Disc-DRAM-WCK-ODT_LP5.xlsx':
            filters = 'AVK_SMV_1D_Disc_DRAMWCKODT'
            sheetname = 'Dram_WCK-ODT'
            print('=======================DRAMWCKODT=========================')

        else:
            continue

        data = P1P(filters=filters)
        data.add_input(condition=condition,sheetname=sheetname)