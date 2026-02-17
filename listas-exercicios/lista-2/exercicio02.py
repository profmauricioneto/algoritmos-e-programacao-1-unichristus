import math

valor = float(input("Digite um valor: "))

if valor < 0:
    print("valor digitado é negativo")
else:
    print(f"Quadrado do valor: {valor ** 2}")
    print(f"Raiz quadrada do valor: {math.sqrt(valor)}")