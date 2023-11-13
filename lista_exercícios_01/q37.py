# Solicita ao usuário um valor inteiro (tempo em segundos)
segundos_total = int(input("Digite o tempo de duração em segundos: "))

# Calcula as horas, minutos e segundos
horas = segundos_total // 3600
minutos = (segundos_total % 3600) // 60
segundos = (segundos_total % 3600) % 60

print(f"{horas}:{minutos}:{segundos}")