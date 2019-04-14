import math
a = float(input('digite o valor do primeiro cateto do triangulo retangulo '))
b = float(input('digite o valor do segundo '))
c = math.hypot(a,b)
print('o comprimento da hipotenusa é {}'.format(c))
