import random


opcoes = ['pedra', 'papel', 'tesoura']

while True:
    
    opcao_computador = random.randint(0, 2)

    
    opcao_computador = opcoes[opcao_computador]

    
    opcao_jogador = input("Escolha uma opção (pedra, papel, tesoura): ")

    
    if (opcao_jogador == 'pedra' and opcao_computador == 'tesoura') or \
       (opcao_jogador == 'tesoura' and opcao_computador == 'papel') or \
       (opcao_jogador == 'papel' and opcao_computador == 'pedra'):
        print('Jogador venceu!')
    elif opcao_jogador == opcao_computador:
        print('Empate!')
    else:
        print('Computador venceu!')

    
    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() != 's':
        break