import 'ie.dart';

//Creamos la clase Artificiales extendiendo los atributos y metodos de personajes
class Artificiales extends Characters {
  String? id_player, name, creator, type, cod;

  void attack() => print('Artificial Attack...');
  void defense() => print('Artificial Defense...');
}
