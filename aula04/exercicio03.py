valorCompra = int(input('Digite o valor da compra:'))

if valorCompra > 200:
  valorDesconto = valorCompra * 0.2
  valorFinal = valorCompra - valorDesconto
  print(f'O valor da compra com desconto é: {valorFinal}')
else:
  print(f'O valor da compra é: {valorCompra}')