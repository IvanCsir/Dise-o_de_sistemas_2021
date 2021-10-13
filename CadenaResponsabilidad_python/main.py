from banco import *
from ejecutivoCuenta import *
from liderTeamEjecutivo import *
from gerente import *
from director import *

if __name__=="__main__":

    banco = Banco()

    monto = 10000

    banco.ejecutivoCuenta.solicitudPrestamo(monto)

