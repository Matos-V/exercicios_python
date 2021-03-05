n1 = float(input("digite o valor do primeiro segmento de reta: "))
n2 = float(input("digite o valor do segundo segmento de reta: "))
n3 = float(input("digite o valor do terceiro segmento de reta: "))
n = sorted([n1,n2,n3])

if (n[0]+n[1]) < n[2]:
    print("esses segmentos de reta não formam triangulo pois {} + {} é menor que {}".format(n[0],n[1],n[2]))
else:
    print("esses segmentos de reta formam triangulo pois {} + {} é maior ou igual a {}".format(n[0], n[1], n[2]))
