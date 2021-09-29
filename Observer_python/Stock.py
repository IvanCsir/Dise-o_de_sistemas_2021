from ILibroMalEstado import ILibroMalEstado

class Stock(ILibroMalEstado):
    print("Stock: ")
    def update(self, libro):
        if libro.estado.upper == "MALO":
            print("Se da de baja el libro " , libro.titulo , " por su estado.")
        print("El libro " , libro.titulo , " vuelve a estar en stock.")