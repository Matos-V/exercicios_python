print("tabela de preços:\ndistancia menor ou igual a 200km - R$0.50 por km\ndistancia maior que 200km - R$0.45 por km")
km = float(input("qual a distancia da sua viagem? "))
if km<=200:
    p = km*0.5
    print("Sua viagem custa {:.2f} reais".format(p))
else:
    p = km*0.45
    print("sua viagem custa {:.2f}".format(p))