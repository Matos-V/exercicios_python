# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:53:13 2019

@author: Vitor
"""

compra = float(input('Qual o valor da sua compra? '))
print('FORMAS DE PAGAMENTO:')
print('1 - à vista no dinheiro/cheque')
print('2 - à vista no cartão')
print('3 - em 2 vezes no cartão')
print('4 - 3 vezes ou mais no cartão')
op = int(input('opção escolhida: '))

if op == 1:
    print('sua compra terá 10% de desconto então vc pagará {:.2f}'.format(0.9*compra))
elif op == 2:
    print('sua compra terá 5% de desconto então vc pagará {:.2f}'.format(0.95*compra))
elif op == 3:
    print('sua compra não terá desconto então vc pagará duas parcelas de {:.2f}'.format(compra/2))
else:
    p = int(input('numero de parcelas: '))
    print('sua compra terá 20% de juros então vc pagará {}, dividido em {} parcelas de {:.2f}'.format(1.2*compra,p,1.2*compra/p))