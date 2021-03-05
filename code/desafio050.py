# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:32:20 2019

@author: Vitor
"""

soma = 0
cont = 0

for x in range(1,7):
    n = int(input('digite o {}º valor: '.format(x)))
    if n%2 == 0:
        soma += n
        cont += 1
print('vc digitou {} numeros pares e a soma deles é {}'.format(cont,soma))