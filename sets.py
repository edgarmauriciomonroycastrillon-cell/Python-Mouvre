# SETS 
# No acepta datos repetidos , y no tienen orden no tienen index
my_set = {"Mauro" , "Monroy" , 1.73, 21}


# Inicialmente aparece que es un diccionario
print(type(my_set))


# len , cuenta los elementos que tiene la lista
print(len(my_set))

my_set.add("Castrillon")
print(my_set)


# Datos repetidos , no los muestra no lo acepta
my_set.add("Castrillon")
print(my_set)

my_set.clear()
print("Hola , aca esta limpio o se limpiaron los datos  " + str(my_set))


'''8. Eliminar duplicados
Crea sin_duplicados(lista) que retorne la lista sin elementos repetidos. 
Hazla de dos formas: con un set y con un for, manteniendo el orden original.'''


