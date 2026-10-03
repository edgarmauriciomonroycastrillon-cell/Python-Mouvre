class Pokemon:


    ## Construtor
    def __init__(self, nombre, nivel, salud=100, color='Amarillo'):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.color = color


# Getters y setters

   # Nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


    # Salud
    @property
    def salud(self):
        return self.__salud

    @salud.setter
    def salud(self, salud):
        if not 0 <= salud <= 500:
            print("Salud invalida")
            self.__salud = 100     # Por si colocan un valor invalido el valor por defecto es 100
        else:
            self.__salud = salud


    # Nivel
    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        if nivel < 0:
            print("Nivel NO valido")
            self.__nivel = None   # Por si colocan un valor invalido por defecto el nivel va a hacer 1
        else: 
            self.__nivel = nivel
