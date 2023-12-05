# Solicita ao usuário que insira o salário
salario = float(input("Insira o salário do funcionário: "))

# Calcula o aumento com base no salário
if salario > 1250.00:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

# Calcula o novo salário
novo_salario = salario + aumento

# Imprime o novo salário
print("O novo salário com aumento é: R$", novo_salario)