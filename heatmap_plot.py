# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:35:00 2019

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
heat_df = df.as_matrix()
print (heat_df)
ax.set_xticklabels(A)
plt.imshow(heat_df, cmap='hot', interpolation='nearest')
plt.show()