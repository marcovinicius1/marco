vLagua = int(input('Digite o valor da conta de água:'))
vLluz = int(input('Digite o valor da conta de luz:'))
vLtel = int(input('Digite o valor da conta de telefone:'))
vLsalario = int(input('Digite o valor do seu salário:'))

vLcontatotal = vLagua + vLluz + vLtel

if vLsalario > vLcontatotal:
  print(f'O valor total das contas é: {vLcontatotal} e sobrou {vLsalario - vLcontatotal} do salário.')
elif vLsalario < vLcontatotal:
  print(f'Salário insuficiente. Faltam {vLcontatotal - vLsalario} para pagar as contas.')