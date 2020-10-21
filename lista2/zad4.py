import math
lista1 = []
lista2 = []
for i in range(25):
    y = (i**2)**2 / (math.sqrt((i**2)**2+4)+2) # Bardziej dokładne
    x = math.sqrt(i**4 + 4) - 2 # Mniej dokładne
    lista1.append(y)
    lista2.append(x)
print(lista1)
print(lista2)