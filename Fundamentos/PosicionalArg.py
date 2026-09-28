def imprimir_nombre (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    print(f"Hola {primer_nombre} {segundo_nombre} "\
          f"{primer_apellido} {segundo_apellido} "\
            "Bienvenido")

# Posicional arguments                      mismo orden de como se definieron los argumentos
imprimir_nombre("Edgar", "Mauricio" , "Monroy", "Castrillon")   # El mismo orden de como se definieron los argumentos en la funcion

# Keywords arguments                        decimos la clave de los argumentos
imprimir_nombre(segundo_apellido="Castrillon", primer_nombre="Edgar", segundo_nombre="Mauricio", primer_apellido="Monroy")


# Se pueden mezclar
imprimir_nombre("Edgar", "Mauricio", primer_apellido="Monroy", segundo_apellido="Castrillon")







# Iterable unpacking - Desempacamiento de iterables
estudiante = ("Edgar", "Mauricio", "Monroy", "Castrillon")     # Es una dupla

imprimir_nombre(*estudiante)    # Importante pasarle el * 



# Dictionary unpacking - Desempacamiento de dicionario
estudiante_dict = {"primer_apellido" : "Monroy", "primer_nombre" : "Edgar", "segundo_nombre" : "Mauricio" 
                   , "segundo_apellido" : "Castrillon"}

imprimir_nombre(**estudiante_dict)     # con dos ** le definimos que lo desempaque
