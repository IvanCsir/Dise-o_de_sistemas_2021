from celular_samsungFact import *
from celular_xiaomiFact import *

class Cliente():
    def accion_cliente(self, factory):
        pantalla = factory.crear_pantalla()
        bateria = factory.crear_bateria()

        print(pantalla.funcion_pantalla())
        print(bateria.funcion_bateria())