import math

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

if a == 0:
  print('Não é equação do segundo grau')
else:
  delta = b**2 - 4*a*c
  if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'As raízes são: {x1} e {x2}')
  elif delta == 0:
    x = -b / (2*a)
    print(f'A raiz é: {x}')
  else:
    print(f'Não há raízes reais')