# Importaciones 
from ast import List
from abc import  abstractmethod, ABC
from Debilidades import Debilidades
from Ficha import IFicha
from enums import Estado
from Caracterizacion  import Caracterizacion
from Personalida import Personalidad




class Personaje(IFicha, ABC):
    _name: str
    __life: float
    _energy: float
    _strong: float
    _velocity: float
    _armor: float
    __liga: str
    __enemigo: None
    __caracterizacion: List
    _estado: Estado

    #Realizamos un constructor donde se inicialice a los personajes con sus atributos.
    def __init__(self,  name, life, energy, strong, velocity, armor, estado, enemigo=None, liga=None):
        
        self._name = name
        self.__life = life
        self._energy = energy
        self._strong = strong
        self._velocity = velocity
        self._armor = armor 
        self.__enemigo = enemigo
        self.__liga = liga
        self._estado = estado
        
        
        
    def anhadir(self, caracterizacion: Caracterizacion):
        self.__caracterizacion.append(caracterizacion)
    
    def getEnemigo(self):
        return self.__enemigo
    def Enemigo(self, personaje):
        self.__enemigo = personaje

    def Liga(self, liga):
        self.__liga = liga
    def getLiga(self):
        return self.__liga

    def getdanio(self, danio):
        #El personaje recibe danio en battalla
        
        self.__life -= danio
        
    def setEstado(self): #Se verifica y setea el estado
        if self.__life <= 0:
            self.__life = 0
            self._estado = Estado.MUERTO
        else: 
            self._estado = Estado.VIVO

    def getlife(self):
        return self.__life
    
        
    def attack(self, personaje):
        if personaje.__estado.name == "VIVO":
            personaje.getdanio(self._strong)
            print("Ataque basico ha sido exitoso")
        else: 
            print("Personaje no esta vivo. . . .")




    def anhadir_test(self, existencia: Caracterizacion):
        for i in self.__caracterizacion:
            if i == existencia:
                return True
            else:
                return False


    def especialAttack(self, personaje, especialAttack):
        if personaje.__estado.name == "VIVO":

            for i in super().__caracterizacion:
                if i.getName() == especialAttack:
                    if isinstance(i) or isinstance(i, Debilidades):
                        print("Don't attack")
                    else:
                        personaje.getdanio(i.getDamage())
                        print("Great Attack")
        else: 
            print("this character is dead")
   
   