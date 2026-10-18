from poo_repaso import producto

class ProductoPerecedero(producto):

    def __init__(self, nombre, precio, stock,dias_para_vencer):
        super().__init__(nombre, precio, stock)
        self.dias_para_vencer = dias_para_vencer

    #Getter y Setter de la propia clase
    @property
    def dias_para_vencer(self):
        return self.__dias_para_vencer

    @dias_para_vencer.setter
    def dias_para_vencer(self, dias_para_vencer):
        self.__dias_para_vencer = dias_para_vencer


    #Funcion propia
    def esta_vencido(self):
        if self.__dias_para_vencer <= 0:
            return True
        return False 

    def __str__(self):   # Se imprime solo sin necesidad de llamarlo 
        return f"{super().__str__()} se vence en {self.__dias_para_vencer} dias"


# Prueba
if __name__ == "__main__":
    carne = ProductoPerecedero("Carne", 1500, 5, 2)   
    print(carne)