fila = list(range(1, 11))
ticket = 11

while True:
    print('\nDigite f para adicionar alguém à fila, a para atender uma pessoa, ou s para sair.')
    opcao = input()
    if opcao == 'f':
        fila.append(ticket)
        ticket += 1
        print(f'Fila atual: {fila}, Tamanho: {len(fila)}')
    elif opcao == 'a':
        if len(fila) > 0:
            fila.pop(0)
            print(f'Fila atual: {fila}, Tamanho: {len(fila)}')
        else:
            print('A fila está vazia.')
    elif opcao == 's':
        break
    else:
        print('Opção inválida. Tente novamente.')