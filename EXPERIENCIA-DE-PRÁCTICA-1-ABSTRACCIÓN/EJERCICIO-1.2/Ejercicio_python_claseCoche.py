# Clase Coche: Representa un coche con atributos como modelo, año y velocidad, y métodos para interactuar con el coche.
class Coche:
    def __init__(self, modelo, año, velocidad):
        self.modelo = modelo
        self.año = año
        self.velocidad = velocidad

    # Métodos para acceder a los atributos
    def get_modelo(self):  # Modelo del coche
        return self.modelo

    def get_año(self):  # Año del coche
        return self.año

    def get_velocidad(self):  # Velocidad actual del coche
        return self.velocidad

  
# a) ¿Qué métodos son necesarios para acelerar y frenar los coches?
  
    # Método para acelerar el coche
    def acelerar(self):
        self.velocidad += 1 # Aumenta la velocidad en 1 km/h
        print(self.modelo + "ha acelerado, Velocidad actual: " + self.velocidad +"km/h")

    # Método para frenar el coche
    def frenar(self):
        if self.velocidad >= 80:
            self.velocidad -= 10  # Disminuye la velocidad en 10 km/h
            print(self.modelo + "ha frenado. Nueva velocidad:" + self.velocidad +"km/h")
        else:
            print(self.modelo + "siga, tiene una velocidad adecuada. Velocidad actual: "  + self.velocidad + "km/h")

#b) ¿Cómo se pueden crear diferentes objetos para representar diferentes coches?
coche1 = Coche("Toyota Corolla", 2020, 60)
coche2 = Coche("Ford Mustang", 2018, 120)
coche3 = Coche("Tesla Model S", 2022, 100)


# Interactuar con los coches
coche1.acelerar()
coche1.frenar()

coche2.acelerar()
coche2.frenar()

coche3.acelerar()
coche3.frenar()
