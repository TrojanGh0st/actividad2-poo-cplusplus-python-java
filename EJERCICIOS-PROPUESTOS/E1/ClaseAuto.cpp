#include <iostream>
#include <string>

using namespace std;

// Definición de la clase Auto
class Auto {
private:
    string marca;
    int velocidadMaxima;

public:
    // Métodos para establecer los valores de los atributos
    void setMarca(string _marca) {
        marca = _marca;
    }

    void setVelocidadMaxima(int _velocidadMaxima) {
        velocidadMaxima = _velocidadMaxima;
    }

    // Métodos para obtener los valores de los atributos
    string getMarca() const {
        return marca;
    }

    int getVelocidadMaxima() const {
        return velocidadMaxima;
    }

    // Método para simular la velocidad del auto en la carrera
    int correr() const {
        // Simulación de la velocidad como un número aleatorio entre 1 y la velocidad máxima del auto
        return rand() % velocidadMaxima + 1;
    }
};

// Definición de la clase Carrera
class Carrera {
private:
    int distanciaTotal;
    int dificultadComputadora;

public:
    // Métodos para establecer los valores de los atributos
    void setDistanciaTotal(int _distanciaTotal) {
        distanciaTotal = _distanciaTotal;
    }

    void setDificultadComputadora(int _dificultadComputadora) {
        dificultadComputadora = _dificultadComputadora;
    }

    // Método para simular la carrera entre un auto jugador y un auto de la computadora
    void simularCarrera(const Auto& jugador) const {
        Auto computadora;
        computadora.setVelocidadMaxima(dificultadComputadora);

        int distanciaJugador = 0;
        int distanciaComputadora = 0;

        while (distanciaJugador < distanciaTotal && distanciaComputadora < distanciaTotal) {
            int velocidadJugador = jugador.correr();
            int velocidadComputadora = computadora.correr();

            distanciaJugador += velocidadJugador;
            distanciaComputadora += velocidadComputadora;
        }

        if (distanciaJugador >= distanciaTotal && distanciaComputadora >= distanciaTotal) {
            cout << "¡Es un empate!" << endl;
        } else if (distanciaJugador >= distanciaTotal) {
            cout << "¡Has ganado la carrera!" << endl;
        } else {
            cout << "¡La computadora ha ganado la carrera!" << endl;
        }
    }
};

int main() {
    // Creación de objetos de la clase Auto
    Auto jugador;
    Auto computadora;

    // Establecimiento de atributos para el jugador
    jugador.setMarca("Jugador");
    jugador.setVelocidadMaxima(120);

    // Establecimiento de atributos para la computadora
    computadora.setMarca("Computadora");

    // Creación de objeto de la clase Carrera
    Carrera carrera;

    // Establecimiento de atributos para la carrera
    carrera.setDistanciaTotal(1000);
    carrera.setDificultadComputadora(100);

    // Simular la carrera
    carrera.simularCarrera(jugador);

    return 0;
}
