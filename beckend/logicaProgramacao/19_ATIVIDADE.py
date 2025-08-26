# Criar uma lista com cadastro de usuario, usar (função,lista, try/except,laços)
# Cadastrar 
# Alterar
# Excluir
# Listar

usuarios = []

def cadastrar_usuario():
    try:
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        usuarios.append({"nome": nome, "idade": idade})
        print("Usuário cadastrado com sucesso!\n")
    except ValueError:
        print("Idade inválida. Tente novamente.\n")


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
    else:
        print("Lista de usuários:")
        for indice, usuario in enumerate(usuarios):
            print(f"{indice} - Nome: {usuario['nome']}, Idade: {usuario['idade']}")
        print()


def alterar_usuario():
    try:
        listar_usuarios()
        indice = int(input("Digite o número do usuário que deseja alterar: "))
        if 0 <= indice < len(usuarios):
            novo_nome = input("Digite o novo nome: ")
            nova_idade = int(input("Digite a nova idade: "))
            usuarios[indice]["nome"] = novo_nome
            usuarios[indice]["idade"] = nova_idade
            print("Usuário alterado com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")


def excluir_usuario():
    try:
        listar_usuarios()
        indice = int(input("Digite o número do usuário que deseja excluir: "))
        if 0 <= indice < len(usuarios):
            usuarios.pop(indice)
            print("Usuário excluído com sucesso!\n")
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida. Tente novamente.\n")


def menu():
    while True:
        print("=== MENU ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Alterar usuário")
        print("4 - Excluir usuário")
        print("5 - Sair")
        
        escolha = input("Escolha uma opção: ")
        print()

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            listar_usuarios()
        elif escolha == "3":
            alterar_usuario()
        elif escolha == "4":
            excluir_usuario()
        elif escolha == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


menu()
