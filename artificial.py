
from characters import Personaje
from enums import Laboratorio, TypeArticial

class Artificiales(Personaje):
    
    __TypeArtificial: TypeArticial
    __LAB: Laboratorio
    def __init__(self, name, life, energy, strong, velocity, armor, estado, Range, Laboratorio, enemigo=None, liga=None):
        super().__init__( name, life, energy, strong, velocity, armor, estado, enemigo, liga)
      
        self.__TypeArtificial = Range
        self.__LAB = Laboratorio

    def getRange(self):
        return self.__TypeArtificial
    def getLaboratorio(self):
        return self.__LAB

    