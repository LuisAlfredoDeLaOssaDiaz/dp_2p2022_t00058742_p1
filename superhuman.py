from characters import Personaje
from enums import SuperHuman

class SuperHumanos(Personaje):
    superHuman: SuperHuman

    def __init__(self,  nombre, vida, estamina, fuerza, velocidad, armadura,mana, estado, clase, enemigo=None, liga=None):
        super().__init__(nombre, vida, estamina, fuerza, velocidad, armadura,mana, estado,  enemigo, liga)
        self.__superHuman = clase

    def getShClases(self):
        return self.__superHuman.name