n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
n3 = int(input("digite um numero: "))
n = [n1,n2,n3]
print(n)
n = sorted(n)
print(n)
print("{} é o menor numero e {} é o maior".format(n[0],n[2]))