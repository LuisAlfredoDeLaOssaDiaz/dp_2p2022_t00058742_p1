from characters import Personaje
from Ificha import IFicha
from enums import TypeAlienigena

class Aliens(Personaje):
    __TypeAlienigena: TypeAlienigena

    def __init__(self,  name, life, energy, strong, velocity, armor, estado, TypeAlien, caracterizacion=[], enemigo=None, liga=None):
        
        super().__init__(name, life, energy, strong, velocity, armor, estado,caracterizacion, enemigo, liga)
        
        self.__TypeAlienigena = TypeAlien

    def getTypeAlien(self):
        return self.__TypeAlienigena.name
    