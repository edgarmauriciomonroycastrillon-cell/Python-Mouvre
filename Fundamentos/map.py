# Funciones de orden superior son funciones que aceptan otras funciones como argumentos 
# Pueden retornar una funcion o una lista


# map , la aplica a cada uno de los elementos de un iterable, como un for

lista_nombre = ['maria','carlos','pepe']

lista_nombres_mayus = list(map(str.upper, lista_nombre))   # str de orden superior, upper convertir cada uno a mayus, ,despues el iterable
# Casteo es converitr datos de un tipo a otro , map muestra cosas raras por eso list para convertir en lista y mostrar


print(lista_nombres_mayus)

#Ejercicio 2 , sin MAP
lista_frutas = ['banano', 'pera', 'manzana', 'uva']
subfix = '_fruta'

def agregar_sufix(iterable, subfijo):
    resultado = []
    for i in iterable:
        resultado.append(i + subfijo)
    return resultado




lista_frutas_subfix = agregar_sufix(lista_frutas, subfix)
print(lista_frutas_subfix)


# Con map
lista_frutas = ['banano', 'pera', 'manzana', 'uva']
subfix = '_fruta'

def agregar_subfijo (iterable):
    return iterable + subfix


lista_frutas_subfix_map = list(map(agregar_subfijo,lista_frutas))
print(lista_frutas_subfix_map)



# Funcion de orden superior
lista_frutas_subfix_map = list(map(lambda iterable : iterable + subfix,lista_frutas))  # Pamos lambda dentro de map