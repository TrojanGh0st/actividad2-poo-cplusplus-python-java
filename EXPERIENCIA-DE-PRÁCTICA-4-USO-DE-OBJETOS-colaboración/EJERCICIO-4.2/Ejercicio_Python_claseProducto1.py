# Clase Producto: Representa un producto con atributos como nombre, precio y cantidad.
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

# Clase Factura: Representa una factura con un método para agregar productos.
class Factura:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

# a) ¿Cómo se crea una clase de factura?
# Se crea una clase llamada Factura con la palabra clave class seguida del nombre de la clase.
# Por ejemplo:
# class Factura:

# b) ¿Cómo se crea una clase de producto?
# Se crea una clase llamada Producto con la palabra clave class seguida del nombre de la clase.
# Por ejemplo:
# class Producto:

# c) ¿Cómo se utiliza un objeto de la clase de producto como parámetro en el método de la clase de factura?
# El objeto de la clase Producto se pasa como parámetro al llamar al método de la clase Factura.
# Por ejemplo:
# factura = Factura()
# producto = Producto("Camisa", 20, 2)
# factura.agregar_producto(producto)

# d) ¿Cómo se agrega un objeto a una lista?
# Para agregar un objeto a una lista, se utiliza el método append(). En este caso, se utiliza para agregar un producto a la lista de productos en la clase Factura.
# Por ejemplo:
# productos = []  # Lista vacía
# producto = Producto("Camisa", 20, 2)  # Crear un objeto de la clase Producto
# productos.append(producto)  # Agregar el producto a la lista
