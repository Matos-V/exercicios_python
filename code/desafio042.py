# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:28:30 2019

@author: Vitor
"""

l1 = float(input('digite os comprimentos dos lados do triangulo: l1 = '))
l2 = float(input('l2 = '))
l3 = float(input('l3 = '))
l = [l1,l2,l3]
L = sorted(l)
if L[2]>(L[1]+L[0]):
    print('Isso nem é triangulo')
if (L[2] == L[1]) & (L[2] == L[0]):
    print('é um triangulo equilatero')
elif (L[2] == L[1]) | (L[2] == L[0]) | (L[1] == L[0]):
    print('é um triangulo isósceles')
else:
    print('é um triangulo escaleno')