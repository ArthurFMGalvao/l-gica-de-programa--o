def ordenacao_bolha(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                # Troca os elementos de lugar
                tmp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = tmp
    return lista

# Testando o algoritmo
print(ordenacao_bolha([7, 4, 3, 12, 8]))  # Saída: [3, 4, 7, 8, 12]