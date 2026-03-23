while(True):
    opcao = int(input("Digite a opção [1 - somar, 2 - subtrair, 3 - multiplicar e 4 - dividir]: "))
    if (opcao >=1) and (opcao <= 4):
        break

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

resultado = 0
flag = False

if (opcao == 1):
    resultado = num1 + num2
elif (opcao == 2):
    resultado = num1 - num2
elif (opcao == 3):
    resultado = num1 * num2
elif (opcao == 4):
    if (num2 == 0):
        print("Não é possível divisão por zero!")
        flag = True
    else:
        resultado = num1/num2
else:
    print("Nenhuma opcao válida escolhida!")
    flag = True

if (flag):
    print("Fim do Programa")
else:
    print(f"O resultado da operação é: {resultado}")