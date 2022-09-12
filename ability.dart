import 'ie.dart';

class Ability extends Caracterizacion {
  String? name;

  double? damage;
  double? cost;
  int? op;

  @override
  void attack() {
    print("cost mana");

    this.mana = mana - 1;
  }

  @override
  void defense() {
    print('Increment mana');

    this.mana = mana + 1;
  }
}
