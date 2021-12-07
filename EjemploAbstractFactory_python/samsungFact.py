from factory import Fabrica
from pantalla_samsung import *
from bateria_samsung import *


class CelularSamsungFac(Fabrica):
    def crear_pantalla(self):
        return PantallaSamsung()

    def crear_bateria(self):
        return BateriaSamsung()