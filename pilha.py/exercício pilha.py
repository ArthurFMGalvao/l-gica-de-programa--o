pilha = list(range(1, 6))
pratos = 6

while True:
    print('\nDigite E para empilhar um novo prato , D para desempilhar removendo um prato da pilha; ou s para sair.')
    opcao = input()
    if opcao == 'E':
        pilha.append(pratos)
        pratos += 1
        print(f'pilha atual: {pilha}, Tamanho: {len(pilha)}')
    elif opcao == 'D':
        if len(pilha) > 0:
            pilha.pop(0)
            print(f'pilha atual: {pilha}, Tamanho: {len(pilha)}')
        else:
            print('A pilha está vazia.')
    elif opcao == 's':
        break
    else:
        print('Opção inválida. Tente novamente.')