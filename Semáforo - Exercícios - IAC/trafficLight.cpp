// c++ code
//
/*
  this program blinks pin 13 of the arduino (the
  built-in led)
*/

#include <Adafruit_LiquidCrystal.h>

Adafruit_LiquidCrystal lcd_1(0);

#define echoPin 5
#define trigPin 4

long duration;
int distance;

int firstGreen = 8;
int firstYellow = 9;
int firstRed = 10;
int firstButton = 11;

int secondGreen = 0;
int secondYellow = 1;
int secondRed = 2;
int secondButton = 3;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(firstGreen, OUTPUT);
  pinMode(firstYellow, OUTPUT);
  pinMode(firstRed, OUTPUT);
  pinMode(firstButton, INPUT);

  pinMode(secondGreen, OUTPUT);
  pinMode(secondYellow, OUTPUT);
  pinMode(secondRed, OUTPUT);
  pinMode(secondButton, INPUT);

  digitalWrite(firstYellow, LOW);
  digitalWrite(firstRed, LOW);

  digitalWrite(secondYellow, LOW);
  digitalWrite(secondGreen, LOW);

  lcd_1.begin(16, 2);
}

void loop() {
  // if (digitalRead(firstButton) == HIGH or digitalRead(secondButton) == HIGH)
  // {
  //   delay(15); // 15 miliseconds

  //   if (digitalRead(firstButton) == HIGH or digitalRead(secondButton) ==
  //   HIGH) {
  //     // turn on firstRed
  //     digitalWrite(firstRed, HIGH);
  //     digitalWrite(firstYellow, LOW);
  //     digitalWrite(firstGreen, LOW);

  //     // turn on secondRed
  //     digitalWrite(secondRed, HIGH);
  //     digitalWrite(secondYellow, LOW);
  //     digitalWrite(secondGreen, LOW);

  //     for (int seconds = 0; seconds < 10; seconds++) {
  //       lcd_1.clear();
  //       lcd_1.print("SIGA");
  //       lcd_1.setCursor(0, 1);
  //       lcd_1.print(10 - seconds);
  //       delay(1000);
  //     }
  //     digitalWrite(firstButton, LOW);
  //     digitalWrite(secondButton, LOW);
  //     digitalWrite(secondRed, LOW);
  //     digitalWrite(firstRed, LOW);
  //   }
  // }

  Serial.begin(9600);
  Serial.println("Ultrasonic Sensor HC-SR04 Test");
  Serial.println("with Arduino UNO R3");
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  if (distance <= 20) {

    // turn on firstRed
    digitalWrite(firstRed, HIGH);
    digitalWrite(firstYellow, LOW);
    digitalWrite(firstGreen, LOW);

    // turn on secondRed
    digitalWrite(secondRed, HIGH);
    digitalWrite(secondYellow, LOW);
    digitalWrite(secondGreen, LOW);

    for (int seconds = 0; seconds < 10; seconds++) {
      lcd_1.clear();
      lcd_1.print("SIGA");
      lcd_1.setCursor(0, 1);
      lcd_1.print(10 - seconds);
      delay(1000);
    }
    digitalWrite(firstButton, LOW);
    digitalWrite(secondButton, LOW);
    digitalWrite(secondRed, LOW);
    digitalWrite(firstRed, LOW);
  }
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  lcd_1.clear();
  lcd_1.print("PARE");

  digitalWrite(firstGreen, HIGH);
  digitalWrite(secondRed, HIGH);
  delay(2000); // 2 seconds

  digitalWrite(firstGreen, LOW);
  digitalWrite(secondRed, LOW);

  digitalWrite(firstYellow, HIGH);
  digitalWrite(secondYellow, HIGH);
  delay(1000); // 1 second

  digitalWrite(firstYellow, LOW);
  digitalWrite(firstRed, HIGH);
  digitalWrite(secondYellow, LOW);
  digitalWrite(secondGreen, HIGH);
  delay(2000); // 2 seconds

  digitalWrite(firstRed, LOW);
  digitalWrite(secondGreen, LOW);
}
