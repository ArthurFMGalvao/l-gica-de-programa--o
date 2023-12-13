def verifica_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return 'Erro'
            pilha.pop()
    return 'OK' if not pilha else 'Erro'

# Solicitando ao usuário que insira a expressão de parênteses
expressao = input("Insira a expressão de parênteses: ")
print(verifica_parenteses(expressao))