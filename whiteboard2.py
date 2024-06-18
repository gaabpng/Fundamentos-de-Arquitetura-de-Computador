def transcricao(lista):
    global palavra
    i = 0
    while i < len(lista):
        if i + 2 < len(lista) and lista[i] == "1" and lista[i + 1] == "1" and lista[i + 2] == "1":
            palavra.append("-")
            i += 3  # Pula os próximos dois elementos, pois já foram processados
        elif i + 1 < len(lista) and lista[i] == "1" and lista[i + 1] == "0":
            palavra.append(".")
            i += 1  # Pula o próximo elemento, pois já foi processado
        elif i+1 < len(lista) and lista[i] == "0" and lista[i+1] == "0":
            palavra.append(" ")
            i += 1  # Pula para o próximo elemento
        else:
            i+= 1
    return palavra

# Entrada do usuário
lista = ['1', '1', '1','1', '1', '1','1', '1', '1','0', '0','1', '0', '1', '0', '1','0','0',  '1', '1', '1','1', '1', '1','1', '1', '1']
entrada = ""

# while entrada != "-1":
#     entrada = input()
#     if entrada != "-1":
#         lista.append(entrada)

# Adiciona dois zeros ao final da lista para garantir que a lógica funcione corretamente
lista.append("0")
lista.append("0")


# Transcrição da lista para a palavra
palavra = []
transcricao(lista)

palavra.pop()
# Imprime a palavra resultante
print(lista)
print(palavra)
