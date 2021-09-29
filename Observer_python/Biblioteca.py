from Administracion import Administracion
from Compras import Compras
from Stock import Stock
from AlarmaLibro import AlarmaLibro

class Biblioteca:
    
    @staticmethod
    def devuelve_libro(libro):
        print("Informe devolución de libro " , libro.titulo, ".")
        attach_array = [Administracion(), Compras(), Stock()]
        AlarmaLibro.multi_attach(attach_array)
        AlarmaLibro.notify_observers(libro)