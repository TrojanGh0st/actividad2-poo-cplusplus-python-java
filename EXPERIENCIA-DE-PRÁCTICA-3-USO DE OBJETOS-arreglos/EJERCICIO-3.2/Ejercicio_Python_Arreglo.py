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

# a) ¿Cómo se crean arreglos de objetos?
# Para crear un arreglo de objetos en Python, se pueden utilizar listas.
# Por ejemplo:
animales = []

# b) ¿Cómo se agregan objetos a un arreglo?
# Para agregar objetos a un arreglo, se utiliza el método append() de la lista.
# Por ejemplo:
animales.append(Animal("Chimuelo", 2, "perro"))

# c) ¿Cómo se recorren los objetos en un arreglo?
# Se puede recorrer los objetos en un arreglo utilizando un bucle for.
# Por ejemplo:
for animal in animales:
    print(animal.get_nombre(), animal.get_edad(), animal.get_tipo())
