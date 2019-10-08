"""
	Ejercicio con funcion lambda: raiz y potencia
	@pablom7
"""
import math
lista = [(10, 2), (8, 7), (5, 4), (3, 11), (10, 11)]
#funcion para obtener la raiz cuadrada
raiz = lambda x: math.sqrt(x[0])
#funcion para obtener el cuadrado
potencia = lambda x: x[1]**2

funcion = lambda x: (raiz(x), potencia(x))
print(list(map(funcion, lista)))
