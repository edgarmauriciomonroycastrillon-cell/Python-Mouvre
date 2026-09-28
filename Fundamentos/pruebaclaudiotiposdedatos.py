inventario = ["espada", "escudo", "pocion", "mapa"]
coordenadas = (10,25)
enemigos_derrotados = {"globin", "orco", "globin", "dragon"}
jugador = {"nombre": "Mauro", "nivel": 5, "vida": 100.0, "inventario": inventario, "posicion": coordenadas}


# 1 objetos en el inventario
print("Numero de onjetos en el inventario : " + str(len(inventario)))
print("Inventario:  " + str((inventario)))
# 2 Enemigos derrotados 
print("\nCantidad de enemigos derrotados : " + str(len(enemigos_derrotados)))
print("Nombre de enemigos derrotados : " + str((enemigos_derrotados)))
#Agregar antorcha al final del inventario 
inventario.append("Antorcha")    # ¿para añadir elementos declaro la variables de nuevo o solo escribo la variables y la funcion y ya ? aclarame eso porfa
print(f"\nEl inventario actualizado es :  + {inventario}") 
# Quitar posicon con index
inventario.pop(2)
print(f"\nEl inventario actualizado es :  + {inventario}") 
# Cambiar el nivel 6
jugador["nivel"] = 6
print(f"\nEl nivel del jugador ha sido actualizado, su nivel es:  {jugador["nivel"]}")
#Añadir al diccionario "clase": "guerro"
jugador ["clase"] = "guerrero"
print(f"\nLos atributos actualizados son: {jugador}")
# Eliminar la clace vida del diccionario 
del jugador["vida"]
print(f"\nLos atributos actualizados son: {jugador}")
# Solo las claves del diccionario
print(f"Estas son las claves del diccionario: {list(jugador.keys())}")
# Primer objeto del inventario desde el diccionario
print(f"El primer objeto de invenario es: {jugador["inventario"][0]}")
# Agrega troll
enemigos_derrotados.add("troll")
print(f"Lista de enemigos derrotados actualizada {enemigos_derrotados}")
# Mensaje con f string
print(f"{jugador['nombre']} es un {jugador['clase']} de nivel {jugador['nivel']} y tiene {len(inventario)} objetos")