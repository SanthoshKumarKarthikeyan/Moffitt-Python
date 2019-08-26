# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:55:55 2019

@author: 80018096
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
import pandas as pd
import xlrd
from PIL import Image
heat_df = pd.read_excel('Top150genes_mutandnonmutsamples.xlsx')
A = list(heat_df['sample'])
print(A)
df = heat_df[heat_df.columns.values[1:]]
fig, ax = plt.subplots()
im = ax.imshow(df,cmap='seismic')
#ax.set_xticks(np.arange(len(farmers)))
#ax.set_yticks(np.arange(len(vegetables)))
#ax.set_xticklabels(farmers)
ax.set_yticklabels(A)