import 'ie.dart';

class testPersonajes extends Human {
  @override
  // TODO: implement Name
  String? get name => super.name = this.name = 'Naruto';
  @override
  // TODO: implement id_player
  String? get id_player => super.id_player = this.id_player = "T00058742";
  @override
  // TODO: implement country
  String? get country => super.country = this.country = 'Colombia';

  @override
  // TODO: implement type
  String? get type => super.type = this.type = "Guerrero";
  @override
  // TODO: implement Sex
  String? get Sex => super.Sex = this.Sex = 'Masculino';

  @override
  void attack() => null;

  @override
  void defense() => null;
}
