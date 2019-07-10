valores = []
for n in range(0,5):
    entrada = int(input('digite um valor: '))
    if n==0:
        valores.append(entrada)
    else:
        if entrada > max(valores):
            valores.append(entrada)
        for m in range(0,len(valores)):
            if entrada < valores[m]:
                valores.insert(valores.index(valores[m]),entrada)
                break
print(valores)
