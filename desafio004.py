coisa = input('Digite algo:')
if coisa.isalnum():
    print('vc digitou numeros e/ou letras')
    if coisa.isalpha():
        print('vc digitou apenas letras')
        if coisa.islower():
            print('vc digitou letras minusculas')
        if coisa.isupper():
            print('vc digitou letras maiusculas')
        if coisa.istitle():
            print('vc digitou algo com letra maiuscula')
if coisa.isspace():
    print('vc digitou um espaço')
if coisa.isdecimal():
    print('vc digitou apenas numeros')
