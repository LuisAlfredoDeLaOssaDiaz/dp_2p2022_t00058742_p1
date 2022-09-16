import unittest
from enums import *
from Debilidades import Debilidades
from Habilidades import Habilidades
from Personalida import Personalidad
from Poderes import Poderes
from Armas import Armas 

from Aliens import Aliens
from Artificiales import Artificiales
from Humanos import Humano
from SuperHumanos import SuperHumanos

class TestPersonaje(unittest.TestCase):
    # Hacer uso del test para verificar a funcionabilidad de metodo add
    def test_personaje_add(self):
        self.Captain_America.Add(self.arrogancia)
        self.assertTrue(self.Captain_America.add_test(self.arrogancia))
    
    # Hacer uso del test para verificar a funcionabilidad de metodo enemigo
    def test_personaje_Enemigo(self):
        self.Captain_America.Enemigo(self.MarcianManHunter)
        self.assertEqual(self.Captain_America.getEnemigo(), self.MarcianManHunter)
        
    # Hacer uso del test para verificar a funcionabilidad de metodo liga

    def test_personaje_liga(self):
        self.Captain_America.Liga("MARVEL")
        self.assertEqual(self.Captain_America.getLiga(), "MARVEL")

    # PERSONAJES PARA TESTEAR
    
    
    Flash = SuperHumanos("Barry Allen", 455, 358, 500,250,500, 100, Estado.VIVO,SuperHuman.VELOCISTA)
    XENO = Aliens("X", 300, 200, 250, 210, 100, 10, Estado.VIVO, TypeAlienigena.XENOMORFOS)
    Androide18 = Artificiales("18", 800, 15, 500, 70, 20, TypeArticial.mac_3, Laboratorio.LAB_X11)
    Captain_America = Humano("Steve Rogers", 150, 180, 100, 20, 100, 100, Estado.VIVO, HumanStatus.COMANDANTE, Sexo.MAN)
    # Caracterizacion para Testear
    
    flY = Poderes("FLY", 500, 100, "Fly", Elemento.AIRE)
    venenophobia = Debilidades("venenophiba", Elemento.VENENO, -0.4)
    AK47 = Armas("AK47", 50,100,30,30)
    Sniper= Armas("Sniper", 70,100,30,30)

    arrogancia = Personalidad("Astucia", "Es Astuto")

    

if __name__ == "__main__":
    unittest.main()