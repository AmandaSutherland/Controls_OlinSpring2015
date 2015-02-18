//include wire library
#include <Wire.h>

// These constants won't change.  They're used to give names
// to the pins used:
const int analogOutPin = 9; // Analog output pin that the LED is attached to
int outputValue;
//set the address of the temp sensor
int temp_address = 72;
int kP = 5 ; 
float kI = 0.1; 
int P;
int I ; 
long IntegralSum ;

void setup()
{
  Serial.begin(9600);
  Wire.begin();
}

void loop()
{
    Wire.beginTransmission(temp_address);  //start talking
    Wire.write((uint8_t) 0);                                //Ask for register zero
    Wire.endTransmission();                           //Complete transmission
    Wire.requestFrom(temp_address, 1);     //request 1 byte
    while(Wire.available() == 0);                      //wait for response
    int c = Wire.read();                                        //get the temp
   
    // proportiona8l control/
    int Error = 40 - c;

    IntegralSum += Error;
    P = Error * kP;
    I = IntegralSum * kI;
    outputValue = P+I;
    if (c >= 40){  // don't heat transistor if temp is above 40 
      outputValue = 0 ; 
    }
    else if (outputValue > 128 ){
      outputValue = 128;   
    }
  
     // change the analog out value:
    analogWrite(analogOutPin, outputValue);
    
    //convert from celcius to farenheight 
    int f = round(c*(9.0/5.0) +32.0);
    
    //print the results 
    Serial.print(c);
//    Serial.print(" C, ");
//    Serial.print(f);
//    Serial.print(" F, ");
    Serial.print(",");
    Serial.println(outputValue);
//    Serial.println(" outputValue");
    
    //delay, then do it again
    delay(250);
     
}
