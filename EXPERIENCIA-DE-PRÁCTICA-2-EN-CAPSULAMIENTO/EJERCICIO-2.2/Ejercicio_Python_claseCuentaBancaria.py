# Clase CuentaBancaria: Representa una cuenta bancaria con atributos como saldo y número de cuenta, y métodos get y set para cada atributo.
class CuentaBancaria:
    def __init__(self, saldo, numero_cuenta):
        self._saldo = saldo
        self._numero_cuenta = numero_cuenta

# a) Beneficios del uso de métodos get y set en la clase de cuenta bancaria:

# a) Beneficios del uso de métodos get y set en la clase de cuenta bancaria:

# - Encapsulamiento: Al utilizar los métodos get y set en la clase de cuenta bancaria, se puede controlar el acceso a los atributos como saldo y número de cuenta. Esto ayuda a mejorar la seguridad y privacidad de la información de la cuenta bancaria, ya que evita que los atributos sean modificados directamente desde fuera de la clase sin la validación adecuada.
# - Validación de datos: Los métodos set pueden incluir lógica para validar los datos antes de establecer un nuevo valor para el saldo o el número de cuenta. Por ejemplo, se puede verificar si el saldo es positivo antes de realizar una transacción o si el número de cuenta tiene el formato correcto. Esto ayuda a garantizar la integridad de los datos y prevenir errores en la manipulación de la cuenta bancaria.


    # Métodos get para cada atributo
    def get_saldo(self):  # Obtener saldo
        return self._saldo

    def get_numero_cuenta(self):  # Obtener número de cuenta
        return self._numero_cuenta

    # Métodos set para cada atributo
    def set_saldo(self, saldo):  # Establecer saldo
        self._saldo = saldo

    def set_numero_cuenta(self, numero_cuenta):  # Establecer número de cuenta
        self._numero_cuenta = numero_cuenta


# b) Cómo se pueden utilizar los métodos get y set para actualizar y recuperar información sobre diferentes cuentas bancarias:

# Objetos
cuenta1 = CuentaBancaria(1000, "1234567890")
cuenta2 = CuentaBancaria(5000, "0987654321")

# GET Y SET
# Actualizar información utilizando métodos set
cuenta1.set_saldo(1500)
cuenta2.set_numero_cuenta("9876543210")

# Recuperar información utilizando métodos get
print(cuenta1.get_saldo(), cuenta1.get_numero_cuenta())
print(cuenta2.get_saldo(), cuenta2.get_numero_cuenta())
