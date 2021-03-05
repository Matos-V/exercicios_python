d = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos km foram rodados? '))
total = 60*d + 0.15*km
print("O total a pagar é R${:.2f}".format(total))
