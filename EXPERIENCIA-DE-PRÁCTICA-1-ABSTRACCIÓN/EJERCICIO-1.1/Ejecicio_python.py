# Clase Animal: Representa a un animal con atributos como nombre, edad y tipo, y métodos para interactuar con el animal.
class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    # Métodos para acceder a los atributos
    def get_nombre(self):  # Nombre del animal
        return self.nombre

    def get_edad(self):  # Edad del animal
        return self.edad

    def get_tipo(self):  # Tipo de animal
        return self.tipo

# a) Qué métodos son necesarios para hacer sonidos y alimentar a los animales?
  
    # Método para alimentar al animal
    def alimentar_animal(self):
        print(self.nombre + " fue alimentado.") # Mensaje indicando que animal fué alimentado

    # Método para hacer sonidos
    def hacer_sonido_animal(self):  # Mensaje indicando el sonido que hace cada animal que esté incluido
        if self.tipo == "perro":
            print("¡Guau!")
        elif self.tipo == "gato":
            print("¡Miau!")
        elif self.tipo == "oveja":
            print("¡Beee!")
        else:
            print("No está en la lista.")


# b) ¿Cómo se pueden crear diferentes objetos para representar diferentes animales?

perro = Animal("Chimuelo", 2, "perro")
gato = Animal("Tarzán", 3, "gato")
oveja = Animal("Dolly", 1, "oveja")


#Interacturar
perro.alimentar_animal()
perro.hacer_sonido()

gato.alimentar_animal()
gato.hacer_sonido()

oveja.alimentar_animal()
oveja.hacer_sonido()
