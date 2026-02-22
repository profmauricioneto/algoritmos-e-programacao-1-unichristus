numero = int(input("Digite um número inteiro e positivo: "))

for i in range(1, numero + 1):
    if (numero % i == 0):
        print(i)