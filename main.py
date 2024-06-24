import serial

# Configuração da porta serial - ajuste a porta e a taxa de transmissão conforme necessário
porta_serial = serial.Serial('COM3', 9600)  

def morse_para_letras(morse_string):
    # Dicionário de tradução de Morse para letras
    morse_para_letra = {
        ".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D',
        ".": 'E', "..-.": 'F', "--.": 'G', "....": 'H',
        "..": 'I', ".---": 'J', "-.-": 'K', ".-..": 'L',
        "--": 'M', "-.": 'N', "---": 'O', ".--.": 'P',
        "--.-": 'Q', ".-.": 'R', "...": 'S', "-": 'T',
        "..-": 'U', "...-": 'V', ".--": 'W', "-..-": 'X',
        "-.--": 'Y', "--..": 'Z', "-----": '0', ".----": '1',
        "..---": '2', "...--": '3', "....-": '4', ".....": '5',
        "-....": '6', "--...": '7', "---..": '8', "----.": '9',
        ".-.-.-": '.', "--..--": ',', "..--..": '?', "-..-.": '/',
        "-....-": '-', "-.--.": '(', "-.--.-": ')', ".----.": "'",
        "---...": ':', ".-..-.": '"', ".--.-.": '@', "-.-.--": '!',
        " ": ' '  # Espaço em Morse
    }

    # Dividir a string de Morse em palavras
    palavras_morse = morse_string.strip().split(" ")

    # Traduzir cada palavra em Morse para letras
    letras = []
    for palavra in palavras_morse:
        letras_palavra = [morse_para_letra[simbolo] for simbolo in palavra.split()]
        letras.append("".join(letras_palavra))

    # Retornar a lista de palavras traduzidas
    return " ".join(letras)

def tradutor_binário(binary):
    # Verifica se o comprimento da string é múltiplo de 2
    if len(binary) % 2 != 0:
        binary = binary[:-1]
    
    # Dicionário para conversão de pares binários para Morse
    morse_dict = {
        '00': ' ',
        '01': '.',
        '11': '-'
    }
    
    # Converte a string binária para Morse
    morse_string = ''
    for i in range(0, len(binary), 2):
        pair = binary[i:i+2]
        if pair in morse_dict:
            morse_string += morse_dict[pair]
  
    return morse_string


# Lista para armazenar os dados recebidos
dados_serial = []


try:
    while True:
        # Lê uma linha da porta serial
        linha = porta_serial.readline().decode('utf-8').strip()
        
        # Adiciona a linha à lista de dados
        dados_serial.append(linha)
        
        # Exibe a linha lida (opcional)
        print(linha)
        
except KeyboardInterrupt: # Tratamento de interrupção de teclado (Ctrl+C)
    porta_serial.close()
    print("Leitura da porta serial encerrada.")

# Remover todas as ocorrências de "==================" da lista
dados_serial = [item for item in dados_serial if item != "=================="]

# Exibe os dados coletados após remoção de "=================="
print("Dados coletados:")
print(dados_serial)

# Juntando todos os dados em uma única string
strjoin = ''.join(dados_serial)


# Testando a função de tradução binária para Morse
morse_output = tradutor_binário(strjoin)
print(f"Binario: {strjoin}")
print(f"Morse: {morse_output}")


# Exemplo de uso da função morse_para_letras com a string de Morse gerada
letras = morse_para_letras(morse_output)
print(f"Texto em Morse traduzido para letras: {letras}")
