senhacorreta = input ("senha correta")
senha = input ("Digite sua senha:")
nome = input ("Digite seu nome:")
salario = float(input("Digite seu salario:"))

while senha != senhacorreta:
    print("senha incorreta")
    input ("Digite a senha correta:")

print("Bem-Vindo", nome)
salarioanual = salario * 12

if (salarioanual > 100000):
    print ("rico")
else:
    print ("faz o l")
       