
import pandas as pd
import xlrd

mut_df = pd.read_excel('STK11_mut&non-mut.xlsx')
transposed_mut_df = mut_df.set_index('Gene ID').loc[['STK11']].T
patientList = list(transposed_mut_df[transposed_mut_df['STK11']==0].index)
rna_df = pd.read_excel('RNA_SEQ.xlsx')
transposed_rna_df = rna_df[rna_df['sample'] == 'STK11'].set_index('sample').T
result = transposed_rna_df.loc[patientList]
writer = pd.ExcelWriter('output1.xlsx')
result.to_excel(writer,'Result')
writer.save()

