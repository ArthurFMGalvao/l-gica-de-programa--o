# Defina os valores de A, B, C e D
valores = [
    (1, 2, True, False),
    (10, 3, False, True),
    (5, 1, True, True)
]

# Para cada conjunto de valores, calcule o resultado da expressão
for A, B, C, D in valores:
    resultado = A > B and C or not D
    print(f"Para A={A}, B={B}, C={C}, D={D}, o resultado da expressão é: {resultado}")