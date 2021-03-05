# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:40:12 2019

@author: Vitor
"""

print('{} 10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA {} '.format('-','-'))
p1 = int(input('primeiro termo: '))
r = int(input('razão: '))

for x in range(0,10):
    print('{}º = {}'.format(x+1,p1+r*x))
