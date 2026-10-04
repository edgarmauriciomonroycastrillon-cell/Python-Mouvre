from tipoelectrico import TipoElectrico

class PikachuAmarillo(TipoElectrico):




    def __init__(self,nombre, salud, nivell, voltaje_max, amperaje_max, color, 
                 longitud_cola=0):
        super().__init__(nombre=nombre,nivel=nivell,salud=salud,color=color, voltaje_maximo=voltaje_max, amperaje_maximo=amperaje_max)  # Heredamos sus atributos , de esta manera
        self.longitud_cola = longitud_cola


     #Getters y Setters   , los de padre no viven aqui, las propias de la clase si

    @property
    def longitud_cola(self):
        return self.__longitud_cola

    @longitud_cola.setter
    def longitud_cola(self, longitud_cola):
        if longitud_cola < 0:
            print("Longitud cola invalida , 0 cm por defecto")
            self.__longitud_cola = 0    # por defecto 0 si la colocan mal
        else:
            self.__longitud_cola = longitud_cola


    # Metodo propios
    def atacar_cola_hierro(self):
        print(f"Ataque con Cola de Hierro y genera {self.longitud_cola/0.5}")   # Clase abstratas , tiene su operaciones y el objeto solo las llama
                                                                                # No las ve
   

if __name__ == '__main__':   # solo ejecutar una porcion de codigo

    pikachu_4 = PikachuAmarillo("Ramiro", 152, 50, 50, 4, "Morado", 150)   
    # Getters     
    print(f"Nombre: {pikachu_4.nombre} y su nivel de batalla es :  {pikachu_4.nivel} y es de tipo : {pikachu_4.tipo} y su longitud es: {pikachu_4.longitud_cola}" )


    pikachu_4.atacar()
    pikachu_4.atacar_cola_hierro()