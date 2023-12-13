# Lista global para armazenar as tarefas
lista_de_tarefas = []

def adicionar_tarefa(tarefa):
    # Adiciona a tarefa à lista global
    lista_de_tarefas.append(tarefa)

def exibir_tarefas():
    # Imprime todas as tarefas
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(lista_de_tarefas, 1):
        print(f"{i}. {tarefa}")

adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer compras")
adicionar_tarefa("Preparar apresentação")

exibir_tarefas()