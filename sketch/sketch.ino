// Definição de constantes
const int piezoPin = A2;       // Pino analógico onde o piezo está conectado
const int ledPin = 13;         // Pino do LED integrado
const int threshold = 120;     // Valor de limiar para o sensor piezo
const unsigned long interval = 1300; // Intervalo de verificação em milissegundos

// Variáveis para controle de tempo
unsigned long previousMillis = 0;

void setup() {
  // Inicializa a comunicação serial
  Serial.begin(9600);
  
  // Configura o pino do LED como saída
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Verifica o tempo decorrido
  unsigned long currentMillis = millis();
  
  // Se o tempo decorrido for maior ou igual ao intervalo especificado
  if (currentMillis - previousMillis >= interval) {
    // Atualiza o tempo da última verificação
    previousMillis = currentMillis;
    
    // Lê o valor do sensor piezo
    int sensorValue = analogRead(piezoPin);
    
    // Verifica o valor lido e imprime a mensagem correspondente
    if (sensorValue > threshold) {
      Serial.println("0");
    } else {
      Serial.println("1");
    }
    
    // Pisca o LED integrado
    digitalWrite(ledPin, HIGH);  // Liga o LED
    delay(50);                   // Espera 50ms
    digitalWrite(ledPin, LOW);   // Desliga o LED
    
    static int count = 0;
    count++;
    
    // A cada dois prints, imprime "=================="
    if (count % 2 == 0) {
      Serial.println("==================");
    }
  }
}
