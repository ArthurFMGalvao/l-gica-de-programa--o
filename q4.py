valor = (int(input("Digite um valor monetário: ")))


notas = [100, 50, 20, 10, 5, 2, 1]


quantidade_notas = {nota: 0 for nota in notas}


for nota in notas:
    if valor >= nota:
        quantidade_notas[nota] = valor // nota
        valor %= nota



print("NOTAS:")
for nota, quantidade in quantidade_notas.items():
    print(f"{quantidade} nota(s) de R$ {nota:.2f}")

