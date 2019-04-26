# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:24:02 2019

@author: Vitor
"""

ano = int(input('Em que ano você nasceu? '))
if 2019-ano > 18:
    print('Quem nasceu em {} tem ou terá {} anos'.format(ano,2019-ano))
    if 2019 - ano == 19:
        print('Deveria ter se alistado ano passado')
    else:
        print('deveria ter se alistado a {} anos'.format(2001-ano))
    print('seu alistamento foi em {}'.format(ano+18))
elif 2019-ano < 18:
    print('Quem nasceu em {} tem ou terá {} anos'.format(ano,2019-ano))
    print('seu alistamento será em {}'.format(ano+18))
else:
    print('Você tem ou terá 18 anos esse ano!')
    print('Seu alistamento deverá ser feito IMEDIATAMENTE!')