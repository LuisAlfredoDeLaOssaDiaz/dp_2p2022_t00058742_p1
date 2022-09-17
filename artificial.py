from characterization import Caracterizacion
from characters import Personaje
from enums import Laboratorio, TypeArticial

class Artificiales(Personaje):
    __RangoArtificial: TypeArticial
    __Laboratorio: Laboratorio
    def __init__(self,nombre, vida, estamina, fuerza, velocidad, armadura, RangoArtificial, Laboratorio, caracterizacion=[], enemigo=None, liga=None):
        super().__init__(nombre, vida, estamina, fuerza, velocidad, armadura, caracterizacion, enemigo, liga)
        "Inicializador de Persojane, nombre: str, vida: float, estamina: float, fuerza: float, velocidad: float, armadura: float, caracterizacion: list of objects, enemigo: Personaje[defaul->none] liga: str"
        self.__RangoArtificial = RangoArtificial
        self.__Laboratorio = Laboratorio

    def getRangoArtificial(self):
        return self.__RangoArtificial
    def getLaboratorio(self):
        return self.__Laboratorio
    