import 'ie.dart';

void main(List<String> args) {
  final human = new Human();
  final superhuman = new SuperHuman();
  final artificiales = new Artificiales();
  final aliens = new Aliens();

  Attack(human);
  Attack(superhuman);

  Defense(human);
  Defense(superhuman);

  Attack(artificiales);

  Attack(aliens);
}
