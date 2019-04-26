# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:43:38 2019

@author: Vitor
"""
import numpy as np
n = 0
y = 0
a = np.arange(1,501)

for x in range(1,501):
    if (x%3 == 0) & (x%2 == 1):
        y = y + x
        n = n + 1

print('soma dos {} numeros é igual a {}'.format(n,y))