# Leia as notas das três matérias
materia1 = float(input("Digite a nota da primeira matéria: "))
materia2 = float(input("Digite a nota da segunda matéria: "))
materia3 = float(input("Digite a nota da terceira matéria: "))

# Leia o número total de faltas
faltas = int(input("Digite o número total de faltas: "))

# Calcule a média das notas
media = (materia1 + materia2 + materia3) / 3

# Calcule a frequência
frequencia = ((30 - faltas) / 30) * 100

# Determine se o aluno foi aprovado
aprovado = media > 7 and frequencia >= 75

print("Aluno aprovado?", aprovado)