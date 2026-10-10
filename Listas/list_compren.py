
lista = [1,2,3,4,5]

cuadrado = []

# Guardar lista con numeros cuadrados
for x in lista:
    cuadrado.append(x ** 2)
print(cuadrado)

# List Comprenhension

cuadrado_list = [y ** 2 for y in lista]  # Lo musmo que arriba pero en un sola linea de codigo
print(cuadrado_list)




cuadrado_list_par = [y ** 2 for y in lista if y % 2 == 0]  # Le podemos agregar filtros 
print(cuadrado_list_par)




# List comprenhension anidados

# Sin list
matriz = []
for i in range(3):
    lista_interna = []
    for j in range(1,4):
        lista_interna.append(j)
    matriz.append(lista_interna)
print(matriz)


matriz_list = [[j for j in range(1,4)]for i in range(3)]
print(matriz_list)