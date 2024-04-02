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


# Crear objetos de la clase Animal
perro = Animal("Chimuelo", 2, "perro")
gato = Animal("Tarzán", 3, "gato")
oveja = Animal("Dolly", 1, "oveja")

# Interactuar con los animales
perro.alimentar_animal()
perro.hacer_sonido()

gato.alimentar_animal()
gato.hacer_sonido()

oveja.alimentar_animal()
oveja.hacer_sonido()

# a) ¿Cómo se agregan objetos a un arreglo?
# Para agregar un objeto a un arreglo, se utiliza el método append().
animales = []
animales.append(perro)
animales.append(gato)
animales.append(oveja)

# b) ¿Cómo se elimina un objeto de un arreglo?
# Para eliminar un objeto de un arreglo, se utiliza la palabra clave del con el índice del objeto que se desea eliminar.
# Por ejemplo, para eliminar el primer objeto en el arreglo:
del animales[0]

# c) ¿Cómo se modifica un objeto en un arreglo?
# Para modificar un objeto en un arreglo, se accede al objeto a través de su índice y se actualizan sus atributos.
# Por ejemplo, para modificar la edad del segundo objeto en el arreglo:
animales[1].edad = 4

# Mostrar información de los animales en el arreglo después de las operaciones
print("\nDespués de las operaciones:")
for animal in animales:
    print(animal.get_nombre(), animal.get_edad(), animal.get_tipo())

# Crear un nuevo animal para comparar
perro_nuevo = Animal("Chimuelo", 2, "perro")

# Comprobar si el animal está en el arreglo
print("\nComprobación de animal en el arreglo:")
for animal in animales:
    if animal == perro_nuevo:
        print("¡El animal está en el arreglo!")
        break
else:
    print("El animal no está en el arreglo.")
