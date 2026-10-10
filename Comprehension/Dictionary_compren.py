
lista = [1,2,3,4,5]

cuadrado_dict = {}

# Guardar lista con numeros cuadrados
for x in lista:
    cuadrado_dict[x] = x**2
print(cuadrado_dict)

cuadrado_dict_compr = {y ** 2 for y in lista}  # Lo musmo que arriba pero en un sola linea de codigo
print(cuadrado_dict_compr)

# Filtros igual que los de la lista

