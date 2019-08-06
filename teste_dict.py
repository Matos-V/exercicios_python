Turma = dict()
while True:
    nome = input('Nome do aluno: ')
    Turma[nome] = dict()
    idade = int(input('Idade do aluno: '))
    notas = list()
    notas.clear()
    for n in range(3)
        nota = round(float(input('Nota final: ')),1)
        notas.append(nota)
    Turma[nome]['idade'] = idade
    Turma[nome]['media final'] = sum(notas)/len(notas)
    parada = input('Deseja sair? ')
    if parada == 'sim':
        break
print(Turma)