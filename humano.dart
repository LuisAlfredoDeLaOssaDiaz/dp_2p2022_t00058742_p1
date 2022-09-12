import 'ie.dart';

class Human extends Characters {
  String? id_player, name, country, type, Sex;
  List<String>? get Powers => super.Powers = null;

  void attack() => print('Attack...');
  void defense() => print('Defense...');
}
