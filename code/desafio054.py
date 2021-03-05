# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:36:17 2019

@author: Vitor
"""

contM = 0
contm = 0

for x in range(1,8):
    n = int(input('em que ano a {}ª pessoa nasceu? '.format(x)))
    if (2019-n) < 18:
        contm += 1
    else:
        contM +=1
print('Das 7 pessoas, {} são maiores de idade e {} são menores de idade!'.format(contM,contm))