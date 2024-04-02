# Clase Avión: Representa un avión con atributos como el modelo y la cantidad de combustible.
class Avion:
    def __init__(self, modelo, combustible):
        self.modelo = modelo
        self.combustible = combustible

    def verificar_combustible_suficiente(self, duracion_mision, consumo_combustible):
        combustible_necesario = duracion_mision * consumo_combustible
        if self.combustible >= combustible_necesario:
            print("El avión tiene suficiente combustible para completar la misión.")
        else:
            print("El avión no tiene suficiente combustible para completar la misión.")

# Clase Misión: Representa una misión de vuelo con atributos como el destino, la duración y la tripulación necesaria.
class Mision:
    def __init__(self, destino, duracion, tripulacion):
        self.destino = destino
        self.duracion = duracion
        self.tripulacion = tripulacion

    def simular_mision(self, avion, consumo_combustible):
        avion.verificar_combustible_suficiente(self.duracion, consumo_combustible)

# Ejemplo de uso:
avion = Avion("Boeing 747", 10000)  # Crear un avión con 10000 litros de combustible
mision = Mision("Nueva York", 8, 3)  # Planificar una misión a Nueva York que dura 8 horas y requiere una tripulación de 3 personas

# Simular la misión y verificar si el avión tiene suficiente combustible
mision.simular_mision(avion, 1200)  # Suponiendo que el avión consume 1200 litros de combustible por hora
