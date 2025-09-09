# sou o dono de uma concessionaria e vi o sistema do dono da padaria. gostari de um sistema igual para meus carros.

carros = []

def menu():                                            
    print("\nMENU - CONCESSIONÁRIA")
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. Alterar carro")
    print("4. Excluir carro")
    print("5. Sair")

def cadastrar():                                       
    modelo = input("Modelo do carro: ")
    marca = input("Marca do carro: ")
    try:
        ano = int(input("Ano do carro: "))
        carro = {"modelo": modelo, "marca": marca, "ano": ano}
        carros.append(carro)
        print("Carro cadastrado com sucesso!")
    except ValueError:
        print("Ano inválido. Digite apenas números.")

def listar():                                           
    if not carros:
        print("Nenhum carro cadastrado.")
    else:
        print("\nLista de carros:")
        for i, carro in enumerate(carros):             
            print(f"{i} - Modelo: {carro['modelo']}, Marca: {carro['marca']}, Ano: {carro['ano']}")

def alterar():
    listar()
    try:
        i = int(input("ID do carro para alterar: "))
        if 0 <= i < len(carros):
            modelo = input("Novo modelo: ")
            marca = input("Nova marca: ")
            ano = int(input("Novo ano: "))
            carros[i] = {"modelo": modelo, "marca": marca, "ano": ano}
            print("Carro alterado com sucesso!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida. Digite corretamente.")

def excluir():
    listar()
    try:
        i = int(input("ID do carro para excluir: "))
        if 0 <= i < len(carros):
            carros.pop(i)
            print("Carro excluído com sucesso!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

while True:
    menu()
    opcao = input("Opção: ")
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        alterar()
    elif opcao == '4':
        excluir()
    elif opcao == '5':
        print("Saindo do sistema da concessionária...")
        break
    else:
        print("Opção inválida. Tente novamente.")