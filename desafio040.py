# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:40:34 2019

@author: Vitor
"""

n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
media = (n1+n2)/2
if media < 5:
    print('sua media foi {}'.format(media))
    print('Situação: reprovado')
elif media < 7:
    print('sua media foi {}'.format(media))
    print('Situação: recuperação')
else:
    print('sua media foi {}'.format(media))
    print('Situação: aprovado')