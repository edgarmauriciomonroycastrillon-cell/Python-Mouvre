from tipofuego import TipoFuego
class Charmander(TipoFuego):

    def __init__(self, nombre, nivel, salud, color, temperatura_maxima):
        super().__init__(nombre, nivel, salud,color, temperatura_maxima)   # Herencia de atributos



if __name__ == "__main__":    # solo ejecutar una porcion de codigo
    charmander_1 = Charmander('Sof', 700, 1000, 'Rojo', 500)
    print("---------------------------------------------------------------------")
    print(f"Nombre: {charmander_1.nombre} \nNivel: {charmander_1.nivel} \nSalud: {charmander_1.salud} \nColor: {charmander_1.color} \nTemperatura Maxima: {charmander_1.temperatura_maxima}")


    print("---------------------------------------------------------------------")
    print("--------------------------------SETTER------------------------------")
    charmander_1.salud = 100
    charmander_1.temperatura_maxima = 1000
    print(f"Nombre: {charmander_1.nombre} \nNivel: {charmander_1.nivel} \nSalud: {charmander_1.salud} \nColor: {charmander_1.color} \nTemperatura Maxima: {charmander_1.temperatura_maxima}")
    charmander_1.atacar()    # Poliformismo , hereda de pokemon atacar pro con funcion de tipo fuego