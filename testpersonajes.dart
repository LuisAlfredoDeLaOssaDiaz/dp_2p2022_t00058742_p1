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

class testpersonajes2 extends Aliens {
  @override
  // TODO: implement Name
  String? get name => super.name = this.name = 'Zardok';
  @override
  // TODO: implement id_player
  String? get id_player => super.id_player = this.id_player = "T000880400";
  @override
  // TODO: implement country
  String? get Galaxy => super.galaxy = this.galaxy = 'nova';

  @override
  // TODO: implement type
  String? get type => super.type = this.type = "Depredator";
  @override
  // TODO: implement Sex
  String? get Sex => super.Sex = this.Sex = 'Femenino';
}

class testpersonajes3 extends Artificiales {
  @override
  // TODO: implement Name
  String? get name => super.name = this.name = '18';
  @override
  // TODO: implement id_player
  String? get id_player => super.id_player = this.id_player = "T00088123";
  @override
  // TODO: implement country
  String? get Creator => super.creator = this.creator = 'Doc Mczero';

  @override
  // TODO: implement type
  String? get type => super.type = this.type = "Androide";
  @override
  // TODO: implement Sex
  String? get COD => super.cod = this.cod = '123456789';
}

class testPersonajes3 extends SuperHuman {
  @override
  // TODO: implement Name
  String? get name => super.name = this.name = 'SuperMan';
  @override
  // TODO: implement id_player
  String? get id_player => super.id_player = this.id_player = "T000512342";
  @override
  // TODO: implement country
  String? get country => super.country = this.country = 'EEUU';

  @override
  // TODO: implement type
  String? get type => super.type = this.type = "Heroe";
  @override
  // TODO: implement Sex
  String? get Sex => super.Sex = this.Sex = 'Masculino';

  @override
  void attack() => null;

  @override
  void defense() => null;
}
