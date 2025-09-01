# TRABALHANDO COM ARQUIVOS
# With open ('compras.TxT',"w")
# w abrir o arquivo nomodo escrita
# a abrir no modo edição
# r abrir no modo leitura
  
  with open ("Tarefas.txt", "w") as arquivo:
    arquivo.write ("Lavar a Louça \n")
    arquivo.write ("Lavar Quintal")

# Ler o arquivo

with open ("compras.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Ler o arquivo linha por linha

with open ("compras.txt" "r") as arquivo:
    for produto in arquivo:
        print ("produto:" produto.strip())
                                #"Strip" = Remover espaços em branco
       
# Acrescentar dados ao final

with open ("compras.txt", "a") as arquivo:
     arquivo.write("arroz")