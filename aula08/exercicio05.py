n = int(input("Digite o número de termos da série de Fibonacci: "))

if n <= 0:
  print("O número de termos deve ser maior que zero.")
else:

  termo1 = 0
  termo2 = 1

  print("Série de Fibonacci:")
  print(termo1)
  print(termo2)

  for i in range(2, n):
    proximo_termo = termo1 + termo2
    print(proximo_termo)
    termo1 = termo2
    termo2 = proximo_termo
