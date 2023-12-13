num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


resultado_multiplicacao = 0
for _ in range(abs(num2)):
    resultado_multiplicacao += num1
if num2 < 0:
    resultado_multiplicacao = -resultado_multiplicacao

print(f"O resultado da multiplicação é: {resultado_multiplicacao}")


resultado_divisao = 0
resto = abs(num1)
while resto >= abs(num2):
    resto -= abs(num2)
    resultado_divisao += 1
if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
    resultado_divisao = -resultado_divisao

print(f"O resultado da divisão é: {resultado_divisao}")
print(f"O resto da divisão é: {resto}")