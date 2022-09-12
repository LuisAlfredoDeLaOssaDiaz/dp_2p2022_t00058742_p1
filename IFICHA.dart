import 'dart:io';

import 'ie.dart';

class ificha extends Characters {
  void add(Characters) {
    print('Ingrese un nuevo personaje: ');
    var namep;
    namep = stdin.readLineSync();
    this.Name = namep;
    var level = stdin.readLineSync();
    this.Level = level as int?;
    var vidad = stdin.readLineSync();
    this.vida = vidad as double;
    var manab = stdin.readLineSync();
    this.mana = manab as double;
    var liga = stdin.readLineSync();
    this.liga = liga;
    List<String>? Power = stdin.readLineSync() as List<String>?;
    this.Powers = Power;
    List<String>? abilit = stdin.readLineSync() as List<String>?;
    this.ability = abilit;
    List<String>? Weaknes = stdin.readLineSync() as List<String>?;
    this.Weakness = Weaknes;
    List<String>? Weapon = stdin.readLineSync() as List<String>?;
    this.Weapons = Weapon;
    String? Personalit = stdin.readLineSync();
    this.Personality = Personalit;
    String? Enem = stdin.readLineSync();
    this.Enemy = Enem;
  }

  String? Liga(Characters) {
    return this.liga;
  }

  String? enemy() {
    return this.Enemy;
  }

  @override
  void attack() {}

  @override
  void defense() {}
}
