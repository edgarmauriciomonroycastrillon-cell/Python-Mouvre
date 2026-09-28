# TUPLAS ()
## Mas estritas que las listas , no se puede modificar son inmutables  
my_tuple = tuple()

my_informacion = (21, 1.73, "Mauro", "Monroy")


# Mostar todos los elementos dentro de la tupla
print(my_informacion[1])
# Mostar un elemento dentro de la tupla , del index
print(my_informacion[1])


# Aca el index me dice donde esta el elemento la posicion ( no me permite agregar cosas a la lista)
print(my_informacion.index("Mauro"))


# Pasar de tupla a lista 
my_informacion = list(my_informacion)
print(type(my_informacion))

#Pasar a tupla de nuevo
my_informacion = tuple(my_informacion)
print(type(my_informacion))

# del , palabra reservada para eliminar una variable
del my_informacion 

# print(my_imformacion) , elimino la tupla ya no existe al llamarla , me arroja error