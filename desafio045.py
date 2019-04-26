# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:04:56 2019

@author: Vitor
"""

import random as rd
import time as tm

pc = rd.randint(0,2)

print('0 - PEDRA')
print('1 - PAPEL')
print('2 - TESOURA')
player = int(input('Faça sua jogada: '))

if pc == 0:
    if player == 0:
        print('Computador jogou PEDRA!')
        print('Jogador jogou PEDRA!')
        tm.sleep(1)
        print('O JOGO DEU EMPAAATE!')
    if player == 1:
        print('Computador jogou PEDRA!')
        print('Jogador jogou PAPEL!')
        tm.sleep(1)
        print('O JOGADOR GANHOOOOU!')
    if player == 2:
        print('Computador jogou PEDRA!')
        print('Jogador jogou TESOURA!')
        tm.sleep(1)
        print('O COMPUTADOR GANHOOOOU!')
if pc == 1:
    if player == 0:
        print('Computador jogou PAPEL!')
        print('Jogador jogou PEDRA!')
        tm.sleep(1)
        print('O COMPUTADOR GANHOOOOU!')
    if player == 1:
        print('Computador jogou PAPEL!')
        print('Jogador jogou PAPEL!')
        tm.sleep(1)
        print('O JOGO DEU EMPAAATE!')
    if player == 2:
        print('Computador jogou PAPEL!')
        print('Jogador jogou TESOURA!')
        tm.sleep(1)
        print('O JOGADOR GANHOOOOU!')
if pc == 2:
    if player == 0:
        print('Computador jogou TESOURA!')
        print('Jogador jogou PEDRA!')
        tm.sleep(1)
        print('O JOGADOR GANHOOOOU!')
    if player == 1:
        print('Computador jogou TESOURA!')
        print('Jogador jogou PAPEL!')
        tm.sleep(1)
        print('O COMPUTADOR GANHOOOOU!')
    if player == 2:
        print('Computador jogou TESOURA!')
        print('Jogador jogou TESOURA!')
        tm.sleep(1)
        print('O JOGO DEU EMPAAATE!')