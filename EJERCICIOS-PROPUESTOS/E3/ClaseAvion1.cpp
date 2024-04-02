#include <iostream>
#include <string>

using namespace std;

// Definición de la clase Avión
class Avion {
private:
    string destino;
    int duracionMision; // Duración de la misión en horas
    int tripulacionNecesaria; // Número de tripulantes necesarios
    int combustible; // Cantidad de combustible en litros

public:
    // Constructor
    Avion(string _destino = "", int _duracion = 0, int _tripulacion = 0, int _combustible = 0) : destino(_destino), duracionMision(_duracion), tripulacionNecesaria(_tripulacion), combustible(_combustible) {}

    // Método para comprobar si el avión tiene suficiente combustible para completar la misión
    bool verificarCombustible() const {
        int consumoPorHora = 20; // Supongamos que el avión consume 20 litros de combustible por hora de vuelo
        int consumoTotal = consumoPorHora * duracionMision;
        return combustible >= consumoTotal;
    }
};

// Definición de la clase Misión
class Mision {
private:
    Avion avion;

public:
    // Constructor
    Mision(const Avion& _avion) : avion(_avion) {}

    // Método para simular la misión
    void simularMision() {
        if (avion.verificarCombustible()) {
            cout << "La misión hacia " << avion.destino << " se ha completado con éxito." << endl;
        } else {
            cout << "El avión no tiene suficiente combustible para completar la misión hacia " << avion.destino << "." << endl;
        }
    }
};

int main() {
    // Crear un avión para la misión
    Avion avion("Nueva York", 6, 2, 120); // Destino: Nueva York, Duración de la misión: 6 horas, Tripulación necesaria: 2, Combustible: 120 litros

    // Crear una misión con el avión
    Mision mision(avion);

    // Simular la misión
    mision.simularMision();

    return 0;
}
