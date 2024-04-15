vLHAula = float(input(f'Digite o valor da hora aula:'))
cgHoraria = int(input('Digite a carga horaria: '))

sLbase = vLHAula * cgHoraria * 4.5
add = sLbase * 1/6
sLfinal = sLbase + add

print(f'Salário final: R${sLfinal:.2f}')