num = int(input("Digite um numero positivo: "))
if (num > 0) and (num <= 10):
    for i in range(11):
        print(f"{num}*{i} = {num * i}")
else:
    print("O valor de entrada é inválido!")