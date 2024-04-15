n_valor = int(input("Quantos valores deseja inserir? "))
v_positivo = 0
v_negativo = 0
menor_valor = 0

for i in range(n_valor):
    valor = float(input("Digite o valor: "))
    
    if valor > 0:
        v_positivo += 1
    elif valor < 0:
        v_negativo += 1
    
    if menor_valor is 0 or valor < menor_valor:
        menor_valor = valor

print("Quantidade de valores positivos:", v_positivo)
print("Quantidade de valores negativos:", v_negativo)
print("Menor valor inserido:", menor_valor)