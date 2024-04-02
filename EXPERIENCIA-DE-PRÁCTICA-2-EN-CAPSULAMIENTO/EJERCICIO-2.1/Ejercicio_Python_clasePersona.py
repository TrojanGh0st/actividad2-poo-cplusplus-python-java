# Clase Persona: Representa a una persona con atributos como nombre, edad y género, y métodos get y set para cada atributo.
class Persona:
    def __init__(self, nombre, edad, genero):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero

# a) Beneficios del uso de métodos get y set en la clase de persona:

# - Encapsulamiento: Al usar los métodos get y set se puede controlar el acceso a los atributos de la clase, lo que mejora la seguridad o privacidad, así también para evitar que hayan modificaciones erradas.
# - Validación de datos: Al usar se puede controlar y validar.
  
    # Métodos get para cada atributo
    def get_nombre(self):  # Obtener nombre
        return self._nombre

    def get_edad(self):  # Obtener edad
        return self._edad

    def get_genero(self):  # Obtener género
        return self._genero

    # Métodos set para cada atributo
    def set_nombre(self, nombre):  # Establecer nombre
        self._nombre = nombre

    def set_edad(self, edad):  # Establecer edad
        self._edad = edad

    def set_genero(self, genero):  # Establecer género
        self._genero = genero



# b) Cómo se pueden utilizar los métodos get y set para actualizar y recuperar información sobre diferentes personas:

# Objetos
persona1 = Persona("Juan", 25, "Masculino")
persona2 = Persona("María", 30, "Femenino")

# GET Y SET
# Actualizar información utilizando métodos set
persona1.set_edad(26)
persona2.set_genero("Femenina")

# Recuperar información utilizando métodos get
print(persona1.get_nombre(), persona1.get_edad(), persona1.get_genero())
print(persona2.get_nombre(), persona2.get_edad(), persona2.get_genero())
