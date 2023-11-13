# Entrada de dados
distancia = float(input("Digite a distância percorrida (em km): "))
combustivel = float(input("Digite o total de combustível gasto (em litros): "))

# Cálculo do consumo médio
consumo_medio = distancia / combustivel

# Saída de dados
print(f'{consumo_medio:.3f} km/l')