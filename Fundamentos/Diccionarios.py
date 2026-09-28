# Diccionarios

# Guarda un valor con una clave o un valor

#Claves y los valores pueden ser tipo de dato (lista, tuplas,set,enteros , flotantes , strings)

my_dict = {"nombre": "Mauricio",
        "Apellido": "Monroy",
        "Edad": 21,
        "Altura": 1.73,
        5: "Clave 5",
        "Lenguajes": ["Python", "C++", "C"]} # Puedo giardar diferentes tipos de datos dentro de mi dicionario

# Elementos dentro de mi dicionario 
print(len(my_dict))



# Mpstar todo el diccionario 
print(my_dict)
# Buscar algo en especifo con la clave, debe ser igual hasta el tipo de dato 
print(my_dict["nombre"])


# Actalizar valor 
my_dict["nombre"] = "Juan"
print(my_dict["nombre"])


#Añadir un nuevo clave valor al dicionario
my_dict["Nick_name"] = "Mao"
print(my_dict)

#Eliminar UN solo elemento del diccionario, accediendo desde la clave
del my_dict["Altura"]
print(my_dict)


# Buscar si algo esta dentro de mi tipo de dato , pero con dicionarios solo buscamos por clave
print("nombre" in my_dict)



# Items retorna el diccionario
print(my_dict.items())
# Keys , nos muestra las claves del diccionario
print(my_dict.keys())
# Values , nos muestra los valores del diccionario
print(my_dict.values())



# fromkeys cuando creo un diccionario sin valores solo con las claves 
my_new_dict = my_dict.fromkeys("Nombre", "Apodo")
print(my_new_dict)