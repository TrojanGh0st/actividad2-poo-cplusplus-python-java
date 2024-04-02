# Clase Inventario: Administra los productos disponibles y agotados, así como los pedidos y facturas.
class Inventario:
    def __init__(self):
        self.productos_disponibles = []
        self.productos_agotados = []
        self.facturas = []

    def agregar_producto(self, producto):
        self.productos_disponibles.append(producto)

    def actualizar_inventario(self, producto, cantidad):
        if producto in self.productos_disponibles:
            if cantidad <= 0:
                self.productos_disponibles.remove(producto)
                self.productos_agotados.append(producto)
                print(f"{producto} se ha agotado.")
            else:
                print(f"Se han vendido {cantidad} unidades de {producto}.")
        else:
            print(f"No hay suficientes existencias de {producto}.")

    def realizar_pedido(self, cliente, productos):
        factura = {"cliente": cliente, "productos": productos}
        self.facturas.append(factura)
        print("Pedido realizado con éxito.")

# Ejemplo de uso:
inventario = Inventario()

# Agregar productos al inventario
inventario.agregar_producto("Camisa")
inventario.agregar_producto("Pantalón")
inventario.agregar_producto("Zapatos")

# Simular una venta y actualizar el inventario
inventario.actualizar_inventario("Camisa", 1)
inventario.actualizar_inventario("Pantalón", 2)
inventario.actualizar_inventario("Zapatos", 0)  # Indica que los zapatos están agotados

# Realizar un pedido para un cliente
inventario.realizar_pedido("Cliente1", ["Camisa", "Pantalón"])
