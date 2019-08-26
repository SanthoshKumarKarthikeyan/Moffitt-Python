# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:38:53 2019

@author: 80018096
"""

import matplotlib.pyplot as plt
import math
import pandas as pd
import xlrd
pca_df = pd.read_excel('PCA_results_T.xlsx')
A = list(pca_df['PC1'])
B = list(pca_df['PC2'])
A1 = list(A[:76])
A2 = list(A[76:])
B1 = list(B[:76])
B2 = list(B[76:])
plt.plot([A1],[B1], 'r^')
plt.plot([A2],[B2],'g^')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PC1 vs PC2 STK11')
plt.show()
