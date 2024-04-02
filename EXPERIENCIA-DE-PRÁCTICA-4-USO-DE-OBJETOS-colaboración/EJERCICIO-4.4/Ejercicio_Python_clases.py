# Clase Producto: Representa un producto con atributos como nombre y precio.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Clase Tienda: Representa una tienda con una lista de productos disponibles y una lista de compras de clientes.
class Tienda:
    def __init__(self):
        self.productos_disponibles = []
        self.lista_compras = []

# Clase Cliente: Representa un cliente con una lista de productos comprados.
class Cliente:
    def __init__(self):
        self.lista_compras = []

    def agregar_producto(self, producto):
        self.lista_compras.append(producto)

    def pagar_cuenta(self):
        total = sum(producto.precio for producto in self.lista_compras)
        print(f"Total a pagar: ${total}")

# a) ¿Cómo se crea una clase de tienda?
# Se crea una clase llamada Tienda con la palabra clave class seguida del nombre de la clase.
# Por ejemplo:
# class Tienda:

# b) ¿Cómo se crea una clase de cliente?
# Se crea una clase llamada Cliente con la palabra clave class seguida del nombre de la clase.
# Por ejemplo:
# class Cliente:

# c) ¿Cómo se utilizan objetos de la clase de producto como elementos de una lista?
# Se crean objetos de la clase Producto y se agregan a una lista.
# Por ejemplo:
# producto1 = Producto("Camisa", 20)
# producto2 = Producto("Pantalón", 30)
# lista_productos = [producto1, producto2]

# d) ¿Cómo se agregan elementos a una lista?
# Se utiliza el método append() para agregar elementos a una lista.
# Por ejemplo:
# lista = []  # Lista vacía
# elemento = "elemento"  # Crear un elemento
# lista.append(elemento)  # Agregar el elemento a la lista
