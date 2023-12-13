# op = operação num = número

def tabuada(op, num):
    for i in range(1, 11):
        if op == 'adição':
            print(f'{num} + {i} = {num + i}')
        elif op == 'subtração':
            print(f'{num} - {i} = {num - i}')
        elif op == 'multiplicação':
            print(f'{num} * {i} = {num * i}')
        elif op == 'divisão':
            print(f'{num} / {i} = {num / i}')

def menu():
    while True:
        print("\nEscolha uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        opcao = input("Digite o número da operação desejada: ")

        if opcao == '5':
            print("Saindo do programa...")
            break

        num = int(input("Digite um número para a tabuada: "))

        if opcao == '1':
            tabuada('adição', num)
        elif opcao == '2':
            tabuada('subtração', num)
        elif opcao == '3':
            tabuada('multiplicação', num)
        elif opcao == '4':
            tabuada('divisão', num)
        else:
            print("Opção inválida. Tente novamente.")


menu()