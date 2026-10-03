# Funciones

#def saludar_usuario():  # entre los parentesis () van los parametros
#    print("Hola como estas")   # si ejecutamos no pasa nada porque NO la llamamos
#    print("Adios")

#saludar_usuario()    #llamamos funcion    



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




continuar = "SI"
while continuar.lower() == "si":
    num1 = int(input("Ingrese numero 1 : "))
    num2 = int(input("Ingrese numero 2 : "))
    operacion = input("Ingrese la operacion: ")

    if operacion.lower() == "sumar" : 
        sumar(num1, num2)
    elif operacion.lower() == "restar" :
        restar(num1, num2)
    elif operacion.lower() == "multiplicar" : 
        multiplicar(num1, num2)
    elif operacion.lower() == "dividir" :
        dividir(num1, num2)
    else:
        print("Operacion NO valida") 
    continuar = input("Si desea continuar escribe SI :")



