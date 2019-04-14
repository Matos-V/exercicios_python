num = int(input('digite um numero: '))
uni = num%10
dez = (num%100 - uni)/10
cen = (num%1000 - dez*10 - uni)/100
mil = num/1000

print('Unidade: {}'.format(uni))
print('dezena: {:.0f}'.format(dez))
print('centena: {:.0f}'.format(cen))
print('milhar: {:.0f}'.format(mil))

uni = num%10
dez = num // 10 %10
cen = num//100%10
mil = num//1000

print('Unidade: {}'.format(uni))
print('dezena: {:.0f}'.format(dez))
print('centena: {:.0f}'.format(cen))
print('milhar: {:.0f}'.format(mil))