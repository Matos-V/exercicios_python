def soma(a,b):
    """
    função que recebe dois parametros e mostra em tela
    a soma delas
    """
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'a soma deu {s}')

def contador(*num):
    print(num)

help(soma)