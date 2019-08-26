# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 18:49:42 2019

@author: Santhosh Kumar K
"""

import math
import pandas as pd
import xlrd

rna_df = pd.read_excel('RNA_SEQ.xlsx')
toppvaluegene_df = pd.read_excel('Top150genes.xlsx')
topgeneList = list(toppvaluegene_df['Genes'])
topgeneList
rna_top5Genes = rna_df.set_index('sample').loc[topgeneList]
writer = pd.ExcelWriter('Top150genes.xlsx')
rna_top5Genes.to_excel(writer,'Result')
writer.save()