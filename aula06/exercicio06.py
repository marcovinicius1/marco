nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0:
  conceito = "A"
elif media >= 7.5:
  conceito = "B"
elif media >= 6.0:
  conceito = "C"
elif media >= 4.0:
  conceito = "D"
else:
  conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
  print(f'APROVADO')
else:
  print(f'REPROVADO')

