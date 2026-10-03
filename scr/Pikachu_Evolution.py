class Pikachu_Evolution:
    __tipo = "Acuatico"    # Atributo de clase

    def __init__(self, nombre, salud, nivel, voltaje_max, amperaje_max, color):  # Atributo de instancia
        self.__nombre = nombre
        self.set_salud(salud)
        self.set_nivel(nivel)
        self.__voltaje_max = voltaje_max
        self.set_amperaje_max(amperaje_max)
        self.color = color


    def atacar(self):
        print(f"El pikachu ataca y genera {self.nivel / 4 } de daño")



    # Getters
    @property
    def tipo(self):
        return self.__tipo

    @property
    def nombre(self):
        return self.__nombre


    @property   
    def voltaje_max(self):
        return self.__voltaje_max

    # Ota manera
    def get_amperaje_max(self):
        return self.__amperaje_max

    def get_salud(self):
        return self.__salud

    def get_nivel(self):
        return self.__nivel




    


    #Setters 
    def set_salud(self, salud):    # parametro de salud como parametro
        if salud < 0:
            print("La salud no puede ser negativa")
        else:
            self.__salud = salud

    @nombre.setter                   # Debe llamarse igual a la funcion del getter si es con @property
    def nombre(self, nombre):
        if nombre == "":
            print("Nombre Invalido")
        else:
            self.__nombre = nombre 


    def set_nivel(self, nivel):
        if not 0 <= nivel  <= 500:
            print("Nivel Invalido")  
        else:
            self.__nivel = nivel 

    @voltaje_max.setter
    def voltaje_max(self, voltaje):
        if not 0 <= voltaje <= 500:
            print("Voltaje Invalido")
        else:
            self.__voltaje_max = voltaje


    def set_amperaje_max(self, amperaje):
        if not 0 <= amperaje <= 1000:
            print("Amperaje Invalido")
        else:
            self.__amperaje_max = amperaje





pikachu_3 = Pikachu_Evolution("Ramiro", 152, 50, 50, 4, "Morado")   
# Getters     
print(f"Nombre: {pikachu_3.nombre} y su nivel de batalla es :  {pikachu_3.get_nivel()} y es de tipo : {pikachu_3.tipo}")

# Modificar atributos de instancia del objeto

# Setters
pikachu_3.__nivel = 700




# Modificar atributos de clase
#Pikachu_Evolution.tipo = 'Fuego'

