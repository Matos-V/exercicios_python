aluno = dict()
nome = input('Digite o nome do aluno: ')
media = float(input('digite a média do aluno: '))
aluno['nome'] = nome
aluno['media'] = media
if media<7:
    aluno['situação'] = 'reprovado'
else:
    aluno['situação'] = 'aprovado'
for k,v in aluno.items():
    print(f'{k}: {v}')
