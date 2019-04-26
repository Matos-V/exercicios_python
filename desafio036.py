# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:45:07 2019

@author: Vitor
"""
print('A condição é que a prestação mensal seja menor que 30% do seu sálario')
valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salário? '))
ano = int(input('em quantos anos será pago? '))

prest = valor/(12*ano)


if prest > 0.3*sal:
    print('serão prestações de {:.2f} reais e você ganha {:.2f}, logo o emprestimo foi negado!'.format(prest,sal))
else:
    print('serão prestações de {:.2f} reais e você ganha {:.2f}, logo o emprestimo foi aceito!'.format(prest,sal))