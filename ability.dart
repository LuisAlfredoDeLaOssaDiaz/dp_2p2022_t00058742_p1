import 'ie.dart';

//Creamos la clase Ability extendiendo los atributos y metodos de cracterizacion
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
