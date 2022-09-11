import 'ie.dart';

class SuperHuman extends Characters {
  List<String>? get Weapons => super.Weapons = null;
  void attack() => print("Super Attack...");
  void defense() => print('Super Defense...');
  void levelup() => print('***¡Super Level UP!***');
}
