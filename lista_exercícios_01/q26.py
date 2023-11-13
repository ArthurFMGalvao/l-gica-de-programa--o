#Escreva um programa que leia a matrícula de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre a matrícula e o salário do funcionário.

# Inicializando o programa
print("Bem-vindo ao programa de cálculo de salário")

# Lendo a matrícula do funcionário
matricula = input("Digite a matrícula do funcionário: ")

# Lendo o número de horas trabalhadas
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))

# Lendo o valor recebido por hora
valor_por_hora = float(input("Digite o valor que o funcionário recebe por hora: "))

# Calculando o salário
salario = horas_trabalhadas * valor_por_hora

# Mostrando a matrícula e o salário do funcionário
print("MATRICULA =", matricula)
print("SALARIO = R$", format(salario, ".2f"))