#include <iostream>
#include <string>

using namespace std;

// clase Persona
class Persona {
private:
    string nombre;
    int edad;
    string genero;

public:
    // valores de los atributos
    void setNombre(string _nombre) // nombre de la persona
    {
        nombre = _nombre;
    }

    void setEdad(int _edad) // edad de la persona
    {
        edad = _edad;
    }

    void setGenero(string _genero) // género de la persona
    {
        genero = _genero;
    }

    // obtener los valores de los atributos
    string getNombre() const // obtener el nombre de la persona
    {
        return nombre;
    }

    int getEdad() const 
    { // obtener la edad de la persona
        return edad;
    }

    string getGenero() const 
    { // Mobtener el género de la persona
        return genero;
    }

    // acciones con la persona
    void celebrarCumpleaños() 
    { 
        cout << nombre << " esta celebrando su cumpleanios" << endl;
    }

    void presentarse() 
    { 
        cout << "Hola soy " << nombre << " tengo " << edad << " anios y soy " << genero << endl;
    }
};

int main() {
    // Creación de instancias de la clase Persona
    Persona persona1; // Instancia de una persona
    persona1.setNombre("Nylder"); // Establecer el nombre
    persona1.setEdad(30); // Establecer la edad
    persona1.setGenero("Masculino"); // Establecer el género

    Persona persona2; // Instancia de otra persona
    persona2.setNombre("Abby"); // Establecer el nombre 
    persona2.setEdad(25); // Establecer la edad 
    persona2.setGenero("Femenino"); // Establecer el género

    // Mostrar información sobre las personas
    cout <<"\tPersona 1:" <<endl; // información sobre la persona 1
    cout << "Nombre---> " << persona1.getNombre() << "\nEdad--->" << persona1.getEdad() << "\nGenero--->" << persona1.getGenero() << endl;
    persona1.celebrarCumpleaños(); // Celebrar el cumpleaños de la persona 1
    persona1.presentarse(); // Presentar a la persona 1

    cout <<"\tPersona 2:" <<endl; // información sobre la persona 2
    cout << "Nombre---> " << persona2.getNombre() << "\nEdad--->" << persona2.getEdad() << "\nGenero--->" << persona2.getGenero() << endl;
    persona2.celebrarCumpleaños(); // Celebrar el cumpleaños de la persona 2
    persona2.presentarse(); // Presentar a la persona 2

    return 0;
}
