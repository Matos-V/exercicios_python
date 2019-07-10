valores = []
menor = maior = 0

for n in range(0,5):
    valores.append(int(input('digite um numero: ')))
    if n == 1:
        menor = valores[n]
        maior = valores[n]
    if menor > valores[n]:
        menor = valores[n]
    if maior < valores[n]:
        maior = valores[n]
print(valores)
print('o menor valor digitado foi {} e se encontra na posição {}'.format(menor,valores.index(menor)))
print('o maior valor digitado foi {} e se encontra na posição {}'.format(maior,valores.index(maior)))