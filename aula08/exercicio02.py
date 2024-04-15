quantidade_turmas = int(input("Digite a quantidade de turmas: "))

total_alunos = 0

for i in range(1, quantidade_turmas + 1):
  quantidade_alunos = int(input(f"Digite a quantidade de alunos da turma {i}: "))
  total_alunos += quantidade_alunos

media_alunos = total_alunos // quantidade_turmas

print(f"A média de alunos por turma é: {media_alunos}")