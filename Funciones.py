# Funciones

#def saludar_usuario():  # entre los parentesis () van los parametros
#    print("Hola como estas")   # si ejecutamos no pasa nada porque NO la llamamos
#    print("Adios")

#saludar_usuario()    #llamamos funcion    





num1 = int(input("Ingrese numero 1 "))
num2 = int(input("Ingrese numero 2 "))

def sumar (num1, num2):
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")

def restar (num1, num2):
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")

def multiplicar (num1, num2):
    resultado = num1 * num2
    print(f"El resultado de la multiplicacion es: {resultado}")

def dividir (num1, num2):
    resultado = num1 / num2
    print(f"El resultado de la division es: {resultado}")




sumar(num1, num2)  # Colocar los parametros al llamar la funciones  
restar(num1, num2)
multiplicar(num1, num2)
dividir(num1, num2)


