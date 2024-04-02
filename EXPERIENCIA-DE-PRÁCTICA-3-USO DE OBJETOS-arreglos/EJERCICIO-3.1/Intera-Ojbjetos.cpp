#include <iostream>
#include <string>

using namespace std;

// Definición de la clase Animal
class Animal {
private:
    string nombre;
    int edad;
    string tipo;

public:
    //  nombre del animal
    void setNombre(string _nombre) {
        nombre = _nombre;
    }

    // edad del animal
    void setEdad(int _edad) {
        edad = _edad;
    }

    //tipo del animal
    void setTipo(string _tipo) {
        tipo = _tipo;
    }

    // obtener los valores de los atributos

    // obtener el nombre del animal
    string getNombre() const {
        return nombre;
    }

    // obtener la edad del animal
    int getEdad() const {
        return edad;
    }

    // obtener el tipo del animal
    string getTipo() const {
        return tipo;
    }
};

int main() {
    Animal perro, gato;

    perro.setNombre("Platano"); // nombre del perro
    perro.setEdad(5); // edad del perro
    perro.setTipo("Perro"); // tipo del perro

    gato.setNombre("Tiburon"); // nombre del gato
    gato.setEdad(3); // edad del gato
    gato.setTipo("Gato"); // tipo del gato


    cout <<"\tMASCOTA 1:" <<endl; // información sobre el perro
    cout << "Nombre---> " << perro.getNombre() << "\nEdad ---> " << perro.getEdad() << "\nTipo---> " << perro.getTipo() << endl;

    cout <<"\tMASCOTA 2:" <<endl; // información sobre el gato
    cout << "Nombre---> " << gato.getNombre() << "\nEdad ---> " << gato.getEdad() << "\nTipo---> " << gato.getTipo() << endl;

    return 0;
}
