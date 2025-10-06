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
id = int(input("Digite o id do Produto:"))
nome = input("Digite o nome do produto:")
quantidade = int(input("Digite a quantidade:"))
preco = float(input("Digite o preço:"))

# Cria o novo produto
novo_produto = {
    "id" : id,
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

# Modificar Produto

id_produto_modificar = int (input("Digite o id para modificar:"))
nova_quantidade = int (input("Digite a nova quantidade:"))

try:
    with open ("loja.json","r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("arquivo não encontrado")

produto_encontrado = False

for produto in inventario:
    if produto["id"] == id_produto_modificar:
        # Colocamos a Nova Quantidade
        produto["quantidade"] = nova_quantidade
        produto["em_estoque"] = nova_quantidade > 0
        produto_encontrado = True
        break;

if not produto_encontrado:
    print("O produto com o id informado não foi encontrado")  

else:
    with open ("loja.json","w") as arquivo:
        json.dump(inventario, arquivo , ident = 4) 

    print("O arquivo foi alterado com sucesso!!")
     
        




