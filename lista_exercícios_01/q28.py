nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o valor total de vendas efetuadas pelo vendedor no mês: "))

comissao = total_vendas * 0.15
total = salario_fixo + comissao

print("TOTAL = R$ {:.2f}".format(total))