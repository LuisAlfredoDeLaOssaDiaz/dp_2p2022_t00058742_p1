from Caracterizacion  import Caracterizacion
#Clase de habilidades con su constructor y metodos
class Habilidades(Caracterizacion):
    __danio: float
    __costodedanio: float

    def __init__(self, name, damage, cost):
        super().__init__(name)
        self.__danio = damage
        self.__costodedanio = cost
    
    def getName(self):
        return self.__name
    
    def getCost(self):
        return self.__costodedanio
    
    def getDamage(self):
        return self.__danio
        