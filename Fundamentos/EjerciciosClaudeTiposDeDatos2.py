# Ejericicio 1 , tipos de datos
a = 25
b = 3.14
c = "Hola"
d = True
e = None

# Ejercicio 2 Determinar los tipos de datos
print("El tipo de dato de a es : " + str(type(a)))
print("El tipo de dato de b es: " + str(type(b)))
print("El tipo de dato de b es: " + str(type(c)))
print("El tipo de dato de b es: " + str(type(d)))
print("El tipo de dato de b es: " + str(type(e)))

# Ejercicio 3 Converion de tipos
edad = "30"
print(" La conversion de 30 a int + 5  = " + str(int(edad) + 5))

# Ejercicio 4 Numeros decimales
altura = int(input("Ingrese su altura en metros : "))
print("Su altura en cm es : " + str(altura * 100)) 

# Ejercicio 5 Booleanos
x = 10
y = 20
print(type(x > y)) 
print(type(x == 10))
print(type(x != y))

# Ejercicio 6 , Listas
frutas = ["Mango", "Fresa", "Manzana", "Naranja"]
print("La segunda fruta es: " + str(frutas[1]))
frutas.append("Coco")
print("Total de frutas : " + str(len(frutas)))


# Ejercicio 7, Diccionario
persona = dict.fromkeys(["nombre", "edad", "ciudad"])
print(persona["edad"])

persona["nombre"] = "Mao"
persona["edad"] = 21
persona["ciudad"] = "Bogota"

print(type(persona["edad"]))
print(type(persona["nombre"]))
print(type(persona["ciudad"]))