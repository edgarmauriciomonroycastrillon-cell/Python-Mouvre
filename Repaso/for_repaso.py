import random 


# Imprimir la tabla del 1 al 5



for i in range(1,6):   # hago un for , i recorre el rango de 1 a 5 
    for x in range(1,11):    # hago un for anidado , donde x recorre el rango de 1 a 10
        multiplicacion = i * x    # multiplico , i * x , cuando i vale 1 x tambien , SIEMPRE SE RECORRE EL FOR DE ADENTRO PRIMERO
                                  # Osea que mientras i vale 1 x pasa a valer 2 , hasta que se termine el x (for anidado) , empieza la segunda
                                 # vuelta de  i ( del for de afuera)

        print(f"{i} * {x} = {multiplicacion}")   # un f string mostrando la posicion de i y la de x y loa multipicacion (resultado) en cada recorrido





# Posiciones Pares
frase = "La practica hace al maestro"    # tenemos las frase normal , con espacios 
sin_espacios = frase.replace(" ","").lower()  # la frase la colocamos en una nueva variable ,remplazamos los espacios por nada (quitamos los espacios)
                                              # con replace , y ademas colocamos toda la frase en minuscula    
for y,letra in enumerate (sin_espacios):      # hacemos un for con enumerate (para contar la posicion) recorremos la variable (sin_espacios) con dos variables 
                                              # y para contar la posicion que nos devuelve enumerate y letra para saber la letra de frase , que me devuela la letra de sin_espacios

    if y % 2 == 0:               # Aca evaluamos , si la posicion es par
        print(y,letra)           # Imprimimos la posicion (y) y la letra de esa posicion (letra)



# 3 . Inventario
inventario = {"manzana": 12,   # tenemos un  dict , con clave(fruta) y valores(stock) , 
              "pera": 0,
              "uva": 30,
              "banano": 5}

for fruta, cantidad in inventario.items():  # hacemos un for para recorrer el dict , items me retorna la clave (fruta) y el valor(stock)
    if cantidad == 0:                       # Evaluo si el stock (cantidad) es 0
        print(f"Fruta Agotada {fruta}")     #Imprimo la fruta agotada
print(fruta, cantidad)                      # imprimo el inventario que quedo de cada fruta


# Piramide 4.
num1 = int(input("Ingresa un numero entero "))
for a in range(1,num1+1):
    print(a*"*")


# Pares que suman
numeros = [2,7,4,5,3,6]    # Lista 

for i, h in enumerate (numeros):   # un for i para contar la posicion y h recorrere la lista
    for d in numeros[i+1:]:         # for anidados donde d es una posicion a la derecha de h , para que no se repitan
        if h + d == 9:             # condicion que comprueba si h e i suma 9 , imprimalos
            print(h,d)



# Cuenta regresiva
num2 = int(input("Ingresa un numero entero "))

while num2 > 0:      # mientras num2 sea mayor a 0
    num2 -= 1        # a num 2 le resto 1 en cada vuelta
    if num2 == 0:    # si num2 en la vuelta es igual a 0 , imprimo despegue
        print("Despegue!")

# Suma hasta cero

num2 = int(input("Ingresa un numero, ingresa 0 para salir "))
suma = 0     # Inicializo las variables en 0
cantidad = 0
mayor = num2
while num2 !=0:    # Compruebo si el num2 es mayor a 0, ejecutese:

    suma += num2   # a suma sumele el numero 2 , en cada vuelta y se almzacene en cada vuelta
    cantidad += 1   # cuento cuantas vueltas hay dentro del ciclo
    if num2 > mayor:  # pruebo si el num es mayor al acomulador , guarde el nuevo numero
        mayor = num2

    num2 = int(input("Ingresa un numero, ingresa 0 para salir "))  # pregunto numero para que no quede un bucle infinito

if cantidad > 0:   # compruebo si la cantidad(numero de vuelta) es 0,porque si no promedio me da error , no se puede dividir en 0
            
    print(f"La suma es {suma} ") # muestro
    print(f"El promedio es {suma/cantidad:.2f} ")   # :.2f , para que me muestre el numero con dos decimales
    print(f"EL numero mayor es: {mayor}")  

else:
    print("Operacion invalida")    # si las vueltas son 0 retorneme operacion invalida


# Adivina el numero
num3 = int(input("Ingresa un numero y adivina "))
num4 = random.randint(0,100)
intento = 0
while num3 != num4:
    intento += 1
    if num3 > num4:
        print(f"el numero a adivinar es mas bajo a {num3}")
    else:
        print(f"el numero a adivinar es mas alto a {num3}")

    num3 = int(input("Ingresa un numero y adivina "))

print(f"Felicidades adivinaste el numero correcto, lo lograste en {intento} intentos")

# Contraseña
intentos = 0
valid = False

while intentos != 3 and not valid:

    contraseña = input("Ingresa un contraseña con min 8 caracteres y al menos un numero ")
    intentos += 1


    tiene_numero = False
    for caracter in contraseña:
        if caracter.isdigit():
           tiene_numero = True

    if len(contraseña) >= 8 and tiene_numero:
        valid = True
        print("Contraseña valida")
        break
    else:
        print(f"Contraseña incorrecta, te quedan {3-intentos}")

    

if not valid:            
    print("Agotaste los intentos cuenta bloqueada")


# Menu 
Tareas = []
num5 = int(input("1. Agregar Tarea\n2. Ver Tareas\n3. Borrar Tarea\n4. Salir\n: "))     


while num5 != 4:


    if num5 == 1:
        NewTask = input("Ingresa la tarea a agregar ")
        Tareas.append(NewTask)
    elif num5 == 2:
        print(f"Lista de tareas: {Tareas}")
    elif num5 == 3:
        print(Tareas)
        DeleteTask = input("Ingresa la tarea a eliminar ") 
        Tareas.remove(DeleteTask)
    else:
        print("Ingrese una operacion valida ")  

    num5 = int(input("1. Agregar Tarea\n2. Ver Tareas\n3. Borrar Tarea\n4. Salir\n: "))     

# Funciones

#Contar letras
# Este no lo entendui bien mas que todo en el for vocal in "aeiou"
def contar_vocales (frase2):
    frase2 = frase2.replace(" ","").lower()     # Le quitamos los espacios y la colocamos a minuscula
    resultado = {}                              # Creo un dict vacio , donde voy a colocar el resultado

    for vocal in "aeiou":                       # un for para recorrer, voca en vocales
        resultado[vocal] = frase2.count(vocal)  # frase tiene alguna de las vocales las guardo en resultado cada una como vocal

    return resultado


frase = input("Ingresa una frase ")
print(contar_vocales(frase))

# Es palidromo
def es_palindromo (palabra):
    palabraminuscula = palabra.lower()   # palabra en minusculas 
    palabrareverso = palabraminuscula[::-1]   # reversamos la palabra , al volteamos
    return palabraminuscula == palabrareverso # si la palabra al derecho es igual al revez es true si no es false


palabra1 = input("Ingresa una palabra ")
print(es_palindromo(palabra1))


def estadisticas(*args):

    minimo = min(args)
    maximo = max(args)
    promedio = sum(args) / len(args)

    return minimo, maximo, promedio

print(estadisticas(4,8,15))

#Crear perfil
def crear_perfil(nombre, edad, **datos):
    perfil = {"nombre": nombre, "edad": edad}
    perfil.update(datos)    
    return perfil

perfil = crear_perfil("Mauro", 21, ciudad="Bogotà", carrera="industrial")  
print(perfil)


# Aplicar descuento, no lo entendi me ayude mucho con IA
def aplicar_descuento(precio, porcentaje=10):     # definimos la funcion , con paramteros precio y porcentaje por defecto 10
    cuenta = {}   # creamos uin dict vacio donde se va almacenar el "inventario"
    for producto, valor in precio.items():     # un for recorre va recorrer los parametros de la func, y me devueleve clav y val con .items
        cuenta[producto] = valor * (1-porcentaje / 100)    # en el dict de producto , calculams el precion con descuento
    return cuenta 


compra_original = {"Cafe": 15000, "Arroz": 52000, "Azucar": 2500}
compra_con_descuento = aplicar_descuento(compra_original)
print(f"Compra Original {compra_original} \nCompra con descuento del 10% {compra_con_descuento}\nCompra con descuento del 20% {aplicar_descuento(compra_original, 20)}")


# Comprensiones

#LIsta con nombres en mayuscula, no hay funcion , toca recorrer la lista con for


def mayusculas(listas):
    lista_mayuscula = []
    for b in listas:
        lista_mayuscula.append(b.upper())
    return lista_mayuscula




if __name__ == "__main__":
    lista = ['ana', 'luis', 'maria']
    print(mayusculas(lista))   



# solo mostrar multiplicos de 3
for f in range(1,31):
    if f % 3 == 0 and f % 2 != 0:
        print(f)
# compresion
multiplos_de_tres = [f for f in range(1,31) if f % 3 == 0 and f % 2 != 0]
print(multiplos_de_tres)

# datos a minusculas si son mas de 2 letras
info = ['sol','Python','mar','Datos','IA','sol','python'] 

info_minusculas = {i.lower() for i in info if len(i) > 2}
print(info_minusculas)

# Dict de notas
notas = {'Ana': 4.5, 'Luis': 2.8, 'Sara': 3.9, 'Juan': 2.1}

estados_notas = {nombre: "Aprobo" if nota >= 3.0 else 'Reprobo' for nombre, nota in notas.items()}
print(estados_notas)

# Anidada - hecho con ia , esta ni idea ,no he practicado mucho recorrer matrices
matriz = [[1,2,3], [4,5,6], [7,8,9]]

aplanada = [n for fila in matriz for n in fila]
transpuesta = [[fila[i] for fila in matriz] for i in range(3)]

print(aplanada, transpuesta)
