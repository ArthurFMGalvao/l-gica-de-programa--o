import math

# Solicita ao usuário o valor do lado de um quadrado
lado = float(input("Digite o valor do lado de um quadrado: "))

# Calcula o perímetro, área e diagonal
perimetro = 4 * lado
area = lado ** 2
diagonal = lado * math.sqrt(2)

print("O perímetro do quadrado é: ", perimetro)
print("A área do quadrado é: ", area)
print("A diagonal do quadrado é: ", diagonal)