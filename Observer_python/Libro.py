class Libro:

    def __init__(self, titulo, estado):
        self.titulo = titulo
        self.estado = estado

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value