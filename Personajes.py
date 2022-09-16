# Importaciones 
from ast import List
from abc import  abstractmethod, ABC
from Debilidades import Debilidades
from Ficha import IFicha
from enums import Estado
from Caracterizacion  import Caracterizacion
from Personalida import Personalidad




class Personaje(IFicha, ABC):
    __namep: str
    __life: float
    __energy: float
    __strong: float
    __velocity: float
    __armor: float
    __liga: str
    __enemigo: None
    __caracterizacion: List
    __estado: Estado

    #Realizamos un constructor donde se inicialice a los personajes con sus atributos.
    def __init__(self,  name, life, energy, strong, velocity, armor, estado, caracterizacion=[], enemigo=None, liga=None):
        
        self.__namep = name
        self.__life = life
        self.__energy = energy
        self.__strong = strong
        self.__velocity = velocity
        self.__armor = armor 
        self.__enemigo = enemigo
        self.__liga = liga
        self.__estado = estado
        self.__caracterizacion = caracterizacion
        
        
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
            self.__estado = Estado.MUERTO
        else: 
            self.__estado = Estado.VIVO

    def getlife(self):
        return self.__life
    
        
    def attack(self, personaje):
        if personaje.__estado.name == "VIVO":
            personaje.getdanio(self.__strong)
            print("Ataque basico ha sido exitoso")
        else: 
            print("Personaje no esta vivo. . . .")




    def anhadir_test(self, existencia: Caracterizacion):
        for i in self.__caracterizacion:
            if i == existencia:
                return True
            else:
                False


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
   
   