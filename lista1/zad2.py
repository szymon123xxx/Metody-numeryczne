from matplotlib import pyplot
import numpy
N = 101
x = numpy.arange(0, N, 1)
y = 0.1
lista = []
lista2= []
for i in range(N):
    lista.append("x"+str(i)+"="+str(y))
    print(lista[i])
    lista2.append(y)
    y = 3.5*y*(1-y)
pyplot.scatter(x, lista2)
pyplot.show()