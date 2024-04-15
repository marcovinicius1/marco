import math

graus = float(input('Digite o valor do ângulo em graus: '))
graus_radiano = graus * (math.pi / 180)

""" SENO COSSENO TANGENTE """
radianos = graus_radiano
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"O seno do ângulo {graus}° é: {seno}")
print(f"O cosseno do ângulo {graus}° é: {cosseno}")
print(f"A tangente do ângulo {graus}° é: {tangente}")