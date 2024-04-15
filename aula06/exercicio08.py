nome = input("Digite seu nome: ")
horas = int(input("Digite a hora atual (apenas horas): "))

if horas >= 5 and horas <= 12:
  mensagem = "Bom dia"
elif horas >= 13 and horas <= 18:
  mensagem = "Boa tarde"
else:
  mensagem = "Boa noite"

print(f"{mensagem}, {nome}!")