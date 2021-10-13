from ejecutivoCuenta import *
from liderTeamEjecutivo import *
from gerente import *
from director import *

class Banco():

    def __init__(self):
        self.ejecutivoCuenta = EjecutivoCuenta()
        self.liderTeamEjecutivo = LiderEjecutivo()
        self.gerente = Gerente()
        self.director = Director()

        self.ejecutivoCuenta.set_next(self.liderTeamEjecutivo)
        self.liderTeamEjecutivo.set_next(self.gerente)
        self.gerente.set_next(self.director)