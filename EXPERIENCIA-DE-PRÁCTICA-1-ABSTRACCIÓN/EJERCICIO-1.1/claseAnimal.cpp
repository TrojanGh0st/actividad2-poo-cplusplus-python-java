#include <iostream>
#include <string>

using namespace std;

// Definición de clase Animal
class Animal {
private:
    string nombre;
    int edad;
    string tipo;

public:
    // Métodos para establecer los valores de los atributos
    void setNombre(string _nombre) // Método para  el nombre del animal
    {
        nombre = _nombre;
    }

    void setEdad(int _edad) // Método para la edad del animal
    {
        edad = _edad;
    }

    void setTipo(string _tipo) // Método para el tipo del animal
    {
        tipo = _tipo;
    }

    // Métodos para obtener los valores de los atributos
    string getNombre() const // obtener el nombre del animal
    {
        return nombre;
    }

    int getEdad() const { // obtener la edad del animal
        return edad;
    }

    string getTipo() const { // obtener el tipo del animal
        return tipo;
    }

    // Métodos para realizar acciones con el animal
    void alimentar() { // alimentar al animal
        cout << nombre << " está siendo alimentado" << endl;
    }

    void hacerSonido() { // animal haga un sonido
        cout << nombre << " está haciendo sonido" << endl;
    }
};

int main() {
    Animal perro; // Instancia de un perro
    perro.setNombre("Platano"); // Establecer el nombre del perro
    perro.setEdad(5); // Establecer la edad del perro
    perro.setTipo("Perro"); // Establecer el tipo del perro

    Animal gato; // Instancia de un gato
    gato.setNombre("Tiburon"); // Establecer el nombre del gato
    gato.setEdad(3); // Establecer la edad del gato
    gato.setTipo("Gato"); // Establecer el tipo del gato

    // Mostrar información
    cout <<"\nMASCOTA 1:" <<endl; // Imprimir información sobre la mascota 1
    cout << "Nombre---> " << perro.getNombre() << "\nEdad ---> " << perro.getEdad() << "\nTipo---> " << perro.getTipo() << endl; // Imprimir nombre, edad y tipo del perro
    perro.alimentar(); // Alimentar al perro
    perro.hacerSonido(); // Hacer que el perro haga un sonido

    cout <<"\nMASCOTA 2:" <<endl; // Imprimir información sobre la mascota 2
    cout << "Nombre---> " << gato.getNombre() << "\nEdad ---> " << gato.getEdad() << "\nTip
