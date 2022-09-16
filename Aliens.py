from Personajes import Personaje
from Fichai import IFicha
from enums import TypeAlienigena

class Aliens(Personaje):
    __TypeAlienigena: TypeAlienigena

    def __init__(self,  name, life, energy, strong, velocity, armor, estado, TypeAlien, caracterizacion=[], enemigo=None, liga=None):
        
        super().__init__(name, life, energy, strong, velocity, armor, estado,caracterizacion, enemigo, liga)
        
        self.__RazaAlienigena = TypeAlien

    def getTypeAlien(self):
        return self.__RazTypeenigena.name
    