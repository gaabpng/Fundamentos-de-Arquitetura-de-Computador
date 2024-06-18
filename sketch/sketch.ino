const int pinoPiezo = A0;
const int pinoLed = 13;

void setup(){
  pinMode(pinoSinal, INPUT); 
  pinMode(pinoLed, OUTPUT);
  digitalWrite(pinoLed, LOW);
  Serial.print("Inicializando (5 segundos)");
  delay(5000);
}

void piscarLed(){
    digitalWrite(pinoLed, HIGH);
    delay(100);
    digitalWrite(pinoLed, LOW);
}

void loop(){
    piscarLed();

    Serial.println("feito!");
    delay(1500);
}