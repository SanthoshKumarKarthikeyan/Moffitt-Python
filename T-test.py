from scipy import stats
import math
import pandas as pd
import xlrd
rna_df = pd.read_excel('RNA_SEQ.xlsx')
patient_mut = pd.read_excel('patient_mutandnon-mut_list.xlsx')
patient_mut = patient_mut[['Mut samples','Non-Mut samples']]
sampleList = []
sampleList.append('sample')
for sample in list(patient_mut['Mut samples'].values[:76]):
    sampleList.append(sample)
for sample in list(patient_mut['Non-Mut samples'].values):
    sampleList.append(sample)
sample_df = rna_df[sampleList]
writer = pd.ExcelWriter('samplesDF.xlsx')
sample_df.to_excel(writer,'Result')
writer.save()
#stats.ttest_ind(sample_df.iloc[0][1:76].values, sample_df.iloc[0][76:].values, equal_var = False)
#result = pd.DataFrame(columns=["Gene", "statistic","pvalue"])
#for i in range(0,len(sample_df)):
 #   stat = stats.ttest_ind(sample_df.iloc[i][1:76].values, sample_df.iloc[i][76:].values, equal_var = False)
 #   result.set_value(sample_df.iloc[i][0], 0 if math.isnan(stat[0]) else stat[0],0 if math.isnan(stat[1]) else stat[1])
#writer = pd.ExcelWriter('FinalResult.xlsx')
#result.to_excel(writer,'Result')
#writer.save()

