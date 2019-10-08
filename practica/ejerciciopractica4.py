"""
	Ejercicio con funcion lambda: potencia
	@pablom7
"""

lista = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
#funcion para obtener el cubo
potencia = lambda x: x**3

print(list(map(potencia, lista)))