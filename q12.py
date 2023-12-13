def contagem_regressiva_recursiva(n):
    if n < 1:
        return
    else:
        print(n)
        contagem_regressiva_recursiva(n - 1)

# Solicita ao usuário para inserir um número
n = int(input("Por favor, insira um número inteiro para a contagem regressiva: "))

# Chama a função com o número fornecido pelo usuário
contagem_regressiva_recursiva(n)