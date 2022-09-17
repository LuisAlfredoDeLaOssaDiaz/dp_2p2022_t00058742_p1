from characters import Personaje
from enums import HumanStatus, Sexo

class Humano(Personaje):
    HumanStatus: HumanStatus
    Sexo: Sexo

    def __init__(self,   name, life, energy, strong, velocity, armor, estado, HumanStatus, sexo,  enemigo=None, liga=None):
        "Instanciar un humano para agregarlo al juego, puedes agregarle caracteristicas"
        super().__init__( name, life, energy, strong, velocity, armor, estado,  enemigo, liga)
        self.HumanStatus = HumanStatus
        self.Sexo = sexo

    def getHumanStatus(self):
        return self.HumanStatus.name
    def getSexo(self):
        return self.Sexo.name