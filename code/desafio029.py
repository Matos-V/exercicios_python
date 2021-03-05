km = float(input("à quantos km/h vc passou pelo radar? "))
if km <=80:
    print("deu sorte, não foi multado!")
else:
    multa = (km - 80)*7
    print("vish... vai ter que pagar {:.2f} reais de multa".format(multa))
