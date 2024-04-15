idade = int(input('Digite a sua idade:'))
if idade < 16:
  print('Você não pode votar.')
elif idade > 18 and idade < 65:
  print('Você é obrigado a votar.')
elif idade >= 16 and idade <= 18 or idade > 65:
  print('Você é eleitor facultativo.')