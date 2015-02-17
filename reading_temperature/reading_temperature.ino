//include wire library
#include <Wire.h>

//set the address of the temp sensor
int temp_address = 72;

void setup()
{
  Serial.begin(9600);
  Wire.begin();
}

void loop()
{
  //start talking
  Wire.beginTransmission(temp_address);
  //Ask for register zero
  Wire.write((uint8_t) 0);
  //Complte transmission
  Wire.endTransmission();
  //request 1 byte
  Wire.requestFrom(temp_address, 1); 
  //wait for response
  while(Wire.available() == 0);
  //get the temp
  int c = Wire.read();
  
  //convert from celcius to farenheight 
  int f = round(c*(9.0/5.0) +32.0);
  
  //print the results 
  Serial.print(c);
  Serial.print("C,");
  Serial.print(f);
  Serial.println("F");
  
  //delay, then do it again
  delay(50);
  
}
