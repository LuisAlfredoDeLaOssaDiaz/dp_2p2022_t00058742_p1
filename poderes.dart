import 'caracterizacion.dart';
import 'ie.dart';

//Creamos la clase Poderes extendiendo los atributos y metodos de cracterizacion
class Poderes extends Caracterizacion {
  String? name_power;
  String? atributo;
  double? intensity;
  bool? fatality = false;
  void incrementof() {
    fatality = true;
  }

  int? op = 0;
  int? i;
  @override
  void attack() {
    if (op == 1) {
      incrementof();
      if (intensity == true) {
        print("Finish him FATALITY");
        for (i; i! < 2;) {
          this.vida = vida - vida;
        }
      } else {
        print('Normal Attack');
        for (i; i! < 2;) {
          this.vida = vida - 1;
        }
      }
    }
  }

  @override
  void defense() {
    if (op == 1) {
      incrementof();
      if (intensity == true) {
        print("Super DEFENSE");
        for (i; i! < 2;) {
          this.vida = vida + vida;
        }
      } else {
        print('Normal Defense');
        for (i; i! < 2;) {
          this.vida = vida + 1;
        }
      }
    }
  }
}
