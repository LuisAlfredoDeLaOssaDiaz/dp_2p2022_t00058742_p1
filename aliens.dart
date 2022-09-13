import 'ie.dart';

//Creamos la clase Aliens extendiendo los atributos y metodos de personajes
class Aliens extends Characters {
  String? id_player, name, galaxy, type, Sex;

  void attack() => print('Aliens Attack...');
  void defense() => print('Aliens Defense...');
  void levelup() => null;
}
