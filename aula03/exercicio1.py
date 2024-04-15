h = int(input('Qual a altura do tronco da piramide:'))
base_menor = float(input('Valor base menor:'))
base_maior = float(input('Valor base maior:'))

volume = h/3*(base_menor**2 + (base_maior**2 * base_menor**2)**0.5)
print(volume)