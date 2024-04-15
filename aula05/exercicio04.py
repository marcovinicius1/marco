numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(f'[1] Adição\n [2] Subtração\n [3] Multiplicação\n [4] Divisão')

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    print(f'A soma dos números é {numero + numero2}')
elif opcao == 2:
    print(f'A subtração dos números é {numero - numero2}') 
elif opcao == 3:
    print(f'A multiplicação dos números é {numero * numero2}')
elif opcao == 4:
    print(f'A divisão dos números é {numero / numero2}')