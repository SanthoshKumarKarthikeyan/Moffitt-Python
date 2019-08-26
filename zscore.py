# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:34:14 2019

@author: 80018096
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
import pandas as pd
import xlrd
from scipy import stats

zscore_df = pd.read_excel('TCGA_STK11.xlsx')
df = zscore_df[zscore_df.columns.values[1:]]
print(df)
b = stats.zscore(df)
#print(b)
#b_df = b[]
writer = pd.ExcelWriter('Zscore_results_TCGA_STK11.xlsx')
pd.DataFrame(b).to_excel(writer, 'Results')
writer.save()