# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:46:00 2019

@author: Vitor
"""

kg = float(input('qual o seu peso em kg? '))
h = float(input('qual a sua altura em metros? '))
imc = kg/(h**2)

if imc < 18.5:
    print('seu imc é {} e vc está abaixo do peso!'.format(imc))

elif imc < 25.0:
    print('seu imc é {} e vc está no peso ideal!'.format(imc))
    
elif imc < 30.0:
    print('seu imc é {} e vc está com sobrepeso!'.format(imc))
    
elif imc < 40.0:
    print('seu imc é {} e vc está com obesidade!'.format(imc))
    
else:
    print('seu imc é {} e vc está com obesidade mórbida!'.format(imc))