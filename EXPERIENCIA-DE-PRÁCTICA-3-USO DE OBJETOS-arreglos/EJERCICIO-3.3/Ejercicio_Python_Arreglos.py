# Clase Animal: Representa a un animal con atributos como nombre, edad y tipo, y métodos para interactuar con el animal.
class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def get_nombre(self):  
        return self.nombre

    def get_edad(self):  
        return self.edad

    def get_tipo(self):  
        return self.tipo

    def alimentar_animal(self):
        print(self.nombre + " fue alimentado.")

    def hacer_sonido(self):
        if self.tipo == "perro":
            print("¡Guau!")
        elif self.tipo == "gato":
            print("¡Miau!")
        elif self.tipo == "oveja":
            print("¡Beee!")
        else:
            print("No está en la lista.")

# Crear un arreglo de objetos
animales = []

# Crear objetos de la clase Animal
perro = Animal("Chimuelo", 2, "perro")
gato = Animal("Tarzán", 3, "gato")
oveja = Animal("Dolly", 1, "oveja")

# a) ¿Cómo se agrega un objeto a un arreglo?
# Para agregar un objeto a un arreglo, se utiliza el método append().
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
for animal in animales:
    print(animal.get_nombre(), animal.get_edad(), animal.get_tipo())
