# Solicita os números reais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibe as opções para o usuário
print("Escolha uma opção:")
print(f"[1] - Média entre os números digitados \n [2] - Diferença entre o maior e o menor número digitado \n [3] - Produto entre os números digitados \n [4] - Divisão do primeiro pelo segundo")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
  media = (num1 + num2) / 2
  print("A média entre os números digitados é:", media)
elif opcao == 2:
  diferenca = abs(num1 - num2)
  print("A diferença entre o maior e o menor número digitado é:", diferenca)
elif opcao == 3:
  produto = num1 * num2
  print("O produto entre os números digitados é:", produto)
elif opcao == 4:
  if num2 != 0:
    divisao = num1 / num2
    print("A divisão do primeiro pelo segundo número é:", divisao)
  else:
    print("Erro: O segundo número não pode ser zero.")
else:
  print("Erro: Opção inválida.")