class producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    #Getter y Setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        if precio < 0:
            print("Precio NO VALIDO, se mantiene el anterior")
        else:
            self.__precio = precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock





    #Funcion propia
    def __str__(self):
        return (f"{self.nombre} - ${self.precio} - (stock: {self.stock})")

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.__stock -+ cantidad  
            return True
        print("No hay suficiente stock")
        return False
 

    def reponer(self, cantidad):
        self.__stock += cantidad












    # Pruebas 

if __name__ == "__main__":
    cafe = producto('Cafe', 12000, 1)
    print(cafe)

    cafe.precio = -500
    print(cafe)

    print(cafe.vender(55))