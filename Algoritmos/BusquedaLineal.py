# Busqueda Lineal

def busqueda_lineal(lista,objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i 
    return -1

lista = [1,2,3,4,56,6,8,9,55,51,8541,51,541,51,521,51,51,5,15,152,15,41,1,7,8,9,45,54,1,52,15,841,41]


print(busqueda_lineal(lista, 7))
print(busqueda_lineal(lista, 8541))
print(busqueda_lineal(lista, 999))
print(busqueda_lineal(lista, -1))