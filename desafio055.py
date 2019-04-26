# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:42:01 2019

@author: Vitor
"""

PM = 0
Pm = 0

for x in range(1,6):
    n = float(input('qual o peso da {}ª pessoa, em kg? '.format(x)))
    if x == 1:
        PM = n
        Pm = n
    if n > PM:
        PM = n
    if n < Pm:
        Pm = n
print('Das 5 pessoas, a mais pesada tem {}kg e a mais leve tem {}kg'.format(PM,Pm))
