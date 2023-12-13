# Lista de temperaturas
T = [-10, -8, 0, 1, 2, 5, -2, -4]

# Calculando a menor, a maior e a temperatura média
menor_temperatura = min(T)
maior_temperatura = max(T)
temperatura_media = sum(T) / len(T)

# Imprimindo os resultados
print(f"A menor temperatura é: {menor_temperatura}°C")
print(f"A maior temperatura é: {maior_temperatura}°C")
print(f"A temperatura média é: {temperatura_media:.2f}°C")