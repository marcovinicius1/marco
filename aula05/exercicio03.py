produto = input('Digite o nome do produto: ')
vLcompra = float(input('Digite o valor da compra: '))

if vLcompra < 10:
  vLvenda = vLcompra * 1.7
  print(f'O valor de venda do produto {produto} é R${vLvenda:.2f}.')
elif vLcompra >= 10 and vLcompra < 30:
  vLvenda = vLcompra * 1.5
  print(f'O valor de venda do produto {produto} é R${vLvenda:.2f}.')
elif vLcompra >= 30 and vLcompra < 50:
  vLvenda = vLcompra * 1.4
  print(f'O valor de venda do produto {produto} é R${vLvenda:.2f}.')
elif vLcompra >= 50:
  vLvenda = vLcompra * 1.3
  print(f'O valor de venda do produto {produto} é R${vLvenda:.2f}.')