n_aluno = int(input("Digite o número total de alunos na escola: "))

for i in range(n_aluno):
    sexo = input("Digite o sexo do aluno (M para masculino, F para feminino): ")
    altura = float(input("Digite a altura do aluno em metros: "))
    
    soma_altura_M = 0
    soma_altura_F = 0
    
    contador_M = 0 
    contador_F = 0 
    
    if sexo == 'M':
        soma_altura_M += altura
        contador_M += 1
    elif sexo == 'F':
        soma_altura_F += altura
        contador_F += 1
    else:
        print('Sexo inválido!')
        
    media_alturaM = soma_altura_M / contador_M
    media_alturaF = soma_altura_F / contador_F
    
print("Altura média das alunas:", media_alturaM)
print("Altura média dos alunos:", media_alturaF)