from abc import ABC, ABCMeta, abstractmethod

class Bateria(metaclass=ABCMeta):
    @abstractmethod
    def funcion_bateria(self):
        pass