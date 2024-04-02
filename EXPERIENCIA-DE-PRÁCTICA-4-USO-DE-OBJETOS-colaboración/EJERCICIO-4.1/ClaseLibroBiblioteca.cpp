#include <iostream>
#include <string>

using namespace std;

class Libro {
private:
    string titulo;
    string autor;
    bool prestado; // indica si el libro está prestado o no

public:
    // título del libro
    void setTitulo(string _titulo) {
        titulo = _titulo;
    }

    // autor del libro
    void setAutor(string _autor) {
        autor = _autor;
    }

    // Saber si el libro esta prestado
    void prestar() {
        prestado = true;
    }

    // saber si el libro  no esta prestado
    void devolver() {
        prestado = false;
    }


    // obtener el título del libro
    string getTitulo() const {
        return titulo;
    }

    // obtener el autor del libro
    string getAutor() const {
        return autor;
    }

    // verificar si el libro está prestado
    bool estaPrestado() const {
        return prestado;
    }
};

class Biblioteca {
public:
    // prestar un libro de la biblioteca
    void prestarLibro(Libro &libro) {
        if (!libro.estaPrestado()) {
            libro.prestar();
            cout << "El libro \"" << libro.getTitulo() << "\" ha sido prestado." << endl;
        } else {
            cout << "El libro \"" << libro.getTitulo() << "\" ya esta prestado." << endl;
        }
    }

    // devolver un libro a la biblioteca
    void devolverLibro(Libro &libro) {
        if (libro.estaPrestado()) {
            libro.devolver();
            cout << "El libro \"" << libro.getTitulo() << "\" ha sido devuelto." << endl;
        } else {
            cout << "El libro \"" << libro.getTitulo() << "\" no estaba prestado." << endl;
        }
    }
};

int main() {
    Libro libro1, libro2;

    // atributos para el libro 1
    libro1.setTitulo("El Banquete");
    libro1.setAutor("Platon");

    // atributos para el libro 2
    libro2.setTitulo("etica a Nicomaco");
    libro2.setAutor("Aristoteles");

    // objeto de la clase Biblioteca
    Biblioteca biblioteca;

    // Prestar un libro de la biblioteca
    biblioteca.prestarLibro(libro1);
    biblioteca.prestarLibro(libro2);

    // Devolver un libro a la biblioteca
    biblioteca.devolverLibro(libro1);
    biblioteca.devolverLibro(libro2);

    return 0;
}
