numero = int(input("digite um número inteiro: "))

while numero > 0:
    print(numero)
    numero = int(input("digite outro número: "))
    if numero <= 0:
        print("fim")
        break
