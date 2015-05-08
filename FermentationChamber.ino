#include <OneWire.h>
#include <DallasTemperature.h>

const int AIR_TEMP_PIN = 0;
 
// Data wire is plugged into pin 2 on the Arduino
#define ONE_WIRE_BUS 2
 
// Setup a oneWire instance to communicate with any OneWire devices 
// (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);
 
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);
 
void setup(void)
{
  // start serial port
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");

  // Start up the library
  sensors.begin();
}
 
 
void loop(void)
{
  float voltage, degreesC, degreesF;
  voltage = getVoltage(AIR_TEMP_PIN);
  degreesC = (voltage - 0.5)*100.0;
  degreesF = degreesC * (9.0/5.0) + 32.0;
  
  sensors.requestTemperatures(); // Send the command to get temperatures
  Serial.print("wort:");
  Serial.print(sensors.getTempFByIndex(0)); // Why "byIndex"? 
  Serial.print("air:");
  Serial.println(degreesF);
}


float getVoltage(int pin)
{
  return (analogRead(pin) * 0.004882814);
}
