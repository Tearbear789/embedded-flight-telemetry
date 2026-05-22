#include <Arduino.h>

// Initialize
void setup()
{
    Serial.begin(115200);
    delay(2000);

    Serial.println("altitude,battery,pitch,roll");
}

// Main Loop generating random telemetry data
void loop()
{
    float altitude = random(1000, 1200) / 10.0;
    float battery = random(110, 126) / 10.0;
    float pitch = random(-100, 100) / 10.0;
    float roll = random(-100, 100) / 10.0;

    Serial.print(altitude);
    Serial.print(",");
    Serial.print(battery);
    Serial.print(",");
    Serial.print(pitch);
    Serial.print(",");
    Serial.println(roll);

    delay(250);
}