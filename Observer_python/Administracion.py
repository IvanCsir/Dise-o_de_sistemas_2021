from ILibroMalEstado import ILibroMalEstado

class Administracion(ILibroMalEstado):
    def update(self, libro):
        if libro.estado.upper() == "MALO":
            print("Envió una queja formal por libro " , libro.titulo, " por devolución en mal estado.")
        print("Devolución de " , libro.titulo, " en buen estado.")