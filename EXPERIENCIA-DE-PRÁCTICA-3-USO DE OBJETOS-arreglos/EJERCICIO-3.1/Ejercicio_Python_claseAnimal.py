# Clase Animal: Representa a un animal con atributos como nombre, edad y tipo, y métodos para interactuar con el animal.
class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    # Métodos get para cada atributo
    def get_nombre(self):  # Obtener nombre
        return self.nombre

    def get_edad(self):  # Obtener edad
        return self.edad

    def get_tipo(self):  # Obtener tipo
        return self.tipo

    # Método para alimentar al animal
    def alimentar_animal(self):
        print(self.nombre + " fue alimentado.")

    # Método para hacer sonidos
    def hacer_sonido(self):
        if self.tipo == "perro":
            print("¡Guau!")
        elif self.tipo == "gato":
            print("¡Miau!")
        elif self.tipo == "oveja":
            print("¡Beee!")
        else:
            print("No está en la lista.")

    # a) ¿Cómo se crean objetos de una clase?
    # Para crear un objeto de la clase Animal, se utiliza el nombre de la clase dentro de paréntesis los argumentos.
    # Ejemplo:
    # perro = Animal("Chimuelo", 2, "perro")

    # b) ¿Cómo se establecen los valores de los atributos de un objeto?
    # Los valores de los atributos de un objeto se establecen utilizando el constructor de la clase al crear el objeto.

    # c) ¿Cómo se recuperan los valores de los atributos de un objeto?
    # Los valores de los atributos de un objeto se recuperan utilizando los métodos get definidos en la clase Animal.
    # Ejemplo:
    # nombre = perro.get_nombre()
    # edad = perro.get_edad()
    # tipo = perro.get_tipo()

