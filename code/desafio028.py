import random

num = random.randint(0,5)
num2 = int(input("digite um numero de 0 a 5: "))
if num == num2:
    print("Parabens, vc adivinhou o numero aleatório")
else:
    print("vc n acertou o numero aleatório")
print(num)
