from ast import List
from abc import  abstractmethod, ABC
from weakness import Debilidades
from Ificha import IFicha
from enums import Estado
from characterization  import Caracterizacion
from personality import Personalidad

class Personaje(IFicha, ABC):
    _name: str
    __life: float
    _energy: float
    _hidden_power: float
    __strong: float
    _velocity: float
    _armor: float
    __liga: str
    __enemigo: None
    __caracterizacion: List
    _estado: Estado

    def __init__(self,  name, life, energy, strong, velocity, armor,hidden_power, estado, caracterizacion=[], enemigo=None, liga=None):
       
        self._name = name
        self.__life = life
        self._hidden_power = hidden_power
        self._energy = energy
        self.__strong = strong
        self._velocity = velocity
        self._armor = armor
        self.__enemigo = enemigo
        self.__liga = liga
        self._estado = estado
        self.__caracterizacion = caracterizacion

    
    def Add(self, caracterizacion: Caracterizacion):
        self.__caracterizacion.append(caracterizacion)
    
    def getEnemigo(self):
        return self.__enemigo
    def Enemigo(self, personaje):
        self.__enemigo = personaje

    def Liga(self, liga):
        self.__liga = liga
    def getLiga(self):
        return self.__liga

    def recibirDaño(self, danio):
        """RECIBIR DAÑO """
        self.__life -= danio
        
    def setEstado(self):
        if self.__life <= 0:
            self.__life = 0
            self._estado = Estado.MUERTO
        else: 
            self._estado = Estado.VIVO

    def getlife(self):
        return self.__life
    
        
    def atacar(self, personaje):
        if personaje._estado.name == "VIVO":
            personaje.recibirDaño(self.__strong)
            print("Ataque basico ha sido exitoso")
        else: 
            print("Personaje no esta vivo. . . .")

    def ataqueEspecial(self, personaje, ataqueEspecial):
        if personaje._estado.name == "VIVO":

            for i in super().__caracterizacion:
                if i.getName() == ataqueEspecial:
                    if isinstance(i, Personalidad) or isinstance(i, Debilidades):
                        print("no se puede atacar con una Personalidad")
                    else:
                        personaje.recibirDaño(i.getDamage())
                        print("Has atacado con exito. . .")
        else: 
            print("Personaje muerto")


    def add_test(self, existencia: Caracterizacion):
        for i in self.__caracterizacion:
            if i == existencia:
                return True
            else:
                return False