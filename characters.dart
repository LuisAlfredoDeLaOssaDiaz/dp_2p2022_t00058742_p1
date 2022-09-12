abstract class Characters {
  String? Name;
  int? Level = 1;
  double vida = 10.0;
  double mana = 0.0;
  String? liga;
  List<String>? Powers;
  List<String>? ability;
  List<String>? Weakness;
  List<String>? Weapons;
  String? Personality;
  String? Enemy;

  void attack();
  void defense();
}
