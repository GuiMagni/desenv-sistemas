salario = float (input("Digite seu salário"))

if salario > 5000:
    impostoporcentual = 0.08
else:
    impostoporcentual = 00.5

imposto_mensal = salario * impostoporcentual
imposto_anual = imposto_mensal * 12
salario_anual = salario * 12

print("Imposto mensal ", imposto_mensal )
print("Imposto anual ", imposto_anual)
print("salario anual", salario_anual)