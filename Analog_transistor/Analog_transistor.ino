/*
  Analog input, analog output, serial output
 
 Reads an analog input pin, maps the result to a range from 0 to 255
 and uses the result to set the pulsewidth modulation (PWM) of an output pin.
 Also prints the results to the serial monitor.
 
 The circuit:
 * potentiometer connected to analog pin 0.
   Center pin of the potentiometer goes to the analog pin.
   side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 9 to ground
 
 created 29 Dec. 2008
 modified 30 Aug 2011
 by Tom Igoe
 
 This example code is in the public domain.
 
 */

// These constants won't change.  They're used to give names
// to the pins used:
const int analogOutPin = 9; // Analog output pin that the LED is attached to
int outputValue = 128;        // value output to the PWM (analog out) (0-255)

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600); 
}

void loop() {
  // change the analog out value:
  analogWrite(analogOutPin, outputValue);

  // wait 10 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(10);                     
}
