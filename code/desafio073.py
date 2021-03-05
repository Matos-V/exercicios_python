times = ('palmeiras','flamengo','inter','gremio','SP','atletico mineiro','atletico PR','cruzeiro','botafogo','santos','bahia','fluminense','corinthians','chapecoense','Ceara','vasco','sport','america','vitoria','parana')
print('os 5 primeiros times foram:')
for n in times[:5]:
    print(n)
print('\nos ultimos 4 times foram:')
for n in times[-4:]:
    print(n)
print('\nLista em ordem alfabética:')
print(sorted(times))
print('\na chapecoense terminou na posição {}'.format(times.index('chapecoense')+1))