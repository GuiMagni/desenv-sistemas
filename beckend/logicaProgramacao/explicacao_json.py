import json
#{} -> Chaves: Definir um objeto -> Ficha de cadastro -> pessoa: nome,cpf,telefone
#[] -> Colchete: Definir uma lista
# Chave/Valor: Chave Descreve o valor  Chave = telefone  Valor = 4499999999
inventario = []

# Tenta carregar o arquivo existente
try:
    with open("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado. Um novo será criado.")

# Coleta dados do usuário
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço: "))

# Cria o novo produto
novo_produto = {
    "nome": nome,
    "quantidade": quantidade,
    "preco": preco,
    "em_estoque": quantidade > 0
}

# Adiciona ao inventário
inventario.append(novo_produto)

# Salva no arquivo
with open("loja.json", "w") as arquivo:
    json.dump(inventario, arquivo, indent=4)

print("Produto cadastrado com sucesso!")






