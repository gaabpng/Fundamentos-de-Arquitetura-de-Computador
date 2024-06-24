// Variáveis globais
unsigned long ultimoTempo = 0;  // Variável para controlar o tempo da última verificação
const unsigned long intervaloVerificacao = 1300;  // Intervalo desejado entre as verificações em milissegundos
int contadorVerificacoes = 0;  // Contador de verificações

void setup()
{
    Serial.begin(9600);
    pinMode(2, INPUT_PULLUP);
    pinMode(13, OUTPUT);
}

void loop()
{
    // Verificação do tempo para realizar ação a cada intervaloVerificacao
    unsigned long tempoAtual = millis();
    if (tempoAtual - ultimoTempo >= intervaloVerificacao)
    {
        ultimoTempo = tempoAtual;  // Atualiza o último tempo de verificação

        // Realiza a leitura do sensor
        int sensorVal = digitalRead(2);

        // Inverte o valor do sensor para imprimir 1 quando estiver fechado e 0 quando estiver aberto
        int valorParaImprimir = (sensorVal == LOW) ? 1 : 0;

        // Imprime o valor do sensor invertido
        Serial.println(valorParaImprimir);

        // Controla o LED baseado no valor do sensor
        if (sensorVal == HIGH)
        {
            digitalWrite(13, LOW);
        }
        else
        {
            digitalWrite(13, HIGH);
        }

        contadorVerificacoes++;  // Incrementa o contador de verificações

        // A cada duas verificações, imprimir "=================="
        if (contadorVerificacoes % 2 == 0)
        {
            Serial.println("==================");
        }
    }

    // Outras operações do loop podem ser colocadas aqui
    // Importante não usar delay(), pois isso bloquearia o loop.
}
