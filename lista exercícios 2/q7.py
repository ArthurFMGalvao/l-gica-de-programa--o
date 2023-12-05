# Leitura dos valores
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Verificação das condições
if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores não aceitos")