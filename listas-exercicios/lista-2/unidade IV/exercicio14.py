
print("Digite uma das opções: \n1 - somar\n2 - subtrair\n3 - multiplicar\n4 - dividir.")
opcao = int(input("Opção: "))

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
resultado = 0

if (opcao == 1):
    resultado = valor1 + valor2
elif (opcao == 2):
    resultado = valor1 - valor2
elif (opcao == 3):
    resultado = valor1 * valor2
elif (opcao == 4):
    if (valor2 == 0):
        print("Não é possível dividir por zero")
        exit()
    resultado = valor1 / valor2
else:
    print("Opção Inválida!")
    
print(f"O resultado do cálculo é {resultado: .2f}")