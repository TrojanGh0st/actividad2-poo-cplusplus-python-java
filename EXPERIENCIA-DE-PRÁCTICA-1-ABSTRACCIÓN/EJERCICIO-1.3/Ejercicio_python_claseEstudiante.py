# Clase Estudiante: Representa a un estudiante con atributos como nombre, edad y grado, y métodos para interactuar con el estudiante.
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    # Métodos para acceder a los atributos
    def get_nombre(self):  # Nombre del estudiante
        return self.nombre

    def get_edad(self):  # Edad del estudiante
        return self.edad

    def get_grado(self):  # Grado del estudiante
        return self.grado

#a) ¿Qué métodos son necesarios para tomar exámenes y calificar a los estudiantes?

    # Método para tomar exámenes al estudiante
    def tomar_examen(self, curso):
        print(self.nombre + " dando examen " + curso)

    # Método para calificar al estudiante
    def calificar(self, curso, nota):
        print("Estudiante" + self.nombre + " en la curso de " + curso + " su nota es " + str(nota))


# b) ¿Cómo se pueden crear diferentes objetos para representar diferentes estudiantes?
estudiante1 = Estudiante("Juan", 15, "Noveno")
estudiante2 = Estudiante("Maria", 16, "Décimo")
estudiante3 = Estudiante("Pedro", 14, "Octavo")

# Interactuar con los estudiantes
estudiante1.tomar_examen("Matemáticas")
estudiante1.calificar("Matemáticas", 85)

estudiante2.tomar_examen("Ciencias")
estudiante2.calificar("Ciencias", 92)

estudiante3.tomar_examen("Historia")
estudiante3.calificar("Historia", 78)
