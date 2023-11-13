# Solicita ao usuário um valor inteiro
valor = int(input("Digite um valor inteiro: "))

# Define as notas possíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Inicializa um dicionário para armazenar a quantidade de cada nota
quantidade_notas = {nota: 0 for nota in notas}

# Calcula a quantidade de cada nota
for nota in notas:
    if valor >= nota:
        quantidade_notas[nota] = valor // nota
        valor %= nota

print("O valor pode ser decomposto em:")
for nota, quantidade in quantidade_notas.items():
    print(f"{quantidade} nota(s) de R$ {nota},00")