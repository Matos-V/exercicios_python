# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:16:59 2019

@author: Vitor
"""

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite o segundo numero'))

if n1 < n2:
    print('o segundo numero é maior')
elif n2 < n1:
    print('o primeiro numero pe maior')
else:
    print('os numeros são iguais')