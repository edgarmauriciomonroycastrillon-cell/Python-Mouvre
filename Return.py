def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"La suma entre {numero1} y {numero2} es:  {resultado}")

resultado = sumar(3,3)  # el resultado no se guarda dentro de la variable
print(f"El resultado es {resultado}")



# Return para devolver un resultado desde la funcion , y guardar
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado   # el resultado guardalo dentro de la variable resultado


resultado = sumar(3,3)  
resultado_final = resultado * 2  # podemos utilizar el resultado de la funcion para volver a operar
print(f"El resultado es {resultado_final}")





# Multiples retornos / returns
def calcular_precio(nombre_producto, cantidad, precio_u, descuento = 0):   # Descuento es opcional , la iniciamos en 0 si no se llama el parametro
    precio_final = (cantidad * precio_u) * (1-descuento)
    return nombre_producto, cantidad, precio_final   # Aca definimos/retornamos un tupla

compra_final = calcular_precio("Medias", 5, 2500)  # Lo guarda en una tupla
print(f"El precio final es : {compra_final[2]}")

