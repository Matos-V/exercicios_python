numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete')
n = 0

while n != 70:
    n = int(input('digite um numero entre 0 e 7: '))
    if (n < 0) | (n > 7):
        print('numero não se encontra na tupla!')
    else:
        print(f'você digitou o numero {numeros[n]}')
