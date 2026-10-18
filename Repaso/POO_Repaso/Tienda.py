from poo_repaso import producto
from Herencia import ProductoPerecedero

class Tienda():

    def __init__(self):
        self.productos = []

    def agregar(self,producto):
        self.productos.append(producto)

    def buscar(self, nombre):
        for p in self.productos:
            if p.nombre == nombre:
                return p
        return None
    
    def valor_inventario(self):
        total = 0
        for p in self.productos:
            total += p.precio * p.stock
        return total

    def __len__(self):
        return len(self.productos)