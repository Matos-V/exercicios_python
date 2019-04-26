# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:47:41 2019

@author: Vitor
"""

primo = True
n = int(input('digite um numero: '))
for x in range(2,n):
    if n%x == 0:
        primo = False
if primo:
    print('{} é um numero primo!'.format(n))
else:
    print('{} não é um número primo!'.format(n))