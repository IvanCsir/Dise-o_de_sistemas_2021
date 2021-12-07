from abc import ABC, ABCMeta, abstractmethod

class Pantalla(metaclass=ABCMeta):
    @abstractmethod
    def funcion_pantalla(self):
        pass