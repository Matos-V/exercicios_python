s = float(input("Qual o valor do seu salário? "))
if s <=1250:
    s = s + s*0.1
    print("Vc ganhou aumento de 10% e agora ganha {:.2f} reais".format(s))
else:
    s = s + s * 0.15
    print("Vc ganhou aumento de 15% e agora ganha {:.2f} reais".format(s))