import unittest


from enums import *
import enums

from weakness import Debilidades
from ability import Habilidades
from personality import Personalidad
from powers import Poderes
from weaponss import Armas 

from alienz import Aliens
from artificial import Artificiales
from human import Humano
from superhuman import SuperHumanos

class TestPersonaje(unittest.TestCase):
    
    # PERSONAJES PARA TESTEAR
    humano_juan = Humano("Juan", 100, 100, 50, 120, 100, 100, Estado.VIVO, HumanStatus.SUPER_SOLDADO, Sexo.MAN)
    alien_zeus = Aliens("Zeus", 500, 200, 200, 30, 10, 10, Estado.VIVO, TypeAlienigena.XENOMORFOS)
    Artificial_profi = Artificiales("Profi", 800, 150, 300, 70, 200, Estado.VIVO, TypeArticial.mac_2, Laboratorio.LAB_X12)
    super_humano_maria = SuperHumanos("Maria", 500, 500, 500,500,500, 100, Estado.VIVO,SuperHuman.SUPERFUERTE)


    # Caracterizacion para Testear

    pistola = Armas("Pistola", 50,100,30,30)
    m14 = Armas("M14", 70,100,30,30)

    lanza_llamas = Poderes("LanzaLlamas", 500, 100, "LanzaLlamas", Elemento.FUEGO)
    
    pirophobia = Debilidades("Pirophofia", Elemento.FUEGO, -0.4)
    venenophobia = Debilidades("venenophiba", Elemento.VENENO, -0.4)
    
    arrogancia = Personalidad("Arrogancia", "Es Arrogante")
    astucia = Personalidad("Astucia", "Es Astucia")

    lanzar_piedrotas = Habilidades("Lanzar Piedrotas", 500, 20)

    # TESTEAR METODO ADD 
    def test_personaje_add(self):
        self.humano_juan.Add(self.arrogancia)
        self.assertTrue(self.humano_juan.add_test(self.arrogancia))
    
    # TESTEAR METODO ENEMIGO
    def test_personaje_Enemigo(self):
        self.humano_juan.Enemigo(self.alien_zeus)
        self.assertEqual(self.humano_juan.getEnemigo(), self.alien_zeus)
    # TESTEAR SETEO DE LIGA 

    def test_personaje_liga(self):
        self.humano_juan.Liga("Exmachines")
        self.assertEqual(self.humano_juan.getLiga(), "Exmachines")
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
    lanza_llamas = Poderes("LanzaLlamas", 500, 20, "Lanzar fuego de las manos", enums.Elemento.FUEGO)

    def test_poder_nombre(self):
        self.assertAlmostEqual(self.lanza_llamas.getName(), "LanzaLlamas")
    def test_poder_damage(self):
        self.assertEqual(self.lanza_llamas.getDamage(), 500)
    def test_poder_elemento(self):
        self.assertEqual(self.lanza_llamas.getElemento(), "FUEGO")

    # TEST PARA DEBILIDADES
    debilidad_veneno = Debilidades("Venenosis", enums.Elemento.VENENO, -0.5)

    def test_debilidad_efecto(self):
        self.assertEqual(self.debilidad_veneno.getEfecto(), -0.5)
    def test_debilidad_elemento(self):
        self.assertEqual(self.debilidad_veneno.getElemento(), "VENENO")
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