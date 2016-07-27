const int sensor = PC1;
const int light = A2;

void setup()
{
        Serial.begin(9600);
        pinMode(sensor, INPUT);  // set pin for slider input
        pinMode(light, OUTPUT);  // set pin for slider led
}

void loop()
{
	analogWrite(light,0);
        int sensorVal = analogRead(sensor);
        Serial.print("p: ");
        Serial.print(sensorVal);
        Serial.println(" ");
        delay(25); //read 20 times per second
	analogWrite(light,3*0x3F);
        delay(25); //read 20 times per second
}

