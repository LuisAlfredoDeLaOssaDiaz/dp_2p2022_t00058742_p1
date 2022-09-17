from abc import ABC, abstractmethod
from characterization import Caracterizacion



class IFicha(ABC):

    @abstractmethod
    def Add(self, caracterizacion: Caracterizacion):
    
        pass
    @abstractmethod
    def Liga(self, liga):
     
        pass
    @abstractmethod
    def Enemigo(self, enemigo):
   
        pass
    
