contador = 0

while True:
  nuMb = input('Já dormiu? S/N: ')
  
  if nuMb == 'N':
    contador += 1
  elif nuMb == 'S':
    print('Você contou', contador, 'carneirinhos.')
    break
