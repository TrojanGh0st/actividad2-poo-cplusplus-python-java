# Clase Tienda: Representa una tienda con atributos como nombre, dirección y tipo de tienda, y métodos para interactuar con la tienda.
class Tienda:
    def __init__(self, nombre, direccion, tipo):
        self.nombre = nombre
        self.direccion = direccion
        self.tipo = tipo
        self.productos = []  # Lista para almacenar los productos de la tienda

    # Métodos para acceder a los atributos
    def get_nombre(self):  # Nombre de la tienda
        return self.nombre

    def get_direccion(self):  # Dirección de la tienda
        return self.direccion

    def get_tipo(self):  # Tipo de tienda
        return self.tipo

  
#a) ¿Qué métodos son necesarios para vender y agregar productos a las tiendas?
  
    # Método para vender un producto
    def vender_producto(self, producto):
        if producto in self.productos:
            print("Se vendió el producto " + producto + " en " + self.nombre + ".")
            self.productos.remove(producto)
        else:
            print("El producto " + producto + " no está disponible en " + self.nombre + ".")

    # Método para agregar un producto
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Se agregó el producto " + producto + " a " + self.nombre + ".")

# b) ¿Cómo se pueden crear diferentes objetos para representar diferentes tiendas?

tienda1 = Tienda("Supermercado ABC", "Av. Principal 123", "Supermercado")
tienda2 = Tienda("Librería XYZ", "Calle Secundaria 456", "Librería")
tienda3 = Tienda("Ferretería 123", "Plaza Central 789", "Ferretería")

# Interactuar con las tiendas
tienda1.agregar_producto("Manzanas")
tienda1.agregar_producto("Plátanos")
tienda1.vender_producto("Manzanas")

tienda2.agregar_producto("Libro de Matemáticas")
tienda2.agregar_producto("Libro de Historia")
tienda2.vender_producto("Libro de Matemáticas")

tienda3.agregar_producto("Martillo")
tienda3.agregar_producto("Destornillador")
tienda3.vender_producto("Destornillador")
