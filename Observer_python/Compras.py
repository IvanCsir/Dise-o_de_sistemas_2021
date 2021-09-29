from ILibroMalEstado import ILibroMalEstado

class Compras(ILibroMalEstado):

    def update(self, libro):
        if libro.estado.upper == "MALO":
            print("Compras: ")
        print("Se solicita nueva cotización para libro " , libro.titulo)