import math
n = float(input('digite o valor do angulo '))
m = n*math.pi/180
print('os valores de seno, cosseno e tangente de {} são {:.3f}, {:.3f} e {:.3f}'.format(n,math.sin(m),math.cos(m),math.tan(m)))
