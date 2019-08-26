# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:27:48 2019

@author: Santhosh Kumar K
"""

from scipy import stats
import math
import pandas as pd
import xlrd
rna_df = pd.read_excel('Top150genes.xlsx')
patient_mut = pd.read_excel('patient_mutandnon-mut_list.xlsx')
patient_mut = patient_mut[['Mut samples','Non-Mut samples']]
sampleList = []
sampleList.append('sample')
for sample in list(patient_mut['Mut samples'].values[:76]):
    sampleList.append(sample)
for sample in list(patient_mut['Non-Mut samples'].values):
    sampleList.append(sample)
sample_df = rna_df[sampleList]
sample_df = rna_df[sampleList]
writer = pd.ExcelWriter('Top150genes_mutandnonmutsamples.xlsx')
sample_df.to_excel(writer,'Result')
writer.save()