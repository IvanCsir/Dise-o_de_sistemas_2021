#Fábrica abstracta
from abc import ABC, abstractmethod

class Fabrica():
    @abstractmethod
    def crear_pantalla(self):
        pass
    
    @abstractmethod
    def crear_bateria(self):
        pass
