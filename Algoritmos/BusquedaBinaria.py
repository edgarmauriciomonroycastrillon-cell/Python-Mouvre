def busquedaBinaria (lista, objetivo=-1):
    inicio = 0
    fin = len(lista) - 1
    lista_ordenada = sorted(lista)
    contador = 0
    
    while inicio <= fin:
        contador += 1
        medio = (inicio + fin ) // 2

        if lista_ordenada[medio] == objetivo:
            print(f"numero de intentos: {contador}")
            return medio
        elif lista_ordenada[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio -1  
    print(f"numero {objetivo} NO encontrado")            
    return -1

lista_prueba = [1,2,5,9,7,5,6,3,4,3,2]
print(busquedaBinaria(lista_prueba, 2))
print(busquedaBinaria(lista_prueba, 865))
print(busquedaBinaria(lista_prueba, ))