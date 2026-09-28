# GLOBAL
nombre = "Mauricio"     # Variable Global

def imprimir_nombre ():
    global nombre   #le decimos que trabaje con la variable Global la cambia la global a local
    nombre = "Santiago"   #Variables local
    print(f"Hola {nombre} como estas ")

imprimir_nombre()  # imprime la variable local
print(f"Hola {nombre}")  #imprime la variable Global
print("-----------------------------------\n")



# LOCAL

apellido = "Monroy"
def imprimir_apellido ():
    apellido = "Castrillon"   # Aca solo vive la variable dentro de la funcion
    print(f"Hola {apellido} como estas")

imprimir_apellido()
print(f"Hola {apellido}") 
print("-----------------------------------\n")


# ENCLOUSING
def nombre():
    nombre_local = "Mauricioo"
    edad_local = 21
    print(f"Hola {nombre_local} como estas?")
    def imprimir_edad():     # Funcion dentro de otra funcion
        nonlocal edad_local   # imprime la edad local , la de mas arriba
        edad_local = 40
        print(f"Tienes {edad_local} años")
    imprimir_edad() # colocamos la funcion dentro de la funcion mas grande, accede alaa variable dentro de la otra

nombre()
