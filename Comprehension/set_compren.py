
lista = [1,2,3,4,5]

cuadrado_set = set()

# Guardar lista con numeros cuadrados
for x in lista:
    cuadrado_set.add(x**2)
print(cuadrado_set)

cuadrado_set_compr = [y ** 2 for y in lista]  # Lo musmo que arriba pero en un sola linea de codigo
print(cuadrado_set_compr)

# Filtros igual que los de la lista
