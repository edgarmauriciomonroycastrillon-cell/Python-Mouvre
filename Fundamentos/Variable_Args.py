# *Args no sabemos la cantidad de variables que puede utilizar la funcion
# Variable position arguments

def suma (*args):       # *args con varios parametros, importante el asterisco * y args , (internamente es una tupla)
    return sum(args)


resultado = suma(2,5,7)   # Colocamos la cantidad de parametros que se quiere
print(f"El resultado es: {resultado}")