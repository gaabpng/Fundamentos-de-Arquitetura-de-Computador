def tradutor_binário(binary):
    # Verifica se o comprimento da string é múltiplo de 2
    if len(binary) % 2 != 0:
        raise ValueError("A string binária deve ter um comprimento par.")

    # Define a conversão de pares binários para Morse
    morse_dict = {
        '00': ' ',
        '01': '.',
        '11': '-'
    }

    # Converte a string binária para Morse
    morse_string = ''
    for i in range(0, len(binary), 2):
        pair = binary[i:i+2]
        if pair not in morse_dict:
            raise ValueError(f"Par inválido encontrado: {pair}")
        morse_string += morse_dict[pair]
    
    return morse_string

# Testando a função
binary_input = input()
morse_output = tradutor_binário(binary_input)
print(f"Binary: {binary_input}")
print(f"Morse: {morse_output}")
