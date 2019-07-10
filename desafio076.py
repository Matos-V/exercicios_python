produtos = ('shampoo','R$7,00','água','R$1,00','whey protein','R$90,00')
print('{:.<30}{}'.format('produto:','preço:'))
for n in range(0,len(produtos)-1,2):
    print('{:.<30}{}'.format(produtos[n],produtos[n+1]))