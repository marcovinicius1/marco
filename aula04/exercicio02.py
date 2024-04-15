turno_de_trabalho = input('Qual seu turno de trabalho (D/N):')
qtdHoras = float(input('Qual sua quantidade de horas trabalhada:'))

if turno_de_trabalho == 'N':
  noite = 45.00
  pagamento_totalnoite = qtdHoras * noite
  print(f'Você recebe por turno e hora trabalhada: {pagamento_totalnoite}')

elif turno_de_trabalho == 'D':
  dia = 37.50
  pagamento_totaldia = qtdHoras * dia
  print(f'Você recebe por turno e hora trabalhada: {pagamento_totaldia}')