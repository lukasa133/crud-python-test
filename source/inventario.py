class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad):
        self.productos.append({
            "nombre": nombre,
            "cantidad": cantidad
        })
    
    def actualizar_producto(self, nombre, cantidad):
        producto = self.consultar_producto(nombre)
        producto["cantidad"] = cantidad
    
    def consultar_producto(self, nombre):
        for producto in self.productos:
            if producto["nombre"] == nombre:
                return producto
        
    
    def eliminar_producto(self, nombre):
        producto = self.consultar_producto(nombre)
        self.productos.remove(producto)

