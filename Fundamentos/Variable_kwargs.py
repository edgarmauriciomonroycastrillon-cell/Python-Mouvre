# Numero indeterminado de argumentos e identificado con una clave
def conectar_bd(**kwargs):     # Simepre con dos ateriscos ** , el tipo de objeto es un diccionario
    nombre = kwargs['nombre_bd']   # Del dicionario llamos con la clave el valor, guardamos lo que nos pasen en un diccionario
    user = kwargs['usuario']       # NO necesariamente se trabajan con todos los parametros del dict
    password = kwargs.get('password' , 'default')   # Si no tenemos la clave o no la encuentra en el dict la creamos con get
    port = kwargs['port']
    dir_bd = kwargs['dir_bd']
    print(f"Conectado con la base de datos {nombre}")
    print(f"login with {user} - {password}")


conectar_bd(nombre_bd='generico', usuario='root', port=5002, dir_bd='10.25.47.89', query = 'SELECT * FROM ') # Diccionario lo llamamos de api u otra