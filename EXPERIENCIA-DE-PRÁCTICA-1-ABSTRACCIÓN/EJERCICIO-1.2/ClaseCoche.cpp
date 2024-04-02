#include <iostream>
#include <string>

using namespace std;

// clase Coche
class Coche {
private:
    string modelo;
    int año;
    double velocidad;

public:
    // valores de los atributos
    void setModelo(string _modelo) // modelo del coche
    {
        modelo = _modelo;
    }

    void setAño(int _año) // año del coche
    {
        año = _año;
    }

    void setVelocidad(double _velocidad) // la velocidad del coche
    {
        velocidad = _velocidad;
    }

    // obtener los valores de los atributos
    string getModelo() const // modelo del coche
    {
        return modelo;
    }

    int getAño() const { // año del coche
        return año;
    }

    double getVelocidad() const { // velocidad del coche
        return velocidad;
    }

    // acciones con el coche
    void acelerar(double aumento) { // la velocidad del coche
        velocidad += aumento;
        cout << "El coche esta acelerando---> Velocidad actual---> " << velocidad << " km/h" << endl;
    }

    void frenar(double reduccion) { // reducir la velocidad del coche
        if (velocidad >= reduccion) {
            velocidad -= reduccion;
            cout << "El coche esta frenando---> Velocidad actual---> " << velocidad << " km/h" << endl;
        } else {
            cout << "El coche ya está detenido." << endl;
        }
    }
};

int main() {

    Coche coche1; // Instancia de un coche
    coche1.setModelo("Toyota Corolla"); //  modelo del coche
    coche1.setAño(2022); // año del coche
    coche1.setVelocidad(60); // velocidad inicial del coche

    Coche coche2; // Instancia de otro coche
    coche2.setModelo("Honda Civic"); // modelo del otro coche
    coche2.setAño(2020); // año del otro coche
    coche2.setVelocidad(52); // velocidad inicial del otro coche

    // Mostrar información y realizar acciones sobre los coches
    cout <<"\nCoche 1:" <<endl; // información sobre el coche 1
    cout << "Modelo ---> " << coche1.getModelo() << "\nAnio ---> " << coche1.getAño() << "\nVelocidad ---> " << coche1.getVelocidad() << " km/h" << endl; // Imprimir modelo, año y velocidad del coche 1
    coche1.acelerar(50); // Acelerar el coche 1
    coche1.frenar(20); // Frenar el coche 1

    cout <<"\nCoche 2:" <<endl; // información sobre el coche 2
    cout << "Modelo ---> " << coche2.getModelo() << "\nAnio ---> " << coche2.getAño() << "\nVelocidad ---> " << coche2.getVelocidad() << " km/h" << endl; // Imprimir modelo, año y velocidad del coche 2
    coche2.acelerar(70); // Acelerar el coche 2
    coche2.frenar(80); // Frenar el coche 2

    return 0;
}
