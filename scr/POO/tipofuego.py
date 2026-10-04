from Pokemon import Pokemon

class TipoFuego(Pokemon):


    def __init__(self, nombre, nivel, salud, color, temperatura_maxima):
        super().__init__(nombre, nivel, salud, color)
        self.temperatura_maxima = temperatura_maxima


## Getter
    @property
    def temperatura_maxima(self):
        return self.__temperatura_maxima

# Setter
    @temperatura_maxima.setter
    def temperatura_maxima(self, temperatura_maxima):
        if not 0 <= temperatura_maxima <= 1000: 
            print("Temperatura NO valida, temperatura por defecto 100°")
            self.__temperatura_maxima = 100
        else:
            self.__temperatura_maxima = temperatura_maxima 


    def atacar(self):
        print(f"Ataque con fuego y genera {self.temperatura_maxima * 0.5}" )