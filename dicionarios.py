galera = list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo [M/F]: '))[0]
        if pessoa['sexo'] in 'mfMf':
            break
        print('digite M ou F!')
    pessoa['idade'] = int(input('idade: '))
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('quer continuar [S/N]: '))[0]
        if resposta in 'nNsS':
            break
        print('digite S ou N!')
    if resposta in 'nN':
        break