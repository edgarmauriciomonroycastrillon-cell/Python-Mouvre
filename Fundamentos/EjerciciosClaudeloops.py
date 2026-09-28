import turtle # Para moverse
import random # Numero aleatorios



'''Ejercicio 1 – Contar
Con for y range(), imprime:

los números del 1 al 10
los pares del 2 al 20
una cuenta regresiva del 10 al 1 '''

#for i in range (1,11):
#    print(i)

#for j in range (2,22,2):
#    print(j)    

#for k in range (10,0,-1):
#    print(k)

''' Ejercicio 2 – Tabla de multiplicar
Pide un número e imprime su tabla del 1 al 10 con este formato: 7 x 3 = 21.'''

#numero = int(input("Ingrese un numero "))
#for x in range (1,11):
#    y = numero * x
#    print(f" {numero} x {x} = {y}")

'''Ejercicio 3 – Recorrer una lista (for each)
Con tu lista de frutas, imprime cada fruta en MAYÚSCULAS. Luego, con enumerate, imprímelas numeradas empezando en 1:

1. mango
2. fresa'''

#frutas = ["mango", "fresa", "manzana", "naranja"]

#for z, fruta in enumerate(frutas , 1):   #no entendi por que la coma, y fruta sera una nueva variable que es la que recorre y z otra el index
#    print(f"{z} {fruta.upper()}")  

# Ejercicio 4 – Suma y promedio
'''Tienes notas = [4.5, 3.2, 2.8, 5.0, 3.9]. 
Con un for, calcula la suma y el promedio sin usar sum(). Luego cuenta cuántas notas son aprobatorias (>= 3.0).'''

#notas = [4.5, 3.2, 2.8, 5.0, 3.9]
#sumanotas = 0
#notasaprobatorias = 0
#for a in notas:
#    sumanotas += a
#    if a >= 3.0:
#        notasaprobatorias += 1
    
#print(f"La suma de la notas es : {sumanotas}  y el promedio de las notas es: {sumanotas / len(notas)} ")  
#print(f"La cantidad de notas mayores a 3.0 es : {notasaprobatorias}")

'''Ejercicio 5 – Contar vocales
Pide una palabra o frase y cuenta cuántas vocales tiene.
Pista: un for también recorre un string, letra por letra. Y if letra in "aeiou":'''
#frase = input("Ingresa una frase ")
#contador_vocal = 0

#for letra in frase:
#    if letra.lower() in "aeiouáéíóú":
#        contador_vocal += 1
#print(f"Hay {contador_vocal} en la frase")

        
'''Ejercicio 6 – While: adivina el número
Guarda un número secreto (por ejemplo 7). 
Pide al usuario que adivine hasta que acierte. Dile "más alto" o "más bajo" en cada intento y,
 al final, en cuántos intentos lo logró.'''

#numero_secreto = 72

#intentos = 0
#guess_number = int(input("Ingrese un numero "))

#while guess_number != numero_secreto:
#    print("Vuelvelo a intentar")
#    intentos += 1
#    if guess_number < numero_secreto:
#        print("El numero es mas Alto")
#    elif guess_number > numero_secreto:
#        print("El numero es mas Bajo")

#    guess_number = int(input("Ingrese otro numero "))

#print(f"Lo intentaste {intentos} veces")


'''Ejercicio 7 – Reto: menú con while
Mejora tu calculadora: que se repita en un while hasta que el usuario escriba "salir" en la operación. Usa break.'''
    
#while True:    
#    numero1 = float(input("Ingresa el 1 numero "))
#    numero2 = float(input("Ingresa el 2 numero "))


#    operacion = input("Ingresa la operacion: \n 1 = Suma (+) \n 2 = Resta (-) \n 3 = Multiplicacion (*) \n 4 = Division (/) \n Si quiere salir escriba Salir \n")

#    if operacion == "1":
#        print(f"Tu suma es: {numero1 + numero2}")
#    elif operacion == "2":
#        print(f"Tu resta es: {numero1 - numero2}")
#    elif operacion == "3":
#        print(f"Tu multiplicacion es: {numero1 * numero2}")
#    elif operacion == "4":
#        if numero2 == 0:
#            print("No se puede dividir entre cero (0)")
#        else:
#            print(f"Tu division es: {numero1 / numero2}")
#    elif operacion.lower() == "salir":
#        break
#    else:
#        print("Operacion NO valida")





#Ejercicio de hacer un cuadrado
#ventana = turtle.Screen()  #Interfaz grafica
#ventana.bgcolor("white")   #Cambiamos el color
#tortuga = turtle.Turtle()   # Lo que se va a mover
#tortuga.speed(1)    #Cambiamos la velocidad de como se cambia


#for i in range(4):
#    tortuga.forward(100)  #Muevase 100 espacios
#    tortuga.right(90)     # Muevase 90 grados
#ventana.exitonclick()      #Salir con click



#Ejercicio dibujar una estrella
#ventana = turtle.Screen()  #Interfaz grafica
#ventana.bgcolor("white")   #Cambiamos el color
#tortuga = turtle.Turtle()   # Lo que se va a mover
#tortuga.speed(1)    #Cambiamos la velocidad de como se cambia

#for i in range(5):
#    tortuga.forward(150)
#    tortuga.right(144)
#    tortuga.forward(150)
#    tortuga.left(72)
#ventana.exitonclick()


# Break
#meta = 20
#caracol1 = 0
#caracol2 = 0

#while True:
#    avance_caracol_1 = random.randint(1,4)
#    avance_caracol_2 = random.randint(1,4)

#    caracol1 += avance_caracol_1
#    caracol2 += avance_caracol_2

#    print(f"El caracol 1 avanzo: {avance_caracol_1} , con total de avance {caracol1} ")
#    print(f"El caracol 2 avanzo: {avance_caracol_2} , con total de avance {caracol2} ")
#    print("--------------------------------------------------------------------------")
#    if caracol1 >= 20 or caracol2 >= 20:
#        break

#if caracol1 > caracol2:
#    print(f"Felicidades  Caracol 1 GANASTE")
#elif caracol2 > caracol1:
#    print("Felicidades Caracol 2 GANASTE")
#else:
#    print("Empate")





#Continue
#lista_numero = [34,10,23,57,19,2,8,3]

#for i in lista_numero:
#    if i % 2 != 0:
#        continue
#    print(f" {i} es numero Par")