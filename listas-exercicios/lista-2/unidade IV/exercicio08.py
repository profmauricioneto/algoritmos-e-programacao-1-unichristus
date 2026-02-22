import math

valor_a = float(input("Digite o valor de A: "))
if (valor_a == 0):
    print("A equação não é do segundo grau!")
    exit()
valor_b = float(input("Digite o valor de B: "))
valor_c = float(input("Digite o valor de C: "))

# calculando o valor de delta
delta = (valor_b ** 2) - (4*valor_a*valor_c)

if (delta < 0):
    print("Não existe raizes reais")
elif (delta == 0):
    print("Existe uma raiz real")
    raiz = (-1*valor_b + math.sqrt(delta))/(2 * valor_a)
    print(f"Valor da Raiz: {raiz: .2f}")
else:
    print("Existem duas raizes reais distintas")
    raiz1 = (-1*valor_b + math.sqrt(delta))/(2 * valor_a)
    raiz2 = (-1*valor_b - math.sqrt(delta))/(2 * valor_a)
    print(f"Valores da raizes: {raiz1: .2f} e {raiz2: .2f}")
