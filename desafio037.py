# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:56:02 2019

@author: Vitor
"""
import numpy as np

print('Conversor de bases decimais')
num = int(input('Digite o número em base decimal que será transformado: '))
print('1 - binário')
print('2 - octal')
print('3 - hexadecimal')
op = int(input('Escolha uma das opções acima: '))
if op == 1:
    print('{} em binario é {}'.format(num,bin(num)[2:]))
if op == 2:
    print('{} em octal é {}'.format(num,oct(num)[2:]))
if op == 3:
    print('{} em hexadecimal é {}'.format(num,hex(num).upper()[2:]))