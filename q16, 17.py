def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!\n")
    return agenda

def buscar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    if nome in agenda:
        print(f"O número de telefone de {nome} é: {agenda[nome]}\n")
    else:
        print(f"Contato {nome} não encontrado na agenda.\n")

def main():
    agenda = {}
    while True:
        print("Agenda de Contatos:")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            agenda = adicionar_contato(agenda)
        elif opcao == '2':
            buscar_contato(agenda)
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()