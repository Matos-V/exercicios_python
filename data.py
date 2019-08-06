import datetime as date
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, '')

data = date.datetime(2019, 7, 24,18,30,25)
hoje = date.datetime.now()
mes_atual = int(hoje.strftime('%m'))
numero_de_dias_do_mes_atual = mdays[mes_atual]
print(data.strftime('%d/%m/%Y  %H:%M:%S'))
print(hoje.strftime('%A, %d de %B de %Y'))
print('o mes atual tem {} dias'.format(numero_de_dias_do_mes_atual))