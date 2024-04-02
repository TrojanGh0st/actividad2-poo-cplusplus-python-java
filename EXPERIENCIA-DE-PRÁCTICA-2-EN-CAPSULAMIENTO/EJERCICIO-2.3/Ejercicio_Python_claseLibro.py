# Clase Libro: Representa un libro con atributos como título, autor y género, y métodos get y set para cada atributo.
class Libro:
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

# a) Beneficios del uso de métodos get y set en la clase de libro:

# - Encapsulamiento: Al utilizar los métodos get y set en la clase de libro, se puede controlar el acceso a los atributos como título, autor y género. Esto ayuda a mejorar la seguridad y privacidad de la información del libro, ya que evita que los atributos sean modificados directamente desde fuera de la clase sin la validación adecuada.
# - Validación de datos: Los métodos set pueden incluir lógica para validar los datos antes de establecer un nuevo valor para el título, autor o género. Por ejemplo, se puede verificar si el título no está vacío o si el autor es una cadena válida. Esto ayuda a garantizar la integridad de los datos y prevenir errores en la manipulación del libro.

    # Métodos get para cada atributo
    def get_titulo(self):  # Obtener título
        return self._titulo

    def get_autor(self):  # Obtener autor
        return self._autor

    def get_genero(self):  # Obtener género
        return self._genero

    # Métodos set para cada atributo
    def set_titulo(self, titulo):  # Establecer título
        self._titulo = titulo

    def set_autor(self, autor):  # Establecer autor
        self._autor = autor

    def set_genero(self, genero):  # Establecer género
        self._genero = genero

# b) Cómo se pueden utilizar los métodos get y set para actualizar y recuperar información sobre diferentes libros:

# Objetos
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula")
libro2 = Libro("1984", "George Orwell", "Ciencia ficción")

# GET Y SET
# Actualizar información utilizando métodos set
libro1.set_autor("Antoine Saint-Exupéry")
libro2.set_genero("Distopía")

# Recuperar información utilizando métodos get
print(libro1.get_titulo(), libro1.get_autor(), libro1.get_genero())
print(libro2.get_titulo(), libro2.get_autor(), libro2.get_genero())
