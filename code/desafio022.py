nome = str(input("digite seu nome: ")).strip()
print('Seu nome com letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é {}'.format(nome[:nome.find(' ')]))

nome_separado = nome.split()

print('Seu primeiro nome tem {} letras'.format(len(nome_separado[0])))
print('Seu primeiro nome é {}'.format(nome_separado[0]))
