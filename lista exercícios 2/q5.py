meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

valor = int(input("Digite um valor inteiro de 1 a 12: "))

if 1 <= valor <= 12:
    print(meses[valor])
else:
    print("Valor inválido. Por favor, digite um número entre 1 e 12.")