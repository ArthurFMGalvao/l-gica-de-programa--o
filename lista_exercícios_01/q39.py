
valor = float(input("Digite um valor monetário: "))


notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]


quantidade_notas = {nota: 0 for nota in notas}
quantidade_moedas = {moeda: 0 for moeda in moedas}


for nota in notas:
    if valor >= nota:
        quantidade_notas[nota] = valor // nota
        valor %= nota


for moeda in moedas:
    if valor >= moeda:
        quantidade_moedas[moeda] = valor // moeda
        valor %= moeda

print("NOTAS:")
for nota, quantidade in quantidade_notas.items():
    print(f"{quantidade} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
for moeda, quantidade in quantidade_moedas.items():
    print(f"{quantidade} moeda(s) de R$ {moeda:.2f}")