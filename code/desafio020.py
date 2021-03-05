import random

nome1 = input('nome do primeiro aluno: ')
nome2 = input('nome do segundo aluno: ')
nome3 = input('nome do terceiro aluno: ')
nome4 = input('nome do quarto aluno: ')
lista = [nome1,nome2,nome3,nome4]
random.shuffle(lista)
#print('O aluno sorteado para apagar o quadro foi {}'.format(n))
print(lista)
