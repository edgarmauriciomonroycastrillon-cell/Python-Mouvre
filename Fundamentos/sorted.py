# sorted , ordenar los elementos de un iterable , en base a una llave
#Toma como minimo un iterable y devuelve una nueva lista ordenada

estudiante = [('Juana', 22, 95, '555-1234'),
              ('Pedro', 18, 89, '555-5678'),
              ('Juan', 25, 94, '555-9876')]

def ordenar_por_edad (lista):
    return lista[1] 


lista_estudiantes_edad = sorted(estudiante, key=ordenar_por_edad)  # Primero el iterable , despues la key o la funcion 
print(lista_estudiantes_edad)

# Funcion de nivel superior
lista_estudiantes_edad_ls = sorted(estudiante, key = lambda x: x[1], reverse=True)  # ordenamos al revez
print(lista_estudiantes_edad_ls)


# Ordenado por notas
lista_estudiantes_edad_ls = sorted(estudiante, key = lambda x: x[2], reverse=True)  
print(lista_estudiantes_edad_ls)