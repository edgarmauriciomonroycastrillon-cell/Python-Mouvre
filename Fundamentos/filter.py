# Filter , funcion utilizada los argumentos dentro de un iterable
# True si cumplen condiciones , False si no

numeros = [1,2,3,4,5,6,7,8,9,10]

# Funcion explicita

def retornar_par (numero):
    return numero % 2 == 0


filtar_pares = list(filter(retornar_par,numeros))   # filtrer va la funcion y el iterable, en la fucion es mas corta
print(filtar_pares)


# Funcion de orden superior con lambda

filtras_pares_orden_s = list(filter(lambda x : x % 2 == 0, numeros))
print(filtras_pares_orden_s)



# Filtrar los nombres que empiezen con la letra a
name = ['Alice','Bob','Anna','David','Amelia','Charlie']


def retornar_nombres_a (nombre):
    return nombre[0] == 'A'

lista_nombre_a = list(filter(retornar_nombres_a,name))
print(lista_nombre_a)


# Funcion de orden superior
lista_nombre_a = list(filter(lambda x: x[0] == 'A',name))
print(lista_nombre_a)

