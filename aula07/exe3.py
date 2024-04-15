n = int(input("Digite um numero positivo:"))

soma = 0 
for i in range(1, n + 1):
    soma += 1/i
print("A soma é:", soma)