// c++ code
//
/*
  this program blinks pin 13 of the arduino (the
  built-in led)
*/

#include <Adafruit_LiquidCrystal.h>

Adafruit_LiquidCrystal lcd_1(0);

#define echoPin 7
#define trigPin 6

long duration;
int distance;

int firstGreen = 9;
int firstYellow = 10;
int firstRed = 11;

int secondGreen = 2;
int secondYellow = 3;
int secondRed = 4;

int shortDelay = 2500;
int longDelay = 5000;

void setup() {
  // setup the sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // setup the first set of button + lights
  pinMode(firstGreen, OUTPUT);
  pinMode(firstYellow, OUTPUT);
  pinMode(firstRed, OUTPUT);

  // setup the second set of button + lights
  pinMode(secondGreen, OUTPUT);
  pinMode(secondYellow, OUTPUT);
  pinMode(secondRed, OUTPUT);

  // initializes the lcd
  lcd_1.begin(16, 2);
}

void loop() {
  int distance = sonarPulse();

  // 50 centimeters
  if (distance <= 50) {
    digitalWrite(firstRed, LOW);
    digitalWrite(firstYellow, HIGH);
    digitalWrite(firstGreen, LOW);

    digitalWrite(secondRed, HIGH);
    digitalWrite(secondGreen, LOW);
    digitalWrite(secondYellow, LOW);
    delay(shortDelay);

    digitalWrite(firstRed, HIGH);
    digitalWrite(firstYellow, LOW);

    // takes 10 seconds to complete the loop
    for (int seconds = 0; seconds < 10; seconds++) {
      lcd_1.clear();
      lcd_1.print("SIGA");

      lcd_1.setCursor(0, 1);
      lcd_1.print(10 - seconds);
      delay(1000); // 1 second
    }
    digitalWrite(firstRed, LOW);
  }
  trafficDefaultLoop();
}

void trafficDefaultLoop() {
  lcd_1.clear();
  lcd_1.print("PARE");

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

int sonarPulse() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}
