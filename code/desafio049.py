# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:23:51 2019

@author: Vitor
"""

n = int(input('Digite o número para a sua tabuada: '))

for x in range(1,11):
    print('{} x {:2} = {}'.format(n,x,n*x))