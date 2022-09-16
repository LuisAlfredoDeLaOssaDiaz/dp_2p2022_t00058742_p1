from enum import Enum




class Laboratorio(Enum):
   LAB_X10 = 'LABX10'
   LAB_X11 = 'LABX11'
   LAB_X12 = 'LABX12'

class Estado(Enum):
    VIVO = "VIVO"
    MUERTO = "MUERTO"

class HumanStatus(Enum):
    MILLONARIO = 'MILLOARIO SUPER TRAJE'
    SUPER_TRAJE = 'SUPER TRAJE'
    EXTRAORDINARIO = 'EXTRAORDINARIO'
    SUPER_SOLDADO = 'SUPER SOLDADO'

class Sexo(Enum):
    MAN =' MAN'
    WOMAN = 'WOMAN'



class Elemento(Enum):
    AIRE = "AIRE"
    FUEGO = "FUEGO"
    TIERRA = "TIERRA"
    PSIQUICO = "PSIQUICO"
    VENENO = "VENENO"
    NORMAL = "NORMAL"
    AGUA = 'AGUA'
    

class SuperHuman(Enum):
    MUTANTE = 'MUTANTE'
    NORMAL = "NORMAL"
    SUPERFUERTE = "SUPERFUERTE"
    VELOCISTA = "VELOCISTA"
    PSIQUICOS = "PSIQUICOS"
    GLANTER = 'GLANTER '
    VOLADOR = 'VOLADOR'

    
class TypeArticial(Enum):
    mac_1 = 'mac 1'
    mac_2 = 'mac 2'
    mac_3 = 'mac 3'
    mac_4 = 'mac 4'
    
class TypeAlienigena(Enum):
    DEPREDATORS= ' DEPREDADORES'
    XENOMORFOS = ' XENOMORFOS'