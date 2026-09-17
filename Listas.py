## listas 
frutas = ["Manzana", "Fresa" , "Naranja", 21]

# Mostar la lista
print(frutas)
# Contar elementos dentro de la lista 
print(len(frutas))
#Tipo de datos en la lista 
print(type(frutas[3]))


dates = ["Mauro", "Monroy", 21, 22]
name, edad, altura = "Mauro", 21, 171.3
info = [name, edad, altura ]
print(info[-1])
print(dates)

## POP Quitar elementos de la lista con su indice , pop() elimina el ultimo elemento
solo_edad = dates.pop(2)
print(solo_edad)

#Remove  Quitar elementos de la lista con su valor
dates.remove("Monroy")


#Saber la posicion del onjeto en la lista
print("La Posicion del nombre mauricio es: " + str(dates.index("Mauro")))

#Contar cuantas veces los elementos en la lista , contar elementos de la propia lista
print(dates.count("Mauro"))

#Añadir elementos 

# Un solo elemento al final con append (derecha) de la lista
dates.append("Castrillon")
print("Lista actualizada con append se ve asi:\n" + str(dates))

#Añade un elemento en una posicion especifica
dates.insert(1, "Single")
print("La lista actualizada con insert se ve asi: " + str(dates))

# Varios Elementos con Extend, importantes corches [], añade al final (derecha) de la lista
dates.extend(["Cabello negro" , "Vive en bogota"])
print("Lista actualizada con insert se ve asi: \n " + str(dates))




# Ordenar de mayor a menor 
print(dates.sort)

dates.clear()
print(dates)