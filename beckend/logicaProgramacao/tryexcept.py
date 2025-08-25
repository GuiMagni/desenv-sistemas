#Quando você executa um código em Python, é bem comum encontrar erros: 
#seja ao tentar abrir um arquivo que não existe ou ao fazer uma conta 
#que não dá certo, como dividir um número por zero.
#Esses erros, chamados de exceções, podem interromper a execução do seu 
#programa e mostrar mensagens confusas para o usuário.
#O bloco try except serve justamente para isso: capturar essas exceções e permitir 
#que você trate os erros de forma personalizada, evitando que o programa pare de 
#funcionar ou que o usuário veja mensagens técnicas que ele não vai entender.


#ZeroDivisionError: Ocorre quando tentamos dividir um número por zero, o que é matematicamente indefinido.
#Exemplo: 10 / 0

#IndexError: Acontece quando tentamos acessar um índice que não existe em uma lista ou sequência.
#Exemplo: minha_lista[5] onde a lista tem apenas 3 elementos.

#ValueError: É gerado quando passamos um valor inadequado para uma função ou operação, como tentar converter uma string não numérica para int.
#Exemplo: int("abc")

#TypeError: Ocorre quando tentamos realizar uma operação ou função em um tipo de dado que não é compatível.
#Exemplo: "2" + 3 (tentando somar uma string com um número).

#FileNotFoundError: Acontece quando tentamos abrir um arquivo que não existe no caminho especificado.
#Exemplo: open("arquivo_inexistente.txt", "r")

#KeyError: Ocorre quando tentamos acessar uma chave que não existe em um dicionário.
#Exemplo: dicionario["idade"] quando a chave não existe no dicionário.

#AttributeError: É gerado quando tentamos acessar um atributo ou método que não existe em um objeto.
#Exemplo: objeto.metodo_inexistente()

#ImportError: Acontece quando tentamos importar um módulo ou função que não está disponível ou não existe.
#Exemplo: import modulo_inexistente

#NameError: Ocorre quando tentamos usar uma variável que não foi definida no escopo atual.
#Exemplo: print(x) quando x não foi definido previamente.

#TimeoutError: É gerado quando uma operação de rede ou outra operação demora mais tempo do que o esperado, excedendo o limite de tempo.
#Exemplo: Tentativa de conexão com um servidor que não responde a tempo.


def acessar_lista(lista, i):
    try:
        print(lista[i])
    except IndexError:
        print("Erro: Índice fora de alcance.")

minha_lista = [10, 20, 30]
acessar_lista(minha_lista, 2)  # 30
acessar_lista(minha_lista, 5)  # Erro



def dividir(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

dividir(10, 2)  # 5.0
dividir(10, 0)  # Erro





def converter_para_inteiro(valor):
    try:
        print(int(valor))
    except ValueError:
        print("Erro: O valor não pode ser convertido para inteiro.")

converter_para_inteiro("123")  # 123
converter_para_inteiro("abc")  # Erro

