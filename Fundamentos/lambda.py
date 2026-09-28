# Funciones lambda son sencillas , rapidas y temporales para operaciones pequeñas

def retornar_nota (estudiante):
    return estudiante[1]


lambda estudiante: estudiante[1]   #Funcion lambda , lambda nombre reservado

lambda x: x[1]    # primer x son los argumentos y el segundo es el retorno

lista_estudiantes = [('Mauro', 4.2),
                     ('Pepe', 4.1),
                     ('Sofia', 4.0),
                     ('Gabriel', 4.8)]

lista_ordenada = sorted(lista_estudiantes, key=lambda x:x[1], reverse=True)
print(lista_ordenada)


# Ejemplo , funcion lambbda puede ser asiganda a una variable 
lista = [1,2,3]

retorno = lambda y:y[1]

print(retorno(lista))  # le indico el argumento , al llamarla

# Ejercicio 3 con 2 parametros de entrada
sumar = lambda numero1,numero2 : numero1 + numero2    # Retorno implicito
print(sumar(5,5))

restar = lambda x,y : x-y
print(restar(8,4))

multiplicar = lambda x,y : x*y
print(multiplicar(2,10))

dividir = lambda x,y : x/y
print(dividir(4,2))