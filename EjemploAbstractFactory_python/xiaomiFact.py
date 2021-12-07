from factory import Fabrica
from pantalla_samsung import PantallaSamsung
from pantalla_xiaomi import *
from bateria_xiaomi import *


class CelularXiaomiFac(Fabrica):
    def crear_pantalla(self):
        return PantallaXiaomi()

    def crear_bateria(self):
        return BateriaXiaomi()