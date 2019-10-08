"""
	Ejemplo 6: uso de funcion lambda
	@pablom7
"""

lista = [10, 2, 3, 5, 1]
# print(min(lista, key=lambda x: x))
# print(min(lista, key=lambda x: x))

funciones = lambda x: x+100

print(min(list(map(funciones, lista))))