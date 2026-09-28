def calcular_precio(nombre_producto, cantidad, precio_u, descuento = 0):   # Descuento es opcional , la iniciamos en 0 si no se llama el parametro
    precio_final = (cantidad * precio_u) * (1-descuento)
    print(f"El precio final para {nombre_producto} es {precio_final}")

calcular_precio("Manzana", 5, 2500)    
