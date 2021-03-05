# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:14:26 2019

@author: Vitor
"""

ano = int(input('digite o ano em que vc nasceu: '))
idade = 2019-ano
if idade <= 9:
    print('vc tem {} anos e sua categoria é MIRIM!'.format(idade))
elif idade <= 14:
    print('vc tem {} anos e sua categoria é INFANTIL!'.format(idade))
elif idade <= 19:
    print('vc tem {} anos e sua categoria é JUNIOR!'.format(idade))
elif idade <= 25:
    print('vc tem {} anos e sua categoria é ADULTO!'.format(idade))
else:
    print('vc tem {} anos e sua categoria é SÊNIOR!'.format(idade))