# Solicita ao usuário que insira a quantidade de kWh consumida
kWh = float(input("Insira a quantidade de kWh consumida: "))

# Solicita ao usuário que insira o tipo de instalação
tipo_instalacao = input("Insira o tipo de instalação (R para residências, I para indústrias, C para comércios): ")

# Define a tabela de preços
precos = {
    'R': { 'faixa1': 0.40, 'faixa2': 0.65 },
    'I': { 'faixa1': 0.55, 'faixa2': 0.60 },
    'C': { 'faixa1': 0.55, 'faixa2': 0.60 }
}

# Calcula o preço a pagar
if tipo_instalacao == 'R':
    if kWh <= 500:
        preco = kWh * precos['R']['faixa1']
    else:
        preco = kWh * precos['R']['faixa2']
elif tipo_instalacao == 'I':
    if kWh <= 5000:
        preco = kWh * precos['I']['faixa1']
    else:
        preco = kWh * precos['I']['faixa2']
elif tipo_instalacao == 'C':
    if kWh <= 1000:
        preco = kWh * precos['C']['faixa1']
    else:
        preco = kWh * precos['C']['faixa2']

# Imprime o preço a pagar
print("O preço a pagar é: R$", preco)