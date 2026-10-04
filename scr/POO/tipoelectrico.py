from Pokemon import Pokemon

class TipoElectrico(Pokemon):
    __tipo = 'Electrico'

## Construto
    def __init__(self,nombre, nivel, salud, color, voltaje_maximo, amperaje_maximo):
        super().__init__(nombre=nombre, nivel=nivel, salud=salud, color=color)
        self.voltaje_max = voltaje_maximo
        self.amperaje_max = amperaje_maximo






## Getters y Setters
    #Tipo
    @property
    def tipo(self):
        return self.__tipo
   

    # Voltaje
    @property
    def voltaje_max(self):
        return self.__voltaje_max

    @voltaje_max.setter
    def voltaje_max(self, voltaje):
        if not 0 < voltaje <= 100:
            print("Voltaje NO valido")
        else:
            self.__voltaje_max = voltaje

    # Amperaje
    @property
    def amperaje_max(self):
        return self.__amperaje_max

    @amperaje_max.setter
    def amperaje_max(self, amperaje): 
        if not 0 < amperaje <= 200:
            print("Amperaje NO valido")
        else:
            self.__amperaje_max = amperaje 

         
    def atacar(self):
        print(f"Ataca con electricidad y genera {(self.amperaje_max + self.voltaje_max)/4} daño")

