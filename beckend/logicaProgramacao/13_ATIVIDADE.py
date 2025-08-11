#criar função de menu de opções e pedir a opção desejada do usuário
#-criar função de deposito
#-criar função de saque
#-criar função de ver saldo
#-aqao digitar "sair" encerrar o progama

saldo = 0.0

def menu():
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Ver saldo")
    print("Digite 'sair' para encerrar")
    return input("Escolha uma opção: ")

def deposito():
    global saldo
    valor = float(input("Digite o valor para depósito: "))
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido!")