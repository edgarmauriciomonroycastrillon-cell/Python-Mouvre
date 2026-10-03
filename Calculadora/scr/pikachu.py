class pikachu:
    tipo = 'Electrico'   # Todos son electricos 

    def __init__(self, nombre, nivel=1, salud=100):    # Construtor , solo 1
        self.nombre = nombre                           #Variables que pueden cambiar del objeto ,pero que lo deben llevar
        self.nivel = nivel
        self.salud = salud

# Creacion de objeto
pikachu_1 = pikachu('mario', 120, 200)   # puede ir con clave y con posicion , pero si se combina simepre primero las posiciones
pikachu_2 = pikachu('Roberto', salud=200, nivel=5)


print(pikachu_1.tipo, pikachu_1.nombre, pikachu_1.nivel, pikachu_1.salud)
print(pikachu_2.tipo, pikachu_2.nombre, pikachu_2.nivel, pikachu_2.salud)