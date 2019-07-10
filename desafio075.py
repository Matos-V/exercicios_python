numeros = (int(input('digite um numero: ')),int(input('digite um numero: ')),int(input('digite um numero: ')),int(input('digite um numero: ')))
print('o numero 9 foi digitado {} vezes'.format(numeros.count(9)))
if numeros.count(3) != 0:
    print('o numero 3 aparece primeiramente na posição {}'.format(numeros.index(3)+1))
else:
    print('o numero 3 não foi digitado')
n = 0
for pares in numeros:
    if pares%2 == 0:
        n = n+1
print('foram digitados {} numeros pares'.format(n))