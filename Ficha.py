from abc import ABC, abstractmethod
from Caracterizacion import Caracterizacion



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
    
