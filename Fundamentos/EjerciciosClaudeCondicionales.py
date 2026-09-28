''' Ejercicio 1 – Par o impar
Pide un número con input() y di si es par o impar.
Pista: el operador % da el residuo de una división. 7 % 2 da 1. '''

#numero1 = int(input("Ingrese un numero "))
#if numero1 % 2 == 0:
#    print(f"El numero {numero1} es par")
#else:
#    print(f"El numero {numero1} es impar")


''' Ejercicio 2 – Positivo, negativo o cero
Pide un número y di si es positivo, negativo o cero. '''
#numero2 = float(input("Ingrese un numero "))
#if numero2 == 0:
#    print("El numero es cero")
#elif numero2 > 0:
#    print("El numero es positivo")
#else:
#    print("El numero es negativo")


''' Ejercicio 3 – Mayor de dos números
Pide dos números y di cuál es el mayor. Si son iguales, dilo también. '''
#numero3 = float(input("Ingrese numero 1 "))
#numero4 = float(input("Ingrese numero 2 "))

#if numero3 > numero4:
#    print(f"Numero 1 {numero3} es MAYOR a numero 2 {numero4}")
#elif numero4 > numero3:
#   print(f"Numero 2 {numero4} es MAYOR a numero 1 {numero3}")
#else:
#    print(f"El numero {numero3} y el numero {numero4} son IGUALES")

''' Ejercicio 4 – Calificación
Pide una nota del 0 al 5 (puede tener decimales) y muestra:

4.5 a 5 → "Excelente"
4.0 a 4.4 → "Bueno"
3.0 a 3.9 → "Aprobado"
menos de 3.0 → "Reprobado" '''

#nota = float(input("Ingresa la calificacion del 1 al 5: "))
#if nota > 5.0 or nota < 0.0:
#    print("Nota invalida")
#elif nota >= 4.5:
#    print("Nota Excelente")
#elif nota >= 4.0:
#    print("Nota Buena")
#elif nota >= 3.0:
#    print("Nota aprobatoria")
#else:
#    print("Reprobado")

'''Ejercicio 5 – Login simple
Guarda un usuario y una contraseña en variables. Pide al usuario que los escriba y:

si ambos coinciden → "Bienvenido"
si no → "Datos incorrectos" '''

#SaveUser = "Mao123"
#SavePassword = "Maocute"
#User = input("Ingresa tu usuario ")
#password = input("Ingresa la contraseña ")

#if User == SaveUser and password == SavePassword:
#    print("Bienvenido")
#else:
#    print("Datos incorrectos")


''' Ejercicio 6 – Fruta en la lista
Usa tu lista de frutas del ejercicio anterior. Pide el nombre de una fruta y di si está o no en la lista.
Pista: if "Mango" in frutas: '''
#frutas = ["mango", "fresa", "manzana", "naranja"]

#fruta = input("Ingresa la fruta a consultar ")
#if fruta.lower() in frutas:
#    print(f" {fruta} esta en lista")
#else:
#    print(f" {fruta} NO esta en lista")


'''Ejercicio 7 – Reto: calculadora
Pide dos números y una operación (+, -, *, /). Muestra el resultado de esa operación.

Si la operación es / y el segundo número es 0, muestra "No se puede dividir entre cero".
Si la operación no es válida, muestra "Operación no válida".  '''

numero5 = str(input("Ingresa numero 1 "))
numero6 = str(input("Ingresa numero 2 "))
operacion = input("Escoje una operacion:\n Suma = (+) \n Resta = (-) \n Multiplicacion = (*) \n Division = (/) \n")

if operacion == "+":
    print("La suma es : " + str(numero5 + numero6))
elif operacion == "-":
    print("La resta es : " + str(numero5 - numero6))
elif operacion == "*":
    print("La multiplicacion es : " + str(numero5 * numero6))
elif operacion == "/":
    if numero6 == 0:
        print("No se puede dividir entre cero")
    else:
        print("La division es : " + str(numero5 / numero6))
else:
    print("Operacion no valida")

