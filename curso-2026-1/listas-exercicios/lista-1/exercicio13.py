# Um caixa eletrônico deve informar a quantidade mínima de cédulas para um saque. Considere que o caixa possui apenas cédulas de: R$ 100, R$ 50, R$ 20 e R$ 10
# Construa um algoritmo que:
# Leia o valor do saque (múltiplo de 10);
# Calcule e exiba a quantidade de cada cédula utilizada.

valor_saque = int(input("Qual o valor a ser sacado: "))

notas_100 = int(valor_saque / 100)
print(f"Notas 100: {notas_100}")
valor_saque = valor_saque % 100

notas_50 = int(valor_saque / 50)
print(f"Notas 50: {notas_50}")
valor_saque = valor_saque % 50

notas_20 = int(valor_saque / 20)
print(f"Notas 20: {notas_20}")
valor_saque = valor_saque % 20

notas_10 = int(valor_saque / 10)
print(f"Notas 10: {notas_10}")
valor_saque = valor_saque % 10

notas_1 = int(valor_saque / 1)
print(f"Notas 1: {notas_1}")
valor_saque = valor_saque % 1