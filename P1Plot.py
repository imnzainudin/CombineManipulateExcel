import pandas as pd
import os

class P1P():
    def __init__(self,filters=None):
        ori_path = r'C:\Users\mzainudx\OneDrive - Intel Corporation\Desktop\SMV_1D_Phase1_DataIn\test_data\combine_file'
        filename = 'COMBINE.csv'
        path = os.path.join(ori_path, filename)

        df = pd.read_csv(path, na_filter=False, header=None, encoding= 'unicode_escape',low_memory=False)
        self.filter_first_column = df[df.iloc[:, 0].str.startswith(filters)]
        print(self.filter_first_column)

    def add_input(self,condition=None,sheetname=None):
        result_path = r'C:\Users\mzainudx\OneDrive - Intel Corporation\Desktop\SMV_1D_Phase1_DataIn\test_data\Result_compilation'
        compilation_path = condition
        result_compilation_path = os.path.join(result_path,compilation_path)
        print(result_compilation_path)

        df = pd.read_excel(result_compilation_path,header=None)
        print(df)
        
        last_row = df.iloc[-1:].index.values
        if not last_row:
            last_row = [0]

        print(last_row)

        with pd.ExcelWriter(result_compilation_path, engine='openpyxl', mode='a',if_sheet_exists="overlay") as workbook:
            # print(lastrow)
            for lastrow in last_row:
                self.filter_first_column.to_excel(workbook,sheet_name=sheetname, startrow=lastrow+1, index=False,header=False)

# data = P1P(filters='AVK_SMV_1D_Disc_RX-UDFE_RX')
# data.add_input(condition='AVK_SMV_1D_Disc-RXUDFE-Unmatch_LP5.xlsx',sheetname='1D_Disc-RXUDFE')
