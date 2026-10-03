import aritmeticas.operaciones_basicas  as operacionbasicas # llamamos otro archivo y lo guardamos comom alias
import aritmeticas.operaciones_avanzadas as operaciones_avanzadas

suma = operacionbasicas.sumar(2,2)
print(f"El resultado de la suma es: {suma}")

multiplicacion = operaciones_avanzadas.multiplicar(2,3)
print(f"El resultado de la multiplicacion es: {multiplicacion}" )