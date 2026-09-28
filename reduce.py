# aplicar una funcion de manera acomulativa a los elementos de un iterable


from functools import reduce     # toca importar la funcion
numeros = [1,2,3,4,5]

def sumar (numero1, numero2):
    return (numero1 + numero2) * 2


total = reduce(sumar, numeros)  # funcion e iterable, aca suma todos los elementos del iterable y * 2
print(total)


# Orden superior
total_ls = reduce(lambda x,y : (x + y) * 2, numeros)
print(total_ls)