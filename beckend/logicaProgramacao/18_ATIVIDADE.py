# Usando (lista,função,laços,try/except), voce devera criar uma lista com numeros e mensagens,
# Se for numero, adicionar a uma lista a parte. Se for mensagem, tratar com o erro de tipo. Ao
# final, mostrar a lista so com os numeros



def filtrar_numeros(lista_mista):
    numeros = []
    
    for item in lista_mista:
        try:
           
            resultado = item * 1
            numeros.append(item)
        except TypeError:
            print(f"Ignorando valor não numérico: '{item}'")
    
    return numeros

lista_original = [10, "Olá", 25, "Erro", 42, "Mensagem", -7, 3.14, "Fim"]

lista_numeros = filtrar_numeros(lista_original)

print("Lista com apenas números:", lista_numeros)

