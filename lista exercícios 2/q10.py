import random

while True:
    # Geração de um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)

    # Inicialização do palpite
    palpite = 0

    while palpite != numero_secreto:
        # Leitura do palpite do usuário
        palpite = int(input("Digite o seu palpite: "))

        # Verificação do palpite
        if palpite > numero_secreto:
            print("Tente um número menor")
        elif palpite < numero_secreto:
            print("Tente um número maior")

    print(f"Parabéns!! Você acertou o {numero_secreto}")

    # Verificação se o usuário quer continuar jogando
    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() != 's':
        break