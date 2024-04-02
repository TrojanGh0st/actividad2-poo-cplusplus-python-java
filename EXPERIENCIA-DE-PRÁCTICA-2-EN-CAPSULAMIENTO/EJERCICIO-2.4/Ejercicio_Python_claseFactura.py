# Clase Factura: Representa una factura con atributos como número de factura, fecha de emisión y monto, y métodos get y set para cada atributo.
class Factura:
    def __init__(self, numero_factura, fecha_emision, monto):
        self._numero_factura = numero_factura
        self._fecha_emision = fecha_emision
        self._monto = monto

# a) Beneficios del uso de métodos get y set en la clase de factura:

# - Encapsulamiento: Al utilizar los métodos get y set en la clase de factura, se puede controlar el acceso a los atributos como número de factura, fecha de emisión y monto. Esto ayuda a mejorar la seguridad y privacidad de la información de la factura, ya que evita que los atributos sean modificados directamente desde fuera de la clase sin la validación adecuada.
# - Validación de datos: Los métodos set pueden validar los datos antes de establecer un nuevo valor para el número de factura, la fecha de emisión o el monto. 

    # Métodos get para cada atributo
    def get_numero_factura(self):  # Obtener número de factura
        return self._numero_factura

    def get_fecha_emision(self):  # Obtener fecha de emisión
        return self._fecha_emision

    def get_monto(self):  # Obtener monto
        return self._monto

    # Métodos set para cada atributo
    def set_numero_factura(self, numero_factura):  # Establecer número de factura
        self._numero_factura = numero_factura

    def set_fecha_emision(self, fecha_emision):  # Establecer fecha de emisión
        self._fecha_emision = fecha_emision

    def set_monto(self, monto):  # Establecer monto
        self._monto = monto

# b) Cómo se pueden utilizar los métodos get y set para actualizar y recuperar información sobre diferentes facturas:

# Objetos
factura1 = Factura("001", "2024-04-01", 100.50)
factura2 = Factura("002", "2024-04-02", 200.75)

# GET Y SET
# Actualizar información utilizando métodos set
factura1.set_monto(150.25)
factura2.set_fecha_emision("2024-04-03")

# Recuperar información utilizando métodos get
print(factura1.get_numero_factura(), factura1.get_fecha_emision(), factura1.get_monto())
print(factura2.get_numero_factura(), factura2.get_fecha_emision(), factura2.get_monto())
