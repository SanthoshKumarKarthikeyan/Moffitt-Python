# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:31:48 2019

@author: 80018096
"""

from scipy import stats
import math
import pandas as pd
import xlrd

rna_df = pd.read_excel('CCLE_metabolism.xlsx')
patient_mut = pd.read_excel('CCLE_mutations.xlsx')
patient_mut = patient_mut[['STK11 mut and P53 mut']]
sampleList = []
sampleList.append('CCLE_ID')
for sample in list(patient_mut['STK11 mut and P53 mut'].values[:5]):
    sampleList.append(sample)
#for sample in list(patient_mut['STK11 mutant'].values[:35]):
 #   sampleList.append(sample)
sample_df = rna_df[sampleList]
writer = pd.ExcelWriter('STK11 mut and P53 mut_CCLE.xlsx')
sample_df.to_excel(writer,'Result')
writer.save()