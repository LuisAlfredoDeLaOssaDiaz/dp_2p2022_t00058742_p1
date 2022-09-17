from characterization  import Caracterizacion
from enums import Elemento
#Clase de debilidades con su constructor y metodos
class Debilidades(Caracterizacion):
    __efecto: float
    __elemento: Elemento
    def __init__(self, name, elemento,efecto):
        super().__init__(name)
        self.__efecto = efecto
        self.__elemento = elemento
    
    def getEfecto(self):
        return self.__efecto
    def getElemento(self):
        return self.__elemento.name
    