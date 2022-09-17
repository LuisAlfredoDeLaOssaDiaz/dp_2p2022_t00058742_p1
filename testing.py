import unittest
from enumerations import *
import enumerations
#from Debilidades import Debilidades
from habilidades import Habilidades
from personalidad import Personalidad
from poderes import Poderes
from armas import Armas 

from aliens import Aliens
from artificiales import Artificiales
from humanos import Humano
from superhumanos import SuperHumanos

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
    Captain_America = Humano("Steve Rogers", 150, 180, 100, 20, 100, 100, Estado.VIVO, HumanStatus.SUPER_SOLDADO, Sexo.MAN)
    # Caracterizacion para Testear
    
    flY = Poderes("FLY", 500, 100, "Fly", Elemento.AIRE)
    #venenophobia = Debilidades("venenophiba", Elemento.VENENO, -0.4)
    AK47 = Armas("AK47", 50,100,30,30)
    Sniper= Armas("Sniper", 70,100,30,30)

    arrogancia = Personalidad("Astucia", "Es Astuto")

    

if __name__ == "__main__":
    unittest.main()
class TestArmas(unittest.TestCase):
# TEST PARA ARMAS
    def test_Arma_Nombre(self):
        pistola = Armas("Pistola", 50,100,30,30)

        result1 = pistola.getName()
        self.assertEqual(result1, "Pistola")
    
    def test_Arma_Disparo(self):

        pistola = Armas("Pistola", 50,100,30,30)

        result2 = pistola.getDamage()

        self.assertEqual(result2, 50)

    # TEST PARA PODERES
    lanza_llamas = Poderes("LanzaLlamas", 500, 20, "Lanzar fuego de las manos", enumerations.Elemento.FUEGO)

    def test_poder_nombre(self):
        self.assertAlmostEqual(self.lanza_llamas.getName(), "LanzaLlamas")
    def test_poder_damage(self):
        self.assertEqual(self.lanza_llamas.getDamage(), 500)
    def test_poder_elemento(self):
        self.assertEqual(self.lanza_llamas.getElemento(), "FUEGO")

    # TEST PARA DEBILIDADES
   # debilidad_veneno = Debilidades("Venenosis", enumerations.Elemento.VENENO, -0.5)

    
    # TEST PARA HABILIDADES
    lanzar_personaje = Habilidades("Lanzamiento", 500, 50)

    def test_habilidad_cost(self):
        self.assertEqual(self.lanzar_personaje.getCost(), 50)
    def test_habilidad_damage(self):
        self.assertEqual(self.lanzar_personaje.getDamage(), 500)

    # TEST PARA PERSONALIDADES 
    arrogante = Personalidad("Arrogante", "Es Arrogante JAJAJA")
    
    def test_personalidad_name(self):
        self.assertEqual(self.arrogante.getName(), "Arrogante")
    def test_personalidad_descrip(self):
        self.assertEqual(self.arrogante.getDescription(), "Es Arrogante JAJAJA")
if __name__ == "__main__":
    unittest.main()