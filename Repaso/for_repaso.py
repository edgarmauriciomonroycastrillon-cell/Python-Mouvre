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
numeros = [2,7,4,5,3,6]

for h in numeros:
    for d in (h, numeros+1):
        if h + d == 9:
            print(h, d)

           













