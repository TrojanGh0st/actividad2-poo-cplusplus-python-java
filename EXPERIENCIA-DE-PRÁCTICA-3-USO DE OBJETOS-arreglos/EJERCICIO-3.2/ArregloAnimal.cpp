#include <iostream>
#include <string>

using namespace std;

class Animal {
private:
    string nombre;
    int edad;
    string tipo;

public:
    void setNombre(string _nombre) // establecer el nombre del animal
    {
        nombre = _nombre;
    }

    void setEdad(int _edad) // establecer la edad del animal
    {
        edad = _edad;
    }

    void setTipo(string _tipo) // establecer el tipo del animal
    {
        tipo = _tipo;
    }

    string getNombre() const // obtener el nombre del animal
    {
        return nombre;
    }

    int getEdad() const // obtener la edad del animal
    {
        return edad;
    }

    string getTipo() const // obtener el tipo del animal
    {
        return tipo;
    }
};

int main() {
    const int TAM = 3; // Tamaño del arreglo
    Animal animales[TAM]; // arreglo de objetos de la clase Animal

    animales[0].setNombre("Platano");
    animales[0].setEdad(7);
    animales[0].setTipo("Perro");

    animales[1].setNombre("Peruanoxd");
    animales[1].setEdad(1);
    animales[1].setTipo("Gato");

    animales[2].setNombre("Cuy");
    animales[2].setEdad(3);
    animales[2].setTipo("Hamster");

    // ciclo para recorrer y manipular los objetos en el arreglo
    cout << "Información de los animales en el arreglo:" << endl;
    for (int i = 0; i < TAM; ++i) {
        cout << "\tAnimal " << i + 1 << endl;
        cout << "Nombre---> " << animales[i].getNombre() << "\nEdad---> " << animales[i].getEdad() << "\nTipo---> " << animales[i].getTipo() << endl;
    }

    return 0;
}
