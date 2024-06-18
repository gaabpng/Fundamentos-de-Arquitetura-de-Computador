import time

pinoPiezo = "Porta Analógica A0"
pinoLed = "Porta Digital 13" #porta 13 possui um led imbutido no arduino
nome_arquivo = "main.txt"

def setup():
    # define pinos e modos
    # define pino de led como low
    print("Inicializando (5 segundos)")
    time.sleep(5000) #delay de 5 segundos

def escrever(entrada):
    global nome_arquivo

    with open(nome_arquivo, '+a') as arquivo:
        arquivo.write(entrada)


def piscarLed():
    # liga luz
    # espera 100 ms
    # desliga luz
    print()

def loop():
    piscarLed()
    valorPiezo = input() #a entrada será controlado pelo Serial.println do arduino
    if valorPiezo < 150:
        print()

# def op5():
#     nome_arquivo = input("Nome do arquivo: ")
#     nome_arquivo = "Prog1/" + nome_arquivo
#     with open(nome_arquivo, 'a+') as arquivo:
#         nome = input("Nome do aluno: (SEM ESPAÇO) ")
#         matricula = input("Matrícula do aluno: ")
#         p1 = input("Nota da P1: ")
#         p2 = input("Nota da P2: ")
#         trabalho = input("Nota do trabalho: ")

#         linha = f"{nome}\t{matricula}\t{p1}\t{p2}\t{trabalho}\n"
#         arquivo.write(linha)

#         continuar = input("Deseja continuar? (S/N): ").strip().upper()
#         if continuar == "S":
#             op5()
#         else:
#             arquivo.close()
#             print("Dados gravados com sucesso.")
#             main()