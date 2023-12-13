lista = list(range(1, 101))
print(lista)

numero_inicial = 50

comecar_imprimir = False

for numero in lista:
    if numero == numero_inicial:
        comecar_imprimir = True
    if comecar_imprimir and numero % 2 == 0:
        print(numero)

for i in range(100, -1, -1):
    print(i)
print("Fogo!")







num = int(input("Digite um número: "))

# Solicita ao usuário se ele quer ver números pares ou ímpares
tipo = input("Você quer ver números pares ou ímpares? ")

# Verifica a escolha do usuário e imprime os números correspondentes
if tipo.lower() == "pares":
    for i in range(2, num + 1, 2):
        print(i)
elif tipo.lower() == "ímpares":
    for i in range(1, num + 1, 2):
        print(i)
else:
    print("Escolha inválida. Por favor, digite 'pares' ou 'ímpares'.")