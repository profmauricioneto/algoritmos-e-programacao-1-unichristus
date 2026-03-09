import math

message = """ 
Menu de opções
1 - Somar dois números
2 - Dividir dois números
3 - Raiz quadrada de um número
"""

print(message)
opcao = int(input("Digite a opcao desejada: "))
resultado = 0

if opcao == 1:
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    resultado = num1 + num2
elif opcao == 2:
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    if num2 == 0:
        print("Nao é possível divisao por zero!")
        exit()
    else:
        resultado = num1/num2
elif opcao == 3:
    num1 = float(input("Valor: "))
    if num1 < 0:
        print("Nao é possível calcular raiz de negativos!")
        exit()
    resultado = math.sqrt(num1)
else:
    print("Erro. Nenhuma opcao válida foi digitada.")
    exit()
    
print(f"Valor do Calculo: {resultado}")