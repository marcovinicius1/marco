x = float(input("Digite a coordenada x do ponto P: "))
y = float(input("Digite a coordenada y do ponto P: "))

if x > 0 and y > 0:
  print("O ponto P pertence ao 1º quadrante.")
elif x < 0 and y > 0:
  print("O ponto P pertence ao 2º quadrante.")
elif x < 0 and y < 0:
  print("O ponto P pertence ao 3º quadrante.")
elif x > 0 and y < 0:
  print("O ponto P pertence ao 4º quadrante.")
else:
  print("O ponto P está sobre um dos eixos.")