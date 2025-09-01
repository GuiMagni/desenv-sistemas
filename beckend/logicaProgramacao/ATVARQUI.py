# TRABALHANDO COM ARQUIVOS
# EXERCICIO
# CRIE UM ARQUIVO DE NOME alunos.TxT
# ADICIONE 5 ALUNOS NO ARQUIVO USE \n PARA QUEBRAR A LINHA
# CONFIRA ABRINDO O ARQUIVO SE ESCREVEU
# LEIA O ARQUIVO E FAÇA O PRINT DE CADA ALUNO NO TERMINAL

with open ("nome.txt","w") as arquivo:
    arquivo.write("Pablo \n")
    arquivo.write("Lucas \n")
    arquivo.write("Yuri \n")
    arquivo.write("Pedro \n")
    arquivo.write("Gsuilherme \n")
    
with open("alunos.txt", "r") as dados:

 for aluno in arquivo:
    print("aluno"aluno.strip())


