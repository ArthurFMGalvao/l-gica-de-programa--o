def contem_item(lista, item):
    return item in lista

def combina_listas_sem_repeticao(lista1, lista2):
    lista3 = []
    for item in lista1:
        if not contem_item(lista3, item):
            lista3.append(item)
    for item in lista2:
        if not contem_item(lista3, item):
            lista3.append(item)
    return lista3

# Exemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
lista3 = combina_listas_sem_repeticao(lista1, lista2)
print(lista3)  # Saída: [1, 2, 3, 4, 5, 6, 7, 8]