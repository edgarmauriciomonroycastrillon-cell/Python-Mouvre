def calcular_precio_total (*args, **kwargs):
    precio_total = sum(args)
    descuento = kwargs.get('descuento',0)   # si no existe es 0
    impuesto = kwargs.get('impuesto',0)

    precio_total -=  (precio_total * descuento)
    precio_total += (precio_total * impuesto)

    return precio_total

precio_final = calcular_precio_total(100, 65, 30, descuento = 0.2, impuesto = 0.01)  # primera 3 son los args (argumentos), despues kwargs para la clave
print(f"El precio final es : {precio_final}")