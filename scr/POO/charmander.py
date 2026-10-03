from Pokemon import Pokemon
class Charmander(Pokemon):

    def __init__(self, nombre, nivel, salud, color):
        super().__init__(nombre, nivel, salud,color)   # Herencia de atributos


charmander_1 = Charmander('Sof', 700, 1000, 'Rojo')
print("---------------------------------------------------------------------")
print(f"Nombre: {charmander_1.nombre} \nNivel: {charmander_1.nivel} \nSalud: {charmander_1.salud} \nColor: {charmander_1.color}")


print("---------------------------------------------------------------------")
print("--------------------------------SETTER------------------------------")
charmander_1.salud = 100
print(f"Nombre: {charmander_1.nombre} \nNivel: {charmander_1.nivel} \nSalud: {charmander_1.salud} \nColor: {charmander_1.color}")