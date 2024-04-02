# Clase Libro: Representa un libro con atributos como título, autor y estado de préstamo.
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestamo = False

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_prestamo(self):
        return self.prestamo

    def prestar_libro(self):
        self.prestamo = True
        print(f"El libro '{self.titulo}' ha sido prestado.")

    def devolver_libro(self):
        self.prestamo = False
        print(f"El libro '{self.titulo}' ha sido devuelto.")

# Clase Biblioteca: Representa una biblioteca con un método para prestar libros.
class Biblioteca:
    def prestar_libro(self, libro):
        libro.prestar_libro()

# a) ¿Cómo se crea una clase de biblioteca?
# Se crea una clase llamada Biblioteca con la palabra clave class seguida del nombre de la clase.
# Por ejemplo:
# class Biblioteca:

# b) ¿Cómo se crea una clase de libro?
# Se crea una clase llamada Libro con la palabra clave class seguida del nombre de la clase.
# Por ejemplo:
# class Libro:

# c) ¿Cómo se utiliza un objeto de la clase de libro como parámetro en el método de la clase de biblioteca?
# El objeto de la clase Libro se pasa como parámetro al llamar al método de la clase Biblioteca.
# Por ejemplo:
# biblioteca = Biblioteca()
# libro = Libro("Yo", "YOYO")
# biblioteca.prestar_libro(libro)

# d) ¿Cómo se establece un atributo en un objeto de la clase de libro?
# Para establecer un atributo en un objeto de la clase Libro, se accede al atributo y se le asigna un valor.
# Por ejemplo, para establecer el estado de préstamo de un libro:
# libro = Libro("La sombra del viento", "Carlos Ruiz Zafón")
# libro.prestamo = True

# Crear una instancia de la clase Biblioteca
biblioteca = Biblioteca()

# Crear una instancia de la clase Libro
libro = Libro("Yo", "YOYO")

# Llamar al método de prestar_libro en la instancia de Biblioteca y pasar el objeto Libro como parámetro
biblioteca.prestar_libro(libro)

# Imprimir el estado de préstamo del libro
print("Estado de préstamo del libro:", libro.get_prestamo())

# Llamar al método de devolver_libro en el objeto Libro
libro.devolver_libro()

# Imprimir el estado de préstamo del libro después de devolverlo
print("Estado de préstamo del libro después de devolverlo:", libro.get_prestamo())
