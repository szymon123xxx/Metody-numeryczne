import math
lista1 = []
lista2 = []
for i in range(1, 13):
    y = math.sqrt((2**(-(i+i)))**2+1)-1
    z = (2**(-(i+i)))**2/(math.sqrt((2**(-(i+i)))**2+1)+1)
    lista1.append(y)
    lista2.append(z)
print(lista1)
print(lista2)
