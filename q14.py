# Passagem por valor
def alterar_valor(num):
    # Aqui estamos modificando o valor de 'num'.
    # No entanto, essa mudança não afetará a variável original,
    # pois estamos passando o valor, não a referência.
    num = 100
    print(f"Valor dentro da função: {num}")

n = 10
alterar_valor(n)
print(f"Valor fora da função: {n}")




# Passagem por referência
def alterar_lista(lst):
    # Aqui estamos modificando a lista 'lst'.
    # Essa mudança afetará a lista original,
    # pois estamos passando a referência para a lista, não uma cópia dela.
    lst.append(100)
    print(f"Lista dentro da função: {lst}")

lista = [1, 2, 3]
alterar_lista(lista)
print(f"Lista fora da função: {lista}")