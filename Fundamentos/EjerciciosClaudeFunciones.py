'''🟢 Nivel 1: Calentamiento

1. Convertidor de temperatura
Crea celsius_a_fahrenheit(c) y fahrenheit_a_celsius(f). 
Las dos deben usar return, no print. Pruébalas con 0, 100 y -40 (¿qué tiene de curioso el -40? 🤔).'''


def celsius_a_fahrenheit (tem_en_c):
    resultado = (tem_en_c * 1.8) + 32
    return resultado

def fahrenheit_a_celsius (tem_en_f):
    resultado = (tem_en_f-32) / 1.8 
    return resultado



for temp in [0,100,-40]:
    print(f"{temp} °C = {celsius_a_fahrenheit(temp):.1f} °F")
    print(f"{temp} °F = {fahrenheit_a_celsius(temp):.1f} °C")


'''2. Validar edad
Crea es_mayor_de_edad(edad, limite=18) que retorne True o False. Úsala con el límite por defecto y con limite=21.
'''

def es_mayor_de_edad (edad, limite=18):
    return edad >= limite 

print(es_mayor_de_edad(18))
print(es_mayor_de_edad(18,21))

'''Área y perímetro
Crea rectangulo(base, altura) que retorne dos valores: el área y el perímetro. 
Recíbelos con desempaquetado: area, perimetro = rectangulo(5, 3).'''

def rectangulo (base, altura):
    area = base * altura
    perimetro = (2*base) + (2*altura)
    return area, perimetro
area, perimetro = rectangulo(5,3)
print(f'El area es: {area} - El perimetro es: {perimetro}' )


'''. Refactoriza tu Funciones.py
Cambia tus 4 funciones de la calculadora para que usen return en vez de print. 
Protege dividir para que retorne None si el divisor es 0.'''

#def sumar (num1, num2):
'''Resultado es la variable que suma num1 y num 2'''
#    resultado = num1 + num2
'''Retornamos la variable resultado , SOLO VIVE EN LA FUNCION NO LA GUARDA EN UNA VARIABLE, ES LOCAL DE LA FUNCION
    SI QUEREMOS GUARDARLA MAS ADELANTE SERIA ASI:
    resultado_suma = sumar(5,3) , resultado_suma = 8 , la pasamos a global'''
#    return resultado

#def restar (num1, num2):
#    resultado = num1 - num2
#    return resultado

#def multiplicar (num1, num2):
#    resultado = num1 * num2
#    return resultado

#def dividir (num1, num2):
#    if num2 == 0:
#        return None
#    resultado = num1 / num2
#    return resultado

#continuar = "SI"
#while continuar.lower() == "si":
#    num1 = int(input("Ingrese numero 1 : "))
#    num2 = int(input("Ingrese numero 2 : "))
#    operacion = input("Ingrese la operacion: ")

#    if operacion.lower() == "sumar" : 
#        print(f"La suma es : {sumar(num1, num2)}")
#    elif operacion.lower() == "restar" :
#        print(f"La resta es : {restar(num1, num2)}")
#    elif operacion.lower() == "multiplicar" : 
#        print(f"La multiplicacion es : {multiplicar(num1, num2)}")
#    elif operacion.lower() == "dividir" :
#        print(f"La division es : {dividir(num1, num2)}")
  
#    else: 
#        print("Operacion NO Valida")
#        
#    continuar = input("Si desea continuar escribe SI: ")






'''5. Docstring
A cualquier función anterior agrégale un docstring: , LISTO'''


'''6. Filtrar pares
Crea filtrar_pares(lista) que retorne una nueva lista solo con los números pares.
Casos límite: lista vacía y lista sin pares.'''

def filtrar_pares (lista):
    numeros_pares = []

    for i in lista:
        if i % 2 == 0:
            numeros_pares.append(i)

    return numeros_pares




numeros1 = [10,15,20,35,69,54,12,87,32,45,86,13,78,23]
numeros2 = []
numeros3 = [5,7,9,1,17,41,59]

# Caso 1 , numeros pares e impares
numeros_pares = filtrar_pares(numeros1)
# Los organizo
numeros_pares.sort()
#Imprimo
print(numeros_pares)

# Caso 2 , lista vacia
lista_vacia = filtrar_pares(numeros2)
print(lista_vacia)  # Retorno vacia

# Caso 3, Solo impares
lista_solo_impares = filtrar_pares(numeros3)
print(lista_solo_impares)  # Retorna solo vacio

'''7. Contar palabras
Crea contar_palabras(frase) que retorne un diccionario con cuántas veces aparece cada palabra.'''

def contar_palabra (frase):
    palabras = frase.split()
    contador = {}

    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1

    return contador



frase_prueba = "Hola mundo como esta hola hola Hola"
print(contar_palabra(frase_prueba))  # Este lo hice con ayuda de IA no entendia muy bien



'''8. Eliminar duplicados
Crea sin_duplicados(lista) que retorne la lista sin elementos repetidos. 
Hazla de dos formas: con un set y con un for, manteniendo el orden original.'''
def sin_duplicado_set (lista_duplicada_original):
    lista_nueva = list(set(lista_duplicada_original))
    return lista_nueva


def sin_duplicado_for (lista_duplicada_original):
    lista_nueva = []

    for numero in lista_duplicada_original:
        if numero not in lista_nueva:
            lista_nueva.append(numero)
    return lista_nueva


lista_duplicada = [1,1,1,2,3,4,5,5,5,5,6]


#Set

lista_limpia_set = sin_duplicado_set(lista_duplicada)
print(lista_limpia_set)

#For
lista_limpia_for = sin_duplicado_for(lista_duplicada)
print(lista_limpia_for)



''''
9. Carrito de compras con **kwargs
Crea resumen_compra(cliente, *productos, **opciones):

productos son los precios
opciones puede traer descuento, envio y cupon
'''

def resumen_compra (cliente, *productos, **opciones):
    precio_bruto = sum(productos)
    descuento = opciones.get('descuento', 0)
    envio = opciones.get('envio', 0)
    cupon = opciones.get('cupon', 0)
    precio_neto = precio_bruto + envio * (1-descuento) - cupon
#    print("-----------------COMPRA------------------------")
    return cliente, productos, precio_neto

Total = resumen_compra("Mario", 10,14,25,89,107, descuento = 0.2, envio = 10)
print(f"Nombre cliente: {Total[0]},\nPrecio de los productos comprados {Total[1]},\nTotal a pagar : {Total[2]}")


'''10. Buscar en lista de diccionarios
Tienes esta lista:

Crea tres funciones:

buscar_estudiante(lista, nombre), que retorne el diccionario o None
aprobados(lista, minimo=3.0), que retorne los nombres de quienes aprobaron (cuidado con el >= 😉)
mejor_estudiante(lista)


'''


def buscar_estudiante (lista, nombre):
    for estudiante in lista:
        if estudiante["nombre"] == nombre:
            return estudiante
    return None


def estudiantes_aprobados (lista, minimo=3.0):

    estudiantes_aprobados = []

    for aprobados in lista:
        if aprobados['nota'] >= minimo:
            estudiantes_aprobados.append(aprobados["nombre"])
    return estudiantes_aprobados


def mejor_estudiante (lista):
    mejor = lista[0]

    for i in lista:
        if i['nota'] > mejor['nota']:
            mejor = i
    return i





estudiantes = [
    {"nombre": "Mao", "nota": 4.5},
    {"nombre": "Ana", "nota": 2.8},
    {"nombre": "Luis", "nota": 3.9},
]

print(buscar_estudiante(estudiantes,"Ana"))
print(estudiantes_aprobados(estudiantes))
print(mejor_estudiante(estudiantes))