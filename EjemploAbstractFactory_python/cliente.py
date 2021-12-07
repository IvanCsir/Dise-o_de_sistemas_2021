from samsungFact import *
from xiaomiFact import *

class Cliente():
    def accion_cliente(self, factory):
        pantalla = factory.crear_pantalla()
        bateria = factory.crear_bateria()

        print(pantalla.funcion_pantalla())
        print(bateria.funcion_bateria())


if __name__ == "__main__":
    c = Cliente()
    print("Fábrica Samsung: ")
    c.accion_cliente(CelularSamsungFac())
    print("Fábrica Xiaomi: ")
    c.accion_cliente(CelularXiaomiFac())

