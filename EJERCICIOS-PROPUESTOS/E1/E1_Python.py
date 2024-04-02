# Clase Auto: Representa un auto con atributos como la velocidad y el nombre del conductor.
class Auto:
    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento  # Aumentar la velocidad

# Clase Carrera: Representa una carrera con atributos como la distancia total y la dificultad del oponente.
class Carrera:
    def __init__(self, distancia_total, dificultad_oponente):
        self.distancia_total = distancia_total
        self.dificultad_oponente = dificultad_oponente

    def simular_carrera(self, jugador, computadora, incremento_velocidad):
        while jugador.velocidad < self.distancia_total and computadora.velocidad < self.distancia_total:
            jugador.acelerar(incremento_velocidad)
            computadora.acelerar(incremento_velocidad)

        if jugador.velocidad >= self.distancia_total and computadora.velocidad >= self.distancia_total:
            print("¡Es un empate!")
        elif jugador.velocidad >= self.distancia_total:
            print(f"¡{jugador.nombre} ha ganado la carrera!")
        else:
            print("¡La computadora ha ganado la carrera!")


# Ejemplo de uso:
jugador = Auto("Jugador", 0)
computadora = Auto("Computadora", 0)

carrera = Carrera(100, "Difícil")

incremento_velocidad = 5  # Se incrementa la velocidad en 5 en cada paso

carrera.simular_carrera(jugador, computadora, incremento_velocidad)
