valorPrestacao = int(input('Digite o valor da prestãção: '))
multa = int(input('Digite a porcentagem da multa: '))
qtdeDias = int(input('Digite a quantidade de dias atrasados: '))

prestação = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)
print(prestação)