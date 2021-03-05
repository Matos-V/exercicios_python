ano = int(input("digite um ano: "))
if ano%4:
    print("O ano não é bissexto!")
else:
    if (ano%100 == 0) & (ano%400 != 0):
        print("O ano não é bissexto!")
    else:
        print("O ano é bissexto!")

