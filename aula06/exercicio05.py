import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_tinta = math.ceil(area / 3)
latas_tinta = math.ceil(litros_tinta / 18)

preco_total = latas_tinta * 80

print("Quantidade de latas de tinta a serem compradas:", latas_tinta)
print("Preço total das latas de tinta: R$", preco_total)