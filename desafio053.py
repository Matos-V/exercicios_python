# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:19:13 2019

@author: Vitor
"""

nome = str(input('Digite uma palavra ou frase: ')).strip()
nome = nome.replace(' ','')
nome = nome.upper()
nome2 = ''

for x in range(len(nome)-1,-1,-1):
    nome2 += nome[x]
    
print('O inverso de {} é {}'.format(nome,nome2))
if nome == nome2:
    print('Então a palavra é um palíndromo!')
else:
    print('então a palavra não é um palíndromo')