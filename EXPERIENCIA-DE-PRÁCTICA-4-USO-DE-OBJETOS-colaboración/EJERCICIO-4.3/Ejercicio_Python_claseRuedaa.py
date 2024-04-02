# Clase Rueda: Representa una rueda con un atributo para el tamaño.
class Rueda:
    def __init__(self, tamaño):
        self.tamaño = tamaño

# Clase Carro: Representa un carro con cuatro objetos de la clase Rueda como atributos.
class Carro:
    def __init__(self, rueda_delantera_izquierda, rueda_delantera_derecha, rueda_trasera_izquierda, rueda_trasera_derecha):
        self.rueda_delantera_izquierda = rueda_delantera_izquierda
        self.rueda_delantera_derecha = rueda_delantera_derecha
        self.rueda_trasera_izquierda = rueda_trasera_izquierda
        self.rueda_trasera_derecha = rueda_trasera_derecha

    def mover_carro(self):
        print("El carro se está moviendo.")

    def cambiar_ruedas(self, rueda_delantera_izquierda, rueda_delantera_derecha, rueda_trasera_izquierda, rueda_trasera_derecha):
        self.rueda_delantera_izquierda = rueda_delantera_izquierda
        self.rueda_delantera_derecha = rueda_delantera_derecha
        self.rueda_trasera_izquierda = rueda_trasera_izquierda
        self.rueda_trasera_derecha = rueda_trasera_derecha

# a) ¿Cómo se crea una clase de carro?
# Se crea una clase llamada Carro con la palabra clave class seguida del nombre de la clase.
# Por ejemplo:
# class Carro:

# b) ¿Cómo se crea una clase de rueda?
# Se crea una clase llamada Rueda con la palabra clave class seguida del nombre de la clase.
# Por ejemplo:
# class Rueda:

# c) ¿Cómo se utilizan objetos de la clase de rueda como atributos de la clase de carro?
# Se pasan objetos de la clase Rueda como parámetros al crear un objeto de la clase Carro.
# Por ejemplo:
# rueda_delantera_izquierda = Rueda(18)
# rueda_delantera_derecha = Rueda(18)
# rueda_trasera_izquierda = Rueda(18)
# rueda_trasera_derecha = Rueda(18)
# carro = Carro(rueda_delantera_izquierda, rueda_delantera_derecha, rueda_trasera_izquierda, rueda_trasera_derecha)

# d) ¿Cómo se cambian los atributos de los objetos de la clase de rueda?
# Se accede a los atributos de los objetos de la clase Rueda y se les asigna un nuevo valor.
# Por ejemplo, para cambiar el tamaño de una rueda:
# rueda_delantera_izquierda.tamaño = 20
