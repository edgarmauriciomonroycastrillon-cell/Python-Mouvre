from tipoelectrico import TipoElectrico

class PikachuAmarillo( TipoElectrico):




    def __init__(self,nombre, salud, nivell, voltaje_max, amperaje_max, color):
        super().__init__(nombre=nombre,nivel=nivell,salud=salud,color=color, voltaje_maximo=voltaje_max, amperaje_maximo=amperaje_max)  # Heredamos sus atributos , de esta manera





     #Getters y Setters   , los de padre no viven aqui
     
    def atacar(self):
        print(f"Pikachu ataca y genera {self.nivel/4} daño")
    



pikachu_4 = PikachuAmarillo("Ramiro", 152, 50, 50, 4, "Morado")   
# Getters     
print(f"Nombre: {pikachu_4.nombre} y su nivel de batalla es :  {pikachu_4.nivel} y es de tipo : {pikachu_4.tipo}")