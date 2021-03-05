import random as rd

numeros = (rd.randint(0,10),rd.randint(0,10),rd.randint(0,10),rd.randint(0,10),rd.randint(0,10))
print(numeros)
print('o menor numero sorteado foi {} e o maior foi {}'.format(sorted(numeros)[0],sorted(numeros)[len(numeros)-1]))