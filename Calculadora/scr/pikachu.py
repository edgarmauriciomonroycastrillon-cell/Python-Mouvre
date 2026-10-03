class pikachu:

    ## Atributos : todos los objetos lo comparten
    tipo = 'Electrico'   # Todos son electricos 


    # Construtores
    def __init__(self, nombre, nivel=1, salud=100):    # Construtor , solo 1
        self.nombre = nombre                           #Variables que pueden cambiar del objeto ,pero que lo deben llevar
        self.nivel = nivel
        self.salud = salud


    # Metodos
    def atacar(self):       # self es yo mismo 
        print(f"Pikachu ataca y genera : {self.nivel / 4} de daño")   # Llamar los atributos con self. antes
    


# Creacion de objeto
pikachu_1 = pikachu('mario', 120, 200)   # puede ir con clave y con posicion , pero si se combina simepre primero las posiciones
pikachu_2 = pikachu('Roberto', salud=200, nivel=5)

print("-------------------------------------------------------------------")
print(pikachu_1.tipo, pikachu_1.nombre, pikachu_1.nivel, pikachu_1.salud)
print(f"El picachu {pikachu_1.nombre} ataca")
pikachu_1.atacar()


print("-------------------------------------------------------------------")
print(pikachu_2.tipo, pikachu_2.nombre, pikachu_2.nivel, pikachu_2.salud)
print(f"El picachu {pikachu_2.nombre} ataca")
pikachu_2.atacar()
