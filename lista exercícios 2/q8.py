# Leitura dos valores
hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite o minuto inicial: "))
hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite o minuto final: "))

# Cálculo da duração do jogo
if hora_final < hora_inicial or (hora_final == hora_inicial and minuto_final <= minuto_inicial):
    hora_final += 24

duracao_minutos = (hora_final * 60 + minuto_final) - (hora_inicial * 60 + minuto_inicial)

duracao_horas = duracao_minutos // 60
duracao_minutos %= 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")