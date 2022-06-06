// c++ code
//
/*
  this program blinks pin 13 of the arduino (the
  built-in led)
*/

int firstGreen = 9;
int firstYellow = 10;
int firstRed = 11;
int firstButton = 12;

int secondGreen = 2;
int secondYellow = 3;
int secondRed = 4;
int secondButton = 5;

int shortDelay = 2500;
int longDelay = 5000;

void setup() {
  // setup the first set of button + lights
  pinMode(firstGreen, OUTPUT);
  pinMode(firstYellow, OUTPUT);
  pinMode(firstRed, OUTPUT);
  pinMode(firstButton, INPUT);

  // setup the second set of button + lights
  pinMode(secondGreen, OUTPUT);
  pinMode(secondYellow, OUTPUT);
  pinMode(secondRed, OUTPUT);
  pinMode(secondButton, INPUT);
}

void loop() {
  if (digitalRead(firstButton) == HIGH or digitalRead(secondButton) == HIGH) {
    digitalWrite(firstRed, LOW);
    digitalWrite(firstGreen, LOW);
    digitalWrite(firstYellow, HIGH);
    digitalWrite(secondRed, HIGH);
    delay(shortDelay);
    digitalWrite(firstYellow, LOW);
    digitalWrite(firstRed, HIGH);
    digitalWrite(secondGreen, LOW);
    digitalWrite(secondYellow, LOW);
    delay(2*longDelay);
  }
  digitalWrite(firstYellow, LOW);
  digitalWrite(secondRed, LOW);
  trafficDefaultLoop();
}

void trafficDefaultLoop() {
  digitalWrite(firstGreen, HIGH);
  digitalWrite(secondRed, HIGH);
  delay(longDelay);

  digitalWrite(firstGreen, LOW);
  digitalWrite(secondRed, LOW);

  digitalWrite(firstYellow, HIGH);
  digitalWrite(secondGreen, HIGH);
  delay(shortDelay);

  digitalWrite(firstYellow, LOW);
  digitalWrite(secondGreen, LOW);

  digitalWrite(firstRed, HIGH);
  digitalWrite(secondYellow, HIGH);
  delay(longDelay);

  digitalWrite(firstRed, LOW);
  digitalWrite(secondYellow, LOW);
  digitalWrite(firstGreen, HIGH);
}
