idade_total = int(input("digite sua idade em segundos: "))


anos = idade_total// 365
meses = (idade_total % 365) // 30
dias = (idade_total % 365) % 30


print(f"{anos}:{meses}:{dias}")