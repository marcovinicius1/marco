qtdAlunos = int(input('Digite a quantidade de alunos:'))
cntIdade = 0
soma = 0

for i in range(qtdAlunos):
  idade = int(input(f'Digite a idade do aluno {i+1}: '))
  soma += idade
  if idade >= 16:
    cntIdade += 1


TtMedia = soma/qtdAlunos

print(f"Você tem {cntIdade} alunos APTOS a votar.")
print(f'A média de idade é {TtMedia} anos ')