#Fábrica abstracta
from abc import ABC, ABCMeta, abstractmethod

class Fabrica(metaclass=ABCMeta):
    @abstractmethod
    def crear_pantalla(self):
        pass
    
    @abstractmethod
    def crear_bateria(self):
        pass
