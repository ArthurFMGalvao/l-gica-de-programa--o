# Entrada de dados
tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))

# Cálculo da distância percorrida
distancia = tempo * velocidade

# Cálculo da quantidade de litros de combustível gastos
litros = distancia / 12

# Saída de dados
print(f'{litros:.3f}')