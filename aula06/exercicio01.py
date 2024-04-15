salario_fixo = float(input("Digite o salário fixo do funcionário: "))
valor_vendas = float(input("Digite o valor das vendas do funcionário: "))

comissao = valor_vendas * 0.04
salario_final = salario_fixo + comissao

print("A comissão do funcionário é: R$", comissao)
print("O salário final do funcionário é: R$", salario_final)